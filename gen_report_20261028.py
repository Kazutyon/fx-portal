# -*- coding: utf-8 -*-
"""FX日報 2026-10-28（水）生成スクリプト"""
import glob, os

TODAY = '2026-10-28'
WEEKDAY = '水'

HERO_TITLE_SUB = (
    '前営業日10/27（火）のドル円はNY終値157.95円で、前日の157.50円から45銭上昇し3日続伸した。'
    '本日10/28（水）は主要市場の休場がなく、10:00のRBNZ、22:45のBOC、10/29 03:00のFOMCと政策発表が3つ重なる。'
)

SUMMARY_HEADLINE = (
    '米CB消費者信頼感指数の上振れでドル円は157.95円まで続伸。'
    '本日はRBNZ・BOC・FOMCの3中銀が政策を発表する'
)

SUMMARY_BODY = (
    '10/27（火）のドル円は157.67〜157.96円のNY値幅で推移し、157.95円で引けた（ザイFX）。'
    '米CB消費者信頼感指数が91.7（前回84.2）と市場予想を上回り、4カ月ぶりの上昇となったことがドル買いを支えた（ザイFX）。'
    'ドル指数は15日以来の高水準、ユーロドルは14日以来の安値水準まで動いた（みんかぶ）。'
    '本日は主要市場の休場なし（KissFX・ForexFactoryで確認）。'
)

TOP_PAIR_BODY = (
    'ドル円は10/27のNY引けで157.95円と3日続伸し、10/28早朝のEUR/JPYは175.74円（ザイFX）。'
    '10/29 03:00のFOMC（政策金利の予想4.00%据え置き、KissFX・ForexFactory一致）で米金利の方向が決まり、ドル円の値幅が拡大する。'
    '4時間足ランキング（10/27 08:13 JST生成・本日分は未更新）ではEUR/JPYが1位、AUD/JPYが2位、USD/JPYが3位。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'FOMC（10/29 03:00）、RBNZ（10:00）、BOC（22:45）の政策発表が1日に集中し、ウォーシュFRB議長の記者会見が10/29 03:30に控える（KissFX・ForexFactory）。'
    '米株引け後にはアルファベットとマイクロソフトの決算があり、AI投資への不安がリスクセンチメントを左右する（KissFX）。'
    '10/29にECB、10/30に日銀と中銀会合が続く。'
)

KEY_EVENTS_COUNT = '6件'
KEY_EVENTS_SUMMARY = (
    '09:30 豪CPI、10:00 RBNZ政策金利（予想3.00%）、22:45 BOC政策金利（予想が2.25%と2.50%で割れる）、'
    '27:00（10/29 03:00）FOMC政策金利（予想4.00%据え置き）、27:30 ウォーシュFRB議長会見、米株引け後 アルファベット・マイクロソフト決算'
)

MARKET_OVERVIEW = (
    '<strong>米債（10/27 NY）</strong>：5年債入札（700億ドル）は最高落札利回り4.845%、テイル+0.4bp、応札倍率2.33倍で、過去6回平均の2.31倍を上回った（ザイFX）。'
    '<br><strong>ドル指数・ユーロドル</strong>：ドル指数は15日以来の高水準、ユーロドルは14日以来の安値水準（みんかぶ）。ポンドドルは1.33台前半で推移した（みんかぶ）。'
    '<br><strong>オプション市場</strong>：レンジ取引が中心でオプション売りが優勢。ほとんどの期間で円プットの需要が円コールを上回った（1年物を除く、ザイFX）。'
    '<br><strong>VIX・金・原油・米10年債利回り</strong>：Investing.comは月曜のみ取得する運用のため本日は未取得（要確認）。'
    '<br><br><strong>政策金利：</strong> 水曜日のため公式な再確認は行わず、10/26付の日報（月曜更新分）の値を引き継ぐ。FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％。'
    '<br><br><strong>本日の中銀イベント：</strong> RBNZ（10:00、予想3.00%への25bp利上げ）、BOC（22:45、予想は2.25%据え置きと2.50%利上げで割れる）、FOMC（10/29 03:00、予想4.00%据え置き）。'
)

RANKING_ROWS = [
    (1, 'EUR/JPY', 'rank-a', 'A', '10/27 08:13生成のスコア74・適。ADX41.3、方向は下降。10/28早朝は175.74円（ザイFX）。本日分のランキングは未更新。', 'trend-down', '↓'),
    (2, 'AUD/JPY', 'rank-a', 'A', '10/27 08:13生成のスコア67・適。ADX28.6、方向は上昇。9:30の豪CPI（予想+4.2%、前回+4.0%）が値動きの起点になる。', 'trend-up', '↑'),
    (3, 'USD/JPY', 'rank-c', 'C', '10/27 08:13生成のスコア62・候補。ADX41.8、方向はレンジ。157.95円で引け、FOMCが方向を決める。', 'trend-range', '→'),
    (4, 'USD/CAD', 'rank-c', 'C', '10/27 08:13生成のスコア62・候補。ADX37.2、方向は下降。22:45のBOC政策金利が材料。', 'trend-down', '↓'),
    (5, 'GBP/JPY', 'rank-c', 'C', '10/27 08:13生成のスコア57・候補。ADX35.9、方向はレンジ。21:30の英予算案発表（ForexFactoryのみ・要確認）が材料。', 'trend-range', '→'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/27 08:13 JST生成分で、本日（10/28）分は未取得のため旧データを表示している（要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'ドル円は米CB消費者信頼感指数の上振れで157.95円へ3日続伸',
        'NY終値は157.95円で、前営業日の157.50円から45銭のドル高（ザイFX）。米CB消費者信頼感指数は91.7（前回84.2）と予想を上回り、6月以来の高水準、4カ月ぶりの上昇となった（ザイFX）。'
        'ザイFXは耐久財受注・新築住宅販売も予想を上回ったと報じる一方、みんかぶは耐久財受注が予想を下回りドルへの影響は限定的と報じており、耐久財受注の評価は報道間で相違する（要確認）。',
    ),
    (
        'ドル指数は15日以来の高値、ユーロドルは14日以来の安値水準',
        'ドル指数は15日以来の高水準まで上昇し、ユーロドルは14日以来の安値水準に下げた（みんかぶ）。ドル買いの背景は米消費者信頼感の改善と、10/29のFOMCを前にした米金利の上昇である。',
    ),
    (
        '米5年債入札は最高落札利回り4.845%、需要は平均を上回る',
        '700億ドルの米5年債入札は最高落札利回り4.845%、テイル+0.4bp、応札倍率2.33倍で、過去6回平均の2.31倍を上回った（ザイFX）。前日の2年債入札（応札倍率2.59倍）と合わせ、米金利は高止まりした。',
    ),
    (
        '日米の金融政策を見極める展開、オプションはレンジ想定',
        'NY序盤のドル円は157円台後半で、日米の金融政策を見極める展開となった（みんかぶ）。オプション市場ではレンジ取引が中心でオプション売りが優勢、ほとんどの期間で円プット需要が円コールを上回った（1年物を除く、ザイFX）。'
        'ロンドン時間には上げが一服し、午前のみんかぶは朝方にAI関連株の買い戻しで円高が一服したと伝えた。',
    ),
    (
        'カナダ中銀は見方が割れ、英予算案はポンドの試金石に',
        'みんかぶは10/28 01:38付でBOCの政策判断は見方が割れていると報じた。KissFXの予想も2.25%据え置きと2.50%利上げで拮抗している。'
        '英予算案は緊縮財政でポンドが年内1.30ドルまで下落するとの予想が報じられた（みんかぶ・10/28 02:08付）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/28水）への引継ぎ：ドル円は157.95円、米5年債入札の最高落札利回りは4.845%で火曜を終えた。'
    '本日は10:00のRBNZ（予想3.00%）、22:45のBOC（予想割れ）、10/29 03:00のFOMC（予想4.00%据え置き）が重なり、FOMC後の米金利がドル円の方向を決める。'
)

POINTS_EVENTS = [
    '09:30 🇦🇺 豪 消費者物価指数 前年比（Kiss/FF一致。予想+4.2%、前回+4.0%）',
    '10:00 🇳🇿 NZ RBNZ政策金利（Kiss/FF一致。予想3.00%＝25bp利上げ、前回2.75%）',
    '11:00 🇳🇿 NZ ブレマンRBNZ総裁 記者会見（Kiss/FF一致）',
    '22:45 🇨🇦 加 BOC政策金利（Kiss予想は2.25%と2.50%で拮抗／FF予想2.50%、前回2.25%・要確認）',
    '27:00（10/29 03:00）🇺🇸 米 FOMC政策金利（Kiss/FF一致。予想4.00%据え置き、前回4.00%）',
    '27:30（10/29 03:30）🇺🇸 米 ウォーシュFRB議長 記者会見（Kiss/FF一致）',
    '米株引け後 🇺🇸 米 アルファベット・マイクロソフト決算（KissFXのみ・要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：FOMCを前に157.95円の高値圏',
        'ドル円は米CB消費者信頼感指数の上振れで157.95円まで3日続伸した（ザイFX）。10/29 03:00のFOMCが予想の4.00%据え置きなら米金利は高止まりしてドル買いが続き、ウォーシュ議長の会見がタカ派なら158円台を試す。ハト派なら157円台前半までの調整が入る。',
    ),
    (
        '豪ドル：9:30のCPIが予想+4.2%を上回れば利上げ観測が強まる',
        '豪CPIは前年比の予想+4.2%、前回+4.0%、月次は予想+0.7%（FFのみ・要確認）。RBAは9/29に0.25%利上げ済みで、CPIが予想を上回れば11/3会合の追加利上げ観測が強まり、豪ドル買いに振れる。',
    ),
    (
        'NZドル：RBNZは3.00%への25bp利上げが予想',
        'RBNZは9/2会合で0.25%利上げ済みで、今回も予想は25bp利上げの3.00%（Kiss/FF一致）。予想どおりなら織り込み済みで、11:00のブレマン総裁の会見が追加利上げの示唆を含むかが値動きを決める。',
    ),
    (
        'カナダドル：BOCは2.25%据え置きと2.50%利上げで予想が割れる',
        'KissFXの予想は2.25%据え置きと2.50%利上げで拮抗し、ForexFactoryの予想は2.50%（相違・要確認）。9月CPIは前年比+3.1%と予想を下回っており（10/19）、据え置きならカナダドル売り、利上げならカナダドル買いが入る。',
    ),
    (
        '休場：なし',
        'KissFXとForexFactoryのいずれにも本日の主要市場の休場情報はない。',
    ),
    (
        '今週のイベント：10/29 ECB、10/30 日銀',
        '10/29にECB、10/30に日銀の会合がある（KissFX）。本日のFOMC後の米金利の動きが、ECBと日銀を前にしたドル円とユーロドルの方向を決める。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('05:30', '🇺🇸 米', 'API週間原油在庫（FFのみ・要確認）', '低', '—', '—'),
    ('09:15', '🇦🇺 豪', 'RBA ブロック総裁 発言（FFのみ・要確認）', '中', '—', '—'),
    ('09:30', '🇦🇺 豪', '第3四半期消費者物価指数（Kissのみ・数値の前期比/前年比の対応が不明・要確認）', '高', '—', '—'),
    ('09:30', '🇦🇺 豪', '消費者物価指数 前年比（Kiss/FF一致）', '高', '+4.2%', '+4.0%'),
    ('09:30', '🇦🇺 豪', '消費者物価指数 前月比（FFのみ・要確認）', '高', '+0.7%', '+0.4%'),
    ('09:30', '🇦🇺 豪', 'トリム平均CPI 前月比（FFのみ・要確認）', '高', '+0.3%', '+0.2%'),
    ('10:00', '🇳🇿 NZ', 'RBNZ政策金利（Kiss/FF一致）', '高', '3.00%', '2.75%'),
    ('10:00', '🇳🇿 NZ', 'RBNZ声明（Kiss/FF一致）', '高', '—', '—'),
    ('11:00', '🇳🇿 NZ', 'ブレマンRBNZ総裁 記者会見（Kiss/FF一致）', '高', '—', '—'),
    ('16:00', '🇩🇪 独', 'GFK消費者信頼感調査（予想値が相違・要確認）', '低', 'Kiss-30.9／FF-30.1', '-30.6'),
    ('18:00', '🇨🇭 スイス', 'UBS経済見通し（FFのみ・要確認）', '低', '—', '2.6'),
    ('18:42', '🇩🇪 独', '10年債入札（FFのみ・要確認）', '低', '—', '3.58'),
    ('20:00', '🇺🇸 米', 'MBA住宅ローン申請指数（Kissのみ・要確認）', '低', '—', '-5.3%'),
    ('21:30', '🇬🇧 英', '年次予算案発表・秋季予測声明（FFのみ・要確認）', '高', '—', '—'),
    ('21:30', '🇺🇸 米', '卸売在庫 速報値（前回値が相違・要確認）', '低', '+0.5%', 'Kiss+0.5%／FF+0.7%'),
    ('21:30', '🇺🇸 米', '財の貿易収支（FFのみ・要確認）', '低', '-1304億ドル', '-1326億ドル'),
    ('22:00', '🇨🇳 中', 'CB景気先行指数 前月比（FFのみ・要確認）', '低', '—', '-0.2%'),
    ('22:45', '🇨🇦 加', 'BOC政策金利（予想が相違・要確認）', '高', 'Kiss2.25%/2.50%拮抗／FF2.50%', '2.25%'),
    ('22:45', '🇨🇦 加', 'BOC声明・金融政策報告（Kiss/FF一致）', '高', '—', '—'),
    ('23:30', '🇨🇦 加', 'マックレムBOC総裁 記者会見（Kiss/FF一致）', '高', '—', '—'),
    ('23:30', '🇺🇸 米', 'EIA週間原油在庫（前回値が相違・要確認）', '低', 'FF-10万バレル', 'Kiss-306.0万／FF-310万バレル'),
    ('27:00', '🇺🇸 米', 'FOMC政策金利・声明（Kiss/FF一致・10/29 03:00 JST）', '高', '4.00%', '4.00%'),
    ('27:30', '🇺🇸 米', 'ウォーシュFRB議長 記者会見（Kiss/FF一致・10/29 03:30 JST）', '高', '—', '—'),
    ('29:00', '🇺🇸 米', 'アルファベット・マイクロソフト決算（米株引け後・Kissのみ・要確認）', '中', '—', '—'),
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
          <h3>📰 前営業日の相場振り返り（2026-10-27 火）</h3>
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
