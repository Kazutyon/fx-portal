"""experiment: one-shot FX daily authoring from already-extracted, dated facts.

Lifecycle: evidence trial (2026-09-30). Reads inputs of an existing shadow run
read-only and writes sections.json / report.html / checks.json into a NEW run dir
under shadow-output. No hierarchy, no per-section LLM gate; only deterministic
number/date and wording checks are recorded (never used to stop the run).
Never publishes; does not touch the cron or the production pipeline.
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import shutil
import sys
import time
import urllib.request
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import local_fx_daily as daily  # noqa: E402
import local_fx_claim_check as claim_check  # noqa: E402
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


def event_label(e: dict) -> str:
    nums = [f"{k}{e[f]}" for k, f in (("予想", "forecast"), ("前回", "previous")) if str(e.get(f, "")).strip() not in BLANK]
    return f"{e['time_jst']} {COUNTRY.get(e['country'], e['country'])}{e['name'].strip()}" + (f"（{'／'.join(nums)}）" if nums else "")


def sentence(x: dict) -> str:
    """One sourced sentence from an extracted fact: the fact text as extracted (who said it is already in it) plus its article."""
    text = x["fact"].strip()
    if text.startswith("・"):
        return "今日の注目点: " + text.lstrip("・ ").strip().rstrip("。") + "。"
    title = (x.get("source_title") or "").strip()
    return text + (f"（出典: {title}）" if title else "")


PREFIX = re.compile(r"^(\d{4}年\d{1,2}月\d{1,2}日[^、。]{0,20}?、)")


def join_facts(facts: list) -> str:
    """Fact sentences in the order given. The date/market lead-in is kept on the first sentence and dropped from later
    ones only when it is identical, so the reader still sees which day and market every statement is about."""
    def same_lead_in(prefix: str) -> str:  # NY / ニューヨーク and 外為 / 外国為替 are spellings of one market; 欧州 etc. stay different
        return re.sub(r"外国為替|外為|為替", "", prefix.replace("ニューヨーク", "NY"))

    seen, parts, stated = set(), [], []
    for x in facts:
        text = x["fact"].strip()
        nums = figures(text)
        if nums and any(nums <= earlier for earlier in stated):
            continue  # another article restating the same figures: say it once
        stated.append(nums)
        m = PREFIX.match(text)
        if m and same_lead_in(m.group(1)) in seen:
            text = text[m.end():]
        elif m:
            seen.add(same_lead_in(m.group(1)))
        parts.append(text if text.endswith("。") else text + "。")
    return "".join(parts)


def join_sourced(facts: list) -> str:
    """Sourced sentences in order; a run of sentences from the same article names the article once, after the run."""
    out = []
    for n, x in enumerate(facts):
        text = x["fact"].strip()
        if text.startswith("・"):
            out.append(sentence(x))
            continue
        title = (x.get("source_title") or "").strip()
        last_of_run = n + 1 == len(facts) or (facts[n + 1].get("source_title") or "").strip() != title
        out.append(text + (f"（出典: {title}）" if title and last_of_run else ""))
    return " ".join(out)


def is_view(x: dict) -> bool:
    """A market participant's view from a news article. Calendar (C*), weekly schedule (W*) and ranking (R*) facts
    are also typed forecast/outlook but are not views, so only the news facts (N*) qualify."""
    return (x.get("fact_id", "").startswith("N") and x.get("record_type") in ("outlook", "forecast")
            and bool(x.get("fact")) and not x["fact"].lstrip().startswith("・"))


def figures(text: str) -> set:
    """The figures a sentence states (not the date in its lead-in), as numbers so that 1.00 and 1 are the same."""
    return {float(n) for n in re.findall(r"\d+(?:\.\d+)?", PREFIX.sub("", text))}


def restates(text: str, others: list) -> bool:
    """True when an already-chosen sentence says the same thing: nearly the same wording, or the same figures
    (one set contains the other) with some wording in common. Two articles often carry one view in different words."""
    mine = figures(text)
    for other in others:
        ratio = difflib.SequenceMatcher(None, text, other).ratio()
        theirs = figures(other)
        if ratio >= 0.6 or (mine and theirs and (mine <= theirs or theirs <= mine) and ratio >= 0.25):
            return True
    return False


def feature(env_name: str, key: str) -> bool:
    """Experiment switches: an environment variable, or {"<key>": {"enabled": true}} in claude_mirror_shadow.json
    (the file already holds the external-review switch, so the morning cron needs no change)."""
    if os.environ.get(env_name):
        return True
    try:
        value = json.loads(external_review.CONFIG.read_text(encoding="utf-8")).get(key, {})
    except (OSError, ValueError):
        return False
    return isinstance(value, dict) and bool(value.get("enabled"))


HOLIDAY_COUNTRY = {"日本": "JPY", "米国": "USD", "アメリカ": "USD", "英国": "GBP", "イギリス": "GBP", "カナダ": "CAD", "豪": "AUD",
                   "オーストラリア": "AUD", "ニュージーランド": "NZD", "スイス": "CHF", "欧州": "EUR", "ユーロ": "EUR", "ドイツ": "EUR",
                   "フランス": "EUR", "中国": "CNY"}


# an ASCII snake_case name inside reader text is an internal leak; \b does not work next to Japanese characters
CODE_LIKE = r"(?<![A-Za-z0-9_])[a-z]+(?:_[a-z]+)+(?![A-Za-z0-9_])"


def holiday_line(calendar: dict) -> str:
    """Market holidays for the day from the fetched schedule (never from the model).

    'No holiday' is stated only when the holiday list was actually read and had none; a country that is on holiday
    but still has releases on the schedule is flagged for checking (the sources disagree)."""
    text = (calendar.get("holiday_text") or "").strip()
    if text:
        line = f"休場: {text}（KissFXの記載）"
        clash = []
        for name, code in HOLIDAY_COUNTRY.items():
            if name in text and any(e.get("country") == code for e in calendar.get("events", [])):
                clash.append(name)
        if clash:
            line += "。" + "・".join(clash) + "は予定表に同日の指標があり、休場かどうかは要確認"
        return line
    if calendar.get("holiday_checked") or any("kissfx" in u for u in calendar.get("source_urls", [])):
        return "休場なし（KissFXの記載に休場・祝日なし）"
    return "休場の情報は取得できなかった"


def calendar_notes(calendar: dict, key_events: list) -> str:
    """Cross-check note for the schedule: only what was actually compared (events the two sources could be matched on)."""
    events = calendar.get("events", [])
    matched = sum(1 for e in events if e.get("confirmed"))
    shown = {(e.get("time_jst"), (e.get("name") or "").strip()) for e in key_events}
    conflicts = [c for c in calendar.get("conflicts", []) if (c.get("time_jst"), (c.get("name") or "").strip()) in shown]
    text = f"KissFXとForexFactoryで突き合わせできた指標は{matched}件（それ以外は片方の情報のみ）。"
    if conflicts:
        parts = [f"{c['time_jst']} {c['name']}の{'予想' if c.get('field') == 'forecast' else '前回'}はKiss {c.get('kissfx')}／FF {c.get('forexfactory')}"
                 for c in conflicts[:4]]
        text += "表示した主要指標で値が一致しないもの: " + "、".join(parts) + "（要確認）。"
    return text


def closing_ids(material: list) -> dict:
    """pair -> fact_id of the one fact that states that pair's close ("終値は…"): the first in material order."""
    closes = {}
    for x in material:
        pairs = x.get("pairs") or []
        if x.get("fact_id", "").startswith("N") and len(pairs) == 1 and "終値" in x.get("fact", ""):
            closes.setdefault(pairs[0], x["fact_id"])
    return closes


def conflicts_with_close(x: dict, closes: dict) -> bool:
    """A previous-day 'X から Y まで…' range fact for a pair whose close is stated elsewhere: its wording ('…まで上昇し、
    引けた') reads as a second, different close, so only the explicit close is kept."""
    pairs = x.get("pairs") or []
    return (x.get("kind") == "price" and x.get("event_scope", "previous") == "previous" and len(pairs) == 1
            and pairs[0] in closes and x.get("fact_id") != closes[pairs[0]]
            and re.search(r"から[0-9０-９].*まで", x.get("fact", "")) is not None)


def no_market_view_text(titles: str) -> str:
    return f"前営業日の主な話題: {titles}。" if titles else ""


def risk_fallback(events: list) -> str:
    """Risk text when no market participant's view was chosen: the day's high-importance releases, from the calendar."""
    high = [e for e in events if e.get("importance") == "high"]
    if not high:
        return "本日、重要度の高い予定は予定表にない。"
    return "本日の高重要度予定: " + "、".join(event_label(e) for e in high[:6]) + "。"


def is_theme(x: dict) -> bool:
    return bool(x.get("fact")) and x["fact"].lstrip().startswith("・")


def handover_text(events: list) -> str:
    """Today's key schedule built only from calendar fields (no model): time, name, forecast, previous.
    Rows with the same time/country but different numbers are all kept, never merged by guess."""
    def hhmm(e):
        h, m = e["time_jst"].split(":")
        return int(h) * 60 + int(m)

    groups = [("アジア時間帯", 0, 15 * 60), ("欧州時間帯", 15 * 60, 21 * 60), ("NY時間帯", 21 * 60, 10 ** 6)]
    parts, seen = [], set()
    for name, lo, hi in groups:
        rows = []
        for e in sorted(events, key=hhmm):
            if lo <= hhmm(e) < hi and (e["time_jst"], e["country"], e["name"], e.get("forecast"), e.get("previous")) not in seen:
                seen.add((e["time_jst"], e["country"], e["name"], e.get("forecast"), e.get("previous")))
                rows.append(event_label(e))
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


SITE = {"zai.diamond.jp": "ザイFX", "fx.minkabu.jp": "みんかぶ", "www.gaitame.com": "外為どっとコム", "gaitame.com": "外為どっとコム",
        "kissfx.com": "KissFX", "www.investing.com": "Investing.com", "jp.investing.com": "Investing.com"}


def site_of(x: dict) -> str:
    host = re.sub(r"^https?://([^/]+).*$", r"", x.get("source_url") or "")
    return SITE.get(host, host)


def price_moves(material: list, limit_pairs: int = 4, per_pair: int = 4) -> list:
    """The previous day's close and range per pair, so the writer can state the day's net result in one line."""
    closes = closing_ids(material)
    by_id = {x["fact_id"]: x for x in material}
    moves = []
    for pair, close_id in list(closes.items())[:limit_pairs]:
        ids = [close_id] + [x["fact_id"] for x in material
                            if x["fact_id"] != close_id and x.get("event_scope") == "previous" and x.get("pairs") == [pair]
                            and re.search(r"高値|安値|一時|まで", x.get("fact", ""))]
        moves.append({"通貨ペア": pair, "値動き": [{"fact": by_id[i]["fact"], "source": site_of(by_id[i])}
                                                   for i in ids[:per_pair]]})
    return moves


def other_previous_facts(material: list, shown: set, limit: int = 30) -> list:
    """Previous-day facts the topic selection did not pick (stocks, oil, gold, positioning...) as background for the writer."""
    return [{"fact": x["fact"], "source": site_of(x)} for x in material
            if x.get("fact_id", "").startswith("N") and x.get("event_scope") == "previous" and x.get("kind") != "outlook"
            and x["fact_id"] not in shown][:limit]


def write_prose(out: Path, style: str, sections: dict, hero_facts: list, summary_facts: list, market_views: list,
                risk_views: list, topic_facts: list, key_events: list, date_facts: dict, high_events: list,
                material: list | None = None, weekly: str = "") -> None:
    """Experiment (FX_WRITE_BODIES=1): the model writes hero/summary/topic bodies/market/risk as prose from the chosen
    facts, the way the Claude morning run does. Numbers are still checked mechanically against the evidence afterwards."""
    def facts_of(items):
        return [{"id": x["fact_id"], "fact": x["fact"], "quote": x.get("quote", ""), "source": site_of(x)} for x in items]

    data = {"日付": date_facts, "最重要の材料": facts_of(hero_facts), "前営業日の市場全体の材料": facts_of(summary_facts),
            "話題ごとの材料": [{"見出し": t["title"], "材料": facts_of(f)} for t, f in zip(sections["topics"], topic_facts)],
            "地合いに関する見解": facts_of(market_views), "リスクに関する見解": facts_of(risk_views),
            "本日の主な予定": [event_label(e) for e in key_events],
            "本日の高重要度の予定": [{"時刻": e["time"], "国": e["country"], "名称": e["name"],
                                      "予想": e["forecast"], "前回": e["previous"]} for e in high_events]}
    if material:
        data["前営業日の値動き"] = price_moves(material)
        shown = {x["fact_id"] for x in hero_facts + summary_facts + market_views + risk_views}
        shown.update(x["fact_id"] for facts in topic_facts for x in facts)
        data["前営業日のその他の材料"] = other_previous_facts(material, shown)
    if weekly:
        data["今週の予定"] = weekly[:1200]
    task = ("あなたはFXトレード日報の筆者。読者は4時間足でトレンドを把握し、15分・30分足の波とローソク足でエントリーするFXトレーダー。"
            "渡した材料(factとquote)を材料に、読ませる文章を書く。事実の羅列や原文の貼り合わせにせず、何が起き、なぜ動いたか(資料に書かれた背景・理由)、"
            "本日への引継ぎ(注目する水準や、上振れ・下振れならどう動くかという条件付きの見通し)を、自分の言葉で整理して書く。"
            "heroは前営業日の最重要の材料を2文。summaryは前営業日の市場全体の整理を3〜4文。各話題の本文は『話題ごとの材料』と同じ順で、各話題を2〜4文。"
            "handoffは『本日(日付と曜日)への引継ぎ』の段落(3〜4文): 前営業日の終値、本日最大の材料とその時刻、日中の主な予定、"
            "資料にある水準を目安にした条件付きの見通し(上回れば〜、下回れば〜)。"
            "marketは本日の地合いを2〜3文(『地合いに関する見解』を材料に)。riskは本日から今週の最大のリスクを2文"
            "(『リスクに関する見解』と『本日の高重要度の予定』を材料に。予想値・前回値があれば使ってよい。"
            "材料が乏しい日は、『本日の主な予定』から相場を動かしうるものを選んで書く)。"
            "『前営業日の値動き』は主要通貨ペアの終値と高値・安値。『前営業日のその他の材料』は株価・原油・金・ポジションなど相場の背景。『今週の予定』は週の中央銀行会合や決算。heroとsummaryは、前営業日の相場の結論(終値と、何が相場を動かしたか)を、これらも見て言い切る。summaryは数値の羅列にせず、終値→動かした材料→本日への含み、の順で結論として書く。riskの2文目とhandoffの最後の1文は、『今週の予定』にある中央銀行会合や決算に向けた含み(本日の動きとのつながり)を書く。『今週の予定』がなければ書かない。"
            "数値・日付・要人名・出来事は、渡した資料にあるものだけを使い、資料にない水準・数値は作らない。"
            "出典を示すときは（ザイFX）のようにsourceの名前を括弧で添える。"
            "現在は本日の午前7時で、本日の東京・ロンドン・NY市場はまだ始まっていない。前営業日の出来事は過去のこととして書く。"
            "「様子見」「注目したい」「〜の可能性がある」「〜かもしれない」は使わない。")
    n = len(sections["topics"])
    result = call(out, "oneshot-2b-write", task, data,
                  news.schema({"hero": S, "summary": S,
                               "topic_bodies": {"type": "array", "minItems": n, "maxItems": n, "items": S},
                               "market": S, "risk": S, "handoff": S}), 16000)
    sections["handoff"] = result["handoff"].strip()
    sections["hero"], sections["summary"] = result["hero"].strip(), result["summary"].strip()
    sections["market"], sections["risk_body"] = result["market"].strip(), result["risk"].strip()
    for t, body in zip(sections["topics"], result["topic_bodies"]):
        t["body"] = body.strip()


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
    by_id = {x["fact_id"]: x for x in material}
    view_ids = [x["fact_id"] for x in material if is_view(x)]
    theme_ids = [x["fact_id"] for x in material if is_theme(x)]
    event_ids = [x["fact_id"] for x in material if x["fact_id"].startswith("N") and not is_view(x) and not is_theme(x)]
    topics = call(out, "oneshot-2-topics", style +
                  "前営業日の相場の振り返りを組み立てるが、文章は書かず、資料のfactをidで選ぶだけにする。"
                  "heroは冒頭に置く今日の相場の最重要材料のfactのid(1〜2件)。"
                  "topicsは前営業日の主要な出来事の4〜5話題。各話題のfact_idsは、同じ出来事・同じ材料を扱うfactのid(2〜5件、時系列順)、"
                  "titleは話題の見出し(30字以内。資料にある語と数値だけを使い、資料にない因果や数値は書かない)。最重要材料の話題を先頭にする。"
                  "summary_idsは、前営業日の市場全体(主要通貨ペアの終値、主要指標の結果など)を整理するfactのid(4〜6件)。"
                  "hero・各話題・summaryで同じfactを使わない。"
                  f"market_view_idsは、本日の地合いの判断材料となる市場関係者の見解のid(最大3件、{view_ids}から)。",
                  plain,
                  news.schema({"hero_ids": {"type": "array", "minItems": 1, "maxItems": 2, "items": {"type": "string", "enum": event_ids}},
                               "topics": {"type": "array", "minItems": 4, "maxItems": 5, "items": news.schema({
                                   "title": S, "fact_ids": {"type": "array", "minItems": 2, "maxItems": 5,
                                                            "items": {"type": "string", "enum": event_ids}}})},
                               "summary_ids": {"type": "array", "minItems": 4, "maxItems": 6, "items": {"type": "string", "enum": event_ids}},
                               "market_view_ids": {"type": "array", "minItems": 0, "maxItems": 3, "items": {"type": "string", "enum": view_ids or [""]}}}))
    used = set()

    closes = closing_ids(material)

    def take(ids):
        facts = [by_id[i] for i in dict.fromkeys(ids)
                 if i in by_id and i not in used and not conflicts_with_close(by_id[i], closes)]
        used.update(x["fact_id"] for x in facts)
        return facts

    hero_facts = take(topics["hero_ids"])
    topic_list, topic_facts = [], []
    for t in topics["topics"]:
        chosen_facts = take(t["fact_ids"])
        if chosen_facts:
            topic_list.append({"title": t["title"], "body": join_facts(chosen_facts)})
            topic_facts.append(chosen_facts)
    summary_facts = take(topics["summary_ids"])
    titles = "、".join(t["title"] for t in topic_list)
    market_views = [by_id[i] for i in dict.fromkeys(topics.get("market_view_ids", [])) if i in by_id and is_view(by_id[i])]
    point_ids = view_ids + theme_ids + [f"e{n}" for n in range(1, len(calendar["events"]) + 1)]
    today = call(out, "oneshot-3-today", style +
                 "本日の見通しのうち、文章は書かず、資料の項目を番号で選ぶだけにする。"
                 "focus_pairはranking_top5から1ペア。focus_view_idは、選んだ通貨ペアに関する市場関係者の見解のfactのid(なければ空文字)。"
                 f"risk_view_idsは、本日から今週の相場を動かしうる最大のリスクに直結する市場関係者の見解のfactのid(最大2件、見解のidは{view_ids}から。数か月先の予測は選ばない)。"
                 f"point_idsは、本日の注目点として読者に伝えるべき、重複しない項目のid3件(risk_view_idsと同じidは選ばない。factのid、または予定e<today_calendarのno>)。"
                 "key_event_nosは、本日の相場を動かす主要予定のtoday_calendarのno(整数)を8〜12件。"
                 "各国の政策・景況・物価・雇用の主要指標と、中央銀行総裁・要人発言を優先し、同じ指標の副項目や小さな指標は含めない。"
                 "本文で取り上げる通貨ペア(例: ユーロドル、ドル円)に関わる予定を必ず含める。",
                 data,
                 news.schema({"focus_pair": {"type": "string", "enum": pairs},
                              "focus_view_id": {"type": "string", "enum": view_ids + [""]},
                              "risk_view_ids": {"type": "array", "minItems": 0, "maxItems": 2, "items": {"type": "string", "enum": view_ids or [""]}},
                              "point_ids": {"type": "array", "minItems": 3, "maxItems": 3, "items": {"type": "string", "enum": point_ids}},
                              "key_event_nos": {"type": "array", "minItems": 8, "maxItems": 12, "items": {"type": "integer"}}}))

    # The feed's own importance grades are the only filter for "key events"; with a single source (Forex Factory
    # refused) they miss e.g. the Tankan and ISM, so use the model's selection (indices only) when it is valid.
    picked = sorted({n for n in today.get("key_event_nos", []) if 1 <= n <= len(calendar["events"])})
    chosen = [calendar["events"][n - 1] for n in picked] or calendar["key_events"]  # calendar order is already by time

    focus_view = by_id.get(today.get("focus_view_id", ""))
    if focus_view and today["focus_pair"] not in (focus_view.get("pairs") or []):
        focus_view = None  # a view about other pairs does not belong under this pair
    market_ids = {x["fact_id"] for x in market_views}
    risk_views = [by_id[i] for i in dict.fromkeys(today.get("risk_view_ids", []))
                  if i in by_id and is_view(by_id[i]) and i not in market_ids
                  and not restates(by_id[i]["fact"], [x["fact"] for x in market_views])]
    points = []
    for i in dict.fromkeys(today.get("point_ids", [])):
        if i in {v["fact_id"] for v in risk_views}:
            continue  # the same material is not repeated across sections
        if re.fullmatch(r"e\d+", i) and 1 <= int(i[1:]) <= len(calendar["events"]):
            points.append("本日の予定: " + event_label(calendar["events"][int(i[1:]) - 1]) + "。")
        elif i in by_id:
            points.append(sentence(by_id[i]))
    rank = {"high": 0, "medium": 1}
    for e in sorted(chosen, key=lambda x: rank.get(x.get("importance"), 2)):  # the model may repeat or miss an id: fill up to three from today's key schedule, most important first (time order within a grade)
        text = "本日の予定: " + event_label(e) + "。"
        if len(points) >= 3:
            break
        if text not in points:
            points.append(text)
    points = points[:3]
    high = sum(1 for e in calendar["events"] if e["importance"] == "high")
    sections = {"topics": topic_list,
                "hero": join_facts(hero_facts) if hero_facts else f"{topic_list[0]['title']}。",
                "headline": topic_list[0]["title"],
                "summary": join_facts(summary_facts) if summary_facts else f"前営業日の主な話題: {titles}。",
                "market": join_sourced(market_views) or no_market_view_text(titles) or "前営業日の主な話題は材料束にない。",
                "handover": handover_text(chosen),
                "market_holiday": holiday_line(calendar),
                "calendar_notes": calendar_notes(calendar, chosen),
                "focus_pair": today["focus_pair"],
                "focus_body": ranking_sentence(ranking, today["focus_pair"]) + (sentence(focus_view) if focus_view else ""),
                "risk_level": f"高重要度予定 {high}件",
                "risk_body": join_sourced(risk_views) or risk_fallback(calendar["events"]),
                "points": [{"title": f"焦点{i+1}", "body": p} for i, p in enumerate(points)]}
    written = feature("FX_WRITE_BODIES", "prose_writer")  # experiment 2026-10-14: the model writes the prose from the chosen facts
    if written:
        try:
            write_prose(out, style, sections, hero_facts, summary_facts, market_views, risk_views, topic_facts, chosen,
                        data["date_facts"], [e for e in events if e["importance"] == "high"],
                        material, calendar.get("weekly_themes") or "")
        except Exception as error:  # keep the assembled text; record why
            written = False
            sections["prose_error"] = f"{type(error).__name__}: {error}"
    news.save(out / "sections.json", sections)

    evidence = [{"quote": x.get("quote", ""), "fact": x.get("fact", ""), "source_context": x.get("source_context", {}),
                 "published_at": x.get("published_at", "")} for x in material]
    evidence += [{"quote": json.dumps(e, ensure_ascii=False), "fact": "", "source_context": {}, "published_at": ""}
                 for e in events]
    evidence += [{"quote": json.dumps(x, ensure_ascii=False), "fact": "", "source_context": {}, "published_at": ""}
                 for x in data["ranking_top5"] + data["policy_rates"]]
    # handover/focus/risk/points are assembled from sourced facts and the calendar (no model), so they are never
    # sent to the repair step; only the model-written sections can be flagged and rewritten.
    keys = [f"title{i}" for i in range(len(sections["topics"]))]
    if written:  # prose written by the model can be flagged and rewritten like the titles
        keys += ["hero", "summary", "market", "risk", "handoff"] + [f"topic{i}" for i in range(len(sections["topics"]))]

    def texts_of(sec):
        return {"hero": sec["hero"], "headline": sec["headline"], "summary": sec["summary"], "market": sec["market"],
                "handover": sec["handover"], "focus": sec["focus_body"], "risk": sec["risk_body"],
                **({"handoff": sec["handoff"]} if sec.get("handoff") else {}),
                **{f"title{i}": t["title"] for i, t in enumerate(sec["topics"])},
                **{f"topic{i}": t["body"] for i, t in enumerate(sec["topics"])},
                **{f"point{i}": p["body"] for i, p in enumerate(sec["points"])}}

    def mechanical(texts):
        return {"number_date_errors": {k: e for k, v in texts.items() if (e := grounding.number_errors(v, evidence, target))},
                "internal_wording": [k for k, v in texts.items()
                                     if re.search(daily.FORBIDDEN, v, re.I) or re.search(CODE_LIKE, v)],
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
    use_claim_check = feature("FX_CLAIM_CHECK", "claim_check")  # local sentence-level support check (no Codex)
    if use_claim_check:
        checks["claim_check_before"] = claim_check.review(out, verify_data, texts, os.environ.get("FX_REVIEW_MODEL") or None)
        external_issues += external_review.usable_issues(checks["claim_check_before"], keys)

    flagged = ({k for i in review["issues"] + external_issues for k in i["sections"]} | set(checks["number_date_errors"]) |
               set(checks["internal_wording"]) | set(checks["meta_wording"])) & set(keys)
    if flagged:
        problems = [{"sections": i["sections"], "excerpt": i["excerpt"], "reason": i["reason"]}
                    for i in review["issues"] + external_issues]
        problems += [{"sections": [k], "reason": "本文の数値が資料にない: " + ", ".join(v)}
                     for k, v in checks["number_date_errors"].items()]
        try:  # a failed or cut-off repair must not lose the written report (same rule as the verify step)
            fixed = call(out, "oneshot-5-repair",
                         "指摘された記述だけを直す。強すぎる断定の語(確定する・当面続く・最大の・加速する 等)は、資料の範囲の控えめな言い方"
                         "(〜しやすい・〜が意識される 等)に言い換えて、文と条件付きの見通しは残す。"
                         "資料にない数値水準・出来事・原因だけを削除するか、資料にある事実の表現に置き換える。"
                         "条件付きの見通し(上振れ・下振れ)は、資料にある数値だけを使って残す。指摘のない部分は変えない。"
                         "fixesには修正が必要なsectionだけを、修正後の全文で返す。",
                         {**verify_data, "problems": problems, "current": {k: texts[k] for k in sorted(flagged)}},
                         news.schema({"fixes": {"type": "array", "items": news.schema({
                             "section": {"type": "string", "enum": sorted(flagged)}, "text": S})}}), 30000)  # thinking alone used 12000 tokens on 2026-10-06
            for fix in fixed["fixes"]:
                k, text = fix["section"], fix["text"]
                if k.startswith("title"):
                    sections["topics"][int(k[5:])]["title"] = text
                elif k.startswith("topic"):
                    sections["topics"][int(k[5:])]["body"] = text
                elif k.startswith("point"):
                    sections["points"][int(k[5:])]["body"] = text
                else:
                    sections[{"focus": "focus_body", "risk": "risk_body"}.get(k, k)] = text
            checks["repaired_sections"] = [f["section"] for f in fixed["fixes"]]
        except Exception as error:
            checks["repair_error"] = f"{type(error).__name__}: {error}"
    sections["headline"] = sections["topics"][0]["title"]  # the headline is the lead topic's title (may have been repaired)
    news.save(out / "sections.json", sections)
    texts_after = texts_of(sections)
    checks["after_repair"] = {**mechanical(texts_after), "chars": {k: len(v) for k, v in texts_after.items()}}
    # Re-check the repaired text with the same reviewer; recorded only, no further rewrite.
    checks["external_review_after"] = (external_review.review(out, verify_data, texts_after)
                                       if checks.get("repaired_sections") else {"status": "skipped", "reason": "nothing repaired"})
    if use_claim_check:  # recorded only, like the external re-check
        checks["claim_check_after"] = (claim_check.review(out, verify_data, texts_after, os.environ.get("FX_REVIEW_MODEL") or None)
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
