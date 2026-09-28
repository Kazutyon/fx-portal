# OpenClaw FX日報シャドー実行設計

## 目的

OpenClawでAUXEN FX日報を生成するとき、長い一括指示でコンテキストを使い切らないように、調査・設計・生成・検査を分離する。本番HTMLは変更せず、専用シャドーフォルダに成果物を保存する。

## 実行前の固定条件

- モデルはまずローカル `qwen3.6:27b` を使用する。ツール利用が必要なので、ツール非対応モデルは使わない
- 新規セッションで開始する。過去の長い会話を引き継がない
- 対象は `Z:\vscode\projects\FX\fx-portal`
- 出力先は `shadow-output\YYYY-MM-DD-openclaw-vN\`
- `reports\YYYY-MM-DD.html`、`index.html`、`archive.html`、`trigger_prompt.txt`、Git履歴は変更しない
- push・公開・本番ファイル上書きは禁止

## OpenClawへ渡す初回指示

```text
工程は3つの独立したスケジュールに分ける。各工程は新規分離セッションで、対象プロジェクトの `OPENCLAW-FX-SHADOW-MANIFEST.md` と、その工程に指定された当日フォルダ内のファイルだけを読む。`AI-RULES.md`、`CURRENT.md`、`trigger_prompt.txt`、金曜日のHTML、生成スクリプト、`report_gen.py` を工程プロンプトから直接読ませない。これらを読ませるとローカルモデルのコンテキストを圧迫する。

- Stage 1: 外部情報とランキングを調査し、`research.json` と小さな `source-*.json` だけを保存。
- Stage 2: Stage 1のJSONだけを入力に、必要セクションを持つ `report.html`、`inputs.json`、`metadata.json` を保存。
- Stage 3: 同じフォルダの成果物だけを機械検査し、`validation.json` と `comparison-notes.md` を保存。

公開・push・本番HTMLの上書きは禁止。未確認値は創作せず、公開本文に内部処理や取得状況を書かない。
```

## 分割の理由

OpenClawで最初から「調査・分析・HTML生成・Git公開」を依頼すると、調査の途中でコンテキストが膨らみ、金曜日の構造や重要データを落としやすい。各工程の結果を小さなJSON／Markdownに保存し、次工程はそのファイルだけを読み直す。

## 完了判定

シャドーの完了はファイル生成ではなく、次の4点が揃った状態とする。

1. `report.html` が金曜日の主要構造を持つ
2. `validation.json` が機械検査結果を持つ
3. `comparison-notes.md` に不足・未確認点がある
4. 本番ファイルとGitに差分がない

`PASS_WITH_NOTES` は検証成功であって公開許可ではない。カレンダーの時刻差、公式金利の再照合、ブラウザ実画面の未確認が残る場合は本番へ昇格させない。
