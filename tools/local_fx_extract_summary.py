"""keep: source-ID-only intermediate compression for the isolated FX shadow.

The model groups/selects IDs; Python copies the original typed facts verbatim.
Outputs and selection/QC history are evidence retained in the shadow run.
"""
from __future__ import annotations

import json

import local_fx_news as news

BUDGET = 3500  # UTF-8 bytes of retained typed facts; three children <=10.5KB.
CAP = 8
METHOD = "source-id-extractive-v1"


def size(facts):
    return len(json.dumps(facts, ensure_ascii=False).encode("utf-8"))


def assemble(raw, pool, leaf):
    """Validate IDs and copy originals, never accept generated summary prose."""
    if set(raw) != {"groups"} or not isinstance(raw["groups"], list):
        raise ValueError("only groups of original fact_ids are allowed; no prose")
    if not 1 <= len(raw["groups"]) <= 4:
        raise ValueError("group count must be 1..4")
    by_id = {x["fact_id"]: x for x in pool}
    selected = []
    units = []
    for group in raw["groups"]:
        if set(group) != {"fact_ids"} or not isinstance(group["fact_ids"], list) or not group["fact_ids"]:
            raise ValueError("each group needs original fact_ids only, nonempty")
        ids = group["fact_ids"]
        if any(not isinstance(ref, str) or ref not in by_id for ref in ids):
            raise ValueError("unknown original fact ID")
        if len(set(ids)) != len(ids) or set(ids) & set(selected):
            raise ValueError("duplicate original fact ID across groups")
        selected.extend(ids)
        # Metadata remains attached to each original clause even after merging.
        # Newline separation asserts no new causal relation between clauses.
        units.append({"text": "\n".join(
            f'[{by_id[ref].get("event_date") or by_id[ref].get("event_scope", "unknown")} / '
            f'{by_id[ref].get("record_type", "unknown")} / '
            f'{by_id[ref].get("market_session", "unspecified")}] {by_id[ref]["fact"]}'
            for ref in ids), "refs": list(ids)})
    if leaf and set(selected) != set(by_id):
        raise ValueError("leaf must visit and retain every input fact")
    if not leaf and len(selected) > CAP:
        raise ValueError("parent retained fact count exceeds budget")
    retained = [dict(by_id[ref]) for ref in selected]
    if size(retained) > BUDGET:
        raise ValueError("retained original facts exceed byte budget; do not truncate")
    return {"units": units, "retained_facts": retained,
            "omitted_fact_ids": [ref for ref in by_id if ref not in selected], "method": METHOD}


def summarize(api, out, label, pool, dates, leaf):
    if not pool or len({x["fact_id"] for x in pool}) != len(pool):
        raise ValueError("extractive summary requires nonempty unique original IDs")
    ids = [x["fact_id"] for x in pool]
    ref_array = {"type": "array", "items": {"type": "string", "enum": ids},
                 "minItems": 1, "maxItems": len(ids), "uniqueItems": True}
    schema = news.schema({"groups": {"type": "array", "minItems": 1, "maxItems": 4,
                                    "items": news.schema({"fact_ids": ref_array})}})
    task = ("原材料の選別・再配置だけを行う。説明文/要約文/独自分析は出力せず、IDのgroupsだけ返す。"
            "全入力を読んで関連する材料を最大4組に並べる。組内でも各factの日付/型/条件は別のまま。"
            "テーマは今回の入力から判断し固定しない。同じ出来事の背景・反応・反対材料を近くに配置する。"
            "各IDは全groupsで一度だけ使う。独自分析は最後の記事工程で行う。")
    if leaf:
        task += " 小分割の全IDを必ず残す。ここでは削除しない。"
    else:
        task += (f" 統合は最大{CAP}ID、保持factのJSON合計{BUDGET} UTF-8 bytes以内。"
                 "重複/枝葉を減らし、主要な相場変化に必要な背景/実際の反応/当日予定/反対材料を優先する。"
                 "過去の実績や将来の予想を本日実績に読み替えない。重要材料の欠落は別検査で不合格となる。")
    data = {"date_facts": dates, "facts": pool, "retained_byte_budget": BUDGET}
    raw = api.infer_cached(out, label, task, data, schema)
    value = None
    review = None
    for attempt in range(2):
        try:
            value = assemble(raw, pool, leaf)
        except (ValueError, TypeError, KeyError) as error:
            value = None
            review = {"verdict": "FAIL", "reason": str(error)}
        else:
            # No generated fact text exists here. QC assesses selection losses
            # and grouping, not whether an invented explanation is plausible.
            review = api.infer_cached(out, label + f"-review-{attempt}",
                "原材料とID選択を照合する。文章はプログラムが元factと日付/型をそのまま保持し新規文章はない。"
                "採用IDに背景/反応/当日予定/重要な反対材料が必要に応じ残っているか検査。"
                "重複/枝葉の圧縮は許容するが、独立した主要材料や成立条件の消失はFAIL。"
                "全指標・全通貨の機械的列挙は要求しない。groupsの配置は因果断定ではない。理由は具体的に。",
                {**data, "selected_groups": raw["groups"], "omitted_fact_ids": value["omitted_fact_ids"]},
                news.QC_SCHEMA)
        if review["verdict"] == "PASS":
            break
        if attempt == 0:
            raw = api.infer_cached(out, label + "-repair", task +
                " 指摘を守り元の全入力からID選択をやり直す。新しい文を作ることは禁止。",
                {**data, "review": review}, schema)
    news.save(out / "hierarchy" / f"{label}.json",
              {"inputs": pool, "selection": raw, "summary": value, "review": review, "method": METHOD})
    if review["verdict"] != "PASS":
        raise ValueError(f"{label}: extractive selection review failed: {review['reason']}")
    return value
