"""Generate reports/2026-07-27.html (Monday, with fundamentals table)."""

TODAY = "2026-07-27"
WEEKDAY = "月"
HERO_SUB = (
    "週末にかけて米・イランの戦闘終結に向けた協議が進展し、地政学リスクプレミアムが後退。"
    "週明けオセアニア市場でドル円は163.64円を下抜け163.60円台まで反落した。"
    "今週はFOMC（7/28-29）・日銀会合（7/30-31）・BOE（7/30）と主要中銀イベントが集中する重要週。"
)

SIDEBAR_ARCHIVE = """
        <li class="active"><a href="2026-07-27.html">2026-07-27（月）</a></li>
        <li><a href="2026-07-24.html">2026-07-24（金）</a></li>
        <li><a href="2026-07-23.html">2026-07-23（木）</a></li>
        <li><a href="2026-07-22.html">2026-07-22（水）</a></li>
        <li><a href="2026-07-21.html">2026-07-21（火）</a></li>
        <li><a href="2026-07-20.html">2026-07-20（月）</a></li>
        <li><a href="2026-07-17.html">2026-07-17（金）</a></li>
        <li><a href="2026-07-16.html">2026-07-16（木）</a></li>
        <li><a href="2026-07-15.html">2026-07-15（水）</a></li>
        <li><a href="2026-07-14.html">2026-07-14（火）</a></li>
"""

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
      <a href="#"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/><circle cx="8" cy="6" r="2"/><circle cx="17" cy="12" r="2"/><circle cx="11" cy="18" r="2"/></svg>インジケーター</a>
      <a href="#"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="1"/><line x1="9" y1="7" x2="9" y2="4"/><line x1="12" y1="7" x2="12" y2="4"/><line x1="15" y1="7" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="17"/><line x1="12" y1="20" x2="12" y2="17"/><line x1="15" y1="20" x2="15" y2="17"/><line x1="4" y1="9" x2="7" y2="9"/><line x1="4" y1="12" x2="7" y2="12"/><line x1="4" y1="15" x2="7" y2="15"/><line x1="17" y1="9" x2="20" y2="9"/><line x1="17" y1="12" x2="20" y2="12"/><line x1="17" y1="15" x2="20" y2="15"/></svg>EA</a>
      <span class="nav-section">サイト情報</span>
      <a href="../about.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>About</a>
      <a href="../disclaimer.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>免責事項</a>
      <a href="../contact.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>お問い合わせ</a>
    </nav>

    <div style="margin-top:28px; padding-top:20px; border-top:1px solid var(--line);">
      <p style="font-size:11px;color:var(--muted);margin:0 0 10px;letter-spacing:.06em;text-transform:uppercase;">過去のレポート</p>
      <ul class="archive-list">{SIDEBAR_ARCHIVE}</ul>
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
        <em>月曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>米イラン協議進展でドル円反落、FOMC・日銀控え神経質な週明け</h3>
        <p>週末にかけて米国とイランの戦闘終結に向けた協議が進展したと伝わり、地政学リスクプレミアムが後退。週明けのオセアニア市場でドル円は前週末安値163.64円を下抜け163.60円台まで売られた。原油(WTI)も84.73ドル（前日比-0.49%）へ反落する一方、金(ゴールド)は逃避買いの残存で4,091.50ドル（同+0.51%）と底堅い。今週はFOMC（7/28-29）・日銀会合（7/30-31）・BOE（7/30）と主要中銀イベントが集中するため、本日の独IFO・米耐久財受注は方向感を欠く展開になりやすい（要確認）。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>米・イラン協議進展による地政学リスク後退でドル円が反落、163.60円台。今週はFOMC・日銀会合を控え神経質な展開が予想される。4Hデイトレ適性ランキング3位（スコア41・見送り）</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">MEDIUM</h3>
        <p>VIX18.58（前日比-0.64%）と落ち着いた水準。米イラン協議進展で地政学リスクは後退したが、FOMC（7/28-29）・日銀会合（7/30-31）を控え中銀イベントリスクは残存（要確認）</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>15件</h3>
        <p>独IFO景況指数 / 米耐久財受注 / 米ダラス連銀製造業活動指数 / 米国債入札 等</p>
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
              <li>なし（本日7/27は日米欧・主要市場すべて通常営業。確認できた範囲で祝日情報なし）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>17:00 🇩🇪 IFO景況指数 予想86.0〜86.1（前回85.6）<span class="badge-important">★重要</span></li>
              <li>21:30 🇺🇸 耐久財受注 予想+1.6〜1.8%（前回-4.5%）<span class="badge-important">★重要</span></li>
              <li>21:30 🇺🇸 耐久財受注【除輸送用機器】 予想+0.8〜0.9%（前回+1.3%）<span class="badge-important">★重要</span></li>
              <li>23:30 🇺🇸 ダラス連銀製造業活動指数 予想+1.1（前回±0.0）（要確認）</li>
              <li>00:30(28日) 🇺🇸 2年債入札／02:00(28日) 🇺🇸 5年債入札（要確認）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>米・イラン、戦闘終結に向けた協議進展でドル円反落</strong>：週明けオセアニア市場で前週末安値163.64円を下抜け163.60円台まで下落。地政学リスクプレミアムの解消がドル売り要因となっている（要確認）</li>
              <li><strong>今週はFOMC(7/28-29)・日銀会合(7/30-31)・BOE(7/30)が集中</strong>：市場はFOMC・BOEともに据え置きが有力（それぞれ約65%・86%の織り込み）とみているが、日銀会合を境にボラティリティ上昇に注意</li>
              <li><strong>原油(WTI)は地政学リスク後退で84.73ドルへ反落</strong>：ホルムズ海峡の正常化観測が価格の重荷（要確認）</li>
              <li><strong>金(ゴールド)は逃避買いの残存で堅調</strong>：4,091.50ドル（前日比+0.51%）。地政学リスクの完全な後退には至っていないとの見方も（要確認）</li>
              <li><strong>米国指標は「小粒」との見方</strong>：耐久財受注・ダラス連銀とも重要度は中程度で、方向感を欠く展開になりやすい</li>
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
          7/27（月）は、週末にかけて米・イランの戦闘終結に向けた協議が進展したとの報道を受け、地政学リスクプレミアムが後退。オセアニア市場でドル円は前週末安値163.64円を下抜け163.60円台まで反落してスタートした。原油(WTI)も84.73ドル（前日比-0.49%）へ値を下げ、VIXは18.58（前日比-0.64%）と落ち着いた水準で推移している。今週はFOMC(7/28-29)・日銀会合(7/30-31)・BOE(7/30)と主要中銀イベントが集中する重要週で、本日は独IFO景況指数・米耐久財受注が材料となるが、米国指標は小粒との見方もあり方向感は限定的か（要確認）。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派） / 日銀 1.00%（正常化継続、次回7/30-31） / 欧ECB 2.25%（タカ派・据え置き、9月に追加利上げ判断持ち越し）
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
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">米ドル全面安・地政学リスク後退を受け対ドルで底堅い。4Hデイトレ適性ランキング1位（スコア56・唯一の判定「候補」）。今週はBOE(7/30)を控える</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>NZD/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング2位（スコア48・見送り）。RBNZ7/8利上げ後の高値圏を維持しつつ方向感待ち</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">米イラン協議進展の地政学リスク後退でドル円反落、163.60円台。ランキング3位（スコア41・見送り）。今週FOMC・日銀会合を控える</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/CHF</strong><br><span style="color:var(--muted);font-size:12px;">地政学リスク後退で安全資産CHFの巻き戻し売り。ランキング4位（スコア33・見送り）</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/AUD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング5位（スコア31・見送り）。方向感に乏しくレンジ想定</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日05:28 JST時点。GBP/USDのみ判定「候補」（スコア56）、その他は見送り基準（スコア50未満）。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前週末の相場振り返り（2026-07-24〜26）</h3>
          <span>週末を挟んだ主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】「有事のドル買い」継続でドル円163.8円台まで上昇、39年8カ月ぶり高値圏で越週</div>
            週末にかけてイラン情勢の緊迫を背景にした「有事のドル買い」が続き、7/24のNY市場でドル円は163.83円で引けた。米7月PMI速報値・6月新築住宅販売件数が予想を上回ったことも金利高・ドル高を支えた。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】米・イラン、戦闘終結に向けた協議進展で週明けドル円が反落</div>
            週末にかけて米国とイランの戦闘終結に向けた外交協議が進展したと伝わり、週明け27日のオセアニア市場でドル円は売りが先行。前日安値163.64円を下抜け163.60円台まで下落した。地政学リスクプレミアムの解消がドル買い一服につながっている。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】原油はイラン懸念の緩和で反落、週末にかけての急伸から一服</div>
            WTI原油は前週末にかけ供給不安から上昇した後、27日には米イラン協議進展を受けて84.73ドル（前日比-0.49%）まで反落。ホルムズ海峡の正常化観測が価格の重荷となった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】金(ゴールド)は逃避買いの残存で堅調、4,000ドル台後半を維持</div>
            中東情勢の緊迫を背景とした逃避資金流入が続き、COMEX金は週末に4,055.60ドルまで反発。27日時点でも4,091.50ドル（前日比+0.51%）と堅調に推移している。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック⑤】CFTC建玉報告：投機筋の円売り越しが増加、豪ドルは買い越し縮小</div>
            週末にかけて発表されたCFTC建玉報告では、レバレッジド・ファンドの円売り越しが増加した一方、資源国通貨では豪ドルの買い越しが減少するなど、ポジション調整の動きが見られた（要確認）。
          </div>
          <div class="handover">
            <strong>本日（7/27月）への引継ぎ：</strong>
            米・イラン協議進展を受けた地政学リスクプレミアムの解消でドル円は163.60円台まで反落してスタート。今週はFOMC（7/28-29）・日銀会合（7/30-31）・BOE（7/30）と主要中銀イベントが集中する重要週。本日は独IFO景況感・米耐久財受注が材料だが、米国指標は「小粒」との見方もあり方向感は限定的か。地政学リスクの後退がどこまでドル安・リスクオン方向に作用するか見極めが必要（要確認）。
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
            <tr><td>08:50</td><td>🇯🇵 日本</td><td>企業向けサービス価格指数(SPPI)前年比（要確認）</td><td>★</td><td>+3.4%</td><td>+3.3%</td></tr>
            <tr><td>14:00</td><td>🇯🇵 日本</td><td>景気先行CI指数【改定値】（要確認）</td><td>★</td><td>—</td><td>116.8</td></tr>
            <tr><td>14:00</td><td>🇯🇵 日本</td><td>景気一致CI指数【改定値】（要確認）</td><td>★</td><td>—</td><td>118.5</td></tr>
            <tr><td>17:00</td><td>🇩🇪 独</td><td>IFO景況指数</td><td>★★</td><td>86.0〜86.1</td><td>85.6</td></tr>
            <tr><td>17:00</td><td>🇩🇪 独</td><td>IFO現況指数（要確認）</td><td>★</td><td>87.3</td><td>87.0</td></tr>
            <tr><td>17:00</td><td>🇩🇪 独</td><td>IFO景気期待指数（要確認）</td><td>★</td><td>84.7</td><td>84.1</td></tr>
            <tr><td>17:00</td><td>🇪🇺 ユーロ圏</td><td>M3マネーサプライ前年比（要確認）</td><td>★</td><td>+3.2%</td><td>+3.2%</td></tr>
            <tr><td>17:00</td><td>🇪🇺 ユーロ圏</td><td>民間融資残高前年比（要確認）</td><td>★</td><td>+3.1%</td><td>+3.1%</td></tr>
            <tr><td>18:15</td><td>🇪🇺 ユーロ圏</td><td>ECOFIN会合（要確認）</td><td>★</td><td>—</td><td>—</td></tr>
            <tr><td>19:00</td><td>🇬🇧 英国</td><td>CBI流通取引調査／実売上高（要確認）</td><td>★</td><td>-45</td><td>-54</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>耐久財受注</td><td>★★★</td><td>+1.6〜1.8%</td><td>-4.5%</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>耐久財受注【除輸送用機器】</td><td>★★★</td><td>+0.8〜0.9%</td><td>+1.3%</td></tr>
            <tr><td>23:30</td><td>🇺🇸 米国</td><td>ダラス連銀製造業活動指数（要確認）</td><td>★★</td><td>+1.1</td><td>±0.0</td></tr>
            <tr><td>00:30(28日)</td><td>🇺🇸 米国</td><td>2年債入札（要確認）</td><td>★</td><td>690億ドル</td><td>—</td></tr>
            <tr><td>02:00(28日)</td><td>🇺🇸 米国</td><td>5年債入札（要確認）</td><td>★</td><td>700億ドル</td><td>—</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。本日分はKissFX（主・ランク付き）とForexFactoryの機械可読カレンダーの2つの独立ソースで照合済み。両ソースで一致した独IFO景況指数・米耐久財受注（本体／コア）は値の軽微な差異を「〜」で両論併記し、片方のソースにしか掲載がない指標には「（要確認）」を付しています。本日は中央銀行の政策決定はなく、独IFO景況指数（17:00）と米耐久財受注（21:30）が中心。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
      </div>

      <!-- ファンダメンタルズ（月曜日のみ） -->
      <div class="panel full" id="fundamentals">
        <div class="panel-head">
          <h3>🏦 主要中銀ファンダメンタルズ（週次更新）</h3>
          <span>{TODAY} 現在</span>
        </div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>政策金利</th><th>スタンス</th><th>背景・理由</th></tr></thead>
          <tbody>
            <tr>
              <td>FRB</td><td>🇺🇸 USD</td><td><strong>3.50–3.75%</strong></td>
              <td style="color:var(--red);">タカ派</td>
              <td style="font-size:12px;">7/19までにウォーシュ議長はタカ派色を鮮明化。7/1には「インフレリスクは低下したが依然高すぎる」と発言し、声明文から利下げ示唆のフォワードガイダンス文言を削除。次回FOMCは7/28-29で、市場の据え置き織り込みは約65%。</td>
            </tr>
            <tr>
              <td>日銀</td><td>🇯🇵 JPY</td><td><strong>1.00%</strong></td>
              <td style="color:var(--blue);">正常化継続</td>
              <td style="font-size:12px;">6/15-16会合で0.25%利上げを決定して以降、1.00%を維持。次回7/30-31会合は据え置き観測が優勢で、次の利上げは12月との見方が多い。年内1.25%到達の可能性も残る（要確認）。</td>
            </tr>
            <tr>
              <td>ECB</td><td>🇪🇺 EUR</td><td><strong>2.25%</strong></td>
              <td style="color:var(--red);">タカ派・据え置き</td>
              <td style="font-size:12px;">7/23理事会で2会合連続の据え置きを全会一致で決定。ラガルド総裁はエネルギーショックの影響が完全に顕在化していないと指摘し、データ次第の会合毎判断を再表明。追加利上げの判断は9月に持ち越し。</td>
            </tr>
            <tr>
              <td>BOE</td><td>🇬🇧 GBP</td><td><strong>3.75%</strong></td>
              <td style="color:var(--muted);">中立・据え置き継続</td>
              <td style="font-size:12px;">6/17MPCで据え置きを決定して以降3.75%を維持。次回7/30会合（金融政策報告書・総裁会見あり、Super Thursday）ではSONIA先物が据え置き確率を約86%と織り込む。</td>
            </tr>
            <tr>
              <td>RBA</td><td>🇦🇺 AUD</td><td><strong>4.35%</strong></td>
              <td style="color:var(--red);">タカ派</td>
              <td style="font-size:12px;">2月・3月・5月と3会合連続で+0.25%ずつ利上げ（3.85%→4.10%→4.35%）した後、6/16会合で据え置き。中東情勢に伴う供給圧力や資源価格の高止まりを警戒し追加利上げの余地を残す。次回8/11会合まで材料難。</td>
            </tr>
            <tr>
              <td>RBNZ</td><td>🇳🇿 NZD</td><td><strong>2.50%</strong></td>
              <td style="color:var(--red);">タカ派転換</td>
              <td style="font-size:12px;">7/8会合でOCRを2.25%→2.50%へ引き上げ。約3年ぶりの利上げで、6月期インフレ率（3.9%）への対応。委員会内には慎重派も残るが、追加利上げを実施する構えを示している。</td>
            </tr>
            <tr>
              <td>BOC</td><td>🇨🇦 CAD</td><td><strong>2.25%</strong></td>
              <td style="color:var(--muted);">中立</td>
              <td style="font-size:12px;">7/15会合で6会合連続の据え置き。労働市場の軟弱さと貿易摩擦の不確実性、原油価格変動によるインフレ圧力のバランスを注視する姿勢。</td>
            </tr>
            <tr>
              <td>SNB</td><td>🇨🇭 CHF</td><td><strong>0.00%</strong></td>
              <td style="color:var(--muted);">中立</td>
              <td style="font-size:12px;">3会合連続でゼロ金利を維持（直近は6月会合）。中東情勢を踏まえ、必要に応じ為替介入も辞さない姿勢を維持。次回発表は9月の見込み。</td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ 各中銀の公式発表・複数の報道ソース（日本経済新聞・Bloomberg・ジェトロ・各中銀公式サイト等）で確認済み。最新情報は各中銀の公式サイトでご確認ください。</p>
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

with open(f"reports/{TODAY}.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"reports/{TODAY}.html generated")
