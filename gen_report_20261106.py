# -*- coding: utf-8 -*-
"""FX日報 2026-11-06（金）生成スクリプト"""
import glob, os
TODAY = '2026-11-06'
WEEKDAY = '金'
HERO_TITLE_SUB = ('前日11/5（木）はBOEが政策金利を4.00%へ引き上げポンドが買われた一方、米株が急落しドル円は158.50円から157.70円で引けた。本日11/6（金）は22:30の米雇用統計とカナダ雇用統計、25:00の植田日銀総裁発言が最大の材料。')
SUMMARY_HEADLINE = ('ドル円は157.70円引け、本日は22:30の米雇用統計（非農業部門雇用者数予想+6.0〜6.5万人）が方向を決める')
SUMMARY_BODY = ('11/5のドル円は158.50円まで買い戻された後、157.54円まで下落し157.70円で引けた（前営業日158.43円・ザイFX）。米新規失業保険申請件数が予想に反して減少し米長期金利が上昇したことがドルを支えたが、米株の急落でリスク回避の円買いも入った（ザイFX）。'
 'ドル円の1週間ボラティリティは6.23%と10/22以来の低水準で、材料が出れば動きが拡大しやすい（みんかぶ）。'
 '本日は22:30に米・加の雇用統計が重なり、25:00に植田日銀総裁が発言する（KissFX・ForexFactory一致）。')
TOP_PAIR_BODY = ('ドル円は11/5に157.54〜158.50円で推移し157.70円で引けた（ザイFX）。上値は159.10円以上にストップロスの買い、159.50円・160.00円に売りオーダーがあり、下値は157.80円付近にオーダーが集まる（ザイFX）。'
 '米雇用統計の非農業部門雇用者数は予想+6.0万人（KissFX）／+6.5万人（ForexFactory）、前回+2.9万人、失業率予想4.2%、平均時給は前月比+0.3%予想。強ければ米長期金利上昇でドル円は158円台後半を試し、弱ければ157円台前半を割り込みやすい。'
 '4時間足ランキング（11/5 09:27 JST生成・本日分は未更新）ではUSD/JPYは10位（見送り36、ADX15.0）。')
RISK_LEVEL = 'HIGH'
RISK_BODY = ('22:30に米雇用統計（非農業部門雇用者数・失業率・平均時給）とカナダ雇用統計が同時発表され、25:00に植田日銀総裁の発言が控える。'
 '米株は11/5にダウが1,741.67ドル安（-3.26%）、ナスダックは5%超の下落と報じられており（ザイFX・ナスダックの下落率はザイFX単独のため要確認）、リスク回避の波及で週末前の変動が拡大しやすい。'
 'イラン戦争の再開の可能性を伝える見出しもある（ザイFX・要確認）。')
KEY_EVENTS_COUNT = '5件'
KEY_EVENTS_SUMMARY = ('08:30 日本 毎月勤労統計（9月）、19:00 ユーロ圏小売売上高、22:30 米雇用統計・加雇用統計、25:00 植田日銀総裁の発言、24:00 米ミシガン大学消費者信頼感指数（速報値）。')
MARKET_OVERVIEW = ('<strong>VIX・米10年債/2年債利回り・DXY・WTI</strong>：月曜のみの取得項目のため本日は未取得。参考として、米10年債利回りは新規失業保険申請件数の減少を受けて上昇し、ドルを支えた（ザイFX）。'
 '<strong>株</strong>：NYダウは1,741.67ドル安（-3.26%）、ナスダック総合は5%超の下落（ザイFX）。半導体・AI関連株への売りが中心。'
 '<br><br><strong>ユーロドル：</strong>1.1230〜1.1235付近。ユーロのショートポジションが一段と拡大した（みんかぶ）。'
 '<br><br><strong>ボラティリティ：</strong>ドル円の1週間ボラティリティは6.23%と10/22以来の低水準、1カ月物は6.52%（みんかぶ・ザイFX）。'
 '<br><br><strong>今週の焦点：</strong> 11/6 米・加雇用統計、米ミシガン大学消費者信頼感指数（速報値）、植田日銀総裁の発言、ボウマンFRB副議長の発言（KissFX・ForexFactory）。')
RANKING_ROWS = [
 (1,'USD/JPY','rank-c','C','157.70円引け。22:30の米雇用統計が直接の材料で、159.10円以上のストップロス買いと157.80円付近のオーダーが両側に控える（ザイFX）。ランキング10位（見送り36、ADX15.0、上昇）。','trend-range','→'),
 (2,'GBP/USD','rank-c','C','BOEが4.00%へ利上げし8対1の決定、タカ派的と受け止められポンドは買われたが、マン委員の0.5%利上げ主張と次回判断への言及なしで一服した（ザイFX・みんかぶ）。ランキング6位（候補62、ADX34.8、上昇）。','trend-up','↑'),
 (3,'EUR/JPY','rank-c','C','177.10円割れでストップロスの売りが出る水準（ザイFX）。米株急落でクロス円は下押しされやすい。ランキング4位（適66、ADX23.7、上昇。11/5 09:27生成）。','trend-up','↑'),
 (4,'EUR/USD','rank-c','C','1.1230付近。ユーロのショートが拡大しており、米雇用統計が弱ければ買い戻しが入る（みんかぶ）。ランキング7位（候補60、ADX21.1、上昇）。','trend-range','→'),
 (5,'USD/CAD','rank-c','C','22:30に米・加の雇用統計が同時発表され振れ幅が最大になる。加雇用ネット変化は予想+1.46万人（FF）／+1.80万人（Kiss）、前回-6.83万人。ランキング8位（候補59、ADX32.9、下降）。','trend-down','↓'),
]
RANKING_ROWS_HTML = '\n'.join(f"""            <tr>
              <td><span class="rank-badge {b}">{l}</span></td>
              <td><strong>{p}</strong><br><span style="color:var(--muted);font-size:12px;">{d}</span></td>
              <td><span class="{tc}">{ar}</span></td>
            </tr>""" for r,p,b,l,d,tc,ar in RANKING_ROWS)
RANKING_NOTE = ('※ 4時間足ランキングは2026/11/05 09:27 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、11/5時点の数値。1位はEUR/AUD（最適91、ADX40.1、上昇）、2位USD/CHF（適79、ADX38.4、下降）。スコア・ADX・ADR比は補助指標であり、売買推奨ではない。上記の本日の優先順は当日のイベント（米・加雇用統計）を加味した並び。')
TOPICS = [
 ('米株が急落し、ドル円は158.50円から157.54円まで下落','米中間選挙で民主党が勝利したことでAI関連の進展が滞るとの懸念が広がり、半導体株を中心に売りが出た。NYダウは1,741.67ドル安（-3.26%）、ナスダック総合は5%超下落した（ザイFX・ナスダックの下落率は単独ソースのため要確認）。ドル円は158.50円付近まで買い戻された後、157.54円まで下げて157.70円で引けた（前営業日158.43円）。'),
 ('米新規失業保険申請件数が予想に反して減少し、米長期金利上昇でドルが下支え','新規失業保険申請件数が予想に反して減少し、57年ぶりの低水準になったと報じられた（ザイFX・具体的な件数は未確認）。米10年債利回りが上昇し、22時過ぎにドル円は一時158.5円付近まで買い戻された。みんかぶも「NY序盤はドルが円に対して底堅いが、明日の米雇用統計は重要な試金石」と伝えている。'),
 ('BOEが0.25ポイント利上げして4.00%に、ポンドは買われた後に一服','BOEは市場予想どおり政策金利を0.25ポイント引き上げ4.00%とした。決定は8対1で、マン委員は0.5ポイントの利上げを支持した（ザイFX）。事前の想定よりもタカ派な印象で追加利上げの織り込みからポンドが買われたが、マン委員の0.5%主張と次回判断への明言がなかったことでポンド買いは一服した（みんかぶ）。'),
 ('ドル円オプションでリスク警戒、ボラティリティは低水準','ドル円オプションでは変動率が上昇し、リスク警戒感から円コールの買いが強まった。下値のヘッジとみられる（ザイFX）。一方、1週間ボラティリティは6.23%と10/22以来の低水準まで低下しており（みんかぶ）、材料が出れば値幅が出やすい状態にある。'),
]
TOPICS_HTML = '\n'.join(f"""          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{t}</div>
            {b}
          </div>""" for i,(t,b) in enumerate(TOPICS))
HANDOVER = ('本日（11/6金）への引継ぎ：ドル円はNY終値157.70円。22:30の米雇用統計と25:00の植田日銀総裁発言が材料で、158円付近が次の手がかり。'
 '上値は159.10円以上にストップロス買い、159.50円・160.00円に売りオーダー、下値は157.80円付近にオーダー（ザイFX）。ユーロ円は177.10円割れでストップロス売り。'
 '米株急落の余波が東京時間のクロス円に残る。RBA政策金利（11/3）の結果は引き続き確認できない（要確認）。')
POINTS_EVENTS = [
 '08:30 🇯🇵 日 毎月勤労統計（9月・現金給与総額前年比 予想+3.8%、前回+3.8%）（FFのみ・要確認。ザイFXは08:30の発表予定と記載）',
 '16:00 🇩🇪 独 鉱工業生産（Kiss: 予想前月比-0.2%・前年比+2.0%／FF: 予想前月比0.0%。数値不一致のため要確認）',
 '19:00 🇪🇺 欧 小売売上高（予想前月比-0.1%、Kiss/FF一致。前回はKiss +0.6%／FF +0.1%で不一致・要確認）',
 '22:30 🇺🇸 米 雇用統計：非農業部門雇用者数（予想 Kiss +6.0万人／FF +6.5万人、前回+2.9万人）・失業率（予想4.2%、前回4.2%）・平均時給 前月比（予想+0.3%、前回+0.1%）（Kiss/FF一致）',
 '22:30 🇨🇦 加 雇用統計：雇用ネット変化（予想 Kiss +1.80万人／FF +1.46万人、前回-6.83万人）・失業率（予想6.5%、前回6.5%）（Kiss/FF一致）',
 '24:00 🇺🇸 米 ミシガン大学消費者信頼感指数【速報値】（Kiss: 予想47.6・前回48.0／FF: 予想48.1・前回46.3。不一致のため要確認）',
 '25:00 🇯🇵 日 植田日銀総裁の発言（Kiss/FF一致）',
 '26:15 🇺🇸 米 ボウマンFRB副議長の発言（Kiss/FF一致）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)
OTHER_POINTS = [
 ('米雇用統計：非農業部門雇用者数は予想+6.0〜6.5万人','前回は+2.9万人と低水準で、予想を上回れば米長期金利が上昇しドル円は158円台後半を試す。下回れば11/5の下値157.54円を割り込む。11/5の新規失業保険申請件数は予想に反して減少しており、雇用の底堅さが意識されている（ザイFX）。'),
 ('ドル円：158円付近が次の手がかり','159.10円以上にストップロスの買い、159.50円・160.00円に売りオーダー、157.80円付近にもオーダーがあり、NYカット（11/6 23:00 JST）前後で振れやすい（ザイFX）。'),
 ('植田日銀総裁の発言（25:00）','日銀の12月利上げ観測に対する言及が焦点。ドル円オプションでは円コールの買いが強まっており、タカ派的な発言なら円高方向への振れが拡大する。'),
 ('ポンド：BOE後の方向感','BOEの8対1の利上げ決定（マン委員は0.5%を主張）後、ポンド買いは一服した。21:15にピルMPC理事の発言があり、追加利上げの姿勢に言及するかが焦点（KissFX・FF一致）。'),
 ('ユーロ：ショート拡大','ユーロのショートポジションが一段と拡大している（みんかぶ）。19:00のユーロ圏小売売上高と米雇用統計の結果次第で買い戻しが起きる。'),
]
OTHER_POINTS_HTML = '\n'.join(f'              <li><strong>{t}</strong>：{b}</li>' for t,b in OTHER_POINTS)
CAL_ROWS = [
 ('06:00','🇨🇦 加','年次予算発表（FFのみ・要確認）','中','—','—'),
 ('08:30','🇯🇵 日','毎月勤労統計 現金給与総額 前年比（FFのみ・要確認）','低','+3.8%','+3.8%'),
 ('09:00','🇺🇸 米','ローガン・ダラス連銀総裁の発言（KissFXのみ・要確認）','—','—','—'),
 ('16:00','🇬🇧 英','ロイズ住宅価格指数 前月比（Kiss/FF一致）','低','0.0%','0.0%'),
 ('16:00','🇩🇪 独','鉱工業生産（Kiss: 前月比-0.2%・前年比+2.0%／FF: 前月比0.0%。要確認）','低','前月比-0.2%（FF 0.0%）','前月比+1.3%（FF +2.0%）'),
 ('16:45','🇫🇷 仏','貿易収支（Kiss/FF一致・単位表記が異なるため要確認）','低','FF -58億','Kiss -61.22億（FF -61億）'),
 ('16:45','🇫🇷 仏','経常収支（KissFXのみ・要確認）','—','—','-15億'),
 ('17:00','🇨🇭 スイス','外貨準備高（FFのみ・要確認）','低','—','7,700億'),
 ('17:00','🇨🇭 スイス','SECO消費者信頼感指数（FFのみ・要確認）','低','-35','-36'),
 ('18:30','🇺🇸 米','ウィリアムズNY連銀総裁の発言（投票権あり）（Kiss/FF一致）','低','—','—'),
 ('19:00','🇪🇺 ユーロ圏','小売売上高 前月比（Kiss/FF一致）','低','-0.1%','Kiss +0.6%（FF +0.1%）'),
 ('20:00','🇨🇭 スイス','テュディンSNB理事の発言（Kiss/FF一致）','低','—','—'),
 ('21:15','🇬🇧 英','ピルMPC理事の発言（Kiss/FF一致）','低','—','—'),
 ('22:30','🇨🇦 加','失業率（Kiss/FF一致）','高','6.5%','6.5%'),
 ('22:30','🇨🇦 加','雇用ネット変化（Kiss/FF一致）','高','Kiss +1.80万人（FF +1.46万人）','-6.83万人'),
 ('22:30','🇺🇸 米','雇用統計：非農業部門雇用者数（Kiss/FF一致）','高','Kiss +6.0万人（FF +6.5万人）','+2.9万人'),
 ('22:30','🇺🇸 米','雇用統計：失業率（Kiss/FF一致）','高','4.2%','4.2%'),
 ('22:30','🇺🇸 米','雇用統計：平均時給 前月比（Kiss/FF一致）','高','+0.3%','+0.1%'),
 ('22:30','🇺🇸 米','雇用統計：平均時給 前年比／製造業雇用者数（KissFXのみ・要確認）','—','+2.9%／+0.5万人','+3.0%／+0.9万人'),
 ('23:10','🇺🇸 米','ムサレム・セントルイス連銀総裁の発言（投票権なし）（Kiss/FF一致）','低','—','—'),
 ('24:00','🇨🇦 加','Ivey購買部協会指数（Kiss/FF一致）','中','Kiss 予想なし（FF 57.7）','58.2'),
 ('24:00','🇺🇸 米','ミシガン大学消費者信頼感指数【速報値】（Kiss/FF一致・数値不一致で要確認）','中','Kiss 47.6（FF 48.1）','Kiss 48.0（FF 46.3）'),
 ('24:00','🇺🇸 米','ミシガン大学インフレ期待（FFのみ・要確認）','中','—','4.7%'),
 ('25:00','🇯🇵 日','植田日銀総裁の発言（Kiss/FF一致）','高','—','—'),
 ('26:15','🇺🇸 米','ボウマンFRB副議長の発言（投票権あり）（Kiss/FF一致）','低','—','—'),
 ('29:00','🇺🇸 米','消費者信用残高（Kiss/FF一致）','低','Kiss +135億（FF +134億）','Kiss +82.81億（FF +83億）'),
]
def _key(r):
    t=r[0]
    if t=='終日': return (99,0)
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
        <em>{WEEKDAY}</em>
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
              <li>なし（KissFX・ForexFactory JSONに本日の主要市場休場の記載なし）</li>
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
          <h3>📰 前日の相場振り返り（2026-11-05 木）</h3>
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
