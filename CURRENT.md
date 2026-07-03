# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-07-03 / Codex（デイトレ適性ランキングの遅延耐性を改善）
状態: active

## 現在の状態

Phase 1 完了。デザインも一通り完成。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/
- サイドバー: 絵文字 → SVGアウトラインアイコンに刷新済み
- トップ優先情報: PC版 `.today-priority-wrap` + `.market-holiday-bar` 横並び構造。必見経済指標は全件 `<ul class="key-events-list">` で2列グリッド（スマホ1列）
- 日報アーカイブ: `archive.html` を独立ページとして新設。日付・キーワードJSリアルタイム検索付き。`index.html` からアーカイブパネルを削除
- FXマーケットニュース枠: GASから自動取得、2分ごと自動更新
- 独自ドメイン: `https://auxen.jp/` 稼働中。TLS証明書発行済み、`Enforce HTTPS` 有効、HTTPからHTTPSへ301リダイレクト確認済み
- 政策金利: 8中銀すべてを変数化済み。月曜は公式発表+複数ソースで最新値へ更新、火〜金曜は直近値を維持するよう `trigger_prompt.txt` と `generate_index.py` を統一済み
- デイトレ適性: GitHub Actionsで平日04:30 JSTに12通貨ペアを更新。RemoteTriggerは生成済みJSONを使って07:01の日報を作成する。トップページは最新JSONも動的取得し、Actions遅延時でも更新後に表を差し替える
- 2026-07-03 09:49 JST、公開HTML・公開JSON・動的読込スクリプトの本番反映を確認済み
- アクセス解析: GoatCounter全ページ済み
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- RemoteTrigger: 毎朝7時（JST・平日）自動実行中。`trigger_prompt.txt` は generate_index.py と完全同期済み

## 次の一手

1. 次回の平日04:30 GitHub Actions定期実行が07:01までに成功するか確認
2. 07:01 RemoteTriggerと動的JSON読込の両方で当日ランキングが表示されるか確認
3. GoatCounter側でアクセス計測が入るか確認

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 特定商取引法ページ: インジ・EA販売前に追加
