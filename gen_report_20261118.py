# -*- coding: utf-8 -*-
"""FX日報 2026-11-18（水）生成スクリプト"""
import glob, os

TODAY = '2026-11-18'
WEEKDAY = '水'

HERO_TITLE_SUB = (
    '前日11/17（火）は米小売売上高の上振れでユーロドルが1.0968ドルと1年7か月ぶりの安値をつけた。その後、米NSAの通信障害報道と株安で米国債が買われ、ドル売りに転じた。'
    'ドル円は159.12円まで下げて引けた。本日11/18（水）は16:00の英CPIと、28:00（19日04:00）のFOMC議事要旨が中心材料。'
)

SUMMARY_HEADLINE = (
    '強い米指標でドル高、その後の株安で米国債が買われドル安と、1日で流れが逆転した。'
    '本日は英CPIでポンドが動き、深夜のFOMC議事要旨でドル全体の方向が決まる'
)

SUMMARY_BODY = (
    '11/17（火）NYのドル円は159.47円まで上げた後、159.12円まで下げて引けた（ザイFX/フィスコ）。'
    '米10月小売売上高は前月比+0.2%（予想+0.1%）、コントロールグループは+0.6%（予想+0.3%）と上振れ（みんかぶ・ザイFX/フィスコ一致）。'
    'その後、米10月鉱工業生産-0.4%（予想+0.1%）、11月NAHB住宅市場指数25（予想29、14年ぶり低水準）と弱い指標が続いた（ザイFX/フィスコ）。'
    'NSAの通信障害報道でダウは一時900ドル超下落、米10年債利回りは5.08%台へ低下（ザイFX/DZH）。本日11/18（水）の主要市場休場はなし。'
)

TOP_PAIR_BODY = (
    'ドル円は11/17の東京朝に159.61円をつけた後、東京午後に159.07円、ロンドンで158.87円まで下落（ザイFX/DZH・フィスコ）。'
    '下げた理由は、アジア株・欧州株の下落によるリスク回避の円買い（みんかぶ・ザイFX/フィスコ）。'
    '158.87円では200日移動平均線158.78円と一目均衡表の転換線158.73円が支えになり、米小売売上高の上振れで159.47円まで戻した（ザイFX/DZH）。'
    'NYでは株安で米長期金利が下がり、159.12円まで押し戻されて引けた（ザイFX/フィスコ）。'
    '4時間足は上昇トレンドだが高値は切り下がっている。15分・30分足では158.73〜158.87円が下の節目、159.61円（11/17高値）が上の節目。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'ダウは午後2時台で50,828.15ドル（-780.02、-1.51%）、ナスダック-1.09%、S&amp;P500-1.13%（ザイFX/フィスコ）。'
    '原因は米NSAの機密通信ネットワークの障害報道（CNN報道。サイバー攻撃の証拠は現時点で確認されていない、みんかぶ）。'
    'マイクロソフト、米連邦航空局（FAA）、銀行に続くシステム不具合でリスク回避が強まった（ザイFX/フィスコ）。'
    '米国がイランのゲシム（ケシム）島を攻撃したとイランが発表し（みんかぶ・ザイFX/フィスコ）、原油は反発。エヌビディア決算の内容は本日の取得ソースで未確認（要確認）。'
)

KEY_EVENTS_COUNT = '12件'
KEY_EVENTS_SUMMARY = (
    '豪 賃金コスト指数(09:30)、日 20年国債入札(12:35)、英 CPI・PPI(16:00)、英 ベイリーBOE総裁(16:30・24:00)、欧 CPI改定値(19:00)、'
    '米 住宅着工(22:30)、欧 ラガルドECB総裁(23:25)、米 中古住宅販売保留(24:00)、NZ ブレマンRBNZ総裁(27:00)、米 FOMC議事要旨(28:00)、米 ウィリアムズ総裁(28:30)'
)

MARKET_OVERVIEW = (
    '<strong>米株（11/17、NY午後2時台）</strong>：ダウ50,828.15ドル（-780.02、-1.51%）、ナスダック24,243.48（-1.09%）、S&amp;P500 7,332.73（-1.13%）、SOX指数-0.90%（ザイFX/フィスコ）。'
    'ダウは一時900ドル超下落（ザイFX/DZH）。欧州株も続落し、独DAXは-553.27の26,045.37（ザイFX/DZH）。日経平均は801.59円安の58,860.43円（ザイFX/フィスコ）。'
    '<strong>米債利回り</strong>：2年債4.79%（-0.04）、10年債5.10%（-0.03）、30年債5.46%（-0.01）、日米金利差2.22%（ザイFX/フィスコ午後2時台）。10年債は一時5.08%と12日以来の低水準（ザイFX/フィスコ）。'
    '<strong>ドルインデックス</strong>：103.44（-0.11、ザイFX/フィスコ午後2時台）。'
    '<strong>金</strong>：NY金先物3,858.20ドル（+5.20、+0.13%）（ザイFX/フィスコ）。'
    '<strong>原油</strong>：WTI先物86.61ドル（+0.89、+1.04%）（ザイFX/フィスコ）。米国によるイランのケシム島攻撃で供給ひっ迫懸念が再燃し反発（ザイFX/フィスコ）。'
    '<strong>VIX</strong>：水曜日のため本日は未取得（Step 4は月曜のみ）。'
    '<br><br><strong>政策金利（11/16確認分を継続）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。'
    '<br><br><strong>今週の焦点：</strong> 18日 英CPI・FOMC議事要旨（10/27-28会合分）・アンソロピックのIPO価格（みんかぶ）、19日 米中ロ3か国首脳会談（深セン、KissFX・みんかぶ）、20日 日本CPI（KissFX）。'
    '英短期金融市場は12月の英中銀利上げを93%織り込む（みんかぶ）。'
)

RANKING_ROWS = [
    (1, 'USD/CHF', 'rank-a', 'A', 'スコア77・適。ADX45.1、ADR比101％（5日ADR 59.7pips）、4H方向は上昇。ただし11/17のNYは株安で安全通貨のフラン買いが強まり、0.8415フランから0.8380フランまで下落（ザイFX/フィスコ）。4H上昇の押し目か、トレンド転換かを15分足で確認する局面。', 'trend-up', '↑'),
    (2, 'EUR/USD', 'rank-a', 'A', 'スコア75・適。ADX42.0、ADR比93％、方向は下降。11/17は米小売売上高後に1.0968ドルと2025年4月以来の安値をつけた後、米金利低下で1.1024ドルまで反発（ザイFX/DZH・フィスコ）。ストラテジストは「今週ユーロが一段安となる強い材料は見当たらない」と指摘（みんかぶ）。19:00のユーロ圏CPI改定値と23:25のラガルド総裁が材料。', 'trend-down', '↓'),
    (3, 'USD/CAD', 'rank-a', 'A', 'スコア72・適。ADX45.1、ADR比91％、方向は上昇。11/17のカナダ10月住宅着工件数は24.46万件（予想24.00万件）と上振れ（みんかぶ）。原油は1%高で反発しており、カナダドルの支え。22:30に新築住宅価格指数（FFのみ）。', 'trend-up', '↑'),
    (4, 'GBP/USD', 'rank-b', 'B', 'スコア71・適。ADX52.8、ADR比88％、方向は下降。11/17は1.3173ドルまで下げた後、1.3228ドルまで反発（ザイFX/フィスコ）。英10月失業率は4.5%（前回4.4%）に上昇（ザイFX/DZH）。一方、市場は12月の英利上げを93%織り込む（みんかぶ）。16:00の英CPIが最大の材料。', 'trend-down', '↓'),
    (5, 'AUD/USD', 'rank-b', 'B', 'スコア70・適。ADX58.6、ADR比87％、方向は下降。09:30の第3四半期賃金コスト指数は前期比 予想+1.0%（前回+0.8%）（KissFX・FF一致）。上振れならRBAの追加利上げ観測（11/3に4.85%へ利上げ済み）を支える。株安が続けば豪ドルの重し。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/11/17 11:33 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、前日の数値。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        '米小売売上高は上振れ、ユーロドルは1.0968ドルと1年7か月ぶりの安値',
        '米10月小売売上高は前月比+0.2%（予想+0.1%）、除自動車+0.6%（予想+0.4%）、コントロールグループ+0.6%（予想+0.3%）（みんかぶ）。輸入物価指数も前月比+1.1%（予想+0.7%）と上振れ（みんかぶ・ザイFX/フィスコ一致）。'
        '個人消費の強さとインフレ圧力が確認され、米長期金利の上昇でドル買いが先行（ザイFX/フィスコ）。'
        'ユーロドルは22:30過ぎに1.0968ドルと昨年4月以来の安値を更新、ドル円は159.47円まで戻した（ザイFX/DZH）。'
        'ムサレム・セントルイス連銀総裁は「2027年春までに実質政策金利をあと約1%引き上げる必要」「今後数か月で複数回の利上げを支持」と述べた（みんかぶ・ザイFX/フィスコ一致）。',
    ),
    (
        '米NSAの通信障害報道でリスク回避、米国債買いでドルは反落',
        '「米国家安全保障局（NSA）の機密通信ネットワークが大規模な障害に見舞われている」との報道（CNN）で、ダウは一時900ドル超下落（ザイFX/DZH・みんかぶ）。サイバー攻撃を示す証拠は現時点で確認されていない（みんかぶ）。'
        'マイクロソフト、FAA、銀行に続くシステム不具合で、安全資産の米国債が買われた。米10年債利回りは5.15%から5.08%台へ低下（ザイFX/フィスコ・DZH）。'
        '米金利低下でドル売りに転じ、ユーロドルは1.1024ドル、ポンドドルは1.3228ドルまで反発。ドル円は159.12円まで下げて引けた（ザイFX/フィスコ）。'
        '安全通貨としてのフラン買いも強く、ドル・スイスは0.8415フランから0.8380フランへ下落（ザイFX/フィスコ）。',
    ),
    (
        '弱い米指標が続く：鉱工業生産-0.4%、NAHB住宅市場指数は14年ぶり低水準',
        '米10月鉱工業生産は前月比-0.4%（予想+0.1%、前回+0.7%）、設備稼働率は76.4%（予想76.8%）と下振れ（ザイFX/フィスコ・みんかぶ一致）。発表直後にドルは高値から反落（ザイFX/フィスコ）。'
        '米11月NAHB住宅市場指数は25（予想29、前回29）と予想外に低下し、14年ぶりの低水準（ザイFX/フィスコ）。高い住宅ローン金利が住宅市場を圧迫している。'
        'みんかぶは「力強い米経済と底堅い消費はFRBの追加利上げ観測を支えるが、株安が進んで金融環境が引き締まれば、市場は利上げ見通しを後退させる」との見方を伝えた。',
    ),
    (
        'ドル円は東京・ロンドンで158.87円まで下落、200日線で下げ止まる',
        '東京朝に159.61円をつけた後、原油安とアジア株の下落でドル安円高に転じ、午後に159.07円（11日以来の円高水準）まで下げた（みんかぶ・ザイFX/フィスコ）。日経平均は801.59円安（ザイFX/フィスコ）。'
        'ロンドンでは欧州株の続落でリスク回避の円買いが進み、18:30過ぎに158.87円（ザイFX/DZH）。'
        '200日移動平均線158.78円、一目均衡表の転換線158.73円がサポートとして意識され、買い戻された（ザイFX/DZH）。'
        '通貨オプション市場では、1か月物・3か月物でドル・円の下値ヘッジの円コール買いが優勢（ザイFX/フィスコ）。',
    ),
    (
        'ポンドは英雇用統計で失業率が上昇も、英利上げ観測は93%',
        '英10月失業率は4.5%（前回4.4%）、失業保険申請件数は3.32万件（前回0.98万件）と雇用は悪化（ザイFX/DZH）。7-9月のILO失業率は4.6%（前回4.7%）。'
        '一方、9月の英月次GDPは前月比+0.2%とマイナス予想を上回っており、エコノミストは英中銀が追加利上げに踏み切る環境が整いつつあると指摘（みんかぶ）。短期金融市場は12月の利上げを93%織り込む（みんかぶ）。'
        'ポンドドルはロンドンで1.31ドル台に下げた後、NYで1.32ドル台前半に戻し、ポンド円も209円台から210円台に戻した（みんかぶ）。'
        '独11月ZEW景況感指数は35.6（予想28.2、前回28.1）と大幅に上振れ（ザイFX/DZH・フィスコ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/18水）への引継ぎ：ドル円は159.12円、ユーロドルは1.1024ドル付近で引けた（ザイFX/フィスコ）。ドル高の地合いは株安と米金利低下で一服した。'
    '16:00の英10月CPIは前年比 予想+3.6%（前回+3.5%）、コア 予想+2.8%（前回+2.8%）（KissFX・FF一致。フィスコの予想は3.5%）。上振れなら12月利上げ観測がさらに強まりポンド買い、下振れならポンド売り。'
    'ベイリーBOE総裁は16:30と24:00に発言。28:00（19日04:00）のFOMC議事要旨（10/27-28会合分、10対2で据え置き・利上げ主張2名）で、追加利上げを支持する委員の多さがドルを動かす。'
    'KissFXは「米ドル・日本円・ユーロの方向性、米長期金利、為替介入への警戒、AI投資への不安、イラン情勢」を焦点に挙げる。19日は米中ロ首脳会談。'
)

POINTS_EVENTS = [
    '09:30 🇦🇺 豪 第3四半期賃金コスト指数 前期比 予想+1.0%（Kiss/FF一致・Kiss○）',
    '12:35 🇯🇵 日 20年利付国債入札（KissFXのみ・要確認・Kiss◎）',
    '16:00 🇬🇧 英 消費者物価指数 前年比 予想+3.6%／コア 予想+2.8%（Kiss/FF一致・Kiss◎・FF区分:高）',
    '16:00 🇬🇧 英 生産者物価指数・小売物価指数（Kiss/FF一致・Kiss○）',
    '16:30 🇬🇧 英 ベイリーBOE総裁の発言（Kiss/FF一致・Kiss◎）',
    '19:00 🇪🇺 欧 消費者物価指数【改定値】 前年比 予想+4.0%（Kiss/FF一致・Kiss△）',
    '22:30 🇺🇸 米 住宅着工件数 予想125.0万件／建設許可件数 予想137.5万件（Kiss/FF一致・KissランクA）',
    '23:25 🇪🇺 欧 ラガルドECB総裁の発言（Kiss/FF一致・Kiss◎）',
    '24:00 🇬🇧 英 ベイリーBOE総裁の発言（Kiss/FF一致・Kiss◎・FF区分:高）',
    '24:00 🇺🇸 米 中古住宅販売保留 前月比 予想-2.1%（Kiss）／-2.0%（FF）で不一致・要確認（KissランクA）',
    '27:00 🇳🇿 NZ ブレマンRBNZ総裁の発言（Kiss/FF一致・Kiss◎）',
    '28:00 🇺🇸 米 FOMC議事要旨（10/27-28会合分）（Kiss/FF一致・KissランクSS・FF区分:高）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：200日線158.78円と159.61円',
        '4時間足は上昇トレンドだが、11/12・11/13の160円台から高値を切り下げている（ザイFX・みんかぶ）。11/17は158.87円で200日線（158.78円）と転換線（158.73円）に支えられた（ザイFX/DZH）。'
        '15分・30分足では158.73〜158.87円を割ると下げが広がりやすく、守れば押し目買いの水準。上は159.61円（11/17東京高値）。FOMC議事要旨が利上げ寄りなら日米金利差でドル買い、ただし160円手前は介入警戒で上値が重い。',
    ),
    (
        'ポンド：16:00の英CPI',
        '市場は12月の英利上げを93%織り込む（みんかぶ）。織り込みが進んでいる分、CPIが予想を下回るとポンド売りの反応が大きくなりやすい。ポンドドルは4H下降トレンド（ランキング4位）。11/17安値1.3173ドルと高値1.3228ドル（ザイFX/フィスコ）が15分足の節目。',
    ),
    (
        'ユーロドル：1.10ドルの攻防',
        '11/17は1.0968ドルまで下げた後、1.1024ドルまで戻した（ザイFX/フィスコ）。1.10ドル割れで押し目買いが入っている（みんかぶ）。4H下降トレンドの戻りは1.1030ドル前後（11/16・11/17のNY高値）が売り場の目安。23:25のラガルド総裁発言が材料。',
    ),
    (
        'リスク回避：NSA障害・イラン・AI株',
        'NSAの通信障害の続報、米国とイランの攻撃応酬（ゲシム島攻撃、みんかぶ）、エヌビディア決算後のAI関連株の動き（決算内容は要確認）が株価を通じてクロス円を動かす。株安が続けば円買い・フラン買い。',
    ),
    (
        '市場休場：なし',
        '本日11/18（水）は主要市場の休場なし（KissFXの主要国休場日一覧・ForexFactory JSONで一致）。次の休場は11/23日本、11/26米国（KissFX）。APEC首脳会議（深セン、18〜19日）は継続中（KissFX・フィスコ）。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('00:00', '🇺🇸 米', '【発表済み】企業在庫 前月比（前日24:00分）結果+0.5%', 'C', '+0.5%', '+0.4%'),
    ('00:00', '🇺🇸 米', '【発表済み】NAHB住宅市場指数（前日24:00分）結果25', 'C', '29', '29'),
    ('04:25', '🇺🇸 米', '【発表済み】ウィリアムズNY連銀総裁 発言（前日28:25分・Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('06:30', '🇺🇸 米', '【発表済み】API週間石油在庫（FFのみ・要確認）', '（FF低）', '—', '—'),
    ('06:45', '🇳🇿 NZ', '【発表済み】第3四半期 生産者物価指数 産出 前期比（Kiss/FF一致）', '○', '+1.1%（FF）', '+1.6%'),
    ('06:45', '🇳🇿 NZ', '【発表済み】第3四半期 生産者物価指数 投入 前期比（FFのみ・要確認）', '（FF低）', '+1.5%', '+2.9%'),
    ('08:30', '🇦🇺 豪', 'ウエストパック景気先行指数（Kiss/FF一致）', '△', '—', '-0.06%'),
    ('08:50', '🇯🇵 日', '貿易収支（Kiss/FF/フィスコ。予想・前回の値が不一致・要確認）', '×', '-1兆784億（Kiss）／-0.90兆（FF）／-1兆195億（フィスコ）', '-5366億（Kiss・フィスコ）／-0.70兆（FF）'),
    ('08:50', '🇯🇵 日', '輸出 前年比（フィスコのみ・要確認）', '—', '+20.4%', '+16.7%'),
    ('08:50', '🇯🇵 日', '輸入 前年比（フィスコのみ・要確認）', '—', '+25.7%', '+18.9%'),
    ('09:30', '🇦🇺 豪', '第3四半期 賃金コスト指数 前期比（Kiss/FF一致）', '○', '+1.0%', '+0.8%'),
    ('09:30', '🇦🇺 豪', '第3四半期 賃金コスト指数 前年比（KissFXのみ・要確認）', '○', '+3.4%', '+3.2%'),
    ('11:45', '🇩🇪 独', 'ナーゲル独連銀総裁 発言（Kiss/FF一致）', '△', '要人発言', '—'),
    ('12:35', '🇯🇵 日', '20年利付国債入札（KissFXのみ・要確認）', '◎', '—', '—'),
    ('16:00', '🇬🇧 英', '消費者物価指数 前年比（Kiss/FF一致・フィスコ予想3.5%）', '◎', '+3.6%', '+3.5%'),
    ('16:00', '🇬🇧 英', '消費者物価指数 前月比（KissFXのみ・要確認）', '◎', '+0.5%', '+0.4%'),
    ('16:00', '🇬🇧 英', '消費者物価指数 コア 前年比（Kiss/FF一致）', '◎', '+2.8%', '+2.8%'),
    ('16:00', '🇬🇧 英', '生産者物価指数 産出 前月比（Kiss/FF一致・前回はKiss +0.7%、FF 0.8%で不一致・要確認）', '○', '+0.6%', '+0.7%（FF 0.8%）'),
    ('16:00', '🇬🇧 英', '生産者物価指数 産出 前年比（KissFXのみ・要確認）', '○', '+5.1%', '+4.6%'),
    ('16:00', '🇬🇧 英', '生産者物価指数 投入 前月比（FFのみ・要確認）', '（FF低）', '+0.8%', '+1.5%'),
    ('16:00', '🇬🇧 英', '小売物価指数 前年比（Kiss/FF一致）', '○', '+4.1%', '+3.9%'),
    ('16:00', '🇬🇧 英', '小売物価指数 前月比（KissFXのみ・要確認）', '○', '+0.5%', '+0.1%'),
    ('16:02', '🇨🇳 中', '海外直接投資 年初来前年比（FFのみ・要確認）', '（FF低）', '—', '-4.3%'),
    ('16:15', '🇯🇵 日', '訪日外客数（フィスコのみ・要確認）', '—', '—', '310.37万人'),
    ('16:30', '🇬🇧 英', 'ベイリーBOE総裁 発言（Kiss/FF一致）', '◎', '要人発言', '—'),
    ('18:00', '🇪🇺 欧', 'ECB金融安定報告書（FFのみ・要確認）', '（FF中）', '—', '—'),
    ('18:30', '🇬🇧 英', '住宅価格指数 前年比（FFのみ・要確認）', '（FF低）', '+0.7%', '+0.9%'),
    ('19:00', '🇪🇺 欧', '消費者物価指数【改定値】 前年比（Kiss/FF/フィスコ一致）', '△', '+4.0%', '+4.0%'),
    ('19:00', '🇪🇺 欧', '消費者物価指数【改定値】 前月比（KissFXのみ・要確認）', '△', '+0.4%', '+0.4%'),
    ('19:00', '🇪🇺 欧', '消費者物価指数【改定値】 コア 前年比（Kiss/FF一致）', '△', '+2.5%', '+2.5%'),
    ('21:00', '🇺🇸 米', 'MBA住宅ローン申請指数（KissFXのみ・要確認）', 'C', '—', '6.2%'),
    ('22:30', '🇺🇸 米', '住宅着工件数（Kiss/FF一致）', 'A', '125.0万件', '122.1万件'),
    ('22:30', '🇺🇸 米', '建設許可件数（Kiss/FF一致・FF予想138万件）', 'A', '137.5万件', '140.0万件'),
    ('22:30', '🇨🇦 加', '新築住宅価格指数 前月比（FFのみ・要確認）', '（FF低）', '+0.1%', '-0.2%'),
    ('23:25', '🇪🇺 欧', 'ラガルドECB総裁 発言（Kiss/FF一致）', '◎', '要人発言', '—'),
    ('23:30', '🇺🇸 米', 'ハマック・クリーブランド連銀総裁 発言（投票権あり）（KissFXのみ・要確認）', 'AA', '要人発言', '—'),
    ('24:00', '🇬🇧 英', 'ベイリーBOE総裁 発言（Kiss/FF一致）', '◎（FF高）', '要人発言', '—'),
    ('24:00', '🇺🇸 米', '中古住宅販売保留 前月比（Kiss/FF一致・予想はKiss -2.1%、FF -2.0%で不一致・要確認）', 'A', '-2.1%（FF -2.0%）', '-7.3%'),
    ('24:00', '🇺🇸 米', '中古住宅販売保留 前年比（KissFXのみ・要確認）', 'A', '-13.7%', '-12.6%'),
    ('24:30', '🇺🇸 米', '週間原油在庫（Kiss/FF一致）', 'BB', '+40万バレル（FF）', '+465.7万バレル'),
    ('26:15', '🇺🇸 米', 'デイリー・サンフランシスコ連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('26:30', '🇨🇦 加', 'グラベル・カナダ中銀上級副総裁 発言（FFのみ・要確認）', '（FF低）', '要人発言', '—'),
    ('27:00', '🇳🇿 NZ', 'ブレマンRBNZ総裁 発言（Kiss/FF一致）', '◎', '要人発言', '—'),
    ('27:00', '🇺🇸 米', '20年債入札（160億ドル）（KissFXのみ・要確認）', 'AA', '—', '—'),
    ('27:35', '🇺🇸 米', 'バーFRB理事 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('28:00', '🇺🇸 米', 'FOMC議事要旨（10/27-28会合分）（Kiss/FF/フィスコ一致）', 'SS', '—', '—'),
    ('28:30', '🇺🇸 米', 'ウィリアムズNY連銀総裁 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('翌06:00', '🇺🇸 米', '対米証券投資 ネット長期フロー（Kiss/FF/フィスコ一致）', 'C', '1607億ドル（FF）', '2792億ドル'),
    ('翌06:00', '🇺🇸 米', '対米証券投資 ネットフロー合計（KissFXのみ・要確認）', 'C', '—', '1998億ドル'),
    ('翌06:15', '🇺🇸 米', 'カシュカリ・ミネアポリス連銀総裁 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('翌06:45', '🇳🇿 NZ', '貿易収支（Kiss/FF一致）', '○', '-16.50億（FF）', '-19.71億'),
]
def _key(r):
    t = r[0]
    if t.startswith('翌'):
        return (30 + int(t[1:3]), int(t[4:6]))
    if not t[:2].isdigit():
        return (29, 59)
    return (int(t[:2]), int(t[3:5]))
CAL_ROWS.sort(key=_key)

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
              <li>なし（KissFXの主要国休場日一覧・ForexFactory JSONで本日の休場記載なし）。次の休場は11/23（月）日本、11/26（木）米国。</li>
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
          <h3>📰 前日の相場振り返り（2026-11-17 火）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間（24時以降は翌日）。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はKissFXランク（米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×）を優先し、KissFXにない項目はForexFactory区分を（FF高・中・低）で表示。予想値の第3ソースとしてザイFX/フィスコの本日のスケジュールも参照。外為どっとコムのニュース一覧はJavaScript描画のため本文を取得できず、ザイFX・みんかぶ・KissFXで確認。【発表済み】は本日0時〜7時に実施済みの項目（00:00の米指標は前日11/17夜24:00発表分）。「翌」は翌日（11/19木）の日本時間。冬時間のため米東部時間+14時間で換算。</p>
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
