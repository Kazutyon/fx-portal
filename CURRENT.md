# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-10-05 / Claude（07時cronの旧パスを新パスへ修正。10/5朝は旧パスでENOENT失敗、日報未生成）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。9/30の2runは全文未完成/公開なし。Owner指示により観測版のfact_idsを内部整理用の任意ヒントへ変更し、IDの空/誤りだけではFAILにしない。本文は材料束全体の原資料で内容を照合し、根拠外の日時・数値・価格・因果だけを停止対象にする。97オフライン回帰PASS、ローカルLLM実行なし。明日07時の実機で確認。BUG-015/016参照。追加: 10/1 07時から観測版が一括版(oneshot/)を先に並走出力。Owner判断は数日比較後。9/30手動試験は62分で全文完成・全節PASS、カレンダー単一ソース表示で組立可（BUG-021）。反復とメタ文が課題。次は根拠割当の共通化。観測版はclaim-gate再確認・品質/網羅レビューを省略して短縮（BUG-019、実測は10/1朝、見込み15〜20分短縮）。また観測版は節ごとの照合FAILを記録して続行し、通った分を含むreport.htmlを必ず出す（BUG-018、99オフライン回帰PASS）。

## 次の一手

-1. 10/6 07:00の実行を確認する: OpenClaw cron 886af487（FX Portal shadow collect）の`openclaw cron runs`がok、`shadow-output/2026-10-06-local-daily/status.json`が出ること。FFが取れて2ソース照合になっているか（`calendar-source-error.json`が無いこと）、`oneshot/oneshot-checks.json`の`external_review`が`status: ok`か（Codex Luna助言レビュー、約45秒追加、記録のみ）。Qwen自身の検証は同種の取り違えを見逃すため、レビュー指摘を毎日蓄積して精度を評価する。

0. ローカルQwen日報: 今日これ以上再実行しない。次回10/1朝07時のstatus/成果物を確認し、IDの付け方ではなくニュース本文の内容品質で評価する。9/30の2失敗runを保持、特定相場テーマを固定しない。FF単一ソース/全指標/休場/月曜/品質は未解決。FU-20260929-4AD963FE継続。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- ローカル日報の9/30定時結果と品質対策はフォローアップ正本 `FU-20260929-4AD963FE`（既存の経済指標Actions/FRED検証とは別）。

- 特定商取引法ページ: インジ・EA販売前に追加
