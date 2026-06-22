"""Generate the AUXEN 4H day-trading suitability ranking.

Market prices come from Yahoo Finance chart data. The spread values are only
rough cost estimates; they are not live broker quotes.
"""

from __future__ import annotations

import json
import math
import os
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path


JST = timezone(timedelta(hours=9))
OUTPUT_PATH = Path(__file__).with_name("data") / "daytrade-ranking.json"
MIN_SUCCESS = 6

PAIRS = [
    ("EUR/USD", "EURUSD=X", 0.0001, 0.8),
    ("GBP/USD", "GBPUSD=X", 0.0001, 1.2),
    ("AUD/USD", "AUDUSD=X", 0.0001, 1.0),
    ("NZD/USD", "NZDUSD=X", 0.0001, 1.3),
    ("USD/JPY", "JPY=X", 0.01, 0.9),
    ("USD/CAD", "CAD=X", 0.0001, 1.2),
    ("USD/CHF", "CHF=X", 0.0001, 1.2),
    ("EUR/JPY", "EURJPY=X", 0.01, 1.2),
    ("GBP/JPY", "GBPJPY=X", 0.01, 1.8),
    ("AUD/JPY", "AUDJPY=X", 0.01, 1.5),
    ("EUR/GBP", "EURGBP=X", 0.0001, 1.2),
    ("EUR/AUD", "EURAUD=X", 0.0001, 1.8),
]


def fetch_chart(symbol: str, range_: str, interval: str) -> list[dict]:
    encoded = urllib.parse.quote(symbol, safe="")
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{encoded}"
        f"?range={range_}&interval={interval}&events=history"
    )
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 AUXEN-FX-Portal/1.0"})
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                payload = json.load(response)
            result = payload["chart"]["result"][0]
            quote = result["indicators"]["quote"][0]
            candles = []
            for index, timestamp in enumerate(result.get("timestamp", [])):
                values = {key: quote.get(key, [None] * (index + 1))[index] for key in ("open", "high", "low", "close")}
                if all(value is not None and math.isfinite(value) for value in values.values()):
                    candles.append({"time": int(timestamp), **values})
            if not candles:
                raise ValueError(f"{symbol}: no usable candles")
            return candles
        except (OSError, ValueError, KeyError, IndexError, TypeError, json.JSONDecodeError) as error:
            last_error = error
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"{symbol}: {last_error}")


def complete_daily(candles: list[dict]) -> list[dict]:
    today_utc = datetime.now(timezone.utc).date()
    return [c for c in candles if datetime.fromtimestamp(c["time"], timezone.utc).date() < today_utc]


def aggregate_h4(hourly: list[dict]) -> list[dict]:
    buckets: dict[int, list[dict]] = {}
    for candle in hourly:
        dt = datetime.fromtimestamp(candle["time"], timezone.utc)
        bucket_dt = dt.replace(hour=(dt.hour // 4) * 4, minute=0, second=0, microsecond=0)
        buckets.setdefault(int(bucket_dt.timestamp()), []).append(candle)

    current_bucket = int(
        datetime.now(timezone.utc).replace(
            hour=(datetime.now(timezone.utc).hour // 4) * 4, minute=0, second=0, microsecond=0
        ).timestamp()
    )
    result = []
    for timestamp, group in sorted(buckets.items()):
        if timestamp >= current_bucket or len(group) < 3:
            continue
        result.append(
            {
                "time": timestamp,
                "open": group[0]["open"],
                "high": max(c["high"] for c in group),
                "low": min(c["low"] for c in group),
                "close": group[-1]["close"],
            }
        )
    return result


def ema(values: list[float], period: int) -> list[float]:
    if not values:
        return []
    alpha = 2 / (period + 1)
    output = [values[0]]
    for value in values[1:]:
        output.append(alpha * value + (1 - alpha) * output[-1])
    return output


def true_ranges(candles: list[dict]) -> list[float]:
    ranges = []
    previous_close = candles[0]["close"]
    for candle in candles:
        ranges.append(
            max(
                candle["high"] - candle["low"],
                abs(candle["high"] - previous_close),
                abs(candle["low"] - previous_close),
            )
        )
        previous_close = candle["close"]
    return ranges


def wilder(values: list[float], period: int) -> list[float | None]:
    result: list[float | None] = [None] * len(values)
    if len(values) < period:
        return result
    result[period - 1] = sum(values[:period]) / period
    for index in range(period, len(values)):
        result[index] = (result[index - 1] * (period - 1) + values[index]) / period  # type: ignore[operator]
    return result


def adx(candles: list[dict], period: int = 14) -> float:
    tr = true_ranges(candles)
    plus_dm = [0.0]
    minus_dm = [0.0]
    for previous, current in zip(candles, candles[1:]):
        up = current["high"] - previous["high"]
        down = previous["low"] - current["low"]
        plus_dm.append(up if up > down and up > 0 else 0.0)
        minus_dm.append(down if down > up and down > 0 else 0.0)

    atr_values = wilder(tr, period)
    plus_values = wilder(plus_dm, period)
    minus_values = wilder(minus_dm, period)
    dx: list[float] = []
    for atr_value, plus_value, minus_value in zip(atr_values, plus_values, minus_values):
        if not atr_value or plus_value is None or minus_value is None:
            continue
        plus_di = 100 * plus_value / atr_value
        minus_di = 100 * minus_value / atr_value
        denominator = plus_di + minus_di
        dx.append(100 * abs(plus_di - minus_di) / denominator if denominator else 0.0)
    if len(dx) < period:
        raise ValueError("not enough candles for ADX")
    return float(wilder(dx, period)[-1])


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def calculate_pair(name: str, symbol: str, pip: float, spread: float) -> dict:
    daily = complete_daily(fetch_chart(symbol, "5y", "1d"))
    h4 = aggregate_h4(fetch_chart(symbol, "60d", "1h"))
    if len(daily) < 500 or len(h4) < 80:
        raise ValueError(f"{symbol}: insufficient history ({len(daily)} daily, {len(h4)} H4)")

    daily_ranges = [(c["high"] - c["low"]) / pip for c in daily]
    adr_5y = statistics.fmean(daily_ranges)
    adr_5 = statistics.fmean(daily_ranges[-5:])
    adr_ratio = adr_5 / adr_5y * 100

    tr = true_ranges(h4)
    atr_h4 = statistics.fmean(tr[-14:]) / pip
    adx_h4 = adx(h4)
    closes = [c["close"] for c in h4]
    ema20 = ema(closes, 20)
    ema50 = ema(closes, 50)
    slope = (ema20[-1] - ema20[-4]) / pip
    aligned_up = closes[-1] > ema20[-1] > ema50[-1] and slope > 0
    aligned_down = closes[-1] < ema20[-1] < ema50[-1] and slope < 0
    direction = "上昇" if aligned_up else "下降" if aligned_down else "レンジ"

    volatility_score = clamp((adr_ratio - 55) / 75 * 45, 0, 45)
    trend_score = clamp((adx_h4 - 12) / 23 * 28, 0, 28)
    if aligned_up or aligned_down:
        trend_score += 12
    elif abs(slope) > atr_h4 * 0.05:
        trend_score += 5
    trend_score = clamp(trend_score, 0, 40)
    cost_ratio = spread / adr_5 * 100 if adr_5 else 100
    cost_score = clamp(15 - cost_ratio * 2.5, 0, 15)
    eligible = adr_5 >= 30
    score = round(volatility_score + trend_score + cost_score) if eligible else 0

    if not eligible:
        verdict = "対象外"
    elif score >= 80:
        verdict = "最適"
    elif score >= 65:
        verdict = "適"
    elif score >= 50:
        verdict = "候補"
    else:
        verdict = "見送り"

    return {
        "pair": name,
        "symbol": symbol,
        "score": score,
        "verdict": verdict,
        "eligible": eligible,
        "adr_5_pips": round(adr_5, 1),
        "adr_5y_pips": round(adr_5y, 1),
        "adr_ratio_pct": round(adr_ratio, 1),
        "atr_h4_pips": round(atr_h4, 1),
        "adx_h4": round(adx_h4, 1),
        "direction": direction,
        "estimated_spread_pips": spread,
        "cost_ratio_pct": round(cost_ratio, 2),
    }


def main() -> int:
    rankings = []
    errors = []
    for pair in PAIRS:
        try:
            rankings.append(calculate_pair(*pair))
            print(f"OK  {pair[0]}")
        except Exception as error:  # keep the previous published file if the source is temporarily unavailable
            errors.append(f"{pair[0]}: {error}")
            print(f"ERR {pair[0]}: {error}", file=sys.stderr)

    if len(rankings) < MIN_SUCCESS:
        print(
            f"Only {len(rankings)} pairs succeeded; keeping the previous {OUTPUT_PATH.name}.",
            file=sys.stderr,
        )
        return 0

    rankings.sort(key=lambda row: (row["eligible"], row["score"]), reverse=True)
    for rank, row in enumerate((r for r in rankings if r["eligible"]), 1):
        row["rank"] = rank
    for row in rankings:
        if not row["eligible"]:
            row["rank"] = None

    payload = {
        "generated_at_jst": datetime.now(JST).isoformat(timespec="minutes"),
        "source": "Yahoo Finance chart data",
        "methodology": {
            "adr_5y": "直近5年の完了日足における高値－安値の平均",
            "adr_5": "直近5本の完了日足における高値－安値の平均",
            "volatility": "5日ADR ÷ 5年ADR",
            "trend": "4時間足のADX(14)とEMA20・EMA50の並び、EMA20の傾き",
            "cost": "概算スプレッド ÷ 5日ADR",
            "minimum_adr_pips": 30,
        },
        "rankings": rankings,
        "errors": errors,
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT_PATH.with_suffix(".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, OUTPUT_PATH)
    print(f"Wrote {OUTPUT_PATH} ({len(rankings)} pairs, {len(errors)} errors)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
