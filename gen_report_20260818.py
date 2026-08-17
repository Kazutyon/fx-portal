import os

TODAY = '2026-08-18'
WEEKDAY = '火'

recent = sorted([f for f in os.listdir('reports') if f.endswith('.html')], reverse=True)[:10]
DAYS = {'0':'月','1':'火','2':'水','3':'木','4':'金','5':'土','6':'日'}
import datetime as dt
def label(fname):
    name = fname.replace('.html', '')
    d = dt.date.fromisoformat(name)
    return f'{name}（{DAYS[str(d.weekday())]}）'
sidebar_archive = '\n'.join(f'<li><a href="{f}">{label(f)}</a></li>' for f in recent)

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FX日報 2026-08-18（火） | AUXEN FX Portal</title>
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
  <h1>FX日報 2026-08-18（火）</h1>
  <p>前日はNY市場でドル円が159.32円から159.46円へ小反発。本日は15:00の英雇用統計、21:30の米住宅着工件数・建設許可件数に注目。</p>
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
        {sidebar_archive}
      </ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 2026-08-18（火）<span class="badge-live">最新</span></h2>
        <p class="sub">前日はNY市場でドル円が159.32円から159.46円へ小反発。本日は15:00の英雇用統計、21:30の米住宅着工件数・建設許可件数に注目。</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>2026-08-18</strong>
        <em>火曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>前日はドル円が159.46円まで小反発、本日は英雇用統計と米住宅指標に注目</h3>
        <p>8/17（月）のNY市場でドル円は159.32円から159.46円へ小幅上昇した。8月のNY連銀製造業景気指数や8月NAHB住宅市場指数（34→35）が予想に反して改善したことが手掛かりとなり、ドル買いが優勢となった（要確認）。一方で米国の他の経済指標は総じて弱めとなる中、ユーロドルは1.16台に乗せて上昇し、ポンドドルは5月以来の高値圏まで買われるなど、ドル円の底堅さとは対照的に対ユーロ・ポンドではドルの上値が重い展開もみられた。財務省が発表した6月分の対米証券投資（ネット長期フロー）は1,727億ドルの流入となり、米国への資金流入継続がドルの下支え材料となった。円については日本のファンダメンタルズ改善への思惑がある一方で円安圧力も根強く、方向感が定まらない綱引きが続いている（要確認）。本日8/18（火）は15:00発表の英雇用統計（失業率・失業保険申請件数・平均賃金指数）、21:30発表の米住宅着工件数・建設許可件数（ともにKissFXでAランク）が焦点となる。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>GBP/USD 🇬🇧🇺🇸</h3>
        <p>本日15:00発表の英雇用統計（失業保険申請件数はForexFactoryでHigh Impact）が最大の材料。4Hデイトレ適性ランキング2位（スコア48・ADX43.6で上昇トレンド継続）</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">MEDIUM</h3>
        <p>15:00の英雇用統計と21:30の米住宅着工件数・建設許可件数（Aランク）が重なる。米CPI・NFP級の単独最重要イベントはないが、複数の中〜高重要度指標が集中し値動きが出やすい</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>7件</h3>
        <p>英雇用統計 / 独・欧ZEW景況感調査 / 米住宅着工件数・建設許可件数 / 米輸入物価指数 / 米鉱工業生産・設備稼働率 等（本日の市場休場はなし）</p>
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
              <li>09:30 🇦🇺 ウエストパック消費者信頼感指数（要確認・KissFXとForexFactoryで表記相違、指数レベルと前月比の混在）</li>
              <li>15:00 🇬🇧 英雇用統計【失業率・失業保険申請件数・平均賃金指数】<span class="badge-important">★最重要</span>（失業保険申請件数はForexFactoryでHigh Impact、失業率は前回値がKissFX 4.4%／ForexFactory 4.9%で相違・要確認）</li>
              <li>18:00 🇩🇪🇪🇺 独/ユーロ圏ZEW景況感調査（独はKissFX・ForexFactory一致、ユーロ圏の予想値はForexFactoryのみ・要確認）</li>
              <li>21:15 🇨🇦 加住宅着工件数（KissFX・ForexFactoryほぼ一致）</li>
              <li>21:30 🇺🇸 米住宅着工件数・建設許可件数<span class="badge-important">★最重要</span>（KissFXランクA・ForexFactoryと一致）</li>
              <li>21:30 🇺🇸 米輸入物価指数（前月比）（KissFX・ForexFactory一致）</li>
              <li>22:15 🇺🇸 米鉱工業生産・設備稼働率（鉱工業生産はKissFX・ForexFactory一致、設備稼働率は要確認・ForexFactoryのみ）</li>
              <li>23:00 🇺🇸 米中古住宅販売保留（前月比）（KissFX・ForexFactoryで予想値に微差・要確認）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>NY市場でドル円が159.32円から159.46円へ小反発</strong>：米NY連銀製造業景気指数・NAHB住宅市場指数（34→35）の予想外の改善が手掛かりに（要確認）</li>
              <li><strong>ユーロドル・ポンドドルが対ドルで上昇</strong>：ユーロドルは1.16台、ポンドドルは5月以来の高値圏まで買われた</li>
              <li><strong>6月分の対米証券投資が1,727億ドルの流入</strong>：米国への資金流入継続がドルの下支え材料に</li>
              <li><strong>本日は英雇用統計と米住宅指標が焦点</strong>：GBPペア・USDペアともに結果次第で値動きが出やすい</li>
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
          8/18（火）は前日NY市場のドル円小反発（159.32→159.46円）を引き継ぎ、159円台後半での底堅い推移が続く見通し。前日はユーロ・ポンドが対ドルで上昇するなど、通貨ペアによってドルの強弱が分かれる展開だった。本日は15:00の英雇用統計、21:30の米住宅着工件数・建設許可件数（KissFXでAランク）が最大の焦点。18:00の独・ユーロ圏ZEW景況感調査も欧州通貨のセンチメントを左右しうる。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派・据え置き、7/29 9対3・3人が利上げ主張） / 日銀 1.00%（正常化継続、7/31据え置き） / 英BOE 3.75%（中立寄り、本日雇用統計に注目）
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
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング1位（スコア49・見送り）。ADX37.9で上昇トレンド継続、本日18:00の独・ユーロ圏ZEW景況感調査に注目</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング2位（スコア48・見送り）。ADX43.6で上昇トレンド継続、本日15:00の英雇用統計で方向感が定まりやすい</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/CAD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング3位（スコア47・見送り）。ADX35.1で下降トレンド継続、21:15の加住宅着工件数と21:30の米住宅指標が材料</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング4位（スコア36・見送り）。ADX26.4でレンジ、日本発の重要指標はなく21:30の米住宅指標待ち</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>NZD/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング5位（スコア35・見送り）。ADX24.3で上昇トレンド継続、23:50のGDT乳製品オークションにも注意</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日04:49 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-08-17）</h3>
          <span>月曜日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】NY市場でドル円が159円台後半まで小反発</div>
            8/17（月）のNY市場でドル円は159.32円から159.46円へ小幅上昇した。8月のNY連銀製造業景気指数や8月NAHB住宅市場指数（34→35）が予想に反して改善したことが手掛かりとなり、ドル買いが優勢となった（要確認）。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】ユーロ・ポンドは対ドルで上昇、ドル安が優勢な場面も</div>
            米国の他の経済指標は総じて弱めとなる中、ユーロドルは1.16台に乗せて上昇し、ポンドドルは5月以来の高値圏まで買われた。ドル円の底堅さとは対照的に、ドルは対ユーロ・ポンドでは上値の重い展開だった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】6月分の対米証券投資が1,727億ドルの流入</div>
            財務省が発表した6月分の対米証券投資（ネット長期フロー）は1,727億ドルの流入となり、米国への資金流入継続がドルの下支え材料となった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】円は方向感が定まらない展開</div>
            円については日本のファンダメンタルズ改善への思惑がある一方、円安圧力も根強く、相反する材料が綱引きする状況が続いている（要確認）。
          </div>
          <div class="handover">
            <strong>本日（8/18火）への引継ぎ：</strong>
            前日のドル円小反発（159.46円）とユーロ・ポンドの対ドル上昇を引き継ぎ、通貨ペアごとに強弱が分かれる展開を想定。本日は15:00の英雇用統計、21:30の米住宅着工件数・建設許可件数が焦点となり、結果次第でGBP・USDペアの方向感が定まりやすい。
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
            <tr><td><strong>終日</strong></td><td>🌍 主要国</td><td>本日、主要国の市場休場はなし</td><td>—</td><td>—</td><td>—</td></tr>
            <tr><td>05:00</td><td>🇺🇸 米国</td><td>対米証券投資（TICネット長期フロー）（要確認・ForexFactoryのみ）</td><td>低</td><td>151.4B</td><td>232.7B</td></tr>
            <tr><td>09:30</td><td>🇦🇺 豪州</td><td>ウエストパック消費者信頼感指数（要確認・KissFX指数レベル83.9とForexFactory前月比+4.1%で表記相違）</td><td>低</td><td>—</td><td>83.9（指数・KissFX）/+4.1%（前月比・FF）</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>平均賃金指数【3ヶ月/前年比】（要確認・ForexFactoryのみ）</td><td>★★</td><td>+4.0%</td><td>+4.3%</td></tr>
            <tr><td><strong>15:00</strong></td><td>🇬🇧 英国</td><td><strong>失業保険申請件数変化</strong>（KissFX・ForexFactoryで前回一致、予想はForexFactoryのみ・要確認）</td><td><strong>★★★</strong></td><td><strong>+16.5K（FF・要確認）</strong></td><td>+0.67万件</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>失業率（要確認・KissFX前回4.4%とForexFactory前回4.9%で相違、指標定義の差異の可能性）</td><td>★★</td><td>4.8%（FF）</td><td>4.4%（KissFX）/4.9%（FF）</td></tr>
            <tr><td>15:02</td><td>🇨🇳 中国</td><td>対内直接投資【年初来・前年比】（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>-5.0%</td></tr>
            <tr><td>18:00</td><td>🇩🇪 独</td><td>ZEW景況感調査（KissFX・ForexFactory一致）</td><td>★★</td><td>+30.0/+30.1</td><td>+26.3</td></tr>
            <tr><td>18:00</td><td>🇪🇺 ユーロ圏</td><td>ZEW景況感調査（要確認・予想値はForexFactoryのみ、前回値はKissFX・ForexFactory一致）</td><td>低</td><td>+25.9（FF）</td><td>+23.4</td></tr>
            <tr><td>18:33</td><td>🇬🇧 英国</td><td>10年債入札（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>利回り5.04%・応札倍率3.1倍</td></tr>
            <tr><td>21:15</td><td>🇨🇦 カナダ</td><td>住宅着工件数（KissFX・ForexFactoryほぼ一致）</td><td>低</td><td>25.00万件/249K</td><td>23.90万件/239K</td></tr>
            <tr><td>21:15</td><td>🇺🇸 米国</td><td>ADP週間雇用者数変化（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>+8.3K</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>住宅着工件数</strong>（KissFXランクA・ForexFactory一致）</td><td><strong>★★★</strong></td><td><strong>134.2万件/1.34M</strong></td><td>142.7万件/1.43M</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>建設許可件数</strong>（KissFXランクA・ForexFactory一致）</td><td><strong>★★★</strong></td><td><strong>137.5万件/1.37M</strong></td><td>136.7万件/1.37M</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>輸入物価指数（前月比）（KissFX・ForexFactory一致）</td><td>★★</td><td>+0.1%</td><td>+0.3%</td></tr>
            <tr><td>22:15</td><td>🇺🇸 米国</td><td>設備稼働率（要確認・ForexFactoryのみ）</td><td>低</td><td>76.3%</td><td>76.1%</td></tr>
            <tr><td>22:15</td><td>🇺🇸 米国</td><td>鉱工業生産（前月比）（KissFX・ForexFactory一致）</td><td>★★</td><td>+0.3%</td><td>+0.1%</td></tr>
            <tr><td>23:00</td><td>🇺🇸 米国</td><td>中古住宅販売保留（前月比）（KissFX・ForexFactoryで予想値に微差：KissFX±0.0%／FF+0.1%・要確認）</td><td>★★</td><td>±0.0%（KissFX）/+0.1%（FF）</td><td>-5.4%</td></tr>
            <tr><td>23:50</td><td>🇳🇿 NZ</td><td>GDT乳製品オークション価格指数（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>+0.1%</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または時刻・予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。本日の主要市場休場はありません。本日の焦点は15:00の英雇用統計と21:30の米住宅着工件数・建設許可件数です。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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
