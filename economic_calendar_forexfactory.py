"""Fetch Forex Factory's published weekly JSON for shadow validation only."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

FEED_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
JST = timezone(timedelta(hours=9))
IMPACT_MAP = {"Low": "low", "Medium": "medium", "High": "high", "Holiday": "low"}


def fetch_feed(timeout: int = 20) -> list[dict]:
    request = urllib.request.Request(
        FEED_URL,
        headers={"User-Agent": "AUXEN-FX-Portal-Shadow-Calendar/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        payload = json.load(response)
    if not isinstance(payload, list):
        raise ValueError("feed root must be an array")
    return payload


def normalize(payload: list[dict], target_date: str) -> dict:
    events = []
    for item in payload:
        try:
            event_at = datetime.fromisoformat(item["date"]).astimezone(JST)
        except (KeyError, TypeError, ValueError):
            continue
        if event_at.date().isoformat() != target_date:
            continue
        impact = str(item.get("impact", "Low"))
        events.append(
            {
                "time_jst": event_at.strftime("%H:%M"),
                "country": str(item.get("country", "")).upper(),
                "name": str(item.get("title", "")).strip(),
                "importance": IMPACT_MAP.get(impact, "low"),
                "forecast": item.get("forecast") or None,
                "previous": item.get("previous") or None,
                "official": False,
                "source_url": FEED_URL,
            }
        )
    events.sort(key=lambda event: (event["time_jst"], event["country"], event["name"]))
    return {
        "source": "forex-factory-weekly-feed",
        "date": target_date,
        "fetched_at": datetime.now(JST).isoformat(timespec="seconds"),
        "events": events,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.now(JST).date().isoformat())
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        date.fromisoformat(args.date)
        result = normalize(fetch_feed(), args.date)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"wrote {args.output} ({len(result['events'])} events)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
