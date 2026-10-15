# -*- coding: utf-8 -*-
"""FX日報 2026-10-16（金）生成スクリプト"""
import glob, os

TODAY = '2026-10-16'
WEEKDAY = '金'

HERO_TITLE_SUB = (
    '前営業日10/15（木）はドル円が米PPIの上振れ後に157円55銭まで下げたが買い戻され、158円00銭で引けた。'
    '本日10/16（金）は休場なしで、12:30のウォーシュFRB議長発言と11:00のベイリーBOE総裁発言が主要材料となる。'
)

SUMMARY_HEADLINE = (
    'ドル円は156.50〜158.50円のレンジ内で158円00銭引け、米債利回り低下でドル高は一服。'
    '本日は12:30のウォーシュFRB議長発言と週末リスクが焦点'
)

SUMMARY_BODY = (
    '10/15（木）のドル円は、米PPIが予想を上回っても反応が限定的で、157円55銭まで下げたあと158円25銭まで戻し、158円00銭で引けた（ザイFX・みんかぶ）。'
    '米小売売上高の鈍化とAI関連の信用不安で米国債が買われ、米10年債利回りは5.035％まで低下した（ザイFX）。'
    '本日10/16は休場がなく、流動性は通常どおり（ForexFactoryに休場の記載なし）。'
)

TOP_PAIR_BODY = (
    '4時間足ランキング（10/15 07:27 JST生成・本日分は未更新）ではEUR/USDが1位・候補判定（スコア59、ADX22.1、方向は下降）。'
    'ECBの10月追加利上げは見込み薄とされ（みんかぶ）、ユーロの上値は重い。'
    '12:30のウォーシュFRB議長発言と21:30の米輸入物価（前月比予想+0.9％・前回+0.7％）がドル側の変動要因となる。15分・30分足で戻り高値の切り下げを確認してからの戻り売りが基本となる。'
)

RISK_LEVEL = 'MEDIUM'
RISK_BODY = (
    '高重要度は11:00のベイリーBOE総裁発言と12:30のウォーシュFRB議長発言の2本で、米指標は21:30の輸入物価と22:15の鉱工業生産（前月比予想+0.4％・前回0.0％）と軽め。'
    '10/28のFOMCを控えた議長発言で利上げ姿勢が強まればドル買い、慎重な姿勢ならドル売りに振れる。'
    '週末を挟むため、引けにかけてポジション調整が出やすい。'
)

KEY_EVENTS_COUNT = '19件'
KEY_EVENTS_SUMMARY = (
    '英 ベイリーBOE総裁発言(11:00) / 米 ウォーシュFRB議長発言(12:30)・輸入物価(21:30)・鉱工業生産(22:15) / 加 マックレムBOC総裁発言(13:15) / 日 内田日銀副総裁(植田総裁あいさつ代読)(15:30)'
)

MARKET_OVERVIEW = (
    '10/15（木）は米PPIが予想を上回ったがドル円の反応は限定的で、157円台へ下げたあと買い戻された（みんかぶ）。'
    '米小売売上高の鈍化とAI関連の信用不安で米国債が買われ、米10年債利回りは5.035％まで低下した。一方で原油が上昇し、ダウ平均は465ドル高で引けた（ザイFX）。'
    'ドル円の1週間物オプションのボラティリティは7.1％に上昇し、リスクリバーサルでは円コールスプレッドが拡大した（みんかぶ・ザイFX）。'
    '本日は休場がなく、日本時間は11:00のベイリーBOE総裁、12:30のウォーシュFRB議長、13:15のマックレムBOC総裁の発言が続く。'
    '<br><br><strong>政策金利：</strong> 本日は金曜日のため前回更新（10/12）の値を引き継ぐ。FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（詳細は週次更新の月曜日版を参照）。'
    '<br><br><strong>今後の焦点：</strong> 次回FOMCは10/28、ECBは10/29、日銀は10/30。'
)

RANKING_ROWS = [
    (1, 'EUR/USD', 'rank-b', 'B', '直近スコア59・候補。ADX22.1、ADR比93.1％、方向は下降。ECBの10月追加利上げは見込み薄とされる（みんかぶ）。', 'trend-down', '↓'),
    (2, 'USD/CAD', 'rank-b', 'B', '直近スコア58・候補。ADX23.5、ADR比109.5％、方向はレンジ。13:15にマックレムBOC総裁発言、21:30にカナダ対外証券投資。', 'trend-range', '→'),
    (3, 'GBP/USD', 'rank-c', 'C', '直近スコア48・見送り。ADX19.6、ADR比81.1％、方向は下降。11:00のベイリーBOE総裁発言が値幅の出る場面。', 'trend-down', '↓'),
    (4, 'EUR/AUD', 'rank-c', 'C', '直近スコア47・見送り。ADX40.9、方向は下降。ADR比52.2％と値幅が5年平均の約半分。', 'trend-down', '↓'),
    (5, 'EUR/JPY', 'rank-c', 'C', '直近スコア45・見送り。ADX23.5、ADR比67.7％、方向は下降。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/15 07:27 JST生成分（本日分は未更新・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        '米PPIは予想を上回るも反応限定的、ドル円は157円55銭から158円00銭へ買い戻し',
        '米PPI（生産者物価指数）は市場予想を上回ったが、ドル円は157円台へ下げたあとに買い戻された（みんかぶ）。'
        'NY市場では157円55銭まで下落後に158円25銭まで反発し、158円00銭で引けた。前日NY終値158円33銭からは小幅なドル安（ザイFX）。',
    ),
    (
        '米小売売上高の鈍化とAI関連の信用不安で米国債が買われ、米10年債利回りは5.035％へ低下',
        '9月の米小売売上高が鈍化し、AIブームをめぐる信用不安も重なって安全資産の米国債が買われた（ザイFX）。'
        '利回り低下がドル売りを誘った一方、原油上昇でドルは下げ幅を縮めた。ダウ平均は465ドル高で終えた。',
    ),
    (
        'ドル円オプションで円コール買いが加速、1週間物ボラティリティは7.1％に上昇',
        'ドル円の1週間物オプションのボラティリティは7.1％に上昇し、リスクリバーサルでは円コールスプレッドが拡大した。'
        'レンジの上抜けと下値のヘッジの双方に備える買いが強まっている（みんかぶ・ザイFX）。'
        'ザイFXはドル円が156.50〜158.50円のレンジで推移すると見ている。',
    ),
    (
        'ECBの10月追加利上げは見込み薄、英月次GDPは予想外のプラスもポンドの反応は限定的',
        'ECBの10月会合での追加利上げは見込み薄とされた。英国の月次GDPは予想外のプラス成長となったが、ポンドの反応は限定的だった（みんかぶ。10/16付の記事で10/15 NY時間の内容・要確認）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/16金）への引継ぎ：ドル円は158円00銭で前営業日を終えた。'
    '本日は休場がなく、12:30のウォーシュFRB議長発言が最大の材料。'
    '日中は11:00のベイリーBOE総裁発言と15:30の内田日銀副総裁（植田総裁あいさつ代読）が円とポンドの方向を決める。'
    '156.50〜158.50円のレンジの上限158円台半ばと下限156円台後半が目安で、抜けた場合は円コール買いの動きもあり値幅が拡大する。'
)

POINTS_EVENTS = [
    '11:00 🇬🇧 英国 ベイリーBOE総裁 発言（FF・外部ブログ一致。単独Kiss照合不可・要確認）',
    '12:30 🇺🇸 米国 ウォーシュFRB議長 発言（FF・外部ブログ一致。要確認）',
    '13:15 🇨🇦 カナダ マックレムBOC総裁 発言（FF・外部ブログ一致。要確認）',
    '15:30 🇯🇵 日本 内田日銀副総裁 あいさつ（植田総裁のあいさつを代読。ザイFX・外部ブログのみ、FFに記載なし・要確認）',
    '21:30 🇺🇸 米国 輸入物価指数（前月比予想+0.9％・前回+0.7％。FF・外部ブログ一致。要確認）',
    '22:15 🇺🇸 米国 鉱工業生産（前月比予想+0.4％・前回0.0％。FF・外部ブログ一致。要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：12:30のウォーシュFRB議長発言が分岐点',
        'ドル円は10/15に157円55銭〜158円25銭で推移し158円00銭で引けた。10/28のFOMCを控え、議長が追加利上げに前向きな内容を示せば米金利上昇でドル買いが優勢になり158円台半ばへ戻る。'
        '利回り低下が続く慎重な内容なら157円台前半を試す（ザイFX・みんかぶ）。'
        '15:30の内田日銀副総裁の代読あいさつで追加利上げに前向きな内容が出れば円買いが入る。',
    ),
    (
        'ポンド：11:00のベイリーBOE総裁発言',
        'BOEは9/17に3対6の分裂投票で政策金利を3.75％に据え置いた。総裁が追加利上げに前向きならポンド買い、慎重ならポンド売りになる。英月次GDPが予想外のプラスでもポンドの反応は限定的だった（みんかぶ）。次回BOE会合は11/5。',
    ),
    (
        'ユーロ：ECBの10月追加利上げは見込み薄',
        'みんかぶはECBの10月追加利上げは見込み薄と伝えている。18:00にユーロ圏の確定値CPI（予想+3.8％・前回+3.8％）が出る。予想どおりなら材料に乏しく、予想を上回ればECBの利上げ観測が戻りユーロ買いになる。',
    ),
    (
        'カナダドル：13:15のマックレムBOC総裁発言',
        'BOCは政策金利2.25％を据え置いている。10/9の雇用統計が予想外の減少だったため、総裁が景気減速に言及すればカナダドル売り、物価警戒を示せばカナダドル買いになる。次回BOC会合は10/28。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('01:00', '🇺🇸 米', '原油在庫（FFのみ・発表済み・要確認）', '低', '+0.2M', '-3.2M'),
    ('05:30', '🇺🇸 米', 'ハマック・クリーブランド連銀総裁 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('06:30', '🇳🇿 NZ', 'ビジネスNZ製造業指数（FFのみ・要確認）', '低', '—', '53.1'),
    ('06:45', '🇳🇿 NZ', '食品価格指数 [前月比]（FFのみ・要確認）', '低', '—', '+0.3%'),
    ('08:50', '🇯🇵 日', '対外・対内証券投資（ザイFXのみ・要確認）', '低', '—', '—'),
    ('10:10', '🇯🇵 日', '日銀 国債買い入れオペ（ザイFXのみ・要確認）', '低', '—', '—'),
    ('11:00', '🇬🇧 英', 'ベイリーBOE総裁 発言（FF・外部ブログ一致・要確認）', '高', '要人発言', '—'),
    ('11:30', '🇩🇪 独', 'ナーゲル独連銀総裁 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('12:30', '🇺🇸 米', 'ウォーシュFRB議長 発言（FF・外部ブログ一致・要確認）', '高', '要人発言', '—'),
    ('13:15', '🇨🇦 加', 'マックレムBOC総裁 発言（FF・外部ブログ一致・要確認）', '中', '要人発言', '—'),
    ('15:30', '🇯🇵 日', '内田日銀副総裁 あいさつ（植田総裁の代読。ザイFX・外部ブログのみ・要確認）', '中', '要人発言', '—'),
    ('18:00', '🇪🇺 欧', '確定値CPI [前年比]（FFのみ・要確認）', '低', '+3.8%', '+3.8%'),
    ('18:00', '🇪🇺 欧', '確定値コアCPI [前年比]（FFのみ・要確認）', '低', '+2.5%', '+2.5%'),
    ('18:00', '🇪🇺 欧', '貿易収支（FFのみ・要確認）', '低', '+45億', '+50億'),
    ('19:00', '🇮🇹 伊', '貿易収支（FFのみ・要確認）', '低', '+75.0億', '+82.4億'),
    ('21:00', '🇨🇦 加', 'アレクソポウロスBOC政策委員 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('21:15', '🇨🇦 加', '住宅着工件数（FFのみ・要確認）', '低', '23.4万件', '22.9万件'),
    ('21:30', '🇨🇦 加', '対外証券投資（FFのみ・要確認）', '低', '235.9億', '206.5億'),
    ('21:30', '🇺🇸 米', '輸入物価指数 [前月比]（FF・外部ブログ一致・要確認）', '低', '+0.9%', '+0.7%'),
    ('22:15', '🇺🇸 米', '設備稼働率（FFのみ・要確認）', '低', '76.5%', '76.3%'),
    ('22:15', '🇺🇸 米', '鉱工業生産 [前月比]（FF・外部ブログ一致・要確認）', '低', '+0.4%', '0.0%'),
    ('23:15', '🌐 全', 'IMF会合（FFのみ・要確認）', '低', '—', '—'),
]
CAL_ROWS.sort(key=lambda r: r[0])

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
        <em>金曜日</em>
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
        <h3>EUR/USD 🇪🇺🇺🇸</h3>
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
              <li>休場なし（日本・米国・カナダ・欧州とも通常営業。ForexFactoryに本日の休場の記載なし。KissFXは取得不可のため要確認）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-15）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。本日はKissFXが取得できなかったため（別内容のページが返却）、ForexFactory JSONを主ソースとし、外部ブログ・ザイFXで照合できた項目も含め全件「（要確認）」を付記。重要度はForexFactory区分。</p>
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
