#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FX日報 2026-06-25 生成スクリプト"""

import glob, json, os, re
from html import unescape

TODAY = '2026-06-25'
WEEKDAY = '木'
REPORT_PATH = f'reports/{TODAY}.html'

# daytrade ranking
def make_daytrade_ranking(path='data/daytrade-ranking.json'):
    try:
        with open(path, encoding='utf-8') as f:
            payload = json.load(f)
        rankings = payload['rankings']
        updated = payload['generated_at_jst'].replace('T', ' ')[:16]
    except Exception:
        return '<tr><td colspan="8" class="daytrade-empty">初回データを準備中です</td></tr>', '準備中'
    rows = []
    for item in rankings:
        rank = item.get('rank') or '—'
        direction_class = {'上昇': 'trend-up', '下降': 'trend-down'}.get(item['direction'], 'trend-range')
        verdict_class = {'最適':'rank-best','適':'rank-good','候補':'rank-watch','見送り':'rank-skip','対象外':'rank-out'}.get(item['verdict'], 'rank-skip')
        rows.append(f'''<tr>
          <td class="daytrade-rank">{rank}</td><td><strong>{item['pair']}</strong></td>
          <td>{item['adr_5_pips']:.1f}</td><td>{item['adr_ratio_pct']:.0f}%</td>
          <td>{item['atr_h4_pips']:.1f}</td><td>{item['adx_h4']:.1f}</td>
          <td class="{direction_class}">{item['direction']}</td>
          <td><span class="daytrade-verdict {verdict_class}">{item['verdict']} {item['score']}</span></td>
        </tr>''')
    return '\n'.join(rows), updated

DAYTRADE_ROWS_HTML, DAYTRADE_UPDATED = make_daytrade_ranking()

# sidebar archive
report_files = sorted(glob.glob('reports/*.html'), reverse=True)
DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

def make_sidebar_archive(files):
    items = ''
    for i, f in enumerate(files[:10]):
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
        items += f'<li{active}><a href="{name}.html">{label}</a></li>\n'
    return items

SIDEBAR_ARCHIVE = make_sidebar_archive(report_files)

html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FX日報 2026-06-25（木） | AUXEN FX Portal</title>
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
  <h1>FX日報 2026-06-25（木）</h1>
  <p>PCE・GDP確定値ラッシュ。今夜21:30が最大の関門。</p>
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
        <h2>FX日報 2026-06-25（木）<span class="badge-live">最新</span></h2>
        <p class="sub">PCE・GDP確定値・失業保険が21:30に集中——コアPCEがFRBタカ派論の行方を決める最重要デー。</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>2026-06-25</strong>
        <em>木曜日</em>
      </div>
    </header>

    <!-- Summary cards -->
    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>ドル高基調継続</h3>
        <p>EUR/USD年初来安値圏。今夜PCEでFRB利上げ観測強まればドル一段高。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>EUR/USD 🇪🇺🇺🇸</h3>
        <p>年初来安値1.1338更新後。PCE結果次第でトレンド加速</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--yellow)">HIGH</h3>
        <p>PCE・GDP・失業保険・耐久財が21:30に集中。値動き拡大必至</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>8件</h3>
        <p>PCE / GDP確定値 / 失業保険 / 耐久財 / AUD CPI 等</p>
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
              <li>なし（主要市場は全て通常営業）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>08:50 🇯🇵 企業向けサービス価格指数（5月）予想:3.2% 前回:3.1%</li>
              <li>10:30 🇦🇺 消費者物価指数（5月）予想:4.3%<span class="badge-important">★</span></li>
              <li><strong>21:30</strong> 🇺🇸 <strong>コアPCEデフレーター（5月）</strong><span class="badge-important">★最重要</span></li>
              <li><strong>21:30</strong> 🇺🇸 <strong>GDP確定値（Q1）</strong> 予想:1.6%<span class="badge-important">★最重要</span></li>
              <li><strong>21:30</strong> 🇺🇸 <strong>新規失業保険申請件数</strong> 予想:225K<span class="badge-important">★</span></li>
              <li>21:30 🇺🇸 個人所得（5月）予想:+0.4%</li>
              <li>21:30 🇺🇸 個人消費支出（5月）</li>
              <li>21:30 🇺🇸 耐久財受注（5月速報）予想:+0.2%</li>
              <li>23:00 🇺🇸 中古住宅販売仮契約（5月）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>コアPCE上振れシナリオ</strong>：前月比+0.3%超なら9月FRB利上げ確度が高まりUSD/JPY 162円試し・EUR/USD 1.12台前半へ</li>
              <li><strong>コアPCE下振れシナリオ</strong>：前月比+0.1%以下なら利上げ観測後退でドル急落・USD/JPY 160円割れリスク</li>
              <li><strong>AUD CPI（10:30）</strong>：4.3%予想に対し上振れならAUD/USDは下降トレンドに逆らう反発余地。下振れならRBA追加利上げ観測後退でAUD売り加速</li>
              <li><strong>EUR/USD年初来安値更新圏</strong>：1.1338がサポート。割れると次の節目は1.12台。ECB追加利上げ観測後退とFRBタカ派の方向差が引き続きユーロの重石</li>
              <li><strong>USD/JPY介入警戒ライン</strong>：162円前後。前日は161円台でもみ合い。PCE上振れ+介入なければ162円試し</li>
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
          EUR/USDが前日に年初来安値1.1338まで下落。FRBの9月追加利上げ観測（一部エコノミストが指摘）とECBの追加利上げ期待後退（イラン情勢安定化による原油急落が背景）という方向差がユーロを圧迫している。USD/JPYは161円台でもみ合いが続くが、上値には162円前後の為替介入警戒ラインが控える。今夜21:30のコアPCEが今週最大のトリガー。FRBが重視するインフレ指標だけに、結果次第でドル方向性が鮮明になる。<br><br>
          <strong>政策金利：</strong> FRB 3.50〜3.75%（タカ派） / 日銀 1.00%（6/16利上げ） / ECB 2.25%（タカ派転換）
        </div>

        <div class="panel-head" style="margin-top:4px;">
          <h3>🏆 通貨ランキング</h3>
          <span>4Hトレンド・本日の優先順</span>
        </div>
        <table class="fx-table">
          <thead>
            <tr><th>ランク</th><th>ペア</th><th>4H方向</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="rank-badge rank-s">S</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">ADX35・ADR79pips。下降トレンド明確。PCE後のドル買い加速に乗りやすい</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>EUR/USD</strong><br><span style="color:var(--muted);font-size:12px;">年初来安値1.1338圏。ADX47でトレンド強。PCE上振れなら1.12台試し</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>USD/CAD</strong><br><span style="color:var(--muted);font-size:12px;">ADX47で上昇トレンド継続。ドル高局面でCAD売りも重なる</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/JPY</strong><br><span style="color:var(--muted);font-size:12px;">183円台。EUR安 vs 円安で方向感乏しい。ADX30台で注意</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-c">C</span></td>
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">ADX19と弱い。介入警戒で上値重い。161.50-162前後でレンジ消化の可能性</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
          </tbody>
        </table>

        <div class="panel-head" style="margin-top:16px;">
          <h3>📈 4Hデイトレ適性ランキング</h3>
          <span>""" + DAYTRADE_UPDATED + """ JST更新</span>
        </div>
        <div class="daytrade-table-wrap"><table class="fx-table daytrade-table">
          <thead><tr><th>順位</th><th>通貨ペア</th><th>5日ADR</th><th>5年比</th><th>4H ATR</th><th>ADX</th><th>方向</th><th>判定/点</th></tr></thead>
          <tbody>""" + DAYTRADE_ROWS_HTML + """          </tbody>
        </table></div>
        <p class="daytrade-note">価格データ: Yahoo Finance。スプレッドは概算でリアルタイム値ではありません。ランキングは売買推奨ではなく、相場環境を比較する参考情報です。</p>
      </div>

      <!-- 前日振り返り（wide） -->
      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-06-24）</h3>
          <span>昨日の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】EUR/USD、年初来安値を更新（1.1338）</div>
            ロンドン序盤にユーロドルが一時1.1338まで下落し、年初来安値を更新した。背景は中銀スタンスの方向差：FRBは9月の追加利上げを一部市場参加者が織り込み始めているのに対し、イラン情勢安定化による原油急落でECBの追加利上げ期待が後退。またAI関連株の調整で株安リスク回避のドル買いも加わった。前日NY終値（6/23）1.1382から水準を切り下げ、節目の1.1400割れを定着させた形。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】USD/JPY、161円台でもみ合い継続</div>
            東京市場では161.50〜161.69円の狭いレンジ（わずか19銭幅）で推移。週明けに162円を試した後はもみ合いに転じている。FRBのタカ派スタンスを背景にしたドル買い需要が下値を支えている一方、162円前後の為替介入警戒ラインが上値を抑制する構図が続いている。NY市場では米Q1経常収支（−2268億ドル、予想−2270億ドル）が発表されたが、ほぼ予想通りで相場への影響は限定的だった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】EUR/JPY、183円台後半に下落</div>
            ユーロドル下落に連動する形で夕刻以降に円高が進行し、ユーロ円も183円台後半まで下押し。EUR売りとJPY買いが重なったため、EUR/JPYは下方向の勢いが出た。ただしUSD/JPYが介入警戒でもみ合いのため、JPY買いの深さは限定的。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】全般的なドル高とリスク回避</div>
            ロンドン・NY市場ではAI関連株の調整が続き、リスク回避ムードでドル買いが優勢。米5月新築住宅販売件数（64.2万件予想）の結果も東京時間の話題となり、米経済の底堅さがドル支援材料として機能した。
          </div>
          <div class="handover">
            <strong>本日への引継ぎ：</strong>
            今夜21:30のコアPCEデフレーター（5月）とGDP確定値（Q1）が最大の焦点。コアPCEは前月比+0.2%前後のコンセンサスに対し上振れならFRB9月利上げ観測が強まりドル高が加速、下振れなら調整の急反落リスク。EUR/USDは1.1338が目先のサポート、割れると1.12台が射程に。USD/JPYは介入ラインの162円前後がキャップ。新規失業保険申請（予想225K）も雇用の強弱を確認する重要指標。
          </div>
        </div>
      </div>

      <!-- 経済指標カレンダー（full） -->
      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>📅 本日の経済指標カレンダー（全件）</h3>
          <span>Investing.com・ForexFactory 統合</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead><tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr></thead>
          <tbody>
            <tr><td>08:50</td><td>🇯🇵 日本</td><td>企業向けサービス価格指数（5月）</td><td>△</td><td>3.2%</td><td>3.1%</td></tr>
            <tr><td>08:50</td><td>🇯🇵 日本</td><td>対外・対内証券投資（週次）</td><td>×</td><td>—</td><td>—</td></tr>
            <tr><td><strong>10:30</strong></td><td>🇦🇺 豪州</td><td><strong>消費者物価指数（5月）</strong></td><td><strong>○</strong></td><td><strong>4.3%</strong></td><td>（要確認）</td></tr>
            <tr><td>16:00</td><td>🇩🇪 ドイツ</td><td>GFK消費者信頼感（7月）</td><td>△</td><td>—</td><td>—</td></tr>
            <tr><td>17:00</td><td>🇪🇺 ユーロ圏</td><td>ECB経済報告書</td><td>△</td><td>—</td><td>—</td></tr>
            <tr><td>18:00</td><td>🇪🇺 ユーロ圏</td><td>消費者信頼感確定値（6月）</td><td>×</td><td>—</td><td>—</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>コアPCEデフレーター（5月）</strong></td><td><strong>SS</strong></td><td><strong>（要確認）</strong></td><td>（要確認）</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>PCEデフレーター（5月）</strong></td><td><strong>S</strong></td><td><strong>（要確認）</strong></td><td>（要確認）</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>GDP確定値（Q1）</strong></td><td><strong>AA</strong></td><td><strong>1.6%</strong></td><td>（要確認）</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>新規失業保険申請件数</strong></td><td><strong>A</strong></td><td><strong>225K</strong></td><td>229K</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>失業保険継続受給者数</td><td>BB</td><td>—</td><td>—</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>個人所得（5月）</td><td>A</td><td>+0.4%</td><td>—</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td>個人消費支出（5月）</td><td>A</td><td>—</td><td>—</td></tr>
            <tr><td><strong>21:30</strong></td><td>🇺🇸 米国</td><td><strong>耐久財受注（5月速報）</strong></td><td><strong>A</strong></td><td><strong>+0.2%</strong></td><td>—</td></tr>
            <tr><td>23:00</td><td>🇺🇸 米国</td><td>中古住宅販売仮契約（5月）</td><td>BB</td><td>—</td><td>—</td></tr>
            <tr><td>24:00</td><td>🇺🇸 米国</td><td>カンザスシティ連銀製造業景況指数（6月）</td><td>B</td><td>—</td><td>—</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:10px 0 0;">重要度：米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×。（要確認）は取得時点で予想値未発表。</p>
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

with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'✅ {REPORT_PATH} generated')
