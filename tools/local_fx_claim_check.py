"""Sentence-level support check by a local model (2026-10-14).

Each sentence of the model-written prose is judged on its own against the material ("is this sentence supported by
the facts?"). Asking one short question per sentence found all 6 invented/over-stated claims that Codex Luna found
in the 10/13 draft in 60 s, where a whole-draft "find the problems" call found 0-3 (docs: LOG.md 2026-10-14).
Result shape matches local_fx_external_review.review, so local_fx_external_review.usable_issues can consume it."""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request

import local_fx_news as news

CHECKED = re.compile(r"^(hero|summary|market|risk|topic\d+)$")
SPLIT = re.compile(r"(?<=。)")
SYSTEM = ("あなたは資料照合係。『資料』に照らして、検査対象の1文の記述が資料に書かれているか判定する。"
          "数値・人名・出来事・原因・断定の強さのすべてが資料の記述の範囲内なら supported=true。"
          "資料にない人名、資料より強い断定(確定した/当面続く/最大の、など)、資料にない因果・方針・見通しの断定が1つでもあれば "
          "supported=false とし、その部分をunsupported_partに書く。")
SCHEMA = {"type": "object", "properties": {"supported": {"type": "boolean"}, "unsupported_part": {"type": "string"},
                                           "reason": {"type": "string"}},
          "required": ["supported", "unsupported_part", "reason"]}


def sentences(texts: dict) -> list:
    out = []
    for key, text in texts.items():
        if not CHECKED.match(key):
            continue
        for s in SPLIT.split(text):
            s = s.strip()
            if len(s) > 8:
                out.append((key, s))
    return out


def judge(model: str, material: str, key: str, sentence: str, timeout: int = 600) -> dict:
    body = {"model": model, "stream": False, "format": SCHEMA, "keep_alive": "10m", "think": False,
            "options": {"num_ctx": 32768, "temperature": 0, "num_predict": 600},
            "messages": [{"role": "system", "content": SYSTEM},
                         {"role": "user", "content": f"# 資料\n{material}\n\n# 検査対象の1文(セクション: {key})\n{sentence}"}]}
    for attempt in (0, 1):
        try:
            request = urllib.request.Request(news.OLLAMA + "/api/chat", data=json.dumps(body, ensure_ascii=False).encode(),
                                             headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(json.load(response)["message"]["content"])
        except urllib.error.HTTPError:
            if attempt == 0 and "think" in body:  # a model without thinking support rejects the flag
                body.pop("think")
                continue
            raise
    raise RuntimeError("unreachable")


def review(out, verify_data: dict, texts: dict, model: str | None = None) -> dict:
    """Findings in local_fx_external_review.review's shape: {status, reviewer, issues:[{section, excerpt, reason, kind}]}."""
    model = model or news.MODEL
    material = json.dumps({"facts": verify_data["facts"], "original_passages": verify_data["original_passages"]},
                          ensure_ascii=False)
    started, issues, errors = time.monotonic(), [], 0
    items = sentences(texts)
    for key, sentence in items:
        try:
            verdict = judge(model, material, key, sentence)
        except Exception:
            errors += 1
            continue
        if verdict.get("supported") is False:
            issues.append({"section": key, "excerpt": sentence, "kind": "その他",
                           "reason": (verdict.get("reason") or verdict.get("unsupported_part") or "資料に根拠がない")[:300]})
    return {"status": "ok" if errors < max(1, len(items) // 2) else "error", "reviewer": f"local {model} (sentence check)",
            "sentences": len(items), "errors": errors, "issues": issues,
            "elapsed_seconds": round(time.monotonic() - started, 1)}
