# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-14 / Claude（シャドー結果のgit永続化を実装）
状態: active

## 現在の状態

Phase 1 完了。デザインも一通り完成。日々のFX日報・デイトレ適性ランキングは自動運用中（詳細はLOG.md）。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/（独自ドメイン `https://auxen.jp/` も稼働）
- 経済指標シャドー検証: Forex Factory（週間JSON）＋BEA（米GDP・貿易収支等）＋FRED Release Dates API（米雇用統計・CPI・PPI・JOLTS）の3ソース構成。GitHub Actionsで平日05:15 JSTに自動実行、結果は非公開artifact（14日保持）のみで本番日報には未接続
- 2026-08-03〜08-14の10営業日評価: Actions成功率10/10、高重要度確認率は改善前で1/19件（約5.3%）、`publish_ready`誤判定は0件（安全ゲート自体は正しく機能）。原因はBEAの狭いカバー範囲だったため、FREDを追加（詳細はLOG.md 2026-08-17）
- BLS公式サイト直接取得は規約上不採用（全ページ403、bot禁止ポリシー明記）。FRED APIキーは`ebisan444@gmail.com`で登録済み、値はGitHub Actions Secrets `FRED_API_KEY` にのみ保存

## 次の一手

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- 特定商取引法ページ: インジ・EA販売前に追加
