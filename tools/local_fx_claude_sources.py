"""keep: bounded adapters for Claude's public FX sources, shadow only.

Retain code as the project adapter; responses/decisions remain dated evidence.
No models, scheduler, upload, credentials, browser impersonation or fallback.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from datetime import date, datetime, time, timedelta
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import local_fx_news as news

INDEXES = [
    ("zai", "https://zai.diamond.jp/category/zaifxnews", r"/articles/-/\d+"),
    ("minkabu", "https://fx.minkabu.jp/news", r"/news/\d+"),
    ("gaitame", "https://www.gaitame.com/markets/news/", r"/media/entry/[^?#]+"),
]


class ArticleBody(HTMLParser):
    """Capture article/entry-content only; never feed whole navigation to Qwen."""
    def __init__(self, include_main_contents=False):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.capture_depth = None
        self.parts = []
        self.blocked = 0
        self.include_main_contents = include_main_contents
        self.suppressed_depths = []

    def handle_starttag(self, tag, attrs):
        if tag in {"br", "hr", "img", "meta", "link", "input", "source", "wbr"}:
            return
        self.depth += 1
        attrs = dict(attrs)
        if self.capture_depth is None and (
            "entry-content" in attrs.get("class", "").split()
            or attrs.get("itemprop") == "articleBody"
            or (self.include_main_contents and attrs.get("id") == "main-contents")
        ):
            self.capture_depth = self.depth
        if tag in {"script", "style", "nav"}:
            self.blocked += 1
        if re.search(r"(?:^|\s)(?:prcolumn-|article-hitsuji-chart|centraltanshifx)", attrs.get("class", "")):
            self.suppressed_depths.append(self.depth)

    def handle_endtag(self, tag):
        if tag in {"br", "hr", "img", "meta", "link", "input", "source", "wbr"}:
            return
        if tag in {"script", "style", "nav"}:
            self.blocked = max(0, self.blocked - 1)
        if self.depth == self.capture_depth:
            self.capture_depth = None
        if self.depth in self.suppressed_depths:
            self.suppressed_depths.remove(self.depth)
        self.depth = max(0, self.depth - 1)

    def handle_data(self, data):
        if self.capture_depth is not None and not self.blocked and not self.suppressed_depths:
            self.parts.append(data)


def metadata(page):
    def nodes(value):
        if isinstance(value, list):
            for item in value:
                yield from nodes(item)
        elif isinstance(value, dict):
            yield value
            yield from nodes(value.get("@graph", []))
    for raw in re.findall(r"<script[^>]*application/ld\+json[^>]*>(.*?)</script>", page, re.S):
        try:
            for node in nodes(json.loads(raw)):
                kind = node.get("@type", [])
                if any(k in (kind if isinstance(kind, list) else [kind]) for k in ["NewsArticle", "Article", "BlogPosting"]):
                    return node
        except json.JSONDecodeError:
            continue
    raise ValueError("dated article metadata missing")


def article(url, page):
    if urlparse(url).hostname == "fx.minkabu.jp":
        return news.article(url, page)
    meta = metadata(page)
    published = datetime.fromisoformat(meta["datePublished"].replace("Z", "+00:00"))
    if published.tzinfo is None:
        raise ValueError("article timestamp lacks timezone")
    if urlparse(url).hostname == "zai.diamond.jp":
        body = re.search(r"<!--\s*記事本文\s*-->(.*?)<!--\s*記事本文\s*-->", page, re.S)
        visible = re.search(r"(\d{4})年(\d{2})月(\d{2})日\([^)]*\)(\d{2}):(\d{2})公開", page)
        if not visible:
            raise ValueError("Zai body/publication marker missing")
        published = datetime(*(int(x) for x in visible.groups()), tzinfo=news.JST)
        if body:
            text = news.plain(re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", body[1], flags=re.S))
        else:
            parser = ArticleBody(include_main_contents=True)
            parser.feed(page)
            text = re.sub(r"\s+", " ", " ".join(parser.parts)).strip()
    else:
        parser = ArticleBody()
        parser.feed(page)
        text = re.sub(r"\s+", " ", " ".join(parser.parts)).strip()
    # Articles are extracted in <=650-character stages; don't confuse a whole
    # article storage budget with an individual prompt's 24KB budget.
    if len(text) < 80 or len(text.encode("utf-8")) > 32000:
        raise ValueError("article body missing or exceeds per-article budget")
    return {"source_url": url, "title": html.unescape(meta["headline"]),
            "published_at": published.astimezone(news.JST).isoformat(),
            "metadata_published_at": meta["datePublished"],
            "fetched_at": datetime.now(news.JST).isoformat(), "text": text,
            "sha256": hashlib.sha256(text.encode()).hexdigest()}


def collect(target: date, out, snapshot):
    cutoff = datetime.now(news.JST)
    if target != cutoff.date():
        raise ValueError("live source acquisition only supports today's JST date; use dated input for history")
    previous = target - timedelta(days=1)
    while previous.weekday() >= 5:
        previous -= timedelta(days=1)
    start = datetime.combine(previous, time(), news.JST)
    sources, rejected, seen = [], [], set()
    acquired_domains = []
    for label, index, pattern in INDEXES:
        page = snapshot(out, f"{label}-live-index", index)
        links = []
        for href, markup in re.findall(r'<a\b[^>]*href=["\x27]([^"\x27]+)["\x27][^>]*>(.*?)</a>', page, re.S):
            url = urljoin(index, html.unescape(href)).split("#")[0]
            title = news.plain(markup)
            if urlparse(url).hostname != urlparse(index).hostname or not re.fullmatch(pattern, urlparse(url).path):
                continue
            if url in seen or not title or re.search(r"四本値|ピボット|トレンド一覧", title):
                continue
            seen.add(url)
            links.append((url, title))
        links.sort(key=lambda x: 0 if re.search(r"[ＮN][ＹY]為替|ニューヨーク外国為替市場概況", x[1]) else
                   1 if re.search(r"市場概況|発言|介入|オプション|見通し|ラガルド", x[1]) else 2)
        accepted = 0
        for url, title in links[:30]:
            try:
                body = snapshot(out, f"live-article-{hashlib.sha256(url.encode()).hexdigest()[:16]}", url)
                value = article(url, body)
                at = datetime.fromisoformat(value["published_at"])
                if not start <= at <= cutoff:
                    raise ValueError("article outside previous-session/acquisition-start window")
                if value["sha256"] in {s["sha256"] for s in sources}:
                    continue
                value["source_id"] = len(sources)
                sources.append(value)
                accepted += 1
                if accepted >= 7 or len(sources) >= 24:
                    break
            except (OSError, ValueError, KeyError) as error:
                rejected.append({"url": url, "reason": str(error)})
        acquired_domains.append({"index": index, "accepted": accepted})
    # Few articles or no NY recap make a thinner report, not no report: record it and go on. Only "nothing at all" stops.
    coverage_gaps = []
    if len(sources) < 5:
        coverage_gaps.append(f"取得できた記事が{len(sources)}件だけ(通常は5件以上)")
    if not any(re.search(r"[ＮN][ＹY]為替|ニューヨーク外国為替市場概況", x["title"]) for x in sources):
        coverage_gaps.append("ニューヨーク市場の概況記事が取得できなかった")
    news.save(out / "acquisition-review.json", {"indexes": acquired_domains, "rejected": rejected,
              "coverage_gaps": coverage_gaps, "as_of_jst": cutoff.isoformat(), "lifecycle": "evidence"})
    if not sources:
        raise ValueError("news coverage failed: no dated article could be read")
    news.save(out / "source-bundle.json", {"date_jst": target.isoformat(), "sources": sources,
              "as_of_jst": cutoff.isoformat(), "acquisition_mode": "claude-mirror",
              "strict_0700_backtest": False, "lifecycle": "evidence"})


POLICY_URL = "https://zai.diamond.jp/articles/-/401200"  # ザイFX: 主要各国の政策金利の推移 (a public news site, not our own published report)
POLICY_BANKS = {"USD": "FRB", "GBP": "BOE", "JPY": "日銀", "EUR": "ECB", "AUD": "RBA", "NZD": "RBNZ", "CAD": "BOC", "CHF": "SNB"}


def collect_policy(target, out, snapshot, read):
    """Policy rates from the ザイFX history table. The page is the source of truth, never our published report:
    `read(text)` (the local model) says each bank's latest rate and month as the table writes them; this function only
    checks that every copied number (and note) is really in the page. Banks the model could not read are left out."""
    page = snapshot(out, "policy-rate-history", POLICY_URL)
    text = news.plain(re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", page, flags=re.S))
    published = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', page)
    rates = []
    for item in read(text):
        currency = item.get("currency")
        number = str(item.get("rate", "")).replace("%", "").strip()
        note = str(item.get("note", "")).strip()
        if (currency not in POLICY_BANKS or any(x["currency"] == currency for x in rates) or not number
                or not re.search(r"(?<![\d.])" + re.escape(number) + r"(?![\d.])", text)):
            continue
        rates.append({"bank": POLICY_BANKS[currency], "currency": currency,
                      "rate": f"{number}%" + (f"（{note}）" if note and note in text else ""),
                      "as_of": str(item.get("month", "")), "source_url": POLICY_URL})
    if not rates:
        raise ValueError("no policy rate could be read from the history page")
    news.save(out / "policy.json", {"date_jst": target.isoformat(), "rates": rates,
              "source_as_of_jst": published[1] if published else target.isoformat(),
              "method": "ザイFX 政策金利推移表の最新月の値(表の更新が決定直後より遅れることがある)", "lifecycle": "evidence"})


def supplement_previous(target, out, snapshot, sources):
    """Isolated bounded acquisition from the original public indexes only.

    Preserve existing IDs; append up to six previous-session articles per
    domain. Do not read the published report or bypass a refused request.
    """
    marker = out / "supplement-review.json"
    if marker.exists():
        bundle = json.loads((out / "source-bundle.json").read_text(encoding="utf-8"))
        return bundle["sources"]
    cutoff = datetime.combine(target, time(7), news.JST)
    previous = target - timedelta(days=1)
    while previous.weekday() >= 5:
        previous -= timedelta(days=1)
    start = datetime.combine(previous, time(), news.JST)
    sources = list(sources)
    seen = {x["source_url"] for x in sources}
    rejected, stats = [], []
    for label, index, pattern in INDEXES:
        page = snapshot(out, f"{label}-live-index", index)
        links = []
        for href, markup in re.findall(r'<a\b[^>]*href=["\x27]([^"\x27]+)["\x27][^>]*>(.*?)</a>', page, re.S):
            url = urljoin(index, html.unescape(href)).split("#")[0]
            title = news.plain(markup)
            if (url in seen or urlparse(url).hostname != urlparse(index).hostname
                    or not re.fullmatch(pattern, urlparse(url).path) or not title
                    or re.search(r"四本値|ピボット|トレンド一覧", title)):
                continue
            seen.add(url)
            links.append((url, title))
        links.sort(key=lambda x: 0 if re.search(r"外国為替市場概況|[ＮN][ＹY]為替|金利|利回り|ラガルド|発言|原油|オプション", x[1]) else 1)
        added = 0
        for url, title in links[:24]:
            if len(sources) >= 24:
                break
            try:
                body = snapshot(out, f"live-article-{hashlib.sha256(url.encode()).hexdigest()[:16]}", url)
                value = article(url, body)
                if not start <= datetime.fromisoformat(value["published_at"]) <= cutoff:
                    raise ValueError("not in preceding-session / morning-07 publication window")
                if value["sha256"] in {x["sha256"] for x in sources}:
                    continue
                value["source_id"] = len(sources)
                sources.append(value)
                added += 1
                if added == 6:
                    break
            except (OSError, ValueError, KeyError) as error:
                rejected.append({"url": url, "reason": str(error)})
        stats.append({"index": index, "candidate_links": len(links), "added": added})
    bundle = json.loads((out / "source-bundle.json").read_text(encoding="utf-8"))
    bundle["sources"] = sources
    bundle["supplemented_at_jst"] = datetime.now(news.JST).isoformat()
    news.save(out / "source-bundle.json", bundle)
    news.save(marker, {"lifecycle": "evidence", "indexes": stats, "rejected": rejected,
        "total_sources": len(sources), "new_publication_cutoff": cutoff.isoformat(),
        "original_inputs_may_include_afternoon_articles": True, "baseline_used_as_generation_input": False})
    return sources


def recover_article_formats(target, out, snapshot, sources):
    """Recover previously saved format failures; no forbidden HTTP retries."""
    marker = out / "source-format-supplement-review.json"
    if marker.exists():
        return json.loads((out / "source-bundle.json").read_text(encoding="utf-8"))["sources"]
    previous = target - timedelta(days=1)
    while previous.weekday() >= 5:
        previous -= timedelta(days=1)
    start = datetime.combine(previous, time(), news.JST)
    finish = datetime.combine(target, time(7), news.JST)
    review = json.loads((out / "supplement-review.json").read_text(encoding="utf-8"))
    sources, results = list(sources), []
    for item in review["rejected"]:
        if not re.search(r"body/publication marker missing|body missing or exceeds", item["reason"]):
            continue
        url = item["url"]
        path = out / "sources" / f'live-article-{hashlib.sha256(url.encode()).hexdigest()[:16]}.json'
        if not path.exists() or len(sources) >= 24:
            continue
        try:
            value = article(url, snapshot(out, path.stem, url))
            if not start <= datetime.fromisoformat(value["published_at"]) <= finish:
                raise ValueError("outside preceding-session/morning publication window")
            if value["sha256"] in {x["sha256"] for x in sources}:
                continue
            value["source_id"] = len(sources)
            sources.append(value)
            results.append({"url": url, "accepted_source_id": value["source_id"], "text_chars": len(value["text"])})
        except (ValueError, KeyError) as error:
            results.append({"url": url, "rejected": str(error)})
    bundle = json.loads((out / "source-bundle.json").read_text(encoding="utf-8"))
    bundle["sources"] = sources
    news.save(out / "source-bundle.json", bundle)
    news.save(marker, {"lifecycle": "evidence", "results": results, "total_sources": len(sources),
                      "network_refusal_retried": False, "calendar_rows_not_confirmed_from_same_author": True})
    return sources
