# -*- coding: utf-8 -*-
"""FX日報 2026-10-06（火）生成スクリプト"""
import glob, os

TODAY = '2026-10-06'
WEEKDAY = '火'

HERO_TITLE_SUB = (
    '前営業日10/5（月）は米長期金利の上昇と欧州の政治・財政リスクでドル全面高となり、ドル円は157円91銭、ユーロドルは1.11ドル台まで下落してユーロ円は177円22銭で引けた。'
    '本日10/6（火）は中国が休場で、12:35の日本10年債入札、15:35の植田日銀総裁発言、21:30の米貿易収支、22:05のウィリアムズNY連銀総裁発言が材料となる。'
)

SUMMARY_HEADLINE = (
    'ドル円は米長期金利の上昇で157円91銭に引け、ユーロは仏債利回り上昇で1.11ドル台へ下落した。'
    '本日は15:35の植田日銀総裁発言と、明日のFOMC議事要旨を前にした米FRB高官発言が焦点'
)

SUMMARY_BODY = (
    '10/5（月）はユーロドルの売りが引き金となってドル全面高となり、ドル円は158円台を回復した後に157円91銭で引けた（ザイFX）。'
    'ユーロドルは欧州の政治・財政リスクと仏債利回りの上昇で一時1.11ドル台まで下落し、ユーロ円は前営業日比0.44円安の177円22銭で引けた。'
    '米9月ISM非製造業景況指数は54.9と8月の55.4から低下して予想も下回ったが、27カ月連続で拡大・縮小の境目50を上回り、米長期金利の上昇がドル買いを支えた（ザイFX・要確認）。'
    '本日は中国が国慶節（10/7まで）で休場となる。米国の経済指標は21:30の貿易収支（予想-1020億ドル、前回-886億ドル）のみで、材料は日銀総裁発言とFRB高官発言に絞られる。'
)

TOP_PAIR_BODY = (
    'ドル円は10/5のNY終値が157円91銭〜158円ちょうど付近（ザイFX・羊飼いのFXブログ）で、158円台回復後に200日線を試す展開だった。'
    '上値は158円台の200日線と、日米当局の為替介入への警戒（160円手前）が抑える。下値は米長期金利の低下とISM下振れによる157円割れが分岐点となる。'
    '15:35の植田日銀総裁発言が日銀の追加利上げ観測を強めればドル円は下落し、利上げに慎重な内容ならば157円台後半で底堅く推移する。'
    '4時間足ランキング（10/5 07:24 JST生成・本日分は未更新）ではUSD/JPYはスコア60・判定「候補」・ADX20.8・方向は上昇だった。'
)

RISK_LEVEL = 'MEDIUM'
RISK_BODY = (
    '米国の経済指標は貿易収支のみで、中国休場によりアジア時間の流動性が細い。15:35の植田日銀総裁発言と、22:05ウィリアムズNY連銀総裁・23:45ボウマンFRB副議長の発言が為替を動かす。'
    '明日10/7（日本時間8日3:00）に米FOMC議事要旨（9/15-16開催分）が控え、ポジション調整が出やすい。為替介入への思惑も残る。'
)

KEY_EVENTS_COUNT = '7件'
KEY_EVENTS_SUMMARY = (
    '日本10年債入札(12:35) / 植田日銀総裁発言(15:35) / 英サービス・建設業PMI(17:30) / ユーロ圏小売売上高(18:00) / 米貿易収支(21:30) / ウィリアムズNY連銀総裁発言(22:05) / ボウマンFRB副議長発言(23:45)'
)

MARKET_OVERVIEW = (
    '前営業日はユーロドルの売りを起点にドル全面高となり、ドル円は158円台を回復して157円91銭で引けた。ユーロは仏債利回りの上昇と欧州の政治・財政リスクの警戒で一時1.11ドル台まで下落した。'
    'ポンドは10/28の英予算発表を控えて他通貨に対して出遅れている（みんかぶ）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（10/5（月）の更新値を継続。次回更新は来週月曜）。'
    '<br><br><strong>今週の焦点：</strong> 10/6の植田日銀総裁発言、10/7の米FOMC議事要旨（9/15-16開催分）と米10年債入札、10/8のECB議事要旨・日本30年債入札・米30年債入札、10/9のカナダ雇用統計・米ミシガン大学消費者信頼感指数速報値。'
)

RANKING_ROWS = [
    (1, 'EUR/JPY', 'rank-a', 'A', '直近スコア94・最適。ADX35.4、ADR比122.7％、方向は下降。10/5は仏債利回り上昇のユーロ売りで177円22銭引け（前日比-0.44円）。', 'trend-down', '↓'),
    (2, 'EUR/USD', 'rank-b', 'B', '直近スコア74・適。ADX41.2、ADR比92.0％、方向は下降。10/5は一時1.11ドル台まで下落し、1.12ドル前半で引けた。18:00のユーロ圏小売売上高が材料。', 'trend-down', '↓'),
    (3, 'AUD/JPY', 'rank-b', 'B', '直近スコア72・適。ADX41.4、ADR比109.6％、方向はレンジ。08:30の豪ウエストパック消費者信頼感指数が材料。', 'trend-range', '→'),
    (4, 'USD/CHF', 'rank-c', 'C', '直近スコア62・候補。ADX31.3、ADR比95.4％、方向はレンジ。16:00のスイス失業率（予想3.0〜3.1％）が材料。', 'trend-range', '→'),
    (5, 'USD/JPY', 'rank-c', 'C', '直近スコア60・候補。ADX20.8、ADR比96.0％、方向は上昇。15:35の植田日銀総裁発言と21:30の米貿易収支が材料。', 'trend-up', '↑'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/5 07:24 JST生成分（本日分は未更新・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、重要イベント前後はスプレッド拡大と急変に注意する。'
)

TOPICS = [
    (
        'ユーロドルの売りが引き金となり、ドルが全面高',
        '10/5はユーロドルの売りを起点にドルが全面高となり、ドル円は158円台を回復した（みんかぶ）。ザイFXによるとドル円は157円91銭で引け、米長期金利の上昇がドル買いを支えた。',
    ),
    (
        '欧州の政治・財政リスクと仏債利回りの上昇でユーロが下落',
        'ユーロドルは欧州の政治・財政リスクへの警戒が上値を抑え、仏債利回りの上昇が圧迫して一時1.11ドル台まで下落した（みんかぶ）。ユーロ円は前営業日比0.44円安の177円22銭で引けた（ザイFX）。',
    ),
    (
        '米ISM非製造業景況指数は予想を下回り、ドル円の上値を抑制',
        '米9月ISM非製造業景況指数は54.9と8月の55.4から低下し、予想も下回った。ただし27カ月連続で景況の境目50を上回っており、拡大基調は維持している。'
        'ドル円は米長期金利の上昇で下支えされたが、指標の下振れが上値を抑えた（ザイFX・単独ソースのため要確認）。',
    ),
    (
        'ポンドは10/28の英予算発表を前に出遅れ',
        'みんかぶは、10/28の英予算発表を控えてポンドが他通貨に対して出遅れていると指摘している。BOEは9/17に3.75％で据え置き、ポンドは英財政の先行き不透明感に左右されやすい。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/6火）への引継ぎ：ドル円は157円91銭〜158円ちょうど付近、ユーロ円は177円22銭、ユーロドルは1.12ドル前半で前営業日を終えた。'
    '中国が休場で、材料は12:35の日本10年債入札、15:35の植田日銀総裁発言、21:30の米貿易収支、22:05のウィリアムズNY連銀総裁と23:45のボウマンFRB副議長の発言に絞られる。'
    '明日のFOMC議事要旨（9/15-16開催分）を控え、米長期金利の動向がドル円の158円台維持を左右する。'
)

POINTS_EVENTS = [
    '08:01 🇨🇳 中国 祝日で市場休場（10/7まで。Kiss・FF一致）',
    '12:35 🇯🇵 日本 10年利付国債入札（Kiss・FF一致）',
    '15:35 🇯🇵 日本 植田日銀総裁 発言（あいさつ）（Kiss・FF一致）',
    '17:30 🇬🇧 英国 建設業PMI（予想44.9（Kiss）/ 45.0（FF）、前回44.3）／マンMPC委員 発言',
    '18:00 🇪🇺 ユーロ圏 小売売上高 前月比（予想+0.2％、前回-0.6％）',
    '21:30 🇺🇸 米国 貿易収支（予想-1020億ドル（Kiss）/ -1008億ドル（FF）、前回-886億ドル）',
    '22:05 🇺🇸 米国 ウィリアムズNY連銀総裁 発言（Kissのみ・要確認）／23:45 ボウマンFRB副議長 発言（Kiss・FF一致）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        '植田日銀総裁の発言が追加利上げ観測とドル円の方向を左右する',
        '日銀は9/18に0.25%利上げして政策金利1.25%とした。次回会合は10/30で、植田総裁があいさつで追加利上げに前向きな姿勢を示せばドル円は157円割れを試し、慎重姿勢ならば158円台を維持する。'
        '12:35の10年債入札の結果は日本の長期金利と円相場に影響する。',
    ),
    (
        '米貿易収支は小粒、FRB高官発言と3年債入札が米金利の材料',
        '本日の米経済指標は貿易収支のみ。22:05のウィリアムズNY連銀総裁、23:45のボウマンFRB副議長、26:15のシュミッド・カンザスシティ連銀総裁の発言が、10/7のFOMC議事要旨を前にした米金融政策の思惑を左右する。'
        '26:00の米3年債入札（580億ドル）は米長期金利を動かす。',
    ),
    (
        '中国休場でアジア時間は流動性が細い',
        '中国は国慶節（10/7まで）で休場となり、豪ドルとオセアニア通貨は中国要因の売買が薄くなる。08:30の豪ウエストパック消費者信頼感指数が豪ドルの材料となる。',
    ),
    (
        '今週は10/7のFOMC議事要旨、10/9のカナダ雇用統計が控える',
        '10/7に米FOMC議事要旨（9/15-16開催分）と米10年債入札、10/8にECB議事要旨（9/9-10開催分）、10/9にカナダ雇用統計と米ミシガン大学消費者信頼感指数速報値が発表される。'
        '次回の米金融政策発表は10/28、ECBは10/29、日銀は10/30。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('08:01', '🇨🇳 中', '中国 祝日（市場休場・10/7まで。Kiss/FF Bank Holiday一致）', '低', '—', '—'),
    ('06:00', '🇳🇿 NZ', 'NZIER企業信頼感（FFのみ・要確認）', '低', '—', '8'),
    ('08:30', '🇦🇺 豪', 'ウエストパック消費者信頼感指数（Kiss/FF掲載。前回値の表記が異なる：Kiss 84.4／FF -5.2％・要確認）', '低', '—', '84.4（Kiss）'),
    ('09:30', '🇦🇺 豪', 'ANZ求人広告件数 前月比（FFのみ・要確認）', '低', '—', '2.5%'),
    ('12:35', '🇯🇵 日', '10年利付国債入札（Kiss/FF一致）', '中', '—', '—'),
    ('15:00', '🇪🇺 独', '製造業受注 前月比（予想 Kiss -1.0％／FF -0.9％、前回+2.5％）', '低', '-1.0%（Kiss）/ -0.9%（FF）', '+2.5%'),
    ('15:35', '🇯🇵 日', '植田日銀総裁 発言（あいさつ。Kiss/FF一致）', '高', '要人発言', '—'),
    ('15:45', '🇪🇺 仏', '鉱工業生産 前月比（Kiss/FF一致）', '低', '+0.2%', '-0.4%'),
    ('15:45', '🇪🇺 仏', '財政収支（Kiss/FF一致）', '低', '—', '-1459億'),
    ('16:00', '🇨🇭 スイス', '失業率（予想 Kiss 3.0％／FF 3.1％、前回 Kiss 3.0％／FF 3.1％・要確認）', '低', '3.0%（Kiss）/ 3.1%（FF）', '3.0%（Kiss）/ 3.1%（FF）'),
    ('17:30', '🇬🇧 英', '建設業PMI（予想 Kiss 44.9／FF 45.0）', '低', '44.9（Kiss）/ 45.0（FF）', '44.3'),
    ('17:30', '🇬🇧 英', 'マンMPC委員 発言（Kiss/FF一致）', '中', '要人発言', '—'),
    ('17:30', '🇬🇧 英', '住宅エクイティ引き出し 前期比（FFのみ・要確認）', '低', '-11.9B', '-12.6B'),
    ('18:00', '🇪🇺 ユーロ圏', '小売売上高 前月比（Kiss/FF一致）', '低', '+0.2%', '-0.6%'),
    ('21:15', '🇺🇸 米', 'ADP週次雇用者数変化（FFのみ・要確認）', '低', '—', '+2.0万人'),
    ('21:30', '🇨🇦 加', '貿易収支（予想 Kiss +14.5億／FF +15億）', '低', '+14.5億（Kiss）/ +15億（FF）', '+7.7億（Kiss）/ +8億（FF）'),
    ('21:30', '🇺🇸 米', '貿易収支（予想 Kiss -1020億ドル／FF -1008億ドル）', '中', '-1020億（Kiss）/ -1008億（FF）', '-886億ドル'),
    ('22:05', '🇺🇸 米', 'ウィリアムズNY連銀総裁 発言（Kissのみ・要確認）', '中', '要人発言', '—'),
    ('23:00', '🇨🇦 加', 'Ivey購買部協会指数（Kiss/FF一致）', '中', '65.2（FF）', '64.3'),
    ('23:10', '🇺🇸 米', 'RCM/TIPP経済楽観指数（FFのみ・要確認）', '低', '44.5', '45.6'),
    ('23:45', '🇺🇸 米', 'ボウマンFRB副議長 発言（Kiss/FF一致）', '中', '要人発言', '—'),
    ('23:45', '🇺🇸 米', 'ムサレム・セントルイス連銀総裁 発言（Kissのみ・要確認）', '中', '要人発言', '—'),
    ('23:50', '🇳🇿 NZ', 'GDT価格指数（FFのみ・要確認）', '低', '—', '-1.1%'),
    ('26:00', '🇺🇸 米', '3年債入札（Kissのみ・要確認）', '中', '580億ドル', '—'),
    ('26:15', '🇺🇸 米', 'シュミッド・カンザスシティ連銀総裁 発言（Kissのみ・要確認）', '中', '要人発言', '—'),
]
CAL_ROWS.sort(key=lambda r: (r[0] if r[0][:2].isdigit() else '99:99'))

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

FUNDAMENTALS_ROWS = []
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
        <em>火曜日</em>
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
              <li>🇦🇺 豪州市場休場（労働者の日。ForexFactory Bank Holiday / KissFX一致）</li>
              <li>🇨🇳 中国市場休場（国慶節・10/7まで。ForexFactory Bank Holiday / KissFX一致）</li>
              <li>その他の主要市場の休場: なし（🇭🇰 香港は本日の休場情報を確認できず・要確認）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-05）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はForexFactory区分（KissFXのランクは画像表記のため取得不可）。</p>
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
