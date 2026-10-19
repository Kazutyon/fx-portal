# -*- coding: utf-8 -*-
"""FX日報 2026-10-20（火）生成スクリプト"""
import glob, os

TODAY = '2026-10-20'
WEEKDAY = '火'

HERO_TITLE_SUB = (
    '前営業日10/19（月）のドル円は157円70銭〜158円55銭で推移し、158円50銭で引けた。'
    '本日10/20（火）は15:00の英雇用統計と21:30の米住宅着工件数が材料で、市場休場はなく、米株引け後にネットフリックスが決算を発表する。'
)

SUMMARY_HEADLINE = (
    'ドル円は米10年債利回りの5.14％台への上昇で158円50銭まで上げて引け、ユーロはフランスの暴動激化で1.1213ドルへ反落。'
    '本日は15:00の英雇用統計が最大の材料'
)

SUMMARY_BODY = (
    '10/19（月）のNY市場では、中東情勢悪化による原油高と仏暴動の激化によるフランス国債の下落が米国債にも波及し、米10年債利回りが5.14％台まで上昇してドル買い・円売りが進み、ドル円は158.55円の日通し高値を付けて158.50円で引けた（ザイFX）。'
    'ユーロドルは週明けのオセアニア時間に1.1183ドルまで下落した後、欧米時間に下げ渋り1.1213ドルで引けた（ザイFX・みんかぶ）。'
    '本日の市場休場はない（KissFXの休場日一覧では次の休場は10/26のNZ）。経済指標は15:00の英雇用統計と21:30の米住宅着工件数・建設許可件数が中心で、米株引け後にネットフリックスが決算を発表する（KissFX・ForexFactory一致）。'
)

TOP_PAIR_BODY = (
    'ドル円は10/19に157.70〜158.55円で推移し、本日朝は158.40円台（みんかぶ）。米10年債利回りの上昇が円売り・ドル買いを支え、159円前後には売りオーダーがあり、158.57円（200日移動平均線）と14日高値158.95円が上値の目途とされる（ザイFX）。'
    'ドル円オーダーは159.00円に売りやや小さめ、159.10円超えでストップロス買いやや小さめ、158.00円にオプション（OP）20日NYカット、157.50円割れでストップロス売り小さめ（ザイFX）。'
    '4時間足ランキング（10/19 06:38 JST生成の前日分。本日分は未更新）ではUSD/JPYは上位5位に入っていない。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    '中東情勢の悪化（サウジ関連のヘリ墜落、ペルシャ湾でのタンカー2隻への攻撃の報告）で原油先物が続伸し、仏暴動の激化でフランス10年債利回りが4.94％へ上昇した（ザイFX）。'
    '来週に10/28のFOMC、10/29のECB、10/30の日銀会合を控え、為替介入への思惑も159円手前の上値を抑える（KissFX）。'
)

KEY_EVENTS_COUNT = '5件'
KEY_EVENTS_SUMMARY = (
    '日 20年国債入札(12:35) / 英 雇用統計(15:00) / 独・欧 ZEW景況感(18:00) / 米 住宅着工・建設許可件数(21:30) / 米 中古住宅販売保留(23:00)。米株引け後にネットフリックス決算'
)

MARKET_OVERVIEW = (
    '10/19のNY市場で米10年債利回りは5.14％台まで上昇した（ザイFX）。10/19の欧州市場では英10年債利回りが5.432％（+0.059％）、独10年債利回りが3.456％（+0.030％）へ上昇し、FTSE100は10,764.69（-117.21）、DAXは25,319.77（-302.84）と反落した（ザイFX）。'
    'NY原油先物は続伸し、サウジのヘリがイエメン国境付近で墜落、ペルシャ湾でタンカー2隻が攻撃を受けたとの報告で供給ひっ迫懸念が強まった（ザイFX）。'
    'ユーロについては、CFTCの建玉報告（10/13時点）で投機筋のユーロ売り越しが13万7573枚と2016年1月以来の水準に拡大している（ザイFX）。'
    'VIX・米2年債利回り・ドル指数・金の数値は本日の取得ソース（火曜日は取得対象外）で確認していないため記載しない（要確認）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（火曜日は10/19付の日報の値を引き継ぎ。KissFXの会合日程で9月以降の変更がなく、次回会合が10/28以降であることを照合）。'
    '<br><br><strong>今週の焦点：</strong> 10/21に英CPIと米メタ・テスラの決算、10/22にNZ第3四半期CPI、10/23に日本全国CPIと独・欧・英・米の製造業・非製造業PMI（速報値）。FRB高官は10/28のFOMCに向けた発言禁止期間中。次回の主要中銀は10/28（FRB・BOC・RBNZ）、10/29（ECB）、10/30（日銀）（KissFX）。'
)

RANKING_ROWS = [
    (1, 'EUR/AUD', 'rank-a', 'A', '前日生成分のスコア66・適。ADX36.6、ADR比81.8％、方向は上昇。ユーロは仏暴動で売られる一方、本日15:00の英雇用統計・18:00のZEWが欧州通貨の材料。', 'trend-up', '↑'),
    (2, 'AUD/JPY', 'rank-b', 'B', '前日生成分のスコア61・候補。ADX28.5、ADR比85.8％、方向は下降。10/19は109.86〜110.79円で110.64円引け（みんかぶ）。', 'trend-down', '↓'),
    (3, 'USD/CAD', 'rank-c', 'C', '前日生成分のスコア60・候補。ADX20.3、ADR比100.8％、方向は下降。10/19のカナダCPIは前月比+0.1％（予想+0.3％）、前年比+3.1％（予想+3.2％）と予想を下回った（みんかぶ）。', 'trend-down', '↓'),
    (4, 'AUD/USD', 'rank-c', 'C', '前日生成分のスコア58・候補。ADX22.3、ADR比93.6％、方向は下降。', 'trend-down', '↓'),
    (5, 'GBP/USD', 'rank-c', 'C', '前日生成分のスコア55・候補。ADX19.5、ADR比92.6％、方向は上昇。10/19は1.3333〜1.3299ドルで下落（フィスコ）。15:00の英雇用統計が材料。', 'trend-up', '↑'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/19 06:38 JST生成分（本日分は未更新のため前日データを保持）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'ドル円は米10年債利回りの5.14％台への上昇で158円50銭、日通し高値を更新して引け',
        '10/19のNY市場でドル円は158.15円から158.55円まで上昇し、終値は158.50円と前営業日NY終値（158.02円）から48銭のドル高だった。米10年債利回りが5.14％台まで上昇したことで円売り・ドル買いが進んだ。'
        '背景は、中東情勢の悪化による原油高と仏暴動の激化によるフランス国債の下落が米国債にも売りを波及させ、米長期金利を押し上げたことにある（フィスコ・ザイFX）。'
        '東京時間には植田日銀総裁が「基調物価は足元で2％にかなり近づいている」と述べ、高市首相は「高市円安・高市高金利と言われたが明確に否定する」と発言した（みんかぶ）。市場では200日移動平均線の158.57円と14日高値158.95円が上値の目途として意識されている（ザイFX）。',
    ),
    (
        'ユーロはフランスの暴動激化で1.1183ドルまで下落後、下げ渋って1.1213ドルで引け',
        '前週末のフランスの大規模デモに伴う暴動で、同国の財政懸念に社会不安が重なり、週明けのオセアニア時間にユーロドルは1.1183ドルまで下落した。ロンドン序盤にも暴動激化を背景に1.1187ドル付近まで売られたが、15日安値1.1151ドルと14日安値1.1113ドルが意識されて買い戻しが入り、終値は1.1213ドルと前営業日（1.1239ドル）から0.0026ドルのユーロ安だった（ザイFX・みんかぶ）。'
        'ルコルニュ仏首相は地方当局に必要に応じた夜間外出禁止令の導入を要請し、フランス10年債利回りは4.94％まで上昇した（フィスコ）。一方で、フランスの経常赤字は対GDP比1％未満と低く、ECBが市場混乱時に国債を無制限に買い入れる「伝達保護措置（TPI）」を導入していることから、深刻な危機には発展しないとの見方もある（みんかぶ）。'
        'ユーロ円は176.73〜177.78円で、終値177.73円。',
    ),
    (
        '米10月NAHB住宅市場指数は29と14年ぶりの低水準、ただしドルの反応は限定的',
        'NAHB住宅市場指数は29（予想31、9月32）と2012年6月以来の低水準に落ち込んだ。住宅ローン金利の上昇と建設コストの高止まりで購入者が様子見している（フィスコ）。'
        '米短期金融市場は年内あと1回の利上げを織り込む一方、10月FOMCでの2会合連続の利上げ確率は17％にとどまる（フィスコ）。指標の下振れ自体への為替の反応は限られた（ザイFX）。',
    ),
    (
        'カナダCPIは予想を下回り、英国債・独国債の利回りは上昇',
        '10/19のカナダ9月CPIは前月比+0.1％（予想+0.3％、前回-0.1％）、前年比+3.1％（予想+3.2％、前回+3.0％）だった（みんかぶ）。'
        '欧州市場では仏暴動を受けた債券売りが広がり、英10年債利回りは5.432％（+0.059％）、独10年債利回りは3.456％（+0.030％）へ上昇し、ロンドン株とフランクフルト株はそれぞれ4日ぶりに反落した（ザイFX）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/20火）への引継ぎ：ドル円は158.50円（日通し高値158.55円）、ユーロドルは1.1213ドル、WTI原油は続伸、米10年債利回りは5.14％台で10/19を終えた。'
    '本日は15:00の英雇用統計と21:30の米住宅着工件数が材料となり、米長期金利と原油の動きがドル円の方向を決める。'
    '159円前後の売りオーダーと為替介入への思惑が上値を抑え、10/28のFOMCと10/30の日銀会合を控える。'
)

POINTS_EVENTS = [
    '10:00 🇨🇳 中国 最優遇貸出金利（LPR）1年物・5年物（FFのみ・要確認。予想 3.00％・3.50％）',
    '12:35 🇯🇵 日本 20年利付国債入札（KissFXのみ・要確認。KissFXは注目度高いと評価）',
    '15:00 🇬🇧 英国 失業率・失業保険申請件数（Kiss/FF一致。KissFXは「発表でのポンドへの影響は非常に大きくなりやすい」と評価）',
    '18:00 🇩🇪🇪🇺 ドイツ・ユーロ圏 ZEW景況感調査（Kiss/FF一致。独予想 +30.0（Kiss）・+30.2（FF））',
    '21:30 🇺🇸 米国 住宅着工件数・建設許可件数（Kiss/FF一致。予想 130.0万件・138.5万件〜139万件）',
    '23:00 🇺🇸 米国 中古住宅販売保留（Kiss/FF一致。予想は前月比-1.0％（Kiss）と-0.7％（FF）で不一致・要確認）',
    '米株引け後 🇺🇸 ネットフリックス決算（KissFXのみ・要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：米長期金利の上昇でドル高が継続、159円前後の売りが上値を抑える',
        'ドル円は朝に158.40円台（みんかぶ）。米10年債利回りが5.14％台へ上昇する局面ではドル買いが強まり、159円前後では売りオーダーが意識されて158円台後半の買いには慎重な姿勢が出ている（みんかぶ・ザイFX）。'
        'ザイFXのオーダー情報では159.00円にOP20・23日NYカット、158.00円にOP20〜22日NYカットがあり、本日のNYカットに向けて158.00〜159.00円のレンジに収れんしやすい。ドル・円オプション市場のボラティリティは連日低下し、レンジ相場観測にオプション売りが入っている（ザイFX）。',
    ),
    (
        'ユーロ：フランスの暴動と財政懸念が重し、ただし1.12ドル前後で下げ渋り',
        'フランス10年債利回りは4.94％まで上昇し、独国債との利回り差は債務危機以来の水準に達した（みんかぶ）。ユーロドルは1.1183ドルと1.1187ドルの日通し安値で下げ止まり、投機筋のユーロ売り越しは2016年1月以来の水準まで膨らんでいる（ザイFX）。'
        '夜間外出禁止令の導入など仏情勢が悪化すればユーロ売りが再燃し、15日安値1.1151ドル、14日安値1.1113ドルが下値の目安となる。',
    ),
    (
        '英国：15:00の雇用統計と10/21のCPIがポンドの材料',
        '15:00に英雇用統計が発表される（予想：失業率4.9％（FF）、平均賃金3.8％（FF）、失業保険申請件数+1.94万件（FF））。失業率の前回値はKissFX 4.4％とFF 4.9％で不一致のため要確認。'
        '英10年債利回りは10/19に5.432％へ上昇し、10/21には英CPIが発表される。11/5のBOE会合での追加利上げ観測がポンドの下支えとなる（10/19付日報のみんかぶ報道を引き継ぎ）。',
    ),
    (
        '中東情勢：原油が続伸し、フーシ派の攻撃でサウジが国際投資会議を延期',
        'NY原油先物は続伸し、ペルシャ湾でタンカー2隻が攻撃を受けたとの報告で供給ひっ迫懸念が強まった（ザイFX）。サウジは、フーシ派による攻撃が続いていることを受け、国際投資会議「FII」を来年に延期すると発表した（みんかぶ）。'
        '原油高は米インフレ懸念と米長期金利の上昇を通じてドル高要因となる。',
    ),
    (
        '休場：本日は主要市場の休場なし',
        'KissFXの主要国の休場日一覧では、10/19の香港・中国の次は10/26のニュージーランド。本日10/20に休場する主要市場は確認されない。',
    ),
    (
        '今週のイベント：英CPI・NZ CPI・日本CPI・PMIと米主要企業決算',
        'KissFXによると、10/21に英CPI・米20年債入札・米メタとテスラの決算、10/22にNZ第3四半期CPI、10/23に日本全国CPIと独・欧・英・米の製造業・非製造業PMI（速報値）が発表される。'
        'FRB高官は発言禁止期間中で、10/28のFOMCまで要人発言による方向付けは出にくく、米長期金利と原油が材料になる。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('00:30', '🇨🇦 加', 'BOC企業景況感調査（FFのみ・要確認）', '低', '—', '—'),
    ('10:00', '🇨🇳 中', '最優遇貸出金利（LPR）1年物（FFのみ・要確認）', '低', '3.00%', '3.00%'),
    ('10:00', '🇨🇳 中', '最優遇貸出金利（LPR）5年物（FFのみ・要確認）', '低', '3.50%', '3.50%'),
    ('12:35', '🇯🇵 日', '20年利付国債入札（KissFXのみ・要確認）', '—', '—', '—'),
    ('15:00', '🇩🇪 独', '生産者物価指数 前月比（Kiss/FF一致。予想はKiss+1.6％・FF+1.5％で不一致・要確認）', '低', '+1.6%(Kiss)', '+1.1%'),
    ('15:00', '🇩🇪 独', '生産者物価指数 前年比（Kissのみ・要確認）', '低', '+6.3%', '+4.6%'),
    ('15:00', '🇬🇧 英', '失業率（Kiss/FF一致。前回はKiss4.4％・FF4.9％で不一致・要確認）', '低（Kiss: ポンドへの影響大）', '4.9%(FF)', '4.9%(FF)'),
    ('15:00', '🇬🇧 英', '失業保険申請件数（Kiss/FF一致）', '低', '+1.94万件(FF)', '+2.78万件'),
    ('15:00', '🇬🇧 英', '平均賃金（ボーナス込み）3か月/前年比（FFのみ・要確認）', '中', '+3.8%', '+3.9%'),
    ('15:00', '🇨🇭 スイス', '貿易収支（Kissのみ・要確認）', '—', '—', '+56.1億'),
    ('17:00', '🇪🇺 欧', '経常収支（FFのみ・要確認）', '低', '292億ユーロ', '276億ユーロ'),
    ('18:00', '🇩🇪 独', 'ZEW景況感調査（Kiss/FF一致。予想はKiss+30.0・FF+30.2）', '低', '+30.0(Kiss)', '+34.7'),
    ('18:00', '🇪🇺 欧', 'ZEW景況感調査（Kiss/FF一致）', '低', '+23.6(FF)', '+25.8'),
    ('18:10', '🇨🇳 中', '対内直接投資 年初来前年比（FFのみ・要確認）', '低', '—', '-5.3%'),
    ('18:33', '🇬🇧 英', '10年債入札（FFのみ・要確認）', '低', '—', '5.38|3.3'),
    ('21:15', '🇺🇸 米', 'ADP週次雇用者数変化（FFのみ・要確認）', '低', '—', '+2.48万人'),
    ('21:30', '🇺🇸 米', '住宅着工件数（Kiss/FF一致）', '低', '130.0万件', '127.5万件(Kiss)／128万件(FF)'),
    ('21:30', '🇺🇸 米', '建設許可件数（Kiss/FF一致）', '低', '138.5万件(Kiss)／139万件(FF)', '139.4万件(Kiss)／139万件(FF)'),
    ('23:00', '🇺🇸 米', '中古住宅販売保留 前月比（Kiss/FF一致。予想はKiss-1.0％・FF-0.7％で不一致・要確認）', '低', '-1.0%(Kiss)', '+0.3%'),
    ('23:00', '🇺🇸 米', '中古住宅販売保留 前年比（Kissのみ・要確認）', '低', '—', '-4.9%'),
    ('23:50', '🇳🇿 NZ', 'GDT価格指数（FFのみ・要確認）', '低', '—', '+1.2%'),
    ('26:00', '🇬🇧 英', 'グリーンMPC委員の発言（Kissのみ・要確認。翌02:00）', '要人発言', '—', '—'),
    ('米株引け後', '🇺🇸 米', 'ネットフリックス決算（Kissのみ・要確認）', '企業決算', '—', '—'),
]
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
              <li>なし（KissFXの主要国の休場日一覧に10/20の休場はない。次は10/26のニュージーランド）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-19 月）</h3>
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
