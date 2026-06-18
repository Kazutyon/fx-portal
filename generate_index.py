import glob, os

# ── 今日のデータ ──────────────────
TODAY      = '2026-06-19'
WEEKDAY    = '金'
CARD1_H3   = '円安161円超え・米国休場'
CARD1_P    = 'Juneteenth休場で米国勢不在。英小売売上高・日本CPIで欧州・アジア中心。USD/JPY161台で介入ライン警戒継続。'
CARD2_H3   = 'GBP/USD 🇬🇧🇺🇸'
CARD2_P    = '英5月小売売上高（前回-1.3%）でBOEの次の一手を確認。ハト派傾向が続けばポンド売り圧力が強まる。'
RISK_LEVEL = 'MEDIUM'
RISK_COLOR = 'var(--orange)'
RISK_P     = '米国休場で流動性低下。英小売サプライズ時は値幅増幅しやすい。USD/JPY介入警戒でポジション偏り注意。'
CARD4_H3   = '2件'
CARD4_P    = '日本CPI / 英小売売上高'
HERO_SUB   = 'Juneteenth米国休場——英小売売上高・日本CPIで欧州・アジア中心。161円突破後の介入ラインを警戒。'
FRB_RATE   = '3.50–3.75%'; FRB_STANCE = 'タカ派（年内利上げ観測）'; FRB_COLOR = 'var(--red)'
BOE_RATE   = '3.75%';      BOE_STANCE = 'ハト派寄り（次は利下げ観測）'; BOE_COLOR = 'var(--muted)'
BOJ_RATE   = '1.00%';      BOJ_STANCE = '正常化（6/16利上げ）'; BOJ_COLOR = 'var(--blue)'
ECB_RATE   = '2.25%';      ECB_STANCE = 'タカ派転換（6/11利上げ）'; ECB_COLOR = 'var(--red)'
# ────────────────────────────────────────────────────────

report_files = sorted(glob.glob('reports/*.html'), reverse=True)
DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

def make_archive_cards(files):
    cards = ''
    for i, f in enumerate(files[:12]):
        name = os.path.basename(f).replace('.html','')
        try:
            import datetime
            d = datetime.date.fromisoformat(name)
            wd = DAYS[d.strftime('%A')]
            label = f'{name}（{wd}）'
        except:
            label = name
        badge = '<span class="badge-live" style="font-size:9px;margin-left:6px;">最新</span>' if i == 0 else ''
        if i == 0:
            title = HERO_SUB[:40] + '…' if len(HERO_SUB) > 40 else HERO_SUB
            sub   = f'{CARD1_H3} / Market Risk {RISK_LEVEL}'
        else:
            title = ''; sub = ''
        cards += f'''
        <a href="{f}" class="archive-card">
          <span class="archive-card-date">{label}{badge}</span>
          <p class="archive-card-title">{title}</p>
          <p class="archive-card-sub">{sub}</p>
        </a>'''
    return cards

def make_sidebar_archive(files):
    items = ''
    for i, f in enumerate(files[:10]):
        name = os.path.basename(f).replace('.html','')
        try:
            import datetime
            d = datetime.date.fromisoformat(name)
            wd = DAYS[d.strftime('%A')]
            label = f'{name}（{wd}）'
        except:
            label = name
        items += f'<li><a href="{f}">{label}</a></li>\n'
    return items

ARCHIVE_CARDS = make_archive_cards(report_files)
SIDEBAR_ARCHIVE = make_sidebar_archive(report_files)
TOTAL = len(report_files)
LATEST_PATH = report_files[0] if report_files else f'reports/{TODAY}.html'

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AUXEN FX Portal | FXトレーダーの情報ハブ</title>
<link rel="stylesheet" href="style.css">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/logo.svg">
</head>
<body class="home-page">
<header class="mobile-header">
  <a href="index.html" class="mobile-brand">
    <img src="assets/logo.svg" alt="AUXEN">
    <span><strong>AUXEN</strong><em>FX Research Lab</em></span>
  </a>
  <a href="#mobile-menu" class="mobile-menu-button" aria-label="メニュー">
    <span></span><span></span><span></span>
  </a>
</header>

<section class="mobile-hero">
  <p class="eyebrow">AUXEN FX PORTAL</p>
  <h1>AIと統計で相場を研究する</h1>
  <p>日報・重要指標・政策金利を毎朝更新。</p>
  <span class="mobile-update">更新: {TODAY} / 毎朝7時</span>
</section>

<nav class="mobile-quick-grid" id="mobile-menu" aria-label="スマホ用メニュー">
  <a href="#latest-report"><span>最新日報</span><strong>今日の戦略</strong></a>
  <a href="{LATEST_PATH}#calendar"><span>重要指標</span><strong>本日の予定</strong></a>
  <a href="{LATEST_PATH}#ranking"><span>通貨ランキング</span><strong>優先通貨</strong></a>
  <a href="#rates"><span>政策金利</span><strong>主要中銀</strong></a>
  <a href="#reports"><span>アーカイブ</span><strong>過去日報</strong></a>
  <a href="contact.html"><span>お問い合わせ</span><strong>連絡先</strong></a>
</nav>

<section class="mobile-latest-card" id="latest-report">
  <p class="eyebrow">{TODAY}（{WEEKDAY}） — AI Daily Report</p>
  <h2>{HERO_SUB}</h2>
  <p>{CARD1_H3}。{CARD2_P}</p>
  <a href="{LATEST_PATH}" class="btn-primary">詳細を読む →</a>
</section>

<div class="app">
  <aside class="sidebar">
    <div class="brand">
      <div class="logo"><img src="assets/logo.svg" alt="AUXEN"></div>
      <div><h1>AUXEN</h1><p>FX Research Lab</p></div>
    </div>
    <nav class="side-nav">
      <span class="nav-section">メイン</span>
      <a href="index.html" class="active">🏠 ダッシュボード</a>
      <a href="#reports">📰 日報アーカイブ</a>
      <span class="nav-section">データ</span>
      <a href="#rates">📊 政策金利</a>
      <a href="#strength">💹 通貨強弱 <span class="badge-soon">Soon</span></a>
      <span class="nav-section">ツール・販売</span>
      <a href="#tools">🔧 インジケーター <span class="badge-soon">Soon</span></a>
      <a href="#tools">🤖 EA <span class="badge-soon">Soon</span></a>
      <a href="#analysis">📈 チャート分析 <span class="badge-soon">Soon</span></a>
      <span class="nav-section">サイト情報</span>
      <a href="about.html">ℹ️ About</a>
      <a href="disclaimer.html">⚠️ 免責事項</a>
      <a href="contact.html">✉️ お問い合わせ</a>
    </nav>
    <div class="sidebar-archive">
      <div style="margin-top:28px;padding-top:20px;border-top:1px solid var(--line);">
        <p style="font-size:11px;color:var(--muted);margin:0 0 10px;letter-spacing:.06em;text-transform:uppercase;">最新レポート</p>
        <ul class="archive-list">{SIDEBAR_ARCHIVE}</ul>
      </div>
    </div>
  </aside>
  <main class="main">
    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI-Powered Research</p>
        <h2>AIと統計で相場を研究する <span class="badge-live">LIVE</span></h2>
        <p class="sub">日報・政策金利・ツールをここに集約。AIが毎朝7時（JST）に市場分析を自動更新。</p>
      </div>
      <div class="date-card">
        <span>Last Update</span>
        <strong>{TODAY}</strong>
        <em>毎朝7時 自動更新</em>
      </div>
    </header>
    <div class="hub-section desktop-latest-section"><p class="hub-label">📰 最新日報</p></div>
    <div class="report-feature desktop-report-feature">
      <div class="report-feature-header">
        <div>
          <p class="eyebrow">{TODAY}（{WEEKDAY}） — AI Daily Report</p>
          <h3>{HERO_SUB}</h3>
          <p style="color:var(--muted);font-size:14px;margin:8px 0 0;">{CARD1_H3}。{CARD2_P}</p>
        </div>
        <a href="{LATEST_PATH}" class="btn-primary">詳細を読む →</a>
      </div>
      <div class="summary-grid">
        <div class="card highlight">
          <p class="label">一言まとめ</p>
          <h3>{CARD1_H3}</h3>
          <p>{CARD1_P}</p>
        </div>
        <div class="card">
          <p class="label">最注目通貨</p>
          <h3>{CARD2_H3}</h3>
          <p>{CARD2_P}</p>
        </div>
        <div class="card">
          <p class="label">Market Risk</p>
          <h3 style="color:{RISK_COLOR}">{RISK_LEVEL}</h3>
          <p>{RISK_P}</p>
        </div>
        <div class="card">
          <p class="label">本日の重要指標</p>
          <h3>{CARD4_H3}</h3>
          <p>{CARD4_P}</p>
        </div>
      </div>
    </div>
    <div class="hub-section" id="reports"><p class="hub-label">📂 日報アーカイブ</p></div>
    <div class="panel full" style="margin-bottom:20px;">
      <div class="panel-head"><h3>過去のレポート</h3><span>全{TOTAL}件</span></div>
      <div class="archive-grid">{ARCHIVE_CARDS}</div>
    </div>
    <div class="hub-section" id="rates"><p class="hub-label">📊 データコーナー</p></div>
    <div class="content-grid" style="margin-bottom:20px;">
      <div class="panel">
        <div class="panel-head"><h3>🏦 主要中銀 政策金利</h3><span>{TODAY} 現在</span></div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>金利</th><th>スタンス</th></tr></thead>
          <tbody>
            <tr><td>FRB</td><td>🇺🇸 USD</td><td><strong>{FRB_RATE}</strong></td><td style="color:{FRB_COLOR};font-size:12px;">{FRB_STANCE}</td></tr>
            <tr><td>BOE</td><td>🇬🇧 GBP</td><td><strong>{BOE_RATE}</strong></td><td style="color:{BOE_COLOR};font-size:12px;">{BOE_STANCE}</td></tr>
            <tr><td>日銀</td><td>🇯🇵 JPY</td><td><strong>{BOJ_RATE}</strong></td><td style="color:{BOJ_COLOR};font-size:12px;">{BOJ_STANCE}</td></tr>
            <tr><td>ECB</td><td>🇪🇺 EUR</td><td><strong>{ECB_RATE}</strong></td><td style="color:{ECB_COLOR};font-size:12px;">{ECB_STANCE}</td></tr>
            <tr><td>RBA</td><td>🇦🇺 AUD</td><td style="color:var(--muted);">要確認</td><td style="color:var(--muted);font-size:12px;">—</td></tr>
            <tr><td>RBNZ</td><td>🇳🇿 NZD</td><td style="color:var(--muted);">要確認</td><td style="color:var(--muted);font-size:12px;">—</td></tr>
            <tr><td>BOC</td><td>🇨🇦 CAD</td><td style="color:var(--muted);">要確認</td><td style="color:var(--muted);font-size:12px;">—</td></tr>
            <tr><td>SNB</td><td>🇨🇭 CHF</td><td style="color:var(--muted);">要確認</td><td style="color:var(--muted);font-size:12px;">—</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ FRB/BOE/日銀/ECBは複数ソース確認済み。RBA/RBNZ/BOC/SNBは月曜日報で更新予定。</p>
      </div>
      <div class="panel" id="strength">
        <div class="panel-head"><h3>💹 通貨強弱</h3><span class="badge-soon">Coming Soon</span></div>
        <div class="coming-soon-block">
          <div class="coming-soon-icon">📈</div>
          <p style="color:var(--text);font-weight:600;">通貨強弱チャートを追加予定</p>
          <p style="font-size:13px;">主要8通貨のリアルタイム強弱スコア</p>
        </div>
      </div>
    </div>
    <div class="hub-section" id="tools"><p class="hub-label">🔧 ツール・販売</p></div>
    <div class="content-grid" style="margin-bottom:20px;">
      <div class="panel">
        <div class="panel-head"><h3>📐 MT4インジケーター</h3><span class="badge-soon">Coming Soon</span></div>
        <div class="coming-soon-block">
          <div class="coming-soon-icon">🔧</div>
          <p style="color:var(--text);font-weight:600;">独自開発インジケーター</p>
          <p style="font-size:13px;">4H・15分足特化のトレンドフォロー系</p>
        </div>
      </div>
      <div class="panel">
        <div class="panel-head"><h3>🤖 EA（自動売買）</h3><span class="badge-soon">Coming Soon</span></div>
        <div class="coming-soon-block">
          <div class="coming-soon-icon">🤖</div>
          <p style="color:var(--text);font-weight:600;">バックテスト済みEA</p>
          <p style="font-size:13px;">USD/JPY・EUR/USD対応</p>
        </div>
      </div>
    </div>
    <div class="hub-section" id="analysis"><p class="hub-label">📈 独自チャート分析</p></div>
    <div class="panel full">
      <div class="panel-head"><h3>週次・月次の独自分析レポート</h3><span class="badge-soon">Coming Soon</span></div>
      <div class="coming-soon-block">
        <div class="coming-soon-icon">📊</div>
        <p style="color:var(--text);font-weight:600;">日報に載らない中長期の相場見通し・独自チャート分析を公開予定</p>
        <p style="font-size:13px;">週足・月足レベルのトレンド分析、重要節目の解説</p>
      </div>
    </div>
  </main>
</div>
<nav class="mobile-bottom-nav" aria-label="スマホ下部ナビ">
  <a href="index.html" class="active">Home</a>
  <a href="#latest-report">日報</a>
  <a href="{LATEST_PATH}#calendar">指標</a>
  <a href="#reports">Menu</a>
</nav>
<footer class="footer">
  <div>© 2026 AUXEN FX Portal — 本サイトの情報は投資助言ではありません。FX取引はリスクを伴います。</div>
  <div class="footer-links">
    <a href="about.html">About</a>
    <a href="disclaimer.html">免責事項</a>
    <a href="privacy.html">プライバシーポリシー</a>
    <a href="terms.html">利用規約</a>
    <a href="contact.html">お問い合わせ</a>
  </div>
</footer>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('✅ index.html 再生成完了')
