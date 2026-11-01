# -*- coding: utf-8 -*-
"""FX日報 2026-11-02（月）生成スクリプト"""
import glob, os

TODAY = '2026-11-02'
WEEKDAY = '月'

HERO_TITLE_SUB = (
    '前営業日10/30（金）のドル円は156.96円まで下げた後、157.64円まで戻して引けた。'
    '本日11/2（月）は米10月ISM製造業景況指数（24:00）が主な材料で、明日11/3は日本が休場、米中間選挙とRBA政策発表を控える。'
)

SUMMARY_HEADLINE = (
    '日銀の12月利上げ観測とAI関連株安でドル円は157円台半ばまで戻して引け、ユーロドルは1.115ドル台。'
    '本日は米ISM製造業指数と11/3の米中間選挙・RBA発表の前でポジション調整が中心'
)

SUMMARY_BODY = (
    '10/30（金）のNY市場でドル円は日銀の12月利上げ観測から円買いが強まり156.96円まで下落した後、157.64円まで戻して引けた（ザイFX）。'
    'AI投資の収益化への懸念からNYダウは572ドル安（-1.09%）、COMEX金12月限は3.46%安の3,892.10ドルと大幅続落し、現金確保の売りが広がった（ザイFX）。'
    '日銀は10/30に政策金利1.25%を据え置いた（ザイFX・Admirals。結果の詳細は要確認）。'
    '本日は米ISM製造業景況指数（予想54.7、前回54.5）が米国の注目指標で、Appleの決算が米株引け後に控える（KissFX・ForexFactory）。'
)

TOP_PAIR_BODY = (
    'ドル円は10/30に156.96〜157.64円で推移し157.64円で引けた（ザイFX）。日銀の12月利上げ観測が円の下支えとなる一方、為替介入への思惑が上値を抑える（KissFX）。'
    '本日24:00の米ISM製造業景況指数（予想54.7）で米長期金利が動けば、ドル円の方向が決まる。'
    '4時間足ランキング（10/30 08:28 JST生成・本日分は未更新）ではEUR/JPYが1位（スコア61・候補、ADX29.7、レンジ）、USD/JPYは5位（スコア51・候補、ADX20.0、上昇）。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'AI関連株の下落、フランスの格付け見通し引き下げ（フィッチ）、イラン情勢（米中間選挙後に攻撃再開の思惑・KissFX）が重なる。'
    '明日11/3に米中間選挙とRBA、11/5にBOE、11/6に米雇用統計と植田日銀総裁の発言が続く。'
)

KEY_EVENTS_COUNT = '3件'
KEY_EVENTS_SUMMARY = (
    '米 ISM製造業景況指数(24:00)、独 ナーゲル連銀総裁発言(21:00)、10:45 中 RatingDog製造業PMI。米株引け後にApple決算'
)

MARKET_OVERVIEW = (
    '<strong>VIX</strong>：Investing.comが403のため取得不可（要確認）。'
    '<strong>米10年債・2年債利回り</strong>：同じく取得不可（要確認）。'
    '<strong>ドル指数（DXY）</strong>：取得不可（要確認）。'
    '<strong>金</strong>：COMEX12月限は3.46%安の3,892.10ドルで引けた（ザイFX）。AI関連株の下落で現金確保の売りが広がった。'
    '<strong>原油</strong>：WTIの水準は取得不可（要確認）。ザイFXは10/30の原油先物を小幅高と伝えている。'
    'NYダウは572ドル安（-1.09%）。ユーロ円は3日ぶり反落の175.78円（ザイFX）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 3.00％（要確認）、BOC 2.50％（要確認）、SNB 0.00％（詳細は下表）。'
    '<br><br><strong>今週の焦点：</strong> 11/3 米中間選挙・RBA（四半期報告・総裁会見）・米JOLTS求人、11/4 ユーロ圏CPI速報・米ADP・ISM非製造業、11/5 BOE（四半期報告・総裁会見）、11/6 米雇用統計・加雇用統計・植田日銀総裁の発言（KissFX）。'
)

RANKING_ROWS = [
    (1, 'EUR/JPY', 'rank-c', 'C', '直近スコア61・候補。ADX29.7、ADR比91.2％、方向はレンジ。AI投資懸念とフランス財政不安のユーロ売り、リスクオフの円買いが重なり175円台後半で反落。', 'trend-range', '→'),
    (2, 'NZD/USD', 'rank-c', 'C', '直近スコア57・候補。ADX28.5、ADR比83.3％、方向は下降。RBNZ決定後の水準は要確認。', 'trend-down', '↓'),
    (3, 'GBP/JPY', 'rank-c', 'C', '直近スコア57・候補。ADX25.9、ADR比83.5％、方向は上昇。ポンドドルは9/16以来の高値、BOE利上げがほぼ確実視されている（みんかぶ）。', 'trend-up', '↑'),
    (4, 'AUD/JPY', 'rank-c', 'C', '直近スコア52・候補。ADX16.4、ADR比95.4％、方向は上昇。11/3のRBA発表前。', 'trend-up', '↑'),
    (5, 'USD/JPY', 'rank-c', 'C', '直近スコア51・候補。ADX20.0、ADR比82.7％、方向は上昇。157円台半ばで日銀12月利上げ観測と介入警戒が綱引き。', 'trend-up', '↑'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/30 08:28 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、10/30時点の数値。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        '日銀は据え置き、12月利上げ観測でドル円は156.96円まで下げて157.64円で引け',
        '10/30のNY市場でドル円は日銀の12月利上げ観測から円買いが強まり156.96円まで下落したが、中東情勢も材料視され157.64円まで戻して引けた（ザイFX）。'
        '日銀は10/30に政策金利を1.25%で据え置いた（ザイFX・Admirals。票数・展望レポートの詳細は要確認）。みんかぶはCFTC建玉で円の買い越しが増加したと伝えている。',
    ),
    (
        'AI投資の収益化懸念で米株安、ダウは572ドル安、金は3.46%安の3,892ドル',
        'NYダウは572ドル安（-1.09%）。AI投資の収益化・持続性への懸念が広がった。COMEX金12月限は現金確保の売りで3.46%安の3,892.10ドルと大幅続落した（ザイFX）。'
        'ユーロ円もリスクオフで3日ぶり反落の175.78円で引けた。欧州株はまちまちで英国株のみ上昇した。',
    ),
    (
        'ユーロドルは1.12ドル台に乗せた後1.115ドル台へ反落、フランスの格付け見通しが引き下げ',
        '先週はFOMC後のドル売りでユーロドルが一時1.12ドルに乗せたが、週末は1.11ドル台半ばへ反落した（KissFX）。'
        '週末にフィッチがフランスの格付け見通しを引き下げたが、現時点の市場への影響は限定的（ザイFX）。ECBは10/29に政策金利を据え置き、12月の利上げ期待は残る（みんかぶ）。',
    ),
    (
        'FOMCは3.75〜4.00%で据え置き、12月利上げ観測が残る',
        'FRBは10/28のFOMCで政策金利を3.75〜4.00%に据え置いた（賛成10・反対2、クックとハマックの2名が利上げを主張。Admirals Marketsの報道で単独ソース・要確認）。'
        'ウォーシュ議長の会見後はドル売りが優勢となったが、週末にかけてドル買いが戻った（KissFX）。次回FOMCは12/9。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/2月）への引継ぎ：ドル円は157.64円、ユーロ円は175.78円、金は3,892.10ドルで週末を終えた。'
    '本日は米ISM製造業景況指数（24:00）とApple決算が材料で、11/3の米中間選挙とRBA、11/5のBOE、11/6の米雇用統計を前にポジション調整が出やすい。'
    '日銀の12月利上げ観測は円の下支え、為替介入への思惑はドル円の上値を抑える。'
)

POINTS_EVENTS = [
    '09:30 🇦🇺 豪 住宅建設許可件数（予想+1.8〜+2.0%、前回-6.1%）',
    '10:45 🇨🇳 中 RatingDog（旧財新）製造業PMI（予想52.0、前回52.1）',
    '16:00 🇩🇪 独 小売売上高 前月比（予想+0.4%、前回+1.3%）',
    '18:00 🇪🇺 ユーロ圏 製造業PMI【改定値】（予想52.4、前回52.4）／18:30 🇬🇧 英 製造業PMI【改定値】（予想52.8）',
    '21:00 🇩🇪 ナーゲル独連銀総裁 発言',
    '24:00（翌00:00）🇺🇸 米 ISM製造業景況指数（予想54.7、前回54.5）。ISM製造業価格（予想77.2、前回77.9）',
    '25:15（翌01:15）🇺🇸 グールズビー・シカゴ連銀総裁 発言（KissFXのみ・要確認）',
    '米株引け後 🇺🇸 Apple 決算',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：日銀の12月利上げ観測と介入警戒が上値を抑える、157円台半ば',
        'ドル円は10/30に156.96〜157.64円で推移（ザイFX）。円は12月利上げ観測とCFTCの円買い越し増加で支えられる一方、米長期金利の上昇はドル買い材料。24:00のISM製造業指数が米金利を通じてドル円の方向を決める。',
    ),
    (
        'ユーロ：フランス財政不安とECB利上げ期待が綱引き',
        'フィッチによるフランスの格付け見通し引き下げ（ザイFX）が重し。一方でECBの12月利上げ期待は残る（みんかぶ）。18:00のユーロ圏製造業PMI改定値（予想52.4）と、11/4のユーロ圏CPI速報が次の材料。',
    ),
    (
        '株式・商品：AI投資懸念とApple決算',
        'AI関連株の下落が先週末のリスクオフの発端。米株引け後のApple決算（KissFX）で米株の方向が決まり、為替では円の動きに直結する。金は3,892ドルまで下落。',
    ),
    (
        '休場：本日は主要市場の休場なし、明日11/3は日本が休場',
        'KissFX・ForexFactoryで本日の休場は確認されない。明日11/3（火）は日本の祝日で東京市場が休場（日経225先物・オプションは祝日取引あり、KissFX）。米国の中間選挙の結果は日本時間11/4以降に判明する。',
    ),
    (
        '今週のイベント：11/3 RBA、11/5 BOE、11/6 米雇用統計',
        'RBAは11/3に政策発表（四半期金融政策報告・総裁会見あり）、BOEは11/5（四半期報告・総裁会見あり、利上げがほぼ確実視・みんかぶ）。11/6は米雇用統計・加雇用統計・植田日銀総裁の発言（KissFX）。米冬時間入りで指標の発表時刻が1時間遅くなる。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('09:00', '🇦🇺 豪', 'MIインフレーションゲージ 前月比（FFのみ・要確認）', '低', '—', '0.3%'),
    ('09:30', '🇦🇺 豪', '住宅建設許可件数 前月比（Kiss/FF一致）', '低', '+2.0%（FF +1.8%）', '-6.1%'),
    ('09:30', '🇯🇵 日', '製造業PMI【改定値】（FFのみ・要確認）', '低', '53.3', '53.3'),
    ('09:45', '🇦🇺 豪', 'ANZ求人広告 前月比（FFのみ・要確認）', '低', '—', '2.2%'),
    ('10:45', '🇨🇳 中', 'RatingDog（旧財新）製造業PMI（Kiss/FF一致）', '低', '52.0', '52.1'),
    ('14:30', '🇦🇺 豪', '商品価格 前年比（FFのみ・要確認）', '低', '—', '15.5%'),
    ('16:00', '🇩🇪 独', '小売売上高 前月比（Kiss/FF一致）', '低', '+0.4%', '+1.3%'),
    ('16:30', '🇨🇭 スイス', '小売売上高 前年比（Kiss/FF一致）', '低', '—（FF 3.0%）', '+3.2%'),
    ('17:15', '🇪🇺 西', '製造業PMI（FFのみ・要確認）', '低', '50.4', '51.0'),
    ('17:30', '🇨🇭 スイス', '製造業PMI（Kiss/FF一致）', '低', '55.4（FF 55.3）', '55.3'),
    ('17:45', '🇪🇺 伊', '製造業PMI（FFのみ・要確認）', '低', '49.9', '50.4'),
    ('17:50', '🇫🇷 仏', '製造業PMI【改定値】（Kiss/FF一致）', '低', '49.3', '49.3'),
    ('17:55', '🇩🇪 独', '製造業PMI【改定値】（Kiss/FF一致）', '低', '54.2', '54.2'),
    ('18:00', '🇪🇺 ユーロ圏', '製造業PMI【改定値】（Kiss/FF一致）', '低', '52.4', '52.4'),
    ('18:30', '🇬🇧 英', '製造業PMI【改定値】（Kiss/FF一致）', '低', '52.8', '52.8'),
    ('21:00', '🇩🇪 独', 'ナーゲル独連銀総裁 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('23:30', '🇨🇦 加', '製造業PMI（FFのみ・要確認）', '低', '—', '51.5'),
    ('23:45', '🇺🇸 米', '製造業PMI【改定値】（Kiss/FF一致）', '低', '56.0', '56.0'),
    ('24:00', '🇺🇸 米', 'ISM製造業景況指数（Kiss/FF一致）', '中', '54.7（Kiss 54.6）', '54.5'),
    ('24:00', '🇺🇸 米', '建設支出 前月比（Kiss/FF一致）', '低', '+0.3%', '+0.9%'),
    ('24:00', '🇺🇸 米', 'ISM製造業価格（FFのみ・要確認）', '低', '77.2', '77.9'),
    ('25:15', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（KissFXのみ・要確認）', '低', '要人発言', '—'),
    ('米株引け後', '🇺🇸 米', 'Apple 決算（KissFX）', '—', '—', '—'),
    ('翌06:45', '🇳🇿 NZ', '住宅建設許可 前月比（Kiss/FF一致）', '低', '—', '+5.6%'),
]
def _key(r):
    t = r[0]
    if t.startswith('米株'): return (99, 0)
    if t.startswith('翌'): return (100, 0)
    return (int(t[:2]), int(t[3:5]))
CAL_ROWS.sort(key=_key)

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

FUNDAMENTALS_ROWS = [
    ('FRB', '🇺🇸 USD', '3.75–4.00%', 'var(--red)', 'タカ派',
     '10/28のFOMCで据え置き（Admirals Marketsの報道。賛成10・反対2でクック、ハマックが利上げを主張・要確認）。9月に0.25%利上げ済み。12月利上げの織り込みは75〜86％（Admirals・要確認）。次回FOMCは12/9。'),
    ('日銀', '🇯🇵 JPY', '1.25%', 'var(--blue)', 'タカ派',
     '10/30会合で1.25%を据え置き（ザイFX・Admirals）。会合後も12月利上げ観測から円買いが強まった（ザイFX）。11/6に植田総裁の発言。次回会合は12/18。'),
    ('ECB', '🇪🇺 EUR', '2.50%', 'var(--red)', 'タカ派',
     '10/29の理事会で預金金利2.50%を据え置き（ザイFX）。12月の利上げ期待は残る（みんかぶ）。フランスの格付け見通し引き下げが重し。次回は12/17。'),
    ('BOE', '🇬🇧 GBP', '3.75%', 'var(--muted)', 'タカ派寄り',
     '政策金利3.75%（9/17据え置き）。11/5のMPCは利上げがほぼ確実視されている（みんかぶ）。ポンドドルは9/16以来の高値。'),
    ('RBA', '🇦🇺 AUD', '4.60%', 'var(--red)', 'タカ派',
     '9/29に0.25%利上げして4.60%。11/3に政策発表（四半期金融政策報告・総裁会見あり）。方向性は報道で未確認（要確認）。'),
    ('RBNZ', '🇳🇿 NZD', '3.00%（要確認）', 'var(--red)', 'タカ派',
     '10/28〜29の会合で利上げとザイFXが報道。前回2.75%からの0.25%引き上げで3.00%とみられるが、決定後の水準は公式発表で未確認（要確認）。次回は12/9。'),
    ('BOC', '🇨🇦 CAD', '2.50%（要確認）', 'var(--red)', 'タカ派転換',
     '10/28会合で予想に反して利上げとザイFXが報道。Forex Fundamentalsは2.50%（前回2.25%）と表示するが、単独ソースのため要確認。次回は12/9。'),
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
              <li>🇳🇿 ニュージーランド市場休場（KissFX・ForexFactory一致）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-30 金）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。Admirals Markets・みんかぶ・KissFX・ザイFXの報道で照合。前回更新（10/26）から、10/28〜29にRBNZ・BOCが利上げ（水準は要確認）、日銀・ECB・FRBは据え置き。最新情報は各中銀の公式サイトでご確認ください。</p>
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
