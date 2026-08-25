import glob, os

TODAY = '2026-08-26'
WEEKDAY = '水'
DATE_CARD_WEEKDAY = '水曜日'

HERO_SUB = (
    '前日はウォーシュFRB議長の講演を控えドル円が159円台前半でレンジ推移、'
    '米消費者信頼感指数は89.4と1月来の低水準に低下。本日は10:30の豪CPI、'
    '21:30の米個人所得・支出・GDP改定値・PCEコア・デフレーターなど米指標が集中し、'
    '引け後のNVIDIA決算にも注目が集まる。'
)

SUMMARY_H3 = '前日はウォーシュFRB議長の講演待ちでドル円がレンジ推移、本日は豪CPIと米個人消費・GDP改定値、NVIDIA決算に注目'
SUMMARY_P = (
    '前日8/25（火）はドル円が159円09銭から159円31銭のレンジで推移し、159円14銭で引けた。'
    'ウォーシュFRB議長の講演を控え方向感の乏しい値動きとなる中、8月の米消費者信頼感指数（コンファレンスボード）は89.4に低下し、'
    '1月以来の低水準を記録した。インフレと雇用への懸念の高まりが背景にある。ボストン連銀のコリンズ総裁は速やかな追加利上げを主張し、'
    'タカ派姿勢を強めた。一方、中東情勢の進展期待から原油相場が軟化し、ドル安・円安双方向への圧力が交錯した。'
    'ユーロドルは独経済の底堅さを支えに1.1670ドル近辺で下げ渋った（要確認）。'
    '本日8/26（水）は10:30に豪消費者物価指数（CPI）が発表されるほか、21:30には米個人所得・個人支出、第2四半期GDP改定値、'
    'PCEコア・デフレーター、耐久財受注など米指標が集中して発表される。米国株式市場引け後にはNVIDIAの決算発表を控えており、'
    'リスクセンチメント全般への影響が意識される一日となる。27〜29日のジャクソンホール会合を前に、ポジション調整の続く展開が想定される。'
)

TOP_CURRENCY_H3 = 'EUR/USD 🇪🇺🇺🇸'
TOP_CURRENCY_P = (
    '4Hデイトレ適性ランキング1位（スコア61・候補、ADX40.6で上昇トレンド）。21:30の米個人所得・支出、GDP改定値、耐久財受注など'
    'ドル系指標が集中して発表され、方向性が出やすい組み合わせ'
)

MARKET_RISK = 'MEDIUM'
MARKET_RISK_P = (
    '豪CPIに加え、米個人所得・支出やGDP改定値、PCEコア・デフレーターなど中〜高重要度の指標が21:30に集中するほか、'
    '株式市場引け後のNVIDIA決算がリスク資産全体のセンチメントを左右しやすい一日'
)

KEY_EVENTS_COUNT = '22件'
KEY_EVENTS_SUMMARY = '豪CPI / 米個人所得・支出・GDP改定値・PCEコア・デフレーター・耐久財受注 / NVIDIA決算 等（本日の市場休場はなし）'

POINTS_HOLIDAY = ['本日、主要国の市場休場はなし']

POINTS_EVENTS = [
    '08:50 🇯🇵 企業向けサービス価格指数（SPPI）前年比（ForexFactoryのみ・要確認）',
    '09:30 🇦🇺 ウエストパック景気先行指数（KissFX・ForexFactory両方に掲載も前回値に相違・要確認）',
    '10:30 🇦🇺 消費者物価指数（CPI）<span class="badge-important">★重要</span>（KissFX・ForexFactoryで一致）',
    '19:00 🇬🇧 CBI流通取引調査（KissFX・ForexFactoryで一致）',
    '21:30 🇺🇸 個人所得・個人支出（KissFX・ForexFactoryで一致）',
    '21:30 🇺🇸 PCEコア・デフレーター<span class="badge-important">★重要</span>（KissFX・ForexFactoryでm/mが一致、y/yはKissFXのみのため要確認）',
    '21:30 🇺🇸 第2四半期GDP改定値<span class="badge-important">★重要</span>（KissFX・ForexFactoryで一致）',
    '21:30 🇺🇸 耐久財受注（KissFX・ForexFactoryで予想・前回値に相違・要確認）',
    '米国株式市場引け後 🇺🇸 NVIDIA決算<span class="badge-important">★重要</span>（KissFXのみ・要確認）',
]

POINTS_OTHER = [
    '<strong>米消費者信頼感指数が1月来の最低水準に低下</strong>：8月は89.4となり、インフレ・雇用への懸念の高まりを反映。',
    '<strong>ドル円はウォーシュFRB議長の講演を控えレンジ推移</strong>：159円09銭〜159円31銭で方向感が乏しく、159円14銭で引け。',
    '<strong>ボストン連銀コリンズ総裁がタカ派発言</strong>：速やかな追加利上げの必要性を主張し、インフレ根強さへの警戒を示した。',
    '<strong>中東情勢の進展期待で原油が軟化</strong>：ドル安・円安双方向の圧力が交錯する展開に（要確認）。',
    '<strong>27〜29日のジャクソンホール会合を控え</strong>：ポジション調整含みの値動きが継続。',
]

MARKET_ENV_P = (
    '8/25（火）はウォーシュFRB議長の講演を控えたドル円が159円09銭〜159円31銭のレンジ推移に終始した一方、'
    '米消費者信頼感指数が1月来の最低水準（89.4）に低下し、インフレ・雇用懸念の高まりを印象付けた。'
    'ボストン連銀コリンズ総裁のタカ派発言もドルの下支えとなったが、中東情勢の進展期待による原油安がドルの重荷にもなり、'
    '方向感の定まらない一日となった。本日8/26（水）は10:30の豪CPIを皮切りに、21:30に米個人所得・支出、GDP改定値、'
    'PCEコア・デフレーター、耐久財受注など米指標が集中し、株式市場引け後のNVIDIA決算も控える。'
    '27〜29日のジャクソンホール会合を前にポジション調整の続く展開が想定される。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（据え置き継続、8/27-29ジャクソンホール会合のウォーシュ議長発言に関心集まる） / '
    '日銀 1.00%（正常化継続、7/31会合8対1で据え置き） / ECB 2.25%（預金ファシリティ金利、6/17付適用で据え置き継続）'
)

RANKING_ROWS = [
    ('A', 'rank-a', 'EUR/USD', 'ランキング1位（スコア61・候補）。ADX40.6で上昇トレンド継続、21:30の米指標集中が方向性のきっかけになりやすい', 'trend-up', '↑'),
    ('B', 'rank-b', 'USD/CHF', 'ランキング2位（スコア58・候補）。ADX26.1でレンジ、直近5日ADRは5年平均の98.2%とほぼ平年並み', 'trend-range', '→'),
    ('B', 'rank-b', 'GBP/USD', 'ランキング3位（スコア57・候補）。ADX42.9で強い上昇トレンド、CBI流通取引調査が材料', 'trend-up', '↑'),
    ('B', 'rank-b', 'USD/CAD', 'ランキング4位（スコア57・候補）。ADX28.5でレンジ、原油在庫指標がカナダドル側にも波及しやすい', 'trend-range', '→'),
    ('B', 'rank-b', 'NZD/USD', 'ランキング5位（スコア56・候補）。ADX31.0で上昇トレンド継続、米ドル系指標との綱引きに注目', 'trend-up', '↑'),
]

REVIEW_TOPICS = [
    ('【トピック1】米消費者信頼感指数が1月来の最低水準に低下',
     '8月のコンファレンスボード消費者信頼感指数は89.4となり、1月以来の低水準を記録した。インフレ長期化への懸念と雇用環境の悪化に対する警戒感の高まりが背景。'),
    ('【トピック2】ドル円はウォーシュFRB議長の講演待ちでレンジ推移',
     'ドル円はNY市場で159円09銭から159円31銭のレンジで推移し、159円14銭で引けた。ウォーシュFRB議長の講演を控え、新たな方向感を欠く展開が続いた。'),
    ('【トピック3】ボストン連銀コリンズ総裁がタカ派発言',
     'ボストン連銀のコリンズ総裁は、インフレ圧力の根強さを踏まえ、速やかな追加利上げの必要性を主張した。関税やイラン制裁を巡る材料は相場への影響が限定的だった。'),
    ('【トピック4】中東情勢の進展期待で原油が軟化',
     '中東情勢の進展期待を背景に原油相場が軟化し、ドル安・円安双方向の圧力が交錯する展開となった。ユーロドルは独経済の底堅さを支えに1.1670ドル近辺で下げ渋った（要確認）。'),
]

HANDOVER = (
    '本日（8/26水）への引継ぎ：前日のレンジ相場と消費者信頼感指数の弱さを引き継ぐ中、本日は10:30の豪CPI、'
    '21:30の米個人所得・支出・GDP改定値・PCEコア・デフレーター・耐久財受注と指標が集中し、引け後のNVIDIA決算も控える。'
    '27〜29日のジャクソンホール会合を前に、ポジション調整含みの値動きが続く。'
)

CALENDAR_ROWS = [
    ('08:50', '🇯🇵 日本', '企業向けサービス価格指数（SPPI）【前年比】（ForexFactoryのみ・要確認）', '低', '3.2%', '3.2%', False),
    ('09:30', '🇦🇺 豪', 'ウエストパック景気先行指数（KissFX・ForexFactory両方に掲載も前回値に相違：KissFX+0.04%／FF 0.0%・要確認）', '低', '—', '+0.04%', False),
    ('10:30', '🇦🇺 豪', '消費者物価指数（CPI）【前年比】（KissFX・ForexFactoryで一致）', '高', '+3.3%', '+3.8%', True),
    ('10:30', '🇦🇺 豪', 'CPI【前月比】（ForexFactoryのみ・要確認）', '低', '+0.9%', '-0.1%', False),
    ('10:30', '🇦🇺 豪', 'トリム平均CPI【前月比】（ForexFactoryのみ・要確認）', '中', '+0.4%', '+0.3%', False),
    ('10:30', '🇦🇺 豪', '建設work done【前期比】（ForexFactoryのみ・要確認）', '低', '+0.5%', '+3.4%', False),
    ('17:00', '🇨🇭 スイス', 'UBS景況感期待指数（ForexFactoryのみ・要確認）', '低', '—', '10.0', False),
    ('19:00', '🇬🇧 英', 'CBI流通取引調査（KissFX・ForexFactoryで一致）', '低', '-35', '-26', False),
    ('20:00', '🇺🇸 米国', 'MBA住宅ローン申請指数（KissFXのみ・要確認）', '低', '—', '-0.4%', False),
    ('21:30', '🇺🇸 米国', '個人所得【前月比】（KissFX・ForexFactoryで一致）', '中', '+0.2%', '+0.2%', False),
    ('21:30', '🇺🇸 米国', '個人支出【前月比】（KissFX・ForexFactoryで一致）', '中', '+0.1%', '+0.3%', False),
    ('21:30', '🇺🇸 米国', 'PCEデフレーター【前年比】（KissFXのみ・要確認）', '高', '+3.6%', '+3.7%', False),
    ('21:30', '🇺🇸 米国', 'PCEコア・デフレーター【前月比】（KissFX・ForexFactoryで一致）', '高', '+0.2%', '+0.1%', True),
    ('21:30', '🇺🇸 米国', 'PCEコア・デフレーター【前年比】（KissFXのみ・要確認）', '高', '+3.3%', '+3.3%', False),
    ('21:30', '🇺🇸 米国', '第2四半期GDP【改定値・前期比年率】（KissFX・ForexFactoryで一致）', '高', '+1.5%', '+1.5%', True),
    ('21:30', '🇺🇸 米国', 'GDPデフレーター【改定値・前期比年率】（KissFX・ForexFactoryで一致）', '中', '+6.2%', '+6.2%', False),
    ('21:30', '🇺🇸 米国', '個人消費【改定値・前期比年率】（KissFXのみ・要確認）', '高', '+3.2%', '+3.2%', False),
    ('21:30', '🇺🇸 米国', '耐久財受注【前月比】（KissFX予想+0.5%/前回+0.5%、ForexFactory予想+0.4%/前回+0.3%・相違のため要確認）', '中', '+0.4〜0.5%', '+0.3〜0.5%', False),
    ('21:30', '🇺🇸 米国', '耐久財受注（除輸送用機器）【前月比】（KissFX前回+0.7%、ForexFactory前回+0.6%・相違のため要確認）', '中', '+0.6%', '+0.6〜0.7%', False),
    ('23:30', '🇺🇸 米国', '週間原油在庫（KissFX・ForexFactoryで概ね一致、予想はForexFactoryのみ掲載）', '低', '+160万バレル', '+440.5万バレル', False),
    ('24:45', '🇺🇸 米国', 'バーキン総裁発言（KissFXは24:45、ForexFactoryは05:00表記で時刻相違・要確認）', '要人発言', '—', '—', False),
    ('26:00（翌02:00）', '🇺🇸 米国', '5年債入札（KissFXのみ・要確認）', '中', '700億ドル', '—', False),
    ('米国株式市場引け後', '🇺🇸 米国', 'NVIDIA決算（KissFXのみ・要確認）', '高', '—', '—', True),
]

# ── HTML構築 ────────────────────────────────────────────
report_files = sorted(glob.glob('reports/*.html'), reverse=True)
sidebar_items = ''
for f in report_files[:10]:
    name = os.path.basename(f).replace('.html', '')
    if name == TODAY:
        continue
DAYS = {'Monday': '月', 'Tuesday': '火', 'Wednesday': '水', 'Thursday': '木', 'Friday': '金', 'Saturday': '土', 'Sunday': '日'}
import datetime as _dt
archive_links = []
for f in report_files:
    name = os.path.basename(f).replace('.html', '')
    if name == TODAY:
        continue
    try:
        d = _dt.date.fromisoformat(name)
        wd = DAYS[d.strftime('%A')]
        label = f'{name}（{wd}）'
    except Exception:
        label = name
    archive_links.append(f'<li><a href="{name}.html">{label}</a></li>')
    if len(archive_links) >= 10:
        break
SIDEBAR_ARCHIVE = '\n'.join(archive_links)

POINTS_HOLIDAY_HTML = '\n'.join(f'              <li>{x}</li>' for x in POINTS_HOLIDAY)
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{x}</li>' for x in POINTS_EVENTS)
POINTS_OTHER_HTML = '\n'.join(f'              <li>{x}</li>' for x in POINTS_OTHER)

RANKING_ROWS_HTML = ''
for badge, badge_class, pair, desc, trend_class, arrow in RANKING_ROWS:
    RANKING_ROWS_HTML += f'''            <tr>
              <td><span class="rank-badge {badge_class}">{badge}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>
'''

REVIEW_TOPICS_HTML = ''
for title, body in REVIEW_TOPICS:
    REVIEW_TOPICS_HTML += f'''          <div class="topic">
            <div class="topic-title">{title}</div>
            {body}
          </div>
'''

CALENDAR_ROWS_HTML = ''
CALENDAR_ROWS_HTML += '            <tr><td>終日</td><td>🌍 主要国</td><td>本日、主要国の市場休場はなし</td><td>—</td><td>—</td><td>—</td></tr>\n'
for time_, country, name, importance, forecast, previous, important in CALENDAR_ROWS:
    badge = ' <span class="badge-important">★重要</span>' if important else ''
    time_cell = f'<strong>{time_}</strong>' if important else time_
    name_cell = f'<strong>{name}</strong>{badge}' if important else f'{name}{badge}'
    CALENDAR_ROWS_HTML += f'            <tr><td>{time_cell}</td><td>{country}</td><td>{name_cell}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>\n'

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
{SIDEBAR_ARCHIVE}
      </ul>
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
        <em>{DATE_CARD_WEEKDAY}</em>
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
        <h3>{TOP_CURRENCY_H3}</h3>
        <p>{TOP_CURRENCY_P}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">{MARKET_RISK}</h3>
        <p>{MARKET_RISK_P}</p>
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
{POINTS_HOLIDAY_HTML}
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
{POINTS_OTHER_HTML}
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
          {MARKET_ENV_P}
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
{RANKING_ROWS_HTML}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日04:54 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-08-25）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{REVIEW_TOPICS_HTML}          <div class="handover">
            <strong>{HANDOVER}</strong>
          </div>
        </div>
      </div>

      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>📅 本日の経済指標カレンダー（全件）</h3>
          <span>KissFX × ForexFactory 2ソース照合済み（要確認あり）</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead>
            <tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr>
          </thead>
          <tbody>
{CALENDAR_ROWS_HTML}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または重要度・予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。26:00表記は日本時間翌日02:00相当です。本日の主要市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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
print(f'reports/{TODAY}.html generated')
