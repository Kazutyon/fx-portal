"""GALLERIA/Qwen daily shadow runner. keep; run artifacts are retained evidence.

The public AUXEN report is fetched only for comparison AFTER generation. This
runner has no public-write, git, push, or model fallback implementation.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import html
import json
import msvcrt
import os
import re
import sys
import time
import urllib.request
from urllib.error import HTTPError
from decimal import Decimal
from datetime import date, datetime, time as daytime, timedelta
from pathlib import Path
from urllib.parse import urlparse

import local_fx_news as news
import local_fx_claude_sources as claude_sources

ROOT, JST = news.ROOT, news.JST
HOSTS = {"fx.minkabu.jp", "zai.diamond.jp", "kissfx.com", "nfs.faireconomy.media",
         "auxen.jp", "www.rba.gov.au", "www.gaitame.com"}
FLAGS = {"JPY": "🇯🇵", "USD": "🇺🇸", "EUR": "🇪🇺", "GBP": "🇬🇧", "AUD": "🇦🇺",
         "NZD": "🇳🇿", "CAD": "🇨🇦", "CHF": "🇨🇭"}
COUNTRIES = {"日": "JPY", "米": "USD", "欧": "EUR", "独": "EUR", "仏": "EUR", "西": "EUR",
             "英": "GBP", "豪": "AUD", "NZ": "NZD", "加": "CAD", "ス": "CHF"}
FORBIDDEN = r"要確認|再確認|取得失敗|OpenClaw|NO_REPLY|シャドー|データ取得"


def mirror_enabled() -> bool:
    config = load(ROOT / "tools" / "claude_mirror_shadow.json")
    return (config.get("acquisition_mode") == "claude-mirror"
            and config.get("internal_source_policy_exception") is True
            and config.get("publish") is False
            and config.get("model") == news.MODEL
            and config.get("num_ctx") == 65536
            and config.get("model_fallback") is False)


def fetch(url: str) -> str:
    if urlparse(url).hostname not in HOSTS:
        raise ValueError("source is outside allowlist")
    if urlparse(url).hostname in {"fx.minkabu.jp", "kissfx.com"} and not mirror_enabled():
        raise ValueError("automatic acquisition is not approved; provide a dated local input snapshot (ECONOMIC-CALENDAR-SOURCE-AUDIT.md)")
    # Use urllib's transparent default client identification, not a custom agent
    # string rejected by RBA's public site. No browser impersonation or proxy.
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request, timeout=25)
    except HTTPError as error:
        # One bounded FF backoff, as in Claude's run; never bypass a refusal.
        if error.code != 429 or urlparse(url).hostname != "nfs.faireconomy.media":
            raise
        retry_after = error.headers.get("Retry-After", "20")
        if not retry_after.isdigit() or int(retry_after) > 30:
            raise
        error.close()
        time.sleep(max(1, int(retry_after)))
        response = urllib.request.urlopen(request, timeout=25)
    with response:
        if urlparse(response.url).hostname not in HOSTS:
            raise ValueError("redirect outside allowlist")
        raw = response.read(1000001)
        if len(raw) > 1000000:
            raise ValueError("source exceeds response byte budget")
        return raw.decode(response.headers.get_content_charset() or "utf-8")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def snapshot(out: Path, label: str, url: str) -> str:
    path = out / "sources" / f"{label}.json"
    if path.exists():
        value = load(path)
        if value["url"] != url or hashlib.sha256(value["body"].encode()).hexdigest() != value["sha256"]:
            raise ValueError(f"cached {label} URL/hash mismatch")
        return value["body"]
    try:
        print(f"SOURCE {label} FETCH", flush=True)
        body = fetch(url)
    except Exception as error:
        raise ValueError(f"{label} ({url}): {error}") from error
    news.save(path, {"url": url, "fetched_at": datetime.now(JST).isoformat(), "body": body,
                    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(), "lifecycle": "evidence"})
    return body


def collect_news(target: date, out: Path) -> list[dict]:
    bundle_path = out / "source-bundle.json"
    if not bundle_path.exists():
        if not mirror_enabled():
            raise ValueError("dated local news input bundle is required")
        claude_sources.collect(target, out, snapshot)
    bundle = load(bundle_path)
    if bundle.get("date_jst") != target.isoformat():
        raise ValueError("news bundle has wrong date")
    sources = bundle["sources"]
    if not 5 <= len(sources) <= 12 or len({s["source_url"] for s in sources}) != len(sources):
        raise ValueError("news source count/uniqueness gate failed")
    cutoff = datetime.combine(target, daytime(7), JST)
    if bundle.get("acquisition_mode") == "claude-mirror":
        cutoff = datetime.fromisoformat(bundle["as_of_jst"])
        if cutoff.tzinfo is None or cutoff.astimezone(JST).date() != target or cutoff > datetime.now(JST):
            raise ValueError("invalid live news acquisition cutoff")
    for i, source in enumerate(sources):
        if source["source_id"] != i or datetime.fromisoformat(source["published_at"]) > cutoff:
            raise ValueError("news source ID/cutoff gate failed")
        if hashlib.sha256(source["text"].encode()).hexdigest() != source["sha256"]:
            raise ValueError("news source hash mismatch")
    return sources


def parse_kiss(page: str, target: date) -> list[dict]:
    events, current_time = [], None
    for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", page, re.S):
        cells = re.findall(r"<td\b([^>]*)>(.*?)</td>", row, re.S)
        timed = next((news.plain(value) for _, value in cells if re.fullmatch(r"\d{2}:\d{2}", news.plain(value))), None)
        title_index = next((i for i, (attr, _) in enumerate(cells) if re.search(r'class="[^"]*\btitle\b', attr)), None)
        if timed:
            current_time = timed
        if title_index is None:
            # Second line of a rowspanned m/m + y/y release.
            values = [news.plain(body) for _, body in cells]
            if events and "[前月比/前年比]" in events[-1]["name"] and len(values) == 2 and not timed:
                parent = events[-1]
                parent["name"] = parent["name"].replace("[前月比/前年比]", "[前月比]")
                events.append({**parent, "name": parent["name"].replace("[前月比]", "[前年比]"),
                               "forecast": values[0], "previous": values[1]})
            continue
        if not current_time:
            continue
        markup = cells[title_index][1].split("→")[0]
        name = news.plain(markup)
        country_match = re.match(r"(NZ|[日米欧独仏西英豪加ス])\)", name)
        if country_match:
            country = COUNTRIES[country_match.group(1)]
            name = name[country_match.end():].strip()
        elif events and name.startswith("↑・"):
            country, name = events[-1]["country"], name[2:]
        else:
            continue
        rank_i = next((i for i, (attr, _) in enumerate(cells) if "rank" in attr), title_index)
        values = [news.plain(body) for _, body in cells[rank_i + 1:]]
        hour, minute = map(int, current_time.split(":"))
        when = datetime.combine(target, daytime(), JST) + timedelta(hours=hour, minutes=minute)
        grade = "high" if ("bg-orange" in row or "icon-aa" in row) else "medium" if ("icon-bb" in row or "icon-maru2" in row) else "low"
        events.append({"time_jst": current_time, "datetime_jst": when.isoformat(), "country": country,
                       "name": name, "importance": grade, "forecast": values[0] if len(values) >= 2 else "—",
                       "previous": values[1] if len(values) >= 2 else "—", "source": "kissfx"})
    if not events:
        raise ValueError("KissFX economic table parser produced no events")
    return events


def event_code(name: str) -> str:
    pairs = [(r"Cash Rate|政策金利", "rba-rate"), (r"Rate Statement|声明発表", "rba-statement"),
             (r"Press Conference|記者会見", "rba-press"), (r"KOF", "kof"),
             (r"Consumer Confidence|消費者信頼感", "confidence"), (r"JOLTS|求人", "jolts"),
             (r"Case.Shiller|S.P/CS|ケース.シラー", "case-shiller"), (r"HPI|住宅価格指数", "housing"),
             (r"GDP", "gdp"), (r"Mann|マンMPC", "mann"),
             (r"Mortgage Approvals|住宅ローン承認", "mortgage-approvals"),
             (r"M4 Money Supply|マネーサプライM4", "m4"),
             (r"Bowman|ボウマン", "bowman"), (r"Barr\b|バーFRB", "barr"),
             (r"Williams|ウィリアムズ", "williams"), (r"Waller|ウォラー", "waller"),
             (r"Goolsbee|グールズビー", "goolsbee"), (r"Musalem|ムサレム", "musalem"),
             (r"Taylor|テイラー", "taylor"), (r"Nagel|ナーゲル", "nagel")]
    code = next((code for pattern, code in pairs if re.search(pattern, name, re.I)), name.casefold())
    return code + "-yy" if "[前年比]" in name or "y/y" in name else code


def numeric_value(text: str):
    text = text.replace("±", "").replace("−", "-").replace("－", "-").replace(",", "")
    found = re.findall(r"([+-]?\d+(?:\.\d+)?)(%|千件|万件|億|[KMB])?", text)
    if not found:
        return None
    value, unit = found[-1]
    multiplier = {"千件": 1000, "万件": 10000, "億": 100000000,
                  "K": 1000, "M": 1000000, "B": 1000000000}.get(unit, 1)
    return Decimal(value) * multiplier


def collect_calendar(target: date, out: Path) -> dict:
    staged = out / "calendar.input.json"
    if staged.exists():
        value = load(staged)
        if value.get("date_jst") != target.isoformat() or not value.get("events"):
            raise ValueError("calendar input date/completeness mismatch")
        news.save(out / "calendar.json", value)
        return value
    kiss_url = f"https://kissfx.com/article/fxdays{target.strftime('%Y%m%d')}.html"
    kiss = snapshot(out, "kissfx", kiss_url)
    ff_url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
    raw = json.loads(snapshot(out, "forexfactory", ff_url))
    start = datetime.combine(target, daytime(), JST)
    finish = start + timedelta(days=1, hours=7)
    ff = []
    for item in raw:
        at = datetime.fromisoformat(item["date"]).astimezone(JST)
        if not start + timedelta(hours=7) <= at < finish:
            continue
        hours = int((at - start).total_seconds() // 3600)
        ff.append({"time_jst": f"{hours:02}:{at.minute:02}", "datetime_jst": at.isoformat(),
                   "country": item["country"], "name": item["title"],
                   "importance": {"High": "high", "Medium": "medium"}.get(item["impact"], "low"),
                   "forecast": item.get("forecast") or "—", "previous": item.get("previous") or "—", "source": "forexfactory"})
    events = parse_kiss(kiss, target)
    matched_ff = set()
    conflicts = []
    for event in events:
        codes = {event_code(event["name"])}
        if "政策金利" in event["name"] and "声明" in event["name"]:
            codes.add("rba-statement")
        candidates = [(i, x) for i, x in enumerate(ff) if x["country"] == event["country"] and event_code(x["name"]) in codes]
        exact = [(i, x) for i, x in candidates if x["time_jst"] == event["time_jst"]]
        event["sources"] = [kiss_url] + ([ff_url] if exact else [])
        event["confirmed"] = bool(exact)
        for i, other in exact:
            matched_ff.add(i)
            if other["importance"] == "high":
                event["importance"] = "high"
            for field in ["forecast", "previous"]:
                left, right = numeric_value(event[field]), numeric_value(other[field])
                if left is not None and right is not None and left != right:
                    conflicts.append({"type": "numeric", "time_jst": event["time_jst"],
                                      "name": event["name"], "field": field,
                                      "kissfx": event[field], "forexfactory": other[field]})
                    # Disagreement belongs in evidence, never a "recheck" note in copy.
                    event[field] = "—"
                elif left is None and right is not None:
                    event[field] = other[field]
        if candidates and not exact:
            conflicts.append({"kiss": event, "ff": [x for _, x in candidates]})
    for i, event in enumerate(ff):
        if i not in matched_ff:
            events.append({**event, "sources": [ff_url], "confirmed": False})
    events.sort(key=lambda x: (x["time_jst"], x["country"], x["name"]))
    # Claude's weekday flow uses KissFX + FF, not mandatory RBA web requests.
    kiss_text = news.plain(re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", kiss, flags=re.S))
    themes_at = kiss_text.find("その他、注目点")
    day_themes = kiss_text[themes_at:themes_at + 2200] if themes_at >= 0 else ""
    weekly_at = next((m.start() for m in re.finditer(r"今週の(?:注目|重要)|週間(?:予定|スケジュール)|週内の", kiss_text)), -1)
    key = [x for x in events if x["importance"] == "high" or event_code(x["name"]) in {"confidence", "jolts", "rba-rate", "rba-press"}]
    result = {"date_jst": target.isoformat(), "events": events, "key_events": key,
              "source_urls": [kiss_url, ff_url],
              "conflicts": conflicts, "holiday_text": "",
              "day_themes": day_themes,
              "weekly_themes": kiss_text[weekly_at:weekly_at + 1800] if weekly_at >= 0 else "",
              "rba_official_excerpt": "", "rba_schedule_excerpt": ""}
    news.save(out / "calendar.json", result)
    return result


def infer_cached(out: Path, label: str, task: str, data, schema: dict) -> dict:
    fingerprint = hashlib.sha256(json.dumps(["qwen-stage-budget-v2", task, data, schema], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    artifact = out / "stages" / f"{label}.json"
    if artifact.exists():
        cached = load(artifact)
        if cached["input_sha256"] == fingerprint:
            print(f"STAGE {label} CACHE", flush=True)
            return cached["value"]
    previous_request = out / "stages" / f"{label}.request.json"
    if previous_request.exists():
        request = load(previous_request)
        previous_hash = hashlib.sha256(json.dumps(request, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        history = {"request": request}
        for suffix in ["response", "metrics"]:
            path = out / "stages" / f"{label}.{suffix}.json"
            if path.exists():
                history[suffix] = load(path)
        if artifact.exists():
            history["artifact"] = load(artifact)
        news.save(out / "stages" / "history" / f"{label}-{previous_hash[:16]}.json", history)
    news.save(out / "progress.json", {"stage": label, "state": "RUNNING", "at": datetime.now(JST).isoformat()})
    print(f"STAGE {label} RUNNING", flush=True)
    value = news.infer(label, task, data, schema, out / "stages")
    news.save(artifact, {"input_sha256": fingerprint, "value": value})
    news.save(out / "progress.json", {"stage": label, "state": "DONE", "at": datetime.now(JST).isoformat()})
    print(f"STAGE {label} DONE", flush=True)
    return value


def source_chunks(text: str) -> list[str]:
    """Keep sentence boundaries and source spelling; avoid lossy one-shot extraction."""
    sentences = re.split(r"(?<=。)", text)
    chunks, current = [], ""
    for sentence in sentences:
        if len(current) >= 350 and len(current + sentence) > 650:
            chunks.append(current)
            current = ""
        current += sentence
    if current:
        if chunks and len(current) < 120:
            chunks[-1] += current
        else:
            chunks.append(current)
    return chunks


def make_sections(sources: list[dict], calendar: dict, ranking: dict, out: Path) -> dict:
    claims = []
    for i, source in enumerate(sources):
        extracted = []
        for part, text in enumerate(source_chunks(source["text"])):
            extracted.extend(infer_cached(out, f"source-{i:02}-part-{part:02}-extract", (
                "この資料の重要な相場材料の事実を2〜6件抽出。価格だけでなく、発言内容・時刻/取引時間帯・原因・条件付き見通しも落とさない。"
                "factは日本語1文、quoteは本文から完全一致する20〜160文字。kindはevent/price/cause/outlook。"
                "実際の価格反応の因果だけcause。予想はoutlook。資料にない因果を補わない。短すぎる引用は禁止。"
            ), {"source_title": source["title"], "source_id": i, "text": text}, news.CLAIM_SCHEMA)["claims"])
        accepted = [c for c in extracted if c["quote"] in source["text"] and 20 <= len(c["quote"]) <= 160]
        rejected = [c for c in extracted if c not in accepted]
        news.save(out / "stages" / f"source-{i:02}-quote-gate.json", {"accepted": accepted, "rejected": rejected})
        if len(accepted) < 2:
            corrected = infer_cached(out, f"source-{i:02}-extract-repair",
                "根拠引用が本文と完全一致する20〜160文字の事実を2〜6件だけ返す。短すぎる引用や変形した引用は不可。価格と予想を区別。",
                {"source": source, "rejected": rejected}, news.CLAIM_SCHEMA)["claims"]
            accepted = [c for c in corrected if c["quote"] in source["text"] and 20 <= len(c["quote"]) <= 160]
        if len(accepted) < 2:
            raise ValueError(f"source {i} has fewer than two grounded claims after repair")
        extracted = accepted
        claims.append({"source_id": i, "source_title": source["title"], "claims": extracted})
        news.save(out / "claims.json", claims)
    plan_schema = news.schema({"topics": {"type": "array", "minItems": 5, "maxItems": 5,
        "items": news.schema({"title": news.STRING, "source_ids": {"type": "array", "items": {"type": "integer"}, "minItems": 1}})}})
    plan_data = [{"source_id": c["source_id"], "source_title": c["source_title"],
                  "facts": [{"kind": x["kind"], "fact": x["fact"]} for x in c["claims"]]} for c in claims]
    plan = infer_cached(out, "news-plan", (
        "前営業日の相場振り返りの5トピックを選ぶ。通貨ペアごとの羅列ではなく出来事単位。"
        "最重要の材料を優先し、ドル円とユーロドルの動き、その背景の中銀発言や金利・原油・地政学を落とさない。"
        "同じ金利/原油の説明を複数トピックに反復しない。景気指標は実際の価格反応を伴う材料より優先度を下げてよい。"
        "同一資料の別の出来事を別トピックに使ってよい。資料にない出来事は選ばない。source_idsは与えた資料番号のみ。"
    ), plan_data, plan_schema)
    topics = []
    for i, topic in enumerate(plan["topics"]):
        ids = topic["source_ids"]
        if not ids or any(type(x) is not int or x not in range(len(sources)) for x in ids):
            raise ValueError("news plan contains invalid source IDs")
        task = (
            "FX日報の振り返り1トピックを日本語で書く。指定の出来事について250〜550文字を目安に、"
            "何が起き、どの価格がどう動き、なぜそうなったかを資料の根拠の範囲で具体的に説明。"
            "文字数不足を一般論で埋めない。同時発生を因果で結ばない。将来の見方は出典の指摘と明示。"
            "内部事情・要確認・再確認を書かない。記事の『きょう』はNY時間と表現し暦日を推測しない。"
            "掲載時刻と出来事の時刻は別。資料がロンドン時間と言う発言をNY時間に移さない。不明な時間帯は書かない。"
            "claim_idsは入力claimsの各source_idを返す。見出しtitleは具体的な出来事。bodyは段落。"
        )
        data = {"topic": topic["title"], "sources": [claims[x] for x in ids],
                "original_materials": [{"source_id": x, "text": sources[x]["text"]} for x in ids]}
        draft = infer_cached(out, f"topic-{i:02}-write", task, data, news.COPY_SCHEMA)
        review_task = "見出しと段落の全ての事実・数字・因果・出来事の時間帯が原資料で裏付けられるかだけ検査。併記された指標を為替の原因にしたらFAIL。掲載がNYでも出来事がロンドンの発言ならNYに変えたらFAIL。NY市場日の表現は掲載日のJSTと異なる場合がある。余計な根拠や勝手な修正をせずPASS/FAILと理由を返す。"
        review_data = {"sources": [sources[x] for x in ids], "draft": draft}
        qc = infer_cached(out, f"topic-{i:02}-review", review_task, review_data, news.QC_SCHEMA)
        if qc["verdict"] != "PASS":
            draft = infer_cached(out, f"topic-{i:02}-repair", task + " 指摘箇所を修正。", {**data, "draft": draft, "review": qc}, news.COPY_SCHEMA)
            qc = infer_cached(out, f"topic-{i:02}-review-repair", review_task, {**review_data, "draft": draft}, news.QC_SCHEMA)
        if re.search(FORBIDDEN, draft["title"] + draft["body"], re.I):
            raise ValueError("internal status leaked into paragraph")
        topics.append({**draft, "source_ids": ids, "review": qc})
        news.save(out / "news.json", {"topics": topics, "publish_ready": False})
    short_topics = [{"title": t["title"], "body": t["body"]} for t in topics]
    key_events = [{k: x[k] for k in ["time_jst", "country", "name", "forecast", "previous"]} for x in calendar["key_events"]]
    editorial = {}
    editorial_data = {"date_jst": calendar["date_jst"], "topics": short_topics,
                      "calendar": key_events, "day_themes": calendar["day_themes"][:2200],
                      "weekly_themes": calendar.get("weekly_themes", "")[:1800]}
    for key, purpose, length in [
        ("hero", "日報冒頭の前営業日の振り返りと本日の焦点", "200〜350"),
        ("headline", "サマリーの具体的な見出し", "80〜140"),
        ("summary", "前営業日の市場全体の振り返りと本日の焦点。個別の材料と価格推移を厚く説明", "500〜800"),
        ("market", "市場環境。原油・金利・当局発言と各通貨の関係、本日の注意条件", "400〜600"),
        ("handover", "本日の引き継ぎ。アジア・欧州・NYの材料と見る条件", "200〜350"),
    ]:
        editorial[key] = infer_cached(out, f"editorial-{key}", (
            f"FX日報の{purpose}だけを書く。日本語{length}文字目安。bodyに段落を返す。"
            "資料の具体的な材料と時刻を整理。当日分析は条件と理由を具体化し、事実と区別する。"
            "資料にない金利や出来事、指標結果を創作しない。内部事情・取得状況・要確認・再確認は禁止。"
        ), editorial_data, news.schema({"body": news.STRING}))["body"]
    focus_data = {"topics": short_topics, "calendar": key_events,
                  "ranking": [{k: v for k, v in item.items() if k != "symbol"} for item in ranking["rankings"][:5]]}
    common = "当日分析は条件付きの見方として説明。数字は入力のまま。資料にない価格予想・金利・出来事、内部事情・要確認・再確認は禁止。"
    focus = infer_cached(out, "focus-pair", common +
        "最注目通貨focus_pairと理由focus_body(200〜350文字)だけ書く。ランキングは変更せず材料の強さも考慮して選ぶ。",
        focus_data, news.schema({"focus_pair": news.STRING, "focus_body": news.STRING}))
    focus.update(infer_cached(out, "focus-risk", common +
        "Market Riskのrisk_levelと具体的理由risk_body(200〜350文字)だけ書く。",
        focus_data, news.schema({"risk_level": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]}, "risk_body": news.STRING})))
    focus.update(infer_cached(out, "focus-points", common +
        "その他注目点3〜5件だけ作る。時刻・数字・観察すべき変化を具体化。各bodyは100〜180文字。",
        focus_data, news.schema({"points": {"type": "array", "minItems": 3, "maxItems": 5,
          "items": news.schema({"title": news.STRING, "body": news.STRING})}})))
    all_copy = json.dumps([editorial, focus], ensure_ascii=False)
    if re.search(FORBIDDEN, all_copy, re.I):
        raise ValueError("internal status leaked into editorial")
    result = {"topics": topics, **editorial, **focus}
    news.save(out / "sections.json", result)
    return result


def esc(text):
    return html.escape(str(text), quote=True)


def render(target: date, sections: dict, calendar: dict, ranking: dict, out: Path) -> str:
    source = (ROOT / "gen_report_20260925.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    joined = next(n.value for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "html" for t in n.targets))
    previous = target - timedelta(days=1)
    while previous.weekday() >= 5:
        previous -= timedelta(days=1)
    weekday = "月火水木金土日"[target.weekday()]
    # Do not turn unresolved/single-source rows into reader-facing "recheck" prose.
    # Retain all rows and disagreements in calendar.json/validation.json instead.
    events = [x for x in calendar["events"] if x["confirmed"]]
    if not events:
        raise ValueError("no confirmed calendar events for reader copy")
    key = calendar["key_events"]
    topics_html = "\n".join(f'<div class="topic"><h4 class="topic-title">{i+1}. {esc(t["title"])}</h4><p>{esc(t["body"])}</p></div>' for i, t in enumerate(sections["topics"]))
    ranks = []
    for r in ranking["rankings"][:5]:
        grade = {"最適": "S", "適": "A", "候補": "B", "見送り": "C", "対象外": "C"}[r["verdict"]]
        trend = {"上昇": ("trend-up", "↑"), "下降": ("trend-down", "↓")}.get(r["direction"], ("trend-range", "→"))
        flags = "".join(FLAGS.get(c, "") for c in r["pair"].split("/"))
        desc = f'第{r["rank"]}位・スコア{r["score"]}・{r["verdict"]} / ADX {r["adx_h4"]} / ADR比 {r["adr_ratio_pct"]}% / {r["direction"]}'
        ranks.append(f'<tr><td><span class="rank-badge rank-{grade.lower()}">{grade}</span></td><td><strong>{esc(r["pair"])} {flags}</strong><br><span style="color:var(--muted);font-size:12px;">{esc(desc)}</span></td><td><span class="{trend[0]}">{trend[1]}</span></td></tr>')
    archive = sorted((p for p in (ROOT / "reports").glob("*.html")
                      if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem) and p.stem < target.isoformat()), reverse=True)[:15]
    ctx = {"TODAY": target.isoformat(), "WEEKDAY": weekday, "HERO_TITLE_SUB": esc(sections["hero"]),
           "SUMMARY_HEADLINE": esc(sections["headline"]), "SUMMARY_BODY": esc(sections["summary"]),
           "TOP_PAIR_BODY": esc(sections["focus_body"]), "RISK_LEVEL": esc(sections["risk_level"]),
           "RISK_BODY": esc(sections["risk_body"]), "KEY_EVENTS_COUNT": f"{len(key)}件",
           "KEY_EVENTS_SUMMARY": esc(" / ".join(f'{x["time_jst"]} {FLAGS.get(x["country"], "")} {x["name"]}' for x in key)),
           "POINTS_EVENTS_HTML": "\n".join(f'<li>{esc(x["time_jst"])} {FLAGS.get(x["country"], "")} {esc(x["name"])}</li>' for x in key),
           "OTHER_POINTS_HTML": "\n".join(f'<li><strong>{esc(x["title"])}</strong>：{esc(x["body"])}</li>' for x in sections["points"]),
           "MARKET_OVERVIEW": esc(sections["market"]), "RANKING_ROWS_HTML": "\n".join(ranks),
           "RANKING_NOTE": f'4Hデイトレ適性ランキング・{esc(ranking["generated_at_jst"])} 時点。スコアはボラティリティ、トレンド、取引コストをもとに算出。',
           "TOPICS_HTML": topics_html, "HANDOVER": esc(sections["handover"]),
           "CAL_ROWS_HTML": "\n".join(f'<tr><td>{esc(x["time_jst"])}</td><td>{FLAGS.get(x["country"], "")} {esc(x["country"])}</td><td>{esc(x["name"])}</td><td>{"★高" if x["importance"] == "high" else "中" if x["importance"] == "medium" else "低"}</td><td>{esc(x["forecast"])}</td><td>{esc(x["previous"])}</td></tr>' for x in events),
           "SIDEBAR_ARCHIVE_HTML": "\n".join(f'<li><a href="../../reports/{p.name}">{p.stem}</a></li>' for p in archive)}
    parts = []
    for value in joined.values:
        if isinstance(value, ast.Constant):
            parts.append(value.value)
        elif isinstance(value, ast.FormattedValue) and isinstance(value.value, ast.Name):
            parts.append(ctx[value.value.id])
        else:
            raise ValueError("template contains unsupported expression")
    report = "".join(parts)
    report = report.replace("本日の経済指標カレンダー（全件）", "本日の経済指標カレンダー（主要予定）")
    report = report.replace("<em>金曜日</em>", f"<em>{weekday}曜日</em>")
    report = report.replace("前日の相場振り返り（2026-09-24）", f"前日の相場振り返り（{previous.isoformat()}）")
    risk_color = {"HIGH": "var(--red,#c0392b)", "MEDIUM": "var(--gold,#c9a84c)", "LOW": "var(--cyan,#22d3ee)"}[sections["risk_level"]]
    report = report.replace(f'<h3 style="color:var(--red,#c0392b)">{esc(sections["risk_level"])}</h3>',
                            f'<h3 style="color:{risk_color}">{esc(sections["risk_level"])}</h3>')
    pair = sections["focus_pair"]
    report = report.replace("USD/JPY 🇺🇸🇯🇵</h3>", f'{esc(pair)} {"".join(FLAGS.get(c, "") for c in pair.split("/"))}</h3>')
    agenda = "本日の主要予定：" + " / ".join(f'{x["time_jst"]} {x["name"]}' for x in key[:3])
    report = re.sub(r'<li>中国（祝日）。.*?</li>', lambda _: f'<li>{esc(agenda)}</li>', report)
    report = report.replace("🚫 本日の市場休場", "📍 本日の市場予定")
    report = report.replace("KissFX × ForexFactory 2ソース照合済み（要確認あり）", "時刻はJST・翌日早朝まで")
    report = re.sub(r'<p style="font-size:11px;color:var\(--muted\);margin-top:12px;">※ 時刻はJST。.*?</p>',
                    '<p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。24時以降は翌日早朝。予想値は市場予想であり発表結果ではありません。出典：KissFX、Forex Factory。</p>', report, flags=re.S)
    report = re.sub(r'<script data-goatcounter=.*?</script>', '', report, flags=re.S)
    report = report.replace('href="../', 'href="../../').replace('src="../', 'src="../../')
    # Archive paths were already two levels deep before the generic replacement.
    report = report.replace("../../../reports/", "../../reports/")
    policy_path = out / "policy.json"
    if policy_path.exists():
        policy = load(policy_path)
        if policy["date_jst"] != target.isoformat():
            raise ValueError("dated policy input mismatch")
        policy_as_of = policy.get("source_as_of_jst", policy["date_jst"])
        policy_html = f'<p style="margin-top:16px"><strong>政策金利（{esc(policy_as_of)}時点）：</strong>' + " / ".join(
            f'<a href="{esc(r["source_url"])}" target="_blank" rel="noopener noreferrer">{FLAGS.get(r["currency"], "")} {esc(r["bank"])} {esc(r["rate"])}</a>'
            for r in policy["rates"]) + '</p>'
        report = report.replace(esc(sections["market"]), esc(sections["market"]) + policy_html)
    if target.weekday() == 0:
        # Never silently fake Monday's required rate/sentiment supplement.
        raise ValueError("Monday official-rate/sentiment supplement is not yet implemented")
    (out / "report.html").write_text(report, encoding="utf-8")
    return report


def comparison(target: date, report: str, out: Path) -> dict:
    url = f"https://auxen.jp/reports/{target.isoformat()}.html"
    try:
        baseline = snapshot(out, "auxen-comparison-only", url)
    except ValueError as error:
        value = {"comparison_url": url, "baseline_used_as_generation_input": False,
                 "content_review": "pending", "error": str(error)}
        news.save(out / "comparison.json", value)
        return value
    (out / "baseline.html").write_text(baseline.replace('href="../', 'href="../../').replace('src="../', 'src="../../'), encoding="utf-8")
    def stats(text):
        calendar_section = re.search(r'id="calendar".*?<table[^>]*>(.*?)</table>', text, flags=re.S)
        calendar_rows = len(re.findall(r'<tr\b', calendar_section[1])) - 1 if calendar_section else 0
        return {"visible_chars": len(news.plain(re.sub(r'<script.*?</script>|<style.*?</style>', '', text, flags=re.S))),
                "topics": len(re.findall(r'class="topic"', text)), "calendar_rows": max(0, calendar_rows),
                "flags": len(re.findall(r'[\U0001F1E6-\U0001F1FF]{2}', text)),
                "anchors": {x: f'id="{x}"' in text for x in ["summary", "points", "ranking", "review", "calendar"]}}
    result = {"comparison_url": url, "baseline": stats(baseline), "shadow": stats(report),
              "baseline_used_as_generation_input": False, "content_review": "pending"}
    news.save(out / "comparison.json", result)
    return result


def execute(target: date, out: Path, prepare_only: bool, render_existing: bool = False) -> dict:
    previous_status = out / "status.json"
    if previous_status.exists():
        previous = load(previous_status)
        news.save(out / "status-history" / (re.sub(r"[^0-9A-Za-z]", "-", previous["started_at"]) + ".json"), previous)
    status = {"status": "RUNNING", "date_jst": target.isoformat(), "model": news.MODEL,
              "publish_ready": False, "started_at": datetime.now(JST).isoformat(), "scope": "full daily shadow"}
    status["mode"] = "render_existing_no_llm" if render_existing else "prepare_only" if prepare_only else "generate"
    news.save(out / "status.json", status)
    news.save(ROOT / ".runtime" / "local-fx-shadow" / "latest.json", {**status, "run_dir": str(out)})
    news.save(out / "runner-version.json", {"started_at": status["started_at"],
        "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                  [Path(__file__), Path(news.__file__), Path(claude_sources.__file__), ROOT / "tools" / "claude_mirror_shadow.json"]}})
    try:
        if os.environ.get("COMPUTERNAME", "").upper() != "GALLERIA":
            raise ValueError("wrong host")
        if mirror_enabled() and target.weekday() == 0:
            raise ValueError("Monday Claude rate/sentiment refresh remains unimplemented")
        input_dir = ROOT / "shadow-input" / target.isoformat()
        for name in ["source-bundle.json", "calendar.input.json", "policy.json"]:
            path = input_dir / name
            if path.exists():
                news.save(out / name, load(path))
        sources = collect_news(target, out)
        calendar = collect_calendar(target, out)
        policy_path = out / "policy.json"
        if not policy_path.exists() and mirror_enabled():
            claude_sources.inherit_policy(target, out, snapshot)
        if not policy_path.exists() or load(policy_path).get("date_jst") != target.isoformat():
            raise ValueError("dated official policy input is required before generation")
        ranking = json.loads(snapshot(out, "ranking", "https://auxen.jp/data/daytrade-ranking.json"))
        ranking_at = datetime.fromisoformat(ranking["generated_at_jst"])
        if ranking_at.tzinfo is None or ranking_at > datetime.now(JST) or ranking_at.astimezone(JST).date() > target:
            raise ValueError("ranking timestamp is invalid or from the future")
        today_ranking = ranking_at.astimezone(JST).date() == target
        if not today_ranking and not mirror_enabled():
            raise ValueError("ranking is not from the report day")
        if len(ranking["rankings"]) < 5:
            raise ValueError("ranking contains fewer than five pairs")
        news.save(out / "market.json", {"ranking": ranking, "source_url": "https://auxen.jp/data/daytrade-ranking.json",
                                       "today_ranking": today_ranking, "ranking_stale": not today_ranking})
        if prepare_only:
            status["status"] = "PREPARED"
        else:
            sections = load(out / "sections.json") if render_existing else make_sections(sources, calendar, ranking, out)
            report = render(target, sections, calendar, ranking, out)
            comparison(target, report, out)
            checks = {"five_topics": len(sections["topics"]) == 5,
                      "required_anchors": all(f'id="{x}"' in report for x in ["summary", "points", "ranking", "review", "calendar"]),
                      "no_internal_status": not bool(re.search(FORBIDDEN, report, re.I)),
                      "calendar_nonempty": bool(calendar["events"]), "today_ranking": today_ranking,
                      "topic_source_reviews": all(t["review"]["verdict"] == "PASS" for t in sections["topics"])}
            quality = {"checks": checks, "calendar_conflicts": calendar["conflicts"],
                       "single_source_calendar_rows": [x for x in calendar["events"] if not x["confirmed"]],
                       "human_review": "pending", "publish_ready": False,
                       "displayed_calendar_rows": sum(bool(x["confirmed"]) for x in calendar["events"]),
                       "ranking_after_0700": datetime.fromisoformat(ranking["generated_at_jst"]) > datetime.combine(target, daytime(7), JST)}
            news.save(out / "validation.json", quality)
            if not all(value for key, value in checks.items() if key not in {"topic_source_reviews", "today_ranking"}):
                raise ValueError("structural gate failed")
            status.update(status="SHADOW_COMPLETE_REVIEW_PENDING", report=str(out / "report.html"),
                          quality="pending", news_sources=len(sources), calendar_rows=len(calendar["events"]))
    except Exception as error:
        status.update(status="FAILED", error=f"{type(error).__name__}: {error}")
    status["finished_at"] = datetime.now(JST).isoformat()
    news.save(out / "status.json", status)
    news.save(ROOT / ".runtime" / "local-fx-shadow" / "latest.json", {**status, "run_dir": str(out)})
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", type=date.fromisoformat, default=datetime.now(JST).date())
    parser.add_argument("--run-dir", type=Path)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--render-existing", action="store_true", help="rebuild presentation from the same dated retained text; no LLM calls")
    args = parser.parse_args()
    out = args.run_dir or ROOT / "shadow-output" / f"{args.date}-local-daily"
    out = out.resolve()
    if not out.is_relative_to((ROOT / "shadow-output").resolve()):
        raise ValueError("run directory must be under shadow-output")
    out.mkdir(parents=True, exist_ok=True)
    lock_path = ROOT / ".runtime" / "local-fx-shadow" / "runner.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+b") as lock:
        if lock.tell() == 0:
            lock.write(b"0")
            lock.flush()
        lock.seek(0)
        try:
            msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            print("FAIL: another FX shadow runner holds the execution lock", flush=True)
            return 1
        try:
            status = execute(args.date, out, args.prepare_only, args.render_existing)
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
    print(json.dumps({"run_dir": str(out), **status}, ensure_ascii=True), flush=True)
    return 1 if status["status"] == "FAILED" else 0


if __name__ == "__main__":
    sys.exit(main())
