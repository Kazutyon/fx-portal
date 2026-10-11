# -*- coding: utf-8 -*-
"""FX日報 2026-10-12（月）生成スクリプト"""
import glob, os

TODAY = '2026-10-12'
WEEKDAY = '月'

HERO_TITLE_SUB = (
    '前営業日10/9（金）のドル円は158円43銭まで上昇後に158円15銭へ反落し、158円31銭で引けた。'
    '本日10/12（月）は日本・米国（債券市場）・カナダが祝日で薄商いとなり、18:30のブリーデンBOE副総裁発言が材料で、今週は10/14の米CPIと10/15の小売売上高・PPIが焦点。'
)

SUMMARY_HEADLINE = (
    'ドル円は原油高に連れた米長期金利の上昇で158円31銭に小幅高、カナダドルは雇用減で下落。'
    '本日は日米加の祝日で薄商い、今週は米CPIが焦点'
)

SUMMARY_BODY = (
    '10/9（金）のNY市場では、原油高を受けた米長期金利の上昇でドル買い・円売りが優勢となり、ドル円は158円43銭まで上昇後に158円15銭へ反落して158円31銭（前営業日のNY終値157円88銭から+0.43円）で引けた（ザイFX）。'
    'カナダの9月雇用統計は雇用が予想外に減少し、カナダドルが売られた（みんかぶ）。'
    'COMEX金12月限は中央銀行の買い観測を背景に4,221.42ドル（+1.55％）へ上昇し、NYダウは51,654.95ドル（+0.83％）で引けた（ザイFX）。'
    '本日10/12は日本がスポーツの日、米国がコロンバス・デー（債券市場休場・株式市場は通常取引）、カナダが感謝祭で休場となり、米長期金利の指標となる債券市場が動かない（KissFX・ForexFactory一致）。'
)

TOP_PAIR_BODY = (
    'ドル円は10/9に158.15〜158.43円で推移し、米10年債利回りが5.256％へ上昇する原油高局面ではドル買いが優勢になった（ザイFX・Investing.com）。'
    '先週は157円半ば〜158円半ばで上下しており、本日は米債券市場の休場でドル円の方向を決める金利材料が出ない。'
    '158円台前半を維持すれば10/7高値158.51円を再び試し、割り込めば10/5安値157.44円が下値の目安になる。'
    '4時間足ランキング（10/9 08:50 JST生成・本日分は未更新）ではUSD/JPYは7位・見送り判定（スコア46、方向はレンジ）で、本日の優先対象はEUR/USDとEUR/JPYとなる。'
)

RISK_LEVEL = 'MEDIUM'
RISK_BODY = (
    '日本・米国債券・カナダの休場で流動性が薄く、イラン攻撃の有無をめぐる報道（10/9は情報が錯綜）や原油の変動に対して値が飛びやすい。'
    '原油（WTI 92.39ドル）の動きが米長期金利とドル円を動かす構図は変わらず、フランス国債への懸念によるユーロ売りも先週から続いている（KissFX）。'
)

KEY_EVENTS_COUNT = '3件'
KEY_EVENTS_SUMMARY = (
    '英 ブリーデンBOE副総裁発言(18:30) / 英 マンMPC委員発言(21:50) / 米 ハマック・クリーブランド連銀総裁発言(翌01:10・要確認)。日米加は休場'
)

MARKET_OVERVIEW = (
    '先週金曜のドル円は、原油高を受けた米長期金利の上昇で小幅高となった。米10年債利回りは本日07時台で5.256％（+0.012）、2年債利回りは4.791％（+0.035）、ドル指数は102.26（+0.05）で、いずれも前営業日からほぼ横ばいで推移している（Investing.com）。'
    'WTI原油は92.39ドル（11月限、+0.73ドル）、金先物12月限は4,212.82ドル（-7.48ドル）、VIX（恐怖指数）は14.84（-0.57、-3.70％）で、リスク回避の動きは強まっていない。'
    'ザイFXによると、10/9はイランへの攻撃があったかどうかの情報が入り乱れたが、為替相場は小動きに留まり、AIへの期待と不安も相場の材料になった。10/10早朝には、トランプ米大統領がロシアによる軽油供給での合意を明らかにして原油が下落に転じた。'
    '本日は日本・米国債券・カナダが休場のため、ドル円・ユーロ円・加ドルの値動きは欧州時間が中心になる。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（詳細は下表。松井証券の政策金利一覧10/12更新・前回10/5の照合値で確認）。'
    '<br><br><strong>今週の焦点：</strong> 10/14に米消費者物価指数、10/15に米小売売上高と生産者物価指数。IMF・世界銀行の年次会合（バンコク、10/12〜18）。次回の主要中銀は10/28（FRB・BOC・RBNZ）、10/29（ECB）、10/30（日銀）。'
)

RANKING_ROWS = [
    (1, 'EUR/USD', 'rank-a', 'A', '直近スコア85・最適。ADX36.0、ADR比108.8％、方向は下降。フランス国債への懸念によるユーロ売りが続き、先週は一時1.11ドル後半まで下落した後は上値が重い（KissFX）。', 'trend-down', '↓'),
    (2, 'EUR/JPY', 'rank-b', 'B', '直近スコア83・最適。ADX33.0、ADR比109.2％、方向は下降。ドル円の底堅さとユーロ売りが綱引きになっている。', 'trend-down', '↓'),
    (3, 'EUR/AUD', 'rank-c', 'C', '直近スコア52・候補。ADX27.3、ADR比75.4％、方向は下降。', 'trend-down', '↓'),
    (4, 'USD/CAD', 'rank-c', 'C', '直近スコア50・候補。ADX28.5、ADR比88.9％、方向はレンジ。10/9のカナダ雇用減でカナダドルが売られた後、本日はカナダ休場で流動性が薄い。', 'trend-range', '→'),
    (5, 'AUD/USD', 'rank-c', 'C', '直近スコア49・見送り。ADX26.8、ADR比71.5％、方向は下降。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/9 08:50 JST生成分（本日分は未更新・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、休場日は流動性低下とスプレッド拡大に注意する。'
)

TOPICS = [
    (
        'ドル円は原油高に連れた米長期金利の上昇で158円43銭まで上昇、終値158円31銭',
        '10/9のNY市場でドル円は一時158.43円まで上昇後、158.15円まで反落して158.31円で引け、前営業日のNY終値157.88円から約43銭上昇した。'
        '原油高を受けた米長期金利の上昇でドル買い・円売りが優勢となった（ザイFX）。米ミシガン大学消費者信頼感指数（速報値）も材料に挙がったが、取得した記事は本文が途切れており数値は確認できていない（要確認）。'
        'みんかぶによるとロンドン時間はドル円が158円台で底堅く推移し、円安水準での振れ幅が大きくドル買い戻しも出た。',
    ),
    (
        'カナダドルは雇用統計で予想外の雇用減となり下落',
        'みんかぶは「カナダドル売られる、雇用統計で予想外の雇用減＝ＮＹ為替」と伝えている。'
        '前回（8月分）が-4.17万人と大幅減だった後の9月分も雇用が減少し、カナダ経済の弱さがカナダドル売りの理由になった（具体的な数値は取得記事で未確認・要確認）。'
        '次回のBOC金融政策発表は10/28で、本日はカナダが感謝祭で休場となる。',
    ),
    (
        'イラン攻撃をめぐる情報が錯綜、原油は反転し金は大幅高',
        'ザイFXによると、10/9はイランへの攻撃があったかどうかの情報が入り乱れ、為替は小動きに留まった。NY原油先物は+0.12ドルで引けた後、10/10早朝にトランプ大統領がロシアによる軽油供給での合意を明らかにして下落に転じた。'
        'COMEX金12月限は中央銀行の買い観測と米長期金利の低下を背景に、4,221.42ドル（+64.42ドル、+1.55％）へ上昇した。',
    ),
    (
        'ドル指数は下げ止まり、ユーロ・ポンド・株式の動き',
        'ロンドン時間にドル指数は低下が一服し、10日移動平均線が支持線として意識された（みんかぶ）。欧州ではユーロ/ポンドでポンド買いが優勢となり、みんかぶは「英中銀が11月と2月に追加利上げに踏み切る可能性が高い」との見出しを伝えている（本文は未確認・要確認）。'
        'NYダウは423.31ドル高の51,654.95ドルで引け（理由の記載なし）、10/10のCME円建て日経225先物は385円安の69,085円で推移した。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/12月）への引継ぎ：ドル円は158円31銭、WTI原油は92.39ドル、米10年債利回りは5.256％で前営業日を終えた。'
    '本日は日本・米国債券・カナダが休場で、ドル円を動かす米金利材料が出ない。欧州時間の18:30ブリーデンBOE副総裁発言と、翌01:10のハマック連銀総裁発言（要確認）が材料になる。'
    '今週は10/14の米CPIと10/15の小売売上高・PPIで10/28のFOMCに向けた流れが決まる。'
)

POINTS_EVENTS = [
    '18:30 🇬🇧 英国 ブリーデンBOE副総裁 発言（Kiss/FF一致）',
    '21:50 🇬🇧 英国 マンMPC委員 発言（Kiss/FF一致）',
    '23:15 🌐 IMF・世界銀行 年次会合 開幕（FFのみ・要確認。ザイFXはバンコクで10/12〜18開催と報道）',
    '翌01:10（25:10） 🇺🇸 米国 ハマック・クリーブランド連銀総裁 発言（投票権あり。Kissのみ・要確認）',
    '※ 米国で注目度の高い経済指標の発表はなし（KissFX）。',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：米債券市場の休場で金利の方向が出ず、158円台前半の攻防',
        'ドル円は10/9に158.43円まで上昇後158.15円へ反落し、158.31円で引けた。先週は157円半ば〜158円半ばで日替わりに上下しており（KissFX）、本日は米債券市場が休場で米長期金利が動かない。'
        '原油が反発すれば158.51円（10/7高値）を、下落すれば157.44円（10/5安値）を試す。為替介入への警戒が160円手前の上値を抑える。次回の日銀発表は10/30、FOMCは10/28。',
    ),
    (
        'ユーロ：フランス国債への懸念が続き、ユーロドルは上値が重い',
        'KissFXによると、先週は何度かフランス国債への懸念でユーロ売りの流れが強まり、ユーロドルは一時1.11ドル後半まで下落した後は上値重く推移した。'
        '10/9のロンドン時間は1.1220ドル近辺（みんかぶ）。フランスでは全国規模の抗議行動が予定されており（みんかぶ）、仏債利回りが上昇すればユーロ売りが再燃する。次回のECB発表は10/29。',
    ),
    (
        '祝日：日本・米国債券・カナダの休場で流動性低下',
        '日本はスポーツの日で東京市場が休場（日経225先物・オプションは祝日取引あり）、米国はコロンバス・デーで銀行・政府機関が休業し債券市場が休場（株式市場は通常取引）、カナダは感謝祭で休場となる（KissFX・ForexFactory一致）。'
        '参加者が減るため、ニュースや原油の変動でスプレッドが拡大し、値が飛びやすい。',
    ),
    (
        '今週のイベント：米CPI・小売売上高・PPIとFRB高官・日銀総裁の発言',
        'みんかぶとKissFXによると、10/14に米消費者物価指数、10/15に小売売上高と生産者物価指数が発表される。ウォーシュFRB議長と植田日銀総裁の発言、米主要企業の決算発表も控える。'
        '10/28のFOMCに向けて米インフレの強さが確認されればドル買いが優勢になり、弱ければドル売りに傾く。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('08:00', '🇯🇵 日', '日本 休場（スポーツの日。Kiss/FF Bank Holiday一致）', '低', '—', '—'),
    ('18:30', '🇬🇧 英', 'ブリーデンBOE副総裁 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('20:00', '🇺🇸 米', '米国 休場（コロンバス・デー。債券市場休場・株式市場は通常取引。Kiss/FF一致）', '低', '—', '—'),
    ('21:00', '🇨🇦 加', 'カナダ 休場（感謝祭。Kiss/FF Bank Holiday一致）', '低', '—', '—'),
    ('21:50', '🇬🇧 英', 'マンMPC委員 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('23:15', '🌐 全', 'IMF・世界銀行 年次会合（FFのみ・要確認）', '低', '—', '—'),
    ('25:10', '🇺🇸 米', 'ハマック・クリーブランド連銀総裁 発言（翌01:10・投票権あり。Kissのみ・要確認）', '低', '要人発言', '—'),
]
CAL_ROWS.sort(key=lambda r: (int(r[0][:2]), r[0]))

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

FUNDAMENTALS_ROWS = [
    ('FRB', '🇺🇸 USD', '3.75–4.00%', 'var(--red)', 'タカ派',
     '9/16のFOMCで0.25%利上げ（全会一致）。SEPのドットプロットでは18人中16人が年内に少なくとも1回の追加利上げを示した。10/2の雇用統計の下振れで10月利上げ確率は13％割れまで低下している（10/5時点）。'
     '今週は10/14の米CPI、10/15の小売売上高・PPIが次回FOMC（10/27-28）の判断材料となる。松井証券の一覧（10/12更新）で3.75〜4.00％を確認。'),
    ('日銀', '🇯🇵 JPY', '1.25%', 'var(--blue)', 'タカ派',
     '9/18会合で0.25%利上げ（1995年以来の高水準）。10/1公表の「主な意見」で内閣府側から利上げ影響の点検を求める意見が出て、早期の連続利上げ警戒は後退。'
     'みんかぶは次の利上げを早くて12月と報じている。今週は植田総裁の発言があり、次回会合は10/29-30。松井証券の一覧で1.25％を確認。'),
    ('ECB', '🇪🇺 EUR', '2.50%', 'var(--red)', 'タカ派',
     '9/10理事会で預金ファシリティ金利を0.25%引き上げて2.50%（主要リファイナンス金利2.65%）。9月のユーロ圏CPI速報値は前年比+3.8％と上振れた。'
     '松井証券の一覧は2.90％と表示しているが、預金金利2.50％・MRO2.65％に対応する限界貸出金利と推定される（要確認）。フランス国債への懸念がユーロの重しで、次回理事会は10/29。'),
    ('BOE', '🇬🇧 GBP', '3.75%', 'var(--muted)', '中立〜タカ派寄り',
     '9/17のMPCで6対3の分裂投票により据え置き。3委員が0.25%利上げを主張した。みんかぶは10/9に「英中銀は11月と2月に追加利上げに踏み切る可能性が高い」との見出しを伝えている（本文未確認・要確認）。'
     '本日18:30にブリーデン副総裁、21:50にマンMPC委員が発言。次回会合は11/5。松井証券の一覧で3.75％を確認。'),
    ('RBA', '🇦🇺 AUD', '4.60%', 'var(--red)', 'タカ派（総裁会見でハト派化）',
     '9/29に政策金利を4.35%から4.60%へ0.25%引き上げ。ブロック総裁の会見で据え置きも検討していたことが判明し、ハト派と受け止められて豪ドルは急落した。'
     '次回会合は11/3。松井証券の一覧で4.60％を確認。'),
    ('RBNZ', '🇳🇿 NZD', '2.75%', 'var(--red)', 'タカ派',
     '9/2の金融政策委員会で0.25%利上げし、2.25%→2.50%（7/8）→2.75%（9/2）と3会合連続の利上げ。声明は将来のOCR経路は未定でタイミングは極めて不確実と付言した。'
     '次回会合は10/28。松井証券の一覧で2.75％を確認。'),
    ('BOC', '🇨🇦 CAD', '2.25%', 'var(--muted)', '中立',
     '9/2会合で据え置き（7会合連続）。10/9の9月雇用統計は予想外の雇用減となり（みんかぶ）、カナダドル売りの材料になった。次回会合は10/28。松井証券の一覧で2.25％を確認。'),
    ('SNB', '🇨🇭 CHF', '0.00%', 'var(--muted)', 'ハト派〜中立',
     '9/24会合を経て政策金利は0.00%。ザイFXの西原宏一氏は9/29のコラムでSNBが事実上「フラン安容認」と評している。松井証券の一覧で0.00％を確認。'
     '次回会合は12/10（Investing.comのみ・要確認）。'),
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
        <em>月曜日</em>
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
              <li>🇯🇵 日本市場休場（スポーツの日。日経225先物・オプションは祝日取引あり。KissFX・ForexFactory一致）</li>
              <li>🇺🇸 米国債券市場休場（コロンバス・デー。株式市場は通常取引。KissFX・ForexFactory一致）</li>
              <li>🇨🇦 カナダ市場休場（感謝祭。KissFX・ForexFactory一致）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-09）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。松井証券の政策金利一覧（10/12 07:19更新）・みんかぶ・ザイFX・KissFX（羊飼い）の報道で照合。前回更新（10/5）から政策金利の変更はなし（各中銀の次回会合は10/27以降）。最新情報は各中銀の公式サイトでご確認ください。</p>
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
