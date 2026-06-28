#!/usr/bin/env python3
"""Generate FX daily report for 2026-06-29 (Monday)"""
import os, glob

TODAY = '2026-06-29'
WEEKDAY = '月'
WEEKDAY_LABEL = '月曜日'
PREV_DATE = '2026-06-26'

report_files = sorted(glob.glob('reports/*.html'), reverse=True)
DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

def make_sidebar_archive(files):
    items = ''
    all_files = [f'reports/{TODAY}.html'] + [f for f in files]
    for i, f in enumerate(all_files[:10]):
        href = f.replace(os.sep, '/')
        name = os.path.basename(f).replace('.html','')
        try:
            import datetime
            d = datetime.date.fromisoformat(name)
            wd = DAYS[d.strftime('%A')]
            label = f'{name}（{wd}）'
        except Exception:
            label = name
        active = ' class="active"' if i == 0 else ''
        items += f'<li{active}><a href="{href}">{label}</a></li>\n'
    return items

SIDEBAR_ARCHIVE = make_sidebar_archive(report_files)

html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FX日報 2026-06-29（月） | AUXEN FX Portal</title>
<link rel="stylesheet" href="../style.css">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../assets/logo.svg">
<script data-goatcounter="https://auxen.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="https://cdn.jsdelivr.net/npm/twemoji@14.0.2/dist/twemoji.min.js" crossorigin="anonymous"></script>
<script>document.addEventListener('DOMContentLoaded',function(){twemoji.parse(document.body,{folder:'svg',ext:'.svg',base:'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/'});});</script>
</head>
<body class="report-page">

<header class="mobile-header">
  <a href="../index.html" class="mobile-brand">
    <img src="../assets/logo.svg" alt="AUXEN">
    <span><strong>AUXEN</strong><em>FX Research Lab</em></span>
  </a>
  <a href="#report-menu" class="mobile-menu-button" aria-label="日報メニュー">
    <span></span><span></span><span></span>
  </a>
</header>

<section class="mobile-report-hero">
  <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
  <h1>FX日報 2026-06-29（月）</h1>
  <p>Q2末・月末リバランス先行。東京CPI結果引き継ぎ、USD/JPY 161円台の攻防へ。</p>
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

  <!-- ── Sidebar ── -->
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
      <a href="#"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/><circle cx="8" cy="6" r="2"/><circle cx="17" cy="12" r="2"/><circle cx="11" cy="18" r="2"/></svg>インジケーター</a>
      <a href="#"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="1"/><line x1="9" y1="7" x2="9" y2="4"/><line x1="12" y1="7" x2="12" y2="4"/><line x1="15" y1="7" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="17"/><line x1="12" y1="20" x2="12" y2="17"/><line x1="15" y1="20" x2="15" y2="17"/><line x1="4" y1="9" x2="7" y2="9"/><line x1="4" y1="12" x2="7" y2="12"/><line x1="4" y1="15" x2="7" y2="15"/><line x1="17" y1="9" x2="20" y2="9"/><line x1="17" y1="12" x2="20" y2="12"/><line x1="17" y1="15" x2="20" y2="15"/></svg>EA</a>
      <span class="nav-section">サイト情報</span>
      <a href="../about.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>About</a>
      <a href="../disclaimer.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>免責事項</a>
      <a href="../contact.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>お問い合わせ</a>
    </nav>

    <div style="margin-top:28px; padding-top:20px; border-top:1px solid var(--line);">
      <p style="font-size:11px;color:var(--muted);margin:0 0 10px;letter-spacing:.06em;text-transform:uppercase;">過去のレポート</p>
      <ul class="archive-list">
""" + SIDEBAR_ARCHIVE + """      </ul>
    </div>
  </aside>

  <!-- ── Main ── -->
  <main class="main">

    <!-- Hero -->
    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 2026-06-29（月）<span class="badge-live">最新</span></h2>
        <p class="sub">Q2末・月末リバランス先行——日本雇用・独CPI速報・未決住宅販売がドル円と欧州通貨の方向性を左右する週明け。</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>2026-06-29</strong>
        <em>月曜日</em>
      </div>
    </header>

    <!-- Summary cards -->
    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>USD/JPY 161円台 Q2末攻防</h3>
        <p>PCE・東京CPI消化後、Q2末リバランスで機関投資家フローが方向性を決める。161.50±を軸に上下を確認。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>Q2末の機関投資家リバランスと月末固定仲値需要が方向性を左右</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--orange)">MEDIUM</h3>
        <p>Q2末フロー・月末調整。独CPI速報（21:00）次第でEUR大きく動く</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>5件</h3>
        <p>日本雇用統計 / 鉱工業生産 / 中国PMI / 独CPI速報 / 未決住宅販売</p>
      </div>
    </div>

    <!-- Content grid -->
    <div class="content-grid">

      <!-- 注目ポイント -->
      <div class="panel" id="points">
        <div class="panel-head">
          <h3>⚔️ 今日の注目ポイント</h3>
          <span>経済指標・イベント</span>
        </div>
        <div class="report-body">
          <div class="points-block">
            <div class="block-title">🚫 本日の市場休場</div>
            <ul class="points-list">
              <li>なし（全主要市場は通常営業）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>08:30 🇯🇵 完全失業率（5月）<span class="badge-important">★</span></li>
              <li>08:30 🇯🇵 有効求人倍率（5月）<span class="badge-important">★</span></li>
              <li>08:30 🇯🇵 鉱工業生産（5月・速報）<span class="badge-important">★</span></li>
              <li>10:00 🇨🇳 中国 製造業PMI（6月）<span class="badge-important">★</span></li>
              <li>10:00 🇨🇳 中国 非製造業PMI（6月）</li>
              <li>15:00 🇩🇪 輸入物価指数（5月）</li>
              <li>16:00 🇩🇪 小売売上高（5月）</li>
              <li>17:00 🇪🇺 ユーロ圏 景況感指数（6月）</li>
              <li><strong>21:00</strong> 🇩🇪 <strong>消費者物価指数・速報（6月）</strong><span class="badge-important">★最重要</span></li>
              <li>23:00 🇺🇸 未決住宅販売指数（5月）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>Q2末・月末リバランスフロー</strong>：年金・ファンドなど機関投資家の四半期末ポートフォリオ調整が月曜から本格化。過去の傾向ではドル売り・円買いに働くケースが多く、USD/JPYの上値を抑える要因。ただし今回はFRBタカ派・日銀様子見の構図でフロー方向が読みづらい。</li>
              <li><strong>独CPI速報（21:00）</strong>：6月ドイツCPIが加速ならECBの7月追加利上げ観測が強まりEUR/USD買い。鈍化なら逆。ECBは6/11に2.25%へ引き上げたばかりで、次の一手は市場が7月ないし9月に織り込み中。</li>
              <li><strong>日本雇用統計（08:30）</strong>：完全失業率・有効求人倍率の改善なら日銀7月追加利上げ論拠が強まる。前回（4月）は完全失業率2.4%・有効求人倍率1.25倍。継続的な雇用改善は賃金上昇→物価上昇の正循環シナリオを支える。</li>
              <li><strong>中国PMI（10:00）</strong>：6月の公式製造業PMI。50超えで景況感拡大。中国景気の強弱はAUD・NZDに直結し、リスクセンチメント全体にも影響。製造業PMIが前回を上回ればリスクオンでJPY売りバイアス。</li>
              <li><strong>月末固定仲値需要</strong>：6月最終週は輸出企業のドル売り（月末決済）と輸入企業のドル買いが交錯。東京時間の仲値（10:00前後）周辺でUSD/JPYが動きやすい。</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 市場環境 + 通貨ランキング -->
      <div class="panel" id="ranking">
        <div class="panel-head">
          <h3>🌏 今日の市場環境</h3>
          <span>地合い・センチメント</span>
        </div>
        <div class="report-body" style="margin-bottom:20px;">
          先週（6/22〜26）の主な流れ：FOMCタカ派（声明修正・ドットチャート年内追加利上げ）の余波が残る中、6/25の米5月PCEが前年比+4.1%と加速。ただしコアPCEが+3.4%と概ね想定内だったためパニック的なドル買いは発生せず、USD/JPYは161.95→161.56へ押し戻された。6/26の東京CPI（6月速報）結果は（要確認）となり、日銀の7月会合に向けた追加利上げ織り込みが変化した可能性がある。<br><br>
          今週は6/30（火）でQ2が終了するため、機関投資家のリバランスフローが週前半に集中する見込み。米国では7/2（木）に雇用統計が発表され、週末は7/4（土）の独立記念日前後で薄商い警戒。当面はUSD/JPYの161円台サポートの堅さを確認しながらのトレードが基本となる。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派） / 日銀 1.00%（6/16利上げ） / ECB 2.25%（タカ派転換）
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
              <td><span class="rank-badge rank-s">S</span></td>
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">Q2末リバランスと月末仲値フローで161円台のサポート確認が最優先</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>EUR/USD</strong><br><span style="color:var(--muted);font-size:12px;">独CPI速報（21:00）次第。加速なら1.14台回復・鈍化なら1.13台へ</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>EUR/JPY</strong><br><span style="color:var(--muted);font-size:12px;">EUR・JPY双方の動き次第。独CPIとリバランスフローが交差</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>AUD/USD</strong><br><span style="color:var(--muted);font-size:12px;">中国PMI（10:00）加速ならAUD買い。0.64台乗せが継続目標</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">今週の指標は少ない。1.32台のサポートを確認しながら推移</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 前日振り返り（wide） -->
      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 先週末の相場振り返り（2026-06-26 金）</h3>
          <span>週末前の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】東京CPI（6月速報）と円相場への影響</div>
            6月26日（金）08:30に東京CPI（6月速報）が発表された。コア（除く生鮮食品）の前年比は（要確認）%と、5月の+2.0%から（加速/鈍化）。前週6/16に日銀が1.00%へ利上げを実施した直後であり、追加利上げに向けた物価目標達成の持続性を示す重要データ。結果が加速傾向を示した場合、日銀の7月会合での追加利上げ（1.25%）織り込みが進みJPY買いへ。鈍化なら逆にJPY売り継続となる。実際の市場反応は（要確認）。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】PCE後のドル売り基調と161円台の攻防</div>
            6/25（木）の米5月PCEが概ね想定内（コアPCE+3.4%）だったことで、週を通じたドル買い勢いは一服。USD/JPYは161.95から161.56まで押し戻され、米10年債利回りは4.36%前後へ低下した。6/26金曜日は週末前のポジション調整が入り、161円台を挟んだ薄商いが続いた。FOMCタカ派ショック（6/17）から約1週間経過し、次の材料を待つ「消化待ち」局面に入った。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】6月Q2の総括——主要中銀が一斉に引き締め</div>
            6月は主要中銀が一致して引き締め方向を強めた月だった。ECB（6/11: 2.25%へ利上げ）、日銀（6/16: 1.00%へ利上げ）、FRB（6/17: FOMC・タカ派スタンスシフト）と3週連続で重要な政策決定が行われた。これにより主要通貨の「金利格差」が再定義され、各通貨ペアの方向性が明確化された。Q2末の今週は、この6月の政策変更を受けたポジション調整・リバランスが完了するタイミングにあたる。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】VIX・米国債利回り・商品市場（要確認）</div>
            VIX（恐怖指数）は（要確認）ポイント前後。米国債10年利回り（要確認）%・2年利回り（要確認）%。DXY（ドルインデックス）は（要確認）付近。金（Gold）は（要確認）ドル/トロイオンス、原油（WTI）は（要確認）ドル/バレル。これらの数値は外部情報取得制限のため今回は実値未取得。週明けの実値で判断すること。
          </div>
          <div class="handover">
            <strong>本日（6/29月曜）への引継ぎ：</strong>
            Q2末リバランスフローが週明けから始まる。機関投資家のドル売り・円買いが出れば161円台前半へ押し戻されるリスク。逆にフロー一巡後は162円台への再トライも。東京時間10:00前後の仲値でUSD/JPYの需給方向を確認。夜21:00の独CPI速報でEUR方向性が確定。7/2（木）の米雇用統計が今週最大の焦点。
          </div>
        </div>
      </div>

      <!-- 経済指標カレンダー（full） -->
      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>📅 本日の経済指標カレンダー（全件）</h3>
          <span>Investing.com・ForexFactory 統合（要確認：外部アクセス制限あり）</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead><tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr></thead>
          <tbody>
            <tr><td><strong>08:30</strong></td><td>🇯🇵 日本</td><td><strong>完全失業率（5月）</strong></td><td><strong>◎</strong></td><td><strong>（要確認）</strong></td><td>2.4%（4月）</td></tr>
            <tr><td><strong>08:30</strong></td><td>🇯🇵 日本</td><td><strong>有効求人倍率（5月）</strong></td><td><strong>◎</strong></td><td><strong>（要確認）</strong></td><td>1.25倍（4月）</td></tr>
            <tr><td><strong>08:30</strong></td><td>🇯🇵 日本</td><td><strong>鉱工業生産・速報（5月）</strong></td><td><strong>○</strong></td><td><strong>（要確認）</strong></td><td>（要確認）</td></tr>
            <tr><td>08:50</td><td>🇯🇵 日本</td><td>当座預金残高（日銀週次）</td><td>△</td><td>—</td><td>—</td></tr>
            <tr><td><strong>10:00</strong></td><td>🇨🇳 中国</td><td><strong>製造業PMI（6月）</strong></td><td><strong>◎</strong></td><td><strong>（要確認）</strong></td><td>（要確認）</td></tr>
            <tr><td>10:00</td><td>🇨🇳 中国</td><td>非製造業PMI（6月）</td><td>○</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>10:00</td><td>🇨🇳 中国</td><td>総合PMI（6月）</td><td>△</td><td>—</td><td>—</td></tr>
            <tr><td>15:00</td><td>🇩🇪 ドイツ</td><td>輸入物価指数（5月）</td><td>△</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>16:00</td><td>🇩🇪 ドイツ</td><td>小売売上高（5月）</td><td>○</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>17:00</td><td>🇪🇺 ユーロ圏</td><td>景況感指数（6月）</td><td>△</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>17:00</td><td>🇪🇺 ユーロ圏</td><td>消費者信頼感・確報（6月）</td><td>×</td><td>—</td><td>—</td></tr>
            <tr><td><strong>21:00</strong></td><td>🇩🇪 ドイツ</td><td><strong>消費者物価指数・速報（6月）</strong></td><td><strong>S</strong></td><td><strong>（要確認）</strong></td><td>（要確認）</td></tr>
            <tr><td>23:00</td><td>🇺🇸 米国</td><td>未決住宅販売指数（5月）</td><td>BB</td><td>（要確認）</td><td>（要確認）</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:10px 0 0;">※ 今週最大イベントは7/2（木）米雇用統計。本日はQ2末リバランスフローと独CPI速報が最重要。外部サイトアクセス制限により予想値・前回値は要確認。</p>
      </div>

      <!-- ファンダメンタルズ（月曜日のみ） -->
      <div class="panel full" id="fundamentals">
        <div class="panel-head">
          <h3>🏦 主要中銀ファンダメンタルズ（週次更新）</h3>
          <span>2026-06-29 現在</span>
        </div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>政策金利</th><th>スタンス</th><th>背景・理由</th></tr></thead>
          <tbody>
            <tr>
              <td>FRB</td><td>🇺🇸 USD</td><td><strong>3.50–3.75%</strong></td>
              <td style="color:var(--red);">タカ派</td>
              <td style="font-size:12px;">6/17 FOMC・4回連続据え置きも声明をタカ派修正。ドットチャートで18人中9人が年内追加利上げ予想。PCEインフレ予想3.6%（前回2.7%）に上方修正。9月利上げ確率が75%超に。</td>
            </tr>
            <tr>
              <td>日銀</td><td>🇯🇵 JPY</td><td><strong>1.00%</strong></td>
              <td style="color:var(--blue);">正常化継続</td>
              <td style="font-size:12px;">6/16 会合で0.75%→1.00%へ25bp利上げ。6/25公表の「主な意見」で「実質金利はきわめて低く追加利上げが適当」との意見複数。次は7月会合（7/30〜31）が焦点。東京CPI・雇用統計が判断材料。</td>
            </tr>
            <tr>
              <td>ECB</td><td>🇪🇺 EUR</td><td><strong>2.25%</strong></td>
              <td style="color:var(--red);">タカ派転換</td>
              <td style="font-size:12px;">6/11 理事会で1.75%→2.25%へ50bp利上げ（予想25bpを超えるサプライズ）。ユーロ圏CPI鈍化が遅れており、追加利上げを7月にも実施する可能性を示唆。本日の独CPI速報が次の判断材料。</td>
            </tr>
            <tr>
              <td>BOE</td><td>🇬🇧 GBP</td><td><strong>3.75%</strong></td>
              <td style="color:var(--muted);">ハト派寄り</td>
              <td style="font-size:12px;">6/18 MPC 7-2で3.75%に据え置き。2名が据え置き反対（利下げ票）でハト派色が強まる。英国インフレは鈍化傾向。次の動きは利下げ方向との観測強。ただし賃金インフレが残存しており時期は未確定。</td>
            </tr>
            <tr>
              <td>RBA</td><td>🇦🇺 AUD</td><td><strong>4.35%</strong></td>
              <td style="color:var(--red);">タカ派</td>
              <td style="font-size:12px;">6/16 理事会で4.35%を据え置き。声明では「インフレが目標に収束するまで時間がかかる」と追加利上げの可能性を保持。豪雇用は底堅く、次の会合（8月）でも据え置きが優勢。</td>
            </tr>
            <tr>
              <td>RBNZ</td><td>🇳🇿 NZD</td><td><strong>2.25%</strong></td>
              <td style="color:var(--red);">タカ派寄り</td>
              <td style="font-size:12px;">5/27 MPC会合で据え置き。ただし「利上げ票」が複数存在し、インフレ再加速なら6月以降の追加利上げも排除しない姿勢。次の会合は7月9日（要確認）。</td>
            </tr>
            <tr>
              <td>BOC</td><td>🇨🇦 CAD</td><td><strong>2.25%</strong></td>
              <td style="color:var(--muted);">中立</td>
              <td style="font-size:12px;">6/10 会合で5会合連続据え置き。カナダ経済は米国の関税リスクに晒されており、利上げよりも利下げ方向への転換が将来的に視野。原油価格の動向がCAD方向性の鍵。</td>
            </tr>
            <tr>
              <td>SNB</td><td>🇨🇭 CHF</td><td><strong>0.00%</strong></td>
              <td style="color:var(--muted);">中立</td>
              <td style="font-size:12px;">6/18 政策会合で0.00%に据え置き（前回のマイナス金利撤廃後を維持）。スイスフランの過度な上昇を防ぐための為替介入を引き続き警戒。ユーロ圏インフレ動向がSNBの政策判断に影響。</td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ 外部サイトアクセス制限により、今週末の最新ニュースは反映できていない項目があります（要確認）。各中銀の公式サイトで最新情報をご確認ください。</p>
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

os.makedirs('reports', exist_ok=True)
with open('reports/2026-06-29.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('reports/2026-06-29.html generated')
