# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-07-03 / Codex（規約準拠の経済指標シャドー検証基盤を実装）
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
- デイトレ適性: GitHub Actionsで平日04:30 JSTに12通貨ペアを更新。RemoteTriggerは生成済みJSONを使って07:01の日報を作成する。トップページは最新JSONも動的取得し、Actions遅延時でも更新後に表を差し替える
- 2026-07-03 09:49 JST、公開HTML・公開JSON・動的読込スクリプトの本番反映を確認済み
- 経済指標: 過去日報に掲載漏れ・別日混入を確認。構造化API＋国内2サイト照合＋公式確認の3層構成へ移行する方針を決定（`DECISIONS.md`）
- 取得元規約確認: みんかぶは非公認スクレイピング禁止。KISS FX・外貨exも明示許諾を確認できないため自動取得を保留。Trading Economicsは旧guest APIが410のため試用キー取得後に再評価
- シャドー検証: `economic_calendar_validate.py` を実装。ライセンス済みAPI・公式・承認済み手動JSONだけを入力し、2ソース一致、対象日、JST時刻、重要度、単一ソース警告を検証。日報には未接続
- 無料第1ソース: Forex Factory週間JSONのアダプターを実装。7月3日は12イベント取得、単一ソースのため安全ゲートが `publish_ready: false` にしたことを確認
- 無料第2ソース: 米BEA公式発表予定アダプターを実装。7月30日のGDP・Personal Income and Outlaysを21:30 JSTへ正規化するライブ取得に成功
- シャドー運用: GitHub Actionsで平日05:15 JSTにForex Factory＋BEAを取得・検証し、14日保存の非公開artifactへ出力する構成。本番日報には未接続
- 初回手動run `28644527327` は8秒で成功。7月3日はBEA対象指標なしのため安全ゲートが公開不可を返し、1,876 bytesの非公開artifact保存を確認
- アクセス解析: GoatCounter全ページ済み
- 法的ページ完備: about / disclaimer / privacy / terms / contact
- RemoteTrigger: 毎朝7時（JST・平日）自動実行中。`trigger_prompt.txt` は generate_index.py と完全同期済み

## 次の一手

1. Forex Factory＋BEAのシャドー結果を5営業日分蓄積する
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する
3. 雇用統計用の無料公式確認元（BLS）を別環境またはAPIで接続する
4. 5営業日後、シャドー結果を過去日報・手動閲覧した国内カレンダーと比較する
4. 次回の平日04:30 GitHub Actions定期実行が07:01までに成功するか確認
5. 07:01 RemoteTriggerと動的JSON読込の両方で当日ランキングが表示されるか確認
6. GoatCounter側でアクセス計測が入るか確認

## 残件・検討中

- お問い合わせ: Google フォームを作成して contact.html に埋め込む
- 特定商取引法ページ: インジ・EA販売前に追加
