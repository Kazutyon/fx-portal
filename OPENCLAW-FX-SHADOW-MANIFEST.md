# OpenClaw FX shadow manifest

これは各工程が読む唯一の設計メモ。大きな手順書・HTML・生成スクリプトを読まず、工程ごとの指定入力だけを使う。

## 共通

- 対象: `Z:\\vscode\\projects\\FX\\fx-portal`
- 当日フォルダ: `shadow-output\\YYYY-MM-DD-openclaw-v2\\`
- 本番 `reports`、`index.html`、`archive.html`、`data`、Git、公開処理は変更禁止。
- 公開本文に内部処理、取得失敗、OpenClaw、要確認、再確認依頼を書かない。

## Stage 1: research.json

入力は当日の公開情報と `data\\daytrade-ranking.json`。前営業日の相場材料を5件、本日の経済予定、政策金利・市場環境、当日ランキングを調べる。各材料は `headline`、`what_happened`、`why_price_moved`、`today_implication`、`source_url` を持つ。予定は `time`、`country`、`event`、`importance`、`source_url` を持つ。確認できない値は推測せず `unverified` として研究JSON内に置く。

## Stage 2: report.html

入力は同じフォルダの `research.json` と `source-*.json` のみ。HTMLは `summary`、`points`、`market overview`、`ranking`、`review`、`calendar`、月曜のみ `fundamentals` を含む。5トピック、国旗アイコン、当日ランキング、政策金利、市場環境を落とさない。未確認値を公開本文へ出さない。`inputs.json` と `metadata.json` も保存する。

## Stage 3: validation.json

入力は同じフォルダの生成物だけ。日付、5トピック、主要セクション、国旗、ランキング、政策金利、カレンダー、内部語句漏れ、本番ファイル非変更を検査する。結果は `PASS` / `PASS_WITH_NOTES` / `FAIL`。機械検査と実ブラウザ確認を分け、`comparison-notes.md` に残す。
