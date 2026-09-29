"""keep: bounded, freely worded summaries for non-publishing observation runs.

Artifacts are retained evidence. Content review is recorded, not used to force
the intermediate selection toward a daily answer. Writers return to originals.
"""
from __future__ import annotations

import json

import local_fx_news as news

BUDGET = 4500
METHOD = "free-summary-observation-v1"


def summarize(api, out, label, inputs, dates, leaf):
    key = "fact_id" if leaf else "node_id"
    ids = [x[key] for x in inputs]
    schema = news.schema({"units": {"type": "array", "minItems": 1, "maxItems": 4,
        "items": news.schema({"text": news.STRING, "refs": {
            "type": "array", "items": {"type": "string", "enum": ids},
            "minItems": 1, "maxItems": len(ids), "uniqueItems": True}})}})
    task = ("入力を読み、次の工程へ渡す相場の要約を作る。重要度・論点・まとめ方は資料から判断する。"
            "日付・数値・予想と実績の区別を保ち、入力にない事実は加えない。"
            "unitsのtextは自由な短い日本語、refsは対応する入力ID。"
            f"全unitsのJSON合計{BUDGET} UTF-8 bytes以内。")
    data = {"date_facts": dates, "inputs": inputs}
    value = api.infer_cached(out, label + "-observation", task, data, schema)
    for attempt in range(2):
        try:
            if not 1 <= len(value["units"]) <= 4:
                raise ValueError("invalid summary unit count")
            for unit in value["units"]:
                if (not isinstance(unit["text"], str) or not unit["text"].strip()
                        or not unit["refs"] or not set(unit["refs"]) <= set(ids)
                        or len(unit["refs"]) != len(set(unit["refs"]))):
                    raise ValueError("invalid summary text or source reference")
            if len(json.dumps(value["units"], ensure_ascii=False).encode()) > BUDGET:
                raise ValueError("summary exceeds stage byte budget; never truncate")
            break
        except (ValueError, KeyError, TypeError) as error:
            news.save(out / "hierarchy" / f"{label}-format-rejected-{attempt}.json",
                      {"value": value, "error": str(error), "lifecycle": "evidence"})
            if attempt:
                raise
            value = api.infer_cached(out, label + "-observation-format-repair",
                task + " JSON形式/参照/容量だけを直す。", {**data, "format_error": str(error)}, schema)
    review = api.infer_cached(out, label + "-observation-review-plan",
        "中間要約を入力と比較し、事実の不一致や重要な情報の落ちがあればFAILと具体的理由を記録。"
        "評価は観測用。特定の通貨/論点/相場観は正解として固定しない。",
        {**data, "summary": value}, news.QC_SCHEMA)
    news.save(out / "hierarchy" / f"{label}.json",
              {"inputs": inputs, "summary": value, "review": review,
               "method": METHOD, "review_is_advisory": True, "lifecycle": "evidence"})
    # No content repair, forced required-fact list, or automatic PASS conversion.
    return value
