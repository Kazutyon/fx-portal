# -*- coding: utf-8 -*-
"""FX日報 2026-10-07（水）生成スクリプト"""
import glob, os

TODAY = '2026-10-07'
WEEKDAY = '水'

HERO_TITLE_SUB = (
    '前営業日10/6（火）はユーロ買い戻しでユーロドルが1.1259ドル、ユーロ円が178円00銭まで上昇し、ドル円は158円10銭で引けた。'
    '本日10/7（水）は中国が休場で、08:00のローガン・ダラス連銀総裁発言、15:00のドイツ鉱工業生産、26:00の米10年債入札、27:00のFOMC議事要旨（9/15-16開催分）が材料となる。'
)

SUMMARY_HEADLINE = (
    'ユーロは独仏債利回り格差の縮小で買い戻され1.1259ドルへ上昇、ドル円は158円10銭で底堅く引けた。'
    '本日は27:00のFOMC議事要旨と26:00の米10年債入札が米長期金利とドル円を動かす'
)

SUMMARY_BODY = (
    '10/6（火）は欧州債務不安が一服して独仏債の利回り格差が縮小し、ユーロドルは一時1.1265ドルまで上昇、ユーロ円は前営業日比0.78円高の178円00銭で引けた（みんかぶ・ザイFX）。'
    'ドル円は米国債利回りの低下で一時158円を割り込んだが、再び158円台に乗せて前営業日比0.19円高の158円10銭で引けた（ザイFX・みんかぶ）。'
    '米8月貿易収支は赤字が1056億ドルと7月の928億ドルから拡大し、予想の1020億ドルも上回った（ザイFX単独・要確認）。'
    '本日は米国の注目度の高い経済指標がなく、中国は国慶節（10/7まで）で休場となる。材料は米長期金利とFOMC議事要旨に絞られる。'
)

TOP_PAIR_BODY = (
    'ドル円は10/6のNY終値が158円10銭で、158円前半の押し目では買いが入る底堅い展開だった（ザイFX・羊飼いのFXブログ）。'
    '上値は為替介入への警戒（160円手前）が抑え、下値は米長期金利の低下による158円割れが分岐点となる。'
    '27:00のFOMC議事要旨で9月の利上げ判断の根拠が示され、追加利上げに前向きな内容ならば米長期金利が上昇してドル円は158円台後半へ上昇し、慎重な内容ならば157円台へ押し戻される。'
    '4時間足ランキング（10/6 09:53 JST生成・本日分は未更新）ではUSD/JPYはスコア60・判定「候補」・ADX24.6・方向は上昇だった。'
)

RISK_LEVEL = 'MEDIUM'
RISK_BODY = (
    '米国の注目度の高い経済指標はなく、中国休場でアジア時間の流動性が細い。08:00のローガン・ダラス連銀総裁発言（投票権あり）、26:00の米10年債入札（390億ドル）、27:00のFOMC議事要旨が為替を動かす。'
    '議事要旨の公表は日本時間の翌朝3:00で、東京時間の日中はポジション調整が出やすい。為替介入への思惑も残る。'
)

KEY_EVENTS_COUNT = '6件'
KEY_EVENTS_SUMMARY = (
    'ローガン・ダラス連銀総裁発言(08:00) / 日本平均現金給与(08:30・要確認) / ドイツ鉱工業生産(15:00) / 米週間原油在庫(23:30) / 米10年債入札(26:00) / FOMC議事要旨(27:00)'
)

MARKET_OVERVIEW = (
    '前営業日は欧州債務不安の一服で独仏債の利回り格差が縮小し、ユーロが買い戻されてユーロドルは1.1259ドル、ユーロ円は178円00銭まで上昇した。ドル円は米国債利回りの低下で一時158円を割り込んだが、再び158円台に乗せて引けた。'
    '欧州株は総じて上昇し、ポンドドルは1.32ドル台を維持した（みんかぶ）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（10/5（月）の更新値を継続。次回更新は来週月曜）。'
    '<br><br><strong>今週の焦点：</strong> 10/7の米FOMC議事要旨（9/15-16開催分）と米10年債入札、10/8のECB議事要旨（9/9-10開催分）・日本30年債入札・米30年債入札、10/9のカナダ雇用統計・米ミシガン大学消費者信頼感指数速報値。'
)

RANKING_ROWS = [
    (1, 'EUR/JPY', 'rank-a', 'A', '直近スコア92・最適。ADX40.3、ADR比119.5％、方向は下降。10/6は独仏債利回り格差の縮小でユーロが買い戻され178円00銭引け（前日比+0.78円）。', 'trend-down', '↓'),
    (2, 'EUR/USD', 'rank-b', 'B', '直近スコア85・最適。ADX44.2、ADR比108.8％、方向は下降。10/6は一時1.1265ドルまで反発し、1.1259ドルで引けた。15:00のドイツ鉱工業生産（予想+0.5％）が材料。', 'trend-down', '↓'),
    (3, 'EUR/AUD', 'rank-b', 'B', '直近スコア78・適。ADX35.3、ADR比100.7％、方向は下降。ユーロ側は15:00のドイツ鉱工業生産、豪ドル側は中国休場による流動性低下が材料。', 'trend-down', '↓'),
    (4, 'AUD/JPY', 'rank-c', 'C', '直近スコア70・適。ADX31.5、ADR比105.5％、方向はレンジ。08:30の日本平均現金給与（要確認）が円側の材料。', 'trend-range', '→'),
    (5, 'USD/CHF', 'rank-c', 'C', '直近スコア64・候補。ADX25.6、ADR比97.8％、方向は上昇。16:00のスイス外貨準備高（要確認）と27:00のFOMC議事要旨が材料。', 'trend-up', '↑'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/6 09:53 JST生成分（本日分は未更新・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、重要イベント前後はスプレッド拡大と急変に注意する。'
)

TOPICS = [
    (
        '欧州債務不安の一服でユーロが買い戻され、ユーロドルは1.12ドル台後半へ反発',
        '10/6は独仏債の利回り格差が縮小し、前日に売られたユーロへ買い戻しが入った。ユーロドルは一時1.1265ドルまで上昇して日中高値を更新し、1.1259ドルで引けた（みんかぶ・ザイFX）。'
        'ユーロ円は前営業日比0.78円高の178円00銭で引けた（ザイFX）。仏債の下落が一服したことが買い戻しの理由となった。',
    ),
    (
        'ドル円は米国債利回りの低下で158円を割り込んだ後、押し目買いで158円10銭で引け',
        'ドル円は米国債利回りの低下で一時158円台を割り込んだが、再び158円台に乗せて底堅く推移した（みんかぶ）。ザイFXによると前営業日比0.19円高の158円10銭で引けた。'
        '通貨オプションの1週間ボラティリティーはドル円で7.34％まで低下し、急変への警戒が後退した（みんかぶ）。',
    ),
    (
        '米8月貿易赤字は1056億ドルへ拡大し、予想を上回る',
        '米8月貿易収支の赤字は1056億ドルと7月の928億ドルから拡大し、予想の1020億ドルを上回った。輸入量は過去最高水準で、関税発動前の駆け込み購入が一因とされる（ザイFX単独・要確認）。'
        '赤字拡大はドル売り材料だが、米長期金利の動きがドル円の方向を決める展開が続いた。',
    ),
    (
        '米雇用統計明けのリスクオン気味の流れが継続、ドル円は押し目買い優勢',
        '羊飼いのFXブログは、米雇用統計明けと週明けから緩やかなリスクオンの流れが続き、10/6はドル売り・ユーロ買い・円買いが優勢となったが、ドル円は158円前半で底堅く推移したと伝えている。'
        '欧州株は総じて上昇し、ポンドドルは1.32ドル台を維持した（みんかぶ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/7水）への引継ぎ：ドル円は158円10銭、ユーロ円は178円00銭、ユーロドルは1.1259ドルで前営業日を終えた。'
    '中国が休場で、材料は08:00のローガン・ダラス連銀総裁発言、15:00のドイツ鉱工業生産、26:00の米10年債入札（390億ドル）、27:00のFOMC議事要旨に絞られる。'
    '議事要旨で米金融政策の方向感が示され、米長期金利がドル円の158円台維持を左右する。'
)

POINTS_EVENTS = [
    '08:00 🇺🇸 米国 ローガン・ダラス連銀総裁 発言（投票権あり。Kissのみ・要確認）',
    '08:30 🇯🇵 日本 平均現金給与 前年比（予想+3.7％、前回+4.7％。FFのみ・要確認）',
    '15:00 🇩🇪 ドイツ 鉱工業生産 前月比（予想+0.5％、前回-1.1％。Kiss/FF一致）',
    '23:30 🇺🇸 米国 週間原油在庫（Kiss/FF一致）',
    '26:00（10/8 02:00） 🇺🇸 米国 10年債入札（390億ドル。Kissのみ・要確認）',
    '27:00（10/8 03:00） 🇺🇸 米国 FOMC議事要旨 9/15-16開催分（Kissのみ・要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'FOMC議事要旨が米長期金利とドル円の方向を左右する',
        'FRBは9/16に0.25%利上げして政策金利を3.75〜4.00%とした。議事要旨で追加利上げに前向きな委員が多いと確認されれば米長期金利が上昇してドル円は158円台後半を試し、慎重な意見が多ければ157円台へ押し戻される。'
        '次回の米金融政策発表は10/28。公表は27:00で、日中は26:00の米10年債入札（390億ドル）の需要が米長期金利の先行指標となる。',
    ),
    (
        'ユーロは15:00のドイツ鉱工業生産と明日のECB議事要旨が材料',
        'ドイツ鉱工業生産の予想は前月比+0.5％（前回-1.1％）。予想を上回ればユーロは1.12ドル台後半を維持し、下回れば前日の買い戻しが一巡してユーロ円は178円を割り込む。'
        '10/8にはECB議事要旨（9/9-10開催分）が公表され、次回の金融政策発表は10/29。',
    ),
    (
        '中国休場でアジア時間は流動性が細い',
        '中国は国慶節（10/7まで）で休場となり、豪ドルとオセアニア通貨は中国要因の売買が薄くなる。休場明けの10/8に中国関連の売買が戻る。',
    ),
    (
        '為替介入と要人発言への警戒が続く',
        'ドル円は158円台で、160円手前では日本当局の為替介入への思惑が上値を抑える。ベッセント米財務長官や日本政府・当局者の為替発言が急変動の引き金となる。'
        '日銀の次回金融政策発表は10/30。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('00:46', '🇳🇿 NZ', 'GDT価格指数（FFのみ・要確認）', '低', '—', '-1.1%'),
    ('02:15', '🇺🇸 米', 'シュミッド・カンザスシティ連銀総裁 発言（Kiss前日掲載/FF一致）', '低', '要人発言', '—'),
    ('05:30', '🇺🇸 米', 'API週間原油在庫（FFのみ・要確認）', '低', '—', '—'),
    ('08:00', '🇺🇸 米', 'ローガン・ダラス連銀総裁 発言（投票権あり。Kissのみ・要確認）', '中', '要人発言', '—'),
    ('08:01', '🇨🇳 中', '中国 祝日（市場休場・10/7まで。Kiss/FF Bank Holiday一致）', '低', '—', '—'),
    ('08:30', '🇯🇵 日', '平均現金給与 前年比（FFのみ・要確認）', '低', '+3.7%', '+4.7%'),
    ('14:00', '🇯🇵 日', '景気先行CI指数 速報値（予想 FF 118.1／前回 Kiss 117.7・FF 117.9で不一致・要確認）', '低', '118.1（FF）', '117.7（Kiss）/ 117.9（FF）'),
    ('14:00', '🇯🇵 日', '景気一致CI指数 速報値（Kissのみ・要確認）', '低', '—', '120.6'),
    ('15:00', '🇩🇪 独', '鉱工業生産 前月比（Kiss/FF一致）', '低', '+0.5%', '-1.1%'),
    ('15:00', '🇬🇧 英', '住宅価格 前月比（予想 Kiss ハリファックス+0.2％／FF Lloyds 0.0％で不一致・要確認）', '低', '+0.2%（Kiss）/ 0.0%（FF）', '-0.2%'),
    ('15:45', '🇫🇷 仏', '貿易収支（Kiss/FF掲載。前回 Kiss -66.69億／FF -67億）', '低', '-65億（FF）', '-66.69億（Kiss）/ -67億（FF）'),
    ('15:45', '🇫🇷 仏', '経常収支（Kissのみ・要確認）', '低', '—', '-47億'),
    ('16:00', '🇨🇭 スイス', '外貨準備高（FFのみ・要確認）', '低', '—', '7700億'),
    ('20:00', '🇺🇸 米', 'MBA住宅ローン申請指数（Kissのみ・要確認）', '低', '—', '-6.0%'),
    ('23:30', '🇺🇸 米', '週間原油在庫（Kiss/FF一致）', '中', '+190万（FF）', '+92.2万（Kiss）/ +90万（FF）'),
    ('26:00', '🇺🇸 米', '10年債入札（Kissのみ・要確認）', '中', '390億ドル', '—'),
    ('27:00', '🇺🇸 米', 'FOMC議事要旨 9/15-16開催分（Kissのみ・要確認）', '高', '—', '—'),
    ('28:00', '🇺🇸 米', '消費者信用残高（Kissのみ・要確認）', '低', '+150.00億', '+180.62億'),
]
CAL_ROWS.sort(key=lambda r: (int(r[0][:2]), r[0]))

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
        <em>{WEEKDAY}曜日</em>
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
          <h3>📰 前営業日の相場振り返り（2026-10-06）</h3>
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
