# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-06-18 / Codex（AUXENロゴサイズ調整）
状態: active

## 現在の状態

Phase 1 完了。ポータル・法的ページ・自動更新トリガーまで整備済み。

- GitHub Pages 稼働中: https://kazutyon.github.io/fx-portal/
- ポータル（index.html）: ハブ型ダッシュボード完成（最新日報 / アーカイブ / 政策金利 / Coming Soon群）
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- 全ページ: フッター + AUXENロゴ + SVGファビコン対応済み
- ブランド素材: `assets/logo.svg` / `favicon.svg`
- trigger_prompt.txt: Step 6-3 をポータル全体再生成方式に更新済み
- RemoteTrigger: 毎朝7時（JST・平日）自動実行 → 日報生成 + index.html 自動更新

## 次の一手

1. **明朝7時（2026-06-19）自動実行を確認** — 日報生成 + index.html 自動更新が動くか
2. 結果を見てフィードバック対応（デザイン・内容・モバイル表示）

## 残件・検討中

- お問い合わせページ: Google フォームを作成して contact.html に埋め込む
- 政策金利テーブル: ECB / RBA / RBNZ / BOC / SNB の現在値を要確認（月曜日報で更新ルール化済み）
- 特定商取引法ページ: インジ・EA販売を始める前に追加
- 過去レポート（Notion 5〜6月分）のHTML移行は Phase 2 以降で検討

## 前回AIが残した次の一手

明朝7時の自動実行（2026-06-19）を確認すること。
正常に動いていれば日報ファイルが `reports/2026-06-19.html` として追加され、
`index.html` の「最新日報」カードと「日報アーカイブ」が自動更新されているはず。
新規日報にも `../assets/logo.svg` と `../favicon.svg` が反映されているか確認する。
問題があれば LOG.md のエラー記録を参照してトリガー側を修正する。
