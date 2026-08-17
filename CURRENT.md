# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-08-17 / Claude（経済指標シャドー10営業日評価・FRED第3ソース追加）
状態: active

## 現在の状態

Phase 1 完了。デザインも一通り完成。日々のFX日報・デイトレ適性ランキングは自動運用中（詳細はLOG.md）。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/（独自ドメイン `https://auxen.jp/` も稼働）
- 経済指標シャドー検証: Forex Factory（週間JSON）＋BEA（米GDP・貿易収支等）＋FRED Release Dates API（米雇用統計・CPI・PPI・JOLTS）の3ソース構成。GitHub Actionsで平日05:15 JSTに自動実行、結果は非公開artifact（14日保持）のみで本番日報には未接続
- 2026-08-03〜08-14の10営業日評価: Actions成功率10/10、高重要度確認率は改善前で1/19件（約5.3%）、`publish_ready`誤判定は0件（安全ゲート自体は正しく機能）。原因はBEAの狭いカバー範囲だったため、FREDを追加（詳細はLOG.md 2026-08-17）
- BLS公式サイト直接取得は規約上不採用（全ページ403、bot禁止ポリシー明記）。FRED APIキーは`ebisan444@gmail.com`で登録済み、値はGitHub Actions Secrets `FRED_API_KEY` にのみ保存

## 次の一手

1. 次回の雇用統計・CPI・PPI・JOLTS該当日（直近は雇用統計9/4、CPI9/11、PPI9/10、JOLTS9/1）に、FRED追加後の高重要度確認率が実際に改善するか確認する
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 特定商取引法ページ: インジ・EA販売前に追加
