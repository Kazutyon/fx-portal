# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-06-19 / Claude（Twemoji導入・過去日報12件HTML移植完了・push済み）
状態: active

## 現在の状態

Phase 1 完了。デザインも一通り完成。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/
- サイドバー: 絵文字 → SVGアウトラインアイコンに刷新済み
- トップ優先情報: PC版 `.today-priority-wrap` + `.market-holiday-bar` 横並び構造。必見経済指標は全件 `<ul class="key-events-list">` で2列グリッド（スマホ1列）
- 日報アーカイブ: `archive.html` を独立ページとして新設。日付・キーワードJSリアルタイム検索付き。`index.html` からアーカイブパネルを削除
- FXマーケットニュース枠: GASから自動取得、2分ごと自動更新
- 独自ドメイン: `auxen.jp` 設定済み。DNS反映後にHTTPS enforce確認が必要
- アクセス解析: GoatCounter全ページ済み
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- RemoteTrigger: 毎朝7時（JST・平日）自動実行中。`trigger_prompt.txt` は generate_index.py と完全同期済み

## 次の一手

1. DNS反映後、`https://auxen.jp/` の表示とGitHub PagesのHTTPS enforceを確認
2. GoatCounter側でアクセス計測が入るか確認

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 政策金利: RBA / RBNZ / BOC / SNB の値を月曜日報で更新（ECBは実装済み）
- 特定商取引法ページ: インジ・EA販売前に追加
- 過去レポート（Notion 6/1〜16分）HTML移行: 完了済み（reports/2026-06-01〜16.html 全12件）
