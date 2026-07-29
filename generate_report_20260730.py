TODAY = '2026-07-30'
WEEKDAY = '木'

HERO_SUMMARY_SHORT = 'FOMC据え置き（3.75%）後のドル売りを引き継ぎ、本日はBOE政策金利決定と米PCE・GDP・雇用統計が重なる最重要日。'

hero = f"""<!DOCTYPE html>
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
  <p>{HERO_SUMMARY_SHORT}</p>
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
      <ul class="archive-list">
        <li class="active"><a href="2026-07-30.html">2026-07-30（木）</a></li>
        <li><a href="2026-07-29.html">2026-07-29（水）</a></li>
        <li><a href="2026-07-28.html">2026-07-28（火）</a></li>
        <li><a href="2026-07-27.html">2026-07-27（月）</a></li>
        <li><a href="2026-07-24.html">2026-07-24（金）</a></li>
        <li><a href="2026-07-23.html">2026-07-23（木）</a></li>
        <li><a href="2026-07-22.html">2026-07-22（水）</a></li>
        <li><a href="2026-07-21.html">2026-07-21（火）</a></li>
        <li><a href="2026-07-20.html">2026-07-20（月）</a></li>
        <li><a href="2026-07-17.html">2026-07-17（金）</a></li>
</ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 {TODAY}（{WEEKDAY}）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_SUMMARY_SHORT}</p>
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
        <h3>FOMC据え置き受けドル売り継続、本日はBOE＋米PCE・GDPの最重要日</h3>
        <p>日本時間30日未明3時に発表されたFOMCは、政策金利を3.50〜3.75%で据え置き（9対3の賛成多数、一部反対）。声明は「物価安定を果たす」姿勢を維持しつつ、雇用は労働力ペースと同水準の伸び、インフレは一部燃料ショックにより高止まりと表現した。結果はほぼ予想通りだったためドル売りが優勢となり、ドル円は163円90銭台から163円20銭台へ下落、ユーロドルは1.1431ドルまで上昇した。同時刻、イランによるヨルダン米軍基地への攻撃報道（要確認・単独ソース）を受けトランプ大統領が報復攻撃を警告し、原油先物が5.42ドル高、NYダウは880ドル安となるリスク回避の動きも重なった。本日30日（木）は前日の流れを引き継ぎつつ、20:00の英BOE政策金利発表・四半期金融政策報告・ベイリー総裁記者会見、21:30の米新規失業保険申請件数・個人所得・PCE(コア)デフレーター・第2四半期GDP速報値・個人消費など、ポンドとドル双方の最重要指標が同日に集中する「スーパーサーズデー」となる。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>GBP/USD 🇬🇧🇺🇸</h3>
        <p>4Hデイトレ適性ランキング2位（スコア37）。ポンド側は20:00のBOE政策金利発表・会見、ドル側は21:30の米PCE・GDP・雇用統計と、両サイドの最重要イベントが本日に集中</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red)">HIGH</h3>
        <p>BOE政策金利発表・ベイリー総裁会見（20:00〜21:00）と米PCEコア・第2四半期GDP速報値・新規失業保険申請件数（21:30）が重なり、ポンド・ドル双方でボラティリティ急拡大の可能性</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>36件</h3>
        <p>英BOE政策金利・会見 / 米PCE・GDP速報値・雇用統計 / 独仏伊西ユーロ圏Q2GDP速報値 / 豪住宅建設許可・貿易物価指数</p>
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
              <li>なし（本日7/30はKissFX・ForexFactoryの休場カレンダーに該当なし。日米欧・主要市場は通常営業）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>10:30 🇦🇺 豪州 住宅建設許可件数・貿易物価指数（前年比予想は出所間で差あり・要確認）</li>
              <li>17:00 🇩🇪 独 第2四半期GDP速報値 予想+0.1%（前回+0.3%）</li>
              <li>18:00 🇪🇺 ユーロ圏 第2四半期GDP速報値・失業率 予想+0.2%／6.2%<span class="badge-important">★重要</span></li>
              <li>20:00 🇬🇧 BOE政策金利発表・四半期金融政策報告 3.75%据え置き予想（前回3.75%）<span class="badge-important">★最重要</span></li>
              <li>21:00 🇬🇧 ベイリーBOE総裁 記者会見<span class="badge-important">★最重要</span></li>
              <li>21:30 🇺🇸 米 新規失業保険申請件数 予想20.0万件（前回18.7万件）<span class="badge-important">★重要</span></li>
              <li>21:30 🇺🇸 米 PCEコア・デフレーター（前月比） 予想+0.2%（前回+0.3%）<span class="badge-important">★最重要</span></li>
              <li>21:30 🇺🇸 米 第2四半期GDP速報値・個人消費（出所間で予想値に差あり・要確認）<span class="badge-important">★最重要</span></li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>BOEは3.75%据え置き予想も投票内訳に注目</strong>：前回MPC投票は2-0-7（利下げ支持ゼロ・据え置き7）で、今回同水準を維持するか、ハト派側への傾きが出るかでポンドの方向性が決まる</li>
              <li><strong>米PCEコアはFRBの物価判断の生命線</strong>：予想+0.2%（前回+0.3%）へ鈍化なら、FOMC後のドル売りが加速しやすい地合い。逆に上振れなら前日のFOMCタカ派寄り解釈が強まりドルが下げ渋る可能性</li>
              <li><strong>ドル円は前日FOMC後の下落（163.90円台→163.20円台）を引き継ぎ東京朝スタート</strong>：BOE・米指標発表までは方向感に乏しいレンジ推移を想定</li>
              <li><strong>イランのヨルダン米軍基地攻撃報道は単独ソースで未確認</strong>（要確認）：事実であれば原油高・リスク回避の巻き戻しが長引く可能性があるが、続報の有無を要ウォッチ</li>
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
          7/30（木）は、前日29日（NY時間、日本時間30日未明3時）のFOMCが政策金利を3.50〜3.75%で据え置いた流れを引き継ぐ。結果はほぼ予想通りだったためドル売りが優勢となり、ドル円は163円90銭台から163円20銭台へ下落、ユーロドルは1.1431ドルまで上昇して東京朝を迎えている。同時刻に伝わったイランによるヨルダン米軍基地攻撃報道（要確認・単独ソース）を受け、原油先物が5.42ドル高、NYダウは880ドル安とリスク回避も重なった。本日最大の材料は20:00の英BOE政策金利発表・ベイリー総裁会見（3.75%据え置き予想）と、21:30の米新規失業保険申請件数・PCEコア・第2四半期GDP速報値・個人消費で、ポンド・ドル双方の方向性を決める「スーパーサーズデー」となる。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派、7/29FOMCで据え置き決定・声明は物価安定重視を継続） / 英BOE 3.75%（本日20:00に政策金利発表・次の判断待ち） / 日銀 1.00%（正常化継続、次回7/30-31）
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
              <td><strong>EUR/AUD</strong><br><span style="color:var(--muted);font-size:12px;">4Hデイトレ適性ランキング1位（スコア48）。4H ADX28.5とトレンド形成十分で、本日は独仏伊西・ユーロ圏のGDP速報値ラッシュとRBA副総裁講演が重なる</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング2位（スコア37・見送り）。20:00のBOE政策金利・会見と21:30の米PCE・GDPが重なり両建てのイベントリスク</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>AUD/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング3位（スコア32・見送り）。10:30の住宅建設許可・貿易物価指数を控えるが、4H ADX15.1とトレンド形成弱く方向感に乏しい</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>NZD/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング4位（スコア29・見送り）。10:00のANZ企業景況感を控えるが手掛かり材料薄くレンジ想定</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/CHF</strong><br><span style="color:var(--muted);font-size:12px;">ランキング5位（スコア26・見送り）。16:00のKOF先行指数を除き材料薄いが、21:30の米指標ラッシュでUSD側のボラティリティに注意</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日05:28 JST時点。全ペアが判定「見送り」基準（スコア50未満）。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-07-29）</h3>
          <span>昨日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】FOMC、政策金利を3.50〜3.75%で据え置き</div>
            日本時間30日未明3時（NY時間29日午後）に発表されたFOMC声明で、米連邦公開市場委員会は政策金利を3.50〜3.75%に据え置くことを9対3の賛成多数で決定した。声明は「物価安定を果たす」との姿勢を継続し、雇用は労働力ペースと同水準の伸び、インフレは一部燃料ショックにより高止まりと説明した。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】FOMC後にドル全面安、ドル円163円台前半へ下落</div>
            結果がほぼ予想通りだったことからドル売りが優勢となり、ドル円は163円90銭台から163円20銭台へ下落。ユーロドルは1.1431ドルまで上昇し、FOMC通過による持ち高整理のドル売りが目立った。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】イランによるヨルダン米軍基地攻撃報道でリスク回避（要確認）</div>
            イランがヨルダンの米軍基地を攻撃したと伝わり、トランプ大統領が激しい報復攻撃を警告したと報じられた。この報道は現時点でzai.diamond.jp（Diamond FX News）のみが伝えており、他の主要ソースでの確認が取れていないため事実関係は要確認だが、報道を受けてWTI原油先物は5.42ドル高となった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】NYダウ880ドル安、リスク回避で株安</div>
            原油高と中東情勢への警戒から投資家のリスク回避姿勢が強まり、NYダウ平均は約880ドル安で引けた。FOMCの据え置き決定自体は市場想定内だったが、地政学リスクの高まりが株式市場の重荷となった。
          </div>
          <div class="handover">
            <strong>本日（7/30木）への引継ぎ：</strong>
            ドル円は163円台前半で東京朝スタート。前日のFOMC据え置き後のドル売り地合いを引き継ぎつつ、20:00のBOE政策金利発表・ベイリー総裁会見と21:30の米PCE・GDP・雇用統計を控え、それまでは方向感に乏しいレンジ推移を想定。イラン関連報道（要確認）の続報有無にも注意。
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
            <tr><td>02:30</td><td>🇨🇦 加</td><td>BOC審議要旨（要確認・ForexFactoryのみ）</td><td>★</td><td>—</td><td>—</td></tr>
            <tr><td><strong>03:00</strong></td><td>🇺🇸 米国</td><td><strong>FOMC政策金利発表（結果判明：3.75%据え置き）</strong></td><td><strong>★★★★★</strong></td><td><strong>3.75%据え置き</strong></td><td>3.75%</td></tr>
            <tr><td>03:00</td><td>🇺🇸 米国</td><td>FOMC声明（結果判明：物価安定重視を継続）</td><td>★★★★★</td><td>—</td><td>—</td></tr>
            <tr><td>03:30</td><td>🇺🇸 米国</td><td>FOMC後記者会見（結果判明）</td><td>★★★★★</td><td>—</td><td>—</td></tr>
            <tr><td>07:40</td><td>🇦🇺 豪州</td><td>RBA次席総裁ハンター講演（要確認・ForexFactoryのみ）</td><td>★</td><td>—</td><td>—</td></tr>
            <tr><td>10:00</td><td>🇳🇿 NZ</td><td>ANZ企業景況感</td><td>★</td><td>—</td><td>+36.6</td></tr>
            <tr><td><strong>10:30</strong></td><td>🇦🇺 豪州</td><td>住宅建設許可件数（前月比、出所間で予想値に差・要確認）</td><td>★</td><td>-0.5%〜-0.7%</td><td>-1.1%</td></tr>
            <tr><td>10:30</td><td>🇦🇺 豪州</td><td>第2四半期輸入物価指数（前期比）</td><td>★</td><td>±0.0%</td><td>+0.1%</td></tr>
            <tr><td>10:30</td><td>🇦🇺 豪州</td><td>第2四半期輸出物価指数（要確認・KissFXのみ）</td><td>★</td><td>+0.8%</td><td>+0.5%</td></tr>
            <tr><td>14:00</td><td>🇯🇵 日本</td><td>消費者信頼感指数（要確認・ForexFactoryのみ）</td><td>★</td><td>34.2</td><td>33.8</td></tr>
            <tr><td>14:30</td><td>🇫🇷 仏</td><td>第2四半期GDP速報値（前期比）</td><td>★★</td><td>+0.2%</td><td>-0.1%</td></tr>
            <tr><td>14:30</td><td>🇫🇷 仏</td><td>消費支出（前月比、要確認・ForexFactoryのみ）</td><td>★</td><td>-0.1%</td><td>+0.5%</td></tr>
            <tr><td>15:29</td><td>🇩🇪 独</td><td>CPI速報値（前月比、要確認・ForexFactoryのみ）</td><td>★★</td><td>+0.7%</td><td>-0.3%</td></tr>
            <tr><td>15:45</td><td>🇫🇷 仏</td><td>民間部門雇用者数速報（要確認・ForexFactoryのみ）</td><td>★</td><td>-0.1%</td><td>-0.1%</td></tr>
            <tr><td>16:00</td><td>🇨🇭 スイス</td><td>KOF先行指数</td><td>★</td><td>100.9</td><td>101.2</td></tr>
            <tr><td>16:00</td><td>🇪🇸 スペイン</td><td>CPI速報値（前年比、要確認・ForexFactoryのみ）</td><td>★</td><td>3.2%</td><td>3.2%</td></tr>
            <tr><td>16:00</td><td>🇪🇸 スペイン</td><td>GDP速報値（前期比、要確認・ForexFactoryのみ）</td><td>★</td><td>0.6%</td><td>0.6%</td></tr>
            <tr><td><strong>17:00</strong></td><td>🇩🇪 独</td><td><strong>第2四半期GDP速報値（前期比）</strong></td><td><strong>★★</strong></td><td><strong>+0.1%</strong></td><td>+0.3%</td></tr>
            <tr><td>17:00</td><td>🇮🇹 伊</td><td>第2四半期GDP速報値（要確認・ForexFactoryのみ）</td><td>★</td><td>0.1%</td><td>0.2%</td></tr>
            <tr><td>18:00</td><td>🇮🇹 伊</td><td>失業率（要確認・ForexFactoryのみ）</td><td>★</td><td>5.0%</td><td>5.0%</td></tr>
            <tr><td><strong>18:00</strong></td><td>🇪🇺 ユーロ圏</td><td><strong>第2四半期GDP速報値（前号、出所間で差・要確認）</strong></td><td><strong>★★★</strong></td><td><strong>+0.2%</strong></td><td>-0.2%〜+0.1%</td></tr>
            <tr><td>18:00</td><td>🇪🇺 ユーロ圏</td><td>失業率</td><td>★</td><td>6.2%</td><td>6.2%</td></tr>
            <tr><td>18:33</td><td>🇮🇹 伊</td><td>10年債入札（要確認・ForexFactoryのみ）</td><td>★</td><td>—</td><td>—</td></tr>
            <tr><td><strong>20:00</strong></td><td>🇬🇧 英国</td><td><strong>BOE政策金利発表</strong></td><td><strong>★★★★★</strong></td><td><strong>3.75%据え置き</strong></td><td>3.75%</td></tr>
            <tr><td>20:00</td><td>🇬🇧 英国</td><td>BOE四半期金融政策報告</td><td>★★★★★</td><td>—</td><td>—</td></tr>
            <tr><td>20:00</td><td>🇬🇧 英国</td><td>MPC投票結果（要確認・ForexFactoryのみ）</td><td>★★★★★</td><td>2-0-7</td><td>2-0-7</td></tr>
            <tr><td>20:00〜21:00</td><td>🇬🇧 英国</td><td>ベイリーBOE総裁記者会見（時刻表記が出所間で20:30/21:00と差・要確認）</td><td>★★★★★</td><td>—</td><td>—</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>新規失業保険申請件数</strong></td><td><strong>★★★★★</strong></td><td><strong>20.0万件</strong></td><td>18.7万件</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>個人所得（前月比）</td><td>★★★</td><td>+0.3%</td><td>+0.7%</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>PCEデフレーター（前年比、要確認・KissFXのみ）</td><td>★★★★★</td><td>+3.7%</td><td>+4.1%</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>PCEコア・デフレーター（前月比）</strong></td><td><strong>★★★★★</strong></td><td><strong>+0.2%</strong></td><td>+0.3%</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>第2四半期GDP速報値（前期比、出所間で予想・前回の値に差・要確認）</strong></td><td><strong>★★★★★</strong></td><td><strong>+2.0%〜+2.1%</strong></td><td>+2.0%〜+2.1%</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>GDP価格指数速報値（要確認・ForexFactoryのみ）</td><td>★★</td><td>4.1%</td><td>3.6%</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>個人消費【GDP内訳・速報値】（要確認・KissFXのみ）</td><td>★★★★★</td><td>+2.3%</td><td>+0.5%</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>個人消費支出（前月比、要確認・ForexFactoryのみ）</td><td>★</td><td>+0.4%</td><td>+0.7%</td></tr>
            <tr><td>23:30</td><td>🇺🇸 米国</td><td>週間天然ガス貯蔵量</td><td>★</td><td>+37B</td><td>+32B</td></tr>
            <tr><td>米株引け後</td><td>🇺🇸 米国</td><td>アップル決算（要確認・KissFXのみ）</td><td>企業決算</td><td>—</td><td>—</td></tr>
            <tr><td>米株引け後</td><td>🇺🇸 米国</td><td>アマゾン決算（要確認・KissFXのみ）</td><td>企業決算</td><td>—</td><td>—</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または両ソース間で数値・時刻に差がある指標には「（要確認）」を付しています。03:00〜03:30のFOMC関連は既に結果判明済みのため、前日の相場振り返りと合わせて参照してください。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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

with open('reports/2026-07-30.html', 'w', encoding='utf-8') as f:
    f.write(hero)
print('reports/2026-07-30.html generated')
