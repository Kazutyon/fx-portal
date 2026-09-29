# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-29 / Codex（根拠保持の修正・シャドー再試験中）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。時点/型/引用周辺の保持と全欄照合を修正し `shadow-output/2026-09-29-grounded-retry/` で少数トピックから再試験中。まだ品質合格・全文完走は未確認。旧通常thinking未完走/隔離OFF不合格の履歴は `docs/EVIDENCE-CLAUDE-MIRROR-SHADOW-20260929.md` に保持。

## 次の一手

0. ローカルQwen日報: 改訂版で2トピックを確認→全editorial照合→全日報シャドー→今日公開版と独立比較。抽出の冒頭再利用/先週混入もゲートで落とす。FF403/外為接続、全指標/休場確認、月曜補足は未解決。既存07:00ジョブは通常thinkingのまま、OFFは隔離試験だけ。明朝成功は未確認。27テストPASS/自己照合PASSを品質合格にしない。設定正本は `CLAUDE-MIRROR-SHADOW-SETTINGS.md`。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- ローカル日報の9/30定時結果と品質対策はフォローアップ正本 `FU-20260929-4AD963FE`（既存の経済指標Actions/FRED検証とは別）。

- 特定商取引法ページ: インジ・EA販売前に追加
