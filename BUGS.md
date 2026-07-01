# BUGS.md — fx-portal

## BUG-002 デイトレ適性ランキングJSONが生成されず準備中表示のまま

**発生日:** 2026-06-24
**発見者:** ユーザー
**状態:** 修正済み（GitHub Actionsへ分離、次回定期実行で継続確認）

### 症状

`index.html` の「4H デイトレ適性ランキング」が、数日経っても「初回データを準備中です」のまま更新されなかった。

### 発生条件

- 2026-06-22 に `daytrade_ranking.py` を追加後、RemoteTrigger が 2026-06-23 / 2026-06-24 の日報を生成
- ただし `data/daytrade-ranking.json` が作成・コミットされなかった

### 原因

- 自動実行手順で `python daytrade_ranking.py` の実行確認が弱く、JSON未生成でも `index.html` が公開されうる状態だった
- 追加で、`generate_index.py` の完了ログに `✅` が含まれており、Windows cp932 コンソールでは `UnicodeEncodeError` で終了する可能性があった

### 修正内容

- 手動で `python daytrade_ranking.py` を実行し、12通貨ペアの実データJSONを生成
- `python generate_index.py` で `index.html` / `archive.html` を再生成
- `generate_index.py` と `trigger_prompt.txt` の完了ログから絵文字を削除
- `trigger_prompt.txt` に `test -s data/daytrade-ranking.json` を追加し、JSON未生成のまま公開しないようにした

### 未解決点

- 2026-06-30 に再確認したところ、日報は6月25・26・29・30日分まで生成されている一方、JSONの `generated_at_jst` は `2026-06-24T17:03+09:00` のままだった。
- `daytrade_ranking.py` は取得成功が6ペア未満でも終了コード0で旧JSONを保持するため、自動実行側では失敗を検知できない。
- `test -s data/daytrade-ranking.json` はファイルの存在と非空しか確認せず、古いJSONも正常扱いする。このため6月24日の修正では再発防止になっていなかった。
- RemoteTriggerの実行ログがローカルにないため、ランキングコマンドが未実行だったのか、Yahoo Finance取得が失敗したのかという直接原因は未確定。
- `daytrade_ranking.py` は成功6ペア未満で終了コード1を返し、旧JSONを保持しつつ自動実行へ失敗を通知するよう修正した。
- `generate_index.py` は `generated_at_jst` と日報日付を比較し、古い場合は最終成功日時を赤字表示、2日以上なら「要確認」に格上げする。
- ランキング失敗時も日報本体は生成・公開を継続するよう `trigger_prompt.txt` を条件分岐へ変更した。
- 重複していたランキング実行を1日1回に整理し、存在しか確認しない `test -s` を廃止した。
- 2026-06-30 10:21 JST に12通貨ペアすべて再取得成功。次回RemoteTriggerで継続確認する。
- 2026-07-01のRemoteTrigger実行ログでYahoo Financeが403を返していたことを確認。RemoteTrigger環境固有のアクセス制限が直接原因。
- ランキング取得を平日06:40 JSTのGitHub Actionsへ分離し、RemoteTriggerは生成済みJSONの鮮度確認だけを行う構成へ変更。
- GitHub Actions手動実行 `28509755331` で取得・計算・JSONコミットがすべて成功。

## BUG-001 Twemoji 導入後にアイコンが巨大化した

**発生日:** 2026-06-19  
**発見者:** ユーザー（スクリーンショットで確認）  
**状態:** 修正済み

### 症状

ポータルトップ（index.html）で、📰・🏦 などのアイコン絵文字が巨大なグレーブロックとして表示され、レイアウトが崩壊した。

### 発生条件

- Windows 環境で国旗絵文字（🇺🇸 等）が "US" などのテキストに変換される問題を解消するため Twemoji を全ページに導入した直後
- index.html（および index.html を生成する `generate_index.py` のテンプレート）のみ該当。archive.html テンプレートは正常だった

### 原因（2段階）

1. **`base` URL の抜け**  
   `generate_index.py` の index.html テンプレート部分で Twemoji 初期化の `base` パラメータを入れ忘れた。`base` がない場合、Twemoji は廃止済みの `https://twemoji.maxcdn.com/` にリクエストするため SVG 画像が全件 404 → 壊れた `<img>` タグになった。

2. **`img.emoji` の CSS サイズ制約なし**  
   `style.css` に `img.emoji` のルールがなかったため、壊れた `<img>` タグが親要素の `font-size` を引き継いで巨大化した（`.coming-soon-icon { font-size: 38px }` など）。

### 修正内容

- `generate_index.py` 114行目: `base:'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/'` を追加
- `style.css`: `img.emoji { height: 1em !important; width: 1em !important; display: inline !important; }` を追加
- `python generate_index.py` で index.html / archive.html を再生成
- commit: `ad6abbc`（base修正）、`bea9d1b`（CSS追加）

### 教訓・再発防止

- Twemoji を新ページに追加するときは必ず `base` URL を指定する（`trigger_prompt.txt` に記載済み）
- 今後 `generate_index.py` のテンプレートを変更するときは archive.html テンプレートとの差異がないか確認する
- `img.emoji` CSS ルールが style.css にあることで、`base` 抜けがあっても巨大化はしない（二重の安全策）
