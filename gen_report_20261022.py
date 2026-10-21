# -*- coding: utf-8 -*-
"""FX日報 2026-10-22（木）生成スクリプト"""
import glob, os

TODAY = '2026-10-22'
WEEKDAY = '木'

HERO_TITLE_SUB = (
    '前営業日10/21（水）のドル円は157円84銭〜158円39銭で推移し、158円14銭で引けた。'
    '本日10/22（木）は06:45のNZ第3四半期CPIと21:30の米新規失業保険申請件数が材料で、市場休場はなく、20:00にトルコ中銀が政策金利を発表する。'
)

SUMMARY_HEADLINE = (
    'ドル円は米10年債利回りの低下で157円84銭まで下げた後、湾岸情勢の報道で158円39銭まで戻し158円14銭で引け。'
    '本日は06:45のNZ CPIと21:30の米新規失業保険申請件数が材料'
)

SUMMARY_BODY = (
    '10/21（水）のNY市場では、原油先物の続落で米長期金利が低下し（米10年債利回りは5.07％台）、ドル円は21時過ぎに157.84円まで下げた。'
    'その後、米国務省が湾岸諸国の大使館員に退避命令を準備しているとの報道で米長期金利が上昇してドル円は158.39円まで戻したが、米政府が退避対象はサウジアラビアのみと説明して報道を否定すると上値は重くなった（ザイFX・フィスコ・DZH）。'
    '米20年債入札（130億ドル）は最高落札利回りが5.469％と1986年1月以来の高水準で、テールが+0.9bpsと低調な結果だったが、ドル円は底堅さを保った（ザイFX）。'
    '本日の市場休場はない（KissFXで確認できる次の休場は10/26のNZ）。経済指標は06:45のNZ第3四半期CPI、20:00のトルコ中銀、21:30の米新規失業保険申請件数が中心（KissFX・ForexFactory一致）。'
)

TOP_PAIR_BODY = (
    'ドル円は10/21に高値158.39円、安値157.84円、終値158.14円（ザイFX・DZH。高値はフィスコ配信158.35円と158.39円で表記が割れており要確認）。前日安値157.83円が下値の目安として機能して下げ止まった。'
    '下値は157.83円・157.70円、上値は10/20高値158.60円が目安となる。'
    '本日は米新規失業保険申請件数（予想20.0万件・前回19.9万件）が米国の主な指標で、米長期金利と湾岸情勢の報道がドル円の方向を決める。'
    '4時間足ランキング（10/21 07:28 JST生成の前日分。本日分は未更新）ではUSD/JPYは上位5位に入っていない。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    '湾岸情勢では、大使館員の退避命令準備の報道とその否定で米長期金利と原油が短時間で反転しており、報道ひとつで急変する状況（ザイFX）。'
    'フランスの暴動と財政懸念も続き、仏10年債利回りは一時5％と2002年以来約24年ぶりの高水準に達した。10/23（金）にはムーディーズによるフランス国債の格付け見直しが予定されている（みんかぶ・DZH）。'
    '来週に10/28のFOMC、10/29のECB、10/30の日銀会合を控え、為替介入への思惑も円売りの上値を抑える（KissFX）。'
)

KEY_EVENTS_COUNT = '4件'
KEY_EVENTS_SUMMARY = (
    'NZ 第3四半期CPI(06:45) / トルコ中銀政策金利(20:00) / 米 新規失業保険申請件数(21:30) / 米 景気先行指数(23:00)。ほか米5年TIPS入札(26:00)'
)

MARKET_OVERVIEW = (
    '10/21のNY市場で米10年債利回りは5.07％台まで低下した後、退避命令報道で反発した（DZH）。米20年債入札は最高落札利回り5.469％と1986年1月以来の高水準で、需要の弱さが確認された（ザイFX）。'
    '日米の株価指数は上昇し、中東情勢の好転期待で株価は買い戻された（ザイFX）。フランス10年債利回りは一時5％に達し、フランスの2027年大統領選の行方と財政赤字削減予算案の審議見通しへの不透明感が背景にある（DZH）。'
    'NY原油先物は続落し、ロシア産ディーゼル燃料の米国向け輸送と米政権のディーゼル緊急備蓄放出計画の報道で供給懸念が和らいだ（ザイFX）。'
    'VIX・米2年債利回り・ドル指数・金の数値は本日の取得ソース（木曜日は取得対象外）で確認していないため記載しない（要確認）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（木曜日は10/21付の日報の値を引き継ぎ。KissFXの会合日程で次回会合が10/28（FRB・BOC・RBNZ）、10/29（ECB）、10/30（日銀）、11/3（RBA）、11/5（BOE）であり、10/21以降に会合がないことを照合）。'
    '<br><br><strong>今週の焦点：</strong> 10/22に06:45のNZ CPIと20:00のトルコ中銀、10/23（金）に独・欧・英・米の製造業・非製造業PMI（速報値）とムーディーズのフランス格付け見直し、来週10/28にFOMC・BOC・RBNZ。FRB高官は10/28のFOMCに向けた発言禁止期間中（KissFX・みんかぶ）。'
)

RANKING_ROWS = [
    (1, 'USD/CAD', 'rank-a', 'A', '前日生成分のスコア80・最適。ADX38.9、ADR比103.4％、方向は下降。原油が続落しており、原油安は加ドルの下押し要因（ザイFX）。', 'trend-down', '↓'),
    (2, 'GBP/USD', 'rank-b', 'B', '前日生成分のスコア67・適。ADX25.9、ADR比99.3％、方向は上昇。10/21は1.3403ドルまで上昇後1.3377ドルへ反落。英CPIが予想を上回り11月利上げ観測が支え（ザイFX）。', 'trend-up', '↑'),
    (3, 'EUR/GBP', 'rank-c', 'C', '前日生成分のスコア59・候補。ADX48.1、ADR比77.7％、方向は下降。英利上げ観測でポンド買いが優勢。', 'trend-down', '↓'),
    (4, 'EUR/AUD', 'rank-c', 'C', '前日生成分のスコア59・候補。ADX22.4、ADR比93.9％、方向は下降。', 'trend-down', '↓'),
    (5, 'AUD/USD', 'rank-c', 'C', '前日生成分のスコア55・候補。ADX19.0、ADR比95.1％、方向は上昇。', 'trend-up', '↑'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/21 07:28 JST生成分（本日分は未更新のため前日データを保持）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'ドル円は米長期金利の低下で157円84銭まで下げ、退避命令報道で158円39銭へ戻し158円14銭で引け',
        '10/21のNY市場でドル円は、原油先物の続落で米10年債利回りが5.07％台まで低下したため円買い・ドル売りが先行し、21時過ぎに日通し安値157.84円を付けた。前日安値157.83円が下値の目安として意識され、下げ止まった（DZH）。'
        'その後、米国務省が湾岸諸国の大使館員に退避命令を準備しているとの報道で米長期金利が上昇し、ドル円は158.39円まで持ち直した。米政府が退避対象はサウジアラビアのみと説明して報道を否定すると上値は重くなり、終値は158.14円と前営業日NY終値（158.17円）から3銭のドル安だった（ザイFX・DZH）。'
        '米20年債入札は最高落札利回り5.469％で1986年1月以来の高水準、テール+0.9bps（過去6回平均0.2bps）と低調だったが、ドル円は底堅さを維持した（ザイFX）。',
    ),
    (
        'ユーロドルは仏財政懸念で1.1214ドルまで下げた後に反発、1.1232ドルで引け',
        'ユーロドルは日本時間夕刻に日通し安値1.1214ドルを付け、NY時間の3時過ぎに日通し高値1.1241ドルまで戻して、終値は1.1232ドルと前営業日（1.1237ドル）から0.0005ドルのユーロ安だった（DZH）。'
        '背景は、フランスの2027年大統領選の行方と、財政赤字削減を進める予算案の審議見通しへの不透明感で、仏10年債利回りは一時5％と2002年以来約24年ぶりの高水準に達した。暴動の激化もユーロ売りを誘った（ザイFX・DZH）。'
        '退避命令報道で米長期金利が上昇した場面では1.1216ドル付近まで押し戻され、報道の否定で買い戻された。ユーロ円は177.28〜177.83円で、終値177.62円。10/23（金）にムーディーズがフランス国債の格付けを見直す予定（みんかぶ）。',
    ),
    (
        '英CPIが予想を上回りポンドドルは1.3403ドルまで上昇、11月利上げ観測が下支え',
        'ポンドドルは1.3403ドルまで上昇した後、1.3377ドルまで反落した（ザイFX）。英消費者物価指数（CPI）が予想を上回り、11月の英中銀（BOE）利上げ観測からポンドは底堅く推移した（ザイFX）。'
        'ロンドン時間にポンドドルは一時1.34台を回復し、NY時間は英国のリスク懸念の後退でポンド上昇に持続力が出ていると指摘された。テクニカル面の目先の上値目標は1.3470ドル（みんかぶ）。'
        'CPIの前年比の確定値は取得ソースで確認できていない（要確認）。',
    ),
    (
        '原油は続落、湾岸情勢の報道で金利と原油が反転',
        'NY原油先物は続落した。ロシア産ディーゼル燃料の米国向け輸送と、米政権によるディーゼル燃料の緊急備蓄放出計画が報じられ、供給混乱への懸念が和らいだ（ザイFX）。'
        '原油安は米インフレ懸念を和らげて米長期金利を押し下げ、ドル売り要因となった。その後、大使館員の退避命令準備の報道で原油と米長期金利は上昇に転じ、米政府の否定で再び反転した。日米の株価指数は中東情勢の好転期待で上昇した（ザイFX）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/22木）への引継ぎ：ドル円は158.14円（日通し安値157.84円・高値158.39円）、ユーロドルは1.1232ドル、ユーロ円は177.62円で10/21を終えた。'
    '本日は06:45のNZ第3四半期CPI（予想 前期比+0.8％・前回+1.5％）がNZドルの材料で、21:30の米新規失業保険申請件数は予想20.0万件（前回19.9万件）。'
    '米長期金利と湾岸情勢の報道がドル円の方向を決め、10/28のFOMCと10/30の日銀会合を控える。'
)

POINTS_EVENTS = [
    '06:45 🇳🇿 NZ 第3四半期消費者物価指数（CPI）前期比（Kiss/FF一致。予想 +0.8％・前回 +1.5％。FFは重要度High）',
    '20:00 🇹🇷 トルコ 中銀政策金利・声明（Kissのみ・要確認。予想は100bpの利下げ、前回は37.00％で据え置き）',
    '21:30 🇺🇸 米国 新規失業保険申請件数（Kiss/FF一致。予想 20.0万件・前回 19.9万件）',
    '23:00 🇺🇸 米国 景気先行指数 前月比（Kiss/FF一致。予想 -0.1％・前回 -0.1％）',
    '26:00 🇺🇸 米国 5年インフレ連動債（TIPS）入札（Kissのみ・要確認。260億ドル。翌02:00）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：米長期金利と湾岸情勢の報道が方向を決める',
        'ドル円は10/21に157.84〜158.39円の狭いレンジで推移し、原油安による米長期金利の低下でドル売り、退避命令報道による金利上昇でドル買いと反転した。'
        '本日は米国の主な指標が21:30の新規失業保険申請件数と23:00の景気先行指数にとどまり、報道による原油・米長期金利の変動がそのままドル円に反映される。下値は157.83円・157.70円、上値は158.60円が目安。来週の日米金融政策会合を前に、狭い持ち合いが続くとの見方が出ている（ザイFX）。',
    ),
    (
        'NZ：06:45の第3四半期CPIが発表直後のNZドルを動かす',
        '予想は前期比+0.8％（前回+1.5％）。予想を上回ればRBNZの10/28会合での利上げ観測が強まりNZドル買い、下回ればNZドル売りとなる。前年比の予想は+3.8％（前回+4.1％）で、Kissのみの確認のため要確認。',
    ),
    (
        'ユーロ：フランス情勢と10/23のムーディーズ格付け見直し',
        '仏10年債利回りが一時5％に達し、財政懸念はユーロの上値を抑える。10/23（金）のムーディーズによるフランス国債の格付け見直しで格下げが出ればユーロ売りが再燃する（みんかぶ）。23:00にはユーロ圏消費者信頼感指数（予想 -17・前回 -17）が発表される（FFのみ・要確認）。',
    ),
    (
        '米国債入札：20年債入札の低調が長期金利の下支えに',
        '10/21の20年債入札は最高落札利回りが5.469％と1986年1月以来の高水準で、テールは+0.9bpsだった（ザイFX）。本日26:00には5年TIPS（260億ドル）の入札があり、結果次第で米長期金利が動く（Kissのみ・要確認）。',
    ),
    (
        '休場：本日は主要市場の休場なし',
        'KissFXで確認できる主要国の次の休場は10/26のニュージーランドで、本日10/22に休場する主要市場は確認されない。',
    ),
    (
        '今週のイベント：金曜のPMIと来週の金融政策イベント',
        '10/23（金）に独・欧・英・米の製造業・非製造業PMI（速報値）とムーディーズのフランス格付け見直し、来週に10/28のFRB・BOC・RBNZ、10/29のECB、10/30の日銀の政策発表が控える（KissFX）。'
        '今週は米主要企業決算（Netflix・Meta・Tesla）も予定されている。FRB高官は発言禁止期間中で、要人発言による方向付けは出にくく、米長期金利と原油が材料になる。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('02:00', '🇺🇸 米', '米20年債入札は10/21分（参考）', '—', '—', '—'),
    ('06:45', '🇳🇿 NZ', '第3四半期消費者物価指数（CPI）前期比（Kiss/FF一致）', '高', '+0.8%', '+1.5%'),
    ('06:45', '🇳🇿 NZ', '第3四半期消費者物価指数（CPI）前年比（Kissのみ・要確認）', '—', '+3.8%', '+4.1%'),
    ('16:30', '🇨🇭 スイス', 'SNB金融政策討議サマリー（FFのみ・要確認）', '低', '—', '—'),
    ('18:10', '🇨🇳 中', '対内直接投資 年初来前年比（FFのみ・要確認）', '低', '—', '-5.3%'),
    ('19:00', '🇬🇧 英', 'CBI鉱工業受注予想（FFのみ・要確認）', '低', '-20', '-9'),
    ('20:00', '🇹🇷 トルコ', '中銀政策金利・声明（Kissのみ・要確認）', '—', '100bp利下げ', '37.00%（据え置き）'),
    ('21:30', '🇺🇸 米', '新規失業保険申請件数（Kiss/FF一致）', '中', '20.0万件', '19.9万件'),
    ('21:30', '🇨🇦 加', '鉱工業製品価格 前月比（FFのみ・要確認）', '低', '+0.9%', '+1.3%'),
    ('21:30', '🇨🇦 加', '原料価格指数 前月比（FFのみ・要確認）', '低', '+3.1%', '+3.1%'),
    ('21:30', '🇨🇦 加', '新築住宅価格指数 前月比（FFのみ・要確認）', '低', '-0.1%', '-0.1%'),
    ('23:00', '🇺🇸 米', '景気先行指数 前月比（Kiss/FF一致）', '低', '-0.1%', '-0.1%'),
    ('23:00', '🇪🇺 欧', '消費者信頼感指数（FFのみ・要確認）', '低', '-17', '-17'),
    ('23:30', '🇺🇸 米', '天然ガス貯蔵量（FFのみ・要確認）', '低', '+80B', '+67B'),
    ('26:00', '🇺🇸 米', '5年インフレ連動債（TIPS）入札（Kissのみ・要確認。翌02:00）', '—', '260億ドル', '—'),
]
CAL_ROWS = [r for r in CAL_ROWS if '参考' not in r[2]]

def _ck(r):
    h = r[0][:2]
    return (99, r[0]) if not h.isdigit() else (int(h), r[0])
CAL_ROWS.sort(key=_ck)

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

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
        <em>木曜日</em>
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
              <li>なし（KissFXの主要国の休場日一覧に10/21の休場はない。次は10/26のニュージーランド）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-21 水）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はForexFactory区分（KissFXのランクは画像表記のため取得不可。KissFXの評価コメントがあるものは併記）。</p>
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
