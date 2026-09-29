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
    if claim["quote"] in source["text"] and len(claim["quote"]) < 20:
        at = source["text"].find(claim["quote"])
        end = source["text"].find("。", at + len(claim["quote"]))
        if end >= 0 and 20 <= end + 1 - at <= 180:
            # Extend a short price sentence with its ORIGINAL next sentence;
            # the stored model request/response remain untouched evidence.
            claim = {**claim, "quote": source["text"][at:end + 1]}
    if claim["quote"] not in source["text"] or not 20 <= len(claim["quote"]) <= 180:
        raise ValueError("claim quotation failed original-source gate")
    result = dict(claim)
    if (result["record_type"] == "actual" and re.search(
            r"予定(?:されている)?|(?:発表|公表|開催)(?:される|する)[。.]?$|行われる[。.]?$|発言がある[。.]?$|会見を行う[。.]?$",
            result["fact"])):
        # A scheduled release is not an already realized economic result.
        result["record_type"] = "forecast"
    if result["record_type"] == "outlook":
        result["kind"] = "outlook"
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
    if re.search(r"貿易収支|GDP|消費者信頼感指数|消費者物価指数|雇用統計|政策金利", claim["fact"]):
        original_context = unicodedata.normalize("NFKC", source["title"] + " " + claim["quote"] + " " +
            json.dumps(result["source_context"], ensure_ascii=False))
        for country, aliases in {"米国": r"米国|アメリカ|米\)|米雇用|米GDP", "英国": r"英国|イギリス|英\)",
                                 "メキシコ": r"メキシコ", "カナダ": r"カナダ|加\)", "豪州": r"豪州|オーストラリア|豪\)"}.items():
            if country in claim["fact"] and not re.search(aliases, original_context):
                raise ValueError(f"economic release country {country} is not grounded in original context")
    temporal_text = unicodedata.normalize("NFKC", claim["quote"] + " " + result["source_context"]["nearby_heading"])
    dated = re.search(r"(\d{1,2})月(\d{1,2})日", temporal_text)
    if dated:
        mentioned = date(target.year, int(dated[1]), int(dated[2]))
        if mentioned < previous_day(target):
            result["event_scope"] = "historical"
    elif re.search(r"先週(?:前半|後半|末|発表|は)|週前半|週末25日", temporal_text):
        result["event_scope"] = "historical"
    at = source["text"].find(claim["quote"])
    before_quote = source["text"][max(0, at - 140):at]
    analytic_context = source["text"][max(0, at - 450):at]
    if re.search(r"総評|基本戦略|想定レンジ", analytic_context):
        result["record_type"] = "outlook"
        result["kind"] = "outlook"
    if re.search(r"先週最大のテーマ[^。]*。[\s]*$", before_quote):
        # A later undated analysis subsection can still describe last week's
        # trigger; a preceding '9/28〜足元' heading is not a blanket timestamp.
        result["event_scope"] = "historical"
    published = datetime.fromisoformat(source["published_at"]).astimezone(news.JST)
    if (result["record_type"] == "outlook" and published.date() < target
            and result["event_scope"] != "historical"):
        # Date the source's reported view, not a future event or this report.
        # Yesterday's '本日/今朝' is never silently promoted to today.
        result["event_scope"] = "previous" if published.date() == previous_day(target) else "historical"
        result["event_date_basis"] = "outlook reported at original publication, not a fresh current-day view"
    morning_ny = (published.date() == target and published.hour < 7
                  and bool(re.search(r"NY為替概況", unicodedata.normalize("NFKC", source["title"]))))
    if (morning_ny and result["event_scope"] == "current" and result["record_type"] == "actual"
            and result["market_session"] in {"NY", "unspecified"}
            and not re.search(rf"(?:{target.month}月)?{target.day}日", quote_normal)):
        result["event_scope"] = "previous"
        result["event_date_basis"] = "actual trading in morning NY recap, not JST publication date"
    if (result["event_scope"] == "unknown" and result["record_type"] == "outlook"
            and morning_ny):
        # This dates the *reported outlook*, never the future budget or price
        # scenario it describes. Its record_type remains outlook.
        result["event_scope"] = "previous"
        result["event_date_basis"] = "outlook reported in preceding NY recap, not forecast event occurrence"
    scope = result["event_scope"]
    result["event_date"] = (previous_day(target).isoformat() if scope == "previous" else
                            target.isoformat() if scope == "current" else None)
    # Explicit event dates outrank the model's publication-day classification.
    # Do not date an analyst's outlook this way: its reporting date is separate
    # from the date of a forecast event.
    if result["record_type"] in {"actual", "forecast"}:
        explicit = re.search(r"(\d{1,2})月(\d{1,2})日", quote_normal)
        relative = re.search(r"明日(?:\d{1,2}月)?(\d{1,2})日", quote_normal)
        event_day = date(target.year, int(explicit[1]), int(explicit[2])) if explicit else None
        if relative:
            source_tomorrow = published.date() + timedelta(days=1)
            if source_tomorrow.day == int(relative[1]):
                event_day = source_tomorrow
        if event_day is not None:
            result["event_date"] = event_day.isoformat()
            result["event_scope"] = ("future" if event_day > target else "current" if event_day == target else
                                     "previous" if event_day == previous_day(target) else "historical")
            result["event_date_basis"] = "explicit original event date, not publication date"
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
        "mode": {"type": "string", "enum": ["fact", "reported_forecast", "conditional", "attributed_outlook"]}})}})


def normalize_modes(copy, evidence):
    """Normalize classification metadata only; never rewrite generated prose."""
    by_id = {x["fact_id"]: x for x in evidence}
    for statement in copy["statements"]:
        linked = [by_id[x] for x in statement["fact_ids"] if x in by_id]
        if (linked and all(x.get("record_type") == "forecast" for x in linked)
                and re.search(r"予想|見込み|予定", statement["text"])
                and not re.search(r"なら|場合|次第", statement["text"])):
            statement["mode"] = "reported_forecast"
        elif (linked and all(x.get("record_type") == "actual" for x in linked)
              and statement["mode"] == "reported_forecast"
              and not re.search(r"予想|見込み|予定|なら|場合|次第|観察|確認|注意|焦点", statement["text"])):
            statement["mode"] = "fact"
    return copy


def country_errors(text, evidence):
    original = json.dumps([{k: x.get(k, "") for k in ["quote", "source_context"]} for x in evidence], ensure_ascii=False)
    if (re.search(r"米伊|イタリア", text) and "イラン" in original
            and not re.search(r"米伊|イタリア", original)):
        return ["Iran replaced by Italy/米伊 without original-source support"]
    return []


def copy_errors(copy, evidence, target):
    allowed = {x["fact_id"]: x for x in evidence}
    errors = []
    if not copy.get("statements"):
        return ["no source-linked statements"]
    title = unicodedata.normalize("NFKC", copy.get("title", ""))
    errors.extend(country_errors(title, evidence))
    if ("利上げ" in title and any(x.get("record_type") == "forecast" and "利上げ" in x.get("fact", "") for x in evidence)
            and not re.search(r"予想|見込み|予定|なら|場合|見通し", title)
            and not any(x.get("record_type") == "actual" and "利上げ" in x.get("fact", "") for x in evidence)):
        errors.append("headline presents rate-hike forecast without a forecast qualifier")
    for statement_no, statement in enumerate(copy["statements"], 1):
        ids = statement["fact_ids"]
        if not ids or any(x not in allowed for x in ids):
            errors.append("invalid or absent fact reference")
            continue
        text = unicodedata.normalize("NFKC", statement["text"])
        linked = [allowed[x] for x in ids]
        errors.extend(country_errors(text, linked))
        if "NY" in text or "ニューヨーク" in text:
            if all(x.get("market_session") == "Tokyo" for x in linked):
                errors.append("Tokyo-only facts assigned to NY")
        future_focus = bool(re.search(r"本日注目すべきは|(?:本日|今日|明日)の焦点は|(?:を注視する|に注目する|が焦点)[。.]?$", text))
        realized_assertion = bool(re.search(r"利上げした|引き上げた|発表された|公表された|実施された|決定された|となった", text))
        if (all(x.get("record_type") in {"forecast", "outlook"} for x in linked)
                and not (future_focus and not realized_assertion)
                and not re.search(r"予想|見込み|予定|見通し|見方|指摘|前回|なら|場合|か[^。]{0,35}(?:確認|観察)|想定|可能性|明日", text)):
            errors.append("forecast/outlook written as realized fact")
            errors.append(f"statement {statement_no}, refs {','.join(ids)}: {text} — 予想/予定/出典の見方または明示的な条件として書く")
        if (re.search(r"本日(?:は|が)?(?:\d+月|月末|四半期末|の|・|、)*最終営業日", text)
                and not re.search(r"本日(?:は|が)?[^。]{0,40}最終営業日[^。]{0,20}(?:明日(?:の)?)?前日", text)
                and any(
                "明日" in str(x) and "最後の営業日" in str(x) for x in linked)):
            errors.append("today contradicts source month-end date")
        if (any(x.get("record_type") == "forecast" for x in linked)
                and re.search(r"利上げ決定|利上げした|引き上げた", text)
                and not re.search(r"予想|見込み|なら|場合|見通し", text)
                and not any(x.get("record_type") == "actual" and "利上げ" in x.get("fact", "") for x in linked)):
            errors.append("rate-hike outcome substituted for scheduled policy decision")
        if "观察" in text:
            errors.append("non-Japanese observation wording: replace 观察 with Japanese 観察")
    return errors


def review_copy(api, out, label, copy, evidence, target):
    errors = copy_errors(copy, evidence, target)
    if "editorial-headline" in label and sum(len(x["text"]) for x in copy["statements"]) > 60:
        errors.append("headline exceeds the compact one-line card budget (60 characters)")
    if any(x in errors for x in ["no source-linked statements", "invalid or absent fact reference"]):
        return {"verdict": "FAIL", "reason": "; ".join(errors)}
    used = set(x for s in copy["statements"] for x in s["fact_ids"])
    originals = [x for x in evidence if x["fact_id"] in used]
    review_draft = {"title": copy["title"], "statements": [
        {"text": s["text"], "fact_ids": s["fact_ids"]} for s in copy["statements"]]}
    observation_rule = (
        "事実の断定と将来の観察質問を分離して照合。観察質問自体が出典に載っている必要はない。"
        "例: 原文にFRB発言予定があれば『予定される発言後、ドルの反応が変わるか観察する』は観察項目であり実績/因果断定ではない。"
        "一方『発言で必ずドル高になる』『発言でドルが上昇した』には、その機序/実績の原文支持が必要。"
        "予定日時、対象通貨、背景の既発生事実、数値と、文中で断定する因果は必ず根拠を照合。"
        "背景と予定を結ぶ文は両方のfact_idsを確認。観察質問の完全一致文がないことだけをFAIL理由にしない。")
    data = {"date_facts": date_facts(target), "original_evidence": originals, "draft": review_draft,
            "observation_vs_assertion_rule": observation_rule}
    task = (observation_rule + "厳格な原資料照合だけ行う。見出しと各statementの日時・取引時間帯・通貨ペア・数字・予想/実績・因果を"
            "fact_idsの原文quoteとsource_contextまで戻って確認。抜粋だけで日時を決めない。"
            "前日のNYと当日東京、先週の出来事を混同したらFAIL。利上げ予想を実施済みにしたらFAIL。"
            "本日JST07時前掲載のNY為替概況の『きょうのNY』は前営業日のNY取引。東京記事には適用しない。"
            "outlookのevent_date_basisは見方が記録された時点であり、将来イベントの実施日ではない。"
            "本文が予想・見込み・予定を紹介している場合、『利上げになる見込み』等は実施済み断定ではない。"
            "将来の予定/予想を紹介する文にif条件は不要。予想と明示しただけの文を創作としてFAILにしない。"
            "日付はdate_factsと照合。条件付き分析の観察項目は、出典に同一の文章があることを要求しない。"
            "資料で述べられた材料と反応の結びつきを本日の確認条件として使うのは許容。"
            "ただし予測を必然の結果と断定、新しい原因/機序/価格目標/予定/実現済み事実を付け加えるのは禁止。"
            "『金利とドル買いがともに弱まるかを確認』のような観察と、『金利が下がるから必ず円高』を区別。"
            "原文の想定レンジ/総評/基本戦略は出典の見方で、市場全体の事実として断定しない。"
            "異なる取引時間帯の原因を特定価格の原因へ混ぜない。根拠のない事実が一つでもあればFAIL。理由は具体的に。")
    def combined(review):
        # Deterministic date/country/length failures do not hide other semantic
        # errors from the ONE repair. Invalid references still stop immediately.
        reasons = errors + ([review["reason"]] if review["verdict"] != "PASS" else [])
        return {"verdict": "FAIL", "reason": "; ".join(reasons)} if reasons else review
    if len(json.dumps(data, ensure_ascii=False).encode()) <= 19000:
        return combined(api.infer_cached(out, label, task, data, news.QC_SCHEMA))
    # Review individual source-linked statements, never drop contexts to fit.
    verdicts = []
    for i, statement in enumerate(review_draft["statements"]):
        refs = set(statement["fact_ids"])
        one = {"date_facts": date_facts(target), "original_evidence": [x for x in originals if x["fact_id"] in refs],
               "draft": {"title": copy["title"], "statements": [statement]},
               "observation_vs_assertion_rule": observation_rule}
        verdicts.append(api.infer_cached(out, f"{label}-{i:02}", task, one, news.QC_SCHEMA))
    return combined({"verdict": "PASS" if all(x["verdict"] == "PASS" for x in verdicts) else "FAIL",
                     "reason": " / ".join(x["reason"] for x in verdicts)})


def author(api, out, label, purpose, evidence, target, length, overview=None):
    if not evidence:
        raise ValueError(f"{label}: no eligible grounded facts")
    # Writers receive typed facts and quotations; reviewers additionally get
    # original opening/headings/context. Neither receives an earlier model draft
    # as the sole source of truth.
    compact = [{k: v for k, v in x.items() if k not in {"source_context", "source_url", "source_title"}}
               for x in evidence]
    data = {"date_facts": date_facts(target), "facts": compact}
    if overview:
        data["global_overview"] = overview
    relations = []
    tomorrow = target + timedelta(days=1)
    for fact in evidence:
        if re.search(rf"明日(?:{tomorrow.month}月)?{tomorrow.day}日[^。]*最後の営業日", fact.get("quote", "")):
            relations.append({"source_fact_id": fact["fact_id"], "source_recorded_day": tomorrow.isoformat(),
                "relation": "本日はその前日。出典の『最後の営業日』は明日を指す。本日とは書かない"})
    if relations:
        data["fixed_calendar_relations"] = relations
    task = (f"FX日報の{purpose}だけを書く。合計{length}文字目安だが、一般論や反復で埋めない。"
            "titleは具体的で短い見出し。statementsの各textは1〜2文、根拠fact_idsを必ず付ける。"
            "各statementは単独で照合される。他のstatementの根拠IDは引き継がない。"
            "前日の圧力と当日の予定を結ぶ分析文には、背景と予定の両方のfact_idsを付ける。"
            "使用する根拠は入力に限る。event_date/market_session/pairs/record_typeを守る。"
            "『きょう』をNYと固定変換しない。historicalは前日の出来事にしない。"
            "forecastは予想、outlookは出典の見方と明示。自分の当日分析はconditionalで条件と観察項目を示す。"
            "分析は確認できる条件と観察項目を具体化する。相場が必ずその方向になるとは断定しない。"
            "『可能性がある/かもしれない/様子見/注目したい』で終えず、何の変化を観察するかを書く。"
            "出典の総評/戦略/レッドラインは誰の見方かを示し、市場全体の確定事実にしない。"
            "発表予定・市場予想の紹介はreported_forecast（例『市場予想は25bp利上げ』）、実施済みとは書かない。"
            "会合は『政策金利決定/発表』であって『利上げ決定』ではない。利上げは予想/条件と本文・title双方に明示。"
            "価格の数字を別ペアへ移さない。資料にない価格目標や因果を作らない。"
            "上昇/下落の方向や回数を、高値/安値という価格水準へ言い換えない。述語の意味を保持する。"
            "本文にfact ID・出典管理・内部状況・要確認・再確認を書かない。")
    draft = normalize_modes(api.infer_cached(out, f"{label}-write", task, data, COPY), evidence)
    qc = review_copy(api, out, f"{label}-review", draft, evidence, target)
    if qc["verdict"] != "PASS":
        draft = normalize_modes(api.infer_cached(out, f"{label}-repair", task + " 指摘された誤りだけ修正。",
                                 {**data, "rejected_draft": draft, "review": qc}, COPY), evidence)
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
                "発言・価格反応・原因・条件付き見通しを拾い、同時発生を因果にしない。" +
                ("先週末はhistorical。前営業日掲載の『本日/今朝』は掲載日であり本日ではない。"
                 "outlookは出典の見方が記録された時点で、将来予定の実施日と混同しない。"
                 if datetime.fromisoformat(source["published_at"]).astimezone(news.JST).date() < target else ""),
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
                    "抽出したfact/型/日時/市場/対象ペアを原文に照合。本日JST07時前掲載のNY為替概況の"
                    "『きょうのNY』は前営業日のNY取引。掲載日のNY取引と取り違えない。東京記事には適用しない。"
                    "outlook/forecastは出典の見方・予定として採用可。"
                    "予測が実現したかは採否条件ではない。複数市場を含む引用のmarket_session=unspecifiedは許容。"
                    "event_date_basisがoutlookなら日付は見方の記録時点で、将来イベントの実施日ではない。"
                    "原文の国や通貨を変更、先週を前日扱い、"
                    "予想を実績扱い、ロンドンをNY扱いなど一つでも誤りがあればそのfactを採用しない。"
                    "factの根拠quoteとsource_contextを使い、article_openingは文脈だけで本文外の事実を追加しない。"
                    "全フィールドが裏付けられるfact_idだけaccepted_fact_idsへ返す。rejectionsに他の全IDと具体的理由を各1文だけ。",
                    {"date_facts": date_facts(target), "claims": chunk_facts}, gate_schema)
                all_ids = {x["fact_id"] for x in chunk_facts}
                accepted = set(checked["accepted_fact_ids"])
                rejected_ids = {x["fact_id"] for x in checked["rejections"]}
                if accepted & rejected_ids or accepted | rejected_ids != all_ids:
                    raise ValueError("claim gate must account for every supplied fact exactly once")
                # Keep indexes stable even when a fact is rejected; never reuse a
                # rejected ID for another fact in a later chunk.
                extracted.extend({**x, "claim_gate_accepted": x["fact_id"] in accepted} for x in chunk_facts)
        is_ny_recap = bool(re.search(r"NY為替概況", unicodedata.normalize("NFKC", source["title"])))
        missing_pairs = [pair for pair in ["USD/JPY", "EUR/USD"] if not any(
            x.get("claim_gate_accepted") and x["record_type"] == "actual" and pair in x["pairs"]
            for x in extracted)] if is_ny_recap else []
        if missing_pairs:
            # One bounded ORIGINAL article, not a merge of all articles or an
            # expansion of the conversation. Recover mandatory pairs lost by
            # general extraction instead of inventing them from other prices.
            literal_names = {"USD/JPY": "ドル円", "EUR/USD": "ユーロドル"}
            missing_pairs = [p for p in missing_pairs if literal_names[p] in source["text"]]
        if missing_pairs:
            core_schema = json.loads(json.dumps(CLAIMS))
            core_schema["properties"]["claims"]["minItems"] = 1
            core_text = source["text"]
            if len(core_text.encode()) > 12000:
                matching = [next((text for text in api.source_chunks(core_text)
                    if literal_names[p] in text), "") for p in missing_pairs]
                core_text = "\n".join(dict.fromkeys(matching))
            extra = api.infer_cached(out, f'source-{source["source_id"]:02}-core-pairs-extract',
                "USD/JPYはドル円、EUR/USDはユーロドル。指定missing_pairsの実際の値動きを1〜3件抽出。"
                "『振幅』『推移』『下げ止まり』も実際の動き。別ペアや将来の価格目標は不可。"
                "quoteは完全一致20〜180文字、event_scope/market_session/record_typeは原文を守る。"
                "JST朝のNY概況は前営業日のNY。資料に記述がないペアは抽出せず空配列。",
                {"date_facts": date_facts(target), "missing_pairs": missing_pairs,
                 "source_title": source["title"], "published_at": source["published_at"], "text": core_text}, core_schema)
            for claim in extra["claims"]:
                if claim["record_type"] != "actual" or not set(claim["pairs"]) & set(missing_pairs):
                    continue
                try:
                    bound = bind_claim(source, claim, len(extracted), target)
                except ValueError:
                    continue
                qc = review_copy(api, out, f'source-{source["source_id"]:02}-core-{len(extracted):02}-review',
                    {"title": "原文の主要ペアの値動き", "statements": [{"text": bound["fact"],
                        "fact_ids": [bound["fact_id"]], "mode": "fact"}]}, [bound], target)
                extracted.append({**bound, "claim_gate_accepted": qc["verdict"] == "PASS"})
        facts.extend(extracted)
        news.save(out / "claims.json", facts)
    if len([x for x in facts if x["event_scope"] == "previous" and x["claim_gate_accepted"]]) < 5:
        raise ValueError("previous-session facts insufficient; do not fill from today's Tokyo")
    return facts


def pick(api, out, label, topic, candidates, target, max_facts=5):
    selection_schema = news.schema({"fact_ids": {"type": "array", "items": news.STRING, "minItems": 0, "maxItems": max_facts}})
    slim = [{k: v for k, v in x.items() if k not in {"source_context", "source_url", "source_title"}} for x in candidates]
    groups = api.evidence_batches(slim, 10500)
    selected = []
    for i, group in enumerate(groups):
        choice = api.infer_cached(out, f"{label}-{i:02}-plan",
            "指定トピックに直結する根拠だけ選ぶ。同じ価格の重複は省き、出来事→実際の反応→理由の組を残す。"
            "本日/先週の出来事を前日に変えない。fact_idsは入力にあるものだけ。該当根拠がなければ空配列。",
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
    # A topic is one consumer, never the master list. Keep accepted unused
    # facts available to every editorial role, with their dates/types intact.
    material = [x for x in facts if x.get("claim_gate_accepted") and
                x.get("event_scope") in {"previous", "current", "historical", "future"}]
    for i, event in enumerate(calendar["events"]):
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
    parts = re.split(r"(?=▼\s*\d{1,2}月\d{1,2}日)" if "▼" in text else r"(?=・)", text)
    return [x.strip() for x in parts if x.strip() and "その他、注目点及び懸念点など" != x.strip()][:18]


def role_evidence(key, material, topics):
    by_id = {x["fact_id"]: x for x in material}
    ordered_ids = list(dict.fromkeys(x for topic in topics for x in topic["claim_ids"]))
    n = [by_id[x] for x in ordered_ids]
    cal = [x for x in material if x["fact_id"].startswith("C")]
    key_cal = [x for x in cal if re.search(r"RBA|記者会見|JOLTS|消費者信頼感", x["fact"])]
    themes = [x for x in material if x["fact_id"].startswith("D")]
    weekly = [x for x in material if x["fact_id"].startswith("W")]
    ranks = [x for x in material if x["fact_id"].startswith("R")]
    if key == "headline":
        chosen = n[:1] + key_cal[:1]
    elif key == "hero":
        chosen = n[:2] + key_cal[:1] + themes[:1]
    elif key == "summary":
        chosen = [by_id[x] for topic in topics for x in topic["claim_ids"][:2]][:8]
    elif key == "market":
        chosen = n[:4] + themes[:2]
    elif key == "handover":
        euro = [x for x in cal if re.search(r"KOF|ナーゲル", x["fact"])]
        chosen = key_cal[:2] + euro[:1] + key_cal[2:4] + themes[:1]
    elif key == "focus":
        chosen = ranks[:3] + n[:2] + key_cal[:1]
    elif key == "risk":
        chosen = n[:2] + key_cal[:4] + themes[:1]
    else:
        chosen = weekly[1:4] if len(weekly) > 1 else weekly + themes[:2]
    return list({x["fact_id"]: x for x in chosen}.values())


ROLE_PURPOSES = {
    "hero": "前日の最大の変化と本日の最重要材料。短い導入",
    "headline": "本日を特徴づける最重要材料。一言",
    "summary": "前日の主要出来事の全体像。円・ドル・欧州政策/米金利等の異なる材料を関連づける",
    "market": "市場環境。金利/政策/地政学/フローの対立と本日の方向判断条件。振り返りの再列挙ではない",
    "handover": "本日への引継ぎ。アジア/欧州/NYごとに予定→結果/発言の何を見る→どの通貨の判断が変わるか",
    "focus": "ランキングと当日の実際の材料を結び、一通貨ペアの条件付き観察を説明",
    "risk": "主要リスク。政策/指標/介入/金利/フローの変化でどの判断が崩れるかを説明",
    "points": "本文以外の具体的焦点。週間予定と月末フロー等。ニュースの反復を避ける",
}


def shared_role_evidence(api, out, key, material, target, topics=None):
    # Catalogs contain facts only; original quotations are loaded by selected
    # IDs for authoring/review. Every batch is visited, no first-N truncation.
    catalog = [{k: x[k] for k in ["fact_id", "fact", "record_type", "event_scope"] if k in x}
               for x in material]
    selected = []
    anchors = role_evidence(key, material, topics) if topics else []
    anchor_ids = list(dict.fromkeys(x["fact_id"] for x in anchors))[:8]
    remaining = 8 - len(anchor_ids)
    schema = news.schema({"fact_ids": {"type": "array", "items": news.STRING, "maxItems": 8}})
    for i, batch in enumerate(api.evidence_batches(catalog, 9000)):
        batch_schema = json.loads(json.dumps(schema))
        batch_schema["properties"]["fact_ids"]["items"] = {"type": "string", "enum": [x["fact_id"] for x in batch]}
        choice = api.infer_cached(out, f"shared-{key}-scan-{i:02}",
            "これは執筆ではなく材料選別だけ。roleを実現する重要事実を最大8件選ぶ。"
            "ニュース本文に未採用の事実も同等に評価する。価格だけでなく発言/金利/背景/予定を残す。"
            "同一出来事の重複は省く。historicalは過去の背景であり前日の出来事ではない。"
            "本日の条件分析に必要な前日背景と当日予定を組で残す。該当材料のないbatchのみ空配列。IDは入力限定。",
            {"role": ROLE_PURPOSES[key], "date_facts": date_facts(target), "facts": batch,
             "already_fixed_fact_ids": anchor_ids,
             "rule": "必須の前日材料/当日予定は別に保持。追加の重要材料を選ぶ。過去背景だけで主材料を置き換えない"}, batch_schema)["fact_ids"]
        allowed = {x["fact_id"] for x in batch}
        if not set(choice) <= allowed:
            raise ValueError("shared role scan returned invalid fact ID")
        selected.extend(x for x in choice if x not in selected and x not in anchor_ids)
    if remaining == 0:
        selected = []
    if len(selected) > remaining:
        reduce_schema = news.schema({"fact_ids": {"type": "array", "items": news.STRING, "maxItems": remaining}})
        pool = [x for x in catalog if x["fact_id"] in selected]
        # Progressive bounded reduction, without merging original articles.
        for round_no in range(5):
            reduced = []
            for i, batch in enumerate(api.evidence_batches(pool, 9000)):
                batch_schema = json.loads(json.dumps(reduce_schema))
                batch_schema["properties"]["fact_ids"]["items"] = {"type": "string", "enum": [x["fact_id"] for x in batch]}
                choice = api.infer_cached(out, f"shared-{key}-reduce-{round_no}-{i}",
                    f"roleの必須根拠とは別に、追加を最大{remaining}件へ絞る。日時を保ち、出来事/背景/当日予定の組を優先。"
                    "ニュース以外の具体的材料を落とさず、同じ話の重複を除く。入力IDのみ。",
                    {"role": ROLE_PURPOSES[key], "facts": batch,
                     "fixed_facts": [x for x in catalog if x["fact_id"] in anchor_ids]}, batch_schema)["fact_ids"]
                if not set(choice) <= {x["fact_id"] for x in batch}:
                    raise ValueError("shared role reduction returned invalid fact ID")
                reduced.extend(x for x in choice if x not in reduced)
            pool = [x for x in pool if x["fact_id"] in reduced]
            if len(pool) <= remaining:
                break
        if len(pool) > remaining:
            raise ValueError("shared role evidence reduction did not converge")
        selected = [x["fact_id"] for x in pool]
    selected = anchor_ids + selected
    if not selected:
        raise ValueError(f"{key}: shared material selection empty")
    by_id = {x["fact_id"]: x for x in material}
    news.save(out / "stages" / f"shared-{key}-allocation.json",
              {"candidate_count": len(catalog), "fixed_fact_ids": anchor_ids,
               "fact_ids": selected, "scope": "all accepted shared facts; role anchors cannot be dropped"})
    return [by_id[x] for x in selected]


def review_editorial_quality(api, out, key, draft, evidence, peers, target, overview=None):
    # Distinct from source correctness: missing analysis/duplication cannot be
    # certified by a quote-existence PASS. A failed quality review is retained.
    return api.infer_cached(out, f"editorial-quality-{key}",
        "記事の編集品質だけを厳しく評価。原文一致だけでPASSにしない。"
        "roleを実現しているか、重要材料を具体的に扱ったか、他欄と同じ事実の羅列になっていないかを検査。"
        "summaryは相場全体の整理、marketは相反する材料と方向判断条件、handoverは予定の一覧ではなく"
        "何の変化でどの通貨の判断が変わるか、focus/riskは条件と観察点が必要。"
        "既存事実からの条件付き分析は許容、価格目標/ニュース/実現済み結果の創作は不可。"
        "hero/headlineは短文なので分析を無理に要求しない。予定・背景の共通言及自体は反復違反ではない。"
        "同じ内容を言い換えるだけ、一般論だけ、材料はあるのに要点を落とす場合はFAIL。具体的理由を返す。",
        {"role": ROLE_PURPOSES[key], "date_facts": date_facts(target),
         "draft": {"title": draft["title"], "body": draft["body"]},
         "available_facts": [{"fact_id": x["fact_id"], "fact": x["fact"]} for x in evidence],
         "global_overview": overview or {},
         "scope_rule": "全体像は構成の参考。欄の役割に不要なテーマや未取得材料を必須にしない。要約だけを事実根拠にしない",
         "other_sections": {k: v["body"][:420] for k, v in peers.items() if k != key}}, news.QC_SCHEMA)


def improve_editorial(api, out, key, purpose, evidence, peers, target, length, overview=None):
    """Keep a source-PASS original if OPTIONAL quality repair corrupts facts.

    This is a REJECTED shadow artifact, not a passing substitute or model
    fallback. Initial author/source failures still propagate and stop the run.
    """
    extra = {"overview": overview} if overview else {}
    draft = author(api, out, f"grounded-editorial-{key}", purpose, evidence, target, length, **extra)
    quality = review_editorial_quality(api, out, key, draft, evidence, peers, target, **extra)
    if quality["verdict"] == "FAIL":
        news.save(out / "stages" / f"editorial-quality-{key}-first-rejected.json", {"draft": draft, "quality": quality})
        try:
            improved = author(api, out, f"grounded-editorial-{key}-quality-repair",
                purpose + "。編集指摘を改善: " + quality["reason"], evidence, target, length, **extra)
        except ValueError as error:
            if "original-context review failed after one repair" not in str(error):
                raise
            # Never use the failed enhancement. Keep the same run's already
            # source-checked original, and force quality failure transparently.
            draft["quality_repair_rejected"] = True
            draft["rejected_quality_repair_reason"] = str(error)
            news.save(out / "stages" / f"editorial-quality-{key}-source-rejected-repair.json",
                {"safe_original": draft, "quality": quality, "repair_error": str(error),
                 "action": "retained source-PASS original for REJECTED shadow only", "publish_ready": False})
        else:
            draft = improved
            quality = review_editorial_quality(api, out, key, draft, evidence, peers, target, **extra)
    draft["quality_review"] = quality
    return draft


def material_coverage(api, out, material, topics, editorial, target):
    catalog = [{"fact_id": x["fact_id"], "fact": x["fact"], "event_scope": x.get("event_scope", "current")}
               for x in material]
    used = {x for t in topics for x in t["claim_ids"]}
    used.update(x for v in editorial.values() for x in v["claim_ids"])
    reviews = []
    for i, batch in enumerate(api.evidence_batches(catalog, 9000)):
        reviews.append(api.infer_cached(out, f"material-coverage-{i:02}",
            "材料網羅だけを検査。記事未使用の事実に、本日/前日の主要な政策発言/米金利/相場反応/重要予定が"
            "残っていないか。全事実使用は不要、historical/重複/枝葉は除外。"
            "同じ主題が別IDで既に使われたなら欠落にしない。採用記事にない新しい主要材料があればFAIL。"
            "日付の違う出来事を同一視しない。不足は原資料のfact_idと内容を具体的に返す。",
            {"date_facts": date_facts(target), "facts": batch, "used_fact_ids": sorted(used & {x["fact_id"] for x in batch}),
             "covered_topics": [x["title"] for x in topics],
             "covered_facts": [x["fact"] for x in material if x["fact_id"] in used][:35]}, news.QC_SCHEMA))
    result = {"verdict": "PASS" if all(x["verdict"] == "PASS" for x in reviews) else "FAIL",
              "reviews": reviews, "available_facts": len(material), "used_facts": len(used),
              "unused_fact_ids": [x["fact_id"] for x in material if x["fact_id"] not in used]}
    news.save(out / "material-coverage.json", result)
    return result


def news_candidates(api, out, prior, target):
    fields = ["fact_id", "kind", "fact", "event_date", "market_session", "pairs", "record_type"]
    pool = [{k: x[k] for k in fields} for x in prior]
    schema = news.schema({"fact_ids": {"type": "array", "items": news.STRING, "maxItems": 6}})
    for round_no in range(6):
        if len(json.dumps(pool, ensure_ascii=False).encode()) <= 17000:
            return pool
        chosen = []
        for i, batch in enumerate(api.evidence_batches(pool, 8500)):
            ids = api.infer_cached(out, f"news-catalog-{round_no}-{i}",
                "主要出来事の計画用に最大6根拠選別。異なる政策/金利/介入/地政学材料と価格反応・理由の組を優先。"
                "同じクロス円値動きの羅列で枠を埋めない。USD/JPYとEUR/USDの実際の反応も残す。入力IDのみ。",
                {"date_facts": date_facts(target), "facts": batch}, schema)["fact_ids"]
            if not set(ids) <= {x["fact_id"] for x in batch}:
                raise ValueError("news catalog returned invalid ID")
            chosen.extend(x for x in ids if x not in chosen)
        pool = [x for x in pool if x["fact_id"] in chosen]
        if not pool:
            raise ValueError("news catalog selection empty")
    raise ValueError("news catalog did not converge within input budget")


def make_sections(api, sources, calendar, ranking, out, topic_probe=0, hierarchical=False):
    target = date.fromisoformat(calendar["date_jst"])
    facts = extract(api, sources, target, out)
    tree = None
    global_overview = None
    if hierarchical:
        import local_fx_hierarchy as hierarchy
        full_material = editorial_facts(calendar, ranking, facts, [])
        news.save(out / "shared-material.json", {"facts": full_material, "lifecycle": "evidence"})
        tree = hierarchy.build(api, out, full_material, target, date_facts(target))
        global_overview = hierarchy.overview(tree)
    prior = [x for x in facts if x["event_scope"] == "previous" and x["claim_gate_accepted"]]
    plan_schema = news.schema({"topics": {"type": "array", "minItems": 3, "maxItems": 5,
        "items": news.schema({"title": news.STRING, "fact_ids": {"type": "array", "items": news.STRING, "minItems": 1, "maxItems": 6}})}})
    plan_data = news_candidates(api, out, prior, target)
    plan = api.infer_cached(out, "grounded-news-plan", "前営業日の主要出来事を3〜5件、重要順で選ぶ。"
        "通貨別の羅列ではなく出来事単位。相場反応と理由のある具体的材料を優先。同じ材料を反復しない。"
        "介入発言とNYの戻しは一つの話題へまとめる。ドル円/ユーロドルの実際の値動きは落とさない。"
        "資料にない出来事は作らず、fact_idsは入力のみ。",
        {"date_facts": date_facts(target), "facts": plan_data, "global_overview": global_overview or {}}, plan_schema)
    topics = []
    for i, topic in enumerate(plan["topics"][:topic_probe or 5]):
        if any(x not in {f["fact_id"] for f in prior} for x in topic["fact_ids"]):
            raise ValueError("news plan selected non-previous or invalid fact")
        evidence = [x for x in prior if x["fact_id"] in topic["fact_ids"]]
        draft = author(api, out, f"grounded-topic-{i:02}",
                       f'前営業日の振り返り「{topic["title"]}」。何が起き、価格がどう動き、なぜ動いたかを説明',
                       evidence, target, "250〜450", **({"overview": global_overview} if global_overview else {}))
        draft["source_ids"] = sorted({x["source_id"] for x in evidence})
        topics.append(draft)
        news.save(out / "news.json", {"topics": topics, "publish_ready": False})
    if topic_probe:
        return {"topics": topics, "probe_only": True}
    material = editorial_facts(calendar, ranking, facts, topics)
    news.save(out / "shared-material.json", {"facts": material, "lifecycle": "evidence",
        "rule": "accepted source facts are retained regardless of news-topic selection; dates/types unchanged"})
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
        evidence = (hierarchy.allocate(api, out, key, material, target, date_facts(target), tree, purpose)
                    if hierarchical else shared_role_evidence(api, out, key, material, target, topics))
        if key in {"hero", "headline"}:
            purpose += "。最重要材料を短く。独立した材料を無理に同じ因果へ結ばない。予定/予想と実際の反応は分ける"
        else:
            purpose += "。材料→価格/金利への作用→本日の条件を役割に合わせて整理。予定だけの羅列や他欄の言い換えにしない"
        draft = improve_editorial(api, out, key, purpose, evidence, editorial, target, length,
                                 **({"overview": global_overview} if global_overview else {}))
        editorial[key] = draft
        news.save(out / "editorial-progress.json", editorial)
    # Recheck all fields against the FINAL peers, not merely preceding fields.
    for key, draft in editorial.items():
        evidence = [x for x in material if x["fact_id"] in draft["claim_ids"]]
        final_review = review_editorial_quality(api, out, key, draft, evidence, editorial, target,
                                              **({"overview": global_overview} if global_overview else {}))
        if draft.get("quality_repair_rejected"):
            draft["quality_review"] = {"verdict": "FAIL", "reason": draft["rejected_quality_repair_reason"],
                                       "final_assessment": final_review}
        else:
            draft["quality_review"] = final_review
    coverage = material_coverage(api, out, material, topics, editorial, target)
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
              "editorial_reviews": {k: x["review"] for k, x in editorial.items()}, "grounded_editorial": editorial,
              "editorial_quality_reviews": {k: x["quality_review"] for k, x in editorial.items()}, "material_coverage": coverage}
    news.save(out / "sections.json", result)
    return result
