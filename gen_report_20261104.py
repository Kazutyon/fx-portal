# -*- coding: utf-8 -*-
"""FX日報 2026-11-04（水）生成スクリプト"""
import glob, os
TODAY = '2026-11-04'
WEEKDAY = '水'
HERO_TITLE_SUB = ('前日11/3（火）のドル円は米JOLT求人件数の上振れで158.77円まで上昇して引けた。本日11/4（水）は米中間選挙の結果判明（日本時間4日以降）、ユーロ圏CPI速報（19:00）、米ADP（22:15）・ISM非製造業（24:00）が材料。')
SUMMARY_HEADLINE = ('ドル円は米求人の上振れで158円台後半、本日は米中間選挙の結果と米ADP・ISM非製造業でドルの方向が決まる')
SUMMARY_BODY = ('11/3のNY市場でドル円は157.98円から158.77円まで上昇した。米9月JOLT求人件数が予想（7.15M）を上回り4カ月ぶりの高水準となり、労働市場の底堅さから米長期金利が上昇したため（ザイFX・みんかぶ）。'
 'ユーロはナーゲル独連銀総裁が「インフレは9月以降悪化した」と述べ、12月のECB利上げ観測が強まって買われた（ザイFX）。本日19:00のユーロ圏CPI速報（予想+4.0%、前回+3.8%）がこの見方の検証になる。'
 'ドル円の目先の上値は9/24高値159.04円（ザイFX）。')
TOP_PAIR_BODY = ('ドル円は11/3に157.98〜158.77円で推移し、158円台で引けた（ザイFX）。米長期金利の上昇がドル買いを支え、159.04円の高値と200日線が上値の節目。為替介入への思惑が159円台で上値を抑える。'
 '22:15の米ADP（予想6.7万人、前回9.0万人）と24:00のISM非製造業（予想54.8、前回54.9）が弱ければ158円割れ、強ければ159円を試す。'
 '4時間足ランキング（11/3 10:42 JST生成・本日分は未更新）ではUSD/JPYは上位6位圏外。')
RISK_LEVEL = 'HIGH'
RISK_BODY = ('米中間選挙の結果が日本時間11/4以降に判明し、政権運営とイラン情勢（選挙後に攻撃再開の思惑・KissFX）が同時に動く。イラン外務次官が米国との衝突に言及する一方、和平交渉の報道も交錯し原油が乱高下している（みんかぶ・ザイFX）。11/5にBOE、11/6に米雇用統計と植田日銀総裁の発言が続く。')
KEY_EVENTS_COUNT = '5件'
KEY_EVENTS_SUMMARY = ('06:45 NZ 第3四半期雇用統計、19:00 ユーロ圏CPI速報、22:15 米ADP、24:00 米ISM非製造業景況指数、24:30 米原油在庫。米中間選挙の結果判明。')
MARKET_OVERVIEW = ('<strong>VIX・米10年債/2年債利回り・DXY・WTI</strong>：月曜のみの取得項目のため本日は未取得。ザイFXは11/3に米長期金利が上昇したと伝えている。'
 '<strong>原油</strong>：イランとの和平工作の報道で反落した後に反発する乱高下（みんかぶ・ザイFX）。'
 '<strong>株</strong>：欧州株はAI懸念で反落、ASMLは最大3.5%下落（ザイFX）。米ダウは午後2時台時点で107ドル安（ザイFX）。ユーロ円は177.60円（ザイFX・4時時点）。'
 '<br><br><strong>ユーロドル：</strong>1.1180〜1.1195付近のもみ合い（みんかぶ）。IMMユーロ売り越しは37万枚で、巻き戻しが起きやすい水準（ザイFX掲載のZEROコラム）。'
 '<br><br><strong>今週の焦点：</strong> 11/4 NZ雇用・ユーロ圏CPI・米ADP・ISM非製造業、11/5 BOE（四半期報告・総裁会見）・米新規失業保険申請件数、11/6 米雇用統計・加雇用統計・植田日銀総裁の発言（KissFX）。')
RANKING_ROWS = [
 (1,'USD/JPY','rank-c','C','158円台後半。米JOLT上振れで長期金利が上昇、159.04円（9/24高値）が上値の節目。22:15ADPと24:00ISMで方向が決まる。','trend-up','↑'),
 (2,'EUR/USD','rank-c','C','1.118〜1.1195のレンジ。19:00のユーロ圏CPI速報（予想+4.0%）が12月ECB利上げ観測を左右する。ADXは18.8でレンジ判定（11/3生成分）。','trend-range','→'),
 (3,'EUR/JPY','rank-c','C','177円台。ユーロ買いと円売りが重なる。4時間足ランキング3位（スコア51・候補、ADX23.0、レンジ。11/3 10:42生成）。','trend-range','→'),
 (4,'NZD/USD','rank-c','C','06:45の第3四半期雇用統計（失業率予想5.5%、就業者数予想+0.4%）でNZドルが動く。ランキング5位（見送り45、ADX19.8、下降）。','trend-down','↓'),
 (5,'GBP/USD','rank-c','C','200日線付近。11/5のBOEを前に、BOEが利上げ期待をけん制するとの見方が出ている（みんかぶ）。ランキング4位（見送り45、ADX24.8、上昇）。','trend-up','↑'),
]
RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {b}">{l}</span></td>
              <td><strong>{p}</strong><br><span style="color:var(--muted);font-size:12px;">{d}</span></td>
              <td><span class="{tc}">{ar}</span></td>
            </tr>''' for r,p,b,l,d,tc,ar in RANKING_ROWS)
RANKING_NOTE = ('※ 4時間足ランキングは2026/11/03 10:42 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、11/3時点の数値。1位はEUR/AUD（スコア61・候補）、2位USD/CHF（52・候補）。スコア・ADX・ADR比は補助指標であり、売買推奨ではない。')
TOPICS = [
 ('米JOLT求人件数が4カ月ぶりの高水準、ドル円は158.77円へ上昇','NY市場でドル円は157.98円から158.77円まで上昇した。米9月JOLT求人件数が予想を上回り、労働市場の底堅さから年内の利上げ観測が強まって米長期金利が上昇した（ザイFX）。ロンドン時間は157円台後半で底堅く、NY序盤に158円台へ乗せた後は上値が重かった（みんかぶ）。'),
 ('独連銀ナーゲル総裁の発言で12月ECB利上げ観測が強まりユーロ買い','ナーゲル総裁は「インフレは9月以降悪化した」と指摘し、燃料コスト上昇の第2次的影響への警戒を示した（ザイFX）。みんかぶは同総裁が来月の利上げを見込んでいるとの見方を伝えている。ユーロドルは1.1180〜1.1195付近でもみ合った。'),
 ('米中間選挙待ちで方向感が出ず、原油は和平工作報道で乱高下','ロンドン為替でドル指数は選挙待ちで方向感が定まらなかった（みんかぶ）。イランとの和平工作の動きが伝わり原油は急落してドル安が進んだが、その後反発した。イラン外務次官はゲシュム島での米国との衝突に言及し、カタール報道は双方に交渉の意思があるとしており、材料が交錯している。'),
 ('日本は文化の日で休場、AI懸念で欧州株は反落','東京市場は休場でレンジ相場となり、短中期のオプション売りが強まった（ザイFX）。欧州株はAI懸念で反落し、ASMLは最大3.5%下落した。RBA政策金利（11/3 12:30、予想4.85%）の結果は取得したソースに記載がなく確認できない（要確認）。'),
]
TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{t}</div>
            {b}
          </div>''' for i,(t,b) in enumerate(TOPICS))
HANDOVER = ('本日（11/4水）への引継ぎ：ドル円は158.77円まで上昇して引け、上値の節目は159.04円（9/24高値）。米中間選挙の結果が日本時間4日以降に判明するため、結果を受けた米金利とイラン情勢の動きがドル円・原油を同時に動かす。ユーロ円は177円台、ユーロは12月ECB利上げ観測で堅い。RBAの結果は要確認。')
POINTS_EVENTS = [
 '06:45 🇳🇿 NZ 第3四半期雇用統計：失業率（予想5.5%、前回5.6%）、就業者数 前期比（予想+0.4%、前回+0.5%）（Kiss/FF一致）',
 '08:50 🇯🇵 日 マネタリーベース 前年比（予想-14.0%、前回-15.2%）（FFのみ・要確認、ザイFXは8:50発表と記載）',
 '10:45 🇨🇳 中 RatingDog（旧財新）非製造業PMI（予想51.7、前回51.6）',
 '17:50〜18:30 🇫🇷🇩🇪🇪🇺🇬🇧 欧英 非製造業PMI【改定値】（ユーロ圏予想51.7、英予想53.1）',
 '19:00 🇪🇺 ユーロ圏 消費者物価指数【速報値】（予想+4.0%、前回+3.8%）／コア（予想+2.5%、前回+2.5%）',
 '22:15 🇺🇸 米 ADP雇用統計（予想6.6万人 ※FFは6.7万人、前回9.0万人）',
 '24:00（翌00:00）🇺🇸 米 ISM非製造業景況指数（予想54.8、前回54.9）／24:30 米 週間原油在庫（FF予想-10万バレル、前回-189.2万）',
 '米株引け後 アーム、クアルコムなど米主要企業の決算（KissFX）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)
OTHER_POINTS = [
 ('ドル円：158円台後半、159.04円が上値の節目','米JOLT上振れによる米長期金利の上昇が支え。22:15のADPと24:00のISM非製造業が強ければ159円を試し、弱ければ158円を割る。介入警戒が159円台で上値を抑える。'),
 ('ユーロ：19:00のCPI速報が12月利上げ観測の検証','予想+4.0%（前回+3.8%）を上回ればユーロ買い、下回れば12月利上げ観測が後退する。IMMユーロ売り越し37万枚は巻き戻し余地を示す（ザイFX掲載コラム）。'),
 ('米中間選挙：結果判明は日本時間4日以降','結果を受けたトランプ米大統領の発言と、イラン情勢（選挙後に攻撃再開の思惑・KissFX）が原油・米金利・ドルに波及する。結果が出るまで大きな持ち越しは避ける局面。'),
 ('NZドル：06:45の雇用統計で動意','失業率予想5.5%（前回5.6%）。KissFXは「NZドルへの影響は非常に大きくなりやすい」と評価している。'),
 ('今週後半：11/5 BOE、11/6 米雇用統計','BOEは11/5に四半期報告・総裁会見つきで発表、11/6は米・加雇用統計と植田日銀総裁の発言（KissFX）。'),
]
OTHER_POINTS_HTML = '\n'.join(f'              <li><strong>{t}</strong>：{b}</li>' for t,b in OTHER_POINTS)
CAL_ROWS = [
 ('06:45','🇳🇿 NZ','第3四半期 失業率（Kiss/FF一致）','高','5.5%','5.6%'),
 ('06:45','🇳🇿 NZ','第3四半期 就業者数 前期比（Kiss/FF一致）','高','+0.4%','+0.5%'),
 ('06:45','🇳🇿 NZ','労働コスト指数 前期比（FFのみ・要確認）','低','0.5%','0.7%'),
 ('08:50','🇯🇵 日','マネタリーベース 前年比（FFのみ・要確認）','低','-14.0%','-15.2%'),
 ('09:00','🇳🇿 NZ','ANZ商品価格 前月比（FFのみ・要確認）','低','—','0.6%'),
 ('09:30','🇦🇺 豪','家計支出 前月比（FFのみ・要確認）','低','0.2%','0.0%'),
 ('10:45','🇨🇳 中','RatingDog（旧財新）非製造業PMI（Kiss/FF一致）','低','51.7','51.6'),
 ('17:00','🇪🇺 西','失業者数変化（FFのみ・要確認）','低','18.7K','23.6K'),
 ('17:15','🇪🇺 西','非製造業PMI（FFのみ・要確認）','低','57.6','58.3'),
 ('17:45','🇪🇺 伊','非製造業PMI（FFのみ・要確認）','低','51.4','51.7'),
 ('17:50','🇫🇷 仏','非製造業PMI【改定値】（Kiss/FF一致）','低','48.4','48.4'),
 ('17:55','🇩🇪 独','非製造業PMI【改定値】（Kiss/FF一致）','低','51.7','51.7'),
 ('18:00','🇪🇺 ユーロ圏','非製造業PMI【改定値】（Kiss/FF一致）','低','51.7','51.7'),
 ('18:30','🇬🇧 英','非製造業PMI【改定値】（Kiss/FF一致）','低','53.1','53.1'),
 ('19:00','🇪🇺 ユーロ圏','消費者物価指数【速報値】前年比（Kiss/FF一致）','中','+4.0%','+3.8%'),
 ('19:00','🇪🇺 ユーロ圏','コア消費者物価指数【速報値】前年比（Kiss/FF一致）','中','+2.5%','+2.5%'),
 ('21:00','🇺🇸 米','MBA住宅ローン申請指数（KissFXのみ・要確認）','低','—','+3.4%'),
 ('22:15','🇺🇸 米','ADP雇用統計（Kiss/FF一致）','低','+6.6万人（FF 6.7万人）','+9.0万人'),
 ('22:30','🇨🇦 加','貿易収支（Kiss/FF一致）','低','+50.0億','+42.0億'),
 ('22:30','🇺🇸 米','貿易収支（Kiss/FF一致）','低','-1079億','-1056億'),
 ('23:45','🇺🇸 米','非製造業PMI【改定値】（Kiss/FF一致）','低','57.9','57.9'),
 ('24:00','🇺🇸 米','ISM非製造業景況指数（Kiss/FF一致）','中','54.8','54.9'),
 ('24:30','🇺🇸 米','週間原油在庫（Kiss/FF一致）','低','-10万バレル（FF）','-189.2万'),
 ('米株引け後','🇺🇸 米','アーム、クアルコムなど主要企業の決算（KissFX）','—','—','—'),
]
def _key(r):
    t=r[0]
    if t.startswith('米株'): return (99,0)
    return (int(t[:2]),int(t[3:5]))
CAL_ROWS.sort(key=_key)
CAL_ROWS_HTML = '\n'.join(f'            <tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td></tr>' for a,b,c,d,e,f in CAL_ROWS)

_files = sorted(glob.glob('reports/*.html'), reverse=True)
_wd = {0:'月',1:'火',2:'水',3:'木',4:'金',5:'土',6:'日'}
import datetime as _dt
archive_entries = []
for _f in _files:
    _n = os.path.basename(_f)[:-5]
    if _n == TODAY:
        continue
    _d = _dt.date.fromisoformat(_n)
    archive_entries.append((f'{_n}.html', f'{_n}（{_wd[_d.weekday()]}）'))
archive_entries = archive_entries[:10]
SIDEBAR_ARCHIVE_HTML = '\n'.join(f'<li><a href="{href}">{label}</a></li>' for href, label in archive_entries)

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
  <p>{HERO_TITLE_SUB}</p>
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
{SIDEBAR_ARCHIVE_HTML}
      </ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 {TODAY}（{WEEKDAY}）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_TITLE_SUB}</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>{TODAY}</strong>
        <em>水</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{SUMMARY_HEADLINE}</h3>
        <p>{SUMMARY_BODY}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>USD/JPY 🇺🇸🇯🇵</h3>
        <p>{TOP_PAIR_BODY}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red,#c0392b)">{RISK_LEVEL}</h3>
        <p>{RISK_BODY}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_EVENTS_COUNT}</h3>
        <p>{KEY_EVENTS_SUMMARY}</p>
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
              <li>なし（KissFX・休場日一覧で本日の主要市場休場は確認されない。日本は昨日の休場明け）</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
{POINTS_EVENTS_HTML}
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">👁 その他注目点</div>
            <ul class="points-list">
{OTHER_POINTS_HTML}
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
          {MARKET_OVERVIEW}
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
{RANKING_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">{RANKING_NOTE}</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-11-03 火）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{TOPICS_HTML}
          <div class="handover">
            <strong>{HANDOVER}</strong>
          </div>
        </div>
      </div>

      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>📅 本日の経済指標カレンダー（全件）</h3>
          <span>本日の主要予定</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead>
            <tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr>
          </thead>
          <tbody>
{CAL_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はForexFactory区分。</p>
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
</html>
"""

with open(f'reports/{TODAY}.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'reports/{TODAY}.html generated')
