TODAY = '2026-08-14'
WEEKDAY = '金'
HERO_SUMMARY = '米PPI・新規失業保険申請件数を通過しドル円は159.50円と小幅続伸で引け。本日は21:30の米小売売上高、23:00のミシガン大学消費者信頼感指数（速報）に関心が集まる。'

report_files_prev = ['2026-08-13', '2026-08-12', '2026-08-11', '2026-08-10', '2026-08-07', '2026-08-06', '2026-08-05', '2026-08-04', '2026-08-03', '2026-07-31']
DAYS = {'2026-08-13':'木','2026-08-12':'水','2026-08-11':'火','2026-08-10':'月','2026-08-07':'金','2026-08-06':'木','2026-08-05':'水','2026-08-04':'火','2026-08-03':'月','2026-07-31':'金'}
sidebar_archive = '\n'.join(f'<li><a href="{d}.html">{d}（{DAYS[d]}）</a></li>' for d in report_files_prev)

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
  <p>{HERO_SUMMARY}</p>
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
        <h2>FX日報 {TODAY}（{WEEKDAY}）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_SUMMARY}</p>
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
        <h3>米PPI・新規失業保険申請件数を通過後もドル円は方向感を欠き、159.50円で小幅続伸のまま引け</h3>
        <p>8/13（木）21:30発表の米7月生産者物価指数（PPI）は市場予想を下回り、インフレ鈍化を意識してやや売りが優勢となる場面があったが、明確な方向感を与えるには至らなかった（要確認）。同時刻発表の新規失業保険申請件数は1カ月ぶりの高水準となり、労働市場減速の兆しを示した。結果としてドル円はNY市場で159.50円と前営業日終値（159.42円）から8銭程度のドル高にとどまり、小幅続伸で引けた。欧州株式市場は米・イラン交渉の膠着を背景に投資家心理が悪化し続落（要確認）。英国では経済成長指標は底堅かったものの個人消費の鈍化が示され、英中銀（BOE）の追加利上げ観測が後退する契機となった（要確認）。本日8/14（金）は21:30の米小売売上高、23:00のミシガン大学消費者信頼感指数（速報値）に関心が集まる。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>159円台後半での小幅続伸基調を引き継ぐ中、本日21:30の米小売売上高・23:00のミシガン大学消費者信頼感指数の結果次第で方向感が定まりやすい</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">MEDIUM</h3>
        <p>21:30の米小売売上高（除自動車）と23:00のミシガン大学消費者信頼感指数（速報）が重なる。単独最重要級のイベントはないが、米指標が集中し値動きが大きくなりやすい</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>6件</h3>
        <p>米小売売上高 / 米小売売上高(除自動車) / 米ミシガン大学消費者信頼感指数(速報) / 豪RBA総裁発言 / 仏CPI改定値 / 欧GDP改定値 等（本日の市場休場はなし）</p>
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
              <li>07:30 🇳🇿 製造業PMI（BusinessNZ）（KissFX・ForexFactory一致）</li>
              <li>08:30 🇦🇺 RBA総裁ブロック(Bullock)氏発言（KissFX・ForexFactory一致）</li>
              <li>15:45 🇫🇷 消費者物価指数改定値（前月比・前年比）（前月比はKissFX・ForexFactory一致、前年比はKissFXのみ・要確認）</li>
              <li>18:00 🇪🇺 ユーロ圏GDP改定値（Q2、前期比・前年比）（前期比はKissFX・ForexFactory一致、前年比はKissFXのみ・要確認）</li>
              <li>21:30 🇨🇦 卸売売上高・製造業出荷（KissFX・ForexFactory一致）</li>
              <li>21:30 🇺🇸 小売売上高<span class="badge-important">★最重要</span>（KissFX・ForexFactory一致・重要度表記に差あり要確認）</li>
              <li>21:30 🇺🇸 小売売上高（除自動車）<span class="badge-important">★最重要</span>（KissFX・ForexFactory一致・重要度表記に差あり要確認）</li>
              <li>23:00 🇺🇸 ミシガン大学消費者信頼感指数【速報値】<span class="badge-important">★最重要</span>（予想・前回値がソース間で相違・要確認）</li>
              <li>23:00 🇺🇸 企業在庫（予想値がソース間で軽微な差異・要確認）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>米PPI・新規失業保険申請件数通過も方向感欠き、ドル円は159.50円で小幅続伸</strong>：PPIは市場予想を下回りやや売りが優勢な場面があったが方向感を与えず、新規失業保険申請件数は1カ月ぶりの高水準（要確認）</li>
              <li><strong>欧州株が続落、米・イラン交渉の膠着でリスク回避</strong>：投資家心理が悪化し売却圧力が発生（要確認）</li>
              <li><strong>英GDP統計は底堅いが個人消費鈍化、BOE利上げ観測が後退</strong>：追加利上げ観測が後退する契機に（要確認）</li>
              <li><strong>円買い介入より継続的な金融引き締めペースが重要との指摘</strong>：日銀の散発的介入よりも引き締めペースが円回復の鍵との見方（要確認）</li>
              <li><strong>ユーロドル、FRB利上げ見送りなら上昇シナリオが意識される</strong>：強気派が忍耐強く待つ局面との指摘（要確認）</li>
              <li><strong>本日は21:30の米小売売上高・23:00のミシガン大学消費者信頼感指数が焦点</strong>：週末を控え、米消費動向を見極める材料として関心が集まる</li>
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
          8/14（金）は前日NY市場でドル円が米PPI・新規失業保険申請件数を通過するも明確な方向感を欠き、159.50円で小幅続伸にとどまった流れを引き継いでスタート。欧州株の続落や英GDP統計を受けたBOE利上げ観測の後退も材料視されたが、いずれも次の方向感を決定づける材料には至っていない（要確認）。本日は21:30の米小売売上高（除自動車）、23:00のミシガン大学消費者信頼感指数（速報）が重なり、週末を控えた米消費動向の確認材料として値動きが大きくなりやすい。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派・据え置き、7/29 9対3・3人が利上げ主張） / 日銀 1.00%（正常化継続、7/31据え置き） / 英BOE 3.75%（中立寄り、7/30据え置き）
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
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング1位（スコア47・見送り）。前日の小幅続伸基調を引き継ぎつつ、本日21:30の米小売売上高で方向感が定まりやすい</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング2位（スコア42・見送り）。ADX16.4で上昇トレンド継続、英GDP通過後の流れを引き継ぐ</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング3位（スコア41・見送り）。ADX36.2とトレンド強めだが方向はレンジ判定、米小売売上高の結果次第で振れやすい</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/CAD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング4位（スコア36・見送り）。ADX20.8で下降トレンド継続、本日21:30の加卸売売上高・製造業出荷にも注意</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング5位（スコア36・見送り）。本日18:00の欧GDP改定値を控え上昇トレンド継続</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日05:03 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-08-13）</h3>
          <span>昨日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】米PPI・新規失業保険申請件数を通過も方向感欠き、ドル円は159.50円で小幅続伸</div>
            21:30発表の米7月生産者物価指数（PPI）は市場予想を下回り、インフレ鈍化を意識してやや売りが優勢となる場面があったが、明確な方向感を与えるには至らなかった（要確認）。同時刻発表の新規失業保険申請件数は1カ月ぶりの高水準となり労働市場減速の兆しを示した。結果としてドル円はNY市場で159.50円と前営業日終値（159.42円）から8銭程度のドル高にとどまり、小幅続伸で引けた。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】欧州株が続落、米・イラン交渉の膠着でリスク回避</div>
            米国とイランの交渉が膠着状態にあることを背景に投資家心理が悪化し、欧州主要株式指数が続落。売却圧力がリスクセンチメントに波及した（要確認）。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】英GDP統計は底堅いが個人消費鈍化、BOE利上げ観測が後退</div>
            英国の経済成長指標は底堅い内容だったが個人消費の伸びが鈍化。これを受けて英中銀（BOE）の追加利上げ観測が後退する契機となった（要確認）。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】円買い介入より継続的な金融引き締めペースが重要との指摘</div>
            市場では日銀による散発的な為替介入よりも、継続的な金融引き締めペースの方が円相場の回復にとって重要との見方が示された（要確認）。
          </div>
          <div class="handover">
            <strong>本日（8/14金）への引継ぎ：</strong>
            前日NY市場でのドル円の小幅続伸（159.50円）を引き継ぎ、米PPI・新規失業保険申請件数通過後も明確な方向感は出ていない。欧州株続落や英BOE利上げ観測の後退も材料視されたが次の方向感を決定づける材料には至らず（要確認）、本日は21:30の米小売売上高・23:00のミシガン大学消費者信頼感指数（速報）の結果が焦点となる。
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
            <tr><td>02:01</td><td>🇺🇸 米国</td><td>30年債入札（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>利回り5.06%/応札倍率2.4倍</td></tr>
            <tr><td>07:00</td><td>🇺🇸 米国</td><td>グールズビーFOMC委員発言（要確認・ForexFactoryのみ）</td><td>低</td><td>要人発言</td><td>—</td></tr>
            <tr><td>07:30</td><td>🇳🇿 NZ</td><td>製造業PMI（BusinessNZ）（KissFX・ForexFactory一致）</td><td>—</td><td>—</td><td>59.7</td></tr>
            <tr><td>07:45</td><td>🇳🇿 NZ</td><td>入国者数（前月比）（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>-2.4%</td></tr>
            <tr><td>08:30</td><td>🇦🇺 豪州</td><td>RBA総裁ブロック(Bullock)氏発言（KissFX・ForexFactory一致）</td><td>★★</td><td>要人発言</td><td>—</td></tr>
            <tr><td>15:00</td><td>🇪🇺 ユーロ圏</td><td>独卸売物価指数（前月比）（要確認・ForexFactoryのみ）</td><td>低</td><td>-0.2%</td><td>-0.7%</td></tr>
            <tr><td>15:02</td><td>🇨🇳 中国</td><td>対中直接投資（年初来・前年比）（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>-5.0%</td></tr>
            <tr><td>15:45</td><td>🇫🇷 フランス</td><td>消費者物価指数改定値（前月比）（KissFX・ForexFactory一致）</td><td>—</td><td>+0.6%</td><td>+0.6%</td></tr>
            <tr><td>15:45</td><td>🇫🇷 フランス</td><td>消費者物価指数改定値（前年比）（要確認・KissFXのみ）</td><td>—</td><td>+2.1%</td><td>+2.1%</td></tr>
            <tr><td><strong>18:00</strong></td><td>🇪🇺 ユーロ圏</td><td><strong>GDP改定値（Q2、前期比）</strong>（KissFX・ForexFactory一致）</td><td><strong>—</strong></td><td><strong>+0.4%</strong></td><td>+0.4%</td></tr>
            <tr><td>18:00</td><td>🇪🇺 ユーロ圏</td><td>GDP改定値（Q2、前年比）（要確認・KissFXのみ）</td><td>—</td><td>+1.0%</td><td>+1.0%</td></tr>
            <tr><td>18:00</td><td>🇪🇺 ユーロ圏</td><td>雇用者数変化（改定値・前期比）（要確認・ForexFactoryのみ）</td><td>低</td><td>+0.1%</td><td>+0.1%</td></tr>
            <tr><td>18:00</td><td>🇪🇺 ユーロ圏</td><td>貿易収支（KissFXとForexFactoryで数値が大きく相違・要確認）</td><td>—</td><td>-78億（KissFX）/-22億（FF）</td><td>-50億</td></tr>
            <tr><td>18:03</td><td>🇨🇳 中国</td><td>マネーサプライM2（前年比）（要確認・ForexFactoryのみ）</td><td>低</td><td>+7.9%</td><td>+8.0%</td></tr>
            <tr><td>18:03</td><td>🇨🇳 中国</td><td>新規融資（要確認・ForexFactoryのみ）</td><td>低</td><td>-500億元</td><td>1兆610億元</td></tr>
            <tr><td>21:30</td><td>🇨🇦 カナダ</td><td>卸売売上高（KissFX・ForexFactory一致）</td><td>—</td><td>+2.7%</td><td>±0.0%</td></tr>
            <tr><td>21:30</td><td>🇨🇦 カナダ</td><td>製造業出荷（KissFX・ForexFactory一致）</td><td>—</td><td>-0.1%</td><td>+1.3%</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>小売売上高</strong>（KissFX・ForexFactory一致・重要度表記に差あり要確認）</td><td><strong>KissFX最高／FF中</strong></td><td><strong>+0.1%</strong></td><td>+0.2%</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>小売売上高（除自動車）</strong>（KissFX・ForexFactory一致・重要度表記に差あり要確認）</td><td><strong>KissFX最高／FF中</strong></td><td><strong>+0.2%</strong></td><td>-0.2%</td></tr>
            <tr><td><strong>23:00</strong></td><td>🇺🇸 米国</td><td><strong>ミシガン大学消費者信頼感指数【速報値】</strong>（予想・前回値がソース間で相違・要確認）</td><td><strong>KissFX最高／FF中</strong></td><td><strong>54.9（KissFX）/54.7（FF）</strong></td><td>55.2（KissFX）/54.4（FF）</td></tr>
            <tr><td>23:00</td><td>🇺🇸 米国</td><td>企業在庫（予想値がソース間で軽微な差異・要確認）</td><td>—</td><td>+0.1%（KissFX）/+0.2%（FF）</td><td>+0.3%</td></tr>
            <tr><td>23:00</td><td>🇺🇸 米国</td><td>ミシガン大学期待インフレ率【速報値】（要確認・ForexFactoryのみ）</td><td>中</td><td>—</td><td>4.2%</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。本日の主要市場休場はありません。本日の焦点は21:30の米小売売上高と23:00のミシガン大学消費者信頼感指数（速報）です。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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
