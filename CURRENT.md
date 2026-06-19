# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-06-19 / Codex（FXマーケットニュース枠実装・push済み）
状態: active

## 現在の状態

Phase 1 完了。デザインも一通り完成。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/
- サイドバー: 絵文字 → SVGアウトラインアイコンに刷新済み（全9ページ）
- hero: `assets/hero-wave.png` 背景 + 暗色オーバーレイ + 粒子ドット + 小型 date-card。原本画像に近い横長比率へ調整済み。
- スマホ版デザイン仕様書: `MOBILE-DESIGN-SPEC.md` 作成済み
- スマホ版UX: `index.html` / `style.css` / `trigger_prompt.txt` に実装済み。390pxプレビュー確認済み。commit `e1d3013` を origin main へpush済み。
- 日報ページスマホUX: `reports/2026-06-18.html` / `style.css` / `trigger_prompt.txt` に実装済み。スマホ専用ヘッダー・小型日報hero・ジャンプメニュー・下部ナビを追加。commit `4e6c2da` を origin main へpush済み。
- FXマーケットニュース枠: `index.html` / `style.css` / `trigger_prompt.txt` に実装済み。GASから自動取得し、2分ごとに自動更新。スマホ表示・自動生成維持ルールも反映。commit `af701a1` を origin main へpush済み。
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- RemoteTrigger: 毎朝7時（JST・平日）自動実行中

## 次の一手

1. 次回の自動生成後、ニュース枠・スマホ版トップ・日報スマホ構造が維持されるか確認
2. 公開ページでFXマーケットニュースの自動取得が安定しているか確認
3. 必要ならニュース枠の件数・表示位置を微調整する

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 政策金利: ECB / RBA / RBNZ / BOC / SNB の値を月曜日報で更新
- 特定商取引法ページ: インジ・EA販売前に追加
- 過去レポート（Notion 5〜6月分）HTML移行: Phase 2 以降

## 前回AIが残した次の一手

FXマーケットニュース枠はcommit `af701a1` でpush済み。
リモートに先行していた 2026-06-19 日報生成コミットを取り込んだうえで、ニュース枠を rebase 済み。
次回の自動生成で、ニュース枠・スマホ版トップ導線・日報スマホ構造が維持されているか確認する。
