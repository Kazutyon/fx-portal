# -*- coding: utf-8 -*-
"""FX日報 2026-11-05（木）生成スクリプト"""
import glob, os
TODAY = '2026-11-05'
WEEKDAY = '木'
HERO_TITLE_SUB = ('前日11/4（水）は米中間選挙で民主党が上下両院を制し、ドル円は158.74円から157.41円まで急落した後、株高を受けて158円台前半（NY終値158.43円）へ戻した。本日11/5（木）は21:00のBOE政策金利（予想4.00%への利上げ）が最大の材料。')
SUMMARY_HEADLINE = ('ドル円は選挙で往って来いの158.43円引け、本日はBOEの利上げ（予想4.00%）とポンドの200日線攻防が主役')
SUMMARY_BODY = ('11/4のドル円は民主党優勢の報道で東京午後に157.41円まで売られたが、トランプ大統領が敗北を受け入れ民主党との協力に前向きな姿勢を示したことと株高で158.60円付近まで戻した（みんかぶ）。'
 'NY終値は158.43円で前日比26銭のドル安（ザイFX）。米10月ISM非製造業は54.5（予想54.8）と弱く、対イラン攻撃回避の期待でWTIが急落し米長期金利も低下したため、ドル買いは続かなかった（ザイFX）。'
 '本日21:00のBOE政策金利は25bp利上げの4.00%が予想（KissFX・ForexFactory一致）で、ポンドドルは200日線（1.3425付近）を上抜けて引けた（みんかぶ）。')
TOP_PAIR_BODY = ('ドル円は11/4に157.41〜158.74円で推移し、158.43円で引けた。200日線が158.60円付近にあり、前日は上抜けに失敗して上値が重い（みんかぶ）。'
 '下値は157円台前半で買いが入っている。米10年債利回りはISM非製造業の弱さと原油安で低下傾向のため、158.74円を超えるにはBOE後のドル高か株高の継続が必要。'
 '22:30の米新規失業保険申請件数（予想19.6万件）と翌6日の米雇用統計（失業率予想4.2%、非農業部門雇用者数予想+6.5万人・ザイFX）を前に、158円台前半が基準になる。'
 '4時間足ランキング（11/4 09:02 JST生成・本日分は未更新）ではUSD/JPYは11位（見送り32、ADX19.0）。')
RISK_LEVEL = 'HIGH'
RISK_BODY = ('21:00にBOE政策金利・四半期金融政策報告、21:30にベイリー総裁会見が重なり、ポンドと円クロスの変動が拡大する。'
 '米中間選挙後もイラン情勢は決着しておらず、イラン最高指導者は米国が「無条件降伏」を求めていると主張し、さらなる攻撃には「はるかに大規模な」報復で応じると発言している（ブルームバーグ・みんかぶ）。'
 '翌11/6は米雇用統計と植田日銀総裁の発言が控える。')
KEY_EVENTS_COUNT = '5件'
KEY_EVENTS_SUMMARY = ('08:50 日銀議事要旨、21:00 BOE政策金利・四半期報告、21:30 ベイリー総裁会見、22:30 米新規失業保険申請件数、27:00 ラガルドECB総裁の発言。米主要企業の決算はピーク。')
MARKET_OVERVIEW = ('<strong>VIX・米10年債/2年債利回り・DXY・WTI</strong>：月曜のみの取得項目のため本日は未取得。参考値として、米10年債利回りは4.96%まで戻した後に低下（ザイFX・フィスコ）、NY原油先物（WTI）は87.13ドルまで下落し1カ月ぶり安値、終値は前日比8.29%安（ザイFX・みんかぶ）。'
 '<strong>株</strong>：米ダウは午後2時台時点で1514.57ドル高の53301.29ドル（ザイFX）。日経平均は前日比893.23円安の62188.63円で大引け、後場には一時3000円超の下げとなった（ザイFX・みんかぶ）。欧州株は中間選挙通過で買いが再開し反発（ザイFX）。'
 '<br><br><strong>ユーロドル：</strong>NY終盤は1.1218ドル前後。1.1273ドルまで上昇後、独10年債利回りの低下を受けて反落した（ザイFX）。ECBの12月利上げは織り込まれている。'
 '<br><br><strong>今週の焦点：</strong> 11/5 BOE政策金利・米新規失業保険申請件数、11/6 米雇用統計・加雇用統計・植田日銀総裁の発言（KissFX）。')
RANKING_ROWS = [
 (1,'GBP/USD','rank-c','C','200日線（1.3425付近）を上抜けて引け、高値は1.3503ドル。21:00のBOEが4.00%への利上げでも、市場が織り込む4回の利上げをけん制すれば上昇は止まる（みんかぶ）。ランキング7位（見送り47、ADX26.8、上昇）。','trend-up','↑'),
 (2,'GBP/JPY','rank-c','C','213円台でポンド円も200日線を上抜けた（みんかぶ）。BOE結果で振れ幅が最大になる。ランキング9位（見送り45、ADX25.7、上昇）。','trend-up','↑'),
 (3,'EUR/JPY','rank-c','C','178円台前半。株高で円売りが強まり178.48円まで上昇した（ザイFX）。ランキング2位（候補56、ADX21.1、上昇。11/4 09:02生成）。','trend-up','↑'),
 (4,'USD/JPY','rank-c','C','158.43円引け。200日線158.60円付近が上値抵抗で、157円台では買いが入る。ランキング11位（見送り32、ADX19.0）。','trend-range','→'),
 (5,'EUR/USD','rank-c','C','1.12台前半のレンジ。ECB 12月利上げ織り込みと独金利低下が綱引き。ランキング6位（見送り47、ADX16.3）。','trend-range','→'),
]
RANKING_ROWS_HTML = '\n'.join(f"""            <tr>
              <td><span class="rank-badge {b}">{l}</span></td>
              <td><strong>{p}</strong><br><span style="color:var(--muted);font-size:12px;">{d}</span></td>
              <td><span class="{tc}">{ar}</span></td>
            </tr>""" for r,p,b,l,d,tc,ar in RANKING_ROWS)
RANKING_NOTE = ('※ 4時間足ランキングは2026/11/04 09:02 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、11/4時点の数値。1位はEUR/AUD（適77、ADX36.1、上昇）、3位USD/CHF（候補55）。スコア・ADX・ADR比は補助指標であり、売買推奨ではない。上記の本日の優先順は当日のイベント（BOE）を加味した並び。')
TOPICS = [
 ('米中間選挙で民主党が上下両院を制し、ドル円は157.41円まで急落後に反発','東京午前に民主党の優勢が伝わると、民主党がAI投資を抑制するとの警戒で株が急落し、ドル売り・円買いが広がった。ドル円は158.74円付近から157.41円まで下落し、日経平均は後場に一時3000円超下げた（みんかぶ）。その後トランプ大統領が劣勢を認め、民主党との協力に前向きな姿勢を示すと動揺が収まり、日経平均は安値から2000円以上反発してドル円も158円台を回復した（みんかぶ）。'),
 ('ロンドン・NYで株高のリスク選好が円売りを誘い、クロス円が上昇','ロンドンでは欧州株が堅調で、ユーロ円は177.15円から178.41円、ポンド円は212.13円から213.78円へ上昇した（みんかぶ）。トランプ政権の行動を議会が抑止し、インフレや紛争に歯止めがかかるとの期待が背景。NYではダウが一時1700ドル超上昇し、ユーロ円は178.48円まで上昇した（みんかぶ・ザイFX）。'),
 ('米指標はまちまち、ISM非製造業の弱さと原油急落で米金利が低下しドル売りが再開','NYでドル円は米10月ADP雇用者数（+8.6万人、予想+6.7万人）と9月貿易赤字の縮小で158.67円まで上昇したが、10月ISM非製造業が54.5（予想54.8）に届かなかった。さらに米の対イラン攻撃激化懸念が後退して原油が急落し、長期金利が低下して158.16円まで下落、158.43円で引けた（ザイFX・フィスコ）。'),
 ('ポンドは200日線を上抜け、BOE会合を前に利上げの織り込み度合いが焦点','ポンドドルは1.3408ドルから1.3503ドルまで上昇し、200日線（1.3425付近）を上抜けた（みんかぶ）。BOEの利上げは確実視されているが、新指標では粘着的・中核的インフレ率が9月に3.3%で横ばいと物価上昇圧力が強まっておらず、短期市場が織り込む4回の利上げ（本日分を含む）を総裁会見でけん制するとの見方がある（みんかぶ）。'),
]
TOPICS_HTML = '\n'.join(f"""          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{t}</div>
            {b}
          </div>""" for i,(t,b) in enumerate(TOPICS))
HANDOVER = ('本日（11/5木）への引継ぎ：ドル円はNY終値158.43円で、200日線158.60円付近が上値抵抗。トランプ大統領は敗北を受け入れたが、イラン最高指導者は「無条件降伏」要求と報復を主張しており、中東情勢は未解決（ブルームバーグ・みんかぶ）。'
 '本日21:00のBOE（予想4.00%への利上げ）の結果とベイリー総裁会見でポンドの200日線攻防が決まる。RBA政策金利（11/3）の結果は引き続き確認できない（要確認）。')
POINTS_EVENTS = [
 '08:50 🇯🇵 日 日銀政策委員会・金融政策決定会合議事要旨（9月17・18日開催分）（Kiss/FF一致）',
 '09:30 🇦🇺 豪 貿易収支（予想+10.00億、前回+4.95億。FFは予想+9.4億、前回+5.0億）（Kiss/FF一致）',
 '21:00 🇬🇧 英 BOE政策金利（予想4.00%＝25bp利上げ、前回3.75%）／政策金利声明／四半期金融政策報告（Kiss/FF一致）',
 '21:30 🇬🇧 英 ベイリーBOE総裁の記者会見（Kiss/FF一致）',
 '22:30 🇺🇸 米 新規失業保険申請件数（予想19.6万件、前回19.4万件）／第3四半期非農業部門労働生産性【速報値】（予想+2.7%、前回+1.4%）（Kiss/FF一致）',
 '22:50 🇺🇸 米 ハマック・クリーブランド連銀総裁の発言（投票権あり）／23:10 バーキン・リッチモンド連銀総裁の発言（Kiss/FF一致）',
 '24:30 🇨🇦 加 マックレムBOC総裁の発言（KissFXのみ・要確認）／27:00 🇪🇺 欧 ラガルドECB総裁の発言（KissFXのみ・要確認）',
 '米主要企業の決算発表（ピーク）（KissFX）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)
OTHER_POINTS = [
 ('ポンド：21:00のBOEが4.00%へ利上げなら織り込み済みで、ガイダンスが焦点','予想は25bp利上げの4.00%（前回3.75%）。短期市場は本日を含め4回の利上げを織り込んでおり、四半期報告とベイリー総裁会見が今後の利上げペースを抑える内容ならポンドは200日線を割り込みやすい。逆に追加利上げを示唆すれば1.35ドル台に定着する。'),
 ('ドル円：158円台前半、200日線158.60円付近が上値抵抗','米10年債利回りの低下（ISM非製造業の弱さと原油安）がドルの上値を抑える。157円台前半では買いが入っており、レンジの下限は157.41円、上限は158.74円。'),
 ('イラン情勢：選挙後も決着せず','トランプ大統領は敗北の一因にイラン戦争を暗に認めたが、イラン最高指導者は米国が「無条件降伏」を求めていると主張している。原油は87ドル台まで急落しており、攻撃再開の報道が出れば逆に急反発する局面（ブルームバーグ・みんかぶ）。'),
 ('日銀議事要旨（08:50）と翌日の植田総裁発言','10/30会合で据え置きとなった日銀の12月利上げ観測が、議事要旨で強まるか後退するかが円の材料。11/6には植田総裁の発言がある（KissFX）。'),
 ('翌11/6：米雇用統計','失業率予想4.2%、非農業部門雇用者数予想+6.5万人（9月は2.92万人）、平均時給は前月比+0.3%の見込み（ザイFX）。本日22:30の新規失業保険申請件数が先行指標。'),
]
OTHER_POINTS_HTML = '\n'.join(f'              <li><strong>{t}</strong>：{b}</li>' for t,b in OTHER_POINTS)
CAL_ROWS = [
 ('08:50','🇯🇵 日','日銀 金融政策決定会合議事要旨（9月17・18日分）（Kiss/FF一致）','低','—','—'),
 ('09:30','🇦🇺 豪','貿易収支（Kiss/FF一致）','低','+10.00億（FF +9.4億）','+4.95億（FF +5.0億）'),
 ('09:30','🇦🇺/🇯🇵','サービス業PMI 52.0／総合PMI 52.3（ザイFX「本日のスケジュール」記載のみ・国表記なし・要確認）','—','—','—'),
 ('12:35','🇯🇵 日','10年利付国債入札（Kiss/FF一致）','低','—','—'),
 ('15:45','🇦🇺 豪','RBAハウザー副総裁の発言（FFのみ・要確認）','低','—','—'),
 ('16:00','🇩🇪 独','製造業受注 前月比（Kiss/FF一致）','低','+4.5%（FF +4.6%）','-10.6%'),
 ('16:45','🇫🇷 仏','鉱工業生産 前月比（Kiss/FF一致）','低','+0.3%','-0.3%'),
 ('16:45','🇫🇷 仏','製造業生産指数 前月比（KissFXのみ・要確認）','低','—','+0.3%'),
 ('17:00','🇨🇭 スイス','失業率（Kiss/FF一致）','低','3.0%（FF 3.1%）','3.0%（FF 3.1%）'),
 ('18:00','🇮🇹 伊','小売売上高 前月比（FFのみ・要確認）','低','0.0%','+0.3%'),
 ('18:30','🇬🇧 英','建設業PMI（Kiss/FF一致）','低','46.5（FF 46.4）','46.1'),
 ('19:00','🇪🇺 ユーロ圏','生産者物価指数 前月比（Kiss/FF一致）','低','+2.5%','+1.9%'),
 ('19:03','🇪🇸 西','10年債入札（FFのみ・要確認）','低','—','4.18%'),
 ('19:18','🇫🇷 仏','10年債入札（FFのみ・要確認）','低','—','4.93%'),
 ('19:30','🇺🇸 米','チャレンジャー人員削減予定数（Kiss/FF一致）','低','—','-19.9%'),
 ('21:00','🇬🇧 英','BOE政策金利（Kiss/FF一致）','高','4.00%（25bp利上げ）','3.75%（据え置き）'),
 ('21:00','🇬🇧 英','BOE MPC票数（FFのみ・要確認）','高','7-0-2','3-0-6'),
 ('21:00','🇬🇧 英','BOE政策金利声明／議事録／四半期金融政策報告（Kiss/FF一致）','高','—','—'),
 ('21:30','🇬🇧 英','ベイリーBOE総裁の記者会見（Kiss/FF一致）','高','—','—'),
 ('21:40','🇨🇭 スイス','シュレーゲルSNB総裁の発言（Kiss/FF一致）','中','—','—'),
 ('22:30','🇺🇸 米','新規失業保険申請件数（Kiss/FF一致）','中','19.6万件（FF 19.7万件）','19.4万件'),
 ('22:30','🇺🇸 米','第3四半期非農業部門労働生産性【速報値】（Kiss/FF一致）','低','+2.7%（FF +2.8%）','+1.4%'),
 ('22:30','🇺🇸 米','第3四半期単位労働費用【速報値】（Kiss/FF一致）','低','+0.5%（FF +0.3%）','+1.2%（FF +1.3%）'),
 ('22:50','🇺🇸 米','ハマック・クリーブランド連銀総裁の発言（Kiss/FF一致）','低','—','—'),
 ('23:10','🇺🇸 米','バーキン・リッチモンド連銀総裁の発言（Kiss/FF一致）','低','—','—'),
 ('24:30','🇨🇦 加','マックレムBOC総裁の発言（KissFXのみ・要確認）','—','—','—'),
 ('24:30','🇺🇸 米','週間天然ガス貯蔵量（KissFXのみ・要確認）','—','—','+80'),
 ('26:45','🇩🇪 独','ナーゲル独連銀総裁の発言（KissFXのみ・要確認）','—','—','—'),
 ('27:00','🇪🇺 欧','ラガルドECB総裁の発言（KissFXのみ・要確認）','—','—','—'),
 ('終日','🇺🇸 米','主要企業の決算発表（ピーク）（KissFX）','—','—','—'),
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
          <h3>📰 前日の相場振り返り（2026-11-04 水）</h3>
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
