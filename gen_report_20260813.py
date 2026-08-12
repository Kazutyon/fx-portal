#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FX日報 2026-08-13（木）生成スクリプト"""
import glob, os
from datetime import date

TODAY = '2026-08-13'
WEEKDAY = '木'

DAYS_JA = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

def sidebar_archive_html():
    files = sorted(glob.glob('reports/*.html'), reverse=True)
    items = ''
    for f in files[:10]:
        name = os.path.basename(f).replace('.html', '')
        try:
            d = date.fromisoformat(name)
            wd = DAYS_JA[d.strftime('%A')]
            label = f'{name}（{wd}）'
        except Exception:
            label = name
        active = ' class="active"' if name == TODAY else ''
        href = name + '.html'
        items += f'<li{active}><a href="{href}">{label}</a></li>\n'
    return items

SIDEBAR_ARCHIVE = sidebar_archive_html()

HERO_SUB = '米CPI通過後にドル買い戻しが優勢となり、ドル円は159.50円と7/31以来の高値を更新。本日は15:00の英GDP速報値（Q2）、21:30の米PPI・新規失業保険申請件数に関心が集まる。'

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
        {SIDEBAR_ARCHIVE}</ul>
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
        <h3>米CPI通過後にドル買い戻しが優勢、ドル円は159.50円と7/31以来の高値を更新</h3>
        <p>8/12（水）21:30発表の米CPIはコア指数が市場予想と一致。発表直後はインフレ鈍化を意識してドル円が158円台まで下落する場面があったが（要確認）、その後市場がコア指数の内容を消化しドル買い戻しが優勢に転じ、NY市場終盤にかけて159.50円まで上昇、7/31以来の高値を更新した。同日実施された420億ドルの米10年債入札では最高落札利回りが4.683%と2007年来の高水準を記録し、財政懸念を意識させる材料となった。また米財務省発表の7月財政赤字は2021年3月以来の最大規模に拡大し、防衛費拡大や関税還付が響いた（要確認）。欧州株の全面安によるリスク回避ムードも一時のドル売り・円買い圧力の一因となった（要確認）。本日8/13は15:00の英国GDP速報値（Q2）、21:30の米新規失業保険申請件数・生産者物価指数（PPI）に関心が集まる。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>米CPI通過後のドル買い戻し基調を引き継ぐ中、本日21:30の米PPI・新規失業保険申請件数の結果次第で方向感が定まりやすい</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">MEDIUM</h3>
        <p>15:00の英GDP速報値（Q2）と21:30の米PPI・新規失業保険申請件数が重なる。米CPI級の単独最重要イベントはないが、複数の中重要度指標が集中し値動きが大きくなりやすい</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>7件</h3>
        <p>英GDP速報値(Q2) / 米生産者物価指数(PPI) / 米新規失業保険申請件数 / 米30年債入札 等（本日の市場休場はなし）</p>
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
              <li>08:50 🇯🇵 国内企業物価指数（PPI）前月比/前年比（前年比はKissFX・ForexFactory一致、前月比はKissFXのみ・要確認）</li>
              <li>15:00 🇬🇧 GDP速報値（Q2、前期比/前年比）<span class="badge-important">★最重要</span>（前期比はKissFX・ForexFactory一致、前年比はKissFXのみ・要確認）</li>
              <li>15:00 🇬🇧 鉱工業生産・製造業生産高・商品貿易収支（KissFX・ForexFactory一致）</li>
              <li>21:15 🇺🇸 ハマックFRB総裁発言（KissFX・ForexFactory一致）</li>
              <li>21:30 🇺🇸 新規失業保険申請件数（KissFX・ForexFactory一致）</li>
              <li>21:30 🇺🇸 生産者物価指数（PPI）前月比/コア前月比<span class="badge-important">★最重要</span>（KissFX・ForexFactory一致）</li>
              <li>21:40 🇺🇸 バーキンFRB総裁発言（KissFX・ForexFactory一致）</li>
              <li>26:00 🇺🇸 30年債入札（翌日未明・要確認・KissFXのみ）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>米CPI通過後、ドル買い戻しが優勢に転じドル円は159.50円と7/31以来の高値を更新</strong>：発表直後は158円台まで下落する場面があったが、コア指数が予想通りだったことを消化しドル買い戻しが強まった（要確認）</li>
              <li><strong>米10年債入札で最高落札利回りが2007年来の高水準</strong>：420億ドルの入札で最高落札利回りは4.683%、応札倍率2.53倍。財政懸念を意識させる材料となった</li>
              <li><strong>米7月財政赤字が2021年3月以来の最大規模に拡大</strong>：防衛費拡大や関税還付が響いた（要確認）</li>
              <li><strong>欧州株が全面安、リスク回避のドル売り・円買い圧力</strong>：欧州株式市場が全面安となりリスク回避ムードが広がった（要確認）</li>
              <li><strong>本日は15:00の英GDP速報値（Q2）が焦点の一つ</strong>：前期比の市場予想は+0.4%（前回+0.6%）。英ポンドクロスの値動きが大きくなりやすい</li>
              <li><strong>21:30の米PPI・新規失業保険申請件数も注視材料に</strong>：CPI通過後のインフレ鈍化ペースを見極める上で、PPIの結果次第でFRBの金融政策観測が振れやすい</li>
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
          8/13（木）は前日NY市場でドル円が米CPI通過後の乱高下を経て159.50円まで上昇し、7/31以来の高値を更新した流れを引き継いでスタート。420億ドルの米10年債入札で最高落札利回りが2007年来の高水準となったほか、米7月財政赤字の拡大も明らかになり、財政懸念を意識した金利上昇圧力がドルの下支え材料となっている。本日は15:00の英GDP速報値（Q2）、21:30の米PPI・新規失業保険申請件数が重なり、複数の中重要度指標の結果次第で値動きが大きくなりやすい。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派・据え置き、7/29 9対3・3人が利上げ主張） / 日銀 1.00%（正常化継続） / 英BOE 3.75%（中立寄り、7/30据え置き）
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
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング1位（スコア47・見送り）。米CPI通過後のドル買い戻し基調を引き継ぎつつ、本日21:30の米PPIで方向感が定まりやすい</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/CAD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング2位（スコア47・見送り）。ADX26.9で下降トレンド継続、原油価格の動向次第で振れやすい</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング3位（スコア43・見送り）。本日15:00の英GDP速報値（Q2）を控え上昇トレンド継続</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング4位（スコア41・見送り）。英GDP発表結果次第で振れやすい</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>AUD/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング5位（スコア37・見送り）。09:15のRBA副総裁発言を通過後、上昇基調を維持</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日05:08 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-08-12）</h3>
          <span>昨日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】米CPI発表後にドル円が乱高下、コア指数が予想通りとなりドル買い戻しが優勢に</div>
            21:30発表の米CPIはコア指数が市場予想と一致。発表直後はインフレ鈍化を意識してドル円が158円台まで下落する場面があったが（要確認）、その後市場がコア指数の内容を消化し切りドル買い戻しが優勢となり、NY市場終盤にかけて159.50円まで上昇、7/31以来の高値を更新した。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】米10年債入札で最高落札利回りが2007年来の高水準に</div>
            420億ドルの米10年債入札で最高落札利回りは4.683%と2007年以来の高水準を記録した（応札倍率2.53倍）。米長期金利の上昇圧力が意識され、財政懸念を背景とした金利上昇がドルの下支え材料となる一方、将来的な財政リスクも意識された。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】米7月財政赤字が2021年3月以来の最大規模に拡大</div>
            米財務省発表で7月の財政赤字は前年から拡大し、2021年3月以来最大となった。防衛費の拡大や関税還付が響いた形で、財政悪化への懸念がドルの上値を抑える一因となった（要確認）。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】欧州株が全面安、リスク回避のドル売り・円買い圧力</div>
            欧州株式市場が全面安となり、リスク回避ムードが広がった。CPI発表前の時間帯にドル売り・円買い圧力の一因になったとみられる（要確認）。
          </div>
          <div class="handover">
            <strong>本日（8/13木）への引継ぎ：</strong>
            前日NY市場でのドル円上昇（159.50円、7/31以来の高値）を引き継ぎ、米CPI通過後のドル買い戻し基調が意識される中で東京・欧州時間が推移。米10年債入札での金利急騰や米財政赤字の拡大も財政懸念の材料としてくすぶる（要確認）。本日は15:00の英GDP速報値（Q2）、21:30の米PPI・新規失業保険申請件数が重なり、複数の中重要度指標の結果次第で値動きが大きくなりやすい。
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
            <tr><td>02:01</td><td>🇺🇸 米国</td><td>10年債入札結果（最高落札利回り4.683%・応札倍率2.53倍、2007年来の高水準）（要確認・ForexFactoryのみ計上、KissFXでは前日8/12扱い）</td><td>高</td><td>—</td><td>—</td></tr>
            <tr><td>02:58</td><td>🇺🇸 米国</td><td>7月財政収支（赤字拡大、2021年3月以来最大）（要確認・ForexFactoryのみ計上、KissFXでは前日8/12扱い）</td><td>中</td><td>-3483億ドル</td><td>-1203億ドル</td></tr>
            <tr><td>08:01</td><td>🇬🇧 英国</td><td>RICS住宅価格指数（KissFX・ForexFactory一致）</td><td>★★</td><td>-30%</td><td>-33%</td></tr>
            <tr><td>08:50</td><td>🇯🇵 日本</td><td>国内企業物価指数（PPI）前月比（要確認・KissFXのみ）</td><td>★★</td><td>+0.6%</td><td>+0.4%</td></tr>
            <tr><td>08:50</td><td>🇯🇵 日本</td><td>国内企業物価指数（PPI）前年比（KissFX・ForexFactory一致）</td><td>★★</td><td>+7.4%</td><td>+7.1%</td></tr>
            <tr><td>09:15</td><td>🇦🇺 豪州</td><td>RBA副総裁ケント発言（要確認・ForexFactoryのみ）</td><td>低</td><td>要人発言</td><td>—</td></tr>
            <tr><td>12:00</td><td>🇳🇿 NZ</td><td>インフレ期待（四半期）（要確認・ForexFactoryのみ）</td><td>中</td><td>—</td><td>+2.53%</td></tr>
            <tr><td><strong>15:00</strong></td><td>🇬🇧 英国</td><td><strong>GDP速報値（Q2、前期比）</strong>（KissFX・ForexFactory一致）</td><td><strong>★★★</strong></td><td><strong>+0.4%</strong></td><td>+0.6%</td></tr>
            <tr><td><strong>15:00</strong></td><td>🇬🇧 英国</td><td><strong>GDP速報値（Q2、前年比）</strong>（要確認・KissFXのみ）</td><td><strong>★★★</strong></td><td><strong>+1.1%</strong></td><td>+0.9%</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>GDP（前月比）（予想値がソース間で差異：KissFX -0.1%／FF 0.0%、要確認）</td><td>★★★</td><td>-0.1%〜0.0%</td><td>+0.1%</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>鉱工業生産（前月比）（KissFX・ForexFactory一致）</td><td>★★</td><td>+0.1%</td><td>-0.5%</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>製造業生産高（前月比）（KissFX・ForexFactory一致）</td><td>★★</td><td>-0.1%</td><td>+0.1%</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>商品貿易収支（KissFX・ForexFactoryほぼ一致）</td><td>★★</td><td>-205.0億ポンド</td><td>-186.6億ポンド</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>建設業算出高（前月比）（要確認・ForexFactoryのみ）</td><td>低</td><td>-0.3%</td><td>-0.8%</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>サービス業指数（3ヶ月/3ヶ月）（要確認・ForexFactoryのみ）</td><td>低</td><td>+0.5%</td><td>+0.7%</td></tr>
            <tr><td>15:00</td><td>🇬🇧 英国</td><td>企業設備投資速報値（前期比）（要確認・ForexFactoryのみ）</td><td>低</td><td>-0.3%</td><td>+0.7%</td></tr>
            <tr><td>15:02</td><td>🇨🇳 中国</td><td>対中直接投資（年初来・前年比）（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>-5.0%</td></tr>
            <tr><td>15:30</td><td>🇨🇭 スイス</td><td>生産者輸入価格（前年比）（要確認・KissFXのみ）</td><td>★</td><td>—</td><td>-2.1%</td></tr>
            <tr><td>15:30</td><td>🇨🇭 スイス</td><td>生産者物価指数（前月比）（要確認・ForexFactoryのみ）</td><td>低</td><td>-0.2%</td><td>-0.3%</td></tr>
            <tr><td>17:03</td><td>🇨🇳 中国</td><td>マネーサプライM2（前年比）（要確認・ForexFactoryのみ）</td><td>低</td><td>+7.9%</td><td>+8.0%</td></tr>
            <tr><td>17:03</td><td>🇨🇳 中国</td><td>新規融資（要確認・ForexFactoryのみ）</td><td>低</td><td>-500億元</td><td>1兆610億元</td></tr>
            <tr><td>18:00</td><td>🇪🇺 ユーロ圏</td><td>鉱工業生産（前月比）（予想値がソース間で軽微な差異：KissFX ±0.0%／FF -0.1%、要確認）</td><td>★★</td><td>±0.0%〜-0.1%</td><td>-0.2%</td></tr>
            <tr><td>21:15</td><td>🇺🇸 米国</td><td>ハマックFRB総裁発言（KissFX・ForexFactory一致）</td><td>★★</td><td>要人発言</td><td>—</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>新規失業保険申請件数</strong>（KissFX・ForexFactory一致）</td><td><strong>★★★</strong></td><td><strong>20.2万件</strong></td><td>19.9万件</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>生産者物価指数（PPI）前月比</strong>（KissFX・ForexFactory一致）</td><td><strong>★★★</strong></td><td><strong>+0.2%</strong></td><td>-0.3%</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>生産者物価指数【コア】前月比</strong>（KissFX・ForexFactory一致）</td><td><strong>★★★</strong></td><td><strong>+0.3%</strong></td><td>+0.2%</td></tr>
            <tr><td>21:40</td><td>🇺🇸 米国</td><td>バーキンFRB総裁発言（KissFX・ForexFactory一致）</td><td>★★</td><td>要人発言</td><td>—</td></tr>
            <tr><td>22:30</td><td>🇬🇧 英国</td><td>CB景気先行指数（前月比）（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>-0.5%</td></tr>
            <tr><td>23:00</td><td>🇺🇸 米国</td><td>住宅ローン延滞率（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>4.44%</td></tr>
            <tr><td>23:30</td><td>🇺🇸 米国</td><td>週間天然ガス貯蔵量（KissFX・ForexFactory一致）</td><td>★</td><td>31B</td><td>+33</td></tr>
            <tr><td>23:30</td><td>🇦🇺 豪州</td><td>CB景気先行指数（前月比）（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>+0.2%</td></tr>
            <tr><td>26:00</td><td>🇺🇸 米国</td><td>30年債入札（翌日未明・要確認・KissFXのみ）</td><td>★★★</td><td>250億ドル</td><td>—</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。本日の主要市場休場はありません。本日の焦点は15:00の英GDP速報値（Q2）と21:30の米PPI・新規失業保険申請件数です。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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
