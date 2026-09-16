import glob, os, re
from datetime import date

TODAY = '2026-09-17'
WEEKDAY = '木'
PREV_DATE = '2026-09-16'

report_files = sorted(glob.glob('reports/*.html'), reverse=True)
DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

def sidebar_archive(files, limit=10):
    items = ''
    for f in files[:limit]:
        href = f.replace(os.sep, '/')
        name = os.path.basename(f).replace('.html', '')
        try:
            d = date.fromisoformat(name)
            wd = DAYS[d.strftime('%A')]
            label = f'{name}（{wd}）'
        except Exception:
            label = name
        items += f'<li><a href="{href.replace("reports/", "")}">{label}</a></li>\n'
    return items

SIDEBAR_ARCHIVE = sidebar_archive(report_files)

HERO_P = (
    '9/16（火）は東京市場でドル円が153円台のもみ合いに終始しFOMC結果待ちの様子見ムードが強かったが、'
    '米8月小売売上高が予想を上回り3月来で最大の伸びとなったことを受けてドル買いが先行した。'
    '米東部時間9/16 14:00（日本時間9/17未明3:00）に判明したFOMCでは市場予想通り0.25%の利上げが決定されFFレートは3.75〜4.00%へ引き上げられた'
    '（2023年以来3年ぶりの利上げ）。声明・ウォーシュFRB議長の記者会見の内容がタカ派的と受け止められたことでドル全面高が加速し、'
    'ドル円は一時156.14円まで上値を伸ばした。トランプ大統領は「米国の金利は1％以下であるべき」とFRBに利下げを求める発言を行い、政治的圧力も意識されている。'
    '本日9/17（木）は20:00に英BOEの政策金利発表（3.75%据え置きが市場予想）、21:30に米新規失業保険申請件数・住宅着工件数・建設許可件数・'
    'フィラデルフィア連銀景況指数など米重要指標が集中し、FOMC後のドル高の持続性が試される一日となる。'
)

SUMMARY_H3 = (
    'FOMCが0.25%利上げでFFレート3.75〜4.00%に（2023年以来3年ぶり）。声明・会見がタカ派的と受け止められドル全面高、'
    'ドル円は一時156.14円。本日は英BOE政策金利発表と米重要指標が集中'
)

SUMMARY_P = HERO_P

TOP_CURRENCY_P = (
    '4Hデイトレ適性ランキング1位（2026-09-17 07:14時点データ、スコア61・候補、ADX25.4でレンジ、直近5日ADRは5年平均の100.4%）。'
    '前日9/16はFOMC結果待ちで東京市場は153円台もみ合いだったが、米小売売上高の上振れとFOMCの0.25%利上げ（タカ派的な声明・会見）を受けてドル買いが加速し、'
    'ドル円は日本時間9/17未明に一時156.14円まで続伸した。本日は英BOEの政策金利発表（20:00）と米重要指標（21:30）が控えており、FOMC後の上昇トレンドが継続するか試される。'
)

RISK_P = (
    '本日は日本時間未明のFOMC（0.25%利上げ、FFレート3.75〜4.00%へ）を受けたドル全面高のフォロースルーに加え、'
    '20:00に英BOEの政策金利発表（据え置き予想だが票内訳次第でポンドが振れる可能性）、21:30に米新規失業保険申請件数・住宅着工件数・建設許可件数・'
    'フィラデルフィア連銀景況指数など米重要指標が集中する。FOMC直後で持ち高調整も入りやすく、終日ボラティリティが高まりやすいためHIGHとした。'
)

KEY_INDICATOR_COUNT = '25件'
KEY_INDICATOR_SUB = '英BOE政策金利＆声明発表 / 米新規失業保険申請件数 / 米住宅着工件数・建設許可件数 / 米フィラデルフィア連銀景況指数 / NZ第2四半期GDP 等（本日の市場休場はなし）'

POINTS_HOLIDAY = ['本日9/17（木）、主要国の市場休場はありません。']

POINTS_KEY_EVENTS = [
    '07:45 🇳🇿 NZ 第2四半期GDP',
    '20:00 🇬🇧 英国 BOE政策金利＆声明発表',
    '21:30 🇺🇸 米国 新規失業保険申請件数',
    '21:30 🇺🇸 米国 住宅着工件数／建設許可件数',
    '21:30 🇺🇸 米国 フィラデルフィア連銀景況指数',
]

POINTS_OTHER = [
    (
        'FOMCが0.25%利上げを決定、FFレートは3.75〜4.00%へ（2023年以来3年ぶり）',
        '米東部時間9/16 14:00（日本時間9/17未明3:00）のFOMCでは市場予想通り0.25%の利上げが決定され、FFレートは3.75〜4.00%へ引き上げられた。'
        'ウォーシュFRB議長の記者会見（3:30〜）を含め声明・会見の内容がタカ派的と受け止められ、ドル全面高が加速した。'
    ),
    (
        'ドル円は一時156.14円まで続伸、FOMC後もドル高地合いが継続',
        'FOMC結果を受けたドル買いが継続し、ドル円は日本時間9/17未明に一時156.14円まで上値を伸ばした。9/16の東京市場は153円台のもみ合いだったが、'
        '米小売売上高の上振れとFOMCの利上げで一段高となった。'
    ),
    (
        'トランプ大統領が利下げを要求、FRBへの政治的圧力も意識',
        'トランプ大統領は「米国の金利は1％以下であるべき」と発言し、FRBの利上げ決定に対抗する姿勢を示した。今後のFRB運営に対する政治的圧力として意識されている。'
    ),
    (
        '本日20:00は英BOEの政策金利発表、3.75%据え置きが市場予想（KissFX・ForexFactory一致）',
        'BOEは3.75%での据え置きが市場予想（KissFX・ForexFactoryの2ソースで一致）。同時にMPCの票内訳（ForexFactoryのみ・要確認）や議事録も公表され、'
        '票が割れた場合はポンドが振れやすい。'
    ),
    (
        '4Hデイトレ適性ランキングは本日07:14時点データに更新済み',
        '本日04:30予定のGitHub Actionsによるランキング自動更新ジョブが完了し、本日07:14時点のデータを本レポートに反映した。'
        '現時点ではUSD/JPYとEUR/JPYが同スコア61で1位タイ。'
    ),
]

MARKET_ENV_P = (
    '9/16（火）はFOMC結果待ちで東京市場のドル円は153円台のもみ合いに終始したが、米8月小売売上高が予想を上回り3月来最大の伸びとなったことでドル買いが先行した。'
    '米東部時間9/16 14:00（日本時間9/17未明3:00）のFOMCでは市場予想通り0.25%の利上げが決定されFFレートは3.75〜4.00%へ引き上げられ（2023年以来3年ぶり）、'
    '声明・記者会見がタカ派的と受け止められたことでドル全面高が加速、ドル円は一時156.14円まで続伸した。トランプ大統領は利下げを要求する発言を行い、政治的圧力も意識されている。'
    '本日9/17（木）は20:00の英BOE政策金利発表（3.75%据え置き予想）、21:30の米新規失業保険申請件数・住宅着工件数・建設許可件数・フィラデルフィア連銀景況指数など'
    '米重要指標が集中し、FOMC後のドル高の持続性が試される一日となる。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.75〜4.00%（タカ派、9/16FOMCで0.25%利上げ実施・2023年以来3年ぶり） / '
    '日銀 1.00%（正常化継続・タカ派寄り、9/17-18会合で1.25%への利上げ方針と報道・要確認、決定は明日9/18） / '
    '英BOE 3.75%（中立〜やや引き締め警戒、本日20:00に政策金利発表・据え置き予想）'
)

RANKING_ROWS = [
    ('B', 'USD/JPY', 'ランキング1位（スコア61・候補）。ADX25.4でレンジ、直近5日ADRは5年平均の100.4%', 'trend-range', '→'),
    ('B', 'EUR/JPY', 'ランキング2位（スコア61・候補）。ADX39.3でレンジ、直近5日ADRは5年平均の81.5%', 'trend-range', '→'),
    ('B', 'NZD/USD', 'ランキング3位（スコア58・候補）。ADX43.5で下降トレンド、直近5日ADRは5年平均の74.1%', 'trend-down', '↓'),
    ('B', 'EUR/USD', 'ランキング4位（スコア56・候補）。ADX45.6で下降トレンド、直近5日ADRは5年平均の64.8%', 'trend-down', '↓'),
    ('B', 'AUD/USD', 'ランキング5位（スコア55・候補）。ADX37.3で下降トレンド、直近5日ADRは5年平均の65.0%', 'trend-down', '↓'),
]

RANKING_NOTE = (
    '※ 4Hデイトレ適性ランキングは2026-09-17 07:14 JST時点のデータ（本日分反映済み）。'
    '数値は目安であり、実際のエントリーは各自のルールで判断してください。本日は日本時間未明のFOMC通過後で、かつ20:00に英BOEの政策金利発表を控えるため、'
    '通常のトレンドフォローに加えイベント前後の値動き・スプレッド拡大に注意してください。'
)

REVIEW_TOPICS = [
    (
        'FOMCが0.25%利上げを決定、FFレートは3.75〜4.00%へ（2023年以来3年ぶり）',
        '米東部時間9/16 14:00（日本時間9/17未明3:00）のFOMCでは市場予想通り0.25%の利上げが決定され、FFレートは3.50〜3.75%から3.75〜4.00%へ引き上げられた。'
        '利上げは2023年以来3年ぶりで、声明・ウォーシュFRB議長の記者会見（3:30〜）の内容がタカ派的と受け止められた。'
    ),
    (
        '米8月小売売上高が予想を上回り3月来で最大の伸び、ドル買いが加速',
        '米8月小売売上高は予想を上回り、3月以来最大の伸びとなった。米経済の底堅さを示す内容となり、FOMC結果発表を控えたドル買いを後押しした。'
    ),
    (
        'トランプ大統領が利下げを要求、FRBの利上げ決定に対抗する姿勢',
        'トランプ大統領は「米国の金利は1％以下であるべき」と発言し、FRBの利上げ決定に対抗する姿勢を示した。今後のFRB運営に対する政治的圧力として市場でも意識されている。'
    ),
    (
        'ドル円は153円台のもみ合いからFOMC後に156円台まで続伸',
        '9/16の東京市場はFOMC結果待ちで153円台のもみ合いに終始したが、米小売売上高の上振れとFOMCの0.25%利上げ・タカ派的な声明を受けてドル買いが加速し、'
        'ドル円は日本時間9/17未明に一時156.14円まで値を伸ばした。'
    ),
]

REVIEW_HANDOVER = (
    '本日（9/17木）への引継ぎ：9/16（火）はFOMC結果待ちで東京市場は153円台のもみ合いだったが、米小売売上高の上振れを受けてドル買いが先行。'
    '米東部時間9/16 14:00（日本時間9/17未明3:00）のFOMCでは市場予想通り0.25%の利上げが決定されFFレートは3.75〜4.00%へ（2023年以来3年ぶり）、'
    '声明・会見がタカ派的と受け止められドル全面高が加速し、ドル円は一時156.14円まで続伸した。トランプ大統領はFRBに利下げを求める発言を行っている。'
    '本日9/17（木）は20:00の英BOE政策金利発表（3.75%据え置き予想）、21:30の米新規失業保険申請件数・住宅着工件数・建設許可件数・フィラデルフィア連銀景況指数など'
    '米重要指標が集中するため、FOMC後のドル高の持続性を確認しつつ、BOE前後のポンドの振れやすさにも注意したい。'
)

# (time, country_flag_label, name, importance, forecast, previous)
CAL_ROWS = [
    ('翌朝03:00（発表済み）', '🇺🇸 米', 'FOMC政策金利・声明発表（KissFX・ForexFactory一致）', '最高', True, '25bp利上げ／3.75〜4.00%', '3.50〜3.75%'),
    ('翌朝03:00（発表済み）', '🇺🇸 米', 'FOMCメンバー経済見通し(SEP)（ForexFactoryのみ・要確認）', '最高', True, '—', '—'),
    ('翌朝03:30（発表済み）', '🇺🇸 米', 'ウォーシュFRB議長 記者会見（ForexFactoryのみ・要確認）', '最高', True, '要人発言', '—'),
    ('翌朝05:00（発表済み）', '🇺🇸 米', '対米証券投資【ネット長期フロー】（ForexFactoryのみ・要確認）', '低', True, '1463億ドル', '1727億ドル'),
    ('07:45', '🇳🇿 NZ', '第2四半期GDP【前期比】（KissFX・ForexFactory一致）', '高', False, '+0.1%', '+0.8%'),
    ('07:45', '🇳🇿 NZ', '第2四半期GDP【前年比】（KissFXのみ・要確認）', '高', False, '+2.2%', '+1.5%'),
    ('15:00', '🇨🇭 スイス', '貿易収支（KissFXのみ・要確認）', '低', False, '—', '+81.4億'),
    ('16:00', '🇨🇭 スイス', 'SECO経済見通し（ForexFactoryのみ・要確認）', '低', False, '—', '—'),
    ('18:00', '🇪🇺 欧', '消費者物価指数【改定値・前月比】（KissFXのみ・要確認）', '低', False, '+0.4%', '+0.4%'),
    ('18:00', '🇪🇺 欧', '消費者物価指数【改定値・前年比】（KissFX・ForexFactory一致）', '低', False, '+3.3%', '+3.3%'),
    ('18:00', '🇪🇺 欧', '消費者物価指数【改定値・コア】（KissFX・ForexFactory一致）', '低', False, '+2.4%', '+2.4%'),
    ('18:03', '🇪🇺 欧', 'スペイン10年債入札（ForexFactoryのみ・要確認）', '低', False, '—', '3.74%／応札倍率2.3倍'),
    ('20:00', '🇬🇧 英', 'BOE政策金利＆声明発表（KissFX・ForexFactory一致）', '最高', False, '3.75%据え置き', '3.75%'),
    ('20:00', '🇬🇧 英', 'BOE議事録公表（KissFXのみ・要確認）', '最高', False, '—', '—'),
    ('20:00', '🇬🇧 英', 'MPC政策金利 票内訳（ForexFactoryのみ・要確認）', '高', False, '据え置き3-利下げ0-利上げ6', '据え置き3-利下げ0-利上げ6'),
    ('21:30', '🇨🇦 加', '鉱工業製品価格【前月比】（KissFX・ForexFactory一致）', '中', False, '±0.0%', '+0.6%'),
    ('21:30', '🇨🇦 加', '原料価格指数【前月比】（KissFX・ForexFactory一致・予想値微差・要確認）', '中', False, '+0.8%(Kiss)/+0.7%(FF)', '-2.2%'),
    ('21:30', '🇨🇦 加', '対内証券投資（KissFX・ForexFactory一致）', '低', False, '28.64億ドル(FF)', '408.3億(Kiss)/40.83億ドル(FF)'),
    ('21:30', '🇺🇸 米', '新規失業保険申請件数（KissFX・ForexFactory一致）', '高', False, '20.7万件', '20.6万件'),
    ('21:30', '🇺🇸 米', '住宅着工件数（KissFX・ForexFactory一致）', '高', False, '131.9万件(Kiss)/132万件(FF)', '123.9万件(Kiss)/124万件(FF)'),
    ('21:30', '🇺🇸 米', '建設許可件数（KissFX・ForexFactory一致）', '高', False, '141.0万件(Kiss)/140万件(FF)', '144.3万件(Kiss)/144万件(FF)'),
    ('21:30', '🇺🇸 米', 'フィラデルフィア連銀景況指数（KissFX・ForexFactory一致・予想値微差・要確認）', '高', False, '+32.5(Kiss)/+31.3(FF)', '+47.4'),
    ('23:00', '🇺🇸 米', '中古住宅販売保留【前月比】（KissFX・ForexFactory一致・予想値微差・要確認）', '低', False, '-0.1%(Kiss)/-0.2%(FF)', '-2.3%'),
    ('23:00', '🇺🇸 米', '中古住宅販売保留【前年比】（KissFXのみ・要確認）', '低', False, '-5.0%', '-2.5%'),
    ('23:30', '🇦🇺 豪', 'CB景気先行指数（ForexFactoryのみ・要確認）', '低', False, '—', '+0.3%'),
    ('23:30', '🇺🇸 米', '週間天然ガス貯蔵量（KissFX・ForexFactory一致）', '低', False, '49B(FF)', '+40(Kiss)/40B(FF)'),
    ('26:00', '🇺🇸 米', '10年インフレ連動債(TIPS)入札（KissFXのみ・要確認）', '高', False, '190億ドル', '—'),
]

def cal_row_html(time, country, name, importance, done, forecast, previous):
    badge = ' <span class="badge-important">★重要</span>' if importance == '最高' else ''
    time_cell = f'<strong>{time}</strong>' if importance == '最高' else time
    name_cell = f'<strong>{name}</strong>{badge}' if importance == '最高' else name
    return f'<tr><td>{time_cell}</td><td>{country}</td><td>{name_cell}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'

CAL_ROWS_HTML = '\n            '.join(cal_row_html(*row) for row in CAL_ROWS)

POINTS_KEY_EVENTS_HTML = '\n'.join(f'              <li>{item}</li>' for item in POINTS_KEY_EVENTS)
POINTS_OTHER_HTML = '\n'.join(
    f'              <li><strong>{title}</strong>：{body}</li>' for title, body in POINTS_OTHER
)
REVIEW_TOPICS_HTML = '\n'.join(
    f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(REVIEW_TOPICS)
)
RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge rank-{rank.lower()}">{rank}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, desc, trend_class, arrow in RANKING_ROWS)

archive_items = SIDEBAR_ARCHIVE

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
  <p>{HERO_P}</p>
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
{archive_items}      </ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 {TODAY}（{WEEKDAY}）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_P}</p>
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
        <h3>{SUMMARY_H3}</h3>
        <p>{SUMMARY_P}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>{TOP_CURRENCY_P}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red)">HIGH</h3>
        <p>{RISK_P}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_INDICATOR_COUNT}</h3>
        <p>{KEY_INDICATOR_SUB}</p>
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
              <li>{POINTS_HOLIDAY[0]}</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
{POINTS_KEY_EVENTS_HTML}
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
{POINTS_OTHER_HTML}
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
          {MARKET_ENV_P}
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
          <h3>📰 前日の相場振り返り（{PREV_DATE}）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{REVIEW_TOPICS_HTML}
          <div class="handover">
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
            {CAL_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き、https://kissfx.com/article/fxdays20260917.html）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。FOMC関連イベント（政策金利・SEP・記者会見・対米証券投資）は日本時間9/17未明にすでに発表済みのため「発表済み」と注記しています。本日は主要国の市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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
