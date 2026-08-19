import glob, os
from datetime import datetime as _dt

TODAY = '2026-08-20'
WEEKDAY = '木'
HERO_SUB = '前日NY市場でドル円は159.60円台から一時158.17円まで急落、米財務省による米国債買い戻し規模拡大の発表と米10年債利回りの低下が主因。本日は10:30の豪雇用統計と21:30の米新規失業保険申請件数・フィラデルフィア連銀景況指数に注目。'

REPORT_SUMMARY = '米国債買い戻し拡大でドル安進行、本日は豪雇用統計とフィラデルフィア指数に注目'
RISK_LEVEL = 'MEDIUM'
RISK_COLOR = 'var(--orange)'

SUMMARY_PARAGRAPH = (
    '前日8/19（水）のNY市場では、東京時間159.60円台で始まったドル円が米長期金利の低下を背景に159.21円前後まで弱含んだ後、'
    '米財務省が残存期間10〜20年・20〜30年の利付国債を対象とした買い戻しオペの1回あたり規模を従来の上限20億ドルから少なくとも40億ドルへ倍増すると発表したことを受けて急落、'
    '一時158.17円まで下値を広げた。この発表を受けて米10年債利回りは4.63%台へ急低下し、ドル売りが強まった。同日公表された7/28-29開催分のFOMC議事録では、'
    '参加者の間でインフレリスクが上方に傾斜したとの判断が示された一方、会合直後に発表された7月雇用統計・CPIの冴えない結果を受けて早期利上げ観測はすでに後退していたため、相場への追加インパクトは限定的だった。'
    '本日8/20（木）は、10:30発表の豪雇用統計（失業率・新規雇用者数、ForexFactoryでHigh Impact）が最大の焦点で、21:30には米新規失業保険申請件数とフィラデルフィア連銀景況指数（ともに前回から鈍化予想）が発表される。'
    '前日からの米長期金利低下・ドル安の流れが継続するか、米指標の結果次第で夜間のドル円の反発余地を見極めたい。'
)

FOCUS_CURRENCY_TITLE = 'AUD/USD 🇦🇺🇺🇸'
FOCUS_CURRENCY_BODY = '本日10:30発表の豪雇用統計（失業率・新規雇用者数、ForexFactoryでHigh Impact）が最大の材料。4Hデイトレ適性ランキング2位（スコア46・ADX34.6で上昇トレンド継続）'

RISK_BODY = '10:30の豪雇用統計（High Impact）に加え、21:30の米新規失業保険申請件数・フィラデルフィア連銀景況指数（ともにMedium Impact）が重なる。前日からの米長期金利低下・ドル安基調が続くかを見極める材料が多く、値動きが出やすい一日。'

KEY_COUNT = '9件'
KEY_COUNT_BODY = '豪雇用統計（失業率・新規雇用者数）/ 米新規失業保険申請件数 / 米フィラデルフィア連銀景況指数 / 米景気先行指数 / 米30年TIPS入札 / 独PPI 等（本日の市場休場はなし）'

KEY_EVENTS_POINTS = [
    ('08:50', '🇯🇵', '貿易収支（通関ベース）', '（KissFXのみ・ForexFactoryと予想/前回が不一致のため要確認）'),
    ('10:30', '🇦🇺', '雇用統計【失業率・新規雇用者数】', '<span class="badge-important">★最重要</span>（KissFX・ForexFactoryで失業率は一致、新規雇用者数の予想値は相違・要確認）'),
    ('15:00', '🇩🇪', '生産者物価指数【前月比/前年比】', '（KissFX・ForexFactoryでほぼ一致）'),
    ('19:00', '🇬🇧', 'CBI企業動向調査', '（KissFX・ForexFactory一致）'),
    ('21:30', '🇺🇸', '新規失業保険申請件数', '<span class="badge-important">★最重要</span>（KissFX・ForexFactory一致）'),
    ('21:30', '🇺🇸', 'フィラデルフィア連銀景況指数', '<span class="badge-important">★最重要</span>（KissFX・ForexFactoryでほぼ一致）'),
    ('23:00', '🇺🇸', '景気先行指数【前月比】', '（KissFX・ForexFactory一致）'),
    ('26:00', '🇺🇸', '30年インフレ連動債(TIPS)入札', '（KissFXのみ）'),
    ('翌07:45', '🇳🇿', '貿易収支', '（KissFXのみ・要確認）'),
]

OTHER_POINTS = [
    ('米長期金利低下でドル全面安', '米財務省の国債買い戻し規模拡大の発表を受けて米10年債利回りが4.63%台へ急低下し、ドル円は159円台後半から158円台前半まで急落した。'),
    ('FOMC議事録はインフレ警戒も市場反応は限定的', '7/28-29開催分の議事録では参加者がインフレリスクの上方傾斜を指摘したが、会合後の7月雇用統計・CPIの下振れで早期利上げ観測はすでに後退しており、相場への追加インパクトは限定的だった。'),
    ('本日は豪雇用統計が最大の焦点', '10:30発表の豪雇用統計（失業率・新規雇用者数）はForexFactoryでHigh Impact。結果次第でAUD/USD・AUD/JPYの値動きが大きくなりやすい。'),
    ('夜間は米指標ラッシュ', '21:30の新規失業保険申請件数・フィラデルフィア連銀景況指数、23:00の景気先行指数と米経済指標が相次ぐ。前回からの鈍化が予想されており、ドル安基調が続くか見極めたい。'),
]

MARKET_ENV_BODY = (
    '8/20（木）は前日NY市場での米長期金利低下・ドル安（ドル円158.17円まで急落）を引き継ぎ、東京時間はドル安地合いで始まる見通し。'
    '前日は米財務省による国債買い戻し規模拡大の発表が最大の材料となり、7/28-29開催分のFOMC議事録は市場予想通りの内容にとどまり反応は限定的だった。'
    '本日は10:30の豪雇用統計が最大の焦点で、21:30には米新規失業保険申請件数・フィラデルフィア連銀景況指数と米指標が集中する。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派・据え置き、7/29 9対3・3人が利上げ主張） / 日銀 1.00%（正常化継続、7/31据え置き） / 豪RBA 4.35%（タカ派、8/11据え置き）'
)

RANKING_ROWS = [
    ('GBP/USD', 'ランキング1位（スコア48・見送り）。ADX35.4で上昇トレンド継続、本日は主要指標が少なく前日からのドル安の流れに連動しやすい', 'up'),
    ('AUD/USD', 'ランキング2位（スコア46・見送り）。ADX34.6で上昇トレンド継続、10:30の豪雇用統計が最大の材料', 'up'),
    ('USD/JPY', 'ランキング3位（スコア39・見送り）。ADX24.3で下降トレンド、前日の米長期金利低下・ドル安を受けて上値の重い展開が続くか注目', 'down'),
    ('NZD/USD', 'ランキング4位（スコア31・見送り）。ADX16.2でトレンド弱含み、米ドル全体の地合いに連動しやすい', 'up'),
    ('USD/CHF', 'ランキング5位（スコア29・見送り）。ADX20.7で下降トレンド、ドル安基調が続くかがポイント', 'down'),
]

REVIEW_TOPICS = [
    ('米財務省の国債買い戻し拡大でドル急落', '米財務省が残存期間10〜20年・20〜30年の利付国債を対象とした買い戻しオペの1回あたり規模を、従来の上限20億ドルから少なくとも40億ドルへ倍増すると発表。これを受けて米10年債利回りは4.63%台へ急低下し、ドル円は159.60円台から一時158.17円まで急落した。'),
    ('FOMC議事録公表もインフレ判断は織り込み済み', '7/28-29開催分のFOMC議事録が公表され、参加者はインフレリスクが上方に傾斜したと判断していたことが示された。もっとも会合直後に発表された7月雇用統計・CPIが予想を下回ったことで早期利上げ観測はすでに後退しており、議事録公表による相場への追加インパクトは限定的にとどまった。'),
    ('ユーロ円は円安基調で184円台後半', 'ユーロ円は円安地合いを継続し184円台後半で推移。ドル安・円安が同時に進む中、クロス円は総じて底堅い動きとなった。'),
    ('英CPIはBOEの利下げ観測に影響', '前々日発表の英雇用統計に続き、英CPIの結果がBOEの金融政策見通しを左右する材料として意識され、ポンド円は212〜216円のレンジを想定した見通しが示されていた。'),
]

REVIEW_HANDOVER = '本日（8/20木）への引継ぎ：前日の米財務省による国債買い戻し拡大発表を受けた米長期金利低下・ドル安の流れを引き継ぐ。本日は10:30の豪雇用統計、21:30の米新規失業保険申請件数・フィラデルフィア連銀景況指数が焦点となり、ドル安基調が継続するかを見極めたい。'

CALENDAR_ROWS = [
    ('08:50', '🇯🇵 日本', '貿易収支（通関ベース）（KissFXのみ・ForexFactory換算値と相違のため要確認）', '△', '-6800億', '-4069億'),
    ('10:00', '🇦🇺 豪州', 'MI消費者物価期待（要確認・ForexFactoryのみ）', '低', '—', '4.7%'),
    ('10:00', '🇨🇳 中国', '1年/5年ローンプライムレート（要確認・ForexFactoryのみ、KissFX非掲載）', '低', '3.00%/3.50%', '3.00%/3.50%'),
    ('10:30', '🇦🇺 豪州', '<strong>失業率</strong>（KissFX・ForexFactory一致、ForexFactoryでHigh Impact）', '<strong>★★★</strong>', '<strong>4.4%</strong>', '4.4%'),
    ('10:30', '🇦🇺 豪州', '新規雇用者数（KissFX予想+1.50万人・ForexFactory予想+1.17万人で相違・要確認、ForexFactoryでHigh Impact）', '★★★', '+1.50万人（KissFX）/+1.17万人（FF）', '+7.63万人'),
    ('12:35', '🇯🇵 日本', '20年利付国債入札（KissFXのみ）', '△', '—', '—'),
    ('15:00', '🇩🇪 独', '生産者物価指数【前月比/前年比】（前月比はKissFX・ForexFactoryでほぼ一致）', '△', '+0.6%/+2.5%（KissFX）', '-0.3%/+1.8%'),
    ('15:00', '🇨🇭 スイス', '貿易収支（KissFXのみ・要確認）', '低', '—', '+38.0億'),
    ('19:00', '🇩🇪 独', 'ブンデスバンク月報（要確認・ForexFactoryのみ）', '低', '—', '—'),
    ('19:00', '🇬🇧 英国', 'CBI企業動向調査（KissFX・ForexFactory一致）', '△', '-40', '-45'),
    ('21:30', '🇨🇦 加', '鉱工業製品価格【前月比】（KissFX・ForexFactoryでほぼ一致）', '△', '-0.5%（KissFX）/-0.4%（FF）', '-1.4%'),
    ('21:30', '🇨🇦 加', '原料価格指数【前月比】（KissFX・ForexFactoryでほぼ一致）', '△', '-2.0%（KissFX）/-1.8%（FF）', '-6.9%'),
    ('21:30', '🇨🇦 加', '新築住宅価格指数【前月比】（要確認・ForexFactoryのみ）', '低', '0.0%', '-0.1%'),
    ('21:30', '🇺🇸 米国', '<strong>新規失業保険申請件数</strong>（KissFX・ForexFactory一致）', '<strong>★★</strong>', '<strong>21.0万件</strong>', '20.9万件'),
    ('21:30', '🇺🇸 米国', '<strong>フィラデルフィア連銀景況指数</strong>（KissFX・ForexFactoryでほぼ一致）', '<strong>★★</strong>', '<strong>+25.0（KissFX）/+24.1（FF）</strong>', '+41.4'),
    ('23:00', '🇺🇸 米国', '景気先行指数【前月比】（KissFX・ForexFactory一致）', '△', '+0.1%', '-0.2%'),
    ('23:30', '🇺🇸 米国', '週間天然ガス貯蔵量（KissFX・ForexFactoryでほぼ一致）', '低', '+15B（FF）', '+36（KissFX）/36B（FF）'),
    ('24:10', '🇺🇸 米国', 'ムサレム・セントルイス連銀総裁発言（投票権なし）（KissFXのみ）', '低', '要人発言', '—'),
    ('26:00', '🇺🇸 米国', '30年インフレ連動債(TIPS)入札（KissFXのみ）', '★', '80億ドル', '—'),
    ('翌07:45', '🇳🇿 NZ', '貿易収支（KissFXのみ・要確認）', '低', '—', '+0.23億'),
]

DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

report_files = sorted(glob.glob('reports/*.html'), reverse=True)
prior_files = [f for f in report_files if os.path.basename(f) != f'{TODAY}.html']

def sidebar_archive(files, limit=10):
    items = ''
    for f in files[:limit]:
        name = os.path.basename(f).replace('.html', '')
        try:
            d = _dt.strptime(name, '%Y-%m-%d')
            wd = DAYS[d.strftime('%A')]
            label = f'{name}（{wd}）'
        except Exception:
            label = name
        items += f'<li><a href="{name}.html">{label}</a></li>\n'
    return items

SIDEBAR_ARCHIVE = sidebar_archive(prior_files)

points_items_html = '\n'.join(
    f'              <li>{t} {flag} {title} {note}</li>'
    for t, flag, title, note in KEY_EVENTS_POINTS
)

other_points_html = '\n'.join(
    f'              <li><strong>{title}</strong>：{body}</li>'
    for title, body in OTHER_POINTS
)

ranking_rows_html = ''
for pair, desc, direction in RANKING_ROWS:
    dir_html = {'up': '<span class="trend-up">↑</span>', 'down': '<span class="trend-down">↓</span>', 'range': '<span class="trend-range">→</span>'}[direction]
    ranking_rows_html += f'''            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td>{dir_html}</td>
            </tr>
'''

review_topics_html = ''
for i, (title, body) in enumerate(REVIEW_TOPICS, start=1):
    review_topics_html += f'''          <div class="topic">
            <div class="topic-title">【トピック{"①②③④⑤"[i-1]}】{title}</div>
            {body}
          </div>
'''

calendar_rows_html = ''
for time_, country, title, impact, forecast, previous in CALENDAR_ROWS:
    calendar_rows_html += f'            <tr><td>{time_}</td><td>{country}</td><td>{title}</td><td>{impact}</td><td>{forecast}</td><td>{previous}</td></tr>\n'

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
{SIDEBAR_ARCHIVE}      </ul>
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
        <h3>{REPORT_SUMMARY}</h3>
        <p>{SUMMARY_PARAGRAPH}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>{FOCUS_CURRENCY_TITLE}</h3>
        <p>{FOCUS_CURRENCY_BODY}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:{RISK_COLOR}">{RISK_LEVEL}</h3>
        <p>{RISK_BODY}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_COUNT}</h3>
        <p>{KEY_COUNT_BODY}</p>
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
              <li>本日、主要国の市場休場はなし</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
{points_items_html}
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
{other_points_html}
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
          {MARKET_ENV_BODY}
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
{ranking_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日04:47 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-08-19）</h3>
          <span>水曜日の主要トピック</span>
        </div>
        <div class="report-body">
{review_topics_html}          <div class="handover">
            <strong>{REVIEW_HANDOVER}</strong>
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
            <tr><td>終日</td><td>🌍 主要国</td><td>本日、主要国の市場休場はなし</td><td>—</td><td>—</td><td>—</td></tr>
{calendar_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。本日の主要市場休場はありません。本日の焦点は10:30の豪雇用統計と21:30の米新規失業保険申請件数・フィラデルフィア連銀景況指数です。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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
