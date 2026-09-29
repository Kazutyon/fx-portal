# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-29 / Codex（共通材料版は未完・不合格）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。最新共通材料版はhandoverのRBA予想断定でFAILED、全文なし、独立INCOMPLETE_REJECTED。ニュース3本/編集4欄まで、全4欄は品質FAIL。記事15件/60回帰テストPASSでも合格ではない。詳細は当日証拠doc、指標/休場/通常thinking・定時完走も未解決。

## 次の一手

0. ローカルQwen日報: 予定名/日時/予想/実績を自由な言い換えから分離し、引継ぎ欄の少数試験を先に行う。前日NYの主要材料取得、全体の編集構成/条件分析/反復、FF403/外為/全指標/休場/月曜補足も残る。9/30の既存07:00結果は読み取りで確認。通常thinking/定時/ゼロキャッシュ成功・OFF既定化は未確認。設定正本は `CLAUDE-MIRROR-SHADOW-SETTINGS.md`。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- ローカル日報の9/30定時結果と品質対策はフォローアップ正本 `FU-20260929-4AD963FE`（既存の経済指標Actions/FRED検証とは別）。

- 特定商取引法ページ: インジ・EA販売前に追加
