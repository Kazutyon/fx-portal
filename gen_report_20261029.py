# -*- coding: utf-8 -*-
"""FX日報 2026-10-29（木）生成スクリプト"""
import glob, os

TODAY = '2026-10-29'
WEEKDAY = '木'

HERO_TITLE_SUB = (
    '前営業日10/28（水）のドル円は、FOMCの据え置きとウォーシュFRB議長の会見で158.35円まで上昇後に反落し、NY終値157.84円と4営業日ぶりに小反落した。'
    '本日10/29（木）は22:15のECB政策金利と21:30の米PCE・GDPが重なる。'
)

SUMMARY_HEADLINE = (
    'FOMC後にドル円は158.35円から157.84円へ反落。'
    '本日はECB政策金利と米PCE・GDPが同時に控える'
)

SUMMARY_BODY = (
    '10/28のFOMCは政策金利を3.75〜4.00％に据え置き、2名が利上げを支持した（ザイFX）。'
    '会見直後のドル円は158.35円まで上昇したが、米10年債利回りの低下で157.88円付近まで反落し、NY終値は157.84円（前日比11銭安）だった（ザイFX）。'
    '本日は主要市場の休場なし（KissFX・ForexFactoryで確認）。'
)

TOP_PAIR_BODY = (
    'ドル円は158円台前半で上値が重く、NY終値は157.84円。'
    '21:30の米PCEコアデフレーター（予想前月比+0.3%・前回+0.2%）と第3四半期GDP速報値（予想+3.2%・前回+2.2%）で米金利の方向が決まる（KissFX・ForexFactory）。'
    '4時間足ランキング（10/28 08:01 JST生成・本日分は未更新）ではEUR/JPYが1位、USD/JPYが2位、GBP/JPYが3位。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    '22:15のECB政策金利（予想2.65%据え置き）と22:45のラガルド総裁会見、21:30の米PCE・GDP速報値が同じ夜に重なる（KissFX・ForexFactory）。'
    '米株引け後にはアマゾンの決算がある（KissFX）。翌10/30は日銀会合と植田総裁の会見が控える。'
)

KEY_EVENTS_COUNT = '5件'
KEY_EVENTS_SUMMARY = (
    '21:30 米個人所得・支出・PCEコアデフレーター、21:30 米第3四半期GDP速報値、21:30 米新規失業保険申請件数、'
    '22:15 ECB政策金利（予想2.65%据え置き）、22:45 ラガルドECB総裁会見'
)

MARKET_OVERVIEW = (
    '<strong>FOMC（10/28 NY）</strong>：政策金利を3.75〜4.00％に据え置き、2名が利上げを支持し、経済活動の判断は上方修正された。声明は地政学リスクで不透明感が強まったと指摘した（ザイFX）。市場では12月の利上げを織り込んだドル買いが見られたと報じられた（ザイFX）。'
    '<br><strong>為替終値</strong>：ドル円157.84円、ユーロ円176.05円、ユーロドル1.1154ドル（ザイFX）。KissFXはFOMCとウォーシュ議長会見を受けてドル売りが強まり、ユーロドルは1.11ドル半ばまで反発したと伝える。'
    '<br><strong>VIX・金・原油・米10年債利回り</strong>：Investing.comは月曜のみ取得する運用のため本日は未取得（要確認）。'
    '<br><br><strong>政策金利：</strong> 木曜日のため公式な再確認は行わず、10/26付の日報（月曜更新分）の値を引き継ぐ。FRBは10/28のFOMC据え置きで3.75〜4.00％を確認。日銀 1.25％、ECB 預金金利2.50％（主要リファイナンス金利2.65％）、BOE 3.75％、RBA 4.60％、SNB 0.00％。RBNZ 2.75％とBOC 2.25％は10/28会合の結果を確認できていない（要確認）。'
    '<br><br><strong>本日の中銀イベント：</strong> ECB（22:15、予想2.65%据え置き）。翌10/30に日銀会合。'
)

RANKING_ROWS = [
    (1, 'EUR/JPY', 'rank-a', 'A', '10/28 08:01生成のスコア71・適。ADX39.7、方向は下降。10/28NY終値176.05円（ザイFX）。22:15のECBが材料。本日分のランキングは未更新。', 'trend-down', '↓'),
    (2, 'USD/JPY', 'rank-c', 'C', '10/28 08:01生成のスコア63・候補。ADX34.1、方向はレンジ。157.84円で引け、21:30の米PCE・GDPが材料。', 'trend-range', '→'),
    (3, 'GBP/JPY', 'rank-c', 'C', '10/28 08:01生成のスコア61・候補。ADX35.4、方向はレンジ。18:30の英住宅ローン承認件数が材料（予想54K）。', 'trend-range', '→'),
    (4, 'AUD/JPY', 'rank-c', 'C', '10/28 08:01生成のスコア55・候補。ADX21.5、方向は上昇。9:30の豪輸入物価指数（予想+1.3%、前回+5.7%）が材料。', 'trend-up', '↑'),
    (5, 'USD/CAD', 'rank-c', 'C', '10/28 08:01生成のスコア45・見送り。ADX26.4、方向はレンジ。21:30の米GDPとBOC会合後の動きが材料。', 'trend-range', '→'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/28 08:01 JST生成分で、本日（10/29）分は未取得のため旧データを表示している（要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'FOMCは3.75〜4.00％で据え置き、2名が利上げを支持',
        'FOMCは政策金利を市場予想どおり3.75〜4.00％に据え置いた。2名が利上げを支持し、経済活動の判断は上方修正された。声明は地政学リスクの展開で不透明感が強まったと指摘した（ザイFX）。利上げ票が出たため、据え置きでも金融引き締め観測が残りドルの下支えになった。',
    ),
    (
        'ウォーシュ議長会見直後にドル円は158.35円へ上昇後、157.88円へ反落',
        '会見直後のドル円は158.35円まで上昇したが、米10年債利回りの低下に合わせて157.88円付近まで下げた（ザイFX）。市場では12月の利上げを織り込んだドル買いが見られたと報じられた（ザイFX）。KissFXはFOMCと会見を受けてドル売りが強まったと伝えており、会見後の方向感は報道間で相違する（要確認）。',
    ),
    (
        'NY終値は157.84円、4営業日ぶりの小反落',
        'ドル円のNY終値は157.84円で前日比11銭安、4営業日ぶりに小反落した。ユーロ円は176.05円、ユーロドルは1.1154ドルで引けた（ザイFX）。ザイFXは株高・原油高の中でもドルが失速したと報じ、別の記事では月末のドル買いフローの可能性を指摘している。',
    ),
    (
        '原油高とドル買いの背景に米軍事作戦への警戒（要確認）',
        'ザイFXは、米国が中間選挙後に短期集中型の軍事作戦を行う可能性への警戒から原油が買われ、金利上昇とドル買いにつながったと報じた。単一ソースの報道であり、事実関係は確認できていない（要確認）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/29木）への引継ぎ：ドル円は157.84円、ユーロ円は176.05円でFOMC後の水曜を終えた。'
    '本日は21:30の米PCE・GDP速報値、22:15のECB政策金利（予想2.65%据え置き）が重なり、米インフレ指標の結果がFOMC後の米金利とドル円の方向を決める。'
)

POINTS_EVENTS = [
    '21:30 🇺🇸 米 新規失業保険申請件数（Kiss/FF一致。予想19.8万件、前回19.4万件）',
    '21:30 🇺🇸 米 個人所得・個人支出（Kiss/FF一致。所得予想+0.3%、支出予想+0.6%）',
    '21:30 🇺🇸 米 PCEコアデフレーター 前月比（Kiss/FF一致。予想+0.3%、前回+0.2%）',
    '21:30 🇺🇸 米 第3四半期GDP速報値（Kiss/FF一致。予想+3.2%、前回+2.2%／FFの前回は+1.5%で相違・要確認）',
    '22:15 🇪🇺 欧 ECB政策金利・声明（Kiss/FF一致。予想2.65%据え置き）',
    '22:45 🇪🇺 欧 ラガルドECB総裁 記者会見（Kiss/FF一致）',
    '米株引け後 🇺🇸 米 アマゾン決算（KissFXのみ・要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：FOMC後の157.84円、21:30のPCE・GDPが方向を決める',
        'ドル円はFOMC後に158.35円から157.84円へ反落した（ザイFX）。PCEコアデフレーターが予想の前月比+0.3%を上回れば米金利が上昇してドル買いが続き、158円台を試す。下回れば利上げ観測が後退し、157円台前半までの調整が入る。',
    ),
    (
        'ユーロ：22:15のECBは2.65%据え置きが予想',
        'ECB主要リファイナンス金利の予想は2.65%据え置きで、前回も2.65%（Kiss/FF一致）。9/10に利上げ済みのため、22:45のラガルド総裁会見で追加利上げの示唆があるかがユーロ円（176.05円）とユーロドル（1.1154ドル）の方向を決める。',
    ),
    (
        'ポンド：18:30の英住宅指標は低位',
        '英住宅ローン承認件数は予想54K（前回55K、FFのみ・要確認。KissFXは前回54.9千件で相違）。ポンドへの影響は限定的で、21:30の米指標後のドル動向が主因になる。',
    ),
    (
        '豪ドル・NZドル：朝の豪輸入物価とNZ企業景況感',
        '09:00のNZ ANZ企業景況感（前回51.9）、09:30の豪第3四半期輸入物価指数（FF予想+1.3%・前回+5.7%）が朝の材料。いずれも重要度は低い。',
    ),
    (
        '休場：なし',
        'KissFXとForexFactoryのいずれにも本日の主要市場の休場情報はない。',
    ),
    (
        '今週のイベント：10/30 日銀、東京都区部CPI',
        '10/30に日銀会合と植田総裁の会見、東京都区部CPIがある（KissFX）。本日のECBと米PCEの結果が、日銀を前にしたドル円とユーロ円の方向に影響する。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('03:00', '🇺🇸 米', 'FOMC政策金利・声明（発表済み：3.75〜4.00%据え置き）', '高', '4.00%', '4.00%'),
    ('03:30', '🇺🇸 米', 'ウォーシュFRB議長 記者会見（発表済み）', '高', '—', '—'),
    ('09:00', '🇳🇿 NZ', 'ANZ企業景況感（Kiss/FF一致）', '低', '—', '51.9'),
    ('09:30', '🇦🇺 豪', '第3四半期輸入物価指数（Kiss/FF一致）', '低', '+1.3%（FF）', '+5.7%'),
    ('09:30', '🇦🇺 豪', '第3四半期輸出物価指数（Kissのみ・要確認）', '低', '—', '+1.1%'),
    ('14:00', '🇯🇵 日', '消費者態度指数（FFのみ・要確認）', '低', '35.1', '35.4'),
    ('18:00', '🇮🇹 伊', '月次失業率（FFのみ・要確認）', '低', '6.2%', '6.2%'),
    ('18:30', '🇬🇧 英', '住宅ローン承認件数（前回値が相違・要確認）', '低', '54.0K', 'Kiss54.9K／FF55K'),
    ('18:30', '🇬🇧 英', '個人向け純貸出（FF）／消費者信用残高（Kiss）（数値が相違・要確認）', '低', 'Kiss+20億／FF+62億', 'Kiss+25億／FF+69億'),
    ('18:30', '🇬🇧 英', 'マネーサプライM4 前月比（予想値が相違・要確認）', '低', 'FF+0.3%', '+0.4%'),
    ('18:33', '🇮🇹 伊', '10年債入札（FFのみ・要確認）', '低', '—', '—'),
    ('21:30', '🇺🇸 米', '新規失業保険申請件数（Kiss/FF一致）', '中', '19.8万件', '19.4万件'),
    ('21:30', '🇺🇸 米', '個人所得 前月比（Kiss/FF一致）', '低', '+0.3%', '+0.2%'),
    ('21:30', '🇺🇸 米', '個人支出 前月比（Kiss/FF一致）', '低', '+0.6%', '+0.9%'),
    ('21:30', '🇺🇸 米', 'PCEコアデフレーター 前月比（Kiss/FF一致）', '高', '+0.3%', '+0.2%'),
    ('21:30', '🇺🇸 米', '第3四半期GDP速報値（前回値が相違・要確認）', '高', '+3.2%', 'Kiss+2.2%／FF+1.5%'),
    ('21:30', '🇺🇸 米', 'GDP価格指数 速報値（前回値が相違・要確認）', '中', '+3.2%', 'Kiss+6.1%／FF+6.2%'),
    ('21:50', '🇨🇦 加', 'グレーヴェルBOC理事 発言（FFのみ・要確認）', '低', '—', '—'),
    ('22:15', '🇪🇺 欧', 'ECB政策金利・声明（Kiss/FF一致）', '高', '2.65%', '2.65%'),
    ('22:45', '🇪🇺 欧', 'ラガルドECB総裁 記者会見（Kiss/FF一致）', '高', '—', '—'),
    ('23:30', '🇺🇸 米', '週間天然ガス貯蔵量（予想値が相違・要確認）', '低', 'FF+75B', '77'),
    ('26:00', '🇺🇸 米', '7年債入札（Kissのみ・要確認）', '低', '440億ドル', '—'),
    ('26:30', '🇨🇭 スイス', 'テュディンSNB理事 発言（Kissのみ・要確認）', '低', '—', '—'),
    ('29:00', '🇺🇸 米', 'アマゾン決算（米株引け後・Kissのみ・要確認）', '中', '—', '—'),
]
CAL_ROWS.sort(key=lambda r: (int(r[0][:2]), r[0]))

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
              <li>なし（KissFX・ForexFactoryとも休場情報なし）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-28 水）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はForexFactory区分（KissFXのみの項目は要確認）。</p>
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
