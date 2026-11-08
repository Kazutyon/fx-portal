# -*- coding: utf-8 -*-
"""FX日報 2026-11-02（月）生成スクリプト"""
import glob, os

TODAY = '2026-11-09'
WEEKDAY = '月'

HERO_TITLE_SUB = (
    '前営業日11/6（金）のドル円は米雇用統計の上振れで158.48円まで反発して引け、ユーロドルは1.1159付近まで安値を更新した。'
    '本日11/9（月）は米国の注目指標がなく、明日11/10の米CPIを前にボウマンFRB副議長の発言（22:40）が材料となる。'
)

SUMMARY_HEADLINE = (
    '米雇用統計の上振れで利上げ観測が強まりドル円は158.48円で引け、ユーロドルは1.11ドル台半ばへ下落。'
    '本日は明日の米CPIを控え、ボウマン副議長の発言と米株の動向が中心'
)

SUMMARY_BODY = (
    '11/6（金）のNY市場でドル円は3営業日ぶりに反発し158.48円で引けた（ザイFX）。10月の米雇用統計は失業率が予想に反して低下し、非農業部門雇用者数も予想を上回ったため、米利上げ観測が強まりドル買いが進んだ（ザイFX）。'
    'ダウ平均は237.33ドル安で、選挙後の株高は1日で終わった（ザイFX）。COMEX金12月限は39.95ドル安の4,073.55ドルと反落した（ザイFX）。'
    '本日は米国の注目度の高い指標がなく、22:40のボウマンFRB副議長の発言、27:00の米3年債入札（580億ドル）が材料（KissFX）。'
)

TOP_PAIR_BODY = (
    'ドル円は11/6に158.48円で引け、NY時間に一時158.58円まで上昇した（みんかぶ・ザイFX）。強い米雇用統計で米金利が上昇し、ドル買いが入った。上値は為替介入への思惑が抑える（KissFX）。'
    '明日11/10の米CPIを控え、本日はボウマン副議長の発言（22:40）で米金利の方向が決まる。'
    '4時間足ランキング（11/6 09:28 JST生成・本日分は未更新）ではUSD/CHFが2位（スコア82・最適、ADX41.7、下降）、USD/JPYは上位8位圏外。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    '米中間選挙後の株式調整とAI関連株の急落（みんかぶ）、為替介入への思惑、イラン情勢、フランス財政不安が重なる。'
    '明日11/10に米CPI、11/13に米PPIが控え、12/9のFOMCに向けた利上げ観測が相場の中心。'
)

KEY_EVENTS_COUNT = '3件'
KEY_EVENTS_SUMMARY = (
    '中 CPI・PPI(10:30)、米 ボウマンFRB副議長発言(22:40)、英 ベイリーBOE総裁発言(26:25)。米国の注目指標は発表なし'
)

MARKET_OVERVIEW = (
    '<strong>VIX</strong>：Investing.comの表示は25.64（前日比-9.01%）だが、取得日が「07/11」表記の遅延データで11/6終値かは未確認（要確認）。'
    '<strong>米10年債・2年債利回り</strong>：取得不可（要確認）。'
    '<strong>ドル指数（DXY）</strong>：取得不可（要確認）。'
    '<strong>金</strong>：COMEX12月限は39.95ドル安の4,073.55ドル。米雇用統計の上振れで利上げ観測が強まり、ドル高が重しとなった（ザイFX）。'
    '<strong>原油</strong>：WTIの水準は取得不可（要確認）。'
    '<strong>米株</strong>：ダウは237.33ドル安。選挙後の株高は1日で終わった（ザイFX）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％（詳細は下表）。'
    '<br><br><strong>今週の焦点：</strong> 11/10 米CPI、11/13 米PPI、日銀の主な意見、ECB理事会に向けたデータ（みんかぶ）。次回FOMCは12/9（KissFX）。'
)

RANKING_ROWS = [
    (1, 'EUR/AUD', 'rank-a', 'A', '直近スコア97・最適。ADX40.9、ADR比129.7％、方向は上昇。ユーロ高・豪ドル安の流れが継続（11/6 09:28 JST生成分）。', 'trend-up', '↑'),
    (2, 'USD/CHF', 'rank-a', 'A', '直近スコア82・最適。ADX41.7、ADR比107.5％、方向は下降。トレンド強度は高いが、金曜のドル買いで戻りが入る局面。', 'trend-down', '↓'),
    (3, 'AUD/JPY', 'rank-b', 'B', '直近スコア78・適。ADX27.4、ADR比115.6％、方向は下降。RBAは11/3に4.85%へ利上げしたが、声明が緩和寄りと評価された。', 'trend-down', '↓'),
    (4, 'GBP/USD', 'rank-c', 'C', '直近スコア57・候補。ADX34.5、方向は上昇。金曜に200日線と100日線を下抜けた（みんかぶ）。', 'trend-up', '↑'),
    (5, 'AUD/USD', 'rank-c', 'C', '直近スコア56・候補。ADX25.9、ADR比83.6％、方向は下降。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/11/06 09:28 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、11/6時点の数値。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        '米雇用統計が上振れ、ドル円は158.48円で3営業日ぶりに反発',
        '10月の米雇用統計は失業率が予想に反して低下し、非農業部門雇用者数も予想以上に増えた。米利上げ観測が強まり、NY市場のドル円は3営業日ぶりに反発して158.48円で引けた（ザイFX）。'
        'ただしみんかぶは「数字の割に反応は鈍い」と伝えており、NY時間の高値は158.58円にとどまった。',
    ),
    (
        'ユーロドルは1.1159付近まで安値を更新',
        'ロンドン時間からドル買いが継続し、NY時間にユーロドルは一時1.1159付近まで下落して安値を更新した（みんかぶ）。欧州株の下落が止まらずリスク警戒が続いたこともユーロの重しとなった。',
    ),
    (
        '米株が反落、AI関連株の急落でリスク警戒',
        'ダウは237.33ドル安。選挙後の株高は1日で終わり、懸念が強まっているとの見方が示された（ザイFX）。NY時間にはAI関連株が急落したが、その後は落ち着きを取り戻した（みんかぶ）。',
    ),
    (
        '金は4,073.55ドルへ反落、ポンドドルは主要移動平均を下抜け',
        'COMEX金12月限は39.95ドル安の4,073.55ドル。米雇用統計の上振れによる利上げ観測の強まりとドル高が重しとなった（ザイFX）。ポンドドルはNY時間に200日線と100日線を下抜けた（みんかぶ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/9月）への引継ぎ：ドル円は158.48円、ユーロドルは1.11ドル台半ばで週末を終えた。'
    '本日は米国の注目指標がなく、22:40のボウマン副議長の発言と27:00の米3年債入札が米金利の材料。'
    '明日11/10の米CPI、11/13の米PPIを前にポジション調整が出やすい。'
    '注記：ザイFX・みんかぶの記事に年表記が「2025年」とあるものがあり、日付・数値はKissFXの週末総括（ドル円158円後半、ユーロドル1.11半ば）と整合するものだけを採用した（要確認）。'
)

POINTS_EVENTS = [
    '10:30 🇨🇳 中 消費者物価指数 前年比（予想+0.8%、前回+0.9%）／生産者物価指数 前年比（予想+5.3%、前回+5.0%）',
    '14:00 🇯🇵 日 景気先行CI指数【速報値】（予想116.6〜116.7、前回118.0）',
    '16:00 🇩🇪 独 貿易収支（予想+187〜192億、前回+195億）',
    '22:40 🇺🇸 米 ボウマンFRB副議長の発言（投票権あり）',
    '24:00（翌00:00）🇺🇸 米 卸売在庫【確報値】（予想+0.6%）／グールズビー・シカゴ連銀総裁 発言（KissFXのみ・要確認）',
    '26:15（翌02:15）🇺🇸 米 バーキン・リッチモンド連銀総裁 発言（KissFXのみ・要確認）／26:25 🇬🇧 英 ベイリーBOE総裁の発言（KissFXのみ・要確認）',
    '27:00（翌03:00）🇺🇸 米 3年債入札（580億ドル、KissFXのみ・要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：米雇用統計の上振れで158円台後半、為替介入への思惑が上値を抑える',
        'ドル円は11/6に158.48円で引けた（ザイFX）。強い雇用統計で米利上げ観測が強まった一方、介入への思惑が上値を抑える（KissFX）。22:40のボウマン副議長の発言が米金利の材料。',
    ),
    (
        'ユーロ：ドル高とリスク警戒で安値更新、フランス財政不安が重し',
        'ユーロドルは1.1159付近まで下落した（みんかぶ）。KissFXはフランス国債・財政への不安を今週の重要材料に挙げている。18:30のSentix投資家信頼感（予想2.1、前回2.7、FFのみ・要確認）が次の材料。',
    ),
    (
        '米CPIを翌日に控えたポジション調整',
        '明日11/10に米CPI、11/13に米PPIが発表される（KissFX）。本日は米国の注目指標がなく、CPI前のポジション調整と米株の動向が為替を動かす。',
    ),
    (
        '休場：本日は主要市場の休場なし',
        'KissFX・ForexFactory JSONで本日の主要市場の休場は確認されない。外為どっとコムのニュース一覧は本文を取得できず、3点目の確認はできていない（要確認）。',
    ),
    (
        '今週の予定：12/9のFOMCに向けた利上げ観測',
        'FRBは10/28のFOMCで3.75〜4.00%に据え置き、次回は12/9。日銀の次回は12/18、ECBは12/17（KissFX）。日銀の主な意見とECB理事会に向けたデータが今週の材料（みんかぶ）。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('07:30', '🇦🇺 豪', 'RBA副総裁補 ハンター氏 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('10:30', '🇨🇳 中', '消費者物価指数 前年比（Kiss/FF一致）', '低', '+0.8%', '+0.9%'),
    ('10:30', '🇨🇳 中', '生産者物価指数 前年比（Kiss/FF一致）', '低', '+5.3%', '+5.0%'),
    ('14:00', '🇯🇵 日', '景気先行CI指数【速報値】（Kiss/FF一致）', '低', '116.6（FF 116.7）', '118.0'),
    ('14:00', '🇯🇵 日', '景気一致CI指数【速報値】（KissFXのみ・要確認）', '低', '119.4', '118.8'),
    ('16:00', '🇩🇪 独', '貿易収支（Kiss/FF一致）', '低', '+187億（FF +192億）', '+195億'),
    ('18:03', '🇨🇳 中', 'M2マネーサプライ 前年比（FFのみ・要確認）', '低', '+7.3%', '+7.2%'),
    ('18:03', '🇨🇳 中', '新規人民元建て融資（FFのみ・要確認）', '低', '800億元', '1兆800億元'),
    ('18:30', '🇪🇺 ユーロ圏', 'Sentix投資家信頼感（FFのみ・要確認）', '低', '2.1', '2.7'),
    ('19:15', '🇪🇺 ユーロ圏', 'ECOFIN会合／ユーログループ会合（FFのみ・要確認）', '低', '—', '—'),
    ('22:40', '🇺🇸 米', 'ボウマンFRB副議長 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('24:00', '🇺🇸 米', '卸売在庫【確報値】（KissFXのみ・要確認）', '低', '+0.6%', '+0.6%'),
    ('24:00', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（KissFXのみ・要確認）', '低', '要人発言', '—'),
    ('26:15', '🇺🇸 米', 'バーキン・リッチモンド連銀総裁 発言（KissFXのみ・要確認）', '低', '要人発言', '—'),
    ('26:25', '🇬🇧 英', 'ベイリーBOE総裁 発言（KissFXのみ・要確認）', '低', '要人発言', '—'),
    ('27:00', '🇺🇸 米', '3年債入札（KissFXのみ・要確認）', '低', '580億ドル', '—'),
]
def _key(r):
    t = r[0]
    return (int(t[:2]), int(t[3:5]))
CAL_ROWS.sort(key=_key)

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

FUNDAMENTALS_ROWS = [
    ('FRB', '🇺🇸 USD', '3.75–4.00%', 'var(--red)', 'タカ派',
     '10/28のFOMCで据え置き。11/6の米雇用統計が上振れ、利上げ観測が強まった（ザイFX）。次回FOMCは12/9。'),
    ('日銀', '🇯🇵 JPY', '1.25%', 'var(--blue)', 'タカ派',
     '10/30会合で1.25%を据え置き。12月利上げ観測が円の下支え（ザイFX）。次回会合は12/18。'),
    ('ECB', '🇪🇺 EUR', '2.50%', 'var(--red)', 'タカ派',
     '10/29の理事会で預金金利2.50%を据え置き。12月の利上げ期待は残る（みんかぶ）。次回は12/17。'),
    ('BOE', '🇬🇧 GBP', '4.00%', 'var(--red)', 'タカ派',
     '11/5のMPCで25bp利上げして4.00%（8対1、マン委員は50bpを主張・ザイFX／みんかぶ一致）。ポンドドルは金曜に200日線・100日線を下抜けた。'),
    ('RBA', '🇦🇺 AUD', '4.85%', 'var(--red)', 'タカ派（声明は緩和寄り）',
     '11/3に25bp利上げして4.85%（6対3、3名が据え置きを主張）。声明から追加利上げの警告文言が外れ、エコノミストは緩和寄りと評価。総裁は追加利上げの余地を否定せず（OrbitRemit・BabyPips等の報道。公式未確認のため要確認）。次回は12/8。'),
    ('RBNZ', '🇳🇿 NZD', '2.75%', 'var(--red)', 'タカ派寄り',
     '10/28会合は4対3で2.75%に据え置き。市場は利上げを織り込んでおり、サプライズ（Westpac・BabyPips）。3名が利上げを主張。12月に25bp利上げの予想（Westpac）。前回の「3.00%（要確認）」は誤りで訂正。'),
    ('BOC', '🇨🇦 CAD', '2.50%', 'var(--red)', 'タカ派転換',
     '10/28会合で25bp利上げして2.50%（BabyPips・Fedratecalc・Forex Fundamentals一致。中銀公式は未確認）。次回は12/9。'),
    ('SNB', '🇨🇭 CHF', '0.00%', 'var(--muted)', 'ハト派〜中立',
     '9/24会合後も0.00%を維持。次回会合は12/10（KissFX）。'),
]

_files = sorted(glob.glob('reports/*.html'), reverse=True)
_wd = {0:'月',1:'火',2:'水',3:'木',4:'金',5:'土',6:'日'}
import datetime as _dt
archive_entries = []
for _f in _files:
    _n = os.path.basename(_f)[:-5]
    if _n == TODAY:
        continue
    _d = _dt.date.fromisoformat(_n)
    archive_entries.append((f'{_n}.html', f'{_n}（{_wd[_d.weekday()]}）'))
archive_entries = archive_entries[:10]
SIDEBAR_ARCHIVE_HTML = '\n'.join(f'<li><a href="{href}">{label}</a></li>' for href, label in archive_entries)

fundamentals_rows_html = ''
for bank, currency, rate, color, stance, reason in FUNDAMENTALS_ROWS:
    fundamentals_rows_html += f'''            <tr>
              <td>{bank}</td><td>{currency}</td><td><strong>{rate}</strong></td>
              <td style="color:{color};">{stance}</td>
              <td style="font-size:12px;">{reason}</td>
            </tr>
'''

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
  <p>{HERO_TITLE_SUB}</p>
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
{SIDEBAR_ARCHIVE_HTML}
      </ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 {TODAY}（{WEEKDAY}）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_TITLE_SUB}</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>{TODAY}</strong>
        <em>月</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{SUMMARY_HEADLINE}</h3>
        <p>{SUMMARY_BODY}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>{TOP_PAIR_BODY}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red,#c0392b)">{RISK_LEVEL}</h3>
        <p>{RISK_BODY}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_EVENTS_COUNT}</h3>
        <p>{KEY_EVENTS_SUMMARY}</p>
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
            <div class="block-title">🚫 本日の市場休場</div>
            <ul class="points-list">
              <li>なし（KissFX・ForexFactory JSONに本日の主要市場休場の記載なし）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
{POINTS_EVENTS_HTML}
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
{OTHER_POINTS_HTML}
            </ul>
          </div>
        </div>
      </div>

      <div class="panel" id="ranking">
        <div class="panel-head">
          <h3>🌏 今日の市場環境</h3>
          <span>地合い・センチメント</span>
        </div>
        <div class="report-body" style="margin-bottom:20px;">
          {MARKET_OVERVIEW}
          </div>

        <div class="panel-head" style="margin-top:4px;">
          <h3>🏆 通貨ランキング</h3>
          <span>本日の優先順</span>
        </div>
        <table class="fx-table">
          <thead>
            <tr><th>ランク</th><th>ペア</th><th>4H</th></tr>
          </thead>
          <tbody>
{RANKING_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">{RANKING_NOTE}</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前営業日の相場振り返り（2026-11-06 金）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{TOPICS_HTML}
          <div class="handover">
            <strong>{HANDOVER}</strong>
          </div>
        </div>
      </div>

      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>📅 本日の経済指標カレンダー（全件）</h3>
          <span>本日の主要予定</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead>
            <tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr>
          </thead>
          <tbody>
{CAL_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はForexFactory区分。</p>
      </div>

      <div class="panel full" id="fundamentals">
        <div class="panel-head">
          <h3>🏦 主要中銀ファンダメンタルズ（週次更新）</h3>
          <span>{TODAY} 現在</span>
        </div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>政策金利</th><th>スタンス</th><th>背景・理由</th></tr></thead>
          <tbody>
{fundamentals_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。ザイFX・みんかぶ・KissFXの報道と各種ニュースで照合。前回更新（11/2）から、RBAが11/3に4.85%へ、BOEが11/5に4.00%へ利上げ。RBNZは2.75%据え置きで前回の3.00%表記を訂正。最新情報は各中銀の公式サイトでご確認ください。</p>
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
</html>
"""

with open(f'reports/{TODAY}.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'reports/{TODAY}.html generated')
