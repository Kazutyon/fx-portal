# FX観測版の07時接続（2026-09-29）

lifecycle: evidence。設定/検証の証拠として保持。生成成功・公開許可の証拠ではない。

## Owner指示と変更

「今しばりすぎてない？ 明日自動で回せるようにして」「あとは数日みて微調整」。従来は中間の重要度QC/必須保持ID/反復修正、特定の因果構成を指示しており、当日への過剰調整の懸念があった。新しい論点必須条件を追加するのでなく、明示`--observation-shadow`で自由要約・中間評価は記録のみ・編集品質の自動修正なしへ切り替える。旧試験は保存する。

keep: `local_fx_summary_observation.py`と回帰。evidence: `shadow-output/2026-09-29-observation-setup/cron-before.json` / `cron-after.json`（設定のみ、成果物ではない）。既存ソース/日付/数値/JSON/参照/容量/ホスト/Qwenモデル/最終原資料ゲート/公開禁止は維持。中間の内容不合格は次工程の構成ヒントとして流れるので、誤要約の影響は残り得る。自己評価/全訪問を全文品質合格にしない。

## 自動接続と読戻し

- 実PC `COMPUTERNAME=GALLERIA`、CLI `gateway.mode=local`。他PCへ操作なし。
- 同じcron `886af487-0b98-4068-a379-8868e804e29f`。`0 7 * * 1-5`、Asia/Tokyo、enabled=true、stagger=0、command argv末尾`--observation-shadow`、同じPython/実行器/cwd/agent/delivery none。次回`2026-09-30 07:00:00 +09:00`をCLIで再読戻し。
- `openclaw cron status`: enabled=true / triggersEnabled=true。設定済みは定時完走ではない。手動cron run/実推論/取得/公開/サービス起動停止は実施していない。
- 同Qwen/64k/通常thinkingのまま。OFF/provider/model変更なし。全体timeoutのみ2400→5400秒、無出力240秒/排他/出力容量は不変。中央既存service noteを先に更新、新Task/常駐なし。
- FF取得拒否時は観測版だけ実在KissFXを継続して観察。不足/拒否は証拠JSONへ。確認済みへ偽装せず、未照合行は従来どおりHTML表に表示しないため、表の欠落は残る。別日のFF値/公開本文による補完なし。

## 検証・限界

90オフライン回帰PASS。新規6件は内容QCのFAIL保持/修正なし、未知参照/容量の安全停止、全元材料訪問と保持区別、編集品質での書換えなし、最終原資料FAIL維持、FF拒否時の単一ソース非確認を確認。CLI helpの引数とPython構文も確認。テストfixtureのimportance欠落はテストで検出して補正、アプリの実生成失敗とは混同しない。途中読み取りのcwd指定ミスは絶対pathで訂正し、誤った集計/変更を採用していない。

実モデルでこの観測版を完走させていない。通常thinkingの出力6144上限、ソース網羅/外為0/実際のNY発言/全指標/休場/月曜は未解決。新要約が事実を保つ保証もなく最終原資料チェックと独立検収が必要。完走/品質/明朝取得成功を保証しない。

## 観測と復旧

9/30朝のstatus、`runner-version.json`、実request、hierarchy、sections/report、validation/comparisonを確認。まず9/30〜10/2の3営業日を同じ設計で観測し、各日の素材/時点/偏り/欠落/反復/評価を比較する。出典がある材料と未取得を区別し、複数日で共通する問題だけ微調整。起動障害は別記録で対処。FU-20260929-4AD963FEを継続。

rollbackは同じcronの`--observation-shadow`を外しtimeout2400秒へ。旧方式/証拠は削除していない。コードはlocal Gitで復元可能。公開・push・別モデル・他PCへ拡大しない。

## 理念との整合性

Qwenは小入力の要約/執筆、保存QCは観測、翌日の独立評価は別担当。CURRENT/DECISIONS/設定正本/FUと実request/JSONで引継ぐ。分割を維持し今日の正解を注入しない。機械検証と内容合格を分離し、公開/採用は人間判断。失敗はBUGS/日別evidenceへ、既存cronの設定保全と排他で復旧する。
