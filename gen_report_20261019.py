# -*- coding: utf-8 -*-
"""FX日報 2026-10-19（月）生成スクリプト"""
import glob, os

TODAY = '2026-10-19'
WEEKDAY = '月'

HERO_TITLE_SUB = (
    '前営業日10/16（金）のドル円は157円70銭〜158円34銭で推移し、158円02銭で引けた。'
    '本日10/19（月）は香港が休場（中国は要確認）で、米国の注目指標はなく、21:30のカナダCPIが主な材料。来週の10/28FOMC・10/30日銀会合を前にFRB高官は発言禁止期間に入る。'
)

SUMMARY_HEADLINE = (
    'ドル円は米金利低下と原油高に挟まれ158円02銭で週末を終え、週明けはフランスのデモ暴徒化でユーロが1.1183ドルへ下落。'
    '本日は米国の注目指標がなく、21:30のカナダCPIが主な材料'
)

SUMMARY_BODY = (
    '10/16（金）のNY市場では、米債利回りの低下を背景にドル売りが強まりドル円は157.70円まで下落したが、NY原油先物が97ドル台から101ドル台後半へ上昇してドル買いが戻り、158.34円まで反発した後に158.02円で引けた（みんかぶ・ザイFX）。'
    '植田日銀総裁がタイでの会見で追加利上げへの前向きな姿勢を示したことも円買い材料となった（みんかぶ）。'
    '週明けのオセアニア市場ではフランスの暴動を嫌気したユーロ売りが先行し、ユーロドルは先週末の引け値1.1239ドル付近から1.1183ドルまで下落した（ザイFX）。'
    '本日は香港が祝日で休場（KissFX。中国本土は同日にGDPなどの発表予定があり休場かどうか要確認）。米国の経済指標で注目度の高いものはない（KissFX・ForexFactory一致）。'
)

TOP_PAIR_BODY = (
    'ドル円は10/16に157.70〜158.34円で推移し、週明けの東京朝は157.91〜158.10円のもみ合い（ザイFX）。'
    '上値は為替介入への警戒で159円手前が抑えられ、10/16朝の安値圏157.7円台が下値の目安となる。米債利回り（10年債5.07％前後）が下がればドル売り、原油（WTI 101ドル台後半）が上がればドル買いに動く構図が先週から続く。'
    '4時間足ランキング（10/19 06:38 JST生成）ではUSD/JPYは11位・見送り判定（スコア25、方向はレンジ）で、本日の優先対象はEUR/AUDとAUD/JPYとなる。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'NY原油先物が101ドル台後半、ブレント原油が5月以来の110ドル台に乗せ、中東情勢を背景にインフレ再燃とドル高・円安の両方向の振れを生んでいる。'
    '加えて週末にフランスのデモが暴徒化してユーロが急落し、10/28のFOMC・10/29のECB・10/30の日銀会合を控える（みんかぶ・KissFX）。'
)

KEY_EVENTS_COUNT = '3件'
KEY_EVENTS_SUMMARY = (
    '中 第3四半期GDP(11:00) / 加 消費者物価指数(21:30) / 米 NAHB住宅市場指数(23:00)。米国の注目度の高い指標なし'
)

MARKET_OVERVIEW = (
    '先週末のNY市場で米10年債利回りは5.1313％まで上昇した後に5.07％前後へ低下した（みんかぶ）。ドル指数は一時103の節目に迫った後、10日線を下抜けて21日線に達する調整となった（みんかぶ）。'
    'NY原油先物は97ドル台から101ドル台後半へ上昇し、ブレント原油は5月以来の110ドル台を付けた。COMEX金12月限は4,189.12ドル（+19.02ドル、+0.46％）で、10月FOMCでの追加利上げ観測の後退が買い材料になった（ザイFX）。'
    'NYダウは52,002.41ドル（-175.28ドル、-0.34％）で引けた。週明け朝のCME円建て日経225先物は10/16の大阪取引所比1,595円安の63,925円で推移している（ザイFX）。'
    'VIX・米2年債利回り・ドル指数の数値はInvesting.comが取得不可（403）のため未確認（要確認）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％（主要リファイナンス金利2.65％）、BOE 3.75％、RBA 4.60％、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（ザイFXの政策金利推移（10/13更新）で全8中銀を確認。KissFXの会合日程で9月以降の変更がないことを照合）。'
    '<br><br><strong>今週の焦点：</strong> 10/20に英雇用統計、10/21に英CPI（米ではメタ・テスラの決算）、10/22にNZ第3四半期CPI、10/23に日本全国CPIと主要国の製造業・非製造業PMI（速報値）。FRB高官は10/28のFOMCに向けた発言禁止期間に入る。次回の主要中銀は10/28（FRB・BOC・RBNZ）、10/29（ECB）、10/30（日銀）。'
)

RANKING_ROWS = [
    (1, 'EUR/AUD', 'rank-a', 'A', '直近スコア66・適。ADX36.6、ADR比81.8％、方向は上昇。週明けにフランスのデモ暴徒化でユーロが売られた一方、豪ドルは4H足で売りが優勢（AUD/JPY・AUD/USDが下降）で、ユーロ売り・豪ドル売りの強弱が焦点。', 'trend-up', '↑'),
    (2, 'AUD/JPY', 'rank-b', 'B', '直近スコア61・候補。ADX28.5、ADR比85.8％、方向は下降。中国GDP(11:00)の結果が豪ドルの方向を決める。', 'trend-down', '↓'),
    (3, 'USD/CAD', 'rank-c', 'C', '直近スコア60・候補。ADX20.3、ADR比100.8％、方向は下降。21:30のカナダCPI（予想 前月比+0.2％・前年比+3.2％）で動きやすい。', 'trend-down', '↓'),
    (4, 'AUD/USD', 'rank-c', 'C', '直近スコア58・候補。ADX22.3、ADR比93.6％、方向は下降。', 'trend-down', '↓'),
    (5, 'GBP/USD', 'rank-c', 'C', '直近スコア55・候補。ADX19.5、ADR比92.6％、方向は上昇。BOEの11月利上げ観測で10/16に1.3372ドルまで上昇した。', 'trend-up', '↑'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/10/19 06:38 JST生成分（本日分取得済み）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'ドル円は米債利回り低下と原油高に挟まれ157円70銭〜158円34銭、終値158円02銭',
        '10/16のNY市場でドル円は、米債利回りの低下を背景にしたドル売りで東京午後の安値を割り込み157.70円を付けた。植田日銀総裁がタイでの会見で追加利上げへの前向きな姿勢を示したことも円買いにつながった（みんかぶ）。'
        'その後、中東情勢を受けてNY原油先物が97ドル台から101ドル台後半へ上昇し、ブレント原油も5月以来の110ドル台を付けたことでドル高が広がり158.34円まで反発。週末のポジション調整で158.00円前後に戻り、NY終値は158.02円と前営業日（158.00円）から2銭のドル高だった（ザイFX）。',
    ),
    (
        'ウォーシュFRB議長が政策の方向性に言及せず、ユーロドル・ポンドドルが上昇後に反落',
        'ウォーシュ米FRB議長が政策の方向性に言及しなかったことで米国の早期利上げ期待が後退し、ドル売りが進んだ（みんかぶ）。'
        'ユーロドルは1.1210ドルから1.1270ドル前後まで上昇した後、原油高によるドル高で1.1210ドル台へ押し戻され、引けは1.1240ドル前後。ポンドドルは11月の追加利上げ期待からユーロ以上に買われ、NY午前に1.3372ドルを付けた後、1.3310ドル前後まで下げて1.3330ドル前後で引けた。'
        'ユーロ円は177.90円台、ポンド円は211.00円近くまで上昇した後、対ドルでの売りに押されて177.40円前後、210.30円台へ戻した。',
    ),
    (
        '米債利回りは5.13％から5.07％へ低下、金は続伸',
        '米10年債利回りはNY朝に5.1313％まで上昇した後、ハイテク株中心の株安もあって5.0645％まで低下し、5.07％前後で週末を迎えた（みんかぶ）。'
        'COMEX金12月限は4,189.12ドル（+19.02ドル）と続伸し、10月FOMCでの追加利上げ観測の後退が買い材料になった。NYダウは52,002.41ドル（-175.28ドル）で引けた（ザイFX）。',
    ),
    (
        '週明け早朝はフランスの暴動を嫌気してユーロが急落',
        '週末のフランスでのデモが暴徒化し、ユーロドルは先週末の引け値1.1239ドル付近から1.1183ドルまで下落、ユーロ円も177円半ばから176.74円まで下げた（ザイFX）。'
        'みんかぶはトランプ米大統領が移民を非難し国境閉鎖を呼びかけたと伝えている。ユーロはその後1.1220ドル台に戻したが、フランス国債への懸念（KissFX）が上値を抑える構図が続く。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/19月）への引継ぎ：ドル円は158.02円、ユーロドルは1.1239ドル（週明けに1.1183ドルまで下落）、WTI原油は101ドル台後半、米10年債利回りは5.07％前後で週末を終えた。'
    '本日は米国の注目指標がなく、米長期金利・原油・米株の動きがドル円の方向を決める。'
    '来週に日銀（10/30）とFOMC（10/28）を控え、為替介入への警戒が159円手前の上値を抑える。'
)

POINTS_EVENTS = [
    '06:45 🇳🇿 NZ 貿易収支（Kiss/FF一致。前回-13.49億NZドル）',
    '08:05 🇦🇺 豪 ケントRBA副総裁補 発言（FFのみ・要確認）',
    '11:00 🇨🇳 中国 第3四半期GDP（Kiss/FF一致。予想 前年比+4.4％）、小売売上高、鉱工業生産、固定資産投資',
    '13:30 🇯🇵 日本 第三次産業活動指数（Kiss/FF一致。予想は-0.4％（Kiss）と-0.3％（FF）で不一致・要確認）',
    '21:30 🇨🇦 カナダ 消費者物価指数（Kiss/FF一致。予想 前月比+0.2％。ForexFactory重要度High）',
    '23:00 🇺🇸 米国 NAHB住宅市場指数（Kiss/FF一致。予想31）',
    '※ 米国で注目度の高い経済指標の発表はなし（KissFX）。',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：金利と原油の綱引きで158円前後、為替介入警戒が上値を抑える',
        'ドル円は10/16に157.70〜158.34円で推移し、朝は157.91〜158.10円のもみ合い（ザイFX）。米債利回りが低下すればドル売り、原油が上昇すればドル買いが強まる関係が先週から続き、159円手前では日米当局者の円安牽制が意識される（みんかぶ）。'
        'みんかぶによると、短期金利市場は10月の日銀会合での利上げ織り込みが約4％にとどまる一方、12月までの追加利上げを約80％織り込んでいる。次回の日銀会合は10/30、FOMCは10/28。',
    ),
    (
        'ユーロ：フランスの政情不安とフランス国債への懸念でユーロ売り',
        '週末のフランスの暴動を受け、ユーロドルは1.1183ドル、ユーロ円は176.74円まで下落した（ザイFX）。KissFXはフランス国債への懸念を本日の注目材料に挙げている。仏債利回りが上昇すればユーロ売りが強まり、次回のECB発表は10/29。',
    ),
    (
        '原油：ブレントが5月以来の110ドル台、中東情勢が為替のリスク要因',
        'NY原油先物は97ドル台から101ドル台後半へ上昇し、ブレントは5月以来の110ドル台を付けた（みんかぶ）。原油高は米インフレ懸念を通じて米長期金利を押し上げ、ドル高の材料になる。KissFXはイラン情勢と商品市場の動向を本日の重要項目に挙げている。',
    ),
    (
        '休場：香港が休場（中国は要確認）',
        'KissFXは本日10/19を香港と中国の祝日としている。一方、ForexFactory・みんかぶ・ザイFXは中国のGDP・小売売上高・鉱工業生産を本日11:00に発表予定としており、中国本土の休場は2ソースで裏付けられていない（要確認）。香港市場の休場で流動性が薄く、アジア時間は値が飛びやすい。',
    ),
    (
        '今週のイベント：英雇用統計・英CPI・日本CPI・PMIと米主要企業決算',
        'KissFXによると、10/20に英雇用統計と米ネットフリックスの決算、10/21に英CPIと米メタ・テスラの決算、10/22にNZ第3四半期CPI、10/23に日本全国CPIと主要国の製造業・非製造業PMI（速報値）が発表される。'
        'FRB高官は発言禁止期間に入り、10/28のFOMCまで要人発言による方向付けはなく、米長期金利と株価が材料になる。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('06:30', '🇳🇿 NZ', 'ビジネスNZサービス業指数（FFのみ・要確認）', '低', '—', '51.2'),
    ('06:45', '🇳🇿 NZ', '貿易収支（Kiss/FF一致）', '低', '-7.75億NZドル（FF）', '-13.49億NZドル'),
    ('08:01', '🇬🇧 英', 'ライトムーブ住宅価格 前月比（Kiss/FF一致）', '低', '—', '+0.7%'),
    ('08:05', '🇦🇺 豪', 'ケントRBA副総裁補 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('10:30', '🇨🇳 中', '新築住宅価格 前月比（FF・みんかぶ・ザイFX一致）', '低', '—', '-0.17%'),
    ('11:00', '🇨🇳 中', '第3四半期GDP 前年比（Kiss/FF一致）／前期比+0.9％（Kiss）', '低', '+4.4%', '+4.3%'),
    ('11:00', '🇨🇳 中', '小売売上高 前年比（Kiss/FF一致）', '低', '+0.5%', '+0.4%'),
    ('11:00', '🇨🇳 中', '鉱工業生産 前年比（Kiss/FF一致。予想はKiss+5.5％・FF+5.4％で不一致・要確認）', '低', '+5.5%(Kiss)', '+5.2%'),
    ('11:00', '🇨🇳 中', '固定資産投資 年初来前年比（Kiss/FF一致）', '低', '-7.3%', '-7.2%'),
    ('11:00', '🇨🇳 中', '失業率（FFのみ・要確認）／NBS記者会見（FFのみ・要確認）', '低', '5.3%', '5.3%'),
    ('13:30', '🇯🇵 日', '第三次産業活動指数 前月比（Kiss/FF一致。予想は-0.4％（Kiss）・-0.3％（FF）で不一致・要確認）', '低', '-0.4%(Kiss)', '+0.4%'),
    ('15:02', '🇨🇳 中', '対内直接投資 年初来前年比（FFのみ・要確認）', '低', '—', '-5.3%'),
    ('21:30', '🇨🇦 加', '消費者物価指数 前月比（Kiss/FF一致）', '高', '+0.2%', '-0.1%'),
    ('21:30', '🇨🇦 加', '消費者物価指数 前年比（Kissのみ・要確認）', '高', '+3.2%', '+3.0%'),
    ('21:30', '🇨🇦 加', 'CPI中央値・トリム平均・コモン 前年比（FFのみ・要確認）', '高', '2.0% / 1.9% / 2.6%', '2.0% / 1.9% / 2.6%'),
    ('23:00', '🇺🇸 米', 'NAHB住宅市場指数（Kiss/FF一致）', '低', '31', '32'),
    ('24:30', '🇨🇦 加', 'BOC企業景況感調査（翌00:30。FFのみ・要確認）', '低', '—', '—'),
]
CAL_ROWS.sort(key=lambda r: (int(r[0][:2]), r[0]))

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

FUNDAMENTALS_ROWS = [
    ('FRB', '🇺🇸 USD', '3.75–4.00%', 'var(--red)', 'タカ派',
     '9/16のFOMCで0.25%利上げ（全会一致）し、上限4.00％。10/16はウォーシュ議長が政策の方向性に言及せず、10月FOMCでの追加利上げ観測が後退した（みんかぶ・ザイFX）。'
     '今週発表の米CPI・PPIはインフレの粘着性を示した。FRB高官は10/19から発言禁止期間に入り、次回FOMCは10/27-28。ザイFXの政策金利推移（10/13更新）で上限4.00％を確認。'),
    ('日銀', '🇯🇵 JPY', '1.25%', 'var(--blue)', 'タカ派',
     '9/18会合で0.25%利上げ。10/16に植田総裁がタイでの会見で追加利上げへの前向きな姿勢を示し、「基調物価が2%からこれ以上上がることは容認できない」とも発言した（みんかぶ）。'
     'ただし同日には「日銀は今月会合で利上げ見送る公算大」と報じられ、10月会合の利上げ織り込みは約4％、12月までの追加利上げは約80％（みんかぶ）。10/23の全国CPI（コア予想+2.1％）が材料で、次回会合は10/29-30。ザイFXで1.25％を確認。'),
    ('ECB', '🇪🇺 EUR', '2.50%', 'var(--red)', 'タカ派',
     '9/10理事会で預金ファシリティ金利を0.25%引き上げて2.50%（主要リファイナンス金利2.65%。ザイFXの推移表で2.65％を確認）。'
     '週明けはフランスのデモ暴徒化でユーロが1.1183ドルまで下落し、フランス国債への懸念（KissFX）がユーロの重しになっている。次回理事会は10/29。'),
    ('BOE', '🇬🇧 GBP', '3.75%', 'var(--muted)', '中立〜タカ派寄り',
     '9/17のMPCで6対3の分裂投票により据え置き。みんかぶは「英中銀11月利上げはほぼ織り込み済み」と伝え、10/16にはポンドが11月の追加利上げ期待で1.3372ドルまで上昇した。'
     '10/20に雇用統計（15:00）、10/21にCPIが発表される。次回会合は11/5。ザイFXで3.75％を確認。'),
    ('RBA', '🇦🇺 AUD', '4.60%', 'var(--red)', 'タカ派（総裁会見でハト派化）',
     '9/29に政策金利を4.35%から4.60%へ0.25%引き上げ。ブロック総裁の会見で据え置きも検討していたことが判明し、ハト派と受け止められた。'
     '本日08:05にケントRBA副総裁補が発言予定（FFのみ・要確認）。次回会合は11/3。ザイFXで4.60％を確認。'),
    ('RBNZ', '🇳🇿 NZD', '2.75%', 'var(--red)', 'タカ派',
     '9/2の金融政策委員会で0.25%利上げし、2.25%→2.50%（7/8）→2.75%（9/2）と3会合連続の利上げ。'
     '10/22のNZ第3四半期CPIは2期連続で4％台に乗せる見通しで、中銀目標範囲を大きく上回る（みんかぶ）。次回会合は10/28。ザイFXで2.75％を確認。'),
    ('BOC', '🇨🇦 CAD', '2.25%', 'var(--muted)', '中立',
     '9/2会合で据え置き（7会合連続）。10/9の9月雇用統計は予想外の雇用減となった。本日21:30にCPI（予想 前月比+0.2％、前年比+3.2％はKissのみ・要確認）が発表され、次回会合は10/28。ザイFXで2.25％を確認。'),
    ('SNB', '🇨🇭 CHF', '0.00%', 'var(--muted)', 'ハト派〜中立',
     '9/24会合を経て政策金利は0.00%を維持。ザイFXの西原宏一氏は9/29のコラムでSNBが事実上「フラン安容認」と評している。ザイFXで0.00％を確認。次回会合は12/10（Investing.comのみ・要確認）。'),
]

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

fundamentals_rows_html = ''
for bank, currency, rate, color, stance, reason in FUNDAMENTALS_ROWS:
    fundamentals_rows_html += f'''            <tr>
              <td>{bank}</td><td>{currency}</td><td><strong>{rate}</strong></td>
              <td style="color:{color};">{stance}</td>
              <td style="font-size:12px;">{reason}</td>
            </tr>
'''

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
        <em>月曜日</em>
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
              <li>🇭🇰 香港市場休場（KissFXの休場日一覧に記載）</li>
              <li>🇨🇳 中国は要確認（KissFXは休場とするが、中国GDPなどは本日11:00に発表予定でForexFactory・みんかぶ・ザイFXと不一致）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-10-16 金）</h3>
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

      <div class="panel full" id="fundamentals">
        <div class="panel-head">
          <h3>🏦 主要中銀ファンダメンタルズ（週次更新）</h3>
          <span>{TODAY} 現在</span>
        </div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>政策金利</th><th>スタンス</th><th>背景・理由</th></tr></thead>
          <tbody>
{fundamentals_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。ザイFXの政策金利推移（10/13更新）・みんかぶ・KissFX（羊飼い）の報道で照合。前回更新（10/12）から政策金利の変更はなし（各中銀の次回会合は10/28以降）。最新情報は各中銀の公式サイトでご確認ください。</p>
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
