"""keep: bounded, provenance-preserving FX shadow authoring and review.

Only the supplied dated sources are used. No upload, scheduler, model fallback,
or acquisition. Run artifacts are evidence, retained with the parent shadow run.
"""
from __future__ import annotations

import json
import re
import unicodedata
from datetime import date, datetime, timedelta

import local_fx_news as news


def previous_day(target):
    previous = target - timedelta(days=1)
    while previous.weekday() >= 5:
        previous -= timedelta(days=1)
    return previous


def date_facts(target):
    return {"today_jst": target.isoformat(), "weekday": "月火水木金土日"[target.weekday()],
            "previous_session_date": previous_day(target).isoformat(),
            "tomorrow_jst": (target + timedelta(days=1)).isoformat(),
            "rule": "掲載日時と出来事日時は別。月末最終営業日は暦日だけから推測しない。"}


def context_for(source, quote):
    text = source["text"]
    at = text.find(quote)
    if at < 0:
        raise ValueError("quote is not verbatim in original source")
    # The opening session/date and nearby heading survive fact selection.
    heading = text.rfind("■", 0, at)
    heading_text = text[heading:heading + 100] if heading >= 0 else ""
    return {"article_opening": text[:200], "nearby_heading": heading_text,
            "quote_surroundings": text[max(0, at - 170):at + len(quote) + 100]}


def bind_claim(source, claim, index, target):
    if claim["quote"] not in source["text"] or not 20 <= len(claim["quote"]) <= 180:
        raise ValueError("claim quotation failed original-source gate")
    result = dict(claim)
    opening = unicodedata.normalize("NFKC", source["text"][:200])
    quote_normal = unicodedata.normalize("NFKC", claim["quote"])
    explicit_sessions = [session for pattern, session in [
        (r"東京市場|東京時間|東京外国為替", "Tokyo"),
        (r"ロンドン時間|ロンドン市場", "London"),
        (r"NY時間|NY為替市場|ニューヨーク市場", "NY")]
        if re.search(pattern, quote_normal)]
    if len(explicit_sessions) == 1:
        result["market_session"] = explicit_sessions[0]
    elif len(explicit_sessions) > 1:
        result["market_session"] = "unspecified"
    # An article explicitly reporting today's Tokyo session cannot be silently
    # reassigned to yesterday merely because its price quote omits the opening.
    if re.search(rf"{target.day}日(?:午前の|の)東京", opening):
        result["event_scope"] = "current"
        result["market_session"] = "Tokyo"
    result.update(fact_id=f'N{source["source_id"]}-{index}', source_id=source["source_id"],
                  source_title=source["title"], source_url=source["source_url"],
                  published_at=source["published_at"], source_context=context_for(source, claim["quote"]))
    temporal_text = unicodedata.normalize("NFKC", claim["quote"] + " " + result["source_context"]["nearby_heading"])
    dated = re.search(r"(\d{1,2})月(\d{1,2})日", temporal_text)
    if dated:
        mentioned = date(target.year, int(dated[1]), int(dated[2]))
        if mentioned < previous_day(target):
            result["event_scope"] = "historical"
    elif re.search(r"先週(?:前半|後半|発表|は)|週前半|週末25日", temporal_text):
        result["event_scope"] = "historical"
    scope = result["event_scope"]
    result["event_date"] = (previous_day(target).isoformat() if scope == "previous" else
                            target.isoformat() if scope == "current" else None)
    return result


CLAIMS = news.schema({"claims": {"type": "array", "minItems": 0, "maxItems": 6,
    "items": news.schema({"kind": {"type": "string", "enum": ["event", "price", "cause", "outlook"]},
        "fact": news.STRING, "quote": news.STRING,
        "event_scope": {"type": "string", "enum": ["previous", "current", "historical", "unknown"]},
        "market_session": {"type": "string", "enum": ["Tokyo", "London", "NY", "unspecified"]},
        "pairs": {"type": "array", "items": news.STRING, "maxItems": 3},
        "record_type": {"type": "string", "enum": ["actual", "forecast", "outlook"]}})}})

COPY = news.schema({"title": news.STRING, "statements": {"type": "array", "minItems": 1, "maxItems": 5,
    "items": news.schema({"text": news.STRING,
        "fact_ids": {"type": "array", "items": news.STRING, "minItems": 1, "maxItems": 3},
        "mode": {"type": "string", "enum": ["fact", "conditional", "attributed_outlook"]}})}})


def copy_errors(copy, evidence, target):
    allowed = {x["fact_id"]: x for x in evidence}
    errors = []
    if not copy.get("statements"):
        return ["no source-linked statements"]
    for statement in copy["statements"]:
        ids = statement["fact_ids"]
        if not ids or any(x not in allowed for x in ids):
            errors.append("invalid or absent fact reference")
            continue
        text = unicodedata.normalize("NFKC", statement["text"])
        linked = [allowed[x] for x in ids]
        if "NY" in text or "ニューヨーク" in text:
            if all(x.get("market_session") == "Tokyo" for x in linked):
                errors.append("Tokyo-only facts assigned to NY")
        if (statement["mode"] == "fact" and all(x.get("record_type") in {"forecast", "outlook"} for x in linked)
                and not re.search(r"予想|予定|見通し|との見方|との指摘|前回", text)):
            errors.append("forecast/outlook written as realized fact")
        if re.search(r"本日.{0,40}最終営業日(?:の)?翌日", text) and any(
                "明日" in str(x) and "最後の営業日" in str(x) for x in linked):
            errors.append("today contradicts source month-end date")
    return errors


def review_copy(api, out, label, copy, evidence, target):
    errors = copy_errors(copy, evidence, target)
    if errors:
        return {"verdict": "FAIL", "reason": "; ".join(errors)}
    used = set(x for s in copy["statements"] for x in s["fact_ids"])
    originals = [x for x in evidence if x["fact_id"] in used]
    data = {"date_facts": date_facts(target), "original_evidence": originals, "draft": copy}
    task = ("厳格な原資料照合だけ行う。見出しと各statementの日時・取引時間帯・通貨ペア・数字・予想/実績・因果を"
            "fact_idsの原文quoteとsource_contextまで戻って確認。抜粋だけで日時を決めない。"
            "前日のNYと当日東京、先週の出来事を混同したらFAIL。利上げ予想を実施済みにしたらFAIL。"
            "日付はdate_factsと照合。条件付き分析は資料の材料に基づく条件/観察項目なら許容するが、"
            "未出典のニュース・価格目標・因果の創作は禁止。段落内に根拠のない事実が一つでもあればFAIL。理由は具体的に。")
    if len(json.dumps(data, ensure_ascii=False).encode()) <= 19000:
        return api.infer_cached(out, label, task, data, news.QC_SCHEMA)
    # Review individual source-linked statements, never drop contexts to fit.
    verdicts = []
    for i, statement in enumerate(copy["statements"]):
        refs = set(statement["fact_ids"])
        one = {"date_facts": date_facts(target), "original_evidence": [x for x in originals if x["fact_id"] in refs],
               "draft": {"title": copy["title"], "statements": [statement]}}
        verdicts.append(api.infer_cached(out, f"{label}-{i:02}", task, one, news.QC_SCHEMA))
    return {"verdict": "PASS" if all(x["verdict"] == "PASS" for x in verdicts) else "FAIL",
            "reason": " / ".join(x["reason"] for x in verdicts)}


def author(api, out, label, purpose, evidence, target, length):
    if not evidence:
        raise ValueError(f"{label}: no eligible grounded facts")
    # Writers receive typed facts and quotations; reviewers additionally get
    # original opening/headings/context. Neither receives an earlier model draft
    # as the sole source of truth.
    compact = [{k: v for k, v in x.items() if k not in {"source_context", "source_url", "source_title"}}
               for x in evidence]
    data = {"date_facts": date_facts(target), "facts": compact}
    task = (f"FX日報の{purpose}だけを書く。合計{length}文字目安だが、一般論や反復で埋めない。"
            "titleは具体的で短い見出し。statementsの各textは1〜2文、根拠fact_idsを必ず付ける。"
            "使用する根拠は入力に限る。event_date/market_session/pairs/record_typeを守る。"
            "『きょう』をNYと固定変換しない。historicalは前日の出来事にしない。"
            "forecastは予想、outlookは出典の見方と明示。自分の当日分析はconditionalで条件と観察項目を示す。"
            "価格の数字を別ペアへ移さない。資料にない価格目標や因果を作らない。"
            "本文にfact ID・出典管理・内部状況・要確認・再確認を書かない。")
    draft = api.infer_cached(out, f"{label}-write", task, data, COPY)
    qc = review_copy(api, out, f"{label}-review", draft, evidence, target)
    if qc["verdict"] != "PASS":
        draft = api.infer_cached(out, f"{label}-repair", task + " 指摘された誤りだけ修正。",
                                 {**data, "rejected_draft": draft, "review": qc}, COPY)
        qc = review_copy(api, out, f"{label}-review-repair", draft, evidence, target)
    news.save(out / "stages" / f"{label}-grounded-review.json", {"draft": draft, "review": qc})
    if qc["verdict"] != "PASS":
        raise ValueError(f"{label}: original-context review failed after one repair: {qc['reason']}")
    body = "\n\n".join(s["text"] for s in draft["statements"])
    if re.search(api.FORBIDDEN, draft["title"] + body, re.I):
        raise ValueError("internal status leaked into copy")
    return {"title": draft["title"], "body": body, "statements": draft["statements"],
            "claim_ids": list(dict.fromkeys(x for s in draft["statements"] for x in s["fact_ids"])),
            "review": qc}


def extract(api, sources, target, out):
    facts = []
    for source in sources:
        extracted = []
        for part, text in enumerate(api.source_chunks(source["text"])):
            value = api.infer_cached(out, f'source-{source["source_id"]:02}-part-{part:02}-typed-extract',
                "重要な事実を0〜6件抽出。quoteはこのtextから完全一致20〜180文字。"
                "event_scopeはprevious=指定前営業日の出来事、current=本日、historical=それ以前/週のまとめ、unknown=不明。"
                "掲載日だけから決めずarticle_opening/nearby_heading/本文の文脈で判断。"
                "朝のNY概況で『きょうのNY』は前営業日のNY。東京市場の『本日』は本日。"
                "日付のない先週の振り返りを前日扱いにしない。"
                "market_sessionは原文の市場、分からなければunspecified。pairsは当該事実の対象だけUSD/JPY等で返す。"
                "実績actual・予想forecast・出典の見通しoutlookを区別。factは日付/市場/ペアを省略せず日本語1文。"
                "発言・価格反応・原因・条件付き見通しを拾い、同時発生を因果にしない。",
                {"date_facts": date_facts(target), "published_at": source["published_at"],
                 "source_title": source["title"], "article_opening": source["text"][:240],
                 "nearby_heading": context_for(source, text)["nearby_heading"], "text": text}, CLAIMS)
            chunk_facts = []
            for claim in value["claims"]:
                if claim["quote"] not in text:
                    news.save(out / "stages" / f'source-{source["source_id"]:02}-part-{part:02}-outside-chunk.json',
                              {"rejected_claim": claim, "reason": "quote must come from this chunk, not article_opening"})
                    continue
                if any(x["quote"] == claim["quote"] for x in extracted):
                    continue
                try:
                    bound = bind_claim(source, claim, len(extracted) + len(chunk_facts), target)
                except ValueError:
                    news.save(out / "stages" / f'source-{source["source_id"]:02}-part-{part:02}-rejected-quote.json', claim)
                    continue
                chunk_facts.append(bound)
            if chunk_facts:
                gate_schema = news.schema({"accepted_fact_ids": {"type": "array", "items": news.STRING, "maxItems": 6},
                    "rejections": {"type": "array", "items": news.schema({"fact_id": news.STRING, "reason": news.STRING})}})
                checked = api.infer_cached(out, f'source-{source["source_id"]:02}-part-{part:02}-claim-gate-review',
                    "抽出したfact/型/日時/市場/対象ペアを原文に照合。原文の国や通貨を変更、先週を前日扱い、"
                    "予想を実績扱い、ロンドンをNY扱いなど一つでも誤りがあればそのfactを採用しない。"
                    "factの根拠quoteとsource_contextを使い、article_openingは文脈だけで本文外の事実を追加しない。"
                    "全フィールドが裏付けられるfact_idだけaccepted_fact_idsへ返す。rejectionsに他の全IDと具体的理由。",
                    {"date_facts": date_facts(target), "claims": chunk_facts}, gate_schema)
                all_ids = {x["fact_id"] for x in chunk_facts}
                accepted = set(checked["accepted_fact_ids"])
                rejected_ids = {x["fact_id"] for x in checked["rejections"]}
                if accepted & rejected_ids or accepted | rejected_ids != all_ids:
                    raise ValueError("claim gate must account for every supplied fact exactly once")
                # Keep indexes stable even when a fact is rejected; never reuse a
                # rejected ID for another fact in a later chunk.
                extracted.extend({**x, "claim_gate_accepted": x["fact_id"] in accepted} for x in chunk_facts)
        facts.extend(extracted)
        news.save(out / "claims.json", facts)
    if len([x for x in facts if x["event_scope"] == "previous" and x["claim_gate_accepted"]]) < 5:
        raise ValueError("previous-session facts insufficient; do not fill from today's Tokyo")
    return facts


def pick(api, out, label, topic, candidates, target, max_facts=5):
    selection_schema = news.schema({"fact_ids": {"type": "array", "items": news.STRING, "minItems": 1, "maxItems": max_facts}})
    slim = [{k: v for k, v in x.items() if k not in {"source_context", "source_url", "source_title"}} for x in candidates]
    groups = api.evidence_batches(slim, 10500)
    selected = []
    for i, group in enumerate(groups):
        choice = api.infer_cached(out, f"{label}-{i:02}-plan",
            "指定トピックに直結する根拠だけ選ぶ。同じ価格の重複は省き、出来事→実際の反応→理由の組を残す。"
            "本日/先週の出来事を前日に変えない。fact_idsは入力にあるものだけ。",
            {"topic": topic, "date_facts": date_facts(target), "facts": group}, selection_schema)["fact_ids"]
        allowed = {x["fact_id"] for x in group}
        if any(x not in allowed for x in choice):
            raise ValueError("invalid selected fact reference")
        selected.extend(x for x in choice if x not in selected)
    # A final bounded selection if candidate batches supplied more than the cap.
    if len(selected) > max_facts:
        pool = [x for x in slim if x["fact_id"] in selected]
        choice = api.infer_cached(out, f"{label}-final-plan", "トピックに直結する非重複の重要根拠だけ選ぶ。",
                                  {"topic": topic, "facts": pool}, selection_schema)["fact_ids"]
        if any(x not in selected for x in choice):
            raise ValueError("invalid final selected fact reference")
        selected = choice
    return [x for x in candidates if x["fact_id"] in selected]


def editorial_facts(calendar, ranking, facts, topics):
    used = {x for t in topics for x in t["claim_ids"]}
    material = [x for x in facts if x["fact_id"] in used]
    for i, event in enumerate(calendar["key_events"]):
        if not event["confirmed"]:
            continue
        text = f'{event["time_jst"]} JST {event["country"]} {event["name"]}。予想 {event["forecast"]}、前回 {event["previous"]}。'
        material.append({"fact_id": f"C{i}", "fact": text, "quote": text,
            "event_date": event["datetime_jst"][:10], "event_scope": "current", "market_session": "unspecified",
            "record_type": "forecast", "pairs": [], "source_context": {"source_urls": event["sources"],
                "notice": "確認済みの発表予定。予想は結果ではない。24時以降は翌日早朝。"}})
    # Keep full day / weekly themes as original snippets, not summaries of model prose.
    for prefix, text in [("D", calendar["day_themes"]), ("W", calendar.get("weekly_themes", ""))]:
        if text:
            for i, chunk in enumerate(api_chunks(text)):
                material.append({"fact_id": f"{prefix}{i}", "fact": chunk, "quote": chunk,
                    "event_scope": "current", "market_session": "unspecified", "pairs": [],
                    "record_type": "outlook", "source_context": {"source_urls": calendar["source_urls"]}})
    for i, item in enumerate(ranking["rankings"][:5]):
        text = f'{item["pair"]} 第{item["rank"]}位、スコア{item["score"]}、{item["verdict"]}、方向{item["direction"]}、ADX {item["adx_h4"]}、ADR比{item["adr_ratio_pct"]}%。算出時点{ranking["generated_at_jst"]}。'
        material.append({"fact_id": f"R{i}", "fact": text, "quote": text, "record_type": "actual",
            "event_scope": "current", "market_session": "unspecified", "pairs": [item["pair"]],
            "source_context": {"source_url": "https://auxen.jp/data/daytrade-ranking.json"}})
    return material


def api_chunks(text):
    # Themes are bounded complete clauses, never cut a date explanation midway.
    parts = re.split(r"(?=・)", text)
    return [x.strip() for x in parts if x.strip()][:18]


def make_sections(api, sources, calendar, ranking, out, topic_probe=0):
    target = date.fromisoformat(calendar["date_jst"])
    facts = extract(api, sources, target, out)
    prior = [x for x in facts if x["event_scope"] == "previous" and x["claim_gate_accepted"]]
    plan_schema = news.schema({"topics": {"type": "array", "minItems": 5, "maxItems": 5,
        "items": news.schema({"title": news.STRING, "fact_ids": {"type": "array", "items": news.STRING, "minItems": 1, "maxItems": 6}})}})
    plan_data = [{k: x[k] for k in ["fact_id", "kind", "fact", "event_date", "market_session", "pairs", "record_type"]} for x in prior]
    plan = api.infer_cached(out, "grounded-news-plan", "前営業日の主要出来事を5件、重要順で選ぶ。"
        "通貨別の羅列ではなく出来事単位。相場反応と理由のある具体的材料を優先。同じ材料を反復しない。"
        "資料にない出来事は作らず、fact_idsは入力のみ。",
        {"date_facts": date_facts(target), "facts": plan_data}, plan_schema)
    topics = []
    for i, topic in enumerate(plan["topics"][:topic_probe or 5]):
        if any(x not in {f["fact_id"] for f in prior} for x in topic["fact_ids"]):
            raise ValueError("news plan selected non-previous or invalid fact")
        evidence = [x for x in prior if x["fact_id"] in topic["fact_ids"]]
        draft = author(api, out, f"grounded-topic-{i:02}",
                       f'前営業日の振り返り「{topic["title"]}」。何が起き、価格がどう動き、なぜ動いたかを説明',
                       evidence, target, "250〜450")
        draft["source_ids"] = sorted({x["source_id"] for x in evidence})
        topics.append(draft)
        news.save(out / "news.json", {"topics": topics, "publish_ready": False})
    if topic_probe:
        return {"topics": topics, "probe_only": True}
    material = editorial_facts(calendar, ranking, facts, topics)
    roles = [
        ("hero", "冒頭。前日の最大の変化と本日の焦点を2点だけ", "120〜200"),
        ("headline", "一言まとめ。最重要材料だけで45文字以内の短文", "30〜45"),
        ("summary", "サマリー。前日の市場全体の変化を、ニュースの丸写しや5件の羅列ではなく整理", "350〜550"),
        ("market", "市場環境。ドル・円・ユーロの地合いを説明し、本日の判断条件を示す。過去ニュースの再列挙はしない", "300〜450"),
        ("handover", "本日の引継ぎ。アジア/欧州/NYの予定時刻と、それぞれ何の変化を見るか。前日のニュースの再要約はしない", "220〜350"),
        ("focus", "注目通貨。ランキング順位と実際の相場材料を併せて1ペアを選び、観察条件を説明", "200〜300"),
        ("risk", "市場リスク。介入警戒/政策発表/指標のうち最重要リスクの条件と影響を説明。発表前は予想・予定と明記", "200〜300"),
        ("points", "その他注目点。月末要因/週後半の指標など本文ニュースと重複しない具体的焦点を3点、各1文", "200〜350"),
    ]
    editorial = {}
    for key, purpose, length in roles:
        candidates = [x for x in material if (key != "summary" or x["fact_id"].startswith("N"))
                      and (key != "handover" or not x["fact_id"].startswith("N"))
                      and (key != "points" or x["fact_id"].startswith(("D", "W", "C")))]
        evidence = pick(api, out, f"editorial-{key}-evidence", purpose, candidates, target, 5)
        editorial[key] = author(api, out, f"grounded-editorial-{key}", purpose, evidence, target, length)
        news.save(out / "editorial-progress.json", editorial)
    # Pair/risk classifications are small independent decisions over already
    # verified text, never a chance to rewrite prose or numbers.
    labels = api.infer_cached(out, "grounded-focus-label-plan",
        "focus_pairは候補ランキングの1ペアだけ。risk_levelは本文理由の程度からHIGH/MEDIUM/LOWを選ぶ。本文を改変しない。",
        {"focus": editorial["focus"]["body"], "risk": editorial["risk"]["body"],
         "pairs": [x["pair"] for x in ranking["rankings"][:5]]},
        news.schema({"focus_pair": news.STRING, "risk_level": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]}}))
    if labels["focus_pair"] not in [x["pair"] for x in ranking["rankings"][:5]]:
        raise ValueError("focus classification returned unranked pair")
    result = {"topics": topics, **{k: editorial[k]["body"] for k in ["hero", "headline", "summary", "market", "handover"]},
              **labels, "focus_body": editorial["focus"]["body"], "risk_body": editorial["risk"]["body"],
              "points": [{"title": f"焦点{i+1}", "body": x["text"]} for i, x in enumerate(editorial["points"]["statements"])],
              "editorial_reviews": {k: x["review"] for k, x in editorial.items()}, "grounded_editorial": editorial}
    news.save(out / "sections.json", result)
    return result
