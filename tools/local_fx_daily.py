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
FORBIDDEN = r"要確認|要再確認|再確認(?:が必要|を要する|してください|中|待ち)|取得失敗|OpenClaw|NO_REPLY|シャドー|データ取得|入力資料|提供資料|原資料|根拠不足"


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
    # The FF feed rejects the default urllib agent with 403; use the project's
    # honest identifying agent (same as economic_calendar_forexfactory.py) for that host only.
    headers = {"User-Agent": "AUXEN-FX-Portal-Shadow-Calendar/1.0"} if urlparse(url).hostname == "nfs.faireconomy.media" else {}
    request = urllib.request.Request(url, headers=headers)
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
    if not 5 <= len(sources) <= 24 or len({s["source_url"] for s in sources}) != len(sources):
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
    found = re.findall(r"([+-]?\d+(?:\.\d+)?)(%|千件|万件|千人|万人|億|[KMB])?", text)
    if not found:
        return None
    value, unit = found[-1]
    multiplier = {"千件": 1000, "万件": 10000, "千人": 1000, "万人": 10000, "億": 100000000,
                  "K": 1000, "M": 1000000, "B": 1000000000}.get(unit, 1)
    return Decimal(value) * multiplier


def numeric_resolution(text: str):
    found = re.findall(r"([+-]?\d+(?:\.\d+)?)(%|千件|万件|千人|万人|億|[KMB])?", text.replace(",", ""))
    if not found:
        return None
    value, unit = found[-1]
    multiplier = {"千件": 1000, "万件": 10000, "千人": 1000, "万人": 10000, "億": 100000000,
                  "K": 1000, "M": 1000000, "B": 1000000000}.get(unit, 1)
    decimals = len(value.split(".")[1]) if "." in value else 0
    return Decimal(multiplier) / Decimal(10) ** decimals


def numeric_agreement(left: str, right: str) -> str:
    a, b = numeric_value(left), numeric_value(right)
    if a is None or b is None:
        return "missing"
    if a == b:
        return "exact"
    ra, rb = numeric_resolution(left), numeric_resolution(right)
    # Only treat a coarser display as compatible with a finer value. Two
    # different values at the same precision are a real unresolved difference.
    coarse, fine, resolution = (a, b, ra) if ra > rb else (b, a, rb)
    if ra != rb and coarse - resolution / 2 <= fine < coarse + resolution / 2:
        return "rounding-compatible"
    return "conflict"


def value_pairs(kiss_events: list, ff_rows: list, taken: set) -> dict:
    """Pair KissFX and Forex Factory rows of the same indicator without a per-event name table: same country and
    time, and the previous values agree (or forecast and previous are both within 2%). Only one-to-one pairs
    where neither side has another candidate; anything ambiguous stays unpaired."""
    def close(a, b):
        x, y = numeric_value(a), numeric_value(b)
        return x is not None and y is not None and abs(x - y) <= Decimal("0.02") * max(abs(x), abs(y))

    def same(event, other):
        if numeric_agreement(event["previous"], other["previous"]) in ("exact", "rounding-compatible"):
            return True
        return close(event["forecast"], other["forecast"]) and close(event["previous"], other["previous"])

    wanted = {k: [i for i, f in enumerate(ff_rows) if i not in taken and f["country"] == e["country"]
                  and f["time_jst"] == e["time_jst"] and same(e, f)] for k, e in enumerate(kiss_events)}
    return {k: c[0] for k, c in wanted.items()
            if len(c) == 1 and sum(1 for other in wanted.values() if c[0] in other) == 1}


def weekly_schedule(text: str, target: date) -> str:
    blocks = []
    pattern = r"▼\s*(\d{1,2})月(\d{1,2})日\([月火水木金土日]\)(.*?)(?=▼\s*\d{1,2}月\d{1,2}日|通知機能|★\s*今週|$)"
    for match in re.finditer(pattern, text, re.S):
        month, day = int(match[1]), int(match[2])
        year = target.year + (1 if target.month == 12 and month == 1 else 0)
        at = date(year, month, day)
        if target <= at < target + timedelta(days=7):
            blocks.append(match[0].strip())
    return " ".join(dict.fromkeys(blocks))


def collect_calendar(target: date, out: Path, allow_single_source: bool = False) -> dict:
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
    ff_available = True
    try:
        raw = json.loads(snapshot(out, "forexfactory", ff_url))
    except ValueError as error:
        if not allow_single_source or not re.search(r"HTTP(?: Error)? (?:403|429)\b", str(error)):
            raise
        # Shadow observation may inspect real KissFX material without FF.
        # Never fabricate corroboration or copy another day's FF snapshot.
        news.save(out / "calendar-source-error.json", {
            "source": ff_url, "error": str(error), "date_jst": target.isoformat(),
            "lifecycle": "evidence", "action": "unconfirmed single-source shadow only"})
        raw = []
        ff_available = False
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
    by_name = {i for e in events for i, x in enumerate(ff) if x["country"] == e["country"]
               and x["time_jst"] == e["time_jst"] and event_code(x["name"]) == event_code(e["name"])}
    unnamed = [n for n, e in enumerate(events) if not any(
        x["country"] == e["country"] and x["time_jst"] == e["time_jst"] and event_code(x["name"]) == event_code(e["name"]) for x in ff)]
    by_value = {unnamed[k]: i for k, i in value_pairs([events[n] for n in unnamed], ff, by_name).items()}
    for n, event in enumerate(events):
        codes = {event_code(event["name"])}
        if "政策金利" in event["name"] and "声明" in event["name"]:
            codes.add("rba-statement")
        candidates = [(i, x) for i, x in enumerate(ff) if x["country"] == event["country"] and event_code(x["name"]) in codes]
        exact = [(i, x) for i, x in candidates if x["time_jst"] == event["time_jst"]]
        if not exact and n in by_value:
            exact = [(by_value[n], ff[by_value[n]])]
        event["sources"] = [kiss_url] + ([ff_url] if exact else [])
        event["confirmed"] = bool(exact)
        for i, other in exact:
            matched_ff.add(i)
            if other["importance"] == "high":
                event["importance"] = "high"
            for field in ["forecast", "previous"]:
                left, right = numeric_value(event[field]), numeric_value(other[field])
                agreement = numeric_agreement(event[field], other[field])
                if agreement == "conflict":
                    conflicts.append({"type": "numeric", "time_jst": event["time_jst"],
                                      "name": event["name"], "field": field,
                                      "kissfx": event[field], "forexfactory": other[field]})
                    # Disagreement belongs in evidence, never a "recheck" note in copy.
                    event[field] = "—"
                elif agreement == "rounding-compatible":
                    event.setdefault("rounding_evidence", []).append({"field": field, "kissfx": event[field], "forexfactory": other[field]})
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
    themes_end = kiss_text.find(f"{target.month}月{target.day}日", themes_at + 20) if themes_at >= 0 else -1
    # Keep the theme list, not a slice of navigation + table + legal notices.
    day_themes = kiss_text[themes_at:themes_end if themes_end > themes_at else themes_at + 1100] if themes_at >= 0 else ""
    key = [x for x in events if x["importance"] == "high" or event_code(x["name"]) in {"confidence", "jolts", "rba-rate", "rba-press"}]
    result = {"date_jst": target.isoformat(), "events": events, "key_events": key,
              "source_urls": [kiss_url] + ([ff_url] if ff_available else []),
              "conflicts": conflicts, "holiday_text": "",
              "day_themes": day_themes,
              "weekly_themes": weekly_schedule(kiss_text, target),
              "rba_official_excerpt": "", "rba_schedule_excerpt": ""}
    news.save(out / "calendar.json", result)
    return result


def infer_cached(out: Path, label: str, task: str, data, schema: dict) -> dict:
    fingerprint = hashlib.sha256(json.dumps(["qwen-stage-budget-v3", task, data, schema, news.FORCE_THINK_OFF], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
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


def evidence_batches(records: list[dict], byte_limit: int = 12000) -> list[list[dict]]:
    """Pack grounded fact/quote pairs without ever merging all article bodies."""
    batches, current = [], []
    for record in records:
        candidate = [*current, record]
        if len(json.dumps(candidate, ensure_ascii=False).encode()) > byte_limit:
            if not current:
                raise ValueError("one evidence record exceeds its stage budget")
            batches.append(current)
            current = [record]
        else:
            current = candidate
    if current:
        batches.append(current)
    return batches


def make_sections(sources: list[dict], calendar: dict, ranking: dict, out: Path, topic_probe: int = 0,
                  hierarchical: bool = False, observational: bool = False, oneshot_only: bool = False) -> dict:
    import local_fx_grounding as grounding
    return grounding.make_sections(sys.modules[__name__], sources, calendar, ranking, out, topic_probe, hierarchical, observational, oneshot_only)


def esc(text):
    return html.escape(str(text), quote=True)


def render(target: date, sections: dict, calendar: dict, ranking: dict, out: Path, allow_single_source: bool = False) -> str:
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
    single_source = False
    if not events and allow_single_source:
        # Observation shadow only: show the one available source honestly labelled, never as cross-checked.
        events = list(calendar["events"])
        single_source = True
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
    risk_color = {"HIGH": "var(--red,#c0392b)", "MEDIUM": "var(--gold,#c9a84c)", "LOW": "var(--cyan,#22d3ee)"}.get(sections["risk_level"], "var(--gold,#c9a84c)")
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
    if single_source:
        report = report.replace("出典：KissFX、Forex Factory。", "出典：KissFXのみ（Forex Factoryは取得不可のため未照合・単一ソース）。")
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
    if target.weekday() == 0 and not allow_single_source:
        # Never silently fake Monday's required rate/sentiment supplement (observation reports are never publishable).
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


def execute(target: date, out: Path, prepare_only: bool, render_existing: bool = False, topic_probe: int = 0,
            supplement_news: bool = False, hierarchical: bool = False, observational: bool = False,
            oneshot_only: bool = False) -> dict:
    previous_status = out / "status.json"
    if previous_status.exists():
        previous = load(previous_status)
        news.save(out / "status-history" / (re.sub(r"[^0-9A-Za-z]", "-", previous["started_at"]) + ".json"), previous)
    status = {"status": "RUNNING", "date_jst": target.isoformat(), "model": news.MODEL,
              "publish_ready": False, "started_at": datetime.now(JST).isoformat(), "scope": "full daily shadow"}
    status["mode"] = "render_existing_no_llm" if render_existing else "prepare_only" if prepare_only else "generate"
    status["think_off_experiment"] = news.FORCE_THINK_OFF
    status["hierarchical_experiment"] = hierarchical
    status["observation_shadow"] = observational
    news.save(out / "status.json", status)
    news.save(ROOT / ".runtime" / "local-fx-shadow" / "latest.json", {**status, "run_dir": str(out)})
    news.save(out / "runner-version.json", {"started_at": status["started_at"],
        "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                  [Path(__file__), Path(news.__file__), Path(claude_sources.__file__),
                   ROOT / "tools" / "local_fx_grounding.py", ROOT / "tools" / "local_fx_hierarchy.py",
                   ROOT / "tools" / "local_fx_extract_summary.py",
                   ROOT / "tools" / "local_fx_summary_observation.py",
                   ROOT / "tools" / "claude_mirror_shadow.json"]}})
    try:
        if os.environ.get("COMPUTERNAME", "").upper() != "GALLERIA":
            raise ValueError("wrong host")
        if mirror_enabled() and target.weekday() == 0 and not observational:
            raise ValueError("Monday Claude rate/sentiment refresh remains unimplemented")
        input_dir = ROOT / "shadow-input" / target.isoformat()
        for name in ["source-bundle.json", "calendar.input.json", "policy.json"]:
            path = input_dir / name
            if path.exists():
                news.save(out / name, load(path))
        sources = collect_news(target, out)
        if supplement_news:
            if not mirror_enabled() or render_existing:
                raise ValueError("supplement requires isolated mirror generation, not render-only")
            sources = claude_sources.supplement_previous(target, out, snapshot, sources)
            sources = claude_sources.recover_article_formats(target, out, snapshot, sources)
        calendar = collect_calendar(target, out, allow_single_source=observational)
        policy_path = out / "policy.json"
        if not policy_path.exists() and mirror_enabled():
            claude_sources.inherit_policy(target, out, snapshot, allow_stale_monday=observational)
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
            sections = load(out / "sections.json") if render_existing else make_sections(sources, calendar, ranking, out, topic_probe, hierarchical, observational, oneshot_only)
            if sections is None:  # one-shot only: its own report/checks live under oneshot/
                failure = out / "oneshot" / "error.json"
                status.update(status="FAILED" if failure.exists() else "ONESHOT_COMPLETE_REVIEW_PENDING",
                              report=str(out / "oneshot" / "report.html"), quality="pending", publish_ready=False)
                if failure.exists():
                    status["error"] = load(failure)["error"]
                status["finished_at"] = datetime.now(JST).isoformat()
                news.save(out / "status.json", status)
                news.save(ROOT / ".runtime" / "local-fx-shadow" / "latest.json", {**status, "run_dir": str(out)})
                return status
            if topic_probe:
                status.update(status="TOPIC_PROBE_COMPLETE_REVIEW_PENDING", probe_topics=len(sections["topics"]),
                              quality="pending", publish_ready=False)
                status["finished_at"] = datetime.now(JST).isoformat()
                news.save(out / "status.json", status)
                news.save(ROOT / ".runtime" / "local-fx-shadow" / "latest.json", {**status, "run_dir": str(out)})
                return status
            report = render(target, sections, calendar, ranking, out, observational)
            comparison(target, report, out)
            checks = {"three_to_five_topics": 3 <= len(sections["topics"]) <= 5,
                      "required_anchors": all(f'id="{x}"' in report for x in ["summary", "points", "ranking", "review", "calendar"]),
                      "no_internal_status": not bool(re.search(FORBIDDEN, report, re.I)),
                      "calendar_nonempty": bool(calendar["events"]), "today_ranking": today_ranking,
                      "topic_source_reviews": all(t["review"]["verdict"] == "PASS" for t in sections["topics"]),
                      "editorial_source_reviews": len(sections.get("editorial_reviews", {})) == 8 and all(
                          r["verdict"] == "PASS" for r in sections.get("editorial_reviews", {}).values()),
                      "editorial_quality": len(sections.get("editorial_quality_reviews", {})) == 8 and all(
                          r["verdict"] in ("PASS", "SKIPPED") for r in sections.get("editorial_quality_reviews", {}).values()),
                      "material_coverage": sections.get("material_coverage", {}).get("verdict") in ("PASS", "SKIPPED"),
                      "calendar_coverage_complete": all(x["confirmed"] for x in calendar["events"])}
            quality = {"checks": checks, "calendar_conflicts": calendar["conflicts"],
                       "single_source_calendar_rows": [x for x in calendar["events"] if not x["confirmed"]],
                       "human_review": "pending", "publish_ready": False,
                       "displayed_calendar_rows": sum(bool(x["confirmed"]) for x in calendar["events"]),
                       "ranking_after_0700": datetime.fromisoformat(ranking["generated_at_jst"]) > datetime.combine(target, daytime(7), JST)}
            news.save(out / "validation.json", quality)
            advisory = {"today_ranking", "calendar_coverage_complete", "editorial_quality", "material_coverage"}
            source_checks = {"three_to_five_topics", "no_internal_status", "topic_source_reviews", "editorial_source_reviews"}
            if observational:
                advisory |= source_checks  # never published: flag, keep the page, do not discard it
            if not all(value for key, value in checks.items() if key not in advisory):
                raise ValueError("structure or source-review gate failed")
            failed_source = [x for x in sorted(source_checks) if not checks[x]] if observational else []
            quality["failed_source_checks"] = failed_source
            news.save(out / "validation.json", quality)
            status.update(status="SHADOW_COMPLETE_REVIEW_PENDING", report=str(out / "report.html"),
                          quality="REJECTED_SOURCE_GAPS" if failed_source else
                          "pending" if all(checks[x] for x in ["calendar_coverage_complete", "editorial_quality", "material_coverage"])
                          else "REJECTED_QUALITY_GAPS",
                          news_sources=len(sources), calendar_rows=len(calendar["events"]))
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
    parser.add_argument("--think-off-experiment", action="store_true", help="explicit isolated Qwen experiment; never selected by cron or after failure automatically")
    parser.add_argument("--topic-probe", type=int, choices=[1, 2], default=0, help="generate and review only the first one/two topics; no editorial or report")
    parser.add_argument("--supplement-news", action="store_true", help="isolated extra preceding-session collection; no scheduler change")
    parser.add_argument("--hierarchical-experiment", action="store_true", help="isolated summary-tree trial; no scheduler/default change")
    parser.add_argument("--with-hierarchy", action="store_true", help="observation shadow: also run the slow hierarchical pipeline (about 60 min) after the one-shot")
    parser.add_argument("--observation-shadow", action="store_true", help="bounded free summaries; advisory intermediate/quality review; never publish")
    args = parser.parse_args()
    if args.observation_shadow:
        args.hierarchical_experiment = True
    news.FORCE_THINK_OFF = args.think_off_experiment
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
            status = execute(args.date, out, args.prepare_only, args.render_existing, args.topic_probe,
                             args.supplement_news, args.hierarchical_experiment, args.observation_shadow,
                             args.observation_shadow and not args.with_hierarchy)
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
    print(json.dumps({"run_dir": str(out), **status}, ensure_ascii=True), flush=True)
    return 1 if status["status"] == "FAILED" else 0


if __name__ == "__main__":
    sys.exit(main())
