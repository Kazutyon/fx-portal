"""keep: record-only check of the published (Claude) daily report against the shadow's collected evidence.

No model calls, no changes to any report. Two mechanical checks per sentence of the published page:
  numbers    prices/decimals that appear in none of the collected articles;
  close-role a pair stated as having closed ("引けた/終値") at a number other than the close an article states
             explicitly ("終値は…"), e.g. an intraday high reported as the close.
A third, coverage, lists the published report's topics (「トピックN」) whose figures the shadow report does not contain
(the Claude run led with something the shadow never wrote); topics are matched by their figures, not by wording.
Results go to published-check.json in the shadow run directory."""
from __future__ import annotations

import html
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import local_fx_grounding as grounding
import local_fx_oneshot as oneshot

PAIR_WORDS = {
    "USD/JPY": r"ドル円|ドル・円", "EUR/USD": r"ユーロドル|ユーロ・ドル", "EUR/JPY": r"ユーロ円|ユーロ・円",
    "GBP/USD": r"ポンドドル|ポンド・ドル", "GBP/JPY": r"ポンド円|ポンド・円", "AUD/USD": r"豪ドル/?米ドル|オーストラリアドル・?ドル",
    "AUD/JPY": r"豪ドル円|豪ドル・円",
}
CLOSED = r"引け|終値"


def page_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    raw = re.sub(r"<(script|style).*?</\1>", " ", raw, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", "\n", raw))


def sentences(text: str) -> list:
    parts = []
    for line in text.splitlines():
        line = line.strip()
        if len(line) >= 12:
            parts += [p.strip() + "。" for p in re.split(r"。", line) if len(p.strip()) >= 8]
    return list(dict.fromkeys(parts))


def evidence_of(run: Path) -> list:
    material = json.loads((run / "shared-material.json").read_text(encoding="utf-8"))["facts"]
    evidence = [{"quote": x.get("quote", ""), "fact": x.get("fact", ""), "source_context": x.get("source_context", {}),
                 "published_at": x.get("published_at", "")} for x in material]
    for p in sorted((run / "sources").glob("*.json")):  # full article text: the published page may use passages the extraction did not
        evidence.append({"quote": p.read_text(encoding="utf-8", errors="replace"), "fact": "", "source_context": {}, "published_at": ""})
    for name in ("market.json", "calendar.json", "policy.json"):  # ranking scores, scheduled events and policy rates are also inputs of the page
        f = run / name
        if f.exists():
            evidence.append({"quote": f.read_text(encoding="utf-8", errors="replace"), "fact": "", "source_context": {}, "published_at": ""})
    return evidence


def close_value(fact: str):
    """The close stated by an article fact: '終値は156.87円', '終値157.95円となり' or '157.50円で終値を付け'."""
    text = unicodedata.normalize("NFKC", fact).replace(",", "")
    # "終値は156.87円", "終値157.95円となり" and "157.50円で終値を付け"; the previous session's close ("前営業日NY終値") is not the day's
    m = (re.search(r"(?<!NY)(?<!前日)終値は?\s*([0-9]+\.[0-9]+)", text)
         or re.search(r"([0-9]+\.[0-9]+)\s*(?:円|ドル)?\s*で終値", text))
    return float(m.group(1)) if m else None


def fetch_published(target: date, root: Path) -> Path | None:
    """The report as published: the local checkout may predate the 07:00 push, so fall back to the live page."""
    local = root / "reports" / f"{target}.html"
    if local.exists():
        return local
    import urllib.request
    try:
        with urllib.request.urlopen(f"https://kazutyon.github.io/fx-portal/reports/{target}.html", timeout=30) as response:
            body = response.read()
    except Exception:
        return None
    cache = root / ".runtime" / "local-fx-shadow" / f"published-{target}.html"
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_bytes(body)
    return cache


def norm_text(text: str) -> str:
    return re.sub(r"(\d+)円(\d{1,2})銭", lambda m: f"{m[1]}.{m[2].zfill(2)}円",
                  unicodedata.normalize("NFKC", text).replace(",", ""))


def topic_blocks(text: str) -> list:
    """The published report's numbered topics: [(title, body)]; a topic runs until the next one or the hand-over line."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    blocks, current = [], None
    for line in lines:
        m = re.match(r"【トピック\d+】(.+)", line)
        if m:
            current = [m.group(1), []]
            blocks.append(current)
        elif current is not None and re.match(r"本日[（(]|ポータル|AUXEN", line):
            current = None
        elif current is not None:
            current[1].append(line)
    return [(t, " ".join(b)) for t, b in blocks]


def figures(text: str) -> list:
    """Distinctive figures of a text: decimals and 3+ digit numbers, not years."""
    found = re.findall(r"(?<![0-9.])\d+(?:\.\d+)?(?![0-9])", norm_text(text))
    return list(dict.fromkeys(t for t in found if ("." in t or len(t) >= 3) and not re.fullmatch(r"20[0-9]{2}", t)))


def coverage(published: Path, shadow_report: Path) -> dict:
    """Which published topics the shadow report lacks. 'covered' >50% of the topic's figures appear in the shadow report,
    'partial' some, 'missing' none; a topic with fewer than two figures is matched by the key words of its title."""
    shadow = norm_text(page_text(shadow_report))
    topics = []
    for title, body in topic_blocks(page_text(published)):
        nums = figures(title + " " + body)
        have = [n for n in nums if re.search(r"(?<![0-9.])" + re.escape(n) + r"(?![0-9])", shadow)]
        if len(nums) >= 2:
            ratio = len(have) / len(nums)
            status = "covered" if ratio > 0.5 else "partial" if have else "missing"
        else:
            terms = re.findall(r"[ァ-ヶー]{3,}|[一-龥]{3,}", title)
            status = "covered" if any(t in shadow for t in terms) else "missing"
        topics.append({"title": title, "status": status, "figures": nums, "missing_figures": [n for n in nums if n not in have]})
    return {"topics": topics, "total": len(topics),
            "missing": sum(t["status"] == "missing" for t in topics), "partial": sum(t["status"] == "partial" for t in topics)}


def check(published: Path, run: Path, target: date) -> dict:
    material = json.loads((run / "shared-material.json").read_text(encoding="utf-8"))["facts"]
    by_id = {x["fact_id"]: x for x in material}
    closes = {pair: close_value(by_id[i]["fact"]) for pair, i in oneshot.closing_ids(material).items()}
    evidence = evidence_of(run)
    flagged = []
    page = sentences(page_text(published))
    # one pass over the whole page (building the evidence corpus per sentence is far too slow), then locate the sentences
    missing = grounding.number_errors(unicodedata.normalize("NFKC", " ".join(page)), evidence, target)
    missing_tokens = {m.group(1) for e in missing if (m := re.match(r"number (\S+) not found", e))}
    for s in page:
        norm_s = unicodedata.normalize("NFKC", s).replace(",", "")
        numbers = [f"number {t} not found in original evidence" for t in sorted(missing_tokens)
                   if re.search(r"(?<![0-9.])" + re.escape(t) + r"(?![0-9])", norm_s)]
        role = []
        if re.search(CLOSED, s):
            norm = unicodedata.normalize("NFKC", s)
            for pair, close in closes.items():
                if close is None or pair not in PAIR_WORDS:
                    continue
                for m in re.finditer(PAIR_WORDS[pair], norm):
                    # a figure belongs to the nearest pair word before it ("ユーロ円は176.05円、ユーロドルは1.1154ドルで引けた")
                    others = [o.start() for w in PAIR_WORDS.values() for o in re.finditer(w, norm) if o.start() >= m.end()]
                    tail = norm[m.end(): min([m.end() + 60] + others)]
                    after = re.search(r"([0-9]+\.[0-9]+)\s*(?:円|ドル)?(?:まで|で)?[^。、]{0,6}?(?:%s)" % CLOSED, tail)
                    if after and abs(float(after.group(1)) - close) > 1e-9:
                        role.append(f"{pair}: states a close of {after.group(1)} but the articles state the close as {close}")
        if numbers or role:
            flagged.append({"sentence": s[:200], "numbers_not_in_articles": numbers, "close_mismatch": role})
    result = {"published": str(published), "date": str(target), "closes_from_articles": closes,
              "sentences_flagged": len(flagged), "flagged": flagged}
    report = run / "oneshot" / "report.html"
    if report.exists():
        result["coverage"] = coverage(published, report)
    return result


def main() -> int:
    target = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    root = Path(__file__).resolve().parent.parent
    published = fetch_published(target, root)
    run = root / "shadow-output" / f"{target}-local-daily"
    if published is None or not (run / "shared-material.json").exists():
        print("published-check skipped (missing report or collected material)")
        return 0
    result = check(published, run, target)
    (run / "published-check.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    cov = result.get("coverage", {})
    print(f"STAGE published-check flagged={result['sentences_flagged']} topics_missing={cov.get('missing')} topics_partial={cov.get('partial')}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
