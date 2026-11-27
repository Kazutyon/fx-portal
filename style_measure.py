"""Count how a report is written, next to the example report (みんなのFX) it is compared with. Numbers only: no text is kept or printed.

Owner 2026-11-27: the daily note in notes/style-notes.md only held impressions ("次回は数値を絞る"), and ten days of reports did not move
(length 2.5-3x, number count 4x+, だ/である vs ~75% です/ます). This prints one line of counted values for that note, as information.

usage: python style_measure.py --mine mine.txt --ref ref.txt     (UTF-8 text files; the reference is read in Step 2 and never saved to the repo)
A failure here must never stop the report: the caller ignores a non-zero exit."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")
POLITE_END = re.compile(r"(です|ます|でした|ました|ません|でしょう|ましょう)$")


def measure(text: str) -> dict:
    flat = re.sub(r"\s+", "", text)
    sentences = [s for s in re.split(r"(?<=。)", flat) if s.strip("。")]
    polite = sum(1 for s in sentences if POLITE_END.search(s.rstrip("。")))
    return {"chars": len(flat),
            "numbers_per_100": round(100 * len(NUMBER.findall(flat)) / len(flat), 1) if flat else 0.0,
            "polite_pct": round(100 * polite / len(sentences)) if sentences else 0}


def note_line(mine: dict, ref: dict) -> str:
    return (f"測定値(コードで数えた値・今日/見本): 字数 {mine['chars']}/{ref['chars']}、"
            f"数値の個数(100字あたり) {mine['numbers_per_100']}/{ref['numbers_per_100']}、"
            f"です・ます調の文 {mine['polite_pct']}%/{ref['polite_pct']}%")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mine", type=Path, required=True)
    parser.add_argument("--ref", type=Path, required=True)
    args = parser.parse_args()
    mine = measure(args.mine.read_text(encoding="utf-8"))
    ref = measure(args.ref.read_text(encoding="utf-8"))
    if not mine["chars"] or not ref["chars"]:
        return 1
    sys.stdout.reconfigure(encoding="utf-8")
    print(note_line(mine, ref))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
