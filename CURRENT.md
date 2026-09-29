# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-29 / Codex（原因調査・段階別対策案、未実装）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。通常thinkingは出力6,144上限で未完走。隔離thinking-OFFは全日報を4分14秒で生成したが、Codex独立評価は不合格。FFライブ403・外為0件、時点混同・月末日付誤り・カレンダー不足が残る。`docs/EVIDENCE-CLAUDE-MIRROR-SHADOW-20260929.md` が最新証拠。

## 次の一手

0. ローカルQwen日報: NY固定の誤指示を除去し、原資料のペア/出来事時点/数値/予想・結果を束縛。前日と当日を分離した2トピック試験→全editorial照合→全日報シャドーの順で対策する（案のみ、未実装）。詳しい原因/合格条件は上記証拠の追加調査節。FF403/外為接続、指標全件照合/丸め差、休場確認、月曜補足も未解決。既存07:00ジョブは通常thinkingのまま、OFFは隔離試験だけ。明朝成功は未確認。18テストPASS/自己照合PASSを品質合格にしない。設定正本は `CLAUDE-MIRROR-SHADOW-SETTINGS.md`。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- ローカル日報の9/30定時結果と品質対策はフォローアップ正本 `FU-20260929-4AD963FE`（既存の経済指標Actions/FRED検証とは別）。

- 特定商取引法ページ: インジ・EA販売前に追加
