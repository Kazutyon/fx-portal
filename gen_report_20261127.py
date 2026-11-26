# -*- coding: utf-8 -*-
"""FX日報 2026-11-27（金）生成スクリプト"""
import glob, os, datetime

TODAY = '2026-11-27'
WEEKDAY = '金'
DAYS = ['月', '火', '水', '木', '金', '土', '日']

HERO_SUB = ('11/26（木）のドル円は、田村日銀審議委員のタカ派発言で158.95円まで下げた後、日欧の株高で159.34円まで戻した。本日は08:30の東京都区部CPIが円の材料で、米国は感謝祭翌日の短縮取引。')

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
    ('06:00', '🇳🇿 NZ', '【発表済み】ANZ消費者信頼感指数（11月）（結果は要確認）', '×', '—', '96.2'),
    ('08:30', '🇯🇵 日', '東京都区部消費者物価指数（11月）前年比', '◎', '+3.1%', '+2.8%'),
    ('08:30', '🇯🇵 日', '東京都区部消費者物価指数（除生鮮）前年比', '◎', '+2.9%〜+3.0%（要確認）', '+2.6%'),
    ('08:50', '🇯🇵 日', '対外・対内証券投資（先週）（要確認）', '低', '—', '—'),
    ('10:30', '🇨🇳 中', '工業利益（10月）前年比（要確認）', '低', '—', '+15.5%'),
    ('16:45', '🇫🇷 仏', '第3四半期GDP 改定値 前期比', '△', '-0.1%', '-0.1%'),
    ('16:45', '🇫🇷 仏', '消費者物価指数 速報値（11月）前月比／前年比', '△', '-0.2%／+3.4%（前年比は要確認）', '+0.4%／+3.4%'),
    ('16:45', '🇫🇷 仏', '消費者支出（10月）前月比', '×', '+0.1%', '-0.5%'),
    ('16:45', '🇫🇷 仏', '民間雇用者数 確報値（第3四半期）前期比（要確認）', '低', '-0.1%', '-0.1%'),
    ('17:00', '🇪🇸 西', '消費者物価指数 速報値（11月）前年比（要確認）', '低', '+4.7%', '+4.9%'),
    ('17:55', '🇩🇪 独', '失業率（11月）', '△', '6.4%', '6.4%'),
    ('17:55', '🇩🇪 独', '失業者数変化（11月）', '△', '+0.45万〜+0.5万人（要確認）', '+0.40万人'),
    ('18:00', '🇪🇺 欧', 'ECB消費者期待調査（10月）（要確認）', '低', '—', '—'),
    ('19:00', '🇪🇺 欧', '経済信頼感指数（11月）（要確認）', '低', '—', '96.9'),
    ('19:00', '🇪🇺 欧', '消費者信頼感指数 確報値（11月）（要確認）', '低', '—', '—'),
    ('19:33', '🇮🇹 伊', '10年債入札（要確認）', '低', '—', '4.49%'),
    ('20:00', '🇧🇷 ブ', 'FGVインフレ IGP-M（11月）前年比（要確認）', '低', '5.96%', '5.24%'),
    ('20:30', '🇮🇳 印', '外貨準備高（先週）（要確認）', '低', '—', '—'),
    ('20:30', '🇧🇷 ブ', 'ローン残高（10月）（要確認）', '低', '—', '0.4%'),
    ('20:30', '🇧🇷 ブ', '融資残高（10月）（要確認）', '低', '—', '7兆4440億レアル'),
    ('20:30', '🇧🇷 ブ', '個人ローン・デフォルト率（10月）（要確認）', '低', '—', '8.1%'),
    ('21:00', '🇧🇷 ブ', '全国失業率（10月）（要確認）', '低', '5.1%', '5.2%'),
    ('21:50', '🇩🇪 独', 'ナーゲル独連銀総裁 発言（時刻は21:40〜21:50で要確認）', '△', '要人発言', '—'),
    ('22:30', '🇨🇦 加', '第3四半期経常収支', '○', '+94.0億〜+95億加ドル（要確認）', '+88.4億加ドル'),
    ('22:30', '🇺🇸 米', '卸売在庫 速報値（10月）前月比', 'C', '+0.5%', '+0.6%（要確認）'),
    ('22:30', '🇺🇸 米', '財の貿易収支 速報値（10月）（要確認）', '低', '-1359億ドル', '-1349億ドル'),
    ('終日', '🇺🇸 米', '感謝祭翌日（ブラックフライデー）で株式市場は短縮取引。注目度の高い米指標の発表なし', '—', '—', '—'),
]
cal_rows = '\n'.join(
    f'            <tr><td>{t}</td><td>{c}</td><td>{n}</td><td>{r}</td><td>{fc}</td><td>{pv}</td></tr>'
    for t, c, n, r, fc, pv in CAL)

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
        <h3>日欧の株高で円売りが戻り、ドル円は159円台前半で週末へ。今日は08:30の東京CPIが円の方向を決め、米国は短縮取引で市場は薄い</h3>
        <p>昨日は田村日銀審議委員が「政策金利を中立水準に早く持っていく必要がある」と述べ、東京朝に円が買われてドル円は158.95円まで下げた。ただ円買いは続かず、エヌビディアをめぐる不安が和らいで日経平均が487円高、欧州ではドイツ株が2%超上げると円とスイスフランが売られ、ドル円はロンドン16時の値決めにかけて159.34円まで戻した。米国は感謝祭で休場し、NY時間は159.2円台で動かなかった。今日は08:30の東京都区部CPI（前年比 予想+3.1%）が日銀の12月利上げ観測を左右する。予想を上回れば円買い、下回れば円売りに傾く。米国はブラックフライデーで株式市場が短縮取引、30日（月）は月末で、薄い市場に月末の売買が重なる。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>AUD/JPY 🇦🇺🇯🇵</h3>
        <p>4時間足デイトレ適性は1位（11/26時点、スコア90・最適、ADX41.8、5日ADR 118.7pips・5年比132%）。昨日は豪第3四半期の民間設備投資が前期比+12.2%（予想+4.3%）と2011年の資源投資ブーム以来の伸びになり、豪ドルが買われた。豪ドル円は105.38円まで下げた後、105.81円まで上げた。AIデータセンター向けの投資が伸びた結果で、来年の豪中銀の利下げ期待は後退した。今日は08:30の東京CPIが円側の材料。CPIが強く円買いになれば豪ドル円は105.38円が下値の目安、CPIが弱く円売りになれば105.81円の上抜けを15分・30分足で確かめて買いを考える。</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--orange,#e67e22)">MEDIUM</h3>
        <p>米国は感謝祭翌日で株式市場が短縮取引となり、米国勢の多くは週明けまで休む。今日は週末、30日（月）は11月最後の営業日で、薄い市場に月末の売買が入ると値が飛びやすい。AI関連株はエヌビディアの経営不安で今週大きく揺れており、米国の新関税案には中国が対抗措置の権利を留保すると反発している。中東ではホルムズ海峡周辺の緊張で原油が一時85ドル台に乗せた。</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>6件</h3>
        <p>日 東京都区部CPI(08:30)、仏 CPI速報値・GDP改定値(16:45)、独 失業率(17:55)、独 ナーゲル連銀総裁 発言(21:50)、加 経常収支(22:30)、米 卸売在庫(22:30)</p>
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
              <li>なし。ただし米国は感謝祭翌日（ブラックフライデー）で株式市場が短縮取引。祝日ではないが連休を取る企業や人が多く、NY時間の参加者は少ない。</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>08:30 🇯🇵 日 東京都区部消費者物価指数（11月）前年比 予想+3.1%・前回+2.8%、除生鮮 予想+2.9%〜+3.0%（要確認）・前回+2.6%（◎）</li>
              <li>16:45 🇫🇷 仏 消費者物価指数 速報値（11月）前月比 予想-0.2%、第3四半期GDP改定値 前期比 予想-0.1%（△）</li>
              <li>17:55 🇩🇪 独 失業率（11月）予想6.4%・前回6.4%（△）</li>
              <li>21:50 🇩🇪 独 ナーゲル独連銀総裁 発言（時刻は21:40〜21:50で要確認）（△）</li>
              <li>22:30 🇨🇦 加 第3四半期経常収支（○）</li>
              <li>22:30 🇺🇸 米 卸売在庫 速報値（10月）前月比 予想+0.5%（C）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>ドル円：159.34円の上値と158.95円の下値</strong>：昨日の高値はロンドン16時の値決めにかけての159.34円、安値は田村委員の発言直後の158.95円。値幅は40銭に満たず、方向は出ていない。上は24日高値の159.58円、その上に節目の160.00円があり、160円に近づくと為替介入への警戒で上値は重い。下は20日安値の158.42円。15分・30分足で159.34円を上抜ければ159.58円まで、158.95円を割れば158.42円までの値動きを想定する。</li>
              <li><strong>東京CPI：日銀の12月利上げ観測を確かめる</strong>：田村委員は昨日、中立金利は2%前後との見方を変えず、数カ月ごとに0.25%ずつ利上げする想定を示した。12/18の日銀会合を前に、東京CPIが予想を上回れば12月利上げ観測が強まり円買い、下回れば円売り。米国の材料が少ない今日は、東京時間の円の動きがその日の方向になりやすい。</li>
              <li><strong>スイスフラン：安全通貨の買いが一服</strong>：AI株安の局面ではスイスフランが買われていたが、昨日は欧州株高で売り戻され、24時間のG10通貨の対ドル成績で最下位になった。ユーロスイスは0.9100から0.9158へ反発した。株が崩れればフラン買いが戻る。米通商代表部がスイスの通貨上昇の抑制を問題視したとの指摘があり、スイス中銀がフラン売り介入に動きにくくなるとの見方もある（要確認）。</li>
              <li><strong>ユーロ：ECB議事要旨は利上げ寄り</strong>：10月会合の議事要旨では、多くのメンバーが10月の利上げを支持し得たとされ、インフレ見通しが大きく改善しない限り利上げが必要との認識が示された。9月以降のユーロ安も議論された。ユーロ円は22時45分ごろに174.89円まで上げ、25日高値の174.88円をわずかに上抜いた。12/17のECB会合に向けてユーロの下値を支える材料。</li>
              <li><strong>米関税案への反発</strong>：米通商代表部は25日、「構造的な過剰生産」を理由に中国・EU・日本・インドなど14の経済圏に新関税を課す準備を進めると発表した。中国商務省は昨日、米国の通商法301条調査を「単独主義的な行為」と批判し、対抗措置を講じる権利を留保すると表明した。続報が薄い市場に出ると、円買い・フラン買いが急に進む。</li>
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
          <strong>米国市場</strong>：11/26は感謝祭で株式・債券市場が休場。米株価指数先物は日本時間27日03:00に取引を終えた。今日も株式市場は短縮取引。<strong>日本株</strong>：日経平均は57,499.16円（+487.54円）。半導体株の買い戻しで前場に一時1,200円超上げたが、AIへの懸念が残り後場は伸び悩んだ。<strong>アジア・欧州株</strong>：ハンセン指数は+1.19%の22,226.88。エヌビディアのファンCEOは調査対象ではないと米副大統領が述べ、不安が和らいだ。ドイツ株は寄り付き+1.8%、NY時間には2%超上げた。<strong>商品</strong>：WTIは時間外で一時85.23ドルまで上げた後、84ドルを割り込んだ。金は3,595ドル台と前日の下げから反発。<strong>その他</strong>：韓国中銀は政策金利を3.25%に引き上げた。<br><br><strong>政策金利（11/23確認値を継続）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。次回会合はRBA 12/8、FRB・RBNZ・BOC 12/9、SNB 12/10、ECB・BOE 12/17、日銀 12/18。<br><br><strong>来週：</strong> 30日（月）が11月最後の営業日。
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
              <td><strong>AUD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア90・最適。ADX41.8、5日ADR 118.7pips（5年比132%）、4H方向はレンジ。昨日は豪設備投資の上振れで105.38円から105.81円まで上げた。今日は08:30の東京CPIで円側が動く。</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>EUR/AUD</strong><br><span style="color:var(--muted);font-size:12px;">スコア82・最適。ADX22.7、5日ADR 144.9pips（5年比132%）、4H方向は上昇。昨日は豪設備投資で豪ドルが買われた一方、ECB議事要旨は利上げ寄りで、ユーロと豪ドルの両方に買い材料が出た。上昇方向が出ている数少ないペア。</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/CHF</strong><br><span style="color:var(--muted);font-size:12px;">スコア77・適。ADX29.7、5日ADR 65.9pips、4H方向は下降。株安局面のフラン買いで下げてきたが、昨日は欧州株高でフランが売り戻され0.8338前後。株が崩れればフラン買い、株高が続けば下げ止まる。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>AUD/USD</strong><br><span style="color:var(--muted);font-size:12px;">スコア72・適。ADX42.1、5日ADR 59.9pips、4H方向はレンジ。11月に入って0.70ドル台から0.65ドル台まで下げた後、昨日は豪設備投資で0.6625前後から0.6649まで反発した。</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア61・候補。ADX22.4、5日ADR 154.0pips、4H方向はレンジ。昨日は東京時間に208.45円まで下げた後、ロンドンで208.92円まで戻した。英国のエネルギー価格上限の引き上げがポンドの上値を抑える。</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4時間足ランキングは本日分が未更新のため、2026/11/26 11:19 JST生成分のスコアを使用した。スコア・ADX・ADRは候補選定の補助指標であり、売買推奨ではない。同スコア61のUSD/CADは、今日の材料が少ないため表から外した。USD/JPYは11/26時点10位（スコア39・見送り、ADX13.6）。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（前営業日 2026-11-26 木）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック1】豪設備投資が大きく上振れ、豪ドル買い（東京朝）</div>
            09:30の豪第3四半期民間設備投資は前期比+12.2%と、予想の+4.3%を大きく上回り、2011年の資源投資ブーム以来の伸びになった。AIデータセンター向けの機器投資が伸びを押し上げた。豪中銀の利下げ期待が後退して豪ドルが買われ、豪ドル米ドルは0.6649ドルまで上げた。この時点のドル円は159.2円前後。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック2】田村日銀委員のタカ派発言で円買い、ただ続かず（東京午前）</div>
            10:00からの講演で田村日銀審議委員は「政策金利を中立水準に早く持っていく必要がある」「物価上振れの兆しには利上げペースの加速など俊敏に反応することが求められる」と述べた。前日のAI株安も重なって円が買われ、ドル円は158.95円まで下げた。ただ発言は従来のタカ派姿勢の範囲内で、円買いはそこで止まった。この時点のドル円は158.95円。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック3】エヌビディア不安の後退で日本株高、ドル円はじり高（東京午後）</div>
            米副大統領がエヌビディアのファンCEOは調査対象ではないと述べ、AI株への不安が和らいだ。日経平均は前場に一時1,200円超上げ、487円高で引けた。円が売られ、ドル円は午後に159.26円まで上げた。田村委員は午後の会見で、数カ月ごとに0.25%ずつ利上げする想定を示した。この時点のドル円は159.16円。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック4】欧州株高で円とスイスフランが売られる、ECB議事要旨は利上げ寄り（ロンドン）</div>
            ドイツ株が2%超上げるなど欧州株が全面高となり、安全通貨の円とスイスフランが売られた。スイスフランは24時間のG10通貨の対ドル成績で最下位、ユーロスイスは0.9100から0.9158へ反発した。21:30のECB議事要旨では、多くのメンバーが10月の利上げを支持し得たとされ、ユーロ円は22時45分ごろに174.89円まで上げた。この時点のドル円は159.25円。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック5】米国は感謝祭で休場、値決めにかけて小高い（NY）</div>
            米国の株式・債券市場が休場し、NY勢がほぼ不在で値動きは細った。ドル円はロンドン16時（日本時間01:00）の値決めにかけて159.34円まで上げ、日中の高値を少しだけ更新した。ユーロドルは1.0970ドル台で上値を切り下げた。米株価指数先物は日本時間03:00に取引を終えた。この時点のドル円は159.27円。
          </div>
          <div class="handover">
            <strong>本日（11/27金）への引継ぎ：昨日のドル円は、田村委員の発言で下げ、株高で戻した一日だった。値幅は158.95〜159.34円と40銭に満たない。日銀の12月利上げ観測とFRBの12月利上げ観測が並んで続き、160円手前の介入警戒が上値を抑える構図は変わらない。今日の材料は08:30の東京都区部CPI。米国は短縮取引で、30日（月）の月末を前に薄い市場が続く。ドル円は159.34円と158.95円のどちらを抜けるかで方向を決める。</strong>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間。冬時間のため米東部時間+14時間で換算。複数の情報で一致した値を掲載し、一致を確認できない項目・数値には「（要確認）」を付記。重要度は米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×。「低」は低重要度の参考指標。【発表済み】は本日0時〜7時に実施済みの項目。</p>
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
