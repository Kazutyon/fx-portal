"""Remove information-source names from published FX reports (one-off, mechanical).

Rules (no AI, no rewriting):
  1. A full-width parenthesis group whose content is ONLY source names / link words
     (一致, のみ, 単独, 照合済み, 確認済み, 要確認, separators) is removed.
     If it contained 要確認, it becomes （要確認）.
  2. Half-width "(FF)" style tags next to a rank are removed.
Everything else is left untouched and reported as residual.
Verification: every difference between before/after must be a pure deletion of text
made only of source tokens, or a replacement by （要確認）.
"""
import difflib
import re
import sys
from pathlib import Path

SRC = r"Investing\.com|財経新聞|みんかぶ|ザイFX|ザイ|フィスコ|DZH|外為どっとコム|外為ドットコム|KissFX|Kiss|ForexFactory|Forex Factory|FF|ロイター|Reuters|Bloomberg"
WORDS = r"確認|一致|のみ|単独|で一致|照合済み|照合|確認済み|2ソース|２ソース|複数ソース|ソース|要確認"
SEP = r"[\s/／・、,，×x＋+&＆と]"
TOKEN = re.compile(f"(?:{SRC}|{WORDS}|{SEP})+")
GROUP = re.compile(r"（([^（）<>]{1,60})）")
HALF = re.compile(r"\((?:" + SRC + r")(?:[/・](?:" + SRC + r"))*\)")
ANY_SRC = re.compile(SRC)


GLUE = re.compile(
    r"ランク[SAB◎○△×]{0,2}|区分[:：]?[高中低]?|[高中低](?![一-龥])|経由|JSON|JS|の主要国休場日一覧|で本日の休場記載なし"
    r"|は\d{1,2}:\d{2}|で時刻不一致|が不一致|不一致|[SAB◎○△×]{1,2}(?=[・、/／）)]|$)"
)
FOOTNOTE = re.compile(r"<p[^>]*>\s*※[^<]*?(?:" + SRC + r")[^<]*</p>\s*")


def clean_group(match):
    inner = match.group(1)
    if not ANY_SRC.search(inner):
        return match.group(0)
    flag = "（要確認）" if "要確認" in inner else ""
    rest = ANY_SRC.sub("", inner)
    rest = GLUE.sub("", rest)
    rest = re.sub(WORDS, "", rest)
    if flag:
        rest = re.sub(r"\d{1,2}:\d{2}|は", "", rest)  # time-mismatch notes carry no extra info
    rest = re.sub(r"[\s/／・、,，。×]+", "", rest)
    if not rest:
        return flag
    # body + separator + pure-source tail (e.g. 「…前回+0.4％。Kiss/FF一致」): drop only the tail
    cut = max(inner.rfind("。"), inner.rfind("・"), inner.rfind("、"))
    if cut > 0:
        tail = inner[cut + 1:]
        if ANY_SRC.search(tail) and TOKEN.fullmatch(tail) and not ANY_SRC.search(inner[:cut]):
            return f"（{inner[:cut]}）" + ("（要確認）" if "要確認" in tail else "")
    return match.group(0)  # real content remains: leave untouched, counted as residual


SPANHDR = re.compile(r"\s*<span>[^<]*?(?:" + SRC + r")[^<]*?(?:統合|照合)[^<]*</span>")


def clean(text):
    text = FOOTNOTE.sub("", text)
    text = SPANHDR.sub("", text)
    text = GROUP.sub(clean_group, text)
    text = HALF.sub("", text)
    return text


def verify(before, after):
    """Return list of problems; empty means only allowed edits happened."""
    problems = []
    sm = difflib.SequenceMatcher(None, before, after, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        deleted, added = before[i1:i2], after[j1:j2]
        if tag == "delete":
            ok = bool(ANY_SRC.search(deleted)) or TOKEN.fullmatch(deleted.strip("（）() ")) is not None
        elif tag == "replace":
            ok = added == "（要確認）" or (added.replace("（要確認）", "") == "" and ANY_SRC.search(deleted))
            ok = ok and bool(ANY_SRC.search(deleted))
        else:
            ok = False
        if not ok:
            problems.append((tag, deleted[:60], added[:60]))
    return problems


def main():
    mode, folder = sys.argv[1], Path(sys.argv[2])
    names = sys.argv[3:]
    files = [folder / n for n in names] if names else sorted(folder.glob("*.html"))
    changed = bad = removed = 0
    residual = []
    for f in files:
        before = f.read_text(encoding="utf-8")
        after = clean(before)
        problems = verify(before, after)
        if problems:
            bad += 1
            print("VERIFY FAIL", f.name, problems[:3])
            continue
        removed += len(ANY_SRC.findall(before)) - len(ANY_SRC.findall(after))
        for m in ANY_SRC.finditer(after):
            residual.append((f.name, after[max(0, m.start() - 25):m.end() + 25].replace("\n", " ")))
        if after != before:
            changed += 1
            if mode == "apply":
                f.write_text(after, encoding="utf-8", newline="")
    print(f"mode={mode} files={len(files)} changed={changed} verify_fail={bad} mentions_removed={removed} residual={len(residual)}")
    for name, ctx in residual[:int(80)]:
        print("  RESIDUAL", name, "|", ctx)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
