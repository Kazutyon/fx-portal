import glob, os, datetime

DATE    = '2026-07-14'
WEEKDAY = '火'

DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

report_files = sorted(glob.glob('reports/*.html'), reverse=True)

def make_sidebar(files, today):
    items = f'        <li class="active"><a href="{today}.html">{today}（{WEEKDAY}）</a></li>\n'
    for f in files[:9]:
        href = os.path.basename(f).replace('.html','')
        name = href
        try:
            d = datetime.date.fromisoformat(name)
            wd = DAYS[d.strftime('%A')]
            label = f'{name}（{wd}）'
        except Exception:
            label = name
        items += f'        <li><a href="{name}.html">{label}</a></li>\n'
    return items

SIDEBAR_ARCHIVE = make_sidebar(report_files, DATE)

html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FX日報 2026-07-14（火） | AUXEN FX Portal</title>
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
  <h1>FX日報 2026-07-14（火）</h1>
  <p>米6月CPIとウォーシュFRB議長の初議会証言を控え、USD/JPYは162円台を挟んだレンジで神経質な値動き。</p>
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
""" + SIDEBAR_ARCHIVE + """      </ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 2026-07-14（火）<span class="badge-live">最新</span></h2>
        <p class="sub">米6月CPIとウォーシュFRB議長の初議会証言を控え、USD/JPYは162円台を挟んだレンジで神経質な値動き。</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>2026-07-14</strong>
        <em>火曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>USD/JPY 米CPI発表待ちのレンジ</h3>
        <p>本日21:30の米6月CPIと直後のウォーシュFRB議長・下院証言が最大の材料。結果次第で162円台を挟んだ振れ幅拡大を想定。</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>米CPI・ウォーシュ議長証言の影響を最も強く受ける通貨ペア。4Hデイトレ適性ランキングは3位（スコア31）</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red)">HIGH</h3>
        <p>米CPIとウォーシュ議長初証言が重なる高ボラティリティの一日。米・イラン緊張再燃も継続材料</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>4件</h3>
        <p>米CPI・ウォーシュ議長証言・日本鉱工業生産・独ZEW景況感指数（時刻は一部要確認）</p>
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
              <li>なし（本日7/14は日米欧・主要市場すべて通常営業。要確認範囲内で祝日情報なし）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
              <li>13:30 🇯🇵 5月 鉱工業生産（確報値）</li>
              <li>18:00 🇩🇪 7月 ZEW景況感指数（発表時刻は要確認）</li>
              <li>21:30 🇺🇸 6月 消費者物価指数（CPI）<span class="badge-important">★最重要</span></li>
              <li>23:00 🇺🇸 ウォーシュFRB議長 下院金融サービス委員会 証言（開始時刻は要確認）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
              <li><strong>米6月CPIは前月比マイナス圏が予想される</strong>：総合CPIは前月比-0.1%予想（5月+0.5%から反落、2020年5月以来ほぼ6年ぶりのマイナス）。米・イラン停戦観測を背景にガソリン価格が9.2%下落したことが指数を押し下げる見通し（要確認）。前年比は+3.8%への鈍化が予想される（要確認）</li>
              <li><strong>コアCPIはFRBが最も注視する数値</strong>：食品・エネルギーを除くコア指数は前年比+2.9%付近での高止まりが予想される（要確認）。ウォーシュ新議長下でのタカ派スタンスを裏付けるかが焦点</li>
              <li><strong>ウォーシュFRB議長が就任後初の議会証言</strong>：CPI発表の約90分後に下院金融サービス委員会で証言予定。翌7/15にはPPI発表直後に上院銀行委員会でも証言する日程（要確認）</li>
              <li><strong>米・イラン軍事的緊張が週明けに再燃</strong>：週末に米国とイランが攻撃を応酬したと伝わり、NY原油(WTI)先物が一時3%超上昇。地政学リスクの高まりがドル買い・原油高材料として意識されている</li>
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
          7/14（火）の東京市場は、前日のGPIF思惑を巡る乱高下を経て、米CPI発表とウォーシュ議長証言を控えたポジション調整が中心の展開。USD/JPYは162円台を挟んだレンジで方向感に乏しいが、CPI結果とウォーシュ議長の発言次第では振れ幅が拡大しやすい一日。米・イラン緊張の再燃を受けた原油高もドルの下支え材料として意識される。<br><br>
          <strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派） / 日銀 1.00%（正常化継続） / NZ中銀 2.50%（タカ派転換）
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
              <td><strong>USD/JPY</strong><br><span style="color:var(--muted);font-size:12px;">本日最大の材料である米CPI・ウォーシュ議長証言の影響を最も強く受ける。162円台を挟んだレンジからの振れ幅拡大に注意</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>NZD/USD</strong><br><span style="color:var(--muted);font-size:12px;">4Hデイトレ適性ランキング1位（スコア48）。RBNZ利上げ後の高値もみ合いが継続</span></td>
              <td><span class="trend-up">↑</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-a">A</span></td>
              <td><strong>USD/CAD</strong><br><span style="color:var(--muted);font-size:12px;">4Hデイトレ適性ランキング2位（スコア47）。米・イラン緊張による原油急伸がCADの支え材料。BOC次回7/15会合を前に動意薄</span></td>
              <td><span class="trend-down">↓</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>EUR/USD</strong><br><span style="color:var(--muted);font-size:12px;">ウォーシュFRB議長とラガルドECB総裁のスタンス差が重石。1.14台前半のレンジ</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
            <tr>
              <td><span class="rank-badge rank-b">B</span></td>
              <td><strong>GBP/USD</strong><br><span style="color:var(--muted);font-size:12px;">BOEは次回8/6まで材料難。米CPI結果への追随的な値動きが中心</span></td>
              <td><span class="trend-range">→</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-07-13）</h3>
          <span>月曜の主要トピック</span>
        </div>
        <div class="report-body">
          <div class="topic">
            <div class="topic-title">【トピック①】米・イラン軍事衝突再燃で原油急伸、ドル買い圧力に</div>
            週明け7/13にかけて米国とイランが週末に攻撃を応酬したと伝わり、NY原油（WTI）先物は一時3%超上昇。地政学リスクの高まりを受けてドル買いが優勢となり、USD/JPYは162円台で下値の堅い展開となった。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック②】GPIF思惑が乱高下の主因に、朝方の円買いから一転円売りへ</div>
            前週金曜（7/10）の片山財務相によるGPIF等年金基金の国内投資拡大を促す発言を受けて円買いが先行し、USD/JPYは一時161.28円まで下落。しかし週明けにGPIFの基本ポートフォリオ変更は見込み薄との報道が伝わると円売りが再燃し、ロンドン時間にUSD/JPYは162.36円まで上昇した。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック③】162.36円で伸び悩み、「円安バブル」に一服感</div>
            162.36円をつけた後は達成感からの調整売りが入り、ロンドン為替ではUSD/JPY162.11円近辺、EUR/USD1.1428円近辺で推移。連日の円安進行に一服感が意識された。
          </div>
          <div class="topic">
            <div class="topic-title">【トピック④】東京午後は円安が再進行、CPI前のポジション調整も</div>
            東京市場の午後に入ると円安が進行。翌日（7/14）の米CPI発表とウォーシュ議長証言を控え、持ち高調整の動きも観測された。
          </div>
          <div class="handover">
            <strong>本日（7/14火）への引継ぎ：</strong>
            GPIF思惑による方向感の乏しい乱高下を経て、本日は21:30の米6月CPIとその約90分後のウォーシュFRB議長・下院証言が最大の材料。米・イラン情勢の緊迫化と原油動向も引き続き警戒材料。
          </div>
        </div>
      </div>

      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>📅 本日の経済指標カレンダー（全件）</h3>
          <span>検索エンジン経由・複数ソース統合（要確認あり）</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead>
            <tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr>
          </thead>
          <tbody>
            <tr><td>13:30</td><td>🇯🇵 日本</td><td>5月 鉱工業生産（確報値）</td><td>△</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>18:00（要確認）</td><td>🇩🇪 ドイツ</td><td>7月 ZEW景況感指数</td><td>○</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>21:30</td><td>🇺🇸 米国</td><td><strong>6月 消費者物価指数（CPI）</strong></td><td><strong>S</strong></td><td><strong>前月比-0.1%程度・前年比+3.8%、コア+2.9%前後（要確認）</strong></td><td>前月比+0.5%・前年比+4.2%、コア+2.9%（要確認）</td></tr>
            <tr><td>23:00（要確認）</td><td>🇺🇸 米国</td><td>ウォーシュFRB議長 下院金融サービス委員会 証言</td><td>S</td><td>—</td><td>—</td></tr>
            <tr><td colspan="6" style="color:var(--muted);font-size:12px;">以下は今週の主要スケジュール（本日集計には含めず）</td></tr>
            <tr><td>7/15(水) 21:30／翌3:00</td><td>🇺🇸 米国</td><td>6月 生産者物価指数（PPI）／ベージュブック・ウォーシュ議長上院証言</td><td>A</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>7/16(木) 21:30</td><td>🇺🇸 米国</td><td>6月 小売売上高</td><td>A</td><td>（要確認）</td><td>（要確認）</td></tr>
            <tr><td>7/17(金) 23:00</td><td>🇺🇸 米国</td><td>ミシガン大学消費者態度指数（速報値）</td><td>BB</td><td>（要確認）</td><td>（要確認）</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。本日もKissFX・Investing.com・ForexFactory・外為どっとコムへのアクセスが組織のネットワークポリシーにより拒否（403）されたため直接取得できず、検索エンジン経由で確認できた範囲のみ掲載しています。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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

with open(f'reports/{DATE}.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'reports/{DATE}.html generated')
