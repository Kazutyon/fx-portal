"""keep: experimental bounded summary tree, not a publishing/cron entrypoint.

Nodes, review results and coverage manifests are evidence in the parent run.
Original facts remain authoritative; summaries only guide editorial decisions.
"""
from __future__ import annotations

import json
import re

import local_fx_news as news


def compact_fact(fact):
    return {k: fact[k] for k in ("fact_id", "fact", "event_date", "event_scope",
            "market_session", "pairs", "record_type") if k in fact}


def refs_schema(ids, maximum):
    return {"type": "array", "items": {"type": "string", "enum": ids},
            "minItems": 1, "maxItems": maximum, "uniqueItems": True}


def summarize(api, out, label, inputs, target, dates, leaf):
    ids = [x["fact_id"] if leaf else x["node_id"] for x in inputs]
    slot_schema = {"type": "integer", "minimum": 0, "maximum": 3}
    if not leaf:
        slot_schema = {"type": "array", "items": slot_schema, "minItems": 1, "maxItems": 4, "uniqueItems": True}
    schema = news.schema({"units": {"type": "array", "minItems": 1, "maxItems": 4,
        # Do not constrain decoding inside a sentence. Check length AFTER
        # generation and reconstruct once; never cut source facts mid-sentence.
        "items": news.schema({"text": {"type": "string"}})},
        "routes": news.schema({ref: slot_schema for ref in ids})})
    data = {"date_facts": dates, "inputs": inputs}
    source_text = " ".join(x["fact"] if leaf else " ".join(x["units"]) for x in inputs)
    # Spelling constraints are factual, not a fixed market theme. This model
    # repeatedly compresses Iran into the Italy abbreviation during merges.
    if "イラン" in source_text and not re.search(r"イタリア|米伊", source_text):
        data["entity_spelling_rules"] = {"イラン": "イランのまま記述。米伊・イタリアへ変更禁止。米国とイランは略さず米国とイランと書く。"}
    task = ("全入力を読んで、相場全体を後で理解するための要約を最大4単位にまとめる。各単位260文字以内。"
            "同じ出来事は統合し、違う日付/市場/通貨/予想/実績は混ぜない。"
            "routesの各入力IDに、その材料を整理したunitsの0始まり番号を返す。全IDを必ず振り分け、未使用番号は不可。"
            "些細な値動きは一群にまとめてよいが、異なる主要材料・反対材料・条件は消さない。"
            "日付/数値/予定と実績/出典の見通しを保持。資料にない因果や結果は作らない。"
            "テーマは固定せず、今回の入力に合わせる。何が起きたかと、分からないことを区別する。"
            "これは内部要約であって記事ではない。元資料に戻るためのroutesを付ける。"
            "IDはroutesだけに書きtextへ埋め込まない。outlookは出典の見通しと明記し、全体の確定事実にしない。"
            "国名・組織名・人名は入力の表記を保ち、独自の漢字略称へ変えない。")
    if not leaf:
        task += (" 子要約には複数の論点がある。親の複数unitsへ対応してよいので、routesには番号の配列を返す。"
                 "全unitsを少なくとも1子の内容に対応させる。"
                 "例: 子Aに論点XとYがあり、親unit0にX、unit1にYを記述した場合、Aのroutesは[0,1]。"
                 "子の最初の論点だけを対応させず、親text中の全事実の出所を番号配列へ含める。")
    raw_value = api.infer_cached(out, label, task, data, schema)
    for attempt in range(2):
        routes = raw_value.get("routes", {})
        value = {"units": [{"text": u["text"], "refs": [ref for ref, slot in routes.items()
                    if (slot == i if leaf else isinstance(slot, list) and i in slot)]}
                    for i, u in enumerate(raw_value["units"])]}
        refs = {r for u in value["units"] for r in u["refs"]}
        errors = []
        def valid_slot(slot):
            values = [slot] if leaf else slot
            return (isinstance(values, list) and 1 <= len(values) <= 4 and
                    all(type(x) is int and 0 <= x < len(value["units"]) for x in values) and
                    len(set(values)) == len(values))
        if set(routes) != set(ids) or not all(valid_slot(slot) for slot in routes.values()):
            errors.append("routes must assign every original ID to an existing summary unit")
        if refs != set(ids):
            errors.append(f"missing input IDs: {sorted(set(ids) - refs)}; unknown IDs: {sorted(refs - set(ids))}")
        if not 1 <= len(value["units"]) <= 4:
            errors.append("unit count must be 1..4")
        for i, unit in enumerate(value["units"]):
            if not unit["refs"] or len(unit["refs"]) != len(set(unit["refs"])):
                errors.append(f"unit {i}: refs must be nonempty and unique: {unit['refs']}")
            if len(unit["text"]) > 260:
                errors.append(f"unit {i}: text exceeds 260 characters")
            if re.search(r"N\d+-\d+|hierarchy-(?:leaf|merge)-", unit["text"]):
                errors.append(f"unit {i}: IDs belong in refs, not prose")
            # Reject known entity corruption before a summary becomes context.
            from local_fx_grounding import country_errors
            quoted = [{"quote": x["fact"] if leaf else " ".join(x["units"])}
                      for x, ref in zip(inputs, ids) if ref in unit["refs"]]
            errors.extend(f"unit {i}: {error}" for error in country_errors(unit["text"], quoted))
        review = api.infer_cached(out, label + f"-review-{attempt}",
            "入力と要約だけを照合。異なる日時/予想/実績/通貨を混ぜた、新しい因果/結果を加えた、"
            "独立した主要材料を消した場合FAIL。枝葉や重複の圧縮は許容。予定紹介を実施済みと誤認しない。"
            "主要な異論や条件が残るかも確認。理由は具体的に。"
            "reference_checksの各textは、そのsupporting_input_idsに指定されたinputsだけで照合する。別unitの入力で補完しない。"
            "textの一部でも参照先にないなら参照欠落でFAIL（全入力の別箇所にあっても不可）。",
            {**data, "summary": value, "reference_checks": [
                {"unit": i, "text": u["text"], "supporting_input_ids": u["refs"]}
                for i, u in enumerate(value["units"])]}, news.QC_SCHEMA)
        if errors:
            reasons = errors + ([review["reason"]] if review["verdict"] != "PASS" else [])
            review = {"verdict": "FAIL", "reason": "; ".join(reasons)}
        if review["verdict"] == "PASS":
            break
        if attempt == 0:
            # Fresh reconstruction from original inputs, not an erroneous
            # summary copied forward as another source of facts.
            raw_value = api.infer_cached(out, label + "-repair", task +
                " 検査指摘を守り、原入力から要約を作り直す。これは圧縮工程であり、一般的な解説・"
                "独自の注目理由・新しい予測/観察項目は追加しない。独自分析は最後の記事工程で行う。"
                "textは入力のfact/子要約の文を短くして結合するだけ。情報が少なければ短文でよい。"
                "『入力には記述がない』『不明』『未確認』『東京の記述はない』など、資料の不足についての説明文は書かない。"
                "NYだけの入力ならNYの事実だけで終える。元factにない市場名/欠落理由/但し書きを追加しない。"
                "参照欠落なら、textの内容を支持する入力IDをroutesでそのunitへ必ず対応させる。"
                "情報量が多ければ内容を省略せず4単位へ分け、単位の最後は必ず意味の完結した文で終える。"
                "例: 入力『対象日にA発表予定』『対象日にB講演予定』なら『対象日にA発表とB講演が予定される。』で終える。"
                "入力にない意味づけを後ろへ付けない。",
                                     {**data, "review": review}, schema)
    news.save(out / "hierarchy" / f"{label}.json", {"inputs": inputs, "summary": value, "review": review})
    if review["verdict"] != "PASS":
        raise ValueError(f"{label}: summary review failed: {review['reason']}")
    return value


def build(api, out, material, target, dates, extractive=False, observational=False):
    if not material or len({x["fact_id"] for x in material}) != len(material):
        raise ValueError("hierarchy requires nonempty unique original fact IDs")
    nodes = []
    # Every accepted fact is visited. No topic/role-specific preselection.
    if extractive:
        import local_fx_extract_summary as selection
    if observational:
        if extractive:
            raise ValueError("choose one summary method")
        import local_fx_summary_observation as observation
    leaf_batches = [batch[j:j + 6]
                    for batch in api.evidence_batches([compact_fact(x) for x in material],
                                                     selection.LEAF_BUDGET if extractive else 4500)
                    for j in range(0, len(batch), 6)]
    for i, batch in enumerate(leaf_batches):
        label = f"hierarchy-leaf-{i:03}"
        value = (observation.summarize(api, out, label, batch, dates, True) if observational else
                 selection.summarize(api, out, label, batch, dates, True) if extractive else
                 summarize(api, out, label, batch, target, dates, True))
        nodes.append({"node_id": label, "units": value["units"],
                      "covered_fact_ids": [x["fact_id"] for x in batch], "children": [],
                      **({"retained_facts": value["retained_facts"], "method": value["method"]} if extractive else {})})
    all_nodes = list(nodes)
    level = 0
    while len(nodes) > 1:
        next_nodes = []
        for i in range(0, len(nodes), 3):
            children = nodes[i:i + 3]
            if len(children) == 1:
                next_nodes.append(children[0])
                continue
            label = f"hierarchy-merge-{level:02}-{i // 3:03}"
            # At most three child summaries, never concatenate all originals.
            if extractive:
                by_id = {f["fact_id"]: f for n in children for f in n["retained_facts"]}
                value = selection.summarize(api, out, label, list(by_id.values()), dates, False)
            else:
                inputs = [{"node_id": n["node_id"], "units": [u["text"] for u in n["units"]]} for n in children]
                value = (observation.summarize(api, out, label, inputs, dates, False) if observational else
                         summarize(api, out, label, inputs, target, dates, False))
            node = {"node_id": label, "units": value["units"],
                    "covered_fact_ids": list(dict.fromkeys(r for n in children for r in n["covered_fact_ids"])),
                    "children": [n["node_id"] for n in children],
                    **({"retained_facts": value["retained_facts"], "omitted_fact_ids": value["omitted_fact_ids"],
                        "method": value["method"]} if extractive else {})}
            next_nodes.append(node)
            all_nodes.append(node)
        nodes = next_nodes
        level += 1
    result = {"root": nodes[0], "nodes": all_nodes, "original_count": len(material),
              "method": observation.METHOD if observational else selection.METHOD if extractive else "abstractive-v1",
              "content_reviews_advisory": observational,
              "lifecycle": "evidence", "rule": "coverage IDs mean visited, not all details retained or verified against original articles"}
    news.save(out / "hierarchy.json", result)
    return result


def overview(tree):
    return {"synopsis": [x["text"] for x in tree["root"]["units"]],
            "rule": "要約は全体構成の手掛かりだけ。記事の事実は別途渡すfact/quoteから照合。要約だけから事実を追加しない"}


def allocate(api, out, key, material, target, dates, tree, purpose):
    candidates = []
    context = overview(tree)
    leaves = [n for n in tree["nodes"] if not n["children"]]
    selected_nodes = []
    for i, batch in enumerate(api.evidence_batches([
            {"node_id": n["node_id"], "units": [u["text"] for u in n["units"]]} for n in leaves], 7500)):
        schema = news.schema({"node_ids": {**refs_schema([n["node_id"] for n in batch], 4), "minItems": 0}})
        ids = api.infer_cached(out, f"hierarchy-{key}-branches-{i}",
            "全体像と欄の役割から、原資料へ戻る必要のある枝を最大4つ選ぶ。IDは入力のみ。"
            "同じ値動きの重複より、必要な背景/予定/反対材料を優先。該当なしは空。",
            {"date_facts": dates, "overview": context, "role": purpose, "branches": batch}, schema)["node_ids"]
        if not set(ids) <= {n["node_id"] for n in batch}:
            raise ValueError("hierarchical branch selection returned unknown node")
        selected_nodes.extend(ids)
    branch_ids = {r for n in leaves if n["node_id"] in selected_nodes for r in n["covered_fact_ids"]}
    branch_material = [x for x in material if x["fact_id"] in branch_ids]
    for i, batch in enumerate(api.evidence_batches([compact_fact(x) for x in branch_material], 4500)):
        schema = news.schema({"fact_ids": {**refs_schema([x["fact_id"] for x in batch], 6), "minItems": 0}})
        ids = api.infer_cached(out, f"hierarchy-{key}-scan-{i:03}",
            "全体像を踏まえ、この欄の役割に必要な根拠を最大6件選ぶ。該当なしは空。"
            "前日背景と本日予定の組、反対材料を残す。全テーマを毎欄に詰め込まない。IDはこのbatchだけ。",
            {"date_facts": dates, "overview": context, "role": purpose, "facts": batch}, schema)["fact_ids"]
        if not set(ids) <= {x["fact_id"] for x in batch}:
            raise ValueError("hierarchical allocation returned unknown original ID")
        candidates.extend(x for x in ids if x not in candidates)
    by_id = {x["fact_id"]: x for x in material}
    # Reduce candidate summaries, not original bodies. Retain no hardcoded market anchors.
    for round_no in range(6):
        pool = [compact_fact(by_id[x]) for x in candidates]
        if len(json.dumps(pool, ensure_ascii=False).encode()) <= 9500:
            batches = [pool]
        else:
            batches = api.evidence_batches(pool, 4500)
        selected = []
        for i, batch in enumerate(batches):
            if not batch:
                continue
            cap = 10 if len(batches) == 1 else 4
            schema = news.schema({"fact_ids": refs_schema([x["fact_id"] for x in batch], cap)})
            ids = api.infer_cached(out, f"hierarchy-{key}-select-{round_no}-{i}",
                f"全体像と欄の役割から最終根拠を最大{cap}件選ぶ。実際の変化/背景/当日条件を必要に応じ組にする。"
                "同じ話を省き、異なる重要材料や反対材料を優先度に応じ保持。テーマを固定しない。入力IDだけ。",
                {"date_facts": dates, "overview": context, "role": purpose, "facts": batch}, schema)["fact_ids"]
            if not set(ids) <= {x["fact_id"] for x in batch}:
                raise ValueError("hierarchical reduction returned unknown original ID")
            selected.extend(x for x in ids if x not in selected)
        candidates = selected
        if len(batches) == 1:
            break
    else:
        raise ValueError("hierarchical allocation did not converge")
    if not candidates:
        raise ValueError(f"{key}: no grounded evidence after hierarchical allocation")
    evidence = [by_id[x] for x in candidates]
    compact = [{k: v for k, v in x.items() if k not in {"source_context", "source_url", "source_title"}} for x in evidence]
    if len(json.dumps(compact, ensure_ascii=False).encode()) > 16000:
        raise ValueError("hierarchical evidence exceeds writer budget; do not truncate facts")
    news.save(out / "hierarchy" / f"allocation-{key}.json",
              {"selected_nodes": selected_nodes, "fact_ids": candidates, "overview": context})
    return evidence
