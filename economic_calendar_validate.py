"""Validate and merge licensed/manual economic-calendar JSON feeds.

This tool intentionally performs no web scraping. Each input must already be
provided by a licensed API, an official source, or an approved manual export.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

TIME_RE = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")
REQUIRED_EVENT_FIELDS = {"time_jst", "country", "name", "importance"}
JST = timezone(timedelta(hours=9))


def load_feed(path: Path, target_date: str) -> dict:
    with path.open(encoding="utf-8") as handle:
        feed = json.load(handle)
    if not isinstance(feed, dict):
        raise ValueError(f"{path}: root must be an object")
    if feed.get("date") != target_date:
        raise ValueError(f"{path}: date {feed.get('date')!r} != {target_date!r}")
    if not isinstance(feed.get("source"), str) or not feed["source"].strip():
        raise ValueError(f"{path}: source is required")
    if not isinstance(feed.get("events"), list):
        raise ValueError(f"{path}: events must be an array")
    return feed


def normalize_name(value: str) -> str:
    value = re.sub(r"[\s　]+", "", value.casefold())
    return re.sub(r"[（）()・／/\[\]【】]", "", value)


def event_key(event: dict) -> tuple[str, str, str]:
    return (
        str(event["time_jst"]),
        str(event["country"]).upper(),
        normalize_name(str(event["name"])),
    )


def validate_event(event: object, source: str, index: int) -> list[str]:
    errors: list[str] = []
    label = f"{source}.events[{index}]"
    if not isinstance(event, dict):
        return [f"{label}: event must be an object"]
    missing = REQUIRED_EVENT_FIELDS - event.keys()
    if missing:
        errors.append(f"{label}: missing {', '.join(sorted(missing))}")
        return errors
    if event["time_jst"] != "TBD" and not TIME_RE.match(str(event["time_jst"])):
        errors.append(f"{label}: invalid JST time {event['time_jst']!r}")
    if not str(event["country"]).strip() or not str(event["name"]).strip():
        errors.append(f"{label}: country and name must not be empty")
    if event["importance"] not in {"low", "medium", "high"}:
        errors.append(f"{label}: importance must be low, medium, or high")
    return errors


def merge_feeds(feeds: list[dict], target_date: str) -> dict:
    grouped: dict[tuple[str, str, str], list[tuple[str, dict]]] = defaultdict(list)
    errors: list[str] = []
    warnings: list[str] = []

    for feed in feeds:
        source = feed["source"]
        for index, event in enumerate(feed["events"]):
            event_errors = validate_event(event, source, index)
            errors.extend(event_errors)
            if not event_errors:
                grouped[event_key(event)].append((source, event))

    merged = []
    for matches in grouped.values():
        sources = sorted({source for source, _ in matches})
        event = dict(matches[0][1])
        event["sources"] = sources
        event["confirmed"] = len(sources) >= 2 or bool(event.get("official"))
        if not event["confirmed"]:
            warnings.append(f"single source: {event['time_jst']} {event['country']} {event['name']}")
        merged.append(event)

    merged.sort(key=lambda item: (item["time_jst"] == "TBD", item["time_jst"], item["country"], item["name"]))
    if len(feeds) < 2:
        warnings.append("fewer than two independent sources")
    if not any(item["importance"] == "high" for item in merged):
        warnings.append("no high-importance events")
    confirmed_count = sum(bool(item["confirmed"]) for item in merged)
    if confirmed_count == 0:
        warnings.append("no events confirmed by a second source or official schedule")

    return {
        "date": target_date,
        "generated_at_jst": datetime.now(JST).isoformat(timespec="seconds"),
        "source_count": len(feeds),
        "event_count": len(merged),
        "confirmed_count": confirmed_count,
        "events": merged,
        "errors": errors,
        "warnings": warnings,
        "publish_ready": not errors and len(feeds) >= 2 and confirmed_count > 0,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--input", action="append", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        date.fromisoformat(args.date)
        feeds = [load_feed(path, args.date) for path in args.input]
        result = merge_feeds(feeds, args.date)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0 if result["publish_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
