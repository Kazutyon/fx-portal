# -*- coding: utf-8 -*-
"""FX日報 2026-10-08（木）生成スクリプト"""
import glob, os

TODAY = '2026-10-08'
WEEKDAY = '木'

HERO_TITLE_SUB = (
    '前営業日10/7（水）はフランス債の再下落でユーロが売られ、ユーロドルは1.1197ドル、ユーロ円は176円98銭へ下落し、ドル円は158円08銭で横ばいだった。'
    '本日10/8（木）は17:30のウォラーFRB理事発言、20:30のECB議事要旨（9/9-10開催分）、21:15のベイリーBOE総裁発言、21:30の米新規失業保険申請件数、26:00の米30年債入札が材料となる。'
)

SUMMARY_HEADLINE = (
    'ユーロは仏債の下落で売られ年初来安値1.1161ドルに接近、ドル円はFOMC議事要旨のタカ派内容でも158円08銭と横ばい。'
    '本日は米長期金利と20:30のECB議事要旨がユーロとドル円を動かす'
)

SUMMARY_BODY = (
    '10/7（水）は仏債が再び売られ、ユーロドルは一時1.1165ドルまで下落して1.1197ドルで引け、ユーロ円は前営業日比1円02銭安の176円98銭で引けた（ザイFX・フィスコ）。'
    '米10年債利回りは一時5.3624％と2002年以来24年ぶりの高水準を付けたが、米10年債入札が好調で5.28％の横ばいで引け、ドル円は158円08銭（前営業日比▲0.02円）と動かなかった（ザイFX）。'
    'FOMC議事要旨（9/15-16開催分）は「当局者19人全員が利上げを支持」「大半が年内の追加利上げを適切と判断」と、タカ派の内容だった（ザイFX・フィスコ）。'
    '本日は米国の注目度の高い指標が新規失業保険申請件数のみで、中国は国慶節明けで市場が再開する。'
)

TOP_PAIR_BODY = (
    'ドル円は10/7のレンジが157.85〜158.51円で、前日安値157.77円と一目均衡表転換線157.67円が下値支持線として機能した（ザイFX）。'
    '上値は158円半ばで押し返され、NY午後は米10年債入札を受けた長期金利の低下で157円90銭付近まで押し戻された。160円手前では為替介入への警戒が上値を抑える。'
    '本日は米長期金利が上昇すればドル円は158円半ばの高値を再び試し、低下すれば157円台前半の支持線157.77円を試す。'
    '4時間足ランキング（10/7 08:10 JST生成・本日分は未更新）ではUSD/JPYはスコア56・判定「候補」・ADX24.0・方向は上昇だった。'
)

RISK_LEVEL = 'MEDIUM'
RISK_BODY = (
    '米長期金利が24年ぶりの高水準にあり、仏債の動きでユーロが急変しやすい。20:30のECB議事要旨と21:15のベイリーBOE総裁発言で欧州通貨が動き、21:30の米新規失業保険申請件数が米長期金利に影響する。'
    'ユーロドルは年初来安値1.1161ドルまで5pips前後に迫っており、割り込めばストップを巻き込んだ急落となる。為替介入への思惑も残る。'
)

KEY_EVENTS_COUNT = '7件'
KEY_EVENTS_SUMMARY = (
    '日本30年債入札(12:35) / ウォラーFRB理事発言(17:30) / ECB議事要旨(20:30) / ベイリーBOE総裁発言(21:15) / 米新規失業保険申請件数(21:30) / カシュカリ連銀総裁発言(23:40・要確認) / 米30年債入札(26:00)'
)

MARKET_OVERVIEW = (
    '前営業日は仏債が再び売られ、ECBの追加利上げ観測も後退したことでユーロが全面安となった。ユーロドルは一時1.1165ドルまで下落し、10/5に付けた年初来安値1.1161ドルが支持線として働いて1.1197ドルで引けた。'
    '米10年債利回りは一時5.3624％と24年ぶりの高水準を付けてダウは341ドル安となり、金は反落して約2カ月ぶりの安値、WTI原油は88.28ドルへ下落した（ザイFX）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（10/5（月）の更新値を継続。次回更新は来週月曜）。'
    '<br><br><strong>今週の焦点：</strong> 10/8のECB議事要旨（9/9-10開催分）・日本30年債入札・米30年債入札、10/9のカナダ雇用統計・米ミシガン大学消費者信頼感指数速報値。'
)

RANKING_ROWS = [
    (1, 'EUR/JPY', 'rank-a', 'A', '直近スコア88・最適。ADX33.6、ADR比128.0％、方向はレンジ。10/7は仏債の下落でユーロ売りが進み、前日比1円02銭安の176円98銭で引けた。20:30のECB議事要旨が材料。', 'trend-range', '→'),
    (2, 'EUR/USD', 'rank-b', 'B', '直近スコア83・最適。ADX36.5、ADR比117.0％、方向はレンジ。10/7は一時1.1165ドルまで下落し、年初来安値1.1161ドルの手前で1.1197ドルに引けた。', 'trend-range', '→'),
    (3, 'EUR/AUD', 'rank-b', 'B', '直近スコア71・適。ADX32.7、ADR比93.7％、方向は下降。ユーロ売り継続でユーロ側が重く、20:30のECB議事要旨が材料。', 'trend-down', '↓'),
    (4, 'GBP/JPY', 'rank-c', 'C', '直近スコア64・候補。ADX17.8、ADR比109.0％、方向は上昇。21:15のベイリーBOE総裁発言と英予算案への警戒（みんかぶ）が材料。', 'trend-up', '↑'),
    (5, 'EUR/GBP', 'rank-c', 'C', '直近スコア59・候補。ADX52.7、ADR比78.3％、方向は下降。ADRが31pipsと小さくコスト比3.88％と高い。ECB議事要旨とBOE総裁発言が同日に重なる。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/7 08:10 JST生成分（本日分は未更新・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、重要イベント前後はスプレッド拡大と急変に注意する。'
)

TOPICS = [
    (
        '仏債の再下落でユーロ売りが再燃、ユーロドルは年初来安値1.1161ドルに接近',
        '10/7はフランスの政治・財政運営への懸念が根強く、ロンドン序盤から仏債が再び売られてユーロが売られた。ECBの追加利上げ観測も後退してユーロ売りに拍車がかかり、ユーロドルは21時30分前に一時1.1165ドルと日通し安値を付けた（ザイFX・フィスコ・みんかぶ）。'
        '10/5の年初来安値1.1161ドルが支持線として働き、1.1197ドル（前営業日比▲0.0062ドル）で引けた。ユーロ円は一時176円55銭まで下落し、前営業日比1円02銭安の176円98銭で引けた。',
    ),
    (
        'FOMC議事要旨はタカ派、米10年債利回りは24年ぶり高水準から入札後に低下',
        '9/15-16開催分のFOMC議事要旨は、当局者19人全員が利上げを支持し、大半が年内の追加利上げを適切とし、複数が政策は十分に景気抑制的ではないと指摘した内容だった（ザイFX・フィスコ）。'
        '米10年債利回りは仏債下落の波及で一時5.3624％と2002年以来24年ぶりの高水準を付けたが、好調な10年債入札（最高落札利回り5.300％）を受けて低下に転じ、5.28％の横ばいで引けた（ザイFX・みんかぶ）。',
    ),
    (
        'ドル円は158円08銭で横ばい、157.85〜158.51円のレンジ',
        '欧州序盤はユーロ主導の円高で一時157.85円まで下落したが、前日安値157.77円と一目均衡表転換線157.67円が支持線として働き、米長期金利の上昇で158.40円付近まで戻った。'
        'NY午後は米10年債入札後の長期金利低下で157.90円付近まで押し戻され、158.08円（前営業日比▲0.02円）で引けた（ザイFX）。高市首相は金利・為替水準について具体的なコメントをしないと述べた（みんかぶ）。',
    ),
    (
        '株安・金安・原油安、イラン情勢と米国の石油備蓄放出が商品市場を左右',
        'ダウは5日ぶりに反落して341ドル安、金先物は米長期金利の上昇で売られ約2カ月ぶりの安値となった。WTI原油は一時90ドル台に乗せたが、湾岸諸国の石油輸出量の急回復とEIA加盟国の石油備蓄放出加速の支持表明で1.16ドル安の88.28ドルで引けた（ザイFX・みんかぶ）。'
        'イランがホルムズ海峡で船舶攻撃を継続していると伝えられている（フィスコ）。トランプ大統領が中間選挙前にイラン攻撃を検討しているとの報道（英テレグラフ）もあるが、単独報道のため要確認。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/8木）への引継ぎ：ドル円は158円08銭、ユーロ円は176円98銭、ユーロドルは1.1197ドルで前営業日を終えた。'
    'ユーロドルは年初来安値1.1161ドルまで約3pipsで、割り込めば仏債の下落とECBの利上げ観測後退が重なったユーロ売りが加速する。'
    '材料は17:30のウォラーFRB理事発言、20:30のECB議事要旨、21:15のベイリーBOE総裁発言、21:30の米新規失業保険申請件数、26:00の米30年債入札に絞られる。'
)

POINTS_EVENTS = [
    '12:35 🇯🇵 日本 30年利付国債入札（Kiss/FF一致）',
    '17:30 🇺🇸 米国 ウォラーFRB理事 発言（投票権あり。Kiss/FF一致）',
    '20:30 🇪🇺 ユーロ圏 ECB理事会議事要旨 9/9-10開催分（Kiss/FF一致）',
    '21:15 🇬🇧 英国 ベイリーBOE総裁 発言（Kiss/FF一致）',
    '21:30 🇺🇸 米国 新規失業保険申請件数（予想20.0万件、前回19.7万件。Kiss/FF一致）',
    '23:40 🇺🇸 米国 カシュカリ・ミネアポリス連銀総裁 発言（投票権あり。Kissのみ・要確認）',
    '26:00（10/9 02:00） 🇺🇸 米国 30年債入札（220億ドル。Kiss/FF一致）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ユーロドルは年初来安値1.1161ドルの攻防、仏債が方向を決める',
        'ユーロドルは10/5の年初来安値1.1161ドルの手前で下げ止まっている。仏債利回りが再び上昇すればユーロ売りが再燃して1.1161ドルを割り込み、仏債が落ち着けば1.12ドル台前半への戻りが入る。'
        '20:30のECB議事要旨で追加利上げに前向きな内容が示されればユーロは下げ止まり、慎重な内容ならばユーロ売りが加速する。次回のECB金融政策発表は10/29。',
    ),
    (
        '米長期金利とドル円：議事要旨はタカ派でも入札後は金利低下',
        'FOMC議事要旨は利上げ全会一致と年内追加利上げの観測を示したが、10/7のドル円は158円08銭と横ばいだった。米10年債利回りは5.28％と24年ぶりの高水準圏にあり、21:30の新規失業保険申請件数（予想20.0万件）が予想を上回れば長期金利が低下してドル円は157円台前半へ下落する。'
        '26:00の米30年債入札（220億ドル）の需要が米長期金利を左右する。次回の米金融政策発表は10/28。',
    ),
    (
        'ポンドは英予算案への警戒、21:15にベイリーBOE総裁発言',
        'ポンドドルは10/7に一時1.3194ドルまで下落した（フィスコ）。みんかぶは英予算案への警戒が背景と伝えている。21:15のベイリーBOE総裁発言と、18:15のグリーン委員、19:30または18:00のピル委員（時刻不一致・要確認）、22:00のロンバルデッリ副総裁と、BOE関係者の発言が続き、ポンドが動きやすい。次回のBOE金融政策発表は11/5。',
    ),
    (
        '為替介入と要人発言への警戒が続く',
        'ドル円は158円台で、160円手前では日本当局の為替介入への思惑が上値を抑える。ベッセント米財務長官や日本政府・当局者の為替発言が急変動の引き金となる。'
        '日銀の次回金融政策発表は10/30。中国は国慶節明けで本日から市場が再開し、豪ドルなど中国要因の売買が戻る。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('02:00', '🇺🇸 米', 'トランプ米大統領 発言（発表済み・FFのみ・要確認）', '中', '—', '—'),
    ('02:01', '🇺🇸 米', '10年債入札（発表済み。最高落札利回り5.300％・みんかぶ。FF掲載）', '低', '—', '4.83%|2.7倍（FF）'),
    ('03:00', '🇺🇸 米', 'FOMC議事要旨 9/15-16開催分（発表済み。当局者19人全員が利上げ支持・ザイFX/フィスコ。Kiss/FF一致）', '高', '—', '—'),
    ('04:00', '🇺🇸 米', '消費者信用残高（発表済み。結果+82.81億ドル・ザイFX/フィスコ。Kiss未掲載・FF/ザイFXで確認）', '低', '+145億（FF）/+150億（フィスコ）', '+180.62億→+177.4億（改定）'),
    ('08:01', '🇬🇧 英', 'RICS住宅価格 DI（Kiss/FF一致）', '低', '-30%', '-28%'),
    ('08:50', '🇯🇵 日', '貿易収支 国際収支（Kissのみ・要確認）', '低', '-7152億', '-3999億'),
    ('08:50', '🇯🇵 日', '経常収支 国際収支（予想 Kiss+3兆1723億／ザイFX+3兆1946億／FF+2.14兆で不一致・要確認）', '低', '+3兆1723億（Kiss）/ +2.14兆（FF）', '+2兆9889億（Kiss/ザイFX）/ +2.52兆（FF）'),
    ('09:00', '🇦🇺 豪', 'メルボルン研究所（MI）期待インフレ率（FFのみ・要確認）', '低', '—', '4.9%'),
    ('12:35', '🇯🇵 日', '30年利付国債入札（Kiss/FF一致）', '低', '—', '—'),
    ('14:00', '🇯🇵 日', '景気ウォッチャー調査 現状判断DI（Kiss/FF一致）', '低', '46.7', '46.4'),
    ('14:00', '🇯🇵 日', '景気ウォッチャー調査 先行き判断DI（Kissのみ・要確認）', '低', '48.5', '48.3'),
    ('15:00', '🇩🇪 独', '貿易収支（Kiss/FF一致）', '低', '+190億', '+213億'),
    ('17:05', '🇨🇭 スイス', 'マルティン SNB理事 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('17:30', '🇬🇧 英', 'BOE信用状況調査（FFのみ・要確認）', '低', '—', '—'),
    ('17:30', '🇺🇸 米', 'ウォラーFRB理事 発言（投票権あり。Kiss/FF一致）', '中', '要人発言', '—'),
    ('18:00', '🇬🇧 英', 'ピルMPC理事 発言（時刻不一致 Kiss18:00／FF19:30・要確認）', '低', '要人発言', '—'),
    ('18:15', '🇬🇧 英', 'グリーンMPC委員 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('18:15', '🇪🇺 欧', 'ユーログループ会合（FFのみ・要確認）', '低', '—', '—'),
    ('20:30', '🇪🇺 欧', 'ECB理事会議事要旨 9/9-10開催分（Kiss/FF一致）', '低', '—', '—'),
    ('21:15', '🇬🇧 英', 'ベイリーBOE総裁 発言（Kiss/FF一致）', '高', '要人発言', '—'),
    ('21:30', '🇺🇸 米', '新規失業保険申請件数（Kiss/FF一致）', '中', '20.0万件', '19.7万件'),
    ('22:00', '🇬🇧 英', 'ロンバルデッリBOE副総裁 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('23:00', '🇺🇸 米', '卸売在庫 確報値 前月比（Kiss/FF一致）', '低', '+0.7%', '+0.7%'),
    ('23:30', '🇺🇸 米', '週間天然ガス貯蔵量（Kiss/FF一致）', '低', '+790億立方フィート', '+640億立方フィート'),
    ('23:40', '🇺🇸 米', 'カシュカリ・ミネアポリス連銀総裁 発言（投票権あり。Kissのみ・要確認）', '低', '要人発言', '—'),
    ('26:00', '🇺🇸 米', '30年債入札（Kiss/FF一致。10/9 02:00 JST）', '低', '220億ドル', '5.31%|2.6倍（FF）'),
    ('26:40', '🇺🇸 米', 'ムサレム・セントルイス連銀総裁 発言（投票権なし。Kiss/FF一致。10/9 02:40 JST）', '低', '要人発言', '—'),
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
              <li>主要市場の休場: なし（中国の国慶節休場は10/7で終了し本日から再開。ForexFactory・KissFXに本日の休場掲載なし）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-07）</h3>
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
