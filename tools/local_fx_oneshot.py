"""experiment: one-shot FX daily authoring from already-extracted, dated facts.

Lifecycle: evidence trial (2026-09-30). Reads inputs of an existing shadow run
read-only and writes sections.json / report.html / checks.json into a NEW run dir
under shadow-output. No hierarchy, no per-section LLM gate; only deterministic
number/date and wording checks are recorded (never used to stop the run).
Never publishes; does not touch the cron or the production pipeline.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import time
import urllib.request
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import local_fx_daily as daily  # noqa: E402
import local_fx_external_review as external_review  # noqa: E402
import local_fx_grounding as grounding  # noqa: E402
import local_fx_news as news  # noqa: E402

S = news.STRING
TEMPERATURE = 0.3
SYSTEM = ("あなたは為替情報サイトAUXENの日報ライターです。渡された資料だけを根拠に、"
          "具体的な数値と因果関係で読ませる日本語の文章を書き、指定JSONだけを返す。資料にない事実・数値は書かない。")


COUNTRY = {"JPY": "日本", "USD": "米国", "EUR": "ユーロ圏", "GBP": "英国", "CHF": "スイス", "CAD": "カナダ",
           "AUD": "豪州", "NZD": "NZ", "CNY": "中国"}
BLANK = {"", "-", "—", "–", "--"}


def handover_text(events: list) -> str:
    """Today's key schedule built only from calendar fields (no model): time, name, forecast, previous.
    Rows with the same time/country but different numbers are all kept, never merged by guess."""
    def hhmm(e):
        h, m = e["time_jst"].split(":")
        return int(h) * 60 + int(m)

    def label(e):
        nums = [f"{k}{e[f]}" for k, f in (("予想", "forecast"), ("前回", "previous")) if str(e.get(f, "")).strip() not in BLANK]
        return f"{e['time_jst']} {COUNTRY.get(e['country'], e['country'])}{e['name'].strip()}" + (f"（{'／'.join(nums)}）" if nums else "")

    groups = [("アジア時間帯", 0, 15 * 60), ("欧州時間帯", 15 * 60, 21 * 60), ("NY時間帯", 21 * 60, 10 ** 6)]
    parts, seen = [], set()
    for name, lo, hi in groups:
        rows = []
        for e in sorted(events, key=hhmm):
            if lo <= hhmm(e) < hi and (e["time_jst"], e["country"], e["name"], e.get("forecast"), e.get("previous")) not in seen:
                seen.add((e["time_jst"], e["country"], e["name"], e.get("forecast"), e.get("previous")))
                rows.append(label(e))
        if rows:
            parts.append(f"{name}: " + "、".join(rows) + "。")
    return "本日の主要予定（日本時間、24時以降は翌日の時刻）。" + "".join(parts) if parts else "本日の主要予定は予定表にない。"


def ranking_sentence(ranking: dict, pair: str) -> str:
    """Rank, score and direction come from the ranking data with the day/time it was computed (never from the model)."""
    item = next(r for r in ranking["rankings"] if r["pair"] == pair)
    at = datetime.fromisoformat(ranking["generated_at_jst"]).astimezone(daily.JST)
    return (f"デイトレ適性ランキング（{at.month}月{at.day}日{at:%H:%M}時点の算出）で{item['rank']}位の{pair}"
            f"（スコア{item['score']}、{item['verdict']}、方向{item['direction']}、ADX {item['adx_h4']}）。")


def compact(facts):
    keep = []
    for x in facts:
        keep.append({"id": x["fact_id"], "fact": x["fact"], "quote": x.get("quote", ""),
                     "scope": x.get("event_scope"), "session": x.get("market_session"),
                     "type": x.get("record_type"), "pairs": x.get("pairs")})
    return keep


def passages(facts):
    """Distinct original article passages around the extracted facts (the extractor can drop
    sentences such as a bond-yield level that only survive here)."""
    seen, result = set(), []
    for x in facts:
        text = (x.get("source_context") or {}).get("quote_surroundings", "").strip()
        key = text[:40]
        if text and key not in seen:
            seen.add(key)
            result.append(text)
    return result


def call(out: Path, label: str, task: str, data: dict, schema: dict, num_predict: int = 12000) -> dict:
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": task + "\n資料:\n" + json.dumps(data, ensure_ascii=False)}]
    body = {"model": news.MODEL, "messages": messages, "format": schema, "stream": False, "think": True,
            "keep_alive": "10m", "options": {"num_ctx": 65536, "num_predict": num_predict, "temperature": TEMPERATURE}}
    news.save(out / "stages" / f"{label}.request.json", body)
    print(f"STAGE {label} RUNNING input_bytes={len(json.dumps(messages, ensure_ascii=False).encode())}", flush=True)
    started = time.monotonic()
    request = urllib.request.Request(news.OLLAMA + "/api/chat", data=json.dumps(body, ensure_ascii=False).encode(),
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=1500) as response:
        result = json.load(response)
    info = {"stage": label, "prompt_tokens": result.get("prompt_eval_count"), "output_tokens": result.get("eval_count"),
            "done_reason": result.get("done_reason"), "elapsed_seconds": round(time.monotonic() - started, 1)}
    news.save(out / "stages" / f"{label}.response.json", result)
    news.save(out / "stages" / f"{label}.metrics.json", info)
    print(json.dumps(info), flush=True)
    if result.get("model") != news.MODEL or result.get("done_reason") != "stop":
        raise ValueError(f"{label}: wrong model or incomplete response ({result.get('done_reason')})")
    value = json.loads(result["message"]["content"])
    if set(value) != set(schema["required"]):
        raise ValueError(f"{label}: fields differ from schema")
    return value


def generate(out: Path, target: date, material: list, calendar: dict, ranking: dict, policy: dict) -> dict:
    """Write sections.json/report.html/oneshot-checks.json into out (which must hold policy.json)."""
    started = datetime.now(daily.JST).isoformat()

    events = [{"no": n, "time": e["time_jst"], "country": e["country"], "name": e["name"].strip(),
               "importance": e["importance"], "forecast": e["forecast"], "previous": e["previous"]}
              for n, e in enumerate(calendar["events"], 1)]  # the feed marks most European releases "low"; never drop by importance
    pairs = [r["pair"] for r in ranking["rankings"][:5]]
    data = {"date_facts": grounding.date_facts(target),
            "facts": compact(material),
            "today_calendar": events,
            "original_passages": passages(material),
            "ranking_top5": [{k: r[k] for k in ["rank", "pair", "score", "verdict", "direction", "adx_h4", "adr_ratio_pct"]}
                             for r in ranking["rankings"][:5]],
            "policy_rates": [{"bank": r["bank"], "rate": r["rate"]} for r in policy["rates"]],
            "themes_today": calendar.get("day_themes", "")[:400]}
    news.save(out / "oneshot-input.json", data)

    style = ("文章の方針: 今日の相場を動かした最重要の材料（数値の大きな変化、利回り、要人発言など）を最初に見つけ、"
             "それを軸に書く。価格・利回り・予想値・前回値などの具体的な数値を入れる。材料同士の因果や対立を説明する。"
             "同じ材料を全欄で繰り返さず、欄ごとに役割の違う内容にする。'資料に基づく''記載の範囲内'のような"
             "資料への言及は書かない。予想は予想、実績は実績と区別する。"
             "現在は本日の午前7時で、本日の東京・ロンドン・NY市場はまだ始まっていない。前営業日の出来事は過去の出来事として書き、"
             "『本日のNY市場』のように未実施の市場を実施済みとして書かない。"
             "利回り・金利・為替レートは、資料にある具体的な水準（例: 利回りが何%まで上昇したか）を必ず書く。"
             "原因や理由は資料に書かれている範囲だけを書き、資料にない因果を自分で作らない。"
             "市場関係者の見方は『〜と指摘されている』のように出所を明示する。"
             "同じ指標や価格が日中に上下した場合は、高値・安値・その後の動きの前後関係が読み手に分かるように書き、時点の違う数値を並べて矛盾して見える書き方をしない。")
    plain = {k: v for k, v in data.items() if k != "ranking_top5"}  # only the focus call needs the ranking
    story = call(out, "oneshot-1-story", style +
                 "前営業日の相場を振り返る導入部分を書く。main_driverは今日の相場の最重要材料を1〜2文で。"
                 "heroは冒頭200字前後、headlineは60字以内の一言まとめ、summaryは前営業日の市場全体の整理350〜550字、"
                 "marketはドル・円・ユーロなどの地合いと相反する材料、判断条件300〜450字。",
                 plain, news.schema({"main_driver": S, "hero": S, "headline": S, "summary": S, "market": S}))
    topics = call(out, "oneshot-2-topics", style +
                  "前営業日(previous)の主要な出来事を4〜5件の話題にまとめる。各話題は何が起き、価格がどう動き、なぜ動いたかを"
                  "250〜450字で。main_driverに関わる話題を先頭にする。pointsは本日の注目点を具体的に3件(各1〜2文)。",
                  {**plain, "main_driver": story["main_driver"]},
                  news.schema({"topics": {"type": "array", "minItems": 4, "maxItems": 5,
                                          "items": news.schema({"title": S, "body": S})},
                               "points": {"type": "array", "minItems": 3, "maxItems": 3, "items": S}}))
    today = call(out, "oneshot-3-today", style +
                 "本日の見通しを書く。focus_pairはranking_top5から1ペア、focus_bodyは観察条件200〜300字"
                 "（順位・スコア・ランキングの数値は別に機械的に付くので書かない）。risk_levelとrisk_bodyは本日最大のリスクと条件200〜300字。"
                 "key_event_nosは、本日の相場を動かす主要予定のtoday_calendarのno(整数)を8〜12件。"
                 "各国の政策・景況・物価・雇用の主要指標と、中央銀行総裁・要人発言を優先し、同じ指標の副項目や小さな指標は含めない。"
                 "本文で取り上げる通貨ペア(例: ユーロドル、ドル円)に関わる予定を必ず含める。",
                 {**data, "main_driver": story["main_driver"]},
                 news.schema({"focus_pair": {"type": "string", "enum": pairs}, "focus_body": S,
                              "risk_level": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]}, "risk_body": S,
                              "key_event_nos": {"type": "array", "minItems": 8, "maxItems": 12, "items": {"type": "integer"}}}))

    # The feed's own importance grades are the only filter for "key events"; with a single source (Forex Factory
    # refused) they miss e.g. the Tankan and ISM, so use the model's selection (indices only) when it is valid.
    picked = sorted({n for n in today.get("key_event_nos", []) if 1 <= n <= len(calendar["events"])})
    chosen = [calendar["events"][n - 1] for n in picked] or calendar["key_events"]  # calendar order is already by time

    sections = {"topics": topics["topics"], "hero": story["hero"], "headline": story["headline"],
                "summary": story["summary"], "market": story["market"], "handover": handover_text(chosen),
                "focus_pair": today["focus_pair"],
                "focus_body": ranking_sentence(ranking, today["focus_pair"]) + today["focus_body"],
                "risk_level": today["risk_level"], "risk_body": today["risk_body"],
                "points": [{"title": f"焦点{i+1}", "body": p} for i, p in enumerate(topics["points"])]}
    news.save(out / "sections.json", sections)

    evidence = [{"quote": x.get("quote", ""), "fact": x.get("fact", ""), "source_context": x.get("source_context", {}),
                 "published_at": x.get("published_at", "")} for x in material]
    evidence += [{"quote": json.dumps(e, ensure_ascii=False), "fact": "", "source_context": {}, "published_at": ""}
                 for e in events]
    evidence += [{"quote": json.dumps(x, ensure_ascii=False), "fact": "", "source_context": {}, "published_at": ""}
                 for x in data["ranking_top5"] + data["policy_rates"]]
    keys = (["hero", "headline", "summary", "market", "handover", "focus", "risk"]
            + [f"topic{i}" for i in range(len(sections["topics"]))] + [f"point{i}" for i in range(len(sections["points"]))])

    def texts_of(sec):
        return {"hero": sec["hero"], "headline": sec["headline"], "summary": sec["summary"], "market": sec["market"],
                "handover": sec["handover"], "focus": sec["focus_body"], "risk": sec["risk_body"],
                **{f"topic{i}": t["body"] for i, t in enumerate(sec["topics"])},
                **{f"point{i}": p["body"] for i, p in enumerate(sec["points"])}}

    def mechanical(texts):
        return {"number_date_errors": {k: e for k, v in texts.items() if (e := grounding.number_errors(v, evidence, target))},
                "internal_wording": [k for k, v in texts.items() if re.search(daily.FORBIDDEN, v, re.I)],
                "meta_wording": [k for k, v in texts.items() if re.search(r"資料に基づ|記載の範囲|資料に記載|資料にない", v)]}

    verify_data = {"date_facts": data["date_facts"], "facts": data["facts"], "today_calendar": events,
                   "original_passages": data["original_passages"]}
    issue_schema = news.schema({"issues": {"type": "array", "items": news.schema({
        "sections": {"type": "array", "items": {"type": "string", "enum": keys}},
        "excerpt": S, "kind": {"type": "string", "enum": ["時制", "資料外の因果", "数値", "資料外の出来事", "予想と実績", "その他"]},
        "reason": S})}})
    verify_task = ("以下の日報本文を資料(facts/original_passages/today_calendar)と照合し、問題のある記述だけを挙げる。"
                   "問題の種類: 時制(未実施の市場を実施済みとして書く等)、資料外の因果(資料に書かれていない原因・理由の断定)、"
                   "数値(資料と異なる、または資料にない具体的な水準)、資料外の出来事(資料にない発言者・制度・イベント)、予想と実績の混同。"
                   "上振れ・下振れなら相場がどう動くかという条件付きの見通しは分析であり、資料に書かれていなくても問題としない。"
                   "ただし資料にない具体的な数値水準や出来事を持ち込んでいれば問題とする。問題がなければ空の配列。文体や好みは指摘しない。")
    texts = texts_of(sections)
    checks = {**mechanical(texts), "chars": {k: len(v) for k, v in texts.items()}, "started_at": started,
              "publish_ready": False}
    try:  # the semantic check is advisory: a cut-off or failed check must not lose the written report
        review = call(out, "oneshot-4-verify", verify_task, {**verify_data, "draft": texts}, issue_schema, 30000)
    except Exception as error:
        review = {"issues": []}
        checks["semantic_check_error"] = f"{type(error).__name__}: {error}"
    checks["semantic_issues"] = review["issues"]
    checks["before_repair"] = {"texts": texts}
    # Second opinion from a different model (Codex Luna); its findings join the repair list below.
    # Failure or disabled just means no extra findings (see local_fx_external_review.py).
    checks["external_review_before"] = external_review.review(out, verify_data, texts)
    external_issues = external_review.usable_issues(checks["external_review_before"], keys)

    flagged = {k for i in review["issues"] + external_issues for k in i["sections"]} | set(checks["number_date_errors"]) |         set(checks["internal_wording"]) | set(checks["meta_wording"])
    if flagged:
        problems = [{"sections": i["sections"], "excerpt": i["excerpt"], "reason": i["reason"]}
                    for i in review["issues"] + external_issues]
        problems += [{"sections": [k], "reason": "本文の数値が資料にない: " + ", ".join(v)}
                     for k, v in checks["number_date_errors"].items()]
        try:  # a failed or cut-off repair must not lose the written report (same rule as the verify step)
            fixed = call(out, "oneshot-5-repair",
                         "指摘された記述だけを直す。資料にない数値水準・出来事・原因は削除するか、資料にある事実の表現に置き換える。"
                         "条件付きの見通し(上振れ・下振れ)は、資料にある数値だけを使って残してよい。指摘のない部分は変えない。"
                         "fixesには修正が必要なsectionだけを、修正後の全文で返す。",
                         {**verify_data, "problems": problems, "current": {k: texts[k] for k in sorted(flagged)}},
                         news.schema({"fixes": {"type": "array", "items": news.schema({
                             "section": {"type": "string", "enum": sorted(flagged)}, "text": S})}}), 30000)  # thinking alone used 12000 tokens on 2026-10-06
            for fix in fixed["fixes"]:
                k, text = fix["section"], fix["text"]
                if k.startswith("topic"):
                    sections["topics"][int(k[5:])]["body"] = text
                elif k.startswith("point"):
                    sections["points"][int(k[5:])]["body"] = text
                else:
                    sections[{"focus": "focus_body", "risk": "risk_body"}.get(k, k)] = text
            checks["repaired_sections"] = [f["section"] for f in fixed["fixes"]]
        except Exception as error:
            checks["repair_error"] = f"{type(error).__name__}: {error}"
    news.save(out / "sections.json", sections)
    texts_after = texts_of(sections)
    checks["after_repair"] = {**mechanical(texts_after), "chars": {k: len(v) for k, v in texts_after.items()}}
    # Re-check the repaired text with the same reviewer; recorded only, no further rewrite.
    checks["external_review_after"] = (external_review.review(out, verify_data, texts_after)
                                       if checks.get("repaired_sections") else {"status": "skipped", "reason": "nothing repaired"})
    checks["finished_at"] = datetime.now(daily.JST).isoformat()
    news.save(out / "oneshot-checks.json", checks)
    shown = {**calendar, "key_events": chosen}
    daily.render(target, sections, shown, ranking, out, allow_single_source=True)
    print(json.dumps({"run_dir": str(out), "status": "ONESHOT_COMPLETE_REVIEW_PENDING",
                      "semantic_issues": len(checks["semantic_issues"]), "repaired": checks.get("repaired_sections", []),
                      "after_repair": {k: v for k, v in checks["after_repair"].items() if k != "chars"}},
                     ensure_ascii=False), flush=True)
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--date", type=date.fromisoformat, required=True)
    args = parser.parse_args()
    root = daily.ROOT / "shadow-output"
    src, out = args.source_run.resolve(), args.run_dir.resolve()
    if not out.is_relative_to(root.resolve()) or not src.is_relative_to(root.resolve()):
        raise ValueError("runs must be under shadow-output")
    out.mkdir(parents=True, exist_ok=True)
    target = args.date
    for name in ["shared-material.json", "calendar.json", "market.json", "policy.json"]:
        shutil.copyfile(src / name, out / name)
    material = json.loads((out / "shared-material.json").read_text(encoding="utf-8"))["facts"]
    calendar = json.loads((out / "calendar.json").read_text(encoding="utf-8"))
    market = json.loads((out / "market.json").read_text(encoding="utf-8"))
    policy = json.loads((out / "policy.json").read_text(encoding="utf-8"))
    ranking = market["ranking"]
    generate(out, target, material, calendar, ranking, policy)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
