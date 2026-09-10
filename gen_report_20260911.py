import glob, os

DATE_LABEL = {
    '2026-09-10': '2026-09-10（木）',
    '2026-09-09': '2026-09-09（水）',
    '2026-09-08': '2026-09-08（火）',
    '2026-09-07': '2026-09-07（月）',
    '2026-09-04': '2026-09-04（金）',
    '2026-09-03': '2026-09-03（木）',
    '2026-09-02': '2026-09-02（水）',
    '2026-09-01': '2026-09-01（火）',
    '2026-08-31': '2026-08-31（月）',
    '2026-08-28': '2026-08-28（金）',
}

sidebar_items = ''.join(
    f'<li><a href="{d}.html">{label}</a></li>\n'
    for d, label in DATE_LABEL.items()
)

HERO_SUMMARY = (
    '前日9/10（木）は米8月PPIが前月比+0.4%・前年比+5.4%と加速しドル買いが強まったほか、'
    '中東（イラン）情勢の緊迫化観測を背景に原油価格が続伸、米財務省の長期債買い戻し規模が51.9億ドルと'
    '期待未達となったことで米国債相場が続落し10年債利回りは4.946%まで上昇した。'
    'ドル円は154円67銭まで上昇後153円85銭まで反落して引け。ECBは定例理事会で市場予想通り0.25%利上げを実施'
    '（預金ファシリティ金利2.25%→2.50%、主要リファイナンス金利2.65%・要確認）し、ユーロ買いが優勢となった。'
    '本日9/11（金）は21:30の米消費者物価指数(CPI)と23:00のミシガン大学消費者信頼感指数・ラガルドECB総裁発言が最大の焦点。'
)

REPORT_SUMMARY_H3 = '米PPI加速・ECB予想通り利上げでドル円154円台乗せ後に反落、本日は米CPIが最大の焦点'
REPORT_SUMMARY_P = (
    '前日9/10（木）のNY市場では、米8月生産者物価指数（PPI）が前月比+0.4%・前年比+5.4%（予想+0.4%/+5.3%）と'
    '伸びが加速し、長期金利上昇に伴うドル買いが強まった。中東（イラン）情勢の緊迫化・長期化への懸念（要確認）から'
    '原油価格が続伸したこともドル買いを支援した。加えて米財務省が実施した長期債買い戻しは規模が51.9億ドルと'
    '事前の想定（60億ドル未満）を下回り、需給悪化を嫌気して米国債相場が続落。米10年債利回りは一時4.946%まで'
    '上昇し2023年以来の高水準を記録した。この結果ドル円は154円67銭まで上昇したが、その後は153円85銭まで反落して引けている。'
    '一方、欧州中央銀行（ECB）は定例理事会で市場予想通り0.25%の利上げを決定し、預金ファシリティ金利を2.25%から'
    '2.50%へ、主要リファイナンス金利を2.65%へ引き上げた（9/16発効・要確認）。中東情勢によるエネルギー高でユーロ圏の'
    'インフレ率が8月に3.3%まで上昇したことを受け、ECBは2026年のインフレ見通しを3.0%へ上方修正しており、'
    'タカ派色を強めたことでユーロ買いが優勢となった。ユーロドルは1.1592～1.1631ドルで方向感の乏しい展開。'
    '欧州株式市場は金利の高止まり警戒から続落した。本日9/11（金）は21:30の米消費者物価指数（CPI）と'
    '23:00のミシガン大学消費者信頼感指数速報値・ラガルドECB総裁発言が最大の焦点となるほか、来週9/16の米FOMC、'
    '9/17の英BOE、9/18の日銀金融政策決定会合を控え、週末を通じたポジション調整にも注意したい。'
)

MOST_WATCHED_PAIR_TITLE = 'USD/JPY 🇺🇸🇯🇵'
MOST_WATCHED_PAIR_BODY = (
    '本日21:30発表の米消費者物価指数（CPI）が最大の焦点。前日のPPI加速を受けて市場はCPIも上振れを警戒しており、'
    '予想（前月比+0.4%・前年比+3.4%）を上回れば来週9/16のFOMCでの金融政策スタンスを巡る思惑からドル買いが'
    '強まりやすい。4Hデイトレ適性ランキングでは現在レンジ判定（スコア86・最適）だが、CPI通過後は方向性が出やすい点に注意。'
)

MARKET_RISK_LEVEL = 'HIGH'
MARKET_RISK_BODY = (
    '本日は21:30に最重要指標の米CPIが控えるほか、23:00のミシガン大学消費者信頼感指数・ラガルドECB総裁発言も'
    '重なる。前日はPPI加速と米国債入札不調でドルが乱高下しており、来週の米FOMC・英BOE・日銀決定会合を控えた'
    '週末でもあることから、指標結果次第で値動きが大きくなりやすい一日。'
)

KEY_EVENTS_COUNT = '21件'
KEY_EVENTS_SUMMARY_LINE = '米消費者物価指数(CPI) / ミシガン大学消費者信頼感指数 / ラガルドECB総裁発言 / 英GDP 等（本日の市場休場はなし）'

POINTS_HOLIDAY = '本日、主要国の市場休場はなし（前日9/10も休場はありませんでした）'

KEY_EVENTS_LIST = [
    '07:30 🇳🇿 NZ製造業景況指数',
    '08:50 🇯🇵 日本 国内企業物価指数(PPI)',
    '15:00 🇬🇧 英GDP【月次】',
    '21:30 🇺🇸 米消費者物価指数(CPI)【前月比/前年比・コア】',
    '23:00 🇪🇺 ラガルドECB総裁 発言',
    '23:00 🇺🇸 ミシガン大学消費者信頼感指数【速報値】',
]

OTHER_POINTS = [
    (
        'ドル円154円台に乗せるも米CPIを前に上値重く153円台後半で推移',
        '前日9/10はNY市場でドル円が154円67銭まで上昇したが153円85銭まで反落して引けた。米8月PPIの加速でドル買いが'
        '強まった一方、直近の急速な円高の流れも残り上値は重い。来週9/18の日銀決定会合での利上げ観測（要確認）も'
        '円の下支え材料として意識されている。'
    ),
    (
        '米PPI加速・米国債入札不調で長期金利急上昇',
        '米8月PPIは前月比+0.4%・前年比+5.4%（予想+0.4%/+5.3%）と加速。加えて米財務省の長期債買い戻し規模が'
        '事前想定の60億ドルを下回る51.9億ドルにとどまったことで需給悪化が意識され、米10年債利回りは一時4.946%まで'
        '上昇し2023年以来の高水準を記録した。'
    ),
    (
        'ECBは市場予想通り0.25%利上げ、預金ファシリティ2.50%へ（要確認）',
        'ECBは定例理事会で主要政策金利を0.25%引き上げ、預金ファシリティ金利を2.25%から2.50%、主要リファイナンス'
        '金利を2.65%とした（9/16発効・要確認）。中東情勢によるエネルギー高でユーロ圏インフレ率が8月に3.3%まで'
        '上昇したことを受け、ECBは2026年のインフレ見通しを3.0%へ上方修正しておりタカ派色が強まった。'
    ),
    (
        '中東（イラン）情勢の緊迫化観測で原油価格が続伸（要確認）',
        '中東・イラン情勢の緊迫化・長期化への懸念が報じられ（要確認）、原油価格が続伸した。エネルギー価格の上昇は'
        '米欧のインフレ圧力を通じて金利観測にも影響しており、CPI発表を控える中で引き続き注視したい。'
    ),
    (
        '本日21:30に米CPI発表、来週はFOMC・BOE・日銀決定会合が集中',
        '本日最大の焦点は21:30発表の米消費者物価指数（CPI）。市場予想は前月比+0.4%・前年比+3.4%（コアは+0.2%/+2.4%）。'
        '前日のPPI加速を受けて上振れ警戒が強まっており、来週9/16の米FOMC、9/17の英BOE、9/18の日銀金融政策決定会合を'
        '控える中で、金融政策見通しへの影響が大きくなりやすい。'
    ),
]

MARKET_ENV_TEXT = (
    '前日9/10（木）は米8月PPIの加速と米国債買い戻し規模の未達を受けたドル買い、および中東情勢緊迫化観測による'
    '原油高（要確認）を背景に、ドル円は154円67銭まで上昇後153円85銭まで反落して引けた。ECBは市場予想通り0.25%'
    '利上げを実施しユーロ買いが優勢となる一方、欧州株式市場は金利の高止まりを警戒し続落した。本日9/11（金）は'
    '21:30の米CPIが最大の焦点で、来週の米FOMC・英BOE・日銀決定会合を控えた週末要因にも注意したい。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派、9/15-16FOMCに向け利上げ観測強まるも一部高官は慎重・要確認） / '
    '日銀 1.00%（正常化継続・タカ派寄り、9月利上げ観測強まる・次回9/17-18、今月1.25%程度への利上げ方針との報道あり・要確認） / '
    '欧ECB 預金ファシリティ金利2.50%（9/10理事会で0.25%利上げ実施・主要リファイナンス金利2.65%、中東情勢によるエネルギー高で'
    'インフレ見通し上方修正・要確認）'
)

RANKING_ROWS = [
    ('A', 'EUR/JPY', 'ランキング1位（スコア93・最適）。ADX62.8で非常に強い下降トレンド、直近5日ADRは5年平均の121.5%', 'down'),
    ('A', 'GBP/JPY', 'ランキング2位（スコア88・最適）。ADX61.7で非常に強い下降トレンド、直近5日ADRは5年平均の113.9%', 'down'),
    ('A', 'USD/JPY', 'ランキング3位（スコア86・最適）。ADX55.6で強いレンジ〜トレンド、直近5日ADRは5年平均の130.0%', 'range'),
    ('A', 'AUD/JPY', 'ランキング4位（スコア80・最適）。ADX63.0で非常に強い下降トレンド、直近5日ADRは5年平均の103.6%', 'down'),
    ('C', 'NZD/USD', 'ランキング5位（スコア51・候補）。ADX28.1でやや弱い下降トレンド、直近5日ADRは5年平均の76.3%', 'down'),
]
RANK_BADGE_CLASS = {'A': 'rank-a', 'B': 'rank-b', 'C': 'rank-b'}
TREND_CLASS = {'down': 'trend-down', 'up': 'trend-up', 'range': 'trend-range'}
TREND_ARROW = {'down': '↓', 'up': '↑', 'range': '→'}

RANKING_ROWS_HTML = ''
for badge, pair, desc, direction in RANKING_ROWS:
    RANKING_ROWS_HTML += f'''            <tr>
              <td><span class="rank-badge {RANK_BADGE_CLASS[badge]}">{badge}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{TREND_CLASS[direction]}">{TREND_ARROW[direction]}</span></td>
            </tr>
'''

REVIEW_TOPICS = [
    (
        'ドル円154円台まで上昇後、153円85銭まで反落して引ける',
        '前日9/10（木）はNY市場でドル円が154円67銭まで上昇する場面があったが、その後は153円85銭まで反落して引けた。'
        '米8月PPIの加速でドル買いが強まる一方、上値では戻り待ちの売りも観測された。'
    ),
    (
        '米8月PPIが加速、長期金利上昇でドル買い支援',
        '米8月生産者物価指数（PPI）は前月比+0.4%・前年比+5.4%（予想+0.4%/+5.3%）と伸びが加速。長期金利の上昇に'
        'つながり、ドル買いを支援した。'
    ),
    (
        '米財務省の長期債買い戻しが期待未達、米10年債利回り4.946%まで上昇',
        '米財務省が実施した長期債買い戻しは規模が51.9億ドルと事前想定の60億ドルを下回り、需給悪化への警戒から'
        '米国債相場が続落。米10年債利回りは一時4.946%まで上昇し2023年以来の高水準を記録した。'
    ),
    (
        'ECBは市場予想通り0.25%利上げ、インフレ見通しを上方修正（要確認）',
        '欧州中央銀行（ECB）は定例理事会で主要政策金利を0.25%引き上げ、預金ファシリティ金利を2.25%から2.50%、'
        '主要リファイナンス金利を2.65%とした（要確認）。中東情勢によるエネルギー高でユーロ圏インフレ率が8月に'
        '3.3%まで上昇したことを受け、ECBは2026年のインフレ見通しを3.0%へ上方修正しており、タカ派色が強まった。'
    ),
    (
        '中東（イラン）情勢の緊迫化観測で原油続伸、欧州株は金利高止まり警戒で続落（要確認）',
        '中東・イラン情勢の緊迫化・長期化への懸念が報じられ（要確認）原油価格が続伸したほか、ECBのタカ派姿勢を'
        '受けた金利の高止まり警戒から欧州株式市場は続落した。'
    ),
]

REVIEW_TOPICS_HTML = ''
for i, (title, body) in enumerate(REVIEW_TOPICS, start=1):
    REVIEW_TOPICS_HTML += f'''          <div class="topic">
            <div class="topic-title">【トピック{i}】{title}</div>
            {body}
          </div>
'''

HANDOVER_TEXT = (
    '本日（9/11金）への引継ぎ：前日はドル円が米PPI加速・米国債入札不調によるドル買いで154円台に乗せる場面もあったが'
    '153円85銭まで反落して引けた。ECBは市場予想通り0.25%利上げを実施しユーロ買いが優勢に。本日は21:30の米CPIが'
    '最大の焦点で、前日のPPI加速を受けて上振れ警戒が強まっている。来週9/16の米FOMC・9/17の英BOE・9/18の日銀決定'
    '会合を控える週末でもあり、CPI結果次第でドル円・ユーロドルとも値動きが大きくなりやすい点に留意したい。'
)

CALENDAR_ROWS = [
    ('01:00', '🇺🇸 米', '週間原油在庫【EIA】（ForexFactoryのみ・要確認）', '低', '-1.4M', '-4.5M', False),
    ('02:01', '🇺🇸 米', '30年債入札（ForexFactoryのみ・要確認）', '低', '—', '前回利回り5.22%/応札倍率2.4倍', False),
    ('07:30', '🇳🇿 NZ', 'BusinessNZ製造業景況指数（KissFX・ForexFactory一致）', '低', '—', '54.3', False),
    ('08:50', '🇯🇵 日', '第3四半期景況判断BSI【全産業】（KissFXのみ・要確認）', '低', '—', '-0.5', False),
    ('08:50', '🇯🇵 日', '第3四半期景況判断BSI【大企業製造業】（KissFX・ForexFactory一致）', '低', '2.5', '-1.8', False),
    ('08:50', '🇯🇵 日', '国内企業物価指数(PPI)【前月比/前年比】（KissFX・ForexFactory一致）', '低', '±0.0%/+7.4%', '+0.1%/+7.2%', False),
    ('15:00', '🇬🇧 英', 'GDP【月次】（KissFX・ForexFactory一致）', '中〜高', '±0.0%', '+0.3%', True),
    ('15:00', '🇬🇧 英', '鉱工業生産【前月比/前年比】（KissFX・ForexFactory一致）', '低〜中', '-0.2%/+0.2%', '-0.2%/-0.2%', False),
    ('15:00', '🇬🇧 英', '製造業生産高【前月比/前年比】（KissFX・ForexFactory一致）', '低〜中', '+0.2%/+2.0%', '-0.5%/+0.5%', False),
    ('15:00', '🇬🇧 英', '商品貿易収支（KissFX・ForexFactory一致）', '低', '-223.00億(約-22.6B)', '-230.07億(約-23.0B)', False),
    ('15:00', '🇬🇧 英', '建設業生産高【前月比】（ForexFactoryのみ・要確認）', '低', '+0.1%', '-0.1%', False),
    ('15:00', '🇬🇧 英', 'サービス業指数【3ヶ月/3ヶ月】（ForexFactoryのみ・要確認）', '低', '—', '+0.5%', False),
    ('16:00', '🇨🇭 スイス', 'SECO消費者信頼感（ForexFactoryのみ・要確認）', '低', '-33', '-35', False),
    ('17:00', '🇮🇹 伊', '四半期失業率（ForexFactoryのみ・要確認）', '低', '5.4%', '5.3%', False),
    ('17:30', '🇬🇧 英', '消費者インフレ期待（ForexFactoryのみ・要確認）', '低', '—', '4.0%', False),
    ('18:15', '🇨🇭 スイス', 'SNBシュレーゲル総裁 発言（ForexFactoryのみ・要確認）', '中', '要人発言', '—', False),
    ('21:30', '🇺🇸 米', '消費者物価指数(CPI)【前月比/前年比】（KissFX・ForexFactory一致）', '最高', '+0.4%/+3.4%', '+0.1%/+3.4%', True),
    ('21:30', '🇺🇸 米', '消費者物価指数コア【前月比/前年比】（KissFX・ForexFactory一致）', '最高', '+0.2%/+2.4%', '+0.2%/+2.5%', False),
    ('23:00', '🇪🇺 欧', 'ラガルドECB総裁 発言（KissFX・ForexFactory一致）', '中〜高', '要人発言', '—', False),
    ('23:00', '🇺🇸 米', 'ミシガン大学消費者信頼感指数【速報値】（KissFX・ForexFactory一致、前回値に相違・要確認）', '中〜高', '51.0', '51.7／51.0（要確認）', False),
    ('23:00', '🇺🇸 米', 'ミシガン大学期待インフレ率【速報値】（ForexFactoryのみ・要確認）', '中', '—', '4.3%', False),
    ('翌03:00', '🇺🇸 米', '財政収支（KissFX・ForexFactory一致、予想値に相違・要確認）', '低', '-4040億／-221.1B（要確認）', '-4323億(-432.3B)', False),
]

CALENDAR_ROWS_HTML = ''
for time_s, country, name, importance, forecast, previous, important in CALENDAR_ROWS:
    badge = ' <span class="badge-important">★重要</span>' if important else ''
    time_cell = f'<strong>{time_s}</strong>' if important else time_s
    name_cell = f'<strong>{name}</strong>{badge}' if important else name
    CALENDAR_ROWS_HTML += f'            <tr><td>{time_cell}</td><td>{country}</td><td>{name_cell}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>\n'

TOTAL_EVENTS = len(CALENDAR_ROWS)

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FX日報 2026-09-11（金） | AUXEN FX Portal</title>
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
  <h1>FX日報 2026-09-11（金）</h1>
  <p>{HERO_SUMMARY}</p>
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
        <h2>FX日報 2026-09-11（金）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_SUMMARY}</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>2026-09-11</strong>
        <em>金曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{REPORT_SUMMARY_H3}</h3>
        <p>{REPORT_SUMMARY_P}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>{MOST_WATCHED_PAIR_TITLE}</h3>
        <p>{MOST_WATCHED_PAIR_BODY}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red,#c0392b)">{MARKET_RISK_LEVEL}</h3>
        <p>{MARKET_RISK_BODY}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_EVENTS_COUNT}</h3>
        <p>{KEY_EVENTS_SUMMARY_LINE}</p>
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
              <li>{POINTS_HOLIDAY}</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
{chr(10).join(f'              <li>{item}</li>' for item in KEY_EVENTS_LIST)}
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
{chr(10).join(f'              <li><strong>{title}</strong>：{body}</li>' for title, body in OTHER_POINTS)}
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
          {MARKET_ENV_TEXT}
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
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは2026-09-11 06:43 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。本日は米CPI等の指標イベントが集中するため、通常のトレンドフォローに加えイベント通過後の値動きにも注意してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-09-10）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{REVIEW_TOPICS_HTML}          <div class="handover">
            <strong>{HANDOVER_TEXT}</strong>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標や、両ソース間で数値に相違がある指標には「（要確認）」を付しています。本日は主要国の市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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

with open('reports/2026-09-11.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('reports/2026-09-11.html generated,', TOTAL_EVENTS, 'calendar rows')
