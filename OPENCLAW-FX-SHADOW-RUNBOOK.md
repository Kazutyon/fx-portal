# OpenClaw FX日報シャドー実行設計

> 現行9/29夕方: Owner「縛りを減らす/明日自動/数日観測」により、既存GALLERIA平日07時cronは`tools/local_fx_daily.py --observation-shadow`へ接続。次回9/30 07:00 JSTを読み戻し。Qwen/64k/通常thinking、公開なし。中間評価は記録のみ、最終原資料照合は維持。今日は起動しない。9/30〜10/2の結果を見てから微調整。正本は`CLAUDE-MIRROR-SHADOW-SETTINGS.md`、証拠は`docs/EVIDENCE-FX-OBSERVATION-SETUP-20260929.md`。以下の無flag例/未接続/停止指示は当時の履歴で、現行cron引数ではない。

> 9/29午後: Owner再承認で実測済み。通常thinkingは未完走、明示OFF隔離試験だけ完走・品質不合格。証拠 `docs/EVIDENCE-CLAUDE-MIRROR-SHADOW-20260929.md`。現在「待機中/未実行」ではない。定時成功は未確認で、FF403・外為0・内容誤りが残る。OFFを通常cronへ追加していない。

> 2026-09-29最新: Owner指示でClaude同取得元へ変更。正本は `CLAUDE-MIRROR-SHADOW-SETTINGS.md`。この改訂で起動・収集・生成・試験は一切行っていない。以下の手動実行例は現在実行しない。日付別入力がない当日は自動アダプターへ進む設定、月曜補足は未実装でFAILED。本文の旧「未接続」「遮断」は変更前の記録。

> 2026-09-29改訂: 現行設計は `OPENCLAW-FX-SPLIT-DESIGN.md`。以下の旧「6つの独立したスケジュール」は廃案。既存07:00ジョブは全日報実行器へ接続済み。ただし正規の日次入力元は未接続なので、全自動完成とは扱わない。

## 現在の実行手順 — 全日報、シャドー限定

GALLERIAで次を実行する。Qwen固定。日付の省略時はJSTの当日を使う。

```powershell
python tools/local_fx_daily.py --date 2026-09-29
```

日付省略時はJST当日。既存OpenClawジョブも同じ実行器を起動する。正規の `shadow-input/YYYY-MM-DD/source-bundle.json` と `calendar.input.json`、日付別の公式金利 `policy.json` を渡す。今日9/29は保存済み資料を `shadow-output/2026-09-29-local-daily/` で再開する。入力がない日はFAILED。禁止/保留サイトを新規自動取得して補わない。

工程は記事内の文区切り抽出→事実だけの材料選別→振り返り1件ごとの執筆/原資料照合→hero/headline/summary/market/handoverを各1回→通貨/リスク/注目点を別々に執筆→PythonでHTML組込み→今日の公開ページとの比較。履歴・ツール・汎用AGENTSはモデルへ渡さない。常にQwen固定、各呼出し64k、入力24KB上限。中断時は同じ日付の同じフォルダで再開し、変更された入力/指示の工程だけ再生成する。

出力は `shadow-output/YYYY-MM-DD-local-daily/`。`report.html`、`sections.json`、`calendar.json`、`validation.json`、`comparison.json`、`stages/*`、`status.json`を読み戻す。公開HTMLは生成後に比較用としてだけ保存する。公開側にも誤りがあり得るため、差があるだけではシャドーの誤りと判定しない。`publish_ready`は常にfalse。本番日報/RemoteTrigger/pushは変更しない。

失敗時は終了コード1、`status.json`にFAILEDと具体的な理由を残す。部分生成物も `news.json` / `stages/*` に残るが、完成状態なしでは採用しない。モデルレビュー不合格のニュース欄は1回だけ新しい推論で修正。当日欄の原資料照合は未実装で、自動品質合格としない。

9/29は既存cronの手動起動で全日報を完走、公開版との内容比較は不合格。`docs/EVIDENCE-LOCAL-FX-DAILY-20260929.md` を参照。モデル5件PASSやSHADOW_COMPLETE_REVIEW_PENDINGは公開品質の合格ではない。独立した `human-review.json` / `comparison-notes.md` が検収結果を保持する。

表示だけの修正は `python tools/local_fx_daily.py --date YYYY-MM-DD --render-existing`。LLMを呼ばず同じ日付の入力/sectionsから再組込み。初回HTML/実行状態を保全し、文章品質改善とは区別する。進捗はstdoutとprogress.json、コードhashはrunner-version.jsonに保存。明朝の正規入力未接続を準備完了と扱わない。

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
