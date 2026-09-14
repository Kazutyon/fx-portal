#!/usr/bin/env python3
# -*- coding: utf-8 -*-

TODAY = '2026-09-15'
WEEKDAY = '火'

HERO_SUMMARY = '9/14（月）はサウジアラビアが東西原油パイプラインの操業停止を発表したことで原油高が進み、FOMC（結果判明は日本時間9/17未明3:00）の利上げ観測も重なってドルが買われ、ドル円は153円61銭から154円35銭へ反発した（一時155円近辺まで上昇）。日経225先物は前日比1415円安の63120円で推移し、リスクオフ的な地合いも意識されている。今週はFOMC・BOE（9/17 20:00JST）・日銀会合（9/18 11:30JST）が集中する中銀ウィークで、本日9/15（火）は15:00の英雇用統計と21:30の米NY連銀製造業景気指数（Empire State）が焦点となる。'

ONE_LINER = 'サウジの東西パイプライン操業停止で原油高・FOMC利上げ観測が重なりドル円は154円台へ反発。本日は英雇用統計とNY連銀製造業景気指数に注目、中銀ウィークは木・金がヤマ場'

SUMMARY_LONG = (
    '9/14（月）のニューヨーク市場では、サウジアラビアがイエメンのフーシ派による攻撃への予防措置として主要な東西原油パイプラインの操業を停止したと伝わり、'
    '原油需給への懸念から原油価格が上昇した。これを受けてドル指数は200日移動平均線を上回る水準まで持ち直し、ドル円は153円61銭から一時155円近辺まで上昇したのち、'
    '154円35銭で取引を終えた（前営業日比約+74銭）。背景には、前週末9/11発表の米8月CPIのコア上振れを受けて今週9/15-16開催のFOMCでの追加利上げ観測が強まっていることもあり、'
    '「金利ウィーク」入りを市場が強く意識している（ニューヨーク為替市場関連報道より）。通貨オプション市場では週明けのイベントリスク上昇を受けてオプション買いが再開しており、'
    'FOMCを控えたボラティリティヘッジの動きが強まっている。一方で日経225先物は前日比1415円安の63120円で推移しており、株式市場の軟調さがリスクオフ的な地合いを示唆する場面もあった。'
    '中東情勢については、ホルムズ海峡再開を巡るイラン・オマーン協議の続報は本稿執筆時点で確認できておらず、地政学リスクプレミアムは原油市場を通じて燃料コスト・インフレ期待に波及し続けている（要確認）。'
    '本日9/15（火）は、日本時間15:00に英国の雇用統計（失業率・失業保険申請件数・平均賃金指数）が発表され、明後日9/17（木）20:00のBOE政策決定会合を控えた重要な判断材料となる。'
    '18:00には独・ユーロ圏のZEW景況感指数、21:30には米NY連銀製造業景気指数（Empire State、KissFXで最高ランク★★★）が発表される。'
    '今週は9/17未明3:00（JST）にFOMCの結果が判明し、同日20:00にBOE、翌9/18 11:30には日銀の政策決定会合の結果が判明する「中銀ウィーク」の本丸は木曜・金曜に集中しており、'
    '本日と明日は木・金に向けたポジション調整とヘッジの動きが主体になりやすい点に留意したい。'
)

RISK_LEVEL = 'MEDIUM'
RISK_TEXT = (
    '本日単体では英雇用統計（15:00・BOEを2日後に控えた重要指標）とNY連銀製造業景気指数（21:30・KissFXで最高ランク）が中心で、'
    '米国発の最重要指標（CPIや雇用統計本体）は本日にはない。ただし前日はサウジのパイプライン操業停止による原油高とFOMC利上げ観測の重なりでドルが全面高となっており、'
    '木曜未明のFOMC・木曜夜のBOE・金曜午前の日銀会合という主要中銀の決定が集中する週の入り口にあるため、木・金に向けてボラティリティが段階的に高まりやすい地合いを踏まえてMEDIUMとした。'
)

TOP_PAIR_NAME = 'USD/JPY 🇺🇸🇯🇵'
TOP_PAIR_TEXT = (
    '4Hデイトレ適性ランキング1位（9/14 06:32時点データ、スコア97・最適、ADX43.9で下降トレンド、直近5日ADRは5年平均の127.7%と値幅拡大）。'
    '前日はサウジのパイプライン操業停止に伴う原油高とFOMC利上げ観測が重なり、153円61銭から154円35銭へ反発した。'
    '本日は英雇用統計・NY連銀製造業景気指数はあるものの米国発の最重要指標はなく、木曜未明のFOMCに向けたポジション調整的な値動きが中心になりやすい。'
)

MARKET_HOLIDAY_H3 = '休場市場なし'
MARKET_HOLIDAY_P = '本日9/15（火）、主要国の市場休場はありません。'

KEY_EVENTS_ITEMS = [
    '11:00 🇨🇳 中国 鉱工業生産・小売売上高・固定資産投資',
    '13:30 🇯🇵 日本 第三次産業活動指数',
    '15:00 🇬🇧 英国 失業率・失業保険申請件数・平均賃金指数',
    '18:00 🇩🇪🇪🇺 独・ユーロ圏 ZEW景況感指数',
    '21:30 🇺🇸 NY連銀製造業景気指数（Empire State）',
]
KEY_EVENTS_HTML = '\n'.join(f'              <li>{item}</li>' for item in KEY_EVENTS_ITEMS)
KEY_EVENTS_HTML_MOBILE = '\n'.join(f'      <li>{item}</li>' for item in KEY_EVENTS_ITEMS)

OTHER_POINTS = [
    (
        'サウジの東西パイプライン操業停止で原油高、FOMC観測と重なりドル全面高',
        'サウジアラビアがイエメンのフーシ派による攻撃への予防措置として主要な東西原油パイプラインの操業を停止したと伝わり、原油価格が上昇。'
        'ドル指数は200日移動平均線を上回る水準まで持ち直し、ドル円は153円61銭から154円35銭まで反発した（ニューヨーク為替市場関連報道より）。',
    ),
    (
        '通貨オプション市場でヘッジ需要増加、FOMC控えボラティリティ意識',
        '週明けのイベントリスク上昇を受けてオプション買いが再開。短期の円コール買いは後退した一方、中期オプションではドル安ヘッジの動きが継続しており、'
        'FOMCを控えた市場のボラティリティ警戒が読み取れる。',
    ),
    (
        '日経225先物が急落（前日比1415円安の63120円）、リスクオフ的な地合いも',
        'CME円建て日経225先物は前営業日比1415円安の63120円で推移。株式市場の軟調さがリスクオフ地合いを示唆しており、円買い圧力につながる可能性がある一方、'
        'ドル円自体は原油高・金利観測を背景に上昇しており、方向感が交錯している。',
    ),
    (
        '今週は中銀ウィーク本番、FOMC・BOE・日銀の決定が木・金に集中',
        '今週はFOMC（結果判明9/17未明3:00JST）、BOE（9/17 20:00JST）、日銀（9/18 11:30JST・会見14:30JST）と主要中銀の政策決定が木曜・金曜に集中する。'
        '本日・明日はこれらに向けたポジション調整の値動きが主体になりやすい。',
    ),
    (
        '4Hデイトレ適性ランキングは前日06:32時点データを継続使用（本日分は未取得・要確認）',
        'RemoteTrigger環境からYahoo Financeへのアクセスが制限されているため、本日06:30予定のランキング自動更新ジョブの結果が本レポート作成時点で確認できていない。'
        '前日06:32時点のデータでは円クロスが上位を占め、いずれも下降トレンドが継続している（要確認）。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(
    f'              <li><strong>{title}</strong>：{body}</li>' for title, body in OTHER_POINTS
)

MARKET_ENV_TEXT = (
    '9/14（月）はサウジアラビアが東西原油パイプラインの操業停止を発表したことで原油価格が上昇し、ドル指数は200日移動平均線を上回る水準まで持ち直した。'
    '前週末9/11発表の米8月CPIのコア上振れを受けたFOMC〈9/15-16、結果判明は9/17未明3:00JST〉の利上げ観測もあり、ドル円は153円61銭から154円35銭へ反発した。'
    '通貨オプション市場では週明けのイベントリスク上昇を受けてヘッジ需要が高まっている一方、日経225先物は前日比1415円安と軟調に推移し、リスクオフ的な地合いも一部で意識されている。'
    '本日9/15（火）は米国発の最重要指標こそないものの、15:00の英雇用統計はBOE（9/17）の判断材料として、21:30のNY連銀製造業景気指数はKissFXで最高ランクに位置づけられており、いずれも注視したい。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.50〜3.75%（タカ派、FOMC〈9/15-16〉の利上げ確率が前週末CPI後に85%超まで上昇・要確認） / '
    '日銀 1.00%（正常化継続・タカ派寄り、9/17-18会合で1.25%への利上げ方針と報道・要確認） / '
    '英BOE 3.75%（中立〜やや引き締め警戒、次回会合9/17に本日の雇用統計が材料となる）'
)

RANKING_ROWS = [
    ('A', 'a', 'USD/JPY', 'ランキング1位（スコア97・最適）。ADX43.9で強い下降トレンド、直近5日ADRは5年平均の127.7%と値幅拡大', 'down'),
    ('A', 'a', 'EUR/JPY', 'ランキング2位（スコア93・最適）。ADX57.1で非常に強い下降トレンド、直近5日ADRは5年平均の121.1%', 'down'),
    ('A', 'a', 'GBP/JPY', 'ランキング3位（スコア84・最適）。ADX58.6で非常に強い下降トレンド、直近5日ADRは5年平均の108.9%', 'down'),
    ('B', 'b', 'AUD/JPY', 'ランキング4位（スコア76・適）。ADX62.5で非常に強い下降トレンド、直近5日ADRは5年平均の97.2%', 'down'),
    ('C', 'b', 'NZD/USD', 'ランキング5位（スコア49・見送り）。ADX28.5でやや弱い下降トレンド、直近5日ADRは5年平均の72.0%', 'down'),
]

def _rank_row(rank_label, rank_cls, pair, desc, direction):
    arrow = {'up': '↑', 'down': '↓', 'range': '→'}[direction]
    trend_cls = {'up': 'trend-up', 'down': 'trend-down', 'range': 'trend-range'}[direction]
    return f'''            <tr>
              <td><span class="rank-badge rank-{rank_cls}">{rank_label}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_cls}">{arrow}</span></td>
            </tr>'''

RANKING_ROWS_HTML = '\n'.join(_rank_row(*row) for row in RANKING_ROWS)

REVIEW_TOPICS = [
    (
        'ドル円が反発、153円61銭から154円35銭へ',
        '前週末9/11発表の米8月CPIコア上振れを受けたFOMC〈9/15-16〉の利上げ観測が続く中、9/14（月）のニューヨーク市場でドル円は153円61銭から154円35銭まで反発し、一時155円近辺まで上昇する場面もあった。',
    ),
    (
        'サウジが東西原油パイプラインの操業停止、原油高でドル指数が200日線を上回る',
        'サウジアラビアがイエメンのフーシ派による攻撃への予防措置として主要な東西原油パイプラインの操業を停止したと伝わり、原油価格が上昇。この地政学的リスクの高まりがドル買いにもつながり、ドル指数は200日移動平均線を上回る水準まで持ち直した。',
    ),
    (
        '通貨オプション市場でヘッジ需要が増加、FOMC控えボラティリティ意識',
        '週明けのイベントリスク上昇を受けてオプション買いが再開した。短期の円コール買いは後退した一方、中期オプションではドル安ヘッジの動きが継続しており、今週のFOMCを控えた市場のボラティリティ警戒がうかがえる。',
    ),
    (
        '米CPI受け「金利ウィーク」入り、中東情勢の不透明感で円債も微妙な位置',
        '前週末の米CPI結果を受けて利上げ確率が上昇し、市場は今週の主要中銀会合ラッシュを意識した「金利ウィーク」に入った。中東情勢の先行き不透明感も重なり、円債利回りも方向感の定まらない展開となっている。',
    ),
    (
        '日経225先物が急落、前日比1415円安の63120円で推移',
        'CME円建て日経225先物は前営業日比1415円安の63120円で推移した。株式市場の軟調さはリスクオフ的な地合いを示唆しており、為替市場でも安全資産としての円需要に一定の影響を与える可能性がある。',
    ),
]
REVIEW_TOPICS_HTML = '\n'.join(
    f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>'''
    for i, (title, body) in enumerate(REVIEW_TOPICS)
)

HANDOVER_TEXT = (
    '9/14（月）はサウジの東西パイプライン操業停止による原油高と、FOMC〈9/15-16〉の利上げ観測が重なりドルが買われ、ドル円は153円61銭から154円35銭へ反発した。'
    '日経225先物は1415円安と軟調で、リスクオフ的な地合いも一部で意識されている。本日9/15（火）は米国発の最重要指標こそないが、15:00の英雇用統計（BOEの判断材料）、'
    '18:00の独・ユーロ圏ZEW景況感指数、21:30のNY連銀製造業景気指数（KissFXで最高ランク）に注目。今週は9/17未明3:00（JST）のFOMC、9/17 20:00のBOE、9/18 11:30の日銀と'
    '主要中銀の決定が木・金に集中するため、本日・明日はそれに向けたポジション調整の値動きが中心になりやすい点に留意したい。'
)

# ── 経済指標カレンダー（KissFX × ForexFactory 2ソース照合） ─────────
CalRow = tuple  # (time, country_flag, name, importance_jp, forecast, previous, important_badge)

CALENDAR_ROWS = [
    ('10:30', '🇨🇳 中国', '新築住宅価格（ForexFactoryのみ・要確認）', '低', '—', '-0.18%', False),
    ('11:00', '🇨🇳 中国', '鉱工業生産【前年比】（KissFX・ForexFactory一致）', '低', '+4.8%', '+4.5%', False),
    ('11:00', '🇨🇳 中国', '小売売上高【前年比】（KissFX・ForexFactory一致）', '低', '+0.8%(KissFX)/+0.7%(FF)', '+0.6%', False),
    ('11:00', '🇨🇳 中国', '固定資産投資【年初来・前年比】（KissFX・ForexFactory一致）', '低', '-7.1%', '-6.7%', False),
    ('11:00', '🇨🇳 中国', '失業率（ForexFactoryのみ・要確認）', '低', '5.2%', '5.2%', False),
    ('11:00', '🇨🇳 中国', 'NBS記者会見（ForexFactoryのみ・要確認）', '低', '要人発言', '—', False),
    ('12:35', '🇯🇵 日本', '20年利付国債入札（KissFXのみ・要確認）', '高', '—', '—', False),
    ('13:30', '🇯🇵 日本', '第三次産業活動指数【前月比】（KissFX・ForexFactory一致）', '低', '+0.3%', '-0.2%', False),
    ('15:00', '🇬🇧 英', '失業保険申請件数（KissFX・ForexFactory一致）', '高', '—', '-1.10万件', True),
    ('15:00', '🇬🇧 英', '失業率（KissFX・ForexFactoryで重要度評価が相違：KissFX高/FF低・要確認）', '高', '5.0%(FF)', '4.3%(KissFX)/4.9%(FF)', True),
    ('15:00', '🇬🇧 英', '平均賃金指数【3ヶ月/前年比】（ForexFactoryのみ・要確認）', '中', '3.9%', '4.1%', False),
    ('15:02', '🇨🇳 中国', '対内直接投資【年初来・前年比】（ForexFactoryのみ・要確認）', '低', '—', '-6.2%', False),
    ('15:45', '🇫🇷 仏', '消費者物価指数【改定値・前月比】（KissFX・ForexFactory一致）', '中', '+0.7%', '+0.7%', False),
    ('17:00', '🇮🇹 伊', '貿易収支（ForexFactoryのみ・要確認）', '低', '47.7億', '42.3億', False),
    ('18:00', '🇩🇪 独', 'ZEW景況感指数（KissFX・ForexFactoryで予想値相違：KissFX+40.0/FF+39.8・要確認）', '中', '+40.0(KissFX)/+39.8(FF)', '+34.2', False),
    ('18:00', '🇪🇺 欧', 'ZEW景況感指数（KissFX・ForexFactory一致）', '中', '+39.2(FF)', '+31.4', False),
    ('18:00', '🇪🇺 欧', '貿易収支（KissFX・ForexFactoryで数値の単位・水準が相違・要確認）', '低', '37億(FF)', '86億(KissFX)/18億(FF)', False),
    ('21:15', '🇺🇸 米', 'ADP週間雇用者数変化（ForexFactoryのみ・要確認）', '低', '—', '1.2万人', False),
    ('21:30', '🇨🇦 加', '卸売売上高【前月比】（ForexFactoryのみ・要確認）', '低', '-0.5%', '+2.8%', False),
    ('21:30', '🇺🇸 米', 'NY連銀製造業景気指数（Empire State）（KissFX・ForexFactory一致・重要度評価は相違：KissFX最高/FF低）', '最高', '+15.0(KissFX)/+14.8(FF)', '+20.6', True),
    ('23:50', '🇳🇿 NZ', 'GDT価格指数（ForexFactoryのみ・要確認）', '低', '—', '+0.9%', False),
    ('翌05:00', '🇺🇸 米', '20年債入札（KissFXのみ・要確認）', '中', '130億ドル', '—', False),
]

def _cal_row(time_, country, name, importance, forecast, previous, important):
    badge = ' <span class="badge-important">★重要</span>' if important else ''
    if important:
        return f'            <tr><td><strong>{time_}</strong></td><td>{country}</td><td><strong>{name}</strong>{badge}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    return f'            <tr><td>{time_}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'

CALENDAR_ROWS_HTML = '\n'.join(_cal_row(*row) for row in CALENDAR_ROWS)
CALENDAR_COUNT = len(CALENDAR_ROWS)

SIDEBAR_ARCHIVE_FILES = [
    '2026-09-14（月）', '2026-09-11（金）', '2026-09-10（木）', '2026-09-09（水）', '2026-09-08（火）',
    '2026-09-07（月）', '2026-09-04（金）', '2026-09-03（木）', '2026-09-02（水）', '2026-09-01（火）',
]
SIDEBAR_ARCHIVE_HREFS = [
    '2026-09-14.html', '2026-09-11.html', '2026-09-10.html', '2026-09-09.html', '2026-09-08.html',
    '2026-09-07.html', '2026-09-04.html', '2026-09-03.html', '2026-09-02.html', '2026-09-01.html',
]
SIDEBAR_ARCHIVE_HTML = '\n'.join(
    f'<li><a href="{href}">{label}</a></li>' for href, label in zip(SIDEBAR_ARCHIVE_HREFS, SIDEBAR_ARCHIVE_FILES)
)

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
  <p>{HERO_SUMMARY}</p>
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
        <p class="sub">{HERO_SUMMARY}</p>
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
        <h3>{ONE_LINER}</h3>
        <p>{SUMMARY_LONG}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>{TOP_PAIR_NAME}</h3>
        <p>{TOP_PAIR_TEXT}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--orange,#c07a2b)">{RISK_LEVEL}</h3>
        <p>{RISK_TEXT}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{CALENDAR_COUNT}件</h3>
        <p>英雇用統計 / 独・ユーロ圏ZEW景況感指数 / NY連銀製造業景気指数 / 中国鉱工業生産・小売売上高 等（本日の市場休場はなし）</p>
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
              <li>{MARKET_HOLIDAY_P}</li>
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
          {MARKET_ENV_TEXT}
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
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">※ 4Hデイトレ適性ランキングは2026-09-14 06:32 JST時点のデータ（本日06:30予定の自動更新はRemoteTrigger環境からのYahoo Financeアクセス制限により本レポート作成時点で未反映・要確認）。数値は目安であり、実際のエントリーは各自のルールで判断してください。今週はFOMC・BOE・日銀会合を控えるため、通常のトレンドフォローに加えイベント前後の値動きにも注意してください。</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>📰 前日の相場振り返り（2026-09-14）</h3>
          <span>前日の主要トピック</span>
        </div>
        <div class="report-body">
{REVIEW_TOPICS_HTML}
          <div class="handover">
            <strong>本日（9/15火）への引継ぎ：{HANDOVER_TEXT}</strong>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻はJST。KissFX（主・ランク付き、https://kissfx.com/article/fxdays20260915.html）とForexFactoryの機械可読カレンダー（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値・重要度評価がソース間で相違する指標には「（要確認）」を付しています。中国の指標は発表時刻の公式指定がないため目安時刻です。本日は主要国の市場休場はありません。指標の網羅性は保証できないため、発表直前に各社カレンダーで再確認してください。</p>
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

with open('reports/2026-09-15.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('reports/2026-09-15.html generated')
