# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-29 / Codex（修正後シャドー全文生成、独立評価不合格）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。修正後の `shadow-output/2026-09-29-grounded-retry/` は全文を生成したが、独立評価REJECTED。指標網羅/休場/材料の厚みと反復が残る。最新証拠は `docs/EVIDENCE-CLAUDE-MIRROR-SHADOW-20260929.md` の15時台節。通常thinkingの出力上限問題と定時完走も未検証。

## 次の一手

0. ローカルQwen日報: 前営業日の主要材料の取得網羅、FF403/外為接続、全指標/休場照合と月曜補足を進める。条件分析と編集欄の反復も改善が必要。9/30の既存07:00結果を読み取り、通常thinkingの出力予算を別途検証する。OFFの既定化/定時完走/ゼロキャッシュ成功は未確認、自己PASSを品質合格にしない。設定正本は `CLAUDE-MIRROR-SHADOW-SETTINGS.md`。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- ローカル日報の9/30定時結果と品質対策はフォローアップ正本 `FU-20260929-4AD963FE`（既存の経済指標Actions/FRED検証とは別）。

- 特定商取引法ページ: インジ・EA販売前に追加
