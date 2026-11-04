"""keep: how important a news fact is, measured by code, and the dataset that lets the weights be learned over the days.

1. signals(material): per fact, how many articles report the same thing (shown to the model that picks the topics).
2. build_day(run, target, published): one file per day under data/importance/ with every fact's measurable features and two
   labels found by code, never by hand: was it in the published report (figures match), was it in the shadow report.
3. fit(): after enough days, a logistic regression says which features go with being in the published report (dependency-free).

The published report is a reference for what a day-trader report usually contains, not the truth, and it is read only offline
here (the morning shadow never takes it as input). Usage:
    python tools/local_fx_importance.py build 2026-11-04 | backfill | fit
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import local_fx_published_check as pc  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "importance"
MIN_DAYS_TO_TRUST = 30  # below this the fit is printed as a preview only

CATEGORIES = {  # statistical features, not rules: the fit says how much each one matters
    "speaker": r"総裁|議長|大統領|長官|首相|理事|発言|述べ|指摘",
    "indicator_result": r"前月比|前年比|予想を|予想(?:は|の)?\d|上回|下回|結果",
    "oil": r"原油|WTI|OPEC",
    "equities": r"ダウ|ナスダック|日経平均|株価|S&P|株式",
    "policy": r"利上げ|利下げ|政策金利|金融政策|FOMC|ECB|日銀|BOE|議事要旨",
    "geopolitics": r"イラン|ウクライナ|中東|イスラエル|戦争|制裁|選挙",
    "bond_yield": r"利回り|国債|債券",
}
PAIRS = ["USD/JPY", "EUR/USD", "EUR/JPY", "GBP/USD", "GBP/JPY", "AUD/USD", "AUD/JPY"]
SITES = {"zai.diamond.jp": "zai", "fx.minkabu.jp": "minkabu", "www.gaitame.com": "gaitame", "gaitame.com": "gaitame"}


def norm(text: str) -> str:
    return pc.norm_text(text)


def fact_figures(fact: dict) -> list:
    return pc.figures(fact.get("fact", ""))


def signals(material: list) -> dict:
    """fact_id -> {"outlets": articles that stated it (merged duplicates), "repeat": other articles with a fact sharing a
    distinctive figure, "articles": the larger of the two plus one: how many articles report this}."""
    owners = {}
    for x in material:
        for figure in fact_figures(x):
            owners.setdefault(figure, set()).add(x.get("source_id", x["fact_id"].split("-")[0]))
    result = {}
    for x in material:
        own = x.get("source_id", x["fact_id"].split("-")[0])
        titles = {t for t in (x.get("source_context") or {}).get("also_stated_in", []) if t}
        repeat = len(set().union(*[owners[f] for f in fact_figures(x)]) - {own}) if fact_figures(x) else 0
        result[x["fact_id"]] = {"outlets": 1 + len(titles), "repeat": repeat, "articles": max(1 + len(titles), 1 + repeat)}
    return result


def surprise(text: str) -> float:
    """|actual - forecast| / |forecast| when the sentence states both ('752.3万件と予想716.4万件'); 0 when it does not."""
    m = re.search(r"(-?\d+(?:\.\d+)?)[^\d。、]{0,8}?(?:と|で|となり|に)[^\d。、]{0,8}?予想(?:は|の|値)?[^\d。、]{0,3}(-?\d+(?:\.\d+)?)", norm(text))
    if not m:
        return 0.0
    actual, forecast = float(m.group(1)), float(m.group(2))
    return min(1.0, abs(actual - forecast) / max(abs(forecast), 1e-9))


def features(x: dict, sig: dict) -> dict:
    text = norm(x.get("fact", ""))
    article, _, index = x["fact_id"].partition("-")
    host = re.sub(r"^https?://([^/]+).*$", r"\1", x.get("source_url") or "")
    f = {
        "log_articles": math.log1p(sig["articles"] - 1), "log_outlets": math.log1p(sig["outlets"] - 1),
        "n_figures": min(len(fact_figures(x)), 6) / 6, "length": min(len(text), 200) / 200,
        "log_position": math.log1p(int(index)) if index.isdigit() else 0.0,
        "log_article_no": math.log1p(int(article[1:])) if article[1:].isdigit() else 0.0,
        "surprise": surprise(text), "has_surprise": float(surprise(text) > 0),
        "scope_previous": float(x.get("event_scope") == "previous"),
        "multi_pair": float(len(x.get("pairs") or []) > 1), "no_pair": float(not x.get("pairs")),
    }
    for kind in ("actual", "outlook", "forecast"):
        f[f"record_{kind}"] = float(x.get("record_type") == kind)
    for kind in ("price", "event", "outlook", "cause"):
        f[f"kind_{kind}"] = float(x.get("kind") == kind)
    for pair in PAIRS:
        f["pair_" + pair.replace("/", "")] = float(pair in (x.get("pairs") or []))
    for name in set(SITES.values()):
        f["site_" + name] = float(SITES.get(host) == name)
    for name, pattern in CATEGORIES.items():
        f["cat_" + name] = float(bool(re.search(pattern, text)))
    return {k: round(v, 4) for k, v in f.items()}


def in_text(fact: dict, page: str):
    """True/False when the fact's figures decide it (more than half of two or more, or the single one); None when it has none."""
    figs = fact_figures(fact)
    if not figs:
        return None
    have = [n for n in figs if re.search(r"(?<![0-9.])" + re.escape(n) + r"(?![0-9])", page)]
    return (len(have) / len(figs) > 0.5) if len(figs) >= 2 else bool(have)


def build_day(run: Path, target: date, published: Path | None, root: Path = ROOT) -> Path | None:
    """Write data/importance/<date>.json for one run; None when the run has no material."""
    material_file = run / "shared-material.json"
    if not material_file.exists():
        return None
    material = [x for x in json.loads(material_file.read_text(encoding="utf-8"))["facts"] if x["fact_id"].startswith("N")]
    sig = signals(material)
    pub = norm(pc.page_text(published)) if published and published.exists() else None
    report = run / "oneshot" / "report.html"
    shadow = norm(pc.page_text(report)) if report.exists() else None
    rows = [{"id": x["fact_id"], "articles": sig[x["fact_id"]]["articles"], "f": features(x, sig[x["fact_id"]]),
             "published": None if pub is None else in_text(x, pub), "shadow": None if shadow is None else in_text(x, shadow)}
            for x in material]
    day = {"date": str(target), "facts": len(rows), "uncapped_extraction": target >= date(2026, 11, 3),
           "published_topics": [t for t, _ in pc.topic_blocks(pc.page_text(published))] if pub is not None else [],
           "rows": rows}
    path = root / "data" / "importance" / f"{target}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(day, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return path


def commit_and_push(root: Path = ROOT, folder: str = "data/importance") -> str:
    """Keep the daily dataset: commit only the dataset folder and push, so it survives without anyone remembering to.
    Other work in the checkout is left alone (the commit is limited to the folder). Offline or any git trouble only returns
    a message; the files stay and the next morning's commit carries them."""
    def git(*args, timeout=120):
        return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, timeout=timeout, encoding="utf-8", errors="replace")

    try:
        if not git("status", "--porcelain", "--", folder).stdout.strip():
            return "nothing new"
        git("add", "--", folder)
        done = git("commit", "-m", f"importance data {date.today()} (automatic)", "--", folder)
        if done.returncode != 0:
            return "commit failed: " + (done.stderr or done.stdout).strip()[:150]
        pulled = git("pull", "--rebase", "--autostash", timeout=180)
        pushed = git("push", timeout=180)
        if pushed.returncode != 0:
            return "committed, push failed (retried next time): " + (pushed.stderr or pulled.stderr).strip()[:150]
        return "committed and pushed"
    except Exception as error:
        return f"skipped: {type(error).__name__}"


def load_days(folder: Path = DATA) -> list:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(folder.glob("20*.json"))]


def auc(scores: list, labels: list) -> float:
    pairs = sorted(zip(scores, labels))
    pos = sum(labels)
    neg = len(labels) - pos
    if not pos or not neg:
        return float("nan")
    rank_sum, i = 0.0, 0
    while i < len(pairs):
        j = i
        while j < len(pairs) and pairs[j][0] == pairs[i][0]:
            j += 1
        mean_rank = (i + j + 1) / 2
        rank_sum += mean_rank * sum(l for _, l in pairs[i:j])
        i = j
    return (rank_sum - pos * (pos + 1) / 2) / (pos * neg)


def train(rows: list, names: list, steps: int = 400, rate: float = 0.3, l2: float = 0.01) -> tuple[list, float]:
    weights, bias = [0.0] * len(names), 0.0
    for _ in range(steps):
        grad, gb = [0.0] * len(names), 0.0
        for features_, y in rows:
            z = bias + sum(w * features_[n] for w, n in zip(weights, names))
            error = 1 / (1 + math.exp(-max(-30, min(30, z)))) - y
            gb += error
            for k, n in enumerate(names):
                grad[k] += error * features_[n]
        size = len(rows)
        weights = [w - rate * (g / size + l2 * w) for w, g in zip(weights, grad)]
        bias -= rate * gb / size
    return weights, bias


def fit(days: list | None = None) -> dict:
    """Logistic regression of 'in the published report' on the features, validated on the latest days."""
    days = days if days is not None else load_days()
    labelled = [d for d in days if d["rows"] and any(r["published"] is not None for r in d["rows"])]
    if len(labelled) < 4:
        return {"status": "not enough days", "days": len(labelled)}
    cut = max(1, int(len(labelled) * 0.7))
    names = sorted(labelled[0]["rows"][0]["f"])
    pick = lambda ds: [(r["f"], float(r["published"])) for d in ds for r in d["rows"] if r["published"] is not None]
    train_rows, test_rows = pick(labelled[:cut]), pick(labelled[cut:])
    weights, bias = train(train_rows, names)
    score = lambda rows: [bias + sum(w * f[n] for w, n in zip(weights, names)) for f, _ in rows]
    result = {"status": "trusted" if len(labelled) >= MIN_DAYS_TO_TRUST else "preview only (too few days)",
              "days": len(labelled), "train_days": cut, "test_days": len(labelled) - cut,
              "base_rate_test": round(sum(y for _, y in test_rows) / max(len(test_rows), 1), 3),
              "auc_train": round(auc(score(train_rows), [y for _, y in train_rows]), 3),
              "auc_test": round(auc(score(test_rows), [y for _, y in test_rows]), 3),
              "weights": dict(sorted(zip(names, (round(w, 3) for w in weights)), key=lambda kv: -abs(kv[1])))}
    return result


def main() -> int:
    command = sys.argv[1] if len(sys.argv) > 1 else "fit"
    if command == "build":
        target = date.fromisoformat(sys.argv[2])
        published = pc.fetch_published(target, ROOT)
        print(build_day(ROOT / "shadow-output" / f"{target}-local-daily", target, published))
    elif command == "backfill":
        for run in sorted((ROOT / "shadow-output").glob("20??-??-??-local-daily")):
            target = date.fromisoformat(run.name[:10])
            published = ROOT / "reports" / f"{target}.html"
            path = build_day(run, target, published if published.exists() else None)
            print(target, path.name if path else "no material")
    else:
        result = fit()
        DATA.mkdir(parents=True, exist_ok=True)
        (DATA / "fit-latest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
