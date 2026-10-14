# -*- coding: utf-8 -*-
"""FX日報 2026-10-15（木）生成スクリプト"""
import glob, os

TODAY = '2026-10-15'
WEEKDAY = '木'

HERO_TITLE_SUB = (
    '前営業日10/14（水）はドル円が米9月CPIの上振れで158円95銭まで上昇したあと、158円05銭まで押し戻されて引けた。'
    '本日10/15（木）は休場なしで、21:30の米小売売上高と生産者物価指数、15:00の英GDPが主要材料となる。'
)

SUMMARY_HEADLINE = (
    'ドル円はCPI上振れ後に158円95銭から158円05銭へ反落、ドル独歩高は一服。'
    '本日は21:30の米小売売上高・PPIと15:00の英GDPが焦点'
)

SUMMARY_BODY = (
    '10/14（水）のドル円は、米9月CPIが予想を上回って158円95銭まで上昇したが、米大手金融の決算が期待に届かずドル買いが後退し、158円05銭まで押し戻された（ザイFX・みんかぶ）。'
    'ユーロドルは一時1.1191ドルまで下げた（みんかぶ）。'
    '本日10/15は休場がなく、流動性は通常どおり（KissFX・ForexFactoryで休場の記載なし）。'
)

TOP_PAIR_BODY = (
    '4時間足ランキング（10/14 08:21 JST生成・本日分は未更新）ではUSD/CADが1位・候補判定（スコア56、ADX23.7、方向はレンジ）。'
    '21:30に米小売売上高（前月比予想+0.3％・前回+1.2％）とPPIが出るため、ドル側の変動要因が重なる。'
    'カナダは21:30に製造業出荷と卸売売上高が出る。方向が出ていないため、15分・30分足で高値安値の切り上げか切り下げが確認できてからの順張りが基本となる。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    '21:30に米小売売上高（前月比予想+0.3％）、PPI（前月比予想+0.6％・前年比予想+5.4％）、フィラデルフィア連銀景況指数（予想28.0前後）が集中する。'
    'CPIの上振れ直後でインフレ指標への感応度が高く、PPIが予想を上回ればドル買い、下回ればドル売りで反応する。'
    '15:00の英GDP（前月比予想-0.1％・前回+0.4％）と09:30の豪雇用統計も値動きを生む。'
)

KEY_EVENTS_COUNT = '9件'
KEY_EVENTS_SUMMARY = (
    '日 機械受注(08:50)・小枝日銀審議委員発言(10:30) / 豪 失業率・雇用者数(09:30) / スイス シュレーゲルSNB総裁発言(13:30) / 英 GDP(15:00)・ベイリーBOE総裁発言(16:30) / 米 小売売上高・PPI・フィラデルフィア連銀(21:30)'
)

MARKET_OVERVIEW = (
    '10/14（水）は米9月CPIが予想を上回り、ドル円は158円95銭まで上昇したあと158円05銭まで押し戻された（ザイFX）。'
    'CPIの前月比は4月以来の高い伸びで、原油高が物価を押し上げた背景がある（ザイFX）。ただし米大手金融の決算が市場の高い期待を下回り、ドルの一方的な買いは後退した。'
    'ユーロドルは一時1.1191ドルまで安値を広げ、英中銀のピル委員は市場が織り込む4回の利上げに懐疑的な見解を示した（みんかぶ）。'
    '本日は休場がなく、日本時間の日中は日銀の小枝審議委員の発言（10:30）、英GDP（15:00）、BOEのベイリー総裁発言（16:30）、夜は21:30の米指標が材料になる。'
    '<br><br><strong>政策金利：</strong> 本日は木曜日のため前回更新（10/12）の値を引き継ぐ。FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（詳細は週次更新の月曜日版を参照）。'
    '<br><br><strong>今週の焦点：</strong> 本日10/15に米小売売上高と生産者物価指数。次回FOMCは10/28、日銀は10/30、ECBは10/29。'
)

RANKING_ROWS = [
    (1, 'USD/CAD', 'rank-b', 'B', '直近スコア56・候補。ADX23.7、ADR比99.4％、方向はレンジ。21:30に米小売売上高とカナダ卸売売上高が重なる。', 'trend-range', '→'),
    (2, 'EUR/USD', 'rank-c', 'C', '直近スコア48・見送り。ADX24.2、ADR比90.1％、方向はレンジ。10/14は一時1.1191ドルまで下げた（みんかぶ）。', 'trend-range', '→'),
    (3, 'EUR/AUD', 'rank-c', 'C', '直近スコア47・見送り。ADX34.9、方向は下降。ADR比50.9％と値幅が5年平均の半分で、09:30の豪雇用統計が値幅の出る場面。', 'trend-down', '↓'),
    (4, 'EUR/JPY', 'rank-c', 'C', '直近スコア40・見送り。ADX23.3、ADR比79.2％、方向はレンジ。', 'trend-range', '→'),
    (5, 'USD/JPY', 'rank-c', 'C', '直近スコア33・見送り。ADX26.9、ADR比60.5％、方向はレンジ。5日ADRは67.6pipsで5年平均111.7pipsを下回る。', 'trend-range', '→'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/14 08:21 JST生成分（本日分は未更新・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        '米9月CPIが予想を上回り、ドル円は158円95銭まで上昇後に158円05銭へ反落',
        '米9月消費者物価指数は前年比で8月から加速し、予想を上回った。前月比は4月以来の高い伸びで、原油高が物価を押し上げた（ザイFX）。'
        'ドル円は158円95銭まで上昇したが、158円05銭まで押し戻されて引けた。ドル円は一時200日移動平均線を上回ったものの維持できなかった（みんかぶ）。',
    ),
    (
        '米大手金融の決算が期待に届かず、ドル買いが後退',
        '米大手金融の収益が市場の高い期待を下回り、ニューヨーク外為市場でドル買いが後退した（ザイFX）。'
        'CPIの上振れで積み上がったドル買いポジションの手じまいが出やすい状況だった。',
    ),
    (
        'ユーロは1.1191ドルまで下落、ECBの急速な利上げ見通しに後退の指摘',
        '投資家が織り込んでいたユーロ圏の急速な利上げ見通しが後退する可能性が指摘され、ユーロドルは一時1.1191ドルまで安値を広げた（みんかぶ）。'
        '英中銀のピル委員も、市場が織り込む4回の利上げに懐疑的な見解を示した。',
    ),
    (
        '米地区連銀経済報告は物価上昇の賃金への波及を指摘',
        'ベージュブックは物価上昇や賃金への波及を示す一方、成長は地区ごとにまちまちとした（ザイFX）。'
        '米30年固定の住宅ローン金利は7.50%と高水準で、住宅ローン申請指数は前週比-2.7%だった（みんかぶ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/15木）への引継ぎ：ドル円は158円05銭で前営業日を終えた。'
    '本日は休場がなく、21:30の米小売売上高（前月比予想+0.3％）とPPI（前月比予想+0.6％）が最大の材料。'
    '日中は10:30の小枝日銀審議委員の発言と15:00の英GDPが円とポンドの方向を決める。CPI後のドル高が一服した水準で、158円台後半が上値、157円台後半が下値の目安となる。'
)

POINTS_EVENTS = [
    '08:50 🇯🇵 日本 機械受注（前月比予想+2.2〜2.3％・前回-3.7％。Kiss/FFで予想差・要確認）',
    '09:30 🇦🇺 豪州 失業率（予想4.6％・前回4.6％）・新規雇用者数（Kiss予想+2.00万人／FF予想+1.96万人・前回+3.95万人。予想差・要確認）',
    '10:30 🇯🇵 日本 小枝日銀審議委員 発言（KissFX・ザイFX確認）',
    '13:30 🇨🇭 スイス シュレーゲルSNB総裁 発言（Kiss/FF一致）',
    '15:00 🇬🇧 英国 GDP（前月比予想-0.1％・前回+0.4％。Kiss/FF一致）',
    '16:30 🇬🇧 英国 ベイリーBOE総裁 発言（FFのみ・要確認）',
    '21:30 🇺🇸 米国 小売売上高（前月比予想+0.3％・前回+1.2％。Kiss/FF一致）',
    '21:30 🇺🇸 米国 生産者物価指数（前月比予想+0.6％・前回+0.4％／コア前月比予想+0.3％・前回+0.2％。Kiss/FF一致）',
    '21:30 🇺🇸 米国 フィラデルフィア連銀景況指数（Kiss予想+28.0／FF予想28.2・前回+37.8。予想差・要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：CPI後の反落で158円台前半、PPIと小売売上高が次の分岐点',
        'ドル円は10/14に158円95銭まで上昇したあと158円05銭で引けた。200日移動平均線を維持できなかったため、158円台前半を割り込めば157円台後半が下値の目安となり、'
        'PPIが予想の前月比+0.6％を上回ればインフレ継続がFRBの追加利上げ観測を支え、158円台後半へ戻る（ザイFX・みんかぶ）。'
        '10:30の小枝日銀審議委員の発言で追加利上げに前向きな内容が出れば円買いが入る。',
    ),
    (
        '豪ドル：09:30の雇用統計',
        '失業率は予想4.6％（前回4.6％）、新規雇用者数は予想+2万人前後（前回+3.95万人）。雇用者数が予想を上回ればRBAの追加利上げ観測が強まり豪ドル買い、下回れば豪ドル売りになる。'
        'RBAは9/29に0.25%利上げ済みで、次回会合は11/3。13:25にはRBA年次報告書の公表もある（FFのみ・要確認）。',
    ),
    (
        'ポンド：15:00の英GDPと16:30のベイリーBOE総裁発言',
        '英GDP（前月比）は予想-0.1％で前回+0.4％から失速する予想。予想を下回ればBOEの追加利上げ観測が後退してポンド売り、予想以上ならポンド買いになる。'
        'ピルMPC委員は市場が織り込む4回の利上げに懐疑的で（みんかぶ）、ベイリー総裁が同調すればポンド売りが加速する。次回BOE会合は11/5。',
    ),
    (
        'スイスフラン：13:30のシュレーゲルSNB総裁発言',
        'SNBは政策金利0.00%を維持しており、事実上フラン安を容認しているとの評価がある。総裁が為替介入や追加緩和に触れればフラン売り、フラン高を容認する発言ならフラン買いになる。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('02:30', '🇺🇸 米', 'バーキン・リッチモンド連銀総裁 発言（FFのみ・発表済み・要確認）', '低', '要人発言', '—'),
    ('03:00', '🇺🇸 米', '地区連銀経済報告（ベージュブック）（FFのみ・発表済み・要確認）', '低', '—', '—'),
    ('04:00', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（FF 04:00／Kiss 23:00で時刻不一致・要確認）', '低', '要人発言', '—'),
    ('05:30', '🇺🇸 米', 'API週間統計報告（FFのみ・要確認）', '低', '—', '—'),
    ('08:50', '🇯🇵 日', '機械受注 [前月比]（Kiss +2.3％／FF +2.2％で予想不一致・要確認）', '低', '+2.3% / +2.2%', '-3.7%'),
    ('08:50', '🇯🇵 日', '機械受注 [前年比]（Kissのみ・要確認）', '低', '+15.6%', '+11.2%'),
    ('09:30', '🇦🇺 豪', '失業率（Kiss/FF一致）', '高', '4.6%', '4.6%'),
    ('09:30', '🇦🇺 豪', '新規雇用者数（Kiss +2.00万人／FF +19.6Kで予想不一致・要確認）', '高', '+2.00万人 / +1.96万人', '+3.95万人'),
    ('10:30', '🇯🇵 日', '小枝日銀審議委員 発言（あいさつ）（KissFX・ザイFX確認）', '中', '要人発言', '—'),
    ('時間未定', '🇯🇵 日', '小枝日銀審議委員 発言（記者会見）（Kissのみ・要確認）', '中', '要人発言', '—'),
    ('11:55', '🇺🇸 米', 'ボウマンFRB副議長 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('12:35', '🇬🇧 英', 'ピルMPC委員 発言（Kiss 12:40／FF 12:35で時刻不一致・要確認）', '低', '要人発言', '—'),
    ('13:25', '🇦🇺 豪', 'RBA年次報告書（FFのみ・要確認）', '低', '—', '—'),
    ('13:30', '🇯🇵 日', '鉱工業生産【確報値】 [前月比]（Kiss/FF一致）', '低', '—（FF -1.7%）', '-1.7%'),
    ('13:30', '🇯🇵 日', '鉱工業生産【確報値】 [前年比]（Kissのみ・要確認）', '低', '—', '+3.4%'),
    ('13:30', '🇨🇭 スイス', 'シュレーゲルSNB総裁 発言（Kiss/FF一致）', '中', '要人発言', '—'),
    ('15:00', '🇬🇧 英', 'GDP [前月比]（Kiss/FF一致）', '高', '-0.1%', '+0.4%'),
    ('15:00', '🇬🇧 英', '鉱工業生産 [前月比]（Kiss/FF一致）', '低', '-0.1%', '+0.2%'),
    ('15:00', '🇬🇧 英', '鉱工業生産 [前年比]（Kissのみ・要確認）', '低', '+0.7%', '+2.6%'),
    ('15:00', '🇬🇧 英', '製造業生産高 [前月比]（Kiss ±0.0％／FF -0.1％で予想不一致・要確認）', '低', '±0.0% / -0.1%', '+0.9%'),
    ('15:00', '🇬🇧 英', '製造業生産高 [前年比]（Kissのみ・要確認）', '低', '+2.3%', '+2.6%'),
    ('15:00', '🇬🇧 英', '商品貿易収支（Kiss -219.00億／FF -21.9B）', '低', '-219億', '-209.65億'),
    ('15:00', '🇬🇧 英', '貿易収支（Kissのみ・要確認）', '低', '-41.5億', '-34.5億'),
    ('15:00', '🇬🇧 英', '建設生産高 [前月比]（FFのみ・要確認）', '低', '0.0%', '0.1%'),
    ('15:00', '🇬🇧 英', 'サービス業指数 [3か月/3か月]（FFのみ・要確認）', '低', '0.8%', '0.6%'),
    ('15:30', '🇨🇭 スイス', '生産者輸入価格 [前月比]（Kiss/FF一致）', '低', '—（FF +0.6%）', '+0.7%'),
    ('15:30', '🇨🇭 スイス', '生産者輸入価格 [前年比]（Kissのみ・要確認）', '低', '—', '-0.7%'),
    ('15:45', '🇫🇷 仏', '消費者物価指数【改定値】 [前月比]（Kiss/FF一致）', '低', '-0.3%', '-0.3%'),
    ('15:45', '🇫🇷 仏', '消費者物価指数【改定値】 [前年比]（Kissのみ・要確認）', '低', '+3.0%', '+3.0%'),
    ('15:45', '🇬🇧 英', 'グリーンMPC委員 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('16:30', '🇬🇧 英', 'ベイリーBOE総裁 発言（FFのみ・要確認）', '中', '要人発言', '—'),
    ('17:45', '🇬🇧 英', 'ブリーデンMPC委員 発言（Kiss/FF一致）', '低', '要人発言', '—'),
    ('18:00', '🇨🇦 加', 'ロジャーズBOC上級副総裁 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('18:00', '🇪🇺 欧', '鉱工業生産 [前月比]（Kiss/FF一致）', '低', '±0.0%', '-0.1%'),
    ('18:00', '🇪🇺 欧', '鉱工業生産 [前年比]（Kissのみ・要確認）', '低', '-0.1%', '±0.0%'),
    ('19:15', '🇪🇺 欧', 'EU経済サミット（FFのみ・要確認）', '中', '—', '—'),
    ('21:30', '🇨🇦 加', '製造業出荷（Kiss/FF一致）', '低', '+1.1%', '-0.4%'),
    ('21:30', '🇨🇦 加', '卸売売上高（Kiss/FF一致）', '低', '-1.5%', '+0.3%'),
    ('21:30', '🇺🇸 米', '新規失業保険申請件数（Kiss 20.0万件／FF 199Kで予想不一致・要確認）', '中', '20.0万件 / 19.9万件', '19.7万件'),
    ('21:30', '🇺🇸 米', '小売売上高 [前月比]（Kiss/FF一致）', '高', '+0.3%', '+1.2%'),
    ('21:30', '🇺🇸 米', '小売売上高【除自動車】 [前月比]（Kiss +0.5％／FF +0.6％で予想不一致・要確認）', '高', '+0.5% / +0.6%', '+1.4%'),
    ('21:30', '🇺🇸 米', '生産者物価指数 [前月比]（Kiss/FF一致）', '高', '+0.6%', '+0.4%'),
    ('21:30', '🇺🇸 米', '生産者物価指数 [前年比]（Kissのみ・要確認）', '高', '+5.4%', '+5.4%'),
    ('21:30', '🇺🇸 米', '生産者物価指数【コア】 [前月比]（Kiss/FF一致）', '高', '+0.3%', '+0.2%'),
    ('21:30', '🇺🇸 米', '生産者物価指数【コア】 [前年比]（Kissのみ・要確認）', '高', '+4.4%', '+4.6%'),
    ('21:30', '🇺🇸 米', 'フィラデルフィア連銀景況指数（Kiss +28.0／FF +28.2で予想不一致・要確認）', '中', '+28.0 / +28.2', '+37.8'),
    ('21:30', '🇺🇸 米', 'NY連銀製造業景気指数（Kiss +12.3／FF +12.1で予想不一致・要確認）', '低', '+12.3 / +12.1', '+7.6'),
    ('23:00', '🇺🇸 米', '企業在庫（Kiss/FF一致）', '低', '+0.4%', '+0.8%'),
    ('23:00', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（Kissのみ・FFは04:00・要確認）', '低', '要人発言', '—'),
    ('23:15', '🌐 全', 'IMF会合（FFのみ・要確認）', '低', '—', '—'),
    ('23:30', '🇺🇸 米', '週間天然ガス貯蔵量（Kiss/FF一致）', '低', '—（FF 76B）', '+85'),
    ('25:00', '🇺🇸 米', '週間原油在庫（Kissのみ・要確認）', '低', '—', '-318.6万'),
    ('29:30', '🇺🇸 米', 'ハマック・クリーブランド連銀総裁 発言（Kissのみ・要確認）', '低', '要人発言', '—'),
    ('30:30', '🇳🇿 NZ', '製造業PMI（Kissのみ・要確認）', '低', '—', '53.1'),
]
CAL_ROWS.sort(key=lambda r: (int(r[0][:2]) if r[0][0].isdigit() else 10, r[0] if r[0][0].isdigit() else '10:31'))

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

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
        <em>木曜日</em>
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
        <h3>EUR/USD 🇪🇺🇺🇸</h3>
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
              <li>休場なし（日本・米国・カナダ・欧州とも通常営業。KissFX・ForexFactoryで本日の休場の記載なし）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-14）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はForexFactory区分（KissFXのランクは画像表記のため取得不可）。</p>
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
