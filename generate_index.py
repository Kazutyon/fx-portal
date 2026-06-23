import glob, json, os, re
from html import unescape

# ── 今日のデータ ──────────────────
TODAY      = '2026-06-24'
WEEKDAY    = '水'
HERO_SUB   = '豪5月CPI・植田総裁発言・独IFO——3指標が本日の相場を制する。USD/JPYは161円台で介入警戒継続。'
MARKET_HOLIDAY_H3 = 'なし'
MARKET_HOLIDAY_P  = '本日（2026-06-24）は主要市場すべて通常取引日です（NYSE・LSE・東証）。'
KEY_EVENTS_ITEMS  = [
    '10:30 🇦🇺 豪5月CPI（前年比）予想4.3%',
    '15:40 🇯🇵 植田和男日銀総裁発言',
    '17:00 🇩🇪 独6月IFO企業景況感 予想85.5',
    '23:00 🇺🇸 米5月新築住宅販売件数 予想63.8万件',
]
REPORT_SUMMARY = 'AUD/USD 豪CPI上振れで買い / USD/JPY 162円介入ライン警戒'
RISK_LEVEL = 'MEDIUM'
FRB_RATE   = '3.50–3.75%'; FRB_STANCE = 'タカ派（9月追加利上げ観測強）'; FRB_COLOR = 'var(--red)'
BOE_RATE   = '3.75%';      BOE_STANCE = 'ハト派寄り（次は利下げ観測）'; BOE_COLOR = 'var(--muted)'
BOJ_RATE   = '1.00%';      BOJ_STANCE = '正常化（6/16利上げ・次回7月据え置き観測）'; BOJ_COLOR = 'var(--blue)'
ECB_RATE   = '2.25%';      ECB_STANCE = 'タカ派転換（6/11利上げ・追加観測あり）'; ECB_COLOR = 'var(--red)'
RBA_RATE   = '4.35%';      RBA_STANCE = 'タカ派（6/16据え置き・追加利上げ余地）'; RBA_COLOR = 'var(--red)'
RBNZ_RATE  = '2.25%';      RBNZ_STANCE = 'タカ派寄り（5/27据え置き・利上げ票あり）'; RBNZ_COLOR = 'var(--red)'
BOC_RATE   = '2.25%';      BOC_STANCE = '中立（6/10・5会合連続据え置き）'; BOC_COLOR = 'var(--muted)'
SNB_RATE   = '0.00%';      SNB_STANCE = '中立（6/18据え置き・為替介入警戒）'; SNB_COLOR = 'var(--muted)'
# ────────────────────────────────────────────────────────

KEY_EVENTS_LIST_HTML = '\n'.join(f'      <li>{item}</li>' for item in KEY_EVENTS_ITEMS)

def make_daytrade_ranking(path='data/daytrade-ranking.json'):
    try:
        with open(path, encoding='utf-8') as f:
            payload = json.load(f)
        rankings = payload['rankings']
        updated = payload['generated_at_jst'].replace('T', ' ')[:16]
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
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

# アーカイブ一覧（reportsフォルダを自動取得）
report_files = sorted(glob.glob('reports/*.html'), reverse=True)
DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}

def clean_text(value):
    value = re.sub(r'<[^>]+>', '', value or '')
    return unescape(value).strip()

def shorten(value, limit=42):
    value = clean_text(value)
    return value[:limit] + '…' if len(value) > limit else value

def extract_report_summary(path):
    try:
        with open(path, encoding='utf-8') as f:
            text = f.read()
    except OSError:
        return '', ''

    title_match = re.search(r'<p class="sub">(.*?)</p>', text, re.S)
    title = shorten(title_match.group(1), 42) if title_match else ''
    summary_match = re.search(r'<p class="label">一言まとめ</p>\s*<h3>(.*?)</h3>', text, re.S)
    risk_match = re.search(r'<p class="label">Market Risk</p>\s*<h3[^>]*>(.*?)</h3>', text, re.S)
    sub_parts = []
    if summary_match:
        sub_parts.append(shorten(summary_match.group(1), 24))
    if risk_match:
        sub_parts.append(f'Market Risk {shorten(risk_match.group(1), 12)}')
    return title, ' / '.join(sub_parts)

def make_archive_cards(files):
    cards = ''
    for i, f in enumerate(files[:12]):
        href = f.replace(os.sep, '/')
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
            sub   = f'{REPORT_SUMMARY} / Market Risk {RISK_LEVEL}'
        else:
            title, sub = extract_report_summary(f)
        cards += f'''
        <a href="{href}" class="archive-card">
          <span class="archive-card-date">{label}{badge}</span>
          <p class="archive-card-title">{title}</p>
          <p class="archive-card-sub">{sub}</p>
        </a>'''
    return cards

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
        except:
            label = name
        items += f'<li><a href="{href}">{label}</a></li>\n'
    return items

ARCHIVE_CARDS = make_archive_cards(report_files)
SIDEBAR_ARCHIVE = make_sidebar_archive(report_files)
TOTAL = len(report_files)
LATEST_PATH = report_files[0].replace(os.sep, '/') if report_files else f'reports/{TODAY}.html'

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AUXEN FX Portal | FXトレーダーの情報ハブ</title>
<link rel="stylesheet" href="style.css">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/logo.svg">
<script data-goatcounter="https://auxen.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="https://cdn.jsdelivr.net/npm/twemoji@14.0.2/dist/twemoji.min.js" crossorigin="anonymous"></script>
<script>document.addEventListener('DOMContentLoaded',function(){{twemoji.parse(document.body,{{folder:'svg',ext:'.svg',base:'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/'}});}});</script>
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
  <a href="archive.html"><span>アーカイブ</span><strong>過去日報</strong></a>
  <a href="contact.html"><span>お問い合わせ</span><strong>連絡先</strong></a>
</nav>

<section class="mobile-latest-card" id="latest-report">
  <p class="eyebrow">{TODAY}（{WEEKDAY}） — AI Daily Report</p>
  <h2>{HERO_SUB}</h2>
  <div class="mobile-latest-points">
    <div>
      <span>本日の市場休場</span>
      <strong>{MARKET_HOLIDAY_H3}</strong>
      <p>{MARKET_HOLIDAY_P}</p>
    </div>
    <div>
      <span>必見経済指標</span>
      <ul class="key-events-list">
{KEY_EVENTS_LIST_HTML}
      </ul>
    </div>
  </div>
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
      <a href="index.html" class="active"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/></svg>ダッシュボード</a>
      <a href="archive.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="12" y2="17"/></svg>日報アーカイブ</a>
      <a href="#market-news"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v2"/><rect x="2" y="8" width="8" height="14" rx="1"/><line x1="6" y1="12" x2="6" y2="12"/><line x1="4" y1="16" x2="8" y2="16"/></svg>FXニュース</a>
      <span class="nav-section">データ</span>
      <a href="#rates"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/></svg>政策金利</a>
      <a href="#strength"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>デイトレ適性</a>
      <span class="nav-section">ツール・販売</span>
      <a href="#tools"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/><circle cx="8" cy="6" r="2"/><circle cx="17" cy="12" r="2"/><circle cx="11" cy="18" r="2"/></svg>インジケーター <span class="badge-soon">Soon</span></a>
      <a href="#tools"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="1"/><line x1="9" y1="7" x2="9" y2="4"/><line x1="12" y1="7" x2="12" y2="4"/><line x1="15" y1="7" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="17"/><line x1="12" y1="20" x2="12" y2="17"/><line x1="15" y1="20" x2="15" y2="17"/><line x1="4" y1="9" x2="7" y2="9"/><line x1="4" y1="12" x2="7" y2="12"/><line x1="4" y1="15" x2="7" y2="15"/><line x1="17" y1="9" x2="20" y2="9"/><line x1="17" y1="12" x2="20" y2="12"/><line x1="17" y1="15" x2="20" y2="15"/></svg>EA <span class="badge-soon">Soon</span></a>
      <a href="#analysis"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><polyline points="7 16 11 11 15 14 19 7"/></svg>チャート分析 <span class="badge-soon">Soon</span></a>
      <span class="nav-section">サイト情報</span>
      <a href="about.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>About</a>
      <a href="disclaimer.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>免責事項</a>
      <a href="contact.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>お問い合わせ</a>
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
        </div>
        <a href="{LATEST_PATH}" class="btn-primary">詳細を読む →</a>
      </div>
      <div class="today-priority-wrap">
        <div class="market-holiday-bar">
          <span class="mh-label">市場休場</span>
          <strong class="mh-title">{MARKET_HOLIDAY_H3}</strong>
          <span class="mh-desc">{MARKET_HOLIDAY_P}</span>
        </div>
        <div class="priority-card key-events-card">
          <p class="label">必見経済指標</p>
          <ul class="key-events-list">
{KEY_EVENTS_LIST_HTML}
          </ul>
        </div>
      </div>
    </div>
    <div class="hub-section" id="market-news"><p class="hub-label">FXマーケットニュース</p></div>
    <div class="panel full fx-news-panel" style="margin-bottom:20px;">
      <div class="panel-head"><h3>主要ヘッドライン <span class="fx-news-source-badge">InvestingLive</span><span class="fx-news-translate-badge">自動翻訳</span></h3><span id="fxNewsUpdated">2分ごとに自動更新</span></div>
      <ul class="fx-news-list" id="fxNewsLive"><li class="fx-news-empty">ニュースを読み込み中...</li></ul>
      <button type="button" class="fx-news-more" id="fxNewsMore">もっと見る →</button>
    </div>
    <div class="hub-section" id="rates"><p class="hub-label">📊 データコーナー</p></div>
    <div class="content-grid" style="margin-bottom:20px;">
      <div class="panel full">
        <div class="panel-head"><h3>🏦 主要中銀 政策金利</h3><span>{TODAY} 現在</span></div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>金利</th><th>スタンス</th></tr></thead>
          <tbody>
            <tr><td>FRB</td><td>🇺🇸 USD</td><td><strong>{FRB_RATE}</strong></td><td style="color:{FRB_COLOR};font-size:12px;">{FRB_STANCE}</td></tr>
            <tr><td>BOE</td><td>🇬🇧 GBP</td><td><strong>{BOE_RATE}</strong></td><td style="color:{BOE_COLOR};font-size:12px;">{BOE_STANCE}</td></tr>
            <tr><td>日銀</td><td>🇯🇵 JPY</td><td><strong>{BOJ_RATE}</strong></td><td style="color:{BOJ_COLOR};font-size:12px;">{BOJ_STANCE}</td></tr>
            <tr><td>ECB</td><td>🇪🇺 EUR</td><td><strong>{ECB_RATE}</strong></td><td style="color:{ECB_COLOR};font-size:12px;">{ECB_STANCE}</td></tr>
            <tr><td>RBA</td><td>🇦🇺 AUD</td><td><strong>{RBA_RATE}</strong></td><td style="color:{RBA_COLOR};font-size:12px;">{RBA_STANCE}</td></tr>
            <tr><td>RBNZ</td><td>🇳🇿 NZD</td><td><strong>{RBNZ_RATE}</strong></td><td style="color:{RBNZ_COLOR};font-size:12px;">{RBNZ_STANCE}</td></tr>
            <tr><td>BOC</td><td>🇨🇦 CAD</td><td><strong>{BOC_RATE}</strong></td><td style="color:{BOC_COLOR};font-size:12px;">{BOC_STANCE}</td></tr>
            <tr><td>SNB</td><td>🇨🇭 CHF</td><td><strong>{SNB_RATE}</strong></td><td style="color:{SNB_COLOR};font-size:12px;">{SNB_STANCE}</td></tr>
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。各中銀の公式発表と複数ソースで確認済み。</p>
      </div>
    </div>
    <div class="panel full daytrade-panel" id="strength" style="margin-bottom:20px;">
      <div class="panel-head"><h3>📈 4H デイトレ適性ランキング</h3><span>{DAYTRADE_UPDATED} JST 更新</span></div>
      <p class="daytrade-lead">直近5日の日中値幅を5年平均と比較し、4時間足ATR・ADX・EMAトレンド・概算コストを総合採点。直近ADR 30pips未満は対象外。</p>
      <div class="daytrade-table-wrap"><table class="fx-table daytrade-table">
        <thead><tr><th>順位</th><th>通貨ペア</th><th>5日ADR</th><th>5年比</th><th>4H ATR</th><th>ADX</th><th>方向</th><th>判定/点</th></tr></thead>
        <tbody>{DAYTRADE_ROWS_HTML}</tbody>
      </table></div>
      <p class="daytrade-note">価格データ: Yahoo Finance。スプレッドは概算でリアルタイム値ではありません。ランキングは売買推奨ではなく、相場環境を比較する参考情報です。</p>
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
  <a href="archive.html">アーカイブ</a>
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
<script>
(function(){{
  const GAS_URL = "https://script.google.com/macros/s/AKfycbyt2OkhAzglhoQOHZDHx_8fpY11lQsKXFQHIzMt-VkZO9Ki6Y02IVpkhgBY8KMVeWgR/exec";
  const list = document.getElementById("fxNewsLive");
  const updated = document.getElementById("fxNewsUpdated");
  const moreButton = document.getElementById("fxNewsMore");
  let latestItems = [];
  let expanded = false;
  if (!list) return;
  function formatTime(value) {{
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "";
    return date.toLocaleString("ja-JP", {{ month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" }});
  }}
  function renderNews(items) {{
    list.innerHTML = "";
    const visibleItems = items.slice(0, expanded ? 20 : 5);
    visibleItems.forEach((item) => {{
      const li = document.createElement("li");
      li.className = "fx-news-item";
      const a = document.createElement("a");
      a.href = item.link || "https://www.investing.com/news/forex-news";
      a.target = "_blank";
      a.rel = "noopener";
      const meta = document.createElement("span");
      meta.className = "fx-news-meta";
      meta.textContent = formatTime(item.pubDate);
      const title = document.createElement("strong");
      title.textContent = item.titleJa || item.title || "Market headline";
      a.append(meta, title);
      li.appendChild(a);
      list.appendChild(li);
    }});
    if (updated) updated.textContent = "最終更新: " + new Date().toLocaleTimeString("ja-JP", {{ hour: "2-digit", minute: "2-digit" }});
    if (moreButton) {{
      moreButton.hidden = items.length <= 5;
      moreButton.textContent = expanded ? "5件に戻す ↑" : "もっと見る →";
    }}
  }}
  async function loadNews() {{
    try {{
      const response = await fetch(GAS_URL, {{ cache: "no-store" }});
      const data = await response.json();
      if (data.status !== "ok" || !Array.isArray(data.items)) throw new Error("news unavailable");
      latestItems = data.items;
      renderNews(latestItems);
    }} catch (error) {{
      if (!list.children.length || list.querySelector(".fx-news-empty")) {{
        list.innerHTML = '<li class="fx-news-empty">ニュースを取得できませんでした。時間をおいて再読み込みしてください。</li>';
      }}
      if (updated) updated.textContent = "自動更新待機中";
    }}
  }}
  if (moreButton) {{
    moreButton.addEventListener("click", () => {{
      expanded = !expanded;
      renderNews(latestItems);
    }});
  }}
  loadNews();
  setInterval(loadNews, 120000);
}})();
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('✅ index.html 再生成完了')

# ── archive.html 生成 ────────────────────────────────────
import datetime as _dt

def _risk_color(r):
    return {'HIGH':'var(--yellow)','MEDIUM':'var(--orange)','LOW':'var(--green)'}.get(r,'var(--muted)')

def _extract_info(path):
    try:
        with open(path, encoding='utf-8') as f:
            t = f.read()
    except OSError:
        return '', '', ''
    title_m = re.search(r'<p class="sub">(.*?)</p>', t, re.S)
    summ_m  = re.search(r'<p class="label">一言まとめ</p>\s*<h3>(.*?)</h3>', t, re.S)
    risk_m  = re.search(r'<p class="label">Market Risk</p>\s*<h3[^>]*>(.*?)</h3>', t, re.S)
    def _c(m): return unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''
    title = _c(title_m)
    title_short = (title[:55] + '…') if len(title) > 55 else title
    return title_short, _c(summ_m), _c(risk_m)

archive_cards_html = ''
for f in report_files:
    href = f.replace(os.sep, '/')
    name = os.path.basename(f).replace('.html','')
    try:
        d  = _dt.date.fromisoformat(name)
        wd = DAYS[d.strftime('%A')]
        label = f'{name}（{wd}）'
    except Exception:
        label = name
    title, summary, risk = _extract_info(f)
    rc = _risk_color(risk)
    risk_span = f' <span style="color:{rc};font-weight:700;">{risk}</span>' if risk else ''
    search_data = f'{name} {label} {title} {summary}'.replace('"','')
    archive_cards_html += f'''    <a href="{href}" class="archive-card" data-search="{search_data}">
      <span class="archive-card-date">{label}</span>
      <p class="archive-card-title">{title}</p>
      <p class="archive-card-sub">{summary}{risk_span}</p>
    </a>\n'''

ATOTAL = len(report_files)

archive_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>日報アーカイブ | AUXEN FX Portal</title>
<link rel="stylesheet" href="style.css">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/logo.svg">
<script data-goatcounter="https://auxen.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="https://cdn.jsdelivr.net/npm/twemoji@14.0.2/dist/twemoji.min.js" crossorigin="anonymous"></script>
<script>document.addEventListener('DOMContentLoaded',function(){{twemoji.parse(document.body,{{folder:'svg',ext:'.svg',base:'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/'}});}});</script>
</head>
<body class="home-page">
<header class="mobile-header">
  <a href="index.html" class="mobile-brand">
    <img src="assets/logo.svg" alt="AUXEN">
    <span><strong>AUXEN</strong><em>FX Research Lab</em></span>
  </a>
</header>
<section class="mobile-hero">
  <p class="eyebrow">AUXEN FX PORTAL</p>
  <h1>日報アーカイブ</h1>
  <p>全{ATOTAL}件 — 日付・キーワードで絞り込み</p>
</section>
<div class="app">
  <aside class="sidebar">
    <div class="brand">
      <div class="logo"><img src="assets/logo.svg" alt="AUXEN"></div>
      <div><h1>AUXEN</h1><p>FX Research Lab</p></div>
    </div>
    <nav class="side-nav">
      <span class="nav-section">メイン</span>
      <a href="index.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/></svg>ダッシュボード</a>
      <a href="archive.html" class="active"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="12" y2="17"/></svg>日報アーカイブ</a>
      <span class="nav-section">サイト情報</span>
      <a href="about.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>About</a>
      <a href="disclaimer.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>免責事項</a>
      <a href="contact.html"><svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>お問い合わせ</a>
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
        <p class="eyebrow">AUXEN FX PORTAL — Archive</p>
        <h2>日報アーカイブ</h2>
        <p class="sub">過去の全FX日報。日付やキーワードで絞り込み検索できます。</p>
      </div>
      <div class="date-card">
        <span>Total</span>
        <strong>{ATOTAL}件</strong>
        <em>全レポート</em>
      </div>
    </header>
    <div class="hub-section"><p class="hub-label">🔍 絞り込み検索</p></div>
    <div class="archive-search-wrap">
      <input type="search" id="archiveSearch" class="archive-search-input"
             placeholder="日付（例: 2026-06）やキーワード（例: FOMC、USD/JPY）で絞り込み">
      <span class="archive-count" id="archiveCount">{ATOTAL}件</span>
    </div>
    <div class="hub-section"><p class="hub-label">📂 全レポート</p></div>
    <div class="archive-grid" id="archiveGrid">
{archive_cards_html}    </div>
  </main>
</div>
<nav class="mobile-bottom-nav" aria-label="スマホ下部ナビ">
  <a href="index.html">Home</a>
  <a href="archive.html" class="active">アーカイブ</a>
  <a href="index.html#rates">金利</a>
  <a href="contact.html">連絡</a>
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
<script>
(function(){{
  const input = document.getElementById('archiveSearch');
  const cards = document.querySelectorAll('#archiveGrid .archive-card');
  const count = document.getElementById('archiveCount');
  input.addEventListener('input', function() {{
    const q = this.value.toLowerCase().trim();
    let n = 0;
    cards.forEach(function(c) {{
      const match = !q || c.dataset.search.toLowerCase().includes(q);
      c.hidden = !match;
      if (match) n++;
    }});
    count.textContent = n + '件';
  }});
}})();
</script>
</body>
</html>"""

with open('archive.html', 'w', encoding='utf-8') as f:
    f.write(archive_html)
print('✅ archive.html 再生成完了')
