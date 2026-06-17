# FX Portal

毎朝7時に自動生成されるFXトレード日報を公開するWebサイト。

## 概要

- **URL**: https://kazutyon.github.io/fx-portal/
- **GitHub**: https://github.com/Kazutyon/fx-portal
- **更新頻度**: 毎朝7時（JST）平日のみ自動更新
- **対象**: かずさん自身 → 将来的にFXトレーダー向けポータルへ拡張

## 構成

```
fx-portal/
├── index.html          # 最新レポートへのリダイレクト
├── style.css           # サイト全体のスタイル
└── reports/
    └── YYYY-MM-DD.html # 日付別レポート
```

## レポート内容

| セクション | 内容 |
|---|---|
| 💡 一言まとめ | 今日の方向性・最注目通貨 |
| ⚔️ 注目ポイント | 経済指標・市場休場・今週テーマ |
| 🌏 市場環境 | リスクオン/オフ・地合い |
| 📰 前日振り返り | 昨日の主要トピック3〜5本 |
| 🏆 通貨ランキング | S/A/B格付け＋理由 |
| 🏦 ファンダメンタルズ | 月曜のみ：各中銀の政策金利・スタンス |
| 📊 市場センチメント | 月曜のみ：VIX・金利・DXY等 |

## 自動化の仕組み

RemoteTrigger `trig_01TMDRWpiSDGRCze4kYCTNor` が毎朝7時に起動し、
FX情報をWebから収集 → HTMLファイル生成 → git push → GitHub Pages自動公開。

## ロードマップ

1. **Phase 1（現在）**: 毎日のレポートをHTMLで自動公開
2. **Phase 2**: デザイン改善・モバイル対応
3. **Phase 3**: チャート・ツール追加（FXトレーダー向けポータル化）
