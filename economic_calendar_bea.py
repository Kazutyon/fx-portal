"""Fetch the public U.S. BEA release schedule for shadow validation."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.request
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

SOURCE_URL = "https://www.bea.gov/news/schedule"
ET = ZoneInfo("America/New_York")
JST = ZoneInfo("Asia/Tokyo")
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.I | re.S)
DATE_RE = re.compile(r'<div class="release-date">([^<]+)</div>\s*<small[^>]*>([^<]+)</small>', re.I | re.S)
TITLE_RE = re.compile(r'<td class="release-title[^>]*>(.*?)</td>', re.I | re.S)


def fetch_html(timeout: int = 20) -> str:
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "AUXEN-FX-Portal-Shadow-Calendar/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        return response.read().decode("utf-8")


def clean_html(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value))).strip()


def importance(title: str) -> str:
    high_terms = ("GDP", "Personal Income and Outlays", "International Trade in Goods and Services")
    return "high" if any(term.casefold() in title.casefold() for term in high_terms) else "medium"


def normalize(page_html: str, target_date: str) -> dict:
    target = date.fromisoformat(target_date)
    events = []
    for row in ROW_RE.findall(page_html):
        date_match = DATE_RE.search(row)
        title_match = TITLE_RE.search(row)
        if not date_match or not title_match:
            continue
        try:
            event_et = datetime.strptime(
                f"{date_match.group(1).strip()} {target.year} {date_match.group(2).strip()}",
                "%B %d %Y %I:%M %p",
            ).replace(tzinfo=ET)
        except ValueError:
            continue
        event_jst = event_et.astimezone(JST)
        if event_jst.date() != target:
            continue
        title = clean_html(title_match.group(1))
        events.append(
            {
                "time_jst": event_jst.strftime("%H:%M"),
                "country": "USD",
                "name": title,
                "importance": importance(title),
                "forecast": None,
                "previous": None,
                "official": True,
                "source_url": SOURCE_URL,
            }
        )
    events.sort(key=lambda event: (event["time_jst"], event["name"]))
    return {
        "source": "us-bea-official-schedule",
        "date": target_date,
        "fetched_at": datetime.now(JST).isoformat(timespec="seconds"),
        "events": events,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.now(JST).date().isoformat())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = normalize(fetch_html(), args.date)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"wrote {args.output} ({len(result['events'])} events)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
