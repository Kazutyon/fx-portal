# LOG

## 2026-06-22 独自ドメインHTTPS診断 / Codex

- `auxen.jp` のAレコード4件はGitHub Pages公式IPへ正しく解決。`www` CNAMEも `kazutyon.github.io` へ解決。
- `http://auxen.jp/` は200 OKのままでHTTPSへリダイレクトされない。
- `https://auxen.jp/` はコンテンツ自体はGitHubから応答するが、証明書名不一致で通常ブラウザで保護されない。
- GitHub Pages APIは `status: built` / `cname: auxen.jp` / `https_enforced: false` / `html_url: http://auxen.jp/` を返した。
- 6/19設定から3日経過しているため、待機ではなくGitHub Settings > PagesでカスタムドメインのRemove→再Saveによる証明書発行ジョブ再開が必要と判定。

## 2026-06-22 auxen.jp HTTPS復旧 / Codex

- ユーザー承認のもと、GitHub Pages APIでCustom domainを一度解除し、`auxen.jp` を再登録。
- TLS証明書が `authorization_created` → `approved` に進み、有効期限2026-09-20の `auxen.jp` / `www.auxen.jp` 証明書を確認。
- `Enforce HTTPS` を有効化。GitHub Pages APIで `status: built` / `html_url: https://auxen.jp/` / `https_enforced: true` を確認。
- `http://auxen.jp/` が301で `https://auxen.jp/` へリダイレクトし、HTTPSが証明書エラーなし200 OKを返すことを実機確認。

## 2026-06-22 主要中銀4行の政策金利更新 / Codex

- 公開トップで「要確認」だったRBA / RBNZ / BOC / SNBを更新。
- RBA: 4.35%（6/16据え置き、追加利上げ余地）。RBA Cash Rate Targetと6/16金融政策声明、複数媒体で照合。
- RBNZ: 2.25%（5/27据え置き、利上げ票あり）。RBNZ 2026年5月MPSと複数媒体で照合。
- BOC: 2.25%（6/10、5会合連続据え置き）。Bank of Canada公式Valet APIと6/10公式声明で確認。
- SNB: 0.00%（6/18据え置き、為替介入警戒）。SNB現行金利ページと6/18公式政策評価で確認。
- `index.html` / `generate_index.py` / `trigger_prompt.txt` を同じ表示に統一し、次回自動生成で「要確認」へ戻らないよう修正。

## 2026-06-22 8中銀の月曜自動更新化 / Codex

- 前回修正でRBA / RBNZ / BOC / SNBが固定値のままだったことを確認。
- `generate_index.py` に4中銀の `*_RATE` / `*_STANCE` / `*_COLOR` 変数を追加し、表のHTMLを変数参照へ変更。
- `trigger_prompt.txt` に8中銀全ての変数と更新ルールを追加。月曜は公式発表+複数ソースで全行更新、火〜金は `index.html` の直近値を引き継ぐ。
- トリガー内の例示値も現在の8中銀データと同期し、平日に古い例示値で上書きしないよう明記。

## 2026-06-19 Twemoji 絵文字アイコン大きさバグ修正 / Claude

- 原因① `generate_index.py` の index.html テンプレートで Twemoji `base` URL が抜けていた → archive.html テンプレートは正常。修正後 `python generate_index.py` 再生成 → push (commit: ad6abbc)
- 原因② `img.emoji` の CSS サイズ制約が style.css になかった → 📰・🏦 などのアイコンが大きいブロックとして表示された。`img.emoji { height: 1em !important; width: 1em !important; display: inline !important; }` を追加 → push (commit: bea9d1b) で解消確認

## 2026-06-19 index.html Twemoji base URL バグ修正 / Claude

- `generate_index.py` の index.html テンプレート（114行目）に `base` パラメータが抜けていたため、ポータルトップの国旗絵文字が壊れたimgタグとなりレイアウト崩壊していた
- archive.html テンプレート・trigger_prompt.txt には正しく入っており、index.html テンプレートだけ抜けていた
- `generate_index.py` 修正 → `python generate_index.py` 再生成 → git push 完了（commit: ad6abbc）

## 2026-06-19 Twemoji導入・国旗絵文字修正 / Claude

- Windows環境で国旗絵文字が "US"/"GB" などの文字列に変換される問題を解消
- 全15レポート（reports/2026-06-01〜19.html）+ index.html + archive.html に Twemoji（v14.0.2）を追加
- 政策金利テーブル・経済指標カレンダーの旗絵文字を復元（🇺🇸🇬🇧🇯🇵🇪🇺🇦🇺🇳🇿🇨🇦🇨🇭）
- generate_index.py / trigger_prompt.txt も同様に更新（将来の日報に自動適用）

## 2026-06-19 Notion FX日報12件 HTML移植完了 / DeepSeek

- `fx-notion-migration.md` の仕事票に従い、2026-06-01〜06-16 の日報12件をHTML生成
- 生成スクリプト: `generate_reports_from_notion.py`（データ埋め込み型、1ファイル生成）
- 全12ファイル: `reports/2026-06-01.html`〜`reports/2026-06-16.html`
- `generate_index.py` を実行し `index.html` / `archive.html` を再生成
- 月曜日分（6/1・6/8・6/15）は主要通貨ファンダメンタルズ＋市場センチメントのパネル追加済み
- git commit & push 完了
- 仕事票を `done/` へ移動、ACTIVE-LOCKS.md を released に更新

## 2026-06-19 Notion FX日報移植準備（DeepSeek仕事票 + コンテンツファイル作成） / Claude

- Notion 2026-06-01〜06-16の日報12ページをMCP経由で取得し、全文を `docs\ai-team-queue\active\fx-notion-content.md` に書き出し
- DeepSeek向け仕事票 `docs\ai-team-queue\active\fx-notion-migration.md` を発行（12ファイル・マッピングルール・完了後処理付き）
- CURRENT.md の残件欄を更新（移行フェーズの状態を明記）
- DeepSeek が仕事票を受け取り次第、reports/2026-06-01.html〜reports/2026-06-16.html の12ファイルが自動生成される予定

## 2026-06-19 デザイン刷新・archive.html新設・trigger_prompt.txt完全同期 / Claude

- PC版「今日の優先情報」: `.today-priority-grid` 2分割 → `today-priority-wrap` + `market-holiday-bar` 横並びバー構造に変更。必見経済指標は全件 `<ul class="key-events-list">` で2列グリッド表示（スマホは1列）
- 日報アーカイブ: `index.html` のアーカイブパネルを削除し `archive.html` を独立ページとして新設。日付・キーワードJSリアルタイム検索付き
- サイドバーナビ: 「日報アーカイブ」リンクを `#reports` → `archive.html` へ変更。「FXニュース」リンクを追加（#market-news）
- モバイルナビ: mobile-quick-grid と mobile-bottom-nav の `#reports` を `archive.html` に変更
- `trigger_prompt.txt`: 全上記変更を反映（今-priority-wrap構造・archive.html生成コードブロック追加・ECB_RATE変数追加）
- `style.css`: `.today-priority-wrap` / `.market-holiday-bar` / `.mh-*` / `.archive-search-*` スタイルを追加
- `python generate_index.py` 実行で index.html / archive.html 両ファイル正常生成確認済み

## 2026-06-19 ポータルトップのUI簡素化（必見経済指標全件表示） / Claude

- ユーザー方針: ポータルには「本日の市場休場」と「必見経済指標（全件）」だけを即見せる。詳細は日報へのリンクをクリックしてから
- `generate_index.py`: CARD1/CARD2/RISK_COLOR/RISK_P/CARD4 変数を削除。`KEY_EVENTS_H3/P` を `KEY_EVENTS_ITEMS`（リスト）に変更。`REPORT_SUMMARY`・`RISK_LEVEL` はアーカイブカード用に残す
- `generate_index.py` テンプレートから `summary-grid`（一言まとめ・最注目通貨・Market Risk・重要指標件数の4カード）を削除
- `generate_index.py` テンプレート: 必見経済指標カードを `<h3>/<p>` から `<ul class="key-events-list"><li>...</li></ul>` に変更（全件表示）
- `generate_index.py` テンプレート: PC版 `report-feature-header` の「まず確認:」サブテキストを削除
- `style.css`: `.key-events-list` / `.key-events-list li` スタイルを追加
- `trigger_prompt.txt`: 変数説明・テンプレートを同様に更新
- `python generate_index.py` 実行で `index.html` 再生成済み

## 2026-06-19 トップ最新日報の優先情報化 / Codex

- ユーザー要望に合わせ、トップページの最新日報枠で「本日の市場休場」と「必見経済指標」を先に確認できる構成へ変更
- `index.html` にPC用 `.today-priority-grid`、スマホ用 `.mobile-latest-points` を追加
- `style.css` に優先情報カードのPC/スマホ表示を追加
- `generate_index.py` に `MARKET_HOLIDAY_*` / `KEY_EVENTS_*` 変数を追加し、自動生成でも同じ導線を維持
- 日報アーカイブの過去カードが空欄になる問題を修正
  - 既存 `reports/*.html` から日報サブタイトル、一言まとめ、Market Risk を抽出して表示
- Windowsローカル生成でもリンクが `reports/...` 形式になるようパスを正規化
- `python -m py_compile generate_index.py` と `python generate_index.py` で確認済み
- ローカル `index.html` をブラウザでプレビュー起動済み

## 2026-06-19 トップページサイドバーSVGアイコン復旧 / Codex

- 2026-06-19の日報自動生成後、`index.html` のPCサイドバーアイコンがSVGアウトラインから絵文字へ戻っていた問題を確認
- 原因: `generate_index.py` と `trigger_prompt.txt` のindex生成テンプレートが絵文字ナビのままだった
- `index.html` / `generate_index.py` / `trigger_prompt.txt` のPCサイドバーナビをインラインSVG + `.nav-icon` へ復旧
- `generate_index.py` に欠けていたGoatCounterタグ、FXマーケットニュース枠、20件展開スクリプトも追加
- `trigger_prompt.txt` に「PC版サイドバーの絵文字アイコン禁止、SVG nav-icon固定」を明記
- `python -m py_compile generate_index.py` で構文確認済み

## 2026-06-19 GoatCounterアクセス解析導入 / Codex

- GoatCounterの計測タグを既存HTML全ページに追加
  - 対象: `index.html` / about / contact / disclaimer / privacy / terms / reports配下3ページ
- 計測先: `https://auxen.goatcounter.com/count`
- `trigger_prompt.txt` にGoatCounterタグ維持ルールを追加
  - 今後の `index.html` 再生成
  - 今後の日報HTML生成
- `privacy.html` を更新し、GoatCounterによるアクセス解析利用を明記
- GoatCounterはCookieによる個人追跡を前提にしない軽量アクセス解析として採用

## 2026-06-19 独自ドメイン auxen.jp 設定 / Codex

- ユーザー取得済みドメイン `auxen.jp` をGitHub Pagesへ向けるため、リポジトリルートに `CNAME` を追加
- `CNAME` の内容: `auxen.jp`
- GitHub公式ドキュメントでapex domainのDNS設定値を確認
  - Aレコード: `185.199.108.153` / `185.199.109.153` / `185.199.110.153` / `185.199.111.153`
  - AAAAレコード: `2606:50c0:8000::153` / `2606:50c0:8001::153` / `2606:50c0:8002::153` / `2606:50c0:8003::153`
  - `www` は `CNAME` で `kazutyon.github.io` へ向ける
- 作業時点では `auxen.jp` / `www.auxen.jp` のDNS応答なし
- DNS反映後、GitHub Pages側でHTTPS enforce確認が必要

## 2026-06-19 FXマーケットニュース枠実装 / Codex

- ユーザー提供のGoogle Apps ScriptニュースAPIを `index.html` に組み込み
- 日報アーカイブ直下、データコーナー直前に `#market-news` のニュース枠を追加
- `fetch` でGASからJSONを取得し、初回読み込み後は2分ごとに自動更新
- `もっと見る` は外部遷移ではなく、同一ページ内で5件→最大20件の展開に変更
- 日本語タイトルのみを主表示し、カードをコンパクト化
- 出典と翻訳注記は見出し横に `InvestingLive` / `自動翻訳` の小型バッジとして表示
- `style.css` にPC/スマホ共通のニュースカード表示を追加
- `trigger_prompt.txt` に自動生成後もニュース枠と自動更新スクリプトを維持する指示を追加
- GASはHTTP 200でJSON応答を確認済み
- リモートに先行していた2026-06-19日報生成コミットを取り込み、競合解消後にcommit `af701a1 Add live FX market news` を origin main へpush済み
- `もっと見る` 展開変更はcommit `fbf2743 Expand market news inline` を origin main へpush済み

## 2026-06-19 日報ページのスマホUXローカル実装 / Codex

- ユーザー提示スクショで、日報ページがスマホ表示時にPC用サイドバー/大型hero寄りで読みにくいことを確認
- `reports/2026-06-18.html` にスマホ専用 `mobile-header` / `mobile-report-hero` / `mobile-report-jump-grid` / `mobile-bottom-nav` を追加
- 日報内アンカーを整理
  - `#summary`: 一言まとめカード
  - `#points`: 今日の注目ポイント
  - `#ranking`: 通貨ランキング
  - `#calendar`: 経済指標カレンダー
  - `#review`: 前日振り返り
- `style.css` に560px以下の日報専用CSSを追加
  - スマホではPC用サイドバー/PC heroを非表示
  - 日報heroを小型化し、2列ジャンプメニューを表示
  - 表はパネル内スクロールにしてページ全体の横スクロールを避ける
- `trigger_prompt.txt` を更新し、明朝以降の自動日報にもスマホ専用構造が入るよう指示を追加
- ローカルHTMLをブラウザで開いてプレビュー可能な状態にした
- ユーザー確認後、commit `4e6c2da Add mobile report UX` を origin main へpush済み

## 2026-06-18 スマホ版UXローカル実装 / Codex

- ChatGPT評価とユーザー方針を受け、スマホ専用レイアウトをローカル実装
- `index.html` にスマホ専用 `mobile-header` / `mobile-hero` / `mobile-quick-grid` / `mobile-latest-card` / `mobile-bottom-nav` を追加
- `style.css` に560px以下専用のスマホ導線CSSを追加
  - PC版サイドバー/heroはトップページのスマホ表示のみ非表示
  - Quick Menu 2列グリッドと最新日報CTAをファーストビュー付近に配置
  - 下部固定ナビを追加
- `reports/2026-06-18.html` に `#ranking` / `#calendar` アンカーを追加
- `trigger_prompt.txt` にスマホ版UX構造維持ルールとindex生成テンプレートを反映
- ローカルChromeで390px表示を確認し、横スクロールなしを確認
- PC版表示も確認し、既存デザインが維持されていることを確認
- commit: `e1d3013 Add mobile UX layout` / push to origin main 済み

## 2026-06-18 スマホ版デザイン仕様書作成 / Codex

- 羊飼いのFXさんのスマホ表示とFX Portalのスマホ表示を比較
- PC版を縮めるだけではなく、スマホ専用の情報導線が必要と判断
- `MOBILE-DESIGN-SPEC.md` を作成
  - スマホ版のファーストビュー構成
  - Quick Menu Grid
  - Latest Report Card
  - Sticky Bottom Nav
  - 実装ステップと受け入れ条件を整理
- Claudeレビュー用の仕事票を作成
  - `docs/ai-team-queue/active/task-2026-06-18-fx-portal-mobile-design-review-claude.md`

## 2026-06-18 hero原本比率への最終調整 / Codex

- ユーザー提示の原本画像に合わせて `style.css` の hero を微調整
- 上ラベルを小さく、主題見出しを少し大きく、サブタイトルを小さく調整
- `LAST UPDATE` の date-card を縮小し、レイアウトの圧迫感を軽減
- hero 内部を上寄せに修正し、下部の銀河/波形が余白側に見える配置へ変更
- 下余白を削り、原本に近い横長比率へ調整
- ローカルプレビューを都度確認し、ユーザーOK後に反映

## 2026-06-18 hero背景画像アセット化・自動生成指示更新 / Codex

- 画像ヘッダーの波形背景を `assets/hero-wave.png` として追加
- `style.css` の `.hero` を実画像背景 + 暗色オーバーレイ + 粒子ドット + 右側 date-card の構成へ更新
- 既存日報 `reports/2026-06-17.html` / `reports/2026-06-18.html` の hero 見出しから絵文字を外し、デザイン内で折れにくい表記へ統一
- `trigger_prompt.txt` に Heroデザイン厳守ルールを追加
  - 今後の自動日報生成で `header.hero` / `.date-card` / `assets/hero-wave.png` を維持するよう明記
  - 自動commit対象に `style.css` / `assets/hero-wave.png` / `trigger_prompt.txt` を追加
- Playwright + ローカルChromeでトップ・日報のデスクトップ/モバイル表示を確認

## 2026-06-18 heroセクション高級化 / Claude Code

- h2: 「FXトレーダーの情報ハブ」→「AIと統計で相場を研究する」
- サブ: 「分析ツールを集約。」+改行 に変更
- `::before` ドットグリッド（26px間隔、1px シアン、opacity .28）
- `::after` SVGインライン波形ライン（下部60px、opacity .28/.15）
- multi-layer radial-gradient: 左上シアン光・右下ゴールド微光
- h2 text-shadow: シアングロー（opacity .10）
- hero に `position:relative; overflow:hidden` 追加、`> *` に z-index:1
- commit: `5ee2cbb` / push 済み

## 2026-06-18 サイドバーアイコンをSVGアウトラインに刷新 / Claude Code

- 全ページの絵文字ナビアイコン（🏠📰📊💹🔧🤖📈ℹ️⚠️✉️📓🔄）を廃止
- Heroicons/Linear スタイルのインラインSVGアウトラインアイコンに置き換え
- `stroke="currentColor"` で色は CSS の `--muted` → `var(--gold)` を自動継承
- `style.css` に `.nav-icon`（15×15px, opacity .7）と hover/active opacity 1 を追加
- 対象ファイル: index / about / disclaimer / privacy / terms / contact / reports/2026-06-17 / reports/2026-06-18
- commit: `329dedc` / push to origin main 済み

## 2026-06-18 AUXENロゴ・SVGファビコン追加 / Codex

- AUXEN FX Portal にブランドロゴとファビコンを追加
  - 追加: `assets/logo.svg`
  - 追加: `favicon.svg`
- 既存ページのサイドバー `AX` ロゴをSVG画像ロゴへ差し替え
  - 対象: `index.html` / about / contact / disclaimer / privacy / terms / reports配下の既存日報
- `style.css` の `.logo` を濃紺 + シアンのAUXENロゴ枠に調整
- `trigger_prompt.txt` も更新し、今後の自動生成日報・index再生成で新ロゴ参照が維持されるようにした
- サイドバーのAUXENロゴ表示サイズを約30%拡大（48px → 62px、モバイルは56px）
- GitHub Pages 反映用に commit & push 済み
  - commit: `653374b Add AUXEN logo and favicon`
  - push先: `origin main`

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
## 2026-06-22 4Hデイトレ適性ランキング実装 / Codex

- 旧「通貨強弱 Coming Soon」を「4H デイトレ適性ランキング」へ置換
- `daytrade_ranking.py` を追加
  - Yahoo Financeの5年日足と60日1時間足を取得し、完了足だけを使用
  - 5年ADR、直近5日ADR、5年比、4時間足ATR(14)、ADX(14)、EMA20/50方向を計算
  - 概算スプレッド比をコスト評価へ反映し、直近ADR 30pips未満は対象外
  - 12通貨ペアを0〜100点で採点し、`data/daytrade-ranking.json` へ安全に置換保存
  - 取得成功が6ペア未満の場合は前回JSONを保持し、空データで壊さない
- `generate_index.py` と `trigger_prompt.txt` のテンプレートを同期
  - 平日毎朝、日報生成前にランキングを更新
  - JSON未生成時は「初回データを準備中」と表示
- `style.css` に横スクロール対応テーブル、判定バッジ、注記表示を追加
- about / contact / disclaimer / privacy / terms のサイドバー表記も更新
- 検証
  - Python構文検査: OK
  - 疑似OHLCデータによるADR・ATR・ADX・EMA・採点計算: OK
  - index/archive再生成の隔離レンダリングテスト: OK
  - 実データ初回生成は外部実行枠上限のため、次回RemoteTriggerで確認予定

## 2026-06-24 デイトレ適性ランキング未更新の修正 / Codex

- ユーザー確認で、数日経っても「4H デイトレ適性ランキング」が「初回データを準備中」のままになっていると判明
- 調査結果
  - RemoteTriggerの日報更新自体は 2026-06-23 / 2026-06-24 と実行済み
  - `data/daytrade-ranking.json` が未生成で、`index.html` が準備中表示のままだった
  - `daytrade_ranking.py` を実データで手動実行したところ12通貨ペアすべて取得成功し、スクリプト本体は正常
  - `generate_index.py` の完了ログに `✅` が含まれ、Windows cp932 コンソールで `UnicodeEncodeError` になる問題も発見
- 修正内容
  - `data/daytrade-ranking.json` を実データで生成
  - `python generate_index.py` で `index.html` / `archive.html` を再生成し、ランキング表示へ反映
  - `generate_index.py` と `trigger_prompt.txt` の完了ログから絵文字を削除
  - `trigger_prompt.txt` に `test -s data/daytrade-ranking.json` を追加し、JSON未生成のまま公開しないよう手順を強化
- 検証
  - `python daytrade_ranking.py`: 12/12通貨ペア成功
  - `python generate_index.py`: OK
  - `python -m py_compile daytrade_ranking.py generate_index.py`: OK
  - `index.html` に `GBP/USD` など実ランキングが出力されることを確認
