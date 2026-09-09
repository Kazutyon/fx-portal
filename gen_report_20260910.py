import json
from datetime import datetime

TODAY = '2026-09-10'
WEEKDAY = '木'

HERO_SUB = (
    '前日9/9（木）はドル円が5日続落し153円56銭で引けた（前営業日153円98銭比42銭のドル安）。'
    '日中は円買いが加速し一時152円09銭まで下落する場面があったが、米財務省が最大60億ドルの'
    '長期国債買い戻しを発表したことと、米10年債入札が最高落札利回り4.834%・応札倍率2.71倍と'
    '好調な結果になったことでドルが買い戻された。本日9/10（木）は21:15のECB政策金利発表（0.25%'
    '利上げの2.65%へ観測）と21:30の米PPI・新規失業保険申請件数が最大の焦点。'
)

MARKET_HOLIDAY_H3 = '休場市場なし'
MARKET_HOLIDAY_P = '本日、主要国の市場休場は確認されていません（KissFX・gaitame.com等で確認）。'

KEY_EVENTS_ITEMS = [
    '10:30 🇯🇵 日銀審議委員 挨拶・記者会見（要確認）',
    '21:15 🇪🇺 ECB政策金利発表（0.25%利上げ→2.65%予想）',
    '21:30 🇺🇸 生産者物価指数(PPI)【前月比/前年比】',
    '21:30 🇺🇸 新規失業保険申請件数',
    '21:45 🇪🇺 ECB ラガルド総裁 記者会見',
    '23:00 🇺🇸 中古住宅販売件数',
]

REPORT_SUMMARY = '米国債買戻し発表と好調な10年債入札でドル反発、本日はECB利上げ発表とPPIに注目'
RISK_LEVEL = 'HIGH'

# 政策金利（火〜金は前日の値を引き継ぎ）
FRB_RATE = '3.50–3.75%'
FRB_STANCE = 'タカ派（9/15-16FOMCに向け利上げ観測強まるも一部高官は慎重・要確認）'
BOE_RATE = '3.75%'
BOE_STANCE = '中立〜やや引き締め警戒（7/30据え置き・次回9/17）'
BOJ_RATE = '1.00%'
BOJ_STANCE = '正常化継続・タカ派寄り（植田総裁・氷見野副総裁発言で9月利上げ観測強まる・次回9/17-18、今月1.25%程度への利上げ方針との報道あり・要確認）'
ECB_RATE = '2.25%'
ECB_STANCE = 'タカ派（預金ファシリティ金利、本日9/10理事会で0.25%利上げ観測・要確認）'
RBA_RATE = '4.35%'
RBA_STANCE = 'タカ派（8/11据え置き、トリム平均インフレ3.6%高止まりで再利上げ余地）'
RBNZ_RATE = '2.75%'
RBNZ_STANCE = 'タカ派（9/2会合で2.50%→2.75%へ利上げ、2会合連続）'
BOC_RATE = '2.25%'
BOC_STANCE = '中立だが引き締めバイアス（9/2会合で7会合連続据え置き）'
SNB_RATE = '0.00%'
SNB_STANCE = '中立（複数会合連続で据え置き・次回9/24または9/25・要確認）'

with open('data/daytrade-ranking.json', encoding='utf-8') as f:
    payload = json.load(f)
rankings = payload['rankings']
generated_at = datetime.fromisoformat(payload['generated_at_jst'])
RANKING_UPDATED = generated_at.strftime('%Y-%m-%d %H:%M')

RANK_BADGE = {1: 'rank-a', 2: 'rank-a', 3: 'rank-a', 4: 'rank-a'}
DIR_ARROW = {'上昇': ('trend-up', '↑'), '下降': ('trend-down', '↓'), 'レンジ': ('trend-range', '→')}

def ranking_row(item):
    badge = RANK_BADGE.get(item['rank'], 'rank-b')
    arrow_class, arrow = DIR_ARROW.get(item['direction'], ('trend-range', '→'))
    return f'''            <tr>
              <td><span class="rank-badge {badge}">{'A' if badge == 'rank-a' else 'B'}</span></td>
              <td><strong>{item['pair']}</strong><br><span style="color:var(--muted);font-size:12px;">ランキング{item['rank']}位（スコア{item['score']}・{item['verdict']}）。ADX{item['adx_h4']:.1f}で{'非常に強い' if item['adx_h4'] >= 50 else '強い' if item['adx_h4'] >= 25 else 'やや弱い'}{item['direction']}トレンド、直近5日ADRは5年平均の{item['adr_ratio_pct']:.1f}%</span></td>
              <td><span class="{arrow_class}">{arrow}</span></td>
            </tr>'''

RANKING_ROWS_HTML = '\n'.join(ranking_row(item) for item in rankings[:5])

CALENDAR_ROWS = [
    ('05:30', '🇺🇸 米', 'API週間統計速報（ForexFactoryのみ・要確認）', '低', '—', '—'),
    ('08:01', '🇬🇧 英', 'RICS住宅価格指数（KissFX・ForexFactory一致）', '中', '-30〜-31%', '-30%'),
    ('10:00', '🇦🇺 豪', 'メルボルン統計局 インフレ期待（ForexFactoryのみ・要確認）', '低', '—', '4.9%'),
    ('10:15', '🇺🇸 米', 'トランプ大統領発言（ForexFactoryのみ・要確認）', '中', '—', '—'),
    ('<strong>10:30</strong>', '🇯🇵 日', '<strong>日銀審議委員 挨拶（KissFXのみ・要確認）</strong> <span class="badge-important">★重要</span>', '高', '要人発言', '—'),
    ('未定', '🇯🇵 日', '日銀審議委員 記者会見（KissFXのみ・要確認）', '高', '要人発言', '—'),
    ('15:00', '🇩🇪 独', '消費者物価指数【改定値・前月比/前年比】（KissFX・ForexFactory一致）', '低〜中', '+0.2%/+2.9%', '+0.2%/+2.9%'),
    ('17:00', '🇮🇹 伊', '鉱工業生産【前月比】（ForexFactoryのみ・要確認）', '低', '+0.3%', '-1.0%'),
    ('20:00', '🇹🇷 土', 'トルコ中銀（TCMB）政策金利（KissFXのみ・要確認）', '高', '37.00%据え置き', '37.00%'),
    ('<strong>21:15</strong>', '🇪🇺 欧', '<strong>ECB政策金利発表（KissFX・ForexFactory一致）</strong> <span class="badge-important">★重要</span>', '最高', '0.25%利上げ→2.65%（主要リファイナンス金利）', '2.40%'),
    ('21:30', '🇺🇸 米', '新規失業保険申請件数（KissFX・ForexFactory一致）', '高', '20.5万件', '20.6万件'),
    ('<strong>21:30</strong>', '🇺🇸 米', '<strong>生産者物価指数(PPI)【前月比/前年比】（KissFX・ForexFactory一致）</strong> <span class="badge-important">★重要</span>', '最高', '+0.4%/+5.3%', '±0.0%/+4.7%'),
    ('21:45', '🇪🇺 欧', 'ECB ラガルド総裁 記者会見（KissFX・ForexFactory一致）', '高', '要人発言', '—'),
    ('23:00', '🇺🇸 米', '中古住宅販売件数（KissFX・ForexFactory一致）', '高', '398万件', '406万件'),
    ('23:00', '🇺🇸 米', '卸売在庫【改定値・前月比】（ForexFactoryのみ・要確認）', '低', '+1.2%', '+1.3%'),
    ('23:30', '🇺🇸 米', '天然ガス在庫（ForexFactoryのみ・要確認）', '低', '+35B', '+30B'),
    ('翌01:00', '🇺🇸 米', '週間原油在庫（KissFXのみ・要確認）', '中', '—', '-445.0万'),
    ('翌02:00', '🇺🇸 米', '30年債入札（発行予定額220億ドル）（KissFXのみ・要確認）', '中', '220億ドル', '—'),
]

CALENDAR_ROWS_HTML = '\n'.join(
    f'            <tr><td>{t}</td><td>{c}</td><td>{n}</td><td>{imp}</td><td>{fc}</td><td>{pv}</td></tr>'
    for t, c, n, imp, fc, pv in CALENDAR_ROWS
)

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
<li><a href="2026-09-09.html">2026-09-09（水）</a></li>
<li><a href="2026-09-08.html">2026-09-08（火）</a></li>
<li><a href="2026-09-07.html">2026-09-07（月）</a></li>
<li><a href="2026-09-04.html">2026-09-04（金）</a></li>
<li><a href="2026-09-03.html">2026-09-03（木）</a></li>
<li><a href="2026-09-02.html">2026-09-02（水）</a></li>
<li><a href="2026-09-01.html">2026-09-01（火）</a></li>
<li><a href="2026-08-31.html">2026-08-31（月）</a></li>
<li><a href="2026-08-28.html">2026-08-28（金）</a></li>
<li><a href="2026-08-27.html">2026-08-27（木）</a></li>
      </ul>
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
        <em>木曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{REPORT_SUMMARY}</h3>
        <p>前日9/9（木）はニューヨーク市場でドル円が5日続落となり153円56銭で引けた（前営業日153円98銭比で42銭のドル安）。日中は円買いの流れが継続し一時152円09銭まで下落する場面があったが、米財務省が最大60億ドルの長期国債買い戻しプログラムを発表したことをきっかけにドルが買い戻され、153円80銭台まで反発する場面もみられた。同日実施された米10年債入札は最高落札利回り4.834%・応札倍率2.71倍と好調な結果となり、国債需給への不安がやや後退したこともドル買い戻しを支えた。株式市場ではダウ平均が一時310ドル安となったほか、欧州株は主要指数が揃って大幅下落して引けており、リスク回避の動きも観測された。トランプ大統領は「中間選挙後にガソリン価格を2ドルへ引き下げる」との趣旨の発言をしたと報じられている（要確認）。本日9/10（木）は21:15にECBが政策金利を発表し、主要リファイナンス金利を0.25%引き上げ2.65%とする観測が強い（要確認）ほか、21:45のラガルド総裁記者会見、21:30の米PPI・新規失業保険申請件数と重要指標が集中する一日になる。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>EUR/USD 🇪🇺🇺🇸</h3>
        <p>本日21:15のECB政策金利発表（0.25%利上げで2.65%へとの観測・要確認）と21:45のラガルド総裁記者会見が最大の焦点。声明文のトーン次第でユーロが大きく動く可能性がある。4Hデイトレ適性ランキングでは対象外だが、本日はイベントドリブンでの値動きに要警戒。</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red,#c0392b)">HIGH</h3>
        <p>本日はECB政策金利発表・記者会見に加え、米PPI・新規失業保険申請件数など米国発の高重要度指標も21時台に集中する。前日は米国債買い戻し発表と好調な10年債入札でドルが乱高下しており、金利イベントへの反応が大きくなりやすい一日。</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>18件</h3>
        <p>ECB政策金利発表 / ラガルド総裁会見 / 米PPI / 米新規失業保険申請件数 等（本日の市場休場はなし）</p>
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
              <li>本日、主要国の市場休場はなし（前日9/9も休場はありませんでした）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>10:30 🇯🇵 日銀審議委員 挨拶・記者会見（要確認）</li>
              <li>20:00 🇹🇷 トルコ中銀（TCMB）政策金利（37.00%据え置き予想）</li>
              <li>21:15 🇪🇺 ECB政策金利発表（0.25%利上げ→2.65%予想）</li>
              <li>21:30 🇺🇸 生産者物価指数(PPI)【前月比/前年比】</li>
              <li>21:30 🇺🇸 新規失業保険申請件数</li>
              <li>21:45 🇪🇺 ECB ラガルド総裁 記者会見</li>
              <li>23:00 🇺🇸 中古住宅販売件数</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>ドル円が5日続落も米国債買い戻し発表で下げ渋る</strong>：前日9/9はNY市場でドル円が5日続落となり153円56銭で引けた（前営業日比42銭のドル安）。日中は一時152円09銭まで下落したが、米財務省の長期国債買い戻しプログラム発表をきっかけに153円80銭台まで反発する場面もあった。</li>
              <li><strong>米10年債入札は好調、利回り4.834%・応札倍率2.71倍</strong>：米財務省が最大60億ドルの長期国債買い戻しを発表したのに続き実施された10年債入札は、最高落札利回り4.834%・応札倍率2.71倍と需要が強く、国債需給不安の後退がドルの下支え材料となった。</li>
              <li><strong>米欧株式が揃って下落</strong>：NY市場ではダウ平均が一時310ドル安となる場面があったほか、欧州の主要株価指数は軒並み大幅安で引けており、リスク回避的な地合いも観測された。</li>
              <li><strong>本日21:15にECB政策金利発表、0.25%利上げ観測（要確認）</strong>：ECBは本日の理事会で主要リファイナンス金利を現行2.40%から2.65%へ0.25%引き上げるとの観測が強い（預金ファシリティ金利は2.25%→2.50%が想定・要確認）。21:45のラガルド総裁会見でのフォワードガイダンスにも注目。</li>
              <li><strong>トランプ大統領「中間選挙後にガソリン価格2ドルへ」と発言（要確認）</strong>：トランプ米大統領が中間選挙後にガソリン価格を2ドルへ引き下げる方針を示唆したと報じられているが、詳細な文脈・実現可能性は確認できていない（要確認）。</li>
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
          前日9/9（木）はニューヨーク市場でドル円が5日続落となり153円56銭で引けた（前営業日比42銭のドル安）。日中は円買いの流れで一時152円09銭まで下落したが、米財務省の長期国債買い戻しプログラム発表と好調な米10年債入札（利回り4.834%・応札倍率2.71倍）を受けてドルが買い戻された。米欧株式は揃って下落しリスク回避的な地合いもみられた。本日9/10（木）は21:15のECB政策金利発表（0.25%利上げ観測・要確認）と21:30の米PPI・新規失業保険申請件数が最大の焦点で、重要指標が21時台に集中する一日となる。<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派、9/15-16FOMCに向け利上げ観測強まるも一部高官は慎重・要確認） / 日銀 1.00%（正常化継続・タカ派寄り、9月利上げ観測強まる・次回9/17-18、今月1.25%程度への利上げ方針との報道あり・要確認） / 欧ECB 2.25%（預金ファシリティ金利。タカ派、本日理事会で0.25%利上げ観測・要確認）
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
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは{RANKING_UPDATED} JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。本日はECB・米PPI等の指標イベントが集中するため、通常のトレンドフォローに加えイベント通過後の値動きにも注意してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-09-09）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック1】ドル円が5日続落、153円56銭で引ける</div>
            前日9/9（木）はNY市場でドル円が5日続落となり153円56銭で引けた（前営業日153円98銭比で42銭のドル安）。日中は円買いの流れが継続し一時152円09銭まで下落する場面があった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック2】米財務省が長期国債買い戻しプログラムを発表、ドル買い戻しの契機に</div>
            米財務省が最大60億ドルの長期国債買い戻しプログラムを発表。国債需給の不安が和らいだことをきっかけにドルが買い戻され、153円80銭台まで反発する場面もみられた。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック3】米10年債入札は好調、利回り4.834%・応札倍率2.71倍</div>
            米10年債入札は最高落札利回り4.834%・応札倍率2.71倍と需要が強く、国債消化への安心感がドルの下支え材料となった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック4】米欧株式が揃って下落</div>
            NY市場ではダウ平均が一時310ドル安となる場面があったほか、欧州の主要株価指数も軒並み大幅安で引けており、リスク回避的な地合いも観測された。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック5】ECB理事会を翌日に控え商いが手控えられる</div>
            本日9/10のECB理事会を控え、ユーロは方向感の乏しい値動きとなった。市場では今回0.25%利上げの後、しばらく利上げを見送るとの見方も出ている（要確認）。
          </div>
          <div class="handover">
            <strong>本日（9/10木）への引継ぎ：前日はドル円が円買い先行から米国債買い戻し発表・好調な10年債入札を受けて下げ渋り153円56銭で引けた（5日続落）。米欧株式は揃って下落しリスク回避的な地合いもみられた。本日は21:15のECB政策金利発表と21:30の米PPI・新規失業保険申請件数が最大の焦点。ECBが0.25%利上げした場合の声明トーン、米PPI次第でドル円・ユーロドルとも値動きが大きくなりやすい点に留意したい。</strong>
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
{CALENDAR_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標には「（要確認）」を付しています。本日は主要国の市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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

with open('reports/2026-09-10.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('reports/2026-09-10.html generated')
