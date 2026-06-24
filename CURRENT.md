# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-06-24 / Codex（デイトレ適性ランキング未更新の修正）
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
- デイトレ適性: 12通貨ペアを5年ADR・直近5日ADR・4H ATR/ADX/EMA・概算コストで採点。`data/daytrade-ranking.json` の実データ生成済み。平日朝のRemoteTriggerで自動更新し、取得障害時は前回JSONを保持
- アクセス解析: GoatCounter全ページ済み
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- RemoteTrigger: 毎朝7時（JST・平日）自動実行中。`trigger_prompt.txt` は generate_index.py と完全同期済み

## 次の一手

1. 次回の平日朝7時実行で、`data/daytrade-ranking.json` の時刻が自動更新されるか確認
2. GoatCounter側でアクセス計測が入るか確認

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 特定商取引法ページ: インジ・EA販売前に追加
