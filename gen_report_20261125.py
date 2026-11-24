# -*- coding: utf-8 -*-
"""FX日報 2026-11-25（水）生成スクリプト"""
import glob, os, datetime

TODAY = '2026-11-25'
WEEKDAY = '水'
DAYS = ['月', '火', '水', '木', '金', '土', '日']

HERO_SUB = ('11/24（火）は米国の関税引き上げ準備の報道でAI・半導体株が再び急落し、米長期金利は2週間ぶりの低さに。ドル指数は0.5%下げたが、消費者信頼感の上振れでドル円は159円台を保った。本日は豪CPIと米PCE・GDP改定値が材料。')

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
    ('00:00', '🇺🇸 米', '【発表済み】コンファレンスボード消費者信頼感指数（11月）結果103.3', 'AA', '92.4', '91.7→91.9に修正'),
    ('00:00', '🇺🇸 米', '【発表済み】リッチモンド連銀製造業指数（11月）結果3', 'C', '-2', '-2'),
    ('02:25', '🇨🇦 加', '【発表済み】マックレムBOC総裁 講演（時刻・内容は要確認）', '◎', '要人発言', '—'),
    ('03:00', '🇺🇸 米', '【発表済み】5年債入札 700億ドル 最高落札利回り4.719%・応札倍率2.37倍', 'A', '—', '—'),
    ('06:30', '🇺🇸 米', '【発表済み】API週間原油在庫（要確認）', '低', '—', '—'),
    ('08:50', '🇯🇵 日', '企業向けサービス価格指数（10月）前年比', '低', '3.6%（要確認）', '3.7%（要確認）'),
    ('09:30', '🇦🇺 豪', '消費者物価指数（10月）前年比', '○', '+4.7%', '+4.3%'),
    ('09:30', '🇦🇺 豪', '消費者物価指数（10月）前月比（要確認）', '○', '+0.4%', '+0.8%'),
    ('09:30', '🇦🇺 豪', 'トリム平均CPI（10月）前月比（要確認）', '○', '+0.3%', '+0.3%'),
    ('09:30', '🇦🇺 豪', '建設工事完了高（第3四半期）前期比（要確認）', '低', '+0.8%', '-2.1%'),
    ('12:35', '🇯🇵 日', '40年利付国債入札（要確認）', '○', '—', '—'),
    ('14:00', '🇯🇵 日', '日銀版コアCPI 前年比', '低', '2.5%（要確認）', '2.4%（要確認）'),
    ('14:30', '🇯🇵 日', '全国・東京地区百貨店売上高（10月）（要確認）', '低', '—', '—'),
    ('15:00', '🇯🇵 日', '工作機械受注（10月・確報）（要確認）', '×', '—', '+42.5%'),
    ('16:00', '🇩🇪 独', 'GDP改定値（第3四半期）前期比', '△', '+0.2%', '+0.2%'),
    ('16:00', '🇩🇪 独', 'GDP改定値（第3四半期）前年比（要確認）', '△', '+1.3%', '+1.3%'),
    ('16:45', '🇫🇷 仏', '消費者信頼感指数（11月）（要確認）', '△', '81', '80'),
    ('18:00', '🇨🇭 ス', 'UBS景気期待指数（要確認）', '低', '—', '-15.3'),
    ('19:42', '🇩🇪 独', '10年債入札（要確認）', '低', '—', '3.37%'),
    ('21:00', '🇺🇸 米', 'MBA住宅ローン申請指数（要確認）', 'C', '—', '-2.3%'),
    ('21:25', '🇺🇸 米', 'ボウマンFRB副議長 発言（投票権あり）（要確認）', 'AA', '要人発言', '—'),
    ('22:30', '🇺🇸 米', '新規失業保険申請件数', 'AA', '20.0万件（要確認）', '20.3万件'),
    ('22:30', '🇺🇸 米', '個人所得（10月）前月比', 'S', '+0.4%', '+0.2%'),
    ('22:30', '🇺🇸 米', '個人支出（10月）前月比', 'S', '+0.4%', '+0.5%'),
    ('22:30', '🇺🇸 米', 'PCEデフレーター（10月）前年比（要確認）', 'S', '+3.8%', '+3.6%'),
    ('22:30', '🇺🇸 米', 'PCEコア・デフレーター（10月）前月比', 'S', '+0.3%', '+0.3%'),
    ('22:30', '🇺🇸 米', 'PCEコア・デフレーター（10月）前年比（要確認）', 'S', '+3.2%', '+3.1%'),
    ('22:30', '🇺🇸 米', 'GDP改定値（第3四半期）前期比年率', 'AA', '+3.5%', '+3.4%'),
    ('22:30', '🇺🇸 米', '個人消費 改定値（第3四半期）（要確認）', 'AA', '+3.9%', '+3.8%'),
    ('22:30', '🇺🇸 米', 'GDPデフレーター 改定値（第3四半期）', 'AA', '+2.3%', '+2.3%'),
    ('22:30', '🇺🇸 米', 'コアPCEデフレーター 改定値（第3四半期）（要確認）', 'AA', '+2.5%', '+2.5%'),
    ('22:30', '🇺🇸 米', '耐久財受注（10月）前月比', 'A', '+0.6%（要確認）', '+1.8%'),
    ('22:30', '🇺🇸 米', '耐久財受注 除輸送用機器（10月）前月比', 'A', '+0.5%', '+0.5%'),
    ('24:00', '🇺🇸 米', '新築住宅販売件数（10月）', 'A', '65.0万件', '67.6万件'),
    ('24:30', '🇺🇸 米', 'EIA週間原油在庫', 'BB', '—', '+338.0万バレル'),
    ('25:30', '🇺🇸 米', '7年債入札 440億ドル（要確認）', 'A', '—', '—'),
    ('26:00', '🇺🇸 米', '週間天然ガス貯蔵量', 'B', '-190億立方フィート（要確認）', '+200億立方フィート'),
    ('28:00', '🇺🇸 米', '地区連銀経済報告（ベージュブック）', 'B', '—', '—'),
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
        <h3>AI株が再び崩れ、ドル高が一服。今日は米PCEとGDPで「利上げ観測の強さ」が試される</h3>
        <p>昨日は米国が日本・EU・中国などへの関税引き上げを準備していると伝わり、半導体株指数は午後2時台で-7.43%と急落した。米10年債利回りは4.90%前後と2週間ぶりの低さまで下がり、ドル指数は-0.50%の103.80。ユーロドルは1.0980ドルまで戻した。一方でドル円は株安でも159円を守った。米消費者信頼感指数が103.3と約2年ぶりの高さとなり、ドル売りが止まったため。今日22:30の米PCEとGDP改定値が強ければ、FRBの追加利上げ観測が戻りドル買い、弱ければ米金利低下とAI株安が重なり円買いに傾く。明日は米国が感謝祭で休場のため、今日のNY時間が週内最後の大きな山場。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>AUD/JPY 🇦🇺🇯🇵</h3>
        <p>4時間足デイトレ適性は1位（11/24時点、スコア83・最適、ADX53.1、方向は下降）。09:30の豪10月CPIは前年比+4.7%の予想で、前回+4.3%から加速する見込み。RBAは11月に利上げしたが、雇用の悪化で追加利上げには慎重な姿勢を示している。CPIが予想を上回れば利上げ観測が戻り豪ドル買い、下回れば下降トレンドに沿った豪ドル売り。昨日NY時間は105.47円前後で、AI株安の円買いとCPIの結果が同じ方向に重なると値幅が大きくなる。15分・30分足では発表直後の1本目の高値・安値を抜けた方向について行く。</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red,#c0392b)">HIGH</h3>
        <p>米株は2日続けて大きく振れた。23日はナスダック+6.75%、24日は午後2時台でナスダック-1.64%、半導体株指数-7.43%。今日は豪CPI、米PCE・GDP改定値・耐久財受注、ベージュブックが1日に集まる。明日26日は米感謝祭で休場、27日は短縮取引、30日は月末で、流動性が落ちる中で指標が出る。</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>9件</h3>
        <p>豪 CPI(09:30)、日 40年債入札(12:35)、米 ボウマンFRB副議長(21:25)、米 PCE・個人所得支出(22:30)、米 GDP改定値(22:30)、米 新規失業保険申請件数(22:30)、米 耐久財受注(22:30)、米 新築住宅販売(24:00)、米 ベージュブック(28:00)</p>
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
              <li>なし。明日11/26（木）は米国が感謝祭で株式・債券市場が休場、27日（金）は米国が短縮取引。米国勢は今日のNY時間を最後に実質的な連休に入る。</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>09:30 🇦🇺 豪 消費者物価指数（10月）前年比 予想+4.7%（○）</li>
              <li>12:35 🇯🇵 日 40年利付国債入札（○）</li>
              <li>21:25 🇺🇸 米 ボウマンFRB副議長 発言（投票権あり、AA）</li>
              <li>22:30 🇺🇸 米 個人所得・個人支出・PCEデフレーター（10月）コア前月比 予想+0.3%（S）</li>
              <li>22:30 🇺🇸 米 GDP改定値（第3四半期）予想+3.5%（AA）</li>
              <li>22:30 🇺🇸 米 新規失業保険申請件数 予想20.0万件（要確認）（AA）</li>
              <li>22:30 🇺🇸 米 耐久財受注（10月）（A）</li>
              <li>24:00 🇺🇸 米 新築住宅販売件数（10月）予想65.0万件（A）</li>
              <li>25:30 🇺🇸 米 7年債入札（A）／28:00 🇺🇸 米 ベージュブック（B）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>ドル円：159.60円の上値と158.75円の下値</strong>：昨日は東京で158.75円まで下げた後、日本株高で159.25円、ロンドンで159.60円付近まで上げた。米金利の低下で159.00円まで押し戻されたが、消費者信頼感の上振れで159.35円で引けた。15分・30分足で159.60円を上抜ければ160円に向けた上昇、159.00円を割れば158.75円まで下げ幅が広がる。160円に近づくと為替介入への警戒が強まり、上値は重くなる。</li>
              <li><strong>米国：PCEとGDPで追加利上げ観測を確認</strong>：PCEコア前月比が予想+0.3%を上回ると、FRBの12/9会合での追加利上げ観測が強まり米金利上昇・ドル買い。下回ればドル売り。21:25のボウマン副議長は発表前の発言で、物価への見方がドルの方向を先に決める。28:00のベージュブックは12月会合前の景気判断材料。</li>
              <li><strong>AI株と関税：円買いの火種</strong>：昨日は米国が補助金を理由に数十の国・地域への関税引き上げを準備していると伝わり、欧州株はDAX-1.26%で反落、米半導体株が大きく売られた。AI株安が続くと、円が安全資産として買われやすい。東京時間は日本株と半導体株の動きがクロス円の方向を左右する。</li>
              <li><strong>ユーロ：1.09ドル台で戻り</strong>：ユーロドルは23日安値1.0881ドルから1.0980ドルまで戻した。独Ifo企業景況感が90.6と予想90.5を上回ったことと、米金利低下によるドル売りが支え。1.10ドルが戻りの節目。ユーロ円は173.21円の安値から174.82円まで戻した。</li>
              <li><strong>原油：中東の攻撃で反発</strong>：リヤドの高層ビルへのフーシ派の攻撃と、ホルムズ海峡での船舶攻撃が伝わり、WTIは81.92ドル（+2.18%）。イランが米国との協議を除外すると報じられた。原油高は米インフレ懸念を通じて米金利を支え、資源国通貨のカナダドルにも買い材料。</li>
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
          <strong>米国株</strong>：11/24は午後2時台でダウ49,939.21ドル（+343.90ドル、+0.66%）、ナスダック23,550.70（-395.62、-1.64%）、S&amp;P500 7,204.13（-0.46%）、半導体株指数（SOX）8,875.41（-7.43%）と、ダウだけが上げる形で分かれた。欧州株はDAX-1.26%、FTSE100-0.13%、CAC40-0.05%と揃って下落。<strong>米国債利回り</strong>：午後2時台で10年債4.90%（前日比-0.04）、2年債4.68%（-0.01）。ロンドン時間に10年債は4.89%付近と2週間ぶりの低さ。<strong>ドル指数</strong>：103.80（-0.50%）。<strong>商品</strong>：WTIは81.92ドル（+1.75ドル、+2.18%）、金は3,584.00ドル（-2.65%）。<br><br><strong>政策金利（11/23確認値を継続）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。次回会合はRBA 12/8、FRB・RBNZ・BOC 12/9、SNB 12/10、ECB・BOE 12/17、日銀 12/18。<br><br><strong>今週の残り：</strong> 26日 米感謝祭休場・田村日銀審議委員の講演と会見・BOE金融安定報告・ECB議事要旨、27日 東京都区部CPI・米短縮取引、30日 月末。
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
              <td><strong>AUD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア83・最適。ADX53.1、5日ADR 96.3pips（5年比108%）、4H方向は下降。09:30の豪CPIが最初の材料で、AI株安の円買いとCPIの下振れが重なれば下降トレンドが続く。昨日NY時間は105.47円前後。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>GBP/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア79・適。ADX39.0、5日ADR 143.8pips、4H方向は下降。昨日は東京で207.00円台を下値に戻し、NY時間に208.58円前後。ポンドドルが1.3124ドルまで戻り、4Hの下降の中で戻りが入っている。値幅は最も大きい。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/JPY</strong><br><span style="color:var(--muted);font-size:12px;">スコア78・適。ADX32.7、5日ADR 119.6pips、4H方向は下降。23日の安値173.21円から昨日は174.82円まで戻した。ADXが低下しており、下降の勢いは弱まっている。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/USD</strong><br><span style="color:var(--muted);font-size:12px;">スコア74・適。ADX34.9、4H方向は下降。昨日は米金利低下で1.0953ドルから1.0980ドルまで上げて引けた。22:30の米PCE・GDPで方向が決まる。1.10ドルが戻りの節目。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">スコア70・適。ADX41.2、4H方向は下降。23日に約1年ぶり安値1.3011ドルを付けた後、昨日は1.3124ドルまで戻した。米指標次第で1.30ドルの節目を再び試す。</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4時間足ランキングは本日分が未更新のため、2026/11/24 13:21 JST生成分のスコアを使用し、11/24の値動きを踏まえて順位を調整した。スコア・ADX・ADRは候補選定の補助指標であり、売買推奨ではない。USD/JPYは11/24時点10位（スコア39・見送り、ADX16.9）。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（前営業日 2026-11-24 火）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック1】日本株高で円売り、ドル円は159.60円付近まで上昇</div>
            前日の米株高を受けて日経平均とアジアのハイテク株が上げ、リスクへの警戒が薄れて円が売られた。ドル円は東京午前に前日のドル高の反動で158.75円まで下げた後、午後に159.25円まで戻した。ロンドン時間は円売りが続き、一時159.60円付近まで上げた。ユーロ円は173.20円台から173.75円、ポンド円は207.00円台から207.70円台へ戻した。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック2】関税引き上げ報道でAI株が再び崩れ、米長期金利が2週間ぶり低水準</div>
            米国が中国・日本・EUなど数十の国・地域を対象に関税引き上げを準備していると伝わった。各国の産業補助金が過剰生産を生み、米製造業に損害を与えているとの理由。これでハイテク株への警戒が広がり、欧州株はDAX-1.26%で反落、米国は午後2時台でナスダック-1.64%、半導体株指数-7.43%と急落した。米国債が買われ、10年債利回りはロンドン時間に4.89%付近と2週間ぶりの低さまで下がった。ドルが売られ、ドル円は159.20円付近まで下げた。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック3】米住宅価格の伸び鈍化でドル売り、消費者信頼感の大幅上振れで下げ止まる</div>
            9月のケース・シラー20都市住宅価格は前年比+2.56%（予想+2.71%）、FHFA住宅価格指数は前月比0.0%（予想+0.2%）と、いずれも予想を下回った。米長期金利が下がり、ドル円は159.00円まで下落した。続く11月の消費者信頼感指数は103.3（予想92.4、前回91.9に上方修正）と約2年ぶりの高さで、現況指数は132.8、期待指数は83.6に上がった。ドル円は159.30円付近まで買い戻され、159.35円で引けた。リッチモンド連銀製造業指数も3（予想-2）と上振れ。5年債入札は最高落札利回り4.719%、応札倍率2.37倍で、需要は底堅かった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック4】ユーロとポンドが買い戻し、ドル指数は-0.50%</div>
            独11月Ifo企業景況感指数は90.6（予想90.5、前回90.1）と小幅に改善し、現況指数89.4、期待指数91.9も前回を上回った。発表直後のユーロの反応は小さかったが、米金利低下によるドル売りが続き、ユーロドルはNY時間に1.0953ドルから1.0980ドルまで上げて引けた。ユーロ円は174.30円から174.82円まで上昇。ポンドドルは1.3087ドルから1.3124ドルへ、ドルスイスは0.8384フランから0.8344フランへ下げた。ドル指数は午後2時台で103.80（-0.50%）と、23日の上げの半分近くを戻した。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック5】中東の攻撃で原油が反発、金は2.65%安</div>
            サウジアラビアの首都リヤドの金融地区にある高層ビルがフーシ派の攻撃を受け、11人が負傷した。ホルムズ海峡でも船舶への攻撃が続き、イランが米国との協議を除外すると報じられたことで、外交による解決への期待が後退した。WTIは81.92ドル（+1.75ドル、+2.18%）と反発。一方で金は3,584.00ドル（-97.70ドル、-2.65%）と大きく下げた。国内では、外為特会の剰余金ルールを緩め、消費税減税の財源として2兆円を確保する方針が伝わった。
          </div>
          <div class="handover">
            <strong>本日（11/25水）への引継ぎ：昨日は関税報道でAI株が崩れ、米金利低下でドルが売られたが、ドル円は消費者信頼感の上振れで159円台を保った。ユーロとポンドは戻りが入り、ドル高の流れは一服している。今日は09:30の豪CPIで豪ドル円、22:30の米PCE・GDP改定値でドル全体の方向が決まる。米指標が強ければドル円は159.60円を超えて160円が視野、弱ければ米金利低下とAI株安で158.75円割れ。明日の米感謝祭休場を前に、NY時間の指標後はポジション調整で値動きが荒くなりやすい。</strong>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間（24時以降は翌日11/26木）。冬時間のため米東部時間+14時間で換算。複数の情報で一致した値を掲載し、一致を確認できない項目・数値には「（要確認）」を付記。重要度は米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×。「低」は低重要度の参考指標。【発表済み】は本日0時〜7時に実施済みの項目。</p>
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
