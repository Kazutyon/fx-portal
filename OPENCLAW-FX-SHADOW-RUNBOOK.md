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
FX日報のOpenClawシャドーを実行する。公開・push・本番HTMLの上書きは禁止。成果物は対象プロジェクトの shadow-output/YYYY-MM-DD-openclaw-vN/ にだけ保存する。

最初に AI-RULES.md、PROJECT-STRUCTURE.md、対象プロジェクトの CURRENT.md、FX-REPORT-REBUILD-SKILL.md、trigger_prompt.txt、直近金曜日のHTMLと生成スクリプト、report_gen.py、data/daytrade-ranking.json を読む。

一度に完成品を書かず、次の工程を順番に実行する。

A. 調査：前営業日のニュース3〜5本を、出来事・価格反応・原因・本日への引継ぎで整理。本日の予定は時刻・国・重要度・イベント名で整理。月曜日は市場環境、政策金利・スタンス、今週の焦点も整理。当日ランキングは生成時刻と数値を反映する。結果を research.json に保存する。

B. 設計：直近金曜日のHTMLを実物テンプレートにし、summary / points / market overview / ranking / review / calendar を維持する。月曜日は fundamentals を追加する。国旗アイコンを維持する。

C. 生成：report.html、inputs.json、metadata.json を専用シャドーフォルダに保存する。

D. 検査：日付、5トピック、国旗、ランキング、政策金利、市場環境、カレンダー、HTMLアンカー、内部語句漏れを確認する。comparison-notes.md に金曜日との差分、不足、未確認点を書く。visual_review は実ブラウザ確認と機械検査を分けて記録する。

内部処理の失敗、取得状況、OpenClaw、要確認、再確認依頼は公開本文に書かない。未確認の数値は創作せず、比較ノート側に残す。最後に validation.json を保存し、本番公開品質かどうかを明示する。
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
