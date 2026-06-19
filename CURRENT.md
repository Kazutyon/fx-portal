# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-06-19 / Codex（GoatCounterアクセス解析実装・push済み）
状態: active

## 現在の状態

Phase 1 完了。デザインも一通り完成。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/
- サイドバー: 絵文字 → SVGアウトラインアイコンに刷新済み（全9ページ）
- hero: `assets/hero-wave.png` 背景 + 暗色オーバーレイ + 粒子ドット + 小型 date-card。原本画像に近い横長比率へ調整済み。
- スマホ版デザイン仕様書: `MOBILE-DESIGN-SPEC.md` 作成済み
- スマホ版UX: `index.html` / `style.css` / `trigger_prompt.txt` に実装済み。390pxプレビュー確認済み。commit `e1d3013` を origin main へpush済み。
- 日報ページスマホUX: `reports/2026-06-18.html` / `style.css` / `trigger_prompt.txt` に実装済み。スマホ専用ヘッダー・小型日報hero・ジャンプメニュー・下部ナビを追加。commit `4e6c2da` を origin main へpush済み。
- FXマーケットニュース枠: `index.html` / `style.css` / `trigger_prompt.txt` に実装済み。GASから自動取得し、2分ごとに自動更新。`もっと見る` は同一ページ内で最大20件まで展開。スマホ表示・自動生成維持ルールも反映。commit `fbf2743` を origin main へpush済み。
- 独自ドメイン: `auxen.jp` 用の `CNAME` を追加し、commit `90da1ee` を origin main へpush済み。DNS側設定待ち。
- アクセス解析: GoatCounter計測タグを既存HTML全ページに追加済み。`trigger_prompt.txt` と `privacy.html` も更新済み。commit `fb62b6f` を origin main へpush済み。
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- RemoteTrigger: 毎朝7時（JST・平日）自動実行中

## 次の一手

1. ドメイン管理画面で不足している `185.199.109.153` のAレコードを追加
2. DNS反映後、`https://auxen.jp/` の表示とGitHub PagesのHTTPS enforceを確認
3. GoatCounter側でアクセス計測が入るか確認

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 政策金利: ECB / RBA / RBNZ / BOC / SNB の値を月曜日報で更新
- 特定商取引法ページ: インジ・EA販売前に追加
- 過去レポート（Notion 5〜6月分）HTML移行: Phase 2 以降

## 前回AIが残した次の一手

独自ドメイン `auxen.jp` のため、リポジトリルートに `CNAME` を追加し、commit `90da1ee` でpush済み。
GoatCounterアクセス解析タグはcommit `fb62b6f` でpush済み。
次にDNS管理画面でGitHub Pages向けA/AAAAレコードを設定する。
DNS反映後、`https://auxen.jp/` と `https://www.auxen.jp/` のリダイレクト/HTTPSを確認する。
