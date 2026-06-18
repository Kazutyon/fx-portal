# LOG

## 2026-06-18 ポータル完成・法的整備 / Claude Code

- index.html をリダイレクトから本格ポータルダッシュボードに刷新
  - ハブ構成: 最新日報フィーチャーカード / 日報アーカイブ / 政策金利テーブル / Coming Soonセクション群
  - モバイル対応: 960px以下でサイドバーが横スクロールナビバーに変化
- 法的ページ5本を新規作成: about / disclaimer / privacy / terms / contact
  - FX情報サイトとして必要な免責事項・リスク開示を記載
  - 有料化時に必要な特商法ページは将来対応として留保
- フッターを全ページ（ポータル・日報・法的ページ）に追加
- ファビコン対応: 全ページに `<link rel="icon">` 追加
  - ロゴ差し替え手順をHTMLコメントで明記（`assets/logo.png` + `favicon.ico`）
- trigger_prompt.txt Step 6-3 を全面改修
  - 旧: 単純なmeta-refreshリダイレクトを生成
  - 新: `generate_index.py` でポータル全体を再生成（日報更新のたびindex.htmlも自動更新）
  - アーカイブは `reports/` フォルダを自動スキャンして件数・カードを動的生成

## 2026-06-18 デザイン修正 + トリガー構成改善 / Claude Code

- 2026-06-18.html のデザイン崩れを修正
  - 旧テンプレート（`.site-header` / `.container` / `.callout`）が style.css に存在しないクラスを使っていた
  - AUXEN 正規構造（`.app` > `.sidebar` + `.main`）に全面書き直し
- trigger_prompt.txt を Step 6-2 AUXENデザイン参照方式に更新
  - 2026-06-17.html を読んで同じ構造で生成する方式
  - 使用禁止クラスを明示（今後のトリガー実行で再発防止）
- トリガーアーキテクチャをメタプロンプト方式に移行
  - RemoteTrigger のプロンプト = 短いメタプロンプト（`cat trigger_prompt.txt` を実行して指示読み込み）
  - 詳細指示は trigger_prompt.txt で git 管理 → トークンを公開リポジトリに含めないよう分離
  - push 認証トークンはメタプロンプト側（非公開）に保持

## 2026-06-18 git push 認証バグ修正 / Claude Code

- 原因調査：トリガーは7:02 JST に起動していたが git push が認証エラーで失敗していた
  - `git push origin main` → リモート環境に認証情報なし
  - Windows Credential Manager の認証情報はローカル PC 専用でクラウドからは使えない
- 修正：Step 6-4 の push コマンドを GitHub OAuth トークン（`gho_`）付き URL に変更
  - `git push origin main` → `git push https://TOKEN@github.com/Kazutyon/fx-portal.git main`
  - トークンは gh CLI 認証済みのもの（`repo` スコープ付き）
- trigger_prompt.txt と RemoteTrigger API 両方を更新済み
- 次の確認：明朝7時（2026-06-19）に自動実行されるか確認

## 2026-06-17 プロジェクト開始 / Claude Code

- GitHub リポジトリ `kazutyon/fx-portal` 作成
- GitHub Pages 有効化（https://kazutyon.github.io/fx-portal/）
- `style.css`・`index.html`・`reports/2026-06-17.html` を作成・push
- RemoteTrigger `trig_01TMDRWpiSDGRCze4kYCTNor` をNotion出力→HTML+GitHub Push出力に変更
  - 許可ツール：`notion-create-pages` / `notion-fetch` を削除、`Bash` + `WebFetch` のみに
  - 接続リポジトリ：`kazutyon/Deli` → `kazutyon/fx-portal` に変更
- `README.md` / `CURRENT.md` / `LOG.md` 作成
