import glob, os

TODAY = '2026-08-27'
WEEKDAY = '木'

HERO_SUB = ('前日はNVIDIA決算が市場予想を上回る増収でも時間外で株価が下落し、ドル円は原油急落と中東（イラン）情勢改善観測を受けた米長期金利低下で159円台前半を上下した。'
            '本日は氷見野日銀副総裁の講演が9月利上げ観測を左右する最大の注目材料となるほか、ECB理事会議事要旨や米新規失業保険申請件数が予定され、'
            '28日のジャクソンホール会合でのウォーシュFRB議長講演を控えたポジション調整含みの展開が続く。')

SUMMARY_TITLE = '氷見野日銀副総裁の講演が9月利上げ観測を左右、ジャクソンホール会合控え調整継続'
SUMMARY_BODY = (
    '前日8/26（水）は、米商務省が発表した第2四半期GDP改定値が前期比年率+1.5%と予想通り・速報値から変わらずだった一方、'
    '個人消費は+3.4%（予想+3.2%）、GDPデフレーターは+6.4%（予想+6.2%）、コアPCE価格指数は+3.6%（予想+3.4%）と内訳のインフレ関連項目が総じて予想を上回った。'
    '単独指標として発表された7月PCEデフレーターも前年比+3.7%と予想+3.6%をわずかに上回ったが、コア指数は前月比+0.2%・前年比+3.3%とそれぞれ予想通りで、市場の反応は限定的だった。'
    'NVIDIAは5〜7月期決算で売上高が前年同期比2倍の962億ドルとなり、QUICK・ファクトセット集計の市場予想922億ドルを上回ったが、引け後の時間外取引で株価は約2%下落した（要確認）。'
    'ドル円はアジア時間に159円49銭近辺まで上値を伸ばした後、欧州時間の原油先物急落でドル売りが優勢になり上げ幅を縮小、NY市場では中東情勢の改善観測とインフレ関連指標の反応限定を受けた米長期金利低下から一時159円08銭まで下落し、最終的に159円19銭で引けた。'
    '日銀の9月利上げ観測は市場で約8割織り込まれており、本日8/27に予定される氷見野副総裁の講演内容が確度を左右するとして関心が集まっている（要確認）。'
    '本日は10:30の氷見野副総裁講演を筆頭に、20:30の欧州ECB理事会議事要旨、21:30の米新規失業保険申請件数・卸売在庫速報値が予定され、'
    '28日のジャクソンホール会合ウォーシュ議長講演を控えたポジション調整含みの一日となる。'
)

TOP_PAIR = 'EUR/USD'
TOP_PAIR_FLAGS = '🇪🇺🇺🇸'
TOP_PAIR_NOTE = ('4Hデイトレ適性ランキング1位（スコア61・候補、ADX40.6で上昇トレンド継続、ランキングデータは2026-08-26 04:54 JST時点で未更新）。'
                  '20:30の欧州ECB理事会議事要旨、21:30の米新規失業保険申請件数・卸売在庫速報値とユーロ・ドル双方に材料が予定され、方向性が出やすい組み合わせ')

RISK_LEVEL = 'MEDIUM'
RISK_NOTE = ('氷見野日銀副総裁の講演が9月利上げ観測の確度を左右する最大の注目材料となるほか、ECB議事要旨や米新規失業保険申請件数など中重要度の指標が並ぶ。'
             '前日のNVIDIA決算後の株価反応と28日のジャクソンホール会合ウォーシュ議長講演を控え、リスクセンチメントに神経質な展開が想定される一日')

KEY_COUNT = '20件'
KEY_COUNT_NOTE = '氷見野副総裁講演 / ECB議事要旨 / 米新規失業保険申請件数・卸売在庫 等（本日の市場休場はなし）'

MARKET_HOLIDAY = '本日、主要国の市場休場はなし'

KEY_EVENTS = [
    '10:30 🇯🇵 氷見野日銀副総裁 講演（9月利上げ観測に関心）',
    '20:30 🇪🇺 ECB理事会議事要旨（7/22-23開催分）',
    '21:30 🇺🇸 新規失業保険申請件数',
    '21:30 🇺🇸 卸売在庫【速報値】',
    '26:00（翌02:00）🇺🇸 米7年債入札',
]

OTHER_POINTS = [
    ('NVIDIA決算は増収でも株価は時間外で軟化', '5〜7月期売上高は前年同期比2倍の962億ドルと市場予想922億ドルを上回ったが、引け後の時間外取引で株価は約2%下落した（要確認）。'),
    ('ドル円は原油急落と米金利低下で方向感が交錯', 'アジア時間159円49銭近辺まで上昇後、欧州時間の原油先物急落と中東情勢改善観測による米長期金利低下でドル売りが優勢となり、NY市場は159円19銭で引けた。'),
    ('氷見野日銀副総裁の講演が9月利上げ観測を左右', '市場は9月利上げを約8割織り込んでおり、本日10:30の講演内容が確度を左右する最大の注目材料（要確認）。'),
    ('27〜29日のジャクソンホール会合が進行中', '28日にウォーシュFRB議長の講演が予定されており、市場の関心はそちらに集まりやすい。'),
    ('来週月曜31日が8月最後の営業日', '月末フローによるポジション調整が意識されやすい時期に入る。'),
]

REVIEW_TOPICS = [
    ('米GDP改定値・PCE関連指標は総じて予想を上回るも金利反応は限定的',
     '米商務省が発表した第2四半期GDP改定値は前期比年率+1.5%（予想通り・速報値から変わらず）。個人消費は+3.4%（予想+3.2%）、GDPデフレーターは+6.4%（予想+6.2%）、コアPCE価格指数は+3.6%（予想+3.4%）と内訳のインフレ関連項目が予想を上回った。単独指標の7月PCEデフレーターも前年比+3.7%と予想+3.6%をわずかに上回ったが、コア指数は前月比+0.2%・前年比+3.3%と予想通りで、市場の反応は限定的だった。'),
    ('NVIDIA決算は増収でも株価は時間外で下落',
     '5〜7月期決算で売上高は前年同期比2倍の962億ドルとなり、QUICK・ファクトセット集計の市場予想922億ドルを上回った。しかし引け後の時間外取引で株価は約2%下落し、好決算にもかかわらず失望売りとなった（要確認）。'),
    ('ドル円は原油急落と米金利低下で方向感が交錯',
     'アジア時間には159円49銭近辺まで上値を伸ばしたが、欧州時間に原油先物が急落するとドル売りが優勢となり上げ幅を縮小。NY市場では中東（イラン）情勢の改善観測とインフレ関連指標の反応限定を受けた米長期金利低下がドル売りを促し、一時159円08銭まで下落する場面もあった。最終的にNY市場は159円19銭で引けた。'),
    ('氷見野日銀副総裁の講演を控え9月利上げ観測が拡大',
     '日銀の9月利上げ観測が強まっており、市場は約8割の確率を織り込んでいる。氷見野副総裁は本日8/27に講演を予定しており、その発言内容が9月会合での利上げ確度を左右するとして関心が集まっている（要確認）。'),
]

HANDOVER = ('本日（8/27木）への引継ぎ：前日はNVIDIA決算の増収を受けても株価が軟化し、ドル円は原油急落と中東情勢改善観測を受けた米金利低下で159円台前半を上下する展開となった。'
            '本日は10:30の氷見野副総裁講演が9月利上げ観測を左右する最大の注目材料となるほか、20:30のECB理事会議事要旨、21:30の米新規失業保険申請件数・卸売在庫速報値が予定される。'
            '28日のジャクソンホール会合ウォーシュ議長講演を控え、ポジション調整含みの値動きが想定される。')

RANKING_LEAD = (
    '8/26（水）はNVIDIA決算が増収でも株価が時間外で下落し、ドル円は原油急落と中東情勢改善観測を受けた米長期金利低下で159円08銭〜159円49銭のレンジで上下し、159円19銭で引けた。'
    '第2四半期GDP改定値や7月PCE関連指標は総じて予想を上回ったものの、28日のジャクソンホール会合ウォーシュ議長講演を控え反応は限定的だった。'
    '本日8/27（木）は10:30の氷見野日銀副総裁講演が9月利上げ観測の確度を左右する最大の注目材料となるほか、20:30のECB理事会議事要旨、21:30の米新規失業保険申請件数・卸売在庫速報値が予定される。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（据え置き継続、8/27-29ジャクソンホール会合のウォーシュ議長発言に関心集まる） / 日銀 1.00%（正常化継続、7/31会合8対1で据え置き、9月利上げ観測が約8割織り込み） / ECB 2.25%（預金ファシリティ金利、6/17付適用で据え置き継続）'
)

RANKING_ROWS = [
    ('A', 'EUR/USD', 'ランキング1位（スコア61・候補）。ADX40.6で上昇トレンド継続、20:30のECB議事要旨・21:30の米指標が方向性のきっかけになりやすい', 'up'),
    ('B', 'USD/CHF', 'ランキング2位（スコア58・候補）。ADX26.1でレンジ、直近5日ADRは5年平均の98.2%とほぼ平年並み', 'range'),
    ('B', 'GBP/USD', 'ランキング3位（スコア57・候補）。ADX42.9で強い上昇トレンド継続', 'up'),
    ('B', 'USD/CAD', 'ランキング4位（スコア57・候補）。ADX28.5でレンジ、原油関連指標がカナダドル側にも波及しやすい', 'range'),
    ('B', 'NZD/USD', 'ランキング5位（スコア56・候補）。ADX31.0で上昇トレンド継続、米ドル系指標との綱引きに注目', 'up'),
]
RANKING_NOTE = '※ 4Hデイトレ適性ランキングは2026-08-26 04:54 JST時点のデータ（本日未更新・RemoteTrigger環境の制約でYahoo Finance再取得不可のため前回値を継続使用）。数値は目安であり、実際のエントリーは各自のルールで判断してください。'

CALENDAR_ROWS = [
    ('10:30', '🇦🇺 豪', '第2四半期民間設備投資【前期比】（KissFX・ForexFactoryで一致）', False, '中', '+0.8%', '+6.5%'),
    ('10:30', '🇦🇺 豪', '家計支出【前月比】（ForexFactoryのみ・要確認）', False, '低', '+0.3%', '+0.8%'),
    ('10:30', '🇦🇺 豪', 'RBA月報（ForexFactoryのみ・要確認）', False, '低', '—', '—'),
    ('10:30', '🇯🇵 日', '氷見野日銀副総裁 講演（あいさつ）（KissFXのみ・要確認）', True, '要人発言', '—', '—'),
    ('未定', '🇯🇵 日', '氷見野日銀副総裁 記者会見（KissFXのみ・要確認）', False, '要人発言', '—', '—'),
    ('15:00', '🇩🇪 独', 'GfK消費者信頼感調査（KissFX・ForexFactoryで一致）', False, '低', '-29.5', '-29.6'),
    ('15:45', '🇫🇷 仏', '生産者物価指数【前月比/前年比】（KissFXのみ・要確認）', False, '低', '-0.6%/—', '-2.6%'),
    ('17:00', '🇪🇺 欧', 'マネーサプライM3【前年比】（ForexFactoryのみ・要確認）', False, '低', '+3.5%', '+3.3%'),
    ('17:00', '🇪🇺 欧', '民間融資【前年比】（ForexFactoryのみ・要確認）', False, '低', '+2.9%', '+3.0%'),
    ('20:30', '🇪🇺 欧', 'ECB理事会議事要旨【7/22-23開催分】（KissFX・ForexFactoryで一致）', False, '中', '—', '—'),
    ('21:30', '🇨🇦 加', '経常収支（KissFX予想+39.0億/前回-71.8億、ForexFactory予想3.5B/前回-7.2B・単位相違のため要確認）', False, '低', '+39.0億(KissFX)/3.5B(FF)', '-71.8億(KissFX)/-7.2B(FF)'),
    ('21:30', '🇺🇸 米国', '新規失業保険申請件数（KissFX・ForexFactoryで一致）', True, '高', '20.8万件', '20.6万件'),
    ('21:30', '🇺🇸 米国', '卸売在庫【速報値】（KissFX・ForexFactoryで一致）', False, '低', '+0.2%', '+0.2%'),
    ('21:30', '🇺🇸 米国', '貿易収支【速報値】（ForexFactoryのみ・要確認）', False, '低', '-1,008億ドル', '-1,015億ドル'),
    ('22:00', '🇨🇳 中国', 'コンファレンスボード景気先行指数【前月比】（ForexFactoryのみ・要確認）', False, '低', '—', '+0.1%'),
    ('23:30', '🇺🇸 米国', '週間天然ガス貯蔵量（KissFX・ForexFactoryで概ね一致）', False, '低', '+19億cf', '+16億cf'),
    ('24:00', '🇺🇸 米国', 'カンザスシティ連銀製造業活動指数（KissFXのみ・要確認）', False, '低', '+10', '+9'),
    ('26:00（翌02:00）', '🇺🇸 米国', '7年債入札（KissFXのみ・要確認）', False, '中', '440億ドル', '—'),
    ('00:45', '🇺🇸 米国', 'バーキン総裁発言（ForexFactoryのみ・要確認）', False, '要人発言', '—', '—'),
    ('01:15', '🇨🇭 スイス', 'マルタン理事発言（ForexFactoryのみ・要確認）', False, '要人発言', '—', '—'),
]

CALENDAR_NOTE = ('※ 時刻はJST。KissFX（主・ランク付き）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。'
                  '両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値がソース間で相違する指標には「（要確認）」を付しています。'
                  '24:00表記は日本時間当日24時（翌日00:00）、26:00表記は翌日02:00相当です。本日の主要市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。')

# ── ここから生成処理 ─────────────────────────────────
report_files = sorted(glob.glob('reports/*.html'), reverse=True)
SIDEBAR_ITEMS = []
DAYS = {'Monday':'月','Tuesday':'火','Wednesday':'水','Thursday':'木','Friday':'金','Saturday':'土','Sunday':'日'}
import datetime as _dt
for f in report_files[:10]:
    name = os.path.basename(f).replace('.html', '')
    href = os.path.basename(f)
    try:
        d = _dt.date.fromisoformat(name)
        wd = DAYS[d.strftime('%A')]
        label = f'{name}（{wd}）'
    except Exception:
        label = name
    SIDEBAR_ITEMS.append(f'<li><a href="{href}">{label}</a></li>')
SIDEBAR_HTML = '\n'.join(SIDEBAR_ITEMS)

KEY_EVENTS_HTML = '\n'.join(f'              <li>{item}</li>' for item in KEY_EVENTS)

OTHER_POINTS_HTML = '\n'.join(
    f'              <li><strong>{title}</strong>：{body}</li>' for title, body in OTHER_POINTS
)

REVIEW_TOPICS_HTML = '\n'.join(
    f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(REVIEW_TOPICS)
)

RANK_CLASS = {'A': 'rank-a', 'B': 'rank-b'}
TREND_CLASS = {'up': 'trend-up', 'range': 'trend-range', 'down': 'trend-down'}
TREND_ARROW = {'up': '↑', 'range': '→', 'down': '↓'}

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {RANK_CLASS[rank]}">{rank}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{note}</span></td>
              <td><span class="{TREND_CLASS[trend]}">{TREND_ARROW[trend]}</span></td>
            </tr>''' for rank, pair, note, trend in RANKING_ROWS)

CALENDAR_ROWS_HTML_LINES = []
CALENDAR_ROWS_HTML_LINES.append('            <tr><td>終日</td><td>🌍 主要国</td><td>' + MARKET_HOLIDAY + '</td><td>—</td><td>—</td><td>—</td></tr>')
for time_jst, country, name, important, importance, forecast, previous in CALENDAR_ROWS:
    badge = ' <span class="badge-important">★重要</span>' if important else ''
    if important:
        CALENDAR_ROWS_HTML_LINES.append(
            f'            <tr><td><strong>{time_jst}</strong></td><td>{country}</td><td><strong>{name}</strong>{badge}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
        )
    else:
        CALENDAR_ROWS_HTML_LINES.append(
            f'            <tr><td>{time_jst}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
        )
CALENDAR_ROWS_HTML = '\n'.join(CALENDAR_ROWS_HTML_LINES)

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
{SIDEBAR_HTML}
      </ul>
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
        <em>{WEEKDAY}曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{SUMMARY_TITLE}</h3>
        <p>{SUMMARY_BODY}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>{TOP_PAIR} {TOP_PAIR_FLAGS}</h3>
        <p>{TOP_PAIR_NOTE}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--gold,#c79a3b)">{RISK_LEVEL}</h3>
        <p>{RISK_NOTE}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_COUNT}</h3>
        <p>{KEY_COUNT_NOTE}</p>
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
              <li>{MARKET_HOLIDAY}</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">📌 必見経済指標（時刻順）</div>
            <ul class="points-list">
{KEY_EVENTS_HTML}
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
          {RANKING_LEAD}
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
          <h3>📰 前日の相場振り返り（2026-08-26）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{REVIEW_TOPICS_HTML}
          <div class="handover">
            <strong>{HANDOVER}</strong>
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
{CALENDAR_ROWS_HTML}
          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">{CALENDAR_NOTE}</p>
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
