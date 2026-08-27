import glob, os

TODAY = '2026-08-28'
WEEKDAY = '金'

HERO_SUB = ('前日はドル円が米新規失業保険申請件数の予想比減少と7月卸売在庫速報値の改善を受けたドル買いで4営業日続伸し159円39銭で引けた一方、'
            '米7年債入札は最高落札利回り4.512％と2024年来の最高水準まで上昇し低調な結果となった。'
            '本日はジャクソンホール会合2日目のウォーシュFRB議長講演が最大の焦点となるほか、東京都区部CPI・カナダGDP・シカゴPMIが重なり、方向感を試す一日となる。')

SUMMARY_TITLE = 'ジャクソンホール会合2日目のウォーシュFRB議長講演が最大の焦点、東京都区部CPI・カナダGDPも重なる'
SUMMARY_BODY = (
    '前日8/27（木）はニューヨーク市場でドル円が4営業日連続で上昇し、終値は159円39銭と前営業日比8銭程度のドル高水準となった。'
    '米週次新規失業保険申請件数は20.8万件と市場予想（20.6万件前後）より減少し、7月卸売在庫速報値も改善したことがドルの底堅さを支えた。'
    '同日実施された440億ドルの米7年債入札は最高落札利回りが4.512％と2024年来の最高水準まで上昇し、需要の弱さが示された（要確認）。'
    '株式市場ではNVIDIA決算を受けた半導体株買いが波及し、ドイツのインフィニオンが3.5％超上昇するなど欧州株はハイテク主導で上昇した。'
    'ユーロドルはロンドン時間に原油高と米長期金利上昇を受けたドル買いが優勢となり、1.1648まで下押しした。'
    '本日8/28（金）はジャクソンホール会合2日目にあたり、23:00のウォーシュFRB議長講演が最大の注目材料となる。'
    '日本時間08:30には東京都区部消費者物価指数、21:30にはカナダの4-6月期GDPと6月分GDP、22:45にはシカゴ購買部協会景気指数、'
    '23:00にはミシガン大学消費者信頼感指数確報値も予定され、週末を控えたポジション調整も交錯しやすい一日となる。'
)

TOP_PAIR = 'USD/CAD'
TOP_PAIR_FLAGS = '🇺🇸🇨🇦'
TOP_PAIR_NOTE = ('4Hデイトレ適性ランキング1位（スコア44・見送り、ADX23.6でレンジ方向、ランキングデータは2026-08-27 07:22 JST時点で本日未更新）。'
                  '21:30のカナダGDP（前月比・4-6月期）でカナダドル側に、23:00のウォーシュFRB議長講演で米ドル側に材料が重なり、'
                  'ランキングスコアは低いものの方向性が出やすい組み合わせ')

RISK_LEVEL = 'HIGH'
RISK_NOTE = ('ジャクソンホール会合2日目にあたる23:00のウォーシュFRB議長講演が最大の注目材料で、金融政策運営に関する発言次第でドル全体が大きく振れやすい。'
             '21:30のカナダGDPや23:00の暫定ベンチマーク雇用者数改定など高重要度の指標も重なり、週末を控えたポジション調整が交錯する神経質な展開が想定される一日')

KEY_COUNT = '22件'
KEY_COUNT_NOTE = 'ウォーシュFRB議長講演（ジャクソンホール） / カナダGDP / 東京都区部CPI / シカゴPMI 等（本日の市場休場はなし）'

MARKET_HOLIDAY = '本日、主要国の市場休場はなし'

KEY_EVENTS = [
    '08:30 🇯🇵 東京都区部消費者物価指数【前年比】',
    '21:30 🇨🇦 GDP【前月比/4-6月期】',
    '22:45 🇺🇸 シカゴ購買部協会景気指数',
    '23:00 🇺🇸 ミシガン大学消費者信頼感指数【確報値】',
    '23:00 🇺🇸 ウォーシュFRB議長 講演（ジャクソンホール会合2日目）',
]

OTHER_POINTS = [
    ('ドル円は4営業日続伸、159円39銭で引け', '米週次新規失業保険申請件数の予想比減少と7月卸売在庫速報値の改善がドルの底堅さを支え、前営業日比8銭程度のドル高水準となった。'),
    ('米7年債入札は低調、最高落札利回り4.512％', '440億ドルの入札で最高落札利回りが2024年来の最高水準まで上昇し、長期金利の上昇圧力が残った（要確認）。'),
    ('欧州株はNVIDIA決算を受けハイテク主導で上昇', '独インフィニオンなど半導体関連株が3.5％超上昇し、欧州主要株式市場を押し上げた。'),
    ('27〜29日のジャクソンホール会合が進行中、本日は2日目', '23:00のウォーシュFRB議長講演が最大の注目材料となる。'),
    ('来週月曜31日が8月最終営業日', '月末フローによるポジション調整が意識されやすい時期に入る。'),
]

REVIEW_TOPICS = [
    ('ドル円は米指標の底堅さを受け4営業日続伸',
     'ニューヨーク市場でドル円は159円39銭で引け、前営業日比8銭程度のドル高となった。米週次新規失業保険申請件数が20.8万件と市場予想（20.6万件前後）より減少したほか、7月卸売在庫速報値も改善し、ドルの底堅さを支えた。'),
    ('米7年債入札が低調、長期金利の上昇圧力が残る',
     '米財務省が実施した440億ドルの7年債入札は最高落札利回りが4.512％と2024年来の最高水準まで上昇し、需要の弱さを示す結果となった（要確認）。'),
    ('NVIDIA決算を受け欧州株はハイテク主導で上昇',
     '米半導体大手NVIDIAの決算が好感され、ドイツの半導体インフィニオンが3.5％超上昇するなど、欧州主要株式市場はハイテク銘柄中心に買われた。'),
    ('ユーロドルはロンドン時間のドル買いで軟化',
     '原油高と米長期金利の上昇を受けてロンドン時間にドル買いが優勢となり、ユーロドルは1.1648まで安値を広げた。'),
]

HANDOVER = ('本日（8/28金）への引継ぎ：前日はドル円が米新規失業保険申請件数の予想比減少と卸売在庫の改善を受けたドル買いで4営業日続伸し159円39銭で引けた一方、'
            '米7年債入札の低調で長期金利の上昇圧力が残った。'
            '本日はジャクソンホール会合2日目にあたり、23:00のウォーシュFRB議長講演が最大の注目材料となるほか、'
            '21:30のカナダGDP、22:45のシカゴPMI、23:00のミシガン大学消費者信頼感指数確報値も予定される。'
            '週末を控えたポジション調整も交錯しやすい一日となる。')

RANKING_LEAD = (
    '8/27（木）はドル円が米新規失業保険申請件数の予想比減少と卸売在庫の改善を受けたドル買いで4営業日続伸し159円39銭で引けた一方、'
    '米7年債入札の低調で長期金利の上昇圧力が残った。ユーロドルはロンドン時間のドル買いで1.1648まで軟化し、欧州株はNVIDIA決算を好感してハイテク主導で上昇した。'
    '本日8/28（金）はジャクソンホール会合2日目にあたり、23:00のウォーシュFRB議長講演が最大の焦点となるほか、21:30のカナダGDP、22:45のシカゴPMIも予定される。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（据え置き継続、8/27-29ジャクソンホール会合のウォーシュ議長発言に関心集まる） / 日銀 1.00%（正常化継続、7/31会合8対1で据え置き、高田委員は1.25%への利上げを提案し否決） / ECB 2.25%（預金ファシリティ金利、6/17付適用で据え置き継続）'
)

RANKING_ROWS = [
    ('B', 'USD/CAD', 'ランキング1位（スコア44・見送り）。ADX23.6でレンジ、21:30のカナダGDPが方向性のきっかけになりやすい', 'range'),
    ('B', 'GBP/USD', 'ランキング2位（スコア43・見送り）。ADX35.3でレンジ、直近5日ADRは5年平均の56.8%と値幅は縮小気味', 'range'),
    ('B', 'AUD/USD', 'ランキング3位（スコア41・見送り）。ADX29.0で上昇トレンド継続', 'up'),
    ('B', 'EUR/USD', 'ランキング4位（スコア39・見送り）。ADX32.0でレンジ', 'range'),
    ('B', 'EUR/AUD', 'ランキング5位（スコア38・見送り）。ADX23.6で下降トレンド継続', 'down'),
]
RANKING_NOTE = ('※ 4Hデイトレ適性ランキングは2026-08-27 07:22 JST時点のデータ（本日未更新・RemoteTrigger環境の制約でYahoo Finance再取得不可のため前回値を継続使用）。'
                 '全ペアが「見送り」水準のスコアで積極的なエントリー根拠としては弱い点に留意してください。数値は目安であり、実際のエントリーは各自のルールで判断してください。')

CALENDAR_ROWS = [
    ('08:30', '🇯🇵 日', '東京都区部CPI【除く生鮮・前年比】（KissFX・ForexFactoryで一致、FF表記はTokyo Core CPI）', True, '中', '+1.8%', '+1.9%'),
    ('08:30', '🇯🇵 日', '東京都区部CPI【総合・前年比】（KissFXのみ・要確認）', False, '中', '+1.9%', '+2.0%'),
    ('08:30', '🇯🇵 日', '失業率（KissFX・ForexFactoryで一致）', False, '低', '2.5%', '2.5%'),
    ('08:30', '🇯🇵 日', '有効求人倍率（KissFXのみ・要確認）', False, '低', '1.19', '1.18'),
    ('12:15', '🌍 各国', 'ジャクソンホール会合（2日目、ForexFactoryのみ・要確認）', False, '中', '—', '—'),
    ('15:00', '🇩🇪 独', '輸入物価指数【前月比/前年比】（KissFX・ForexFactoryで一致）', False, '低', '+0.3%/+6.9%', '-0.7%/+6.1%'),
    ('15:45', '🇫🇷 仏', '消費者物価指数【速報値・前月比/前年比】（KissFX・ForexFactoryで一致）', True, '中', '+0.7%/+2.4%', '+0.6%/+2.1%'),
    ('15:45', '🇫🇷 仏', '第2四半期GDP【改定値・前期比/前年比】（KissFX・ForexFactoryで一致、FF表記は速報値）', False, '中', '+0.2%/+0.7%', '+0.2%/+0.7%'),
    ('15:45', '🇫🇷 仏', '消費者支出【前月比】（KissFX・ForexFactoryで一致）', False, '低', '±0.0%', '+0.4%'),
    ('16:00', '🇨🇭 瑞', 'KOF先行指数（KissFX・ForexFactoryで一致）', False, '低', '103.0', '103.5'),
    ('16:00', '🇪🇸 西', 'スペインCPI速報値【前年比】（ForexFactoryのみ・要確認）', False, '低', '+4.2%', '+3.6%'),
    ('16:55', '🇩🇪 独', '失業率（KissFXのみ・要確認）', False, '低', '6.4%', '6.4%'),
    ('16:55', '🇩🇪 独', '失業者数変化（KissFX・ForexFactoryで概ね一致、単位表記相違のため要確認）', False, '低', '+0.48万人(KissFX)/+4K(FF)', '+0.60万人(KissFX)/+6K(FF)'),
    ('18:33', '🇮🇹 伊', '10年債入札（ForexFactoryのみ・要確認）', False, '低', '—', '利回り4.00%/応札倍率1.7'),
    ('21:30', '🇨🇦 加', 'GDP【前月比/前年比】（KissFX・ForexFactoryで一致）', True, '高', '+0.2%/+2.0%', '+0.3%/+1.7%'),
    ('21:30', '🇨🇦 加', '第2四半期GDP【前期比年率】（KissFXのみ・要確認）', False, '高', '+3.4%', '-0.1%'),
    ('22:00', '🇺🇸 米国', 'ハマックFRB総裁 発言（ForexFactoryのみ・要確認）', False, '要人発言', '—', '—'),
    ('22:45', '🇺🇸 米国', 'シカゴ購買部協会景気指数（KissFX・ForexFactoryで一致・重要度表記に相違）', True, '高', '57.9', '57.6'),
    ('23:00', '🇺🇸 米国', 'ミシガン大学消費者信頼感指数【確報値】（KissFX・ForexFactoryで一致）', True, '高', '51.0', '51.0'),
    ('23:00', '🇺🇸 米国', 'ミシガン大学インフレ期待【確報値】（ForexFactoryのみ・要確認）', False, '中', '—', '+4.3%'),
    ('23:00', '🇺🇸 米国', 'ウォーシュFRB議長 講演（ジャクソンホール会合2日目、KissFX・ForexFactoryで一致）', True, '最高', '要人発言', '—'),
    ('23:00', '🇺🇸 米国', '暫定ベンチマーク雇用者数改定（ForexFactoryのみ・要確認）', False, '高', '—', '-911K'),
]

CALENDAR_NOTE = ('※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。'
                  '両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または名称・単位がソース間で相違する指標には「（要確認）」を付しています。'
                  '本日の主要市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。')

# ── ここから生成処理 ─────────────────────────────────
report_files = sorted(glob.glob('reports/*.html'), reverse=True)
SIDEBAR_ITEMS = []
DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}
import datetime as _dt
for f in report_files[:10]:
    name = os.path.basename(f).replace('.html', '')
    href = os.path.basename(f)
    try:
        d = _dt.date.fromisoformat(name)
        wd = DAYS[d.strftime('%A')]
        label = f'{name}（{wd}）'
    except Exception:
        label = name
    SIDEBAR_ITEMS.append(f'<li><a href="{href}">{label}</a></li>')
SIDEBAR_HTML = '\n'.join(SIDEBAR_ITEMS)

KEY_EVENTS_HTML = '\n'.join(f'              <li>{item}</li>' for item in KEY_EVENTS)

OTHER_POINTS_HTML = '\n'.join(
    f'              <li><strong>{title}</strong>：{body}</li>' for title, body in OTHER_POINTS
)

REVIEW_TOPICS_HTML = '\n'.join(
    f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(REVIEW_TOPICS)
)

RANK_CLASS = {'A': 'rank-a', 'B': 'rank-b'}
TREND_CLASS = {'up': 'trend-up', 'range': 'trend-range', 'down': 'trend-down'}
TREND_ARROW = {'up': '↑', 'range': '→', 'down': '↓'}

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {RANK_CLASS[rank]}">{rank}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{note}</span></td>
              <td><span class="{TREND_CLASS[trend]}">{TREND_ARROW[trend]}</span></td>
            </tr>''' for rank, pair, note, trend in RANKING_ROWS)

CALENDAR_ROWS_HTML_LINES = []
CALENDAR_ROWS_HTML_LINES.append('            <tr><td>終日</td><td>🌍 主要国</td><td>' + MARKET_HOLIDAY + '</td><td>—</td><td>—</td><td>—</td></tr>')
for time_jst, country, name, important, importance, forecast, previous in CALENDAR_ROWS:
    badge = ' <span class="badge-important">★重要</span>' if important else ''
    if important:
        CALENDAR_ROWS_HTML_LINES.append(
            f'            <tr><td><strong>{time_jst}</strong></td><td>{country}</td><td><strong>{name}</strong>{badge}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
        )
    else:
        CALENDAR_ROWS_HTML_LINES.append(
            f'            <tr><td>{time_jst}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
        )
CALENDAR_ROWS_HTML = '\n'.join(CALENDAR_ROWS_HTML_LINES)

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
{SIDEBAR_HTML}
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
        <em>{WEEKDAY}曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{SUMMARY_TITLE}</h3>
        <p>{SUMMARY_BODY}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>{TOP_PAIR} {TOP_PAIR_FLAGS}</h3>
        <p>{TOP_PAIR_NOTE}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">{RISK_LEVEL}</h3>
        <p>{RISK_NOTE}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_COUNT}</h3>
        <p>{KEY_COUNT_NOTE}</p>
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
              <li>{MARKET_HOLIDAY}</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
{KEY_EVENTS_HTML}
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
          {RANKING_LEAD}
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
          <h3>📰 前日の相場振り返り（2026-08-27）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{REVIEW_TOPICS_HTML}
          <div class="handover">
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
{CALENDAR_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">{CALENDAR_NOTE}</p>
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
