"""Model comparison runner: replay a recorded day's material through the real one-shot pipeline with another model.

Usage: python -I tools/local_fx_model_bench.py <model> <YYYY-MM-DD> [<YYYY-MM-DD> ...]
Env: FX_WRITE_BODIES=1 (prose writer), FX_CLAIM_CHECK=1 (local sentence check), FX_LUNA=1 (keep the Codex review),
     FX_BENCH_SUFFIX=<text> (output folder suffix). Writes shadow-output/bench-<model><suffix>-<date>/ -- delete afterwards.
Lifecycle: the outputs are temporary; this script is kept as the way to compare models
(see docs/EVIDENCE-LOCAL-LLM-MODEL-AND-CLAIM-CHECK-20261014.md).
Check free VRAM first and do not run in the 07:00 shadow window."""
Usage: python -I full_bench.py <model> <date> [<date> ...]
Writes to shadow-output/bench-<model-tag>-<date>/ and appends a line to full_bench.jsonl."""
import json, re, shutil, sys, time
from datetime import date
from pathlib import Path

TOOLS = str(Path(__file__).resolve().parent)
sys.path.insert(0, TOOLS)
import local_fx_daily as daily  # noqa
import local_fx_external_review as ext  # noqa
import local_fx_news as news  # noqa
import local_fx_oneshot as one  # noqa

import os
if not os.environ.get("FX_LUNA"):
    ext.review = lambda *a, **k: {"status": "disabled"}

model, dates = sys.argv[1], sys.argv[2:]
news.MODEL = model
tag = re.sub(r"[^a-z0-9]+", "-", model.lower()).strip("-")
root = daily.ROOT / "shadow-output"
log = Path(__file__).resolve().parent.parent / ".runtime" / "model-bench.jsonl"
log.parent.mkdir(parents=True, exist_ok=True)
for d in dates:
    src = root / f"{d}-local-daily"
    import os; out = root / f"bench-{tag}{os.environ.get('FX_BENCH_SUFFIX','')}-{d}"
    out.mkdir(parents=True, exist_ok=True)
    for name in ["shared-material.json", "calendar.json", "market.json", "policy.json"]:
        shutil.copyfile(src / name, out / name)
    rd = lambda n: json.loads((out / n).read_text(encoding="utf-8"))
    material = rd("shared-material.json")["facts"]
    t = time.time()
    rec = {"model": model, "date": d, "out": str(out)}
    try:
        one.generate(out, date.fromisoformat(d), material, rd("calendar.json"), rd("market.json")["ranking"], rd("policy.json"))
        rec["ok"] = True
    except Exception as e:
        rec["ok"] = False
        rec["error"] = f"{type(e).__name__}: {str(e)[:300]}"
    rec["elapsed"] = round(time.time() - t, 1)
    chk = out / "oneshot-checks.json"
    if chk.exists():
        c = json.loads(chk.read_text(encoding="utf-8"))
        rec["number_date_errors"] = c.get("number_date_errors")
        rec["internal_wording"] = c.get("internal_wording")
        rec["meta_wording"] = c.get("meta_wording")
        rec["semantic_issues"] = len(c.get("semantic_issues", []))
        rec["semantic_check_error"] = c.get("semantic_check_error")
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(rec, flush=True)
