"""keep: advisory second-opinion review of the finished one-shot draft by a different model (Codex Luna).

Why: the local Qwen writer and its own verifier share blind spots (2026-10-05: it missed
"前週末高値" mix-ups and 製造業/非製造業). Trial that day: Luna found them in ~44s, other local
models found none. Owner approved the trial and this wiring on 2026-10-05.

Advisory only: the result is recorded in oneshot-checks.json, never rewrites the draft, and any
failure (missing CLI, timeout, bad JSON, disabled) is recorded without stopping the run.
Source article text is sent to the reviewer, so the switch lives in claude_mirror_shadow.json
("external_review.enabled") and defaults to off when the key is absent.
"""
from __future__ import annotations

import json
import re
import subprocess
import time
from pathlib import Path

CONFIG = Path(__file__).resolve().parent / "claude_mirror_shadow.json"
EXTENSIONS = Path.home() / ".vscode" / "extensions"
CODEX_RELATIVE = Path("bin") / "windows-x86_64" / "codex.exe"

TASK = ("以下の日報本文(draft)を資料(facts/original_passages/today_calendar)と照合し、問題のある記述だけを挙げる。"
        "種類: 時制、資料外の因果、数値(資料と異なる/資料にない水準)、資料外の出来事、予想と実績の混同、"
        "取り違え(数字や指標が資料で指すものと本文の呼び方が違う)。"
        "分析としての条件付き見通しは問題にしない。文体は指摘しない。"
        "ファイルやコマンドは使わず、この文章だけで答える。"
        "出力はJSON配列のみ: [{\"section\":..,\"excerpt\":..,\"kind\":..,\"reason\":..}]。問題なければ[]。\n資料:\n")


def settings(config_path: Path = CONFIG) -> dict:
    try:
        value = json.loads(config_path.read_text(encoding="utf-8")).get("external_review", {})
    except (OSError, ValueError):
        return {"enabled": False}
    return value if isinstance(value, dict) else {"enabled": False}


def newest_codex(extensions: Path = EXTENSIONS) -> Path | None:
    found = []
    for folder in extensions.glob("openai.chatgpt-*"):
        match = re.match(r"openai\.chatgpt-(\d+(?:\.\d+)*)", folder.name)
        exe = folder / CODEX_RELATIVE
        if match and exe.is_file():
            found.append((tuple(int(x) for x in match.group(1).split(".")), exe))
    return max(found)[1] if found else None


def parse_issues(text: str) -> list:
    match = re.search(r"\[.*\]", text, re.S)
    if not match:
        raise ValueError("no JSON array in reviewer output")
    issues = json.loads(match.group(0))
    if not isinstance(issues, list) or not all(isinstance(x, dict) for x in issues):
        raise ValueError("reviewer output is not a list of objects")
    return issues


def review(out: Path, verify_data: dict, texts: dict, run=subprocess.run, config_path: Path = CONFIG,
           extensions: Path = EXTENSIONS) -> dict:
    cfg = settings(config_path)
    if not cfg.get("enabled"):
        return {"status": "disabled"}
    model = cfg.get("model", "gpt-5.6-luna")
    result = {"status": "error", "reviewer": f"codex {model}", "owner_approved_on": cfg.get("owner_approved_on")}
    started = time.monotonic()
    try:
        exe = newest_codex(extensions)
        if exe is None:
            raise FileNotFoundError("codex.exe not found under the VS Code extensions folder")
        prompt = TASK + json.dumps({**verify_data, "draft": texts}, ensure_ascii=False)
        last_message = out / "stages" / "external-review.last-message.txt"
        last_message.parent.mkdir(parents=True, exist_ok=True)
        last_message.unlink(missing_ok=True)
        done = run([str(exe), "exec", "-m", model, "--skip-git-repo-check", "-s", "read-only", "-C", str(out),
                    "--output-last-message", str(last_message), "-"],
                   input=prompt, capture_output=True, text=True, encoding="utf-8",
                   timeout=int(cfg.get("timeout_seconds", 300)))
        if done.returncode != 0:
            raise RuntimeError(f"codex exit {done.returncode}: {(done.stderr or '')[-300:]}")
        result["issues"] = parse_issues(last_message.read_text(encoding="utf-8"))
        result["status"] = "ok"
    except Exception as error:  # advisory: never stop the daily run
        result["error"] = f"{type(error).__name__}: {error}"
    result["elapsed_seconds"] = round(time.monotonic() - started, 1)
    return result
