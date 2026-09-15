import glob
import datetime

TODAY = '2026-09-16'
WEEKDAY = '水'

HERO_SUB = (
    '9/15（火）は米NY連銀製造業景気指数（Empire State）が予想を下回る7.6となり6月以来の低水準に落ち込み、新規受注指数も2.0へ大幅悪化した。'
    '一方で米10年債利回りは一時5.0390%まで上昇し原油価格も続伸したことでドルが下支えされ、ドル円は続伸し155円10銭で取引を終えた。'
    '同日の米20年債入札は最高落札利回り5.420%（2020年以降で最高）・応札倍率2.57倍と低調で、米国債需給の弱さも意識されている。'
    '本日9/16（水）はFOMC〈9/15-16開催〉の結果が判明する日（発表は日本時間9/17未明3:00、ウォーシュFRB議長の記者会見は3:30）で、'
    '現在3.50〜3.75%のFF金利について市場予想（KissFX・ForexFactory両ソースで一致）は25bpの追加利上げで3.75〜4.00%。'
    '15:00の英CPI、21:30の米小売売上高も注目され、木曜未明のFOMCに向けて終日ボラティリティが高まりやすい一日となる。'
)

SUMMARY_H3 = (
    'NY連銀製造業指数が急悪化も米金利上昇・原油高でドル円は155円台へ続伸。'
    '本日はFOMCの結果判明日（発表は日本時間9/17未明3:00）、25bp利上げが市場コンセンサス'
)

SUMMARY_P = (
    '9/15（火）のニューヨーク市場では、米9月NY連銀製造業景気指数（Empire State）が予想を下回る7.6となり、6月以来の低水準に落ち込んだ。'
    '特に新規受注指数は2.0へ大幅に悪化し、製造業の減速懸念が意識された。一方で米10年債利回りは一時5.0390%まで上昇し、原油価格も続伸したことで、'
    'ドル円は続伸し155円10銭で取引を終えた。同日実施された米20年債入札では最高落札利回りが5.420%と2020年以降で最高を記録し、応札倍率は2.57倍と低調で、'
    '米国債需給の弱さも意識される結果となった（ニューヨーク為替市場関連報道より）。本日9/16（水）はFOMC〈9/15-16開催〉の結果が判明する日で、発表は日本時間'
    '9/17未明3:00、ウォーシュFRB議長の記者会見は3:30から予定されている。現在のFF金利誘導目標レンジは3.50〜3.75%で、市場予想（KissFX・ForexFactory'
    '両ソースで一致）は0.25%の追加利上げによる3.75〜4.00%への引き上げだが、直近まで市場では据え置きとの見方も根強く残っており、決定は最後までもつれる'
    '可能性がある（要確認）。本日中の主要指標としては、15:00の英消費者物価指数（前年比+3.1%予想、9/17のBOE会合の判断材料）、21:30の米小売売上高'
    '（前月比+0.8%予想）があり、いずれもFOMCに向けたポジション調整の材料となりやすい。なお4Hデイトレ適性ランキングは前日9/15 07:36時点のデータを'
    '継続使用しており、本日分の自動更新は本レポート作成時点で反映されていない（要確認）。'
)

FOCUS_CURRENCY_H3 = 'USD/JPY \U0001F1FA\U0001F1F8\U0001F1EF\U0001F1F5'
FOCUS_CURRENCY_P = (
    '4Hデイトレ適性ランキング1位（2026-09-15 07:36時点データ・要確認、スコア81・最適、ADX32.8でレンジ、直近5日ADRは5年平均の117.4%）。'
    '前日はNY連銀製造業指数の悪化にもかかわらず米金利上昇・原油高でドル円は続伸し155円10銭で引けた。本日はFOMCの結果判明日（日本時間9/17未明3:00）で、'
    '25bp利上げが市場予想となっており、決定内容次第で大きく変動する可能性が高い。'
)

RISK_LEVEL = 'HIGH'
RISK_P = (
    '本日はFOMC〈9/15-16開催〉の結果が日本時間9/17未明3:00に判明する、今週の中銀ウィークの最大イベント当日にあたる。'
    '市場予想は25bp利上げで3.75〜4.00%だが、直近まで据え置き観測も根強く、結果次第でドル円・クロス円が大きく振れる可能性が高い。'
    '15:00の英CPI・21:30の米小売売上高も本日中の重要材料であり、木曜未明にかけて段階的にボラティリティが高まりやすいためHIGHとした。'
)

KEY_COUNT = '37件'
KEY_COUNT_P = '英CPI / 米小売売上高 / FOMC政策金利・声明 / FOMCメンバー見通し(SEP) / ウォーシュFRB議長記者会見 等（本日の市場休場はなし）'

# ── ranking table (top5 from data/daytrade-ranking.json, generated_at 2026-09-15 07:36 JST) ──
RANKING_ROWS = [
    ('A', 'rank-a', 'USD/JPY', 'ランキング1位（スコア81・最適）。ADX32.8でレンジ、直近5日ADRは5年平均の117.4%と値幅拡大', 'trend-range', '→'),
    ('A', 'rank-a', 'EUR/JPY', 'ランキング2位（スコア78・適）。ADX56.2で非常に強い下降トレンド、直近5日ADRは5年平均の97.2%', 'trend-down', '↓'),
    ('A', 'rank-a', 'GBP/JPY', 'ランキング3位（スコア74・適）。ADX55.2で非常に強い下降トレンド、直近5日ADRは5年平均の91.8%', 'trend-down', '↓'),
    ('B', 'rank-b', 'AUD/JPY', 'ランキング4位（スコア65・適）。ADX65.1で非常に強い下降トレンド、直近5日ADRは5年平均の81.1%', 'trend-down', '↓'),
    ('B', 'rank-b', 'NZD/USD', 'ランキング5位（スコア64・候補）。ADX34.5で下降トレンド、直近5日ADRは5年平均の83.4%', 'trend-down', '↓'),
]

MARKET_ENV_P = (
    '9/15（火）はNY連銀製造業景気指数の悪化にもかかわらず、米10年債利回りが一時5.0390%まで上昇し原油価格も続伸したことでドルが下支えされ、'
    'ドル円は155円10銭まで続伸した。米20年債入札は利回り5.420%（2020年以降最高）・応札倍率2.57倍と低調で、国債需給の弱さも意識されている。'
    '本日9/16（水）はFOMC〈9/15-16開催〉の結果判明日で、発表は日本時間9/17未明3:00、市場予想（KissFX・ForexFactory一致）は25bp利上げの3.75〜4.00%。'
    '15:00の英CPIはBOE（9/17）の判断材料、21:30の米小売売上高も終日の値動きに影響しやすく、木曜未明にかけて段階的にボラティリティが高まりやすい一日となる。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派、本日FOMCで25bp利上げ観測が市場コンセンサス・要確認） / '
    '日銀 1.00%（正常化継続・タカ派寄り、9/17-18会合で1.25%への利上げ方針と報道・要確認） / '
    '英BOE 3.75%（中立〜やや引き締め警戒、次回会合9/17に本日の英CPIが材料となる）'
)

RANKING_FOOTNOTE = (
    '※ 4Hデイトレ適性ランキングは2026-09-15 07:36 JST時点のデータ（本日分の自動更新は本レポート作成時点で未反映・要確認）。'
    '数値は目安であり、実際のエントリーは各自のルールで判断してください。本日はFOMCの結果判明日（日本時間9/17未明3:00）のため、'
    '通常のトレンドフォローに加えイベント前後の値動き・スプレッド拡大に注意してください。'
)

# ── 前日振り返り (2026-09-15) ──
REVIEW_TOPICS = [
    ('【トピック1】米NY連銀製造業景気指数が急悪化、新規受注も大幅減',
     '米9月NY連銀製造業景気指数（Empire State）は予想を下回る7.6となり、6月以来の低水準に落ち込んだ。内訳では新規受注指数が2.0へ大幅に悪化し、製造業の先行きに対する懸念が意識された。'),
    ('【トピック2】米10年債利回りが一時5.04%まで上昇、原油高も重なりドル円は155円10銭まで続伸',
     '米10年債利回りは一時5.0390%まで上昇し、原油価格の続伸も重なってドルが下支えされた。ドル円は153円台から続伸し、155円10銭で取引を終えた（ニューヨーク為替市場関連報道より）。'),
    ('【トピック3】米20年債入札が低調、最高落札利回りは2020年以降で最高に',
     '米財務省が実施した米20年債入札は、最高落札利回りが5.420%と2020年以降で最高を記録した。応札倍率も2.57倍と低調で、米国債需給の弱さが意識される結果となった。'),
    ('【トピック4】市場はFOMC結果待ちのポジション調整局面に、木曜未明の発表に注目集まる',
     'FOMC〈9/15-16開催、結果判明は9/17未明3:00JST〉を控え、市場ではポジション調整の動きが強まった。市場予想は25bpの利上げで3.75〜4.00%だが、直近まで据え置き観測も残っており、結果までは方向感が定まりにくい展開が続いている。'),
]

HANDOVER = (
    '本日（9/16水）への引継ぎ：9/15（火）はNY連銀製造業指数の急悪化にもかかわらず、米10年債利回りの上昇（一時5.0390%）と原油高がドルを下支えし、'
    'ドル円は155円10銭まで続伸した。米20年債入札は利回り2020年以降最高・応札倍率2.57倍と低調で、国債需給の弱さも意識されている。'
    '本日9/16（水）はFOMC〈9/15-16開催〉の結果が判明する日（発表は日本時間9/17未明3:00、記者会見3:30）で、市場予想は25bp利上げの3.75〜4.00%だが、'
    '据え置き観測も根強く残っている（要確認）。15:00の英CPI（BOEの判断材料）、21:30の米小売売上高にも注目しつつ、木曜未明のFOMC結果発表に向けて'
    '終日ボラティリティが段階的に高まりやすい点に留意したい。'
)

# ── 経済指標カレンダー（全件、KissFX × ForexFactory 2ソース照合） ──
CALENDAR_ROWS = [
    ('00:39', '\U0001F1F3\U0001F1FF NZ', 'GDT価格指数（ForexFactoryのみ・要確認）', '低', '—', '+0.9%', False),
    ('05:30', '\U0001F1FA\U0001F1F8 米', 'API週間統計速報（ForexFactoryのみ・要確認）', '低', '—', '—', False),
    ('06:04', '\U0001F1F3\U0001F1FF NZ', 'ウエストパック消費者信頼感（ForexFactoryのみ・要確認）', '低', '—', '80.4', False),
    ('07:45', '\U0001F1F3\U0001F1FF NZ', '第2四半期経常収支（KissFX・ForexFactory一致）', '低', '-26.00億(Kiss)/-2.57B(FF)', '-10.08億/-1.01B', False),
    ('08:50', '\U0001F1EF\U0001F1F5 日本', '機械受注【前月比】（KissFX・ForexFactory一致）', '低', '-1.2%', '+9.7%', False),
    ('08:50', '\U0001F1EF\U0001F1F5 日本', '機械受注【前年比】（KissFXのみ・要確認）', '低', '+9.6%', '+16.9%', False),
    ('08:50', '\U0001F1EF\U0001F1F5 日本', '貿易収支（KissFX・ForexFactory一致・単位換算で微差・要確認）', '低', '-10584億(Kiss)/-1.00T(FF)', '-6345億/-0.69T', False),
    ('09:30', '\U0001F1E6\U0001F1FA 豪', 'ウエストパック景気先行指数（KissFX・ForexFactory一致）', '低', '—', '+0.03%(Kiss)/0.0%(FF)', False),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '消費者物価指数【前月比】（KissFXのみ・要確認）', '高', '+0.5%', '+0.3%', True),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '消費者物価指数【前年比】（KissFX・ForexFactory一致）', '高', '+3.1%', '+2.9%', True),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '消費者物価指数【コア】（KissFX・ForexFactory一致）', '低', '+2.6%', '+2.6%', False),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '生産者物価指数（Input）【前月比】（ForexFactoryのみ・要確認）', '中', '+0.6%', '-1.7%', False),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '生産者物価指数（Output）【前月比】（KissFX・ForexFactory一致）', '高', '+0.5%', '+0.2%', False),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '生産者物価指数【前年比】（KissFXのみ・要確認）', '低', '+3.3%', '+3.1%', False),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '小売物価指数【前月比】（KissFXのみ・要確認）', '高', '+0.7%', '+0.6%', False),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '小売物価指数【前年比】（KissFX・ForexFactory一致）', '高', '+3.5%', '+3.2%', False),
    ('15:00', '\U0001F1EC\U0001F1E7 英', '小売物価指数【コア】（KissFXのみ・要確認）', '低', '—', '+3.1%', False),
    ('17:30', '\U0001F1EC\U0001F1E7 英', '住宅価格指数【前年比】（ForexFactoryのみ・要確認）', '低', '+2.1%', '+2.0%', False),
    ('18:00', '\U0001F1EA\U0001F1FA 欧', '鉱工業生産【前月比】（KissFX・ForexFactory一致）', '中', '-0.2%', '＋0.0%', False),
    ('18:00', '\U0001F1EA\U0001F1FA 欧', '鉱工業生産【前年比】（KissFXのみ・要確認）', '低', '-0.1%', '+0.1%', False),
    ('18:34', '\U0001F1E9\U0001F1EA 独', '30年債入札（ForexFactoryのみ・要確認）', '低', '—', '3.65%|1.3倍', False),
    ('20:00', '\U0001F1FA\U0001F1F8 米', 'MBA住宅ローン申請指数（KissFXのみ・要確認）', '低', '—', '-2.7%', False),
    ('21:15', '\U0001F1E8\U0001F1E6 加', '住宅着工件数（KissFX・ForexFactory一致）', '低', '24.00万件(Kiss)/243K(FF)', '22.91万件/229K', False),
    ('21:30', '\U0001F1E8\U0001F1E6 加', '住宅建設許可【前月比】（KissFX・ForexFactory一致）', '低', '-4.8%(Kiss)/-4.7%(FF)', '+18.5%', False),
    ('21:30', '\U0001F1FA\U0001F1F8 米', '小売売上高（KissFX・ForexFactory一致）', '最高', '+0.8%', '-0.6%', True),
    ('21:30', '\U0001F1FA\U0001F1F8 米', '小売売上高【除自動車】（KissFX・ForexFactory一致）', '最高', '+0.5%', '-0.3%', True),
    ('21:30', '\U0001F1FA\U0001F1F8 米', '輸入物価指数【前月比】（KissFX・ForexFactory一致・予想値微差・要確認）', '高', '+0.5%(Kiss)/+0.4%(FF)', '-0.4%', False),
    ('21:30', '\U0001F1FA\U0001F1F8 米', '輸入物価指数【前年比】（KissFXのみ・要確認）', '高', '+6.4%', '+5.9%', False),
    ('23:00', '\U0001F1FA\U0001F1F8 米', '企業在庫（KissFX・ForexFactory一致・予想値微差・要確認）', '低', '+0.8%(Kiss)/+0.6%(FF)', '＋0.0%', False),
    ('23:00', '\U0001F1FA\U0001F1F8 米', 'NAHB住宅市場指数（KissFX・ForexFactory一致）', '低', '34', '35', False),
    ('23:30', '\U0001F1FA\U0001F1F8 米', '週間原油在庫（KissFX・ForexFactory一致）', '低', '—', '-39.1万(Kiss)/-0.4M(FF)', False),
    ('翌01:00', '\U0001F1E9\U0001F1EA 独', 'ナーゲル独連銀総裁発言（KissFXのみ・要確認）', '要人発言', '—', '—', False),
    ('翌03:00', '\U0001F1FA\U0001F1F8 米', 'FOMC政策金利・声明発表（KissFX・ForexFactory週間フィード一致・独立2ソース照合済み）', '最高', '25bp利上げ/4.00%', '3.75%据え置き', True),
    ('翌03:00', '\U0001F1FA\U0001F1F8 米', 'FOMCメンバー経済見通し（SEP）（KissFX・ForexFactory一致）', '最高', '—', '—', True),
    ('翌03:30', '\U0001F1FA\U0001F1F8 米', 'ウォーシュFRB議長 記者会見（KissFX・ForexFactory一致）', '最高', '要人発言', '—', True),
    ('翌05:00', '\U0001F1FA\U0001F1F8 米', '対米証券投資【ネット長期フロー】（KissFXのみ・要確認）', '低', '—', '+1727億', False),
    ('翌05:00', '\U0001F1FA\U0001F1F8 米', '対米証券投資【ネットフロー合計】（KissFXのみ・要確認）', '低', '—', '+1335億', False),
]

CALENDAR_FOOTNOTE = (
    '※ 時刻はJST。KissFX（主・ランク付き、https://kissfx.com/article/fxdays20260916.html）とForexFactoryの機械可読カレンダー'
    '（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。'
    '両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。'
    'FOMC関連イベント（政策金利・SEP・記者会見）はKissFXの「翌03:00/03:30」表記と、ForexFactory週間フィード生データ（2026-09-16T14:00:00-04:00 = JST翌03:00）'
    'の双方で日時・内容を確認済みです。本日は主要国の市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。'
)

# ─────────────────────────────────────────────────────────

DAYS = {'Monday': '月', 'Tuesday': '火', 'Wednesday': '水', 'Thursday': '木', 'Friday': '金', 'Saturday': '土', 'Sunday': '日'}

report_files = sorted(glob.glob('reports/*.html'), reverse=True)
sidebar_items = ''
for f in report_files[:10]:
    name = f.split('/')[-1].replace('.html', '')
    try:
        d = datetime.date.fromisoformat(name)
        wd = DAYS[d.strftime('%A')]
        label = f'{name}（{wd}）'
    except Exception:
        label = name
    sidebar_items += f'<li><a href="{name}.html">{label}</a></li>\n'

key_events_li = '\n'.join(
    f'              <li>{item}</li>' for item in [
        '15:00 \U0001F1EC\U0001F1E7 英国 消費者物価指数（CPI）',
        '21:30 \U0001F1FA\U0001F1F8 米国 小売売上高',
        '翌03:00 \U0001F1FA\U0001F1F8 米国 FOMC政策金利・声明発表',
        '翌03:30 \U0001F1FA\U0001F1F8 米国 ウォーシュFRB議長 記者会見',
    ]
)

ranking_rows_html = ''
for badge, badge_class, pair, desc, trend_class, arrow in RANKING_ROWS:
    ranking_rows_html += f'''            <tr>
              <td><span class="rank-badge {badge_class}">{badge}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>
'''

review_html = ''
for title, body in REVIEW_TOPICS:
    review_html += f'''          <div class="topic">
            <div class="topic-title">{title}</div>
            {body}
          </div>
'''

calendar_rows_html = ''
for time_jst, country, name, importance, forecast, previous, important in CALENDAR_ROWS:
    badge = ' <span class="badge-important">★重要</span>' if important else ''
    if important:
        calendar_rows_html += f'            <tr><td><strong>{time_jst}</strong></td><td>{country}</td><td><strong>{name}</strong>{badge}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>\n'
    else:
        calendar_rows_html += f'            <tr><td>{time_jst}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>\n'

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FX日報 {TODAY}（{WEEKDAY}） | AUXEN FX Portal</title>
<link rel="stylesheet" href="../style.css">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../assets/logo.svg">
<script data-goatcounter="https://auxen.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="https://cdn.jsdelivr.net/npm/twemoji@14.0.2/dist/twemoji.min.js" crossorigin="anonymous"></script>
<script>document.addEventListener('DOMContentLoaded',function(){{twemoji.parse(document.body,{{folder:'svg',ext:'.svg',base:'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/'}});}});</script>
</head>
<body class="report-page">

<header class="mobile-header">
  <a href="../index.html" class="mobile-brand">
    <img src="../assets/logo.svg" alt="AUXEN">
    <span>
      <strong>AUXEN</strong>
      <em>FX Research Lab</em>
    </span>
  </a>
  <a href="#report-menu" class="mobile-menu-button" aria-label="日報メニュー">
    <span></span><span></span><span></span>
  </a>
</header>

<section class="mobile-report-hero">
  <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
  <h1>FX日報 {TODAY}（{WEEKDAY}）</h1>
  <p>{HERO_SUB}</p>
</section>

<nav class="mobile-report-jump-grid" id="report-menu" aria-label="日報メニュー">
  <a href="#summary"><span>一言まとめ</span><strong>今日の方向</strong></a>
  <a href="#points"><span>注目ポイント</span><strong>重要イベント</strong></a>
  <a href="#ranking"><span>通貨ランキング</span><strong>優先通貨</strong></a>
  <a href="#calendar"><span>重要指標</span><strong>本日の予定</strong></a>
  <a href="#review"><span>前日振り返り</span><strong>流れ確認</strong></a>
  <a href="../index.html"><span>ポータル</span><strong>トップへ</strong></a>
</nav>

<div class="app">

  <!-- Sidebar -->
  <aside class="sidebar">
    <div class="brand">
      <div class="logo"><img src="../assets/logo.svg" alt="AUXEN"></div>
      <div>
        <h1>AUXEN</h1>
        <p>FX Research Lab</p>
      </div>
    </div>

    <nav class="side-nav">
      <span class="nav-section">メイン</span>
      <a href="../index.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/></svg>ダッシュボード</a>
      <a href="#" class="active"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="12" y2="17"/></svg>日報</a>
      <a href="../archive.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><polyline points="7 16 11 11 15 14 19 7"/></svg>アーカイブ</a>
      <span class="nav-section">ツール・販売</span>
      <a href="../index.html#tools"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/><circle cx="8" cy="6" r="2"/><circle cx="17" cy="12" r="2"/><circle cx="11" cy="18" r="2"/></svg>トレードインジケーター</a>
      <span class="nav-section">サイト情報</span>
      <a href="../about.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>About</a>
      <a href="../disclaimer.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>免責事項</a>
      <a href="../contact.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>お問い合わせ</a>
    </nav>

    <div style="margin-top:28px; padding-top:20px; border-top:1px solid var(--line);">
      <p style="font-size:11px;color:var(--muted);margin:0 0 10px;letter-spacing:.06em;text-transform:uppercase;">過去のレポート</p>
      <ul class="archive-list">
{sidebar_items}      </ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 {TODAY}（{WEEKDAY}）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_SUB}</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>{TODAY}</strong>
        <em>{WEEKDAY}曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{SUMMARY_H3}</h3>
        <p>{SUMMARY_P}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>{FOCUS_CURRENCY_H3}</h3>
        <p>{FOCUS_CURRENCY_P}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red)">{RISK_LEVEL}</h3>
        <p>{RISK_P}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_COUNT}</h3>
        <p>{KEY_COUNT_P}</p>
      </div>
    </div>

    <div class="content-grid">

      <div class="panel" id="points">
        <div class="panel-head">
          <h3>⚔️ 今日の注目ポイント</h3>
          <span>経済指標・イベント</span>
        </div>
        <div class="report-body">
          <div class="points-block">
            <div class="block-title">\U0001F6AB 本日の市場休場</div>
            <ul class="points-list">
              <li>本日9/16（水）、主要国の市場休場はありません。</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">\U0001F4CC 必見経済指標（時刻順）</div>
            <ul class="points-list">
{key_events_li}
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">\U0001F441 その他注目点</div>
            <ul class="points-list">
              <li><strong>NY連銀製造業指数が急悪化も米金利上昇・原油高でドル円続伸、155円10銭で引け</strong>：米9月NY連銀製造業景気指数は予想を下回る7.6と6月以来の低水準に落ち込み、新規受注指数も2.0へ大幅悪化した。一方で米10年債利回りは一時5.0390%まで上昇し原油価格も続伸、ドルが下支えされドル円は155円10銭まで続伸した。</li>
              <li><strong>米20年債入札が低調、最高落札利回りは2020年以降で最高</strong>：米20年債入札の最高落札利回りは5.420%と2020年以降で最高を記録し、応札倍率は2.57倍と低調。米国債需給の弱さが意識されている。</li>
              <li><strong>本日はFOMC結果判明日、25bp利上げが市場コンセンサスだが据え置き観測も残る（要確認）</strong>：FOMC〈9/15-16開催〉の結果は日本時間9/17未明3:00に判明し、ウォーシュFRB議長の記者会見は3:30から。現在3.50〜3.75%のFF金利について、市場予想（KissFX・ForexFactory両ソースで一致）は25bp利上げの3.75〜4.00%だが、直近まで据え置き観測も根強く残っており最後までもつれる可能性がある。</li>
              <li><strong>4Hデイトレ適性ランキングは前日07:36時点データを継続使用（本日分は未取得・要確認）</strong>：RemoteTrigger環境からYahoo Financeへのアクセスが制限されているため、本日06:30予定のランキング自動更新ジョブの結果が本レポート作成時点で確認できていない。前日07:36時点のデータでは円クロスが上位を占めている（要確認）。</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="panel" id="ranking">
        <div class="panel-head">
          <h3>\U0001F30F 今日の市場環境</h3>
          <span>地合い・センチメント</span>
        </div>
        <div class="report-body" style="margin-bottom:20px;">
          {MARKET_ENV_P}
          </div>

        <div class="panel-head" style="margin-top:4px;">
          <h3>\U0001F3C6 通貨ランキング</h3>
          <span>本日の優先順</span>
        </div>
        <table class="fx-table">
          <thead>
            <tr><th>ランク</th><th>ペア</th><th>4H</th></tr>
          </thead>
          <tbody>
{ranking_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">{RANKING_FOOTNOTE}</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>\U0001F4F0 前日の相場振り返り（2026-09-15）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{review_html}          <div class="handover">
            <strong>{HANDOVER}</strong>
          </div>
        </div>
      </div>

      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>\U0001F4C5 本日の経済指標カレンダー（全件）</h3>
          <span>KissFX × ForexFactory 2ソース照合済み（要確認あり）</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead>
            <tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr>
          </thead>
          <tbody>
{calendar_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">{CALENDAR_FOOTNOTE}</p>
      </div>

    </div><!-- /content-grid -->

  </main>
</div>
<nav class="mobile-bottom-nav" aria-label="スマホ下部ナビ">
  <a href="../index.html">Home</a>
  <a href="#summary" class="active">日報</a>
  <a href="#calendar">指標</a>
  <a href="#report-menu">Menu</a>
</nav>
<footer class="footer">
  <div>© 2026 AUXEN FX Portal — 本サイトの情報は投資助言ではありません。FX取引はリスクを伴います。</div>
  <div class="footer-links">
    <a href="../about.html">About</a>
    <a href="../disclaimer.html">免責事項</a>
    <a href="../privacy.html">プライバシーポリシー</a>
    <a href="../terms.html">利用規約</a>
    <a href="../contact.html">お問い合わせ</a>
  </div>
</footer>
</body>
</html>"""

with open(f'reports/{TODAY}.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'reports/{TODAY}.html generated ({len(CALENDAR_ROWS)} calendar rows)')
