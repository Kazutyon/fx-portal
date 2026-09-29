# OpenClaw FX日報シャドー実行設計

> 2026-09-29改訂: 現行設計は `OPENCLAW-FX-SPLIT-DESIGN.md`。以下の旧「6つの独立したスケジュール」は廃案であり、新規登録・再実行に使わない。既存07:00ジョブを変更する前に全日報の実行器と検収を完成させる。

## 現在の実行手順 — ニュース工程の単体試験

GALLERIAで次を実行する。Qwen固定。日付の省略時はJSTの当日を使う。

```powershell
python tools/local_fx_news.py --date 2026-09-29 --count 3
```

これは当日07:00までに掲載されたニュースの取得→1記事ごとの事実抽出→1トピック執筆→出典照合を試す。履歴や汎用エージェント文書を推論に渡さず、Ollamaへ毎回新規メッセージを送る。OpenClawの定期起動への接続はまだ実施していない。

出力は新しい `shadow-output/YYYY-MM-DD-local-news-pilot-<実行ID>/`。`source-bundle.json`、呼出し別request/response/metrics、根拠引用、レビュー、`status.json`を確認する。正常終了でも全日報の生成成功ではない。`news.json`の `publish_ready` は常にfalseで、人の内容検収が残る。試験器はみんかぶ1サイトだけなので、主要5材料の網羅性は保証しない。

失敗時は終了コード1、`status.json`にFAILEDと具体的な理由を残す。部分生成物は `news.partial.json`だけとし、失敗したものを日報として採用しない。修正は不合格の欄に1回だけ、新しい推論で行う。

FX専用workspaceのAGENTSから静穏時間を削除済み。指定仕事は07:00でも実行し、成果物/検証結果かFAILを返す。`NO_REPLY`で完了させない。

## 旧設計の記録（実行に使用しない）

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
工程は6つの独立したスケジュールに分ける。各工程は新規分離セッションで、対象プロジェクトの `OPENCLAW-FX-SPLIT-DESIGN.md` と、その工程に指定された小JSONだけを読む。`AI-RULES.md`、`CURRENT.md`、`trigger_prompt.txt`、金曜日のHTML、生成スクリプト、`report_gen.py` を工程プロンプトから直接読ませない。これらを読ませるとローカルモデルのコンテキストを圧迫する。

- Stage 1: ニュースだけを調査して `news.json` を保存。
- Stage 2: 経済予定だけを調査して `calendar.json` を保存。
- Stage 3: 政策金利・市場環境・ランキングだけを整理して `market.json` を保存。
- Stage 4: 3つの小JSONだけを統合して `research.json` を保存。
- Stage 5: `research.json` だけから `report.html`、`inputs.json`、`metadata.json` を保存。
- Stage 6: 生成物だけを検査して `validation.json` と `comparison-notes.md` を保存。

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
