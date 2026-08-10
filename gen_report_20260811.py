#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FX日報 2026-08-11（火）生成スクリプト"""
import glob, os
from datetime import date

TODAY = '2026-08-11'
WEEKDAY = '火'

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

HERO_SUB = 'ドル円はNY市場で159.29円まで反発。日本は「山の日」で休場となる中、13:30のRBA政策金利発表を経て明日の米CPIに関心が移る。'

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
        <em>火曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>米ユーロ売り・円買い介入疑惑が影を落とす中、ドル円は159円台へ切り返す</h3>
        <p>8/10（月）のNY市場でドル円は前日比+1.53円の159.29円で終値を迎えた。日銀の9月利上げ示唆報道で一時158.43円まで下押しされたが、追加の円買い介入が入らなかったことを見極めた短期筋が反転。中東情勢悪化を背景にWTI原油先物が82.38ドル付近まで上昇したことによる「有事のドル買い」、ハマック・クリーブランド連銀総裁のタカ派発言、高市政権の積極財政姿勢による円売り圧力（要確認）も重なった。東京早朝にかけてはドル円159.10円台まで上値を伸ばし、ユーロ円・豪ドル円などクロス円も高値を更新している。本日は日本が「山の日」で株式市場等が休場となる中、13:30のRBA政策金利発表（4.35%据え置き予想）を経て、市場の関心は明日8/12の米CPI発表へ移りつつある。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>AUD/USD 🇦🇺🇺🇸</h3>
        <p>13:30のRBA政策金利発表（4.35%据え置き予想）と14:30の総裁記者会見で本日唯一の高重要度イベント</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">MEDIUM</h3>
        <p>RBA政策金利発表・記者会見に加え、米国のユーロ売り・円買い介入疑惑（FT報道）を巡る神経質さが残る。日本は山の日で休場、米国の高重要度指標はなし（要確認）</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>11件</h3>
        <p>RBA政策金利発表・声明・記者会見 / NFIB中小企業楽観指数 / 中古住宅販売件数 等（日本は山の日で市場休場）</p>
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
              <li>日本（山の日）※株式・債券市場等が休場。FX取引自体は行われるが実需フローが細り薄商いに注意（KissFX・ForexFactory一致）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>13:30 🇦🇺 RBA政策金利発表（4.35%据え置き予想）<span class="badge-important">★最重要</span></li>
              <li>13:30 🇦🇺 RBA四半期金融政策報告（SMP）<span class="badge-important">★</span></li>
              <li>14:30 🇦🇺 RBA総裁記者会見<span class="badge-important">★最重要</span></li>
              <li>19:00 🇺🇸 NFIB中小企業楽観指数（予想値がソース間で差異：KissFX97.3／FF97.5、要確認）</li>
              <li>23:00 🇺🇸 中古住宅販売件数（予想405万件・前回409万件）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>米国のユーロ売り・円買い介入疑惑が引き続き重石に</strong>：フィナンシャル・タイムズのスクープ報道によると、7/31に米国が実施した為替介入（ユーロ売り・円買い）についてECBへの事前通告がなく、ラガルド総裁とベッセント米財務長官の電話協議は取引執行後の8/1にずれ込んだとされる。政治的な意図を指摘する分析もある（要確認・分析含む）</li>
              <li><strong>ドル円はNY市場で159.29円まで反発</strong>：前日NY終値157.76円比+1.53円。日銀の9月利上げ示唆報道による下押しを、追加の円買い介入なしを確認した短期筋の反転が上回った</li>
              <li><strong>「有事のドル買い」も支援材料に</strong>：中東情勢悪化を背景にWTI原油先物が82.38ドル付近まで上昇し、ドル買いを誘発</li>
              <li><strong>ハマック・クリーブランド連銀総裁のタカ派発言</strong>：「おそらくある程度の回数の利上げが必要」と発言。短期金融市場は9月利上げを引き続き50%織り込む</li>
              <li><strong>東京早朝はドル円159.10円台まで上値を伸ばす</strong>：WTI原油先物価格の上昇を背景に前日NY序盤高値159.06円を突破。ユーロ円183.76円、豪ドル円112.34円までクロス円も高値更新</li>
              <li><strong>本日は日本が山の日で休場</strong>：RBA政策金利発表を経て、市場の関心は明日8/12の米CPI発表へ徐々に移行</li>
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
          8/11（火）は日本が「山の日」で株式市場等が休場となる中で取引スタート。前日のNY市場ではドル円が159.29円まで反発し、前日比+1.53円のドル高で終値を迎えた。日銀の9月利上げ示唆報道を受け一時158.43円まで下押しされたが、追加の円買い介入が入らなかったことを見極めた短期筋が反転。中東情勢悪化によるWTI原油先物上昇を受けた「有事のドル買い」、ハマック・クリーブランド連銀総裁のタカ派発言も相場を押し上げた。東京早朝にかけてはドル円159.10円台まで上値を伸ばし、ユーロ円・豪ドル円などクロス円も高値を更新している。本日13:30のRBA政策金利発表（4.35%据え置き予想）、14:30の総裁記者会見を経て、市場の関心は明日8/12の米CPI発表へ移りつつある。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派・据え置き、9月利上げ観測50%織り込み） / 日銀 1.00%（正常化継続、9月利上げ示唆報道あり・要確認） / 豪RBA 4.35%（本日13:30政策金利発表・据え置き予想）
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
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング1位（スコア66・適）。NY市場での反発を引き継ぎ159円台で方向感を探る。介入警戒ラインも意識</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>USD/CAD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング2位（スコア56・候補）。原油高を背景にCADが底堅く下押し圧力</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>GBP/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング3位（スコア56・候補）。ドル円の反発に連動しつつレンジ内推移</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">ランキング4位（スコア45・見送り）。ドル全面高の流れの中でも底堅さを維持</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ランキング5位（スコア42・見送り）。方向感に乏しくレンジ推移が継続</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは本日05:07 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで判断してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-08-10）</h3>
          <span>昨日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】ドル円がNY市場で159.29円まで反発、前日比+1.53円のドル高</div>
            8/10のNY市場でドル円は159.29円で終値を迎え、前営業日NY終値（157.76円）比で約1円53銭のドル高となった。日銀の9月利上げ示唆報道を受け一時158.43円まで下押しされたが、「追加の円買い介入がなく、円高を見込んでいた短期筋が反転」したことが上昇の主因（要確認）。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】中東情勢悪化を背景にWTI原油先物が上昇、「有事のドル買い」を誘発</div>
            中東情勢の悪化を背景にWTI原油先物が82.38ドル付近まで上昇。地政学リスクの高まりが「有事のドル買い」を誘引し、ドル円の上昇を後押しした。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】ハマック・クリーブランド連銀総裁のタカ派発言で9月利上げ観測を再燃</div>
            ハマック総裁は「おそらくある程度の回数の利上げが必要」と発言。短期金融市場では9月の利上げ観測が引き続き50%織り込まれており、7月雇用統計の下振れにもかかわらず利上げ観測は後退していない。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】米国のユーロ売り・円買い介入、ECBへの事前通告なしと報道</div>
            フィナンシャル・タイムズのスクープ報道によると、7/31に米国がユーロを売り円を買う為替介入を実施した際、ECBには事前に知らされておらず、取引執行後に把握したという。ラガルド総裁とベッセント米財務長官の電話協議は翌8/1にずれ込んだとされ、市場関係者からは政治的な意図を指摘する分析もある（要確認・分析含む）。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック⑤】高市政権の積極財政姿勢による円売り圧力も指摘</div>
            日本の高市政権による積極財政方針への警戒から、円売り圧力が意識されているとの指摘がある（要確認）。
          </div>
          <div class="handover">
            <strong>本日（8/11火）への引継ぎ：</strong>
            前日NY市場でのドル円反発（159.29円）を引き継ぎ、東京早朝も159.10円台までじり高。日本は本日「山の日」で株式市場等が休場となり、実需フローの細った薄商いが想定される。13:30のRBA政策金利発表（4.35%据え置き予想）と14:30の総裁記者会見でAUD方向感が定まるほか、市場の関心は明日8/12の米CPI発表へ徐々に移行しつつある。米国のユーロ売り・円買い介入を巡る報道も引き続きくすぶり材料として意識される（要確認）。
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
            <tr><td><strong>終日</strong></td><td>🇯🇵 日本</td><td><strong>山の日で株式・債券市場等が休場</strong>（KissFX・ForexFactory一致）</td><td><strong>◎</strong></td><td>—</td><td>—</td></tr>
            <tr><td>04:00</td><td>🇺🇸 米国</td><td>FOMC高官（ハマック・クリーブランド連銀総裁）発言（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>—</td></tr>
            <tr><td>08:01</td><td>🇬🇧 英国</td><td>BRC小売売上高調査 前年比（要確認・ForexFactoryのみ）</td><td>低</td><td>+1.6%</td><td>+1.7%</td></tr>
            <tr><td>10:30</td><td>🇦🇺 豪州</td><td>NAB企業信頼感指数（KissFX・ForexFactory一致）／企業景況感指数（要確認・KissFXのみ、前回+3）</td><td>↑</td><td>—</td><td>-5</td></tr>
            <tr><td><strong>13:30</strong></td><td>🇦🇺 豪州</td><td><strong>RBA政策金利発表・声明</strong>（KissFX・ForexFactory一致）</td><td><strong>★★★</strong></td><td><strong>4.35%据え置き</strong></td><td>4.35%</td></tr>
            <tr><td><strong>13:30</strong></td><td>🇦🇺 豪州</td><td><strong>RBA四半期金融政策報告（SMP）</strong>（一致）</td><td><strong>★★★</strong></td><td>—</td><td>—</td></tr>
            <tr><td><strong>14:30</strong></td><td>🇦🇺 豪州</td><td><strong>RBA総裁記者会見</strong>（一致）</td><td><strong>★★★</strong></td><td>要人発言</td><td>—</td></tr>
            <tr><td>17:00</td><td>🇪🇺 ユーロ圏</td><td>イタリア貿易収支（要確認・ForexFactoryのみ）</td><td>低</td><td>47.4億ユーロ</td><td>47.9億ユーロ</td></tr>
            <tr><td>19:00</td><td>🇺🇸 米国</td><td>NFIB中小企業楽観指数（予想値がソース間で差異：KissFX97.3／FF97.5、要確認）</td><td>↑</td><td>97.3〜97.5</td><td>97.4</td></tr>
            <tr><td>21:15</td><td>🇺🇸 米国</td><td>ADP週間雇用者数変化（要確認・ForexFactoryのみ）</td><td>低</td><td>—</td><td>+15.0K</td></tr>
            <tr><td>23:00</td><td>🇺🇸 米国</td><td>中古住宅販売件数（KissFX・ForexFactory一致）</td><td>→</td><td>405万件</td><td>409万件</td></tr>
            <tr><td>26:00</td><td>🇺🇸 米国</td><td>3年債入札（翌日未明・要確認・KissFXのみ）</td><td>→</td><td>580億ドル</td><td>—</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。本日の主要市場休場は日本（山の日）のみで、KissFX・ForexFactory両ソースで確認済みです。本日の焦点はRBA政策金利発表・記者会見、および明日8/12の米CPI発表です。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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
