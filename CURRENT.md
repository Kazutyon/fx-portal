# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-29 / Codex（ID選別型の隔離試験中、採用保留）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。中間は原fact IDの選別/再配置だけに変更し、日付/数字/型/本文を原値で保持する隔離版を試験中。旧自由要約はleaf022の根拠外解説でFAILED。新方式は同6材料の少数実機で追加解説なし・QC PASS、80回帰PASS。ただし全体要約/全文品質は未確定。最新runは`2026-09-29-extractive-retry`、status/progressと当日証拠docを読む。

## 次の一手

0. ローカルQwen日報: ID選別版の全ツリー/保持と省略/条件と反対材料を独立検査し、全文ができた場合だけ今日の公開版と比較する。テーマ/相場観は固定しない。前日NY材料、構成/反復、FF403/外為/全指標/休場/月曜も残る。9/30既存07:00結果は読み取り確認。午後保存資料・明示OFF・キャッシュ試験を通常thinking/定時成功にしない。FU-20260929-4AD963FE継続、設定正本は `CLAUDE-MIRROR-SHADOW-SETTINGS.md`。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- ローカル日報の9/30定時結果と品質対策はフォローアップ正本 `FU-20260929-4AD963FE`（既存の経済指標Actions/FRED検証とは別）。

- 特定商取引法ページ: インジ・EA販売前に追加
