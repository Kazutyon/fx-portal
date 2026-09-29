# CURRENT

> [!IMPORTANT]
> **このファイルの鉄則：完了済み項目を1行も残してはならない。**
> 完了したタスクは → LOG.md に移して → このファイルから物理削除する。
> **50 行を超えたら肥大化のサイン。即クリーンアップすること。**

最終更新: 2026-09-29 / Codex（Claude同取得元への設定変更、実行禁止）
状態: active

## 現在の状態

ローカルQwen日報の本番採用は保留。Claude同取得元への自動接続コードを設定したが、この改訂の実行・試験はOwner指示で行っていない。内容品質、取得実測、月曜の補足工程が未解決。

## 次の一手

0. ローカルQwen日報: `tools/claude_mirror_shadow.json` と `CLAUDE-MIRROR-SHADOW-SETTINGS.md` が現行設定。Owner指示で内部取得制限をシャドーに限定して変更し、Claudeの3ニュースサイト・KissFX/FF・平日の政策金利表継承・旧ランキングの時点表示に合わせた。既存平日07:00ジョブの入口は変更しない。改訂後は未実行・未試験、明朝成功は未確認。月曜の公式金利/センチメント補足は明示FAILED。品質対策（ペア/数値束縛、予想と結果の分離、全欄原資料照合、重複/指示文漏れ検査）、休場検証が残る。9/29旧版の品質不合格は `docs/EVIDENCE-LOCAL-FX-DAILY-20260929.md`。

1. shadow-history/への実測記録の永続化をワークフローに実装済み（`.github/workflows/economic-calendar-shadow.yml`、2026-09-14）。平日05:15 JST実行のたびにshadow-output/をshadow-history/$TARGET_DATE/へコピーしてgit commit・pushする。artifactの14日保持と違い恒久的に残る。次は数営業日〜FRED対象イベント日（雇用統計・CPI・PPI・JOLTS）を跨いで実データが蓄積されるのを待ち、shadow-history/の実データで捕捉率・重複・時刻適合を再検証する（review_on: 2026-09-30、docs/ops-workbench/follow-up-registry/FOLLOW-UP-REGISTRY.json FU-20260913-1C949F12）
2. Forex Factoryフィードの利用条件をブラウザまたは手動で最終確認する（未着手のまま）
3. 主要指標が揃った状態で、本番日報への接続を検討する（現時点はシャドーのみ、公開判断は保留）

## 残件・検討中

- 特定商取引法ページ: インジ・EA販売前に追加
