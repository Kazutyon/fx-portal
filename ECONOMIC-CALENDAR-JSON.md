# 経済指標シャドーJSON仕様

この仕組みは本番日報へ未接続。正規ライセンスAPI、公式機関、または許可された手動出力だけを入力する。Webサイトを無断スクレイピングしない。

## 入力例

```json
{
  "source": "licensed-api-a",
  "date": "2026-07-03",
  "fetched_at": "2026-07-03T03:30:00+09:00",
  "events": [
    {
      "time_jst": "17:00",
      "country": "EU",
      "name": "ラガルドECB総裁発言",
      "importance": "high",
      "forecast": null,
      "previous": null,
      "official": false,
      "source_url": "https://example.com/event"
    }
  ]
}
```

`time_jst` は `HH:MM` または `TBD`。`importance` は `low`、`medium`、`high`。

## 検証

```powershell
python economic_calendar_validate.py `
  --date 2026-07-03 `
  --input source-a.json `
  --input source-b.json `
  --output data/economic-calendar/2026-07-03.json
```

## 公開可能判定

- 入力元が2系統以上
- JSON構造・対象日・JST時刻・重要度が正常
- 同一イベントは時刻・国・正規化名で統合
- 2系統一致または `official: true` のイベントを確認済み扱い
- 単一ソース、重要指標0件は警告

現段階の `publish_ready` はシャドー検証用であり、日報へ自動反映する許可ではない。

## 無料シャドーソース

Forex Factoryが公開している週間JSONを次で正規化できる。

```powershell
python economic_calendar_forexfactory.py `
  --date 2026-07-03 `
  --output source-forexfactory.json
```

- 配信元: `https://nfs.faireconomy.media/ff_calendar_thisweek.json`
- 取得は週1回～1日1回程度の低頻度に制限する
- 規約ページは調査環境から403のため、再配布や本番表示には未使用
- 単独入力では `publish_ready: false`。独立した第2ソースが必要
