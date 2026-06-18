# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-06-18 / Codex（スマホ版デザイン仕様書作成）
状態: active

## 現在の状態

Phase 1 完了。デザインも一通り完成。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/
- サイドバー: 絵文字 → SVGアウトラインアイコンに刷新済み（全9ページ）
- hero: `assets/hero-wave.png` 背景 + 暗色オーバーレイ + 粒子ドット + 小型 date-card。原本画像に近い横長比率へ調整済み。
- スマホ版デザイン仕様書: `MOBILE-DESIGN-SPEC.md` 作成済み
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- RemoteTrigger: 毎朝7時（JST・平日）自動実行中

## 次の一手

1. Claudeレビュー結果 `MOBILE-DESIGN-REVIEW.md` を確認し、スマホ版実装方針を確定
2. 翌朝の自動日報生成を確認（正常なら `reports/YYYY-MM-DD.html` が追加される）

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 政策金利: ECB / RBA / RBNZ / BOC / SNB の値を月曜日報で更新
- 特定商取引法ページ: インジ・EA販売前に追加
- 過去レポート（Notion 5〜6月分）HTML移行: Phase 2 以降

## 前回AIが残した次の一手

明朝7時の自動実行を確認すること。
正常なら新規日報ファイルが `reports/YYYY-MM-DD.html` として追加され、`index.html` の最新日報カードとアーカイブが更新される。
新規日報の hero が `assets/hero-wave.png` 背景 + `.date-card` 付きで生成されているか確認する。
スマホ版については `MOBILE-DESIGN-SPEC.md` と Claudeレビュー結果を読んでから実装する。
