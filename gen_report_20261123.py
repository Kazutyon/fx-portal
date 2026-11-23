# -*- coding: utf-8 -*-
"""FX日報 2026-11-23（月）生成スクリプト"""
import glob, os, datetime

TODAY = '2026-11-23'
WEEKDAY = '月'
DAYS = ['月', '火', '水', '木', '金', '土', '日']

HERO_SUB = ('先週末11/20（金）はAI関連株の急落でリスク回避の円買いが進み、ドル円は159.84円から158.42円まで下げて200日線を割り込んだ。'
            '本日は日本が勤労感謝の日で休場、欧英米のPMI速報値と翌朝のウィリアムズNY連銀総裁の講演が材料。')

# サイドバー用アーカイブ（今日を除く直近10件）
files = sorted(glob.glob('reports/*.html'), reverse=True)
files = [f for f in files if os.path.basename(f) != f'{TODAY}.html'][:10]
archive_items = ''
for f in files:
    name = os.path.basename(f).replace('.html', '')
    d = datetime.date.fromisoformat(name)
    archive_items += f'<li><a href="{name}.html">{name}（{DAYS[d.weekday()]}）</a></li>\n'

ICON_GRID = '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/></svg>'
ICON_DOC = '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="12" y2="17"/></svg>'
ICON_CHART = '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><polyline points="7 16 11 11 15 14 19 7"/></svg>'
ICON_TOOL = '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/><circle cx="8" cy="6" r="2"/><circle cx="17" cy="12" r="2"/><circle cx="11" cy="18" r="2"/></svg>'
ICON_INFO = '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>'
ICON_SHIELD = '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
ICON_MAIL = '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>'

# 経済指標カレンダー（時刻, 国旗+国, 指標, 重要度, 予想, 前回）
CAL = [
    ('06:45', '🇳🇿 NZ', '【発表済み】第3四半期小売売上高 前期比', '◎', '+0.5%', '-0.5%'),
    ('06:45', '🇳🇿 NZ', '【発表済み】第3四半期コア小売売上高 前期比（要確認）', '低', '+0.8%', '+0.7%'),
    ('07:00', '🇦🇺 豪', '製造業PMI速報値（要確認）', '低', '—', '49.7'),
    ('07:00', '🇦🇺 豪', 'サービス業PMI速報値（要確認）', '低', '—', '47.8'),
    ('終日', '🇯🇵 日', '勤労感謝の日で休場', '—', '—', '—'),
    ('17:15', '🇫🇷 仏', '製造業PMI速報値', '○', '49.8', '49.5（要確認）'),
    ('17:15', '🇫🇷 仏', '非製造業PMI速報値', '○', '47.3（要確認）', '46.2（要確認）'),
    ('17:30', '🇩🇪 独', '製造業PMI速報値', '◎', '54.1', '54.2'),
    ('17:30', '🇩🇪 独', '非製造業PMI速報値', '○', '52.3（要確認）', '52.5（要確認）'),
    ('18:00', '🇪🇺 欧', '製造業PMI速報値', '◎', '52.7', '52.7'),
    ('18:00', '🇪🇺 欧', '非製造業PMI速報値', '○', '51.9（要確認）', '51.4（要確認）'),
    ('18:30', '🇬🇧 英', '製造業PMI速報値', '◎', '53.0', '52.8'),
    ('18:30', '🇬🇧 英', '非製造業PMI速報値', '◎', '53.0', '52.8（要確認）'),
    ('22:00', '🇬🇧 英', 'ピル英中銀チーフエコノミスト 発言', '△', '要人発言', '—'),
    ('22:30', '🇺🇸 米', 'シカゴ連銀全米活動指数（要確認）', 'C', '+0.20', '+0.07'),
    ('22:30', '🇨🇦 加', '第3四半期企業利益 前期比（要確認）', '低', '—', '+8.7%'),
    ('23:45', '🇺🇸 米', '製造業PMI速報値', 'AA', '54.5', '54.9（要確認）'),
    ('23:45', '🇺🇸 米', '非製造業PMI速報値', 'A', '55.6', '56.1（要確認）'),
    ('27:00', '🇺🇸 米', '2年債入札 690億ドル', 'A', '—', '—'),
    ('翌06:00', '🇺🇸 米', 'ウィリアムズNY連銀総裁 講演（投票権あり・質疑応答あり）', 'AA', '要人発言', '—'),
]
cal_rows = '\n'.join(
    f'            <tr><td>{t}</td><td>{c}</td><td>{n}</td><td>{r}</td><td>{fc}</td><td>{pv}</td></tr>'
    for t, c, n, r, fc, pv in CAL)

# 中銀ファンダメンタルズ
FUND = [
    ('FRB', '🇺🇸 USD', '3.75–4.00%', 'var(--red)', 'タカ派（12月利上げ観測は後退気味）',
     '誘導目標レンジは3.75〜4.00%で、次回FOMCは12/9。11月中旬に公表された前回会合の議事要旨では、大半の参加者が追加引き締めを適切と判断し、2名は0.25%を超える利上げも視野に入れた。ただ11/20は株安と米債利回りの低下を受け、短期金融市場が12月利上げを完全には織り込まなくなった。25日の10月PCE価格指数が12月判断の最大の材料。'),
    ('日銀', '🇯🇵 JPY', '1.25%', 'var(--blue)', 'タカ派（12月利上げ期待が高止まり）',
     '無担保コール翌日物の誘導目標は1.25%、次回会合は12/18。7〜9月期GDPはマイナス成長だったが、高田審議委員のタカ派発言で12月利上げ期待は高水準を維持。26日に田村審議委員が金融経済懇談会に出席し、利上げペース加速を支持する発言が出れば円買い材料になる。'),
    ('ECB', '🇪🇺 EUR', '2.50%', 'var(--red)', 'タカ派寄り（12月の行動を示唆する発言）',
     '預金ファシリティ金利は2.50%（主要リファイナンス金利2.65%）、次回理事会は12/17。ナーゲル独連銀総裁が「12月会合で何かをする必要がある」と発言。一方でフランス財政への不安と欧州景気の鈍化がユーロの上値を抑える。26日に10月理事会の議事要旨、27日にフランス国債の格付け見直し。'),
    ('BOE', '🇬🇧 GBP', '4.00%', 'var(--red)', 'タカ派（12月追加利上げを高確率で織り込み）',
     '11月会合で3.75%から4.00%へ利上げ、次回は12/17。英サービスCPIが予想を下回り利上げ観測は一時後退したが、9月月次GDPのプラス成長で12月利上げの織り込みは一時93%まで上昇。来年の利下げ転換観測がポンドの重し。'),
    ('RBA', '🇦🇺 AUD', '4.85%', 'var(--red)', 'タカ派（ただし雇用悪化で追加利上げに慎重）',
     '11月会合で4.60%から4.85%へ利上げ、次回は12/8。11/19の雇用統計が弱く、豪ドルは対ドルで年初来安値0.6662ドルまで下落。25日の10月CPIは自動車燃料の急騰でインフレ加速が見込まれ、上振れなら利上げ観測が再燃する。'),
    ('RBNZ', '🇳🇿 NZD', '2.75%', 'var(--red)', 'タカ派寄り',
     '9月に2.50%から2.75%へ利上げし、その後は据え置き。次回は12/9。本日06:45の第3四半期小売売上高（予想+0.5%）が国内消費の強さを測る材料。'),
    ('BOC', '🇨🇦 CAD', '2.50%', 'var(--red)', 'タカ派転換',
     '10月会合で2.25%から2.50%へ利上げ、次回は12/9。24日にマックレム総裁の講演があり、追加利上げに前向きな発言ならカナダドル買い。'),
    ('SNB', '🇨🇭 CHF', '0.00%', 'var(--muted)', 'ハト派〜中立（フラン高警戒）',
     '2025年6月に0.00%へ引き下げて以降据え置き、次回は12/10。先週はリスク回避でフランが買われたが、円の上昇率がフランを上回った。フラン高が続けば為替介入への警戒が強まる。'),
]
fund_rows = '\n'.join(f'''            <tr>
              <td>{b}</td><td>{c}</td><td><strong>{r}</strong></td>
              <td style="color:{col};">{s}</td>
              <td style="font-size:12px;">{bg}</td>
            </tr>''' for b, c, r, col, s, bg in FUND)

html = f'''<!DOCTYPE html>
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
      <a href="../index.html">{ICON_GRID}ダッシュボード</a>
      <a href="#" class="active">{ICON_DOC}日報</a>
      <a href="../archive.html">{ICON_CHART}アーカイブ</a>
      <span class="nav-section">ツール・販売</span>
      <a href="../index.html#tools">{ICON_TOOL}トレードインジケーター</a>
      <span class="nav-section">サイト情報</span>
      <a href="../about.html">{ICON_INFO}About</a>
      <a href="../disclaimer.html">{ICON_SHIELD}免責事項</a>
      <a href="../contact.html">{ICON_MAIL}お問い合わせ</a>
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
        <p class="sub">{HERO_SUB}</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>{TODAY}</strong>
        <em>{WEEKDAY}</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>株安主導の円買いが続くかが焦点。クロス円は戻り売り優先、ドル円は158.42円と159円台回復の攻防</h3>
        <p>11/20（金）のドル円は始値159.69円、高値159.84円、安値158.42円、終値158.57円。ナスダックの下げが4%を超えるAI関連株の売りでリスク回避が強まり、米国債利回りの低下も重なった。短期金融市場では12月のFRB利上げが完全には織り込まれなくなり、日米金利差の縮小観測がドルの重し。先週の円はG10通貨で最も上昇率が高く、安全通貨のスイスフランも上回った。本日は東京が休場で、欧州勢が参入する夕方以降に値幅が出やすい。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>AUD/JPY 🇦🇺🇯🇵</h3>
        <p>11/20は106.33円で始まり104.73円まで下落、104.97円で引けた。下げの理由は2つ。1つ目は株価急落でリスクに敏感な豪ドルが売られたこと。2つ目は11/19の弱い雇用統計で豪ドルが対ドルの年初来安値0.6662ドルを付け、投機筋の豪ドル売り越しも増えていること。4時間足デイトレ適性は1位（スコア77・適、ADX62.0、方向は下降、5日ADR 88.1pips）。15分・30分足では104.73円を割り込むかが戻り売り継続の分岐点。25日の豪10月CPIが次の大きな材料。</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red,#c0392b)">HIGH</h3>
        <p>VIXは30台（直近30.17、要確認）と警戒水準の20を大きく上回る。11/20は日経平均が一時3,000円超下落し、ナスダックは4%超の下落。1週間物のドル円オプション変動率は6.63%。本日は東京休場で流動性が薄く、値が飛びやすい。今週は25日に米PCEと豪CPIが重なり、26日の米感謝祭以降は参加者が減る。</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>7件</h3>
        <p>NZ 第3四半期小売売上高(06:45・発表済み)、独 製造業PMI(17:30)、欧 製造業PMI(18:00)、英 製造業・非製造業PMI(18:30)、米 製造業PMI(23:45)、米 ウィリアムズNY連銀総裁(翌06:00)</p>
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
              <li>日本：勤労感謝の日で休場。日経平均先物・オプションの祝日取引もなし。今週は11/26（木）が米国の感謝祭で株式・債券市場が休場、27日（金）は米国が短縮取引。</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>【休場】🇯🇵 日本 勤労感謝の日</li>
              <li>06:45 🇳🇿 NZ 第3四半期小売売上高 前期比 予想+0.5%（◎）【発表済み】</li>
              <li>17:30 🇩🇪 独 製造業PMI速報値 予想54.1（◎）</li>
              <li>18:00 🇪🇺 欧 製造業PMI速報値 予想52.7（◎）</li>
              <li>18:30 🇬🇧 英 製造業PMI・非製造業PMI速報値 予想53.0／53.0（◎◎）</li>
              <li>23:45 🇺🇸 米 製造業PMI速報値 予想54.5（AA）・非製造業PMI速報値 予想55.6（A）</li>
              <li>27:00 🇺🇸 米 2年債入札 690億ドル（A）</li>
              <li>翌06:00 🇺🇸 米 ウィリアムズNY連銀総裁 講演（投票権あり、AA）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>ドル円：158.42円と200日線</strong>：11/20に200日移動平均線を割り込み、158.42円まで下げた。19日は159.97円まで上げたが160円は抜けず、160円近辺では為替介入への警戒も上値を抑えた。4時間足デイトレ適性は10位（スコア33・見送り、ADX19.7・レンジ）で、方向感が弱い。15分・30分足で158.42円を割れば下落継続、159円台を回復できなければ戻り売りが優勢。当面は156〜160円のレンジを想定する声がある。</li>
              <li><strong>円：リスク回避の買いが主導</strong>：先週は株安局面で円が買われ、株高局面で売られる展開。投機筋の円買い越しは縮小しており、株価が戻ると円売りの巻き戻しが速い。26日の田村日銀審議委員の懇談会でタカ派発言が出れば円買いが強まる。</li>
              <li><strong>米国：PMIとウィリアムズ総裁</strong>：23:45の米PMIは製造業が予想54.5、非製造業が予想55.6。いずれも前回を下回る予想で、さらに下振れれば米金利の低下を通じてドル売り・円買いが進む。翌06:00のウィリアムズNY連銀総裁が12月利上げ支持を明確にすれば、ドルの下値を支える。</li>
              <li><strong>ユーロ：1.0950〜1.1000ドルの狭いレンジ</strong>：ユーロドルは1.1000ドルが強い上値抵抗、1.09ドル台半ばが下値支持。独・ユーロ圏の製造業PMIが予想を上回ればユーロ買い。フランスの財政不安と27日の格付け見直しが上値の重し。</li>
              <li><strong>ポンド：英PMIで12月利上げ観測を確認</strong>：ポンドドルは英サービスCPIの下振れで先週19日に年初来安値1.3120ドルを付けた。18:30の英PMIが予想を上回れば12月利上げの織り込みが維持されポンド買い、下振れならポンド円は207円台前半の安値を試す。</li>
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
          <strong>VIX</strong>：30.17（前日比-5.72、日付は要確認）。30超はリスク回避が強い水準。<strong>米国債利回り</strong>：10年債4.948%、2年債4.687%（いずれも直近値）。10年債は11/20に5%を割り込み、日米金利差の縮小観測で円買いを後押しした。2-10年差は約+26bp。<strong>ドルインデックス（DXY）</strong>：103.85。先週は年初来高値圏で推移した。<strong>金</strong>：NY金先物12月限は前日終値3,515.40ドル、直近は3,618.35ドルへ反発。11/20は株安の換金売りで大幅続落していた。<strong>原油</strong>：WTIは82.92ドル（直近）。11/20は下振れ後に中東の地政学リスクで反発した。<br><br><strong>政策金利（11/23確認）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。今週は主要8中銀の政策発表なし。<br><br><strong>今週の焦点：</strong> 24日 独Ifo景況感・米消費者信頼感・マックレム加中銀総裁講演、25日 豪10月CPI・米GDP改定値・米10月PCE価格指数・ベージュブック、26日 米感謝祭休場・田村日銀審議委員の懇談会・ECB議事要旨、27日 東京都区部CPI・フランス国債の格付け見直し・ブラックフライデー（米短縮取引）。
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
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>AUD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア77・適。ADX62.0、5日ADR 88.1pips（5年平均比99%）、4H方向は下降。11/20は104.73円まで下げ104.97円引け。株安局面で最も売られやすい組み合わせで、25日の豪CPIが次の材料。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>EUR/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア70・適。ADX37.9、5日ADR 100.5pips（同85%）、4H方向は下降。11/20は175.35円から173.74円まで下げ173.92円引け。フランス財政不安とリスク回避の円買いが同時に効く。本日17:30〜18:00の独・ユーロ圏PMIが材料。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア69・適。ADX49.0、5日ADR 122.8pips（同85%）、4H方向は下降。11/20は209.20円から207.27円まで下げ207.45円引け。9月に支えられた水準を割り込むかが焦点。18:30の英PMIが材料。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/AUD</strong><br><span style="color:var(--muted);font-size:12px;">スコア65・適。ADX42.6、5日ADR 88.1pips（同81%）、4H方向は上昇。豪ドルが弱い雇用統計で売られ、ユーロとの比較で豪ドル安が進んでいる。25日の豪CPIで流れが変わる。</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>AUD/USD</strong><br><span style="color:var(--muted);font-size:12px;">スコア57・候補。ADX61.7と強い下降トレンドだが、5日ADRは40.3pipsと値幅は小さい。年初来安値0.6662ドルが下値の目安。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4時間足ランキングは2026/11/23 09:23 JST生成分。スコア・ADX・ADRは候補選定の補助指標であり、売買推奨ではない。USD/JPYは10位（スコア33・見送り）。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（前営業日 2026-11-20 金）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック1】AI関連株の売りが世界に波及：日経平均は一時3,000円超安、ナスダックは4%超安</div>
            エヌビディアの決算は好調で、アンソロピックのIPOも好調な滑り出しだった。それでもAI関連株を中心に売りが強まった。好材料への期待が大きかった分、失望が大きかったこと、そして巨額のAI投資をどう収益化するのかという疑問が払拭できていないことが理由。東京時間に日経平均が一時3,000円超下落し、NYではIT・ハイテク株の下げがきつくナスダックは4%超下落した。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック2】ドル円は159.84円から158.42円へ急落、200日移動平均線を割り込む</div>
            ドル円は前日に159.97円まで上げたが160円の節目は抜けなかった。11/20は東京朝に159.84円を付けた後、株安を受けたリスク回避の円買いで下落。米国債利回りの低下も重なって200日移動平均線を割り込み、NY時間に158.42円まで下げて158.57円で引けた。前日まで160円に向けて円安が進んでいた流れが一転した形。週間では円がスイスフランを上回る上昇率でG10通貨の首位。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック3】12月のFRB利上げ観測が後退：米国債利回りは低下、10年債は5%割れ</div>
            週半ばに公表された前回FOMCの議事要旨では、大半の参加者が追加引き締めを適切とし、2名は0.25%を超える利上げにも言及していた。このためドル指数は年初来高値圏で推移した。しかし11/20は株安で米国債が買われ、10年債利回りは5%を割り込んだ。短期金融市場は12月利上げを完全には織り込まなくなり、ドルを支えてきた金利面の材料が弱まった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック4】クロス円が全面安：ユーロ円173.74円、ポンド円207.27円、豪ドル円104.73円</div>
            リスク回避の円買いでクロス円は軒並み下落した。ユーロ円は175.35円から173.74円まで下げ173.92円引け、ポンド円は207.27円まで下げ207.45円引け、豪ドル円は104.97円引け、カナダ円は110.44円まで下げ110.53円引け。ドルストレートは方向感が乏しく、ユーロドルは1.0957ドルから1.1000ドルの狭いレンジで1.0968ドル引け。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック5】商品市場：金は換金売りで大幅続落、原油は地政学リスクで反発</div>
            NY金先物12月限は株安を受けた換金売りで大幅続落し、3,515.40ドルで引けた。原油は一時下振れたが、中東の地政学リスクを背景に反発した。原油価格の推移は、25日の豪CPIや米PCEでのエネルギー価格の寄与に直結する。
          </div>
          <div class="handover">
            <strong>本日（11/23月）への引継ぎ：ドル円は158.57円、ユーロドルは1.0968ドル、ユーロ円は173.92円、豪ドル円は104.97円で週を終えた。先週は「FRBの追加利上げ観測によるドル高」と「AI株安による円買い」がぶつかり、金曜は円買いが勝ってドル円は200日線を割り込んだ。週末の新材料は確認できず（要確認）。本日は東京休場で実需の売買がなく、欧州PMIと23:45の米PMIで米金利がどちらへ動くかが方向を決める。米PMIが弱ければドル売り・円買いが続き、ドル円の次の下値目安は158.42円。今週は25日の米PCEで12月利上げの確度を測り、26日の感謝祭以降は薄商いになる。</strong>
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
{cal_rows}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間（24時以降は翌日、「翌」は11/24火）。冬時間のため米東部時間+14時間で換算。複数の情報で一致した値を掲載し、一致を確認できない項目・数値には「（要確認）」を付記。重要度は米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×。「低」は低重要度の参考指標。【発表済み】は本日0時〜7時に実施済みの項目。</p>
      </div>

      <div class="panel full" id="fundamentals">
        <div class="panel-head">
          <h3>🏦 主要中銀ファンダメンタルズ（週次更新）</h3>
          <span>{TODAY} 現在</span>
        </div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>政策金利</th><th>スタンス</th><th>背景・理由</th></tr></thead>
          <tbody>
{fund_rows}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。政策金利は複数の情報で一致を確認。最新情報は各中銀の公式サイトでご確認ください。</p>
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
'''

with open(f'reports/{TODAY}.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'reports/{TODAY}.html written ({len(html)} chars)')
