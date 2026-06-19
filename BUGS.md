# BUGS.md — fx-portal

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
