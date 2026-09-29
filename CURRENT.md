# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-29 / Codex（ID選別型も未完・採用保留）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。最新ID選別型18:03〜18:05試験は39葉/201原材料・13親まで通過し、次段の材料偏り/反対材料欠落でFAILED。原値コピーは保てたが全体要約/全文なし、独立INCOMPLETE_REJECTED。84回帰PASSを日報合格にしない。最新runは`2026-09-29-extractive-retry`、status/independent-reviewと当日証拠docを読む。

## 次の一手

0. ローカルQwen日報: BUG-014の論点偏重と不正QCを対策する。入力から論点を動的に整理し、反対条件を含む各論点の小要約を保持して統合する案と、QCの実省略ID限定schemaを少数試験から検証。テーマ/相場観は固定しない。全ツリー成立→独立検査→全文比較の順。前日NY材料、構成/反復、FF403/外為/全指標/休場/月曜も残る。9/30既存07:00結果は読み取り確認。保存資料・明示OFF・キャッシュを通常thinking/定時成功にしない。FU-20260929-4AD963FE継続、設定正本は `CLAUDE-MIRROR-SHADOW-SETTINGS.md`。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- ローカル日報の9/30定時結果と品質対策はフォローアップ正本 `FU-20260929-4AD963FE`（既存の経済指標Actions/FRED検証とは別）。

- 特定商取引法ページ: インジ・EA販売前に追加
