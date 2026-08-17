"""Fetch official BLS release dates via the FRED Release Dates API for shadow validation."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

API_URL = "https://api.stlouisfed.org/fred/release/dates"
ET = ZoneInfo("America/New_York")
JST = ZoneInfo("Asia/Tokyo")

# release_id -> (release name, standard release time in ET). BLS publishes these
# flagship releases at a fixed time of day; FRED's release-dates endpoint returns
# only the date, not the time.
RELEASES: dict[int, tuple[str, str]] = {
    50: ("Employment Situation", "08:30"),
    10: ("Consumer Price Index", "08:30"),
    46: ("Producer Price Index", "08:30"),
    192: ("Job Openings and Labor Turnover Survey", "10:00"),
}


def fetch_release_dates(api_key: str, release_id: int, start: str, end: str, timeout: int = 20) -> list[str]:
    query = (
        f"?release_id={release_id}&api_key={api_key}&file_type=json"
        f"&realtime_start={start}&realtime_end={end}"
    )
    request = urllib.request.Request(
        API_URL + query, headers={"User-Agent": "AUXEN-FX-Portal-Shadow-Calendar/1.0"}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        payload = json.loads(response.read().decode("utf-8"))
    return [item["date"] for item in payload["release_dates"]]


def normalize(release_dates: dict[int, list[str]], target_date: str) -> dict:
    events = []
    for release_id, (name, time_et) in RELEASES.items():
        if target_date not in release_dates.get(release_id, []):
            continue
        event_et = datetime.strptime(f"{target_date} {time_et}", "%Y-%m-%d %H:%M").replace(tzinfo=ET)
        event_jst = event_et.astimezone(JST)
        events.append(
            {
                "time_jst": event_jst.strftime("%H:%M"),
                "country": "USD",
                "name": name,
                "importance": "high",
                "forecast": None,
                "previous": None,
                "official": True,
                "source_url": f"https://fred.stlouisfed.org/release?rid={release_id}",
            }
        )
    events.sort(key=lambda event: (event["time_jst"], event["name"]))
    return {
        "source": "us-fred-bls-release-calendar",
        "date": target_date,
        "fetched_at": datetime.now(JST).isoformat(timespec="seconds"),
        "events": events,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.now(JST).date().isoformat())
    parser.add_argument("--api-key", default=None, help="Defaults to FRED_API_KEY env var")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    import os

    api_key = args.api_key or os.environ.get("FRED_API_KEY")
    if not api_key:
        print("ERROR: FRED_API_KEY is not set", file=sys.stderr)
        return 1

    target = date.fromisoformat(args.date)
    start = target.isoformat()
    end = date(target.year, 12, 31).isoformat()

    try:
        release_dates = {
            release_id: fetch_release_dates(api_key, release_id, start, end) for release_id in RELEASES
        }
        result = normalize(release_dates, args.date)
    except (OSError, ValueError, RuntimeError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output} ({len(result['events'])} events)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
