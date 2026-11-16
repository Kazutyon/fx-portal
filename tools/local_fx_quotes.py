"""Previous-session closes for stocks, commodities and yields (Dow, S&P 500, Nasdaq, Nikkei, gold, WTI, VIX, US 10y, dollar index).

The articles the shadow reads rarely carry these, so the writer never mentioned gold or the Dow. The figures come
from Yahoo Finance chart data (already the source of the day-trade ranking); the model never produces a number.
Failure leaves an empty list and the report is written without them."""
import json
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from local_fx_grounding import previous_day  # the one definition of the report's previous business day

# symbol, name, unit, decimals
INSTRUMENTS = [
    ("^DJI", "NYダウ", "ドル", 2),
    ("^GSPC", "S&P500", "", 2),
    ("^IXIC", "ナスダック総合", "", 2),
    ("^N225", "日経平均", "円", 2),
    ("GC=F", "金先物(1オンス)", "ドル", 1),
    ("CL=F", "WTI原油先物(1バレル)", "ドル", 2),
    ("^VIX", "VIX指数", "", 2),
    ("^TNX", "米10年債利回り", "％", 3),
    ("DX-Y.NYB", "ドルインデックス", "", 3),
]
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=10d&interval=1d"


def fetch_chart(symbol: str) -> dict:
    request = urllib.request.Request(URL.format(symbol=symbol.replace("^", "%5E")), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)["chart"]["result"][0]


def daily_bars(chart: dict) -> list:
    """(local date, close) per session, in the exchange's own calendar. A session whose close is not published yet keeps
    its date with close None, so a later step can tell "no value yet" (the bar exists) from "market closed" (no bar)."""
    offset = timedelta(seconds=chart["meta"].get("gmtoffset", 0))
    closes = chart["indicators"]["quote"][0]["close"]
    return [((datetime.fromtimestamp(ts, timezone.utc) + offset).date(), close)
            for ts, close in zip(chart["timestamp"], closes)]


def quote_fact(name: str, unit: str, decimals: int, bars: list, target: date, symbol: str, index: int) -> dict | None:
    """The last session up to the report's previous business day (the same date every other part of the report uses),
    with its change from the session before. A bar dated after it (a Sunday-evening bar of a 24-hour instrument, or a
    partial session) is never a close, so it cannot be picked; a market closed on that day falls back to its own last session."""
    done = [b for b in bars if b[0] <= previous_day(target)]
    if not done or done[-1][1] is None:
        # The reference session exists but its close is not published yet (Yahoo fills the Nikkei late): say nothing
        # rather than present an older session as the previous close.
        return None
    done = [b for b in done if b[1] is not None]
    if len(done) < 2:
        return None
    (day, close), (_, before) = done[-1], done[-2]
    change = close - before
    pct = change / before * 100
    sign = "+" if change >= 0 else "-"
    fmt = lambda value: f"{abs(value):,.{decimals}f}"
    verb = "上昇" if change > 0 else "下落" if change < 0 else "横ばい"
    text = (f"{day.isoformat()}の{name}の終値は{close:,.{decimals}f}{unit}で、前の営業日の終値{before:,.{decimals}f}{unit}から"
            f"{fmt(change)}{unit}({sign}{abs(pct):.2f}％){verb}した。")
    return {"fact_id": f"Q{index}", "kind": "price", "event_scope": "previous", "record_type": "actual", "pairs": [],
            "fact": text, "quote": text, "source_title": f"Yahoo Finance {symbol}", "source_url": f"https://finance.yahoo.com/quote/{symbol}",
            "published_at": "", "source_context": {}}


def build(target: date, fetch=fetch_chart) -> list:
    facts = []
    for symbol, name, unit, decimals in INSTRUMENTS:
        try:
            fact = quote_fact(name, unit, decimals, daily_bars(fetch(symbol)), target, symbol, len(facts))
        except Exception:  # one missing instrument must not drop the others
            continue
        if fact:
            facts.append(fact)
    return facts


def load(out: Path, target: date, fetch=fetch_chart) -> list:
    """quotes.json in the run folder is the record: a replay of a saved day reads it instead of fetching again."""
    path = out / "quotes.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    facts = build(target, fetch)
    path.write_text(json.dumps(facts, ensure_ascii=False, indent=1), encoding="utf-8")
    return facts
