# -*- coding: utf-8 -*-
"""FX日報 2026-11-12（木）生成スクリプト"""
import glob, os

TODAY = '2026-11-12'
WEEKDAY = '木'

HERO_TITLE_SUB = (
    '前営業日11/11（水）は米利上げ観測の強まりでドル買いが続き、ドル円は200日線を上抜けて159.94円（9月2日以来）まで上昇、159.79円で引けた。ユーロドルは1.1083ドルと昨年5月以来の安値。'
    '本日11/12（木）は10:30浅田日銀審議委員の講演、16:00英GDP、22:30米新規失業保険申請件数、27:00米30年債入札が材料で、160円手前の介入警戒が上値を抑える。'
)

SUMMARY_HEADLINE = (
    'ドル円は200日線を突破し159.79円で引け、160円の節目と為替介入警戒が当面の上限。'
    '本日は浅田日銀委員の講演・英GDP・米30年債入札でドル高の続き具合を確かめる日'
)

SUMMARY_BODY = (
    '11/11（水）のNY市場でドル円は続伸し、終値159.79円（前日NY終値158.75円）。2時過ぎに159.94円と9月2日以来の高値をつけた（ザイFX/DZH）。'
    '10月米CPIの上振れとFRB高官のタカ派発言で、短期金融市場は12月利上げを完全に、来年3月までの2回目の利上げも完全に織り込んだ（みんかぶ）。ゴールドマン・サックスとノムラは12月に続く来年3月の利上げを予想に加えた（フィスコ）。'
    'ユーロドルは1.11ドルの下値を割り込み1.1083ドル、終値1.1090ドル。米国はベテランズデーで債券市場が休場、株式は通常取引でナスダック+1.60%と大幅高（みんかぶ）。本日の主要市場休場はなし。'
)

TOP_PAIR_BODY = (
    'ドル円は11/11のNY市場で1カ月以上上値を抑えてきた158円台半ば〜159円を上抜け、159.94円まで上昇。終値は159.79円（ザイFX/DZH）。200日線158.70円付近を明確に上回った（みんかぶ／フィスコは158.71円）。'
    '背景はFRBと日銀の利上げペースの差。短期金融市場はFRBの利上げを12月と来年3月までに2回織り込む一方、日銀は来年1月までに1回・6月までに2回と遅い（みんかぶ）。'
    '上値は160円。市場では「160円が近づき、政府・日銀による為替介入への警戒感も広がっている」との声（ザイFX/DZH）。ドル円オプションは円プット買いが強まり、リスクリバーサルの円コール超幅が1カ月物+1.88%→+1.60%へ縮小（フィスコ）。'
    '4時間足は上昇トレンド。15分・30分足では159.30円付近（11/11のピボット、みんかぶ）と200日線158.70円が押し目の目安、160円手前は介入警戒で利食いが出やすい水準。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'ドル円が160円手前まで上昇し、政府・日銀による為替介入への警戒が再燃している（ザイFX/DZH・みんかぶ）。高市首相は11日に「市場の動向に細心の注意」「現行の共同声明に基づき日銀と連携」と述べた（みんかぶ）。'
    '本日は休場明けの米債券市場で30年債入札（27:00、250億ドル）があり、長期金利が再び動く。VIXは17.49（-10.12%）と警戒感は低下（みんかぶ）。'
    'イランのレザイ事務局長が濃縮ウランの国外持ち出しを否定し、米イラン間の隔たりは残る（みんかぶ）。'
)

KEY_EVENTS_COUNT = '8件'
KEY_EVENTS_SUMMARY = (
    '日 浅田日銀審議委員の講演(10:30)・会見(時刻未定)、英 第3四半期GDP速報・月次GDP(16:00)、米 新規失業保険申請件数(22:30)、米 ハマック総裁(23:00)、米 中古住宅販売件数・バーFRB理事(24:00)、米 30年債入札(27:00)、欧 ラガルドECB総裁(28:30)'
)

MARKET_OVERVIEW = (
    '<strong>VIX</strong>：17.49（-1.97、-10.12%）、警戒感は大きく低下（みんかぶ、NY16:10）。'
    '<strong>米株（終値）</strong>：ダウ52,486.49ドル（+254.60、+0.49%）、S&amp;P500 7,619.38（+1.31%）、ナスダック25,466.19（+1.60%）（みんかぶ、NY16:22）。コアウィーブの決算が予想を上回りAI関連株が買い戻された。'
    '欧州株終値はFTSE100 +0.78%、DAX +1.20%、CAC40 +0.66%（みんかぶ）。'
    '<strong>米債利回り</strong>：ベテランズデーで米債券市場は休場。2年債4.74%、10年債4.99%、30年債5.35%（前日比変わらず、フィスコ）。日米金利差2.19%（-0.10、フィスコ午後2時台）。'
    '<strong>ドル指数（DXY）</strong>：102.93（+0.70、+0.68%）、高値102.96（フィスコ、午後2時台）。'
    '<strong>金</strong>：NY金先物12月限の終値4,000.50ドル（-29.70、-0.74%）。FRBの利上げ見通しによるドル高が重し（みんかぶ）。'
    '<strong>原油</strong>：WTI12月限の終値86.53ドル（+0.49、+0.57%）、通常取引序盤に88.74ドルまで上昇。イランのレザイ事務局長が濃縮ウランの引き渡しを否定したことが買い材料（みんかぶ）。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％（前日までの値を引き継ぎ）。'
    '<br><br><strong>今週の焦点：</strong> 本日11/12 英GDP、米新規失業保険申請件数、米30年債入札、浅田日銀審議委員の講演。11/13 米PPI（FF区分:高）。次回FOMCは12/9、ECB・BOEは12/17、日銀は12/18（KissFX）。'
)

RANKING_ROWS = [
    (1, 'AUD/JPY', 'rank-a', 'A', '直近スコア97・最適。ADX36.9、ADR比131％（5日ADR 116.9pips）、4H方向は下降。11/11は円安で東京午前に109.40円まで戻し、NYでは109.49円（00:48時点、みんかぶ）。下降基調への戻りの強さを確認する場面。', 'trend-down', '↓'),
    (2, 'USD/CAD', 'rank-a', 'A', '直近スコア92・最適。ADX33.9、ADR比124％、方向は上昇。FRBの利上げ観測によるドル全面高が支え。22:30にカナダ住宅建設許可（予想-4.1%）。', 'trend-up', '↑'),
    (3, 'AUD/USD', 'rank-a', 'A', '直近スコア84・最適。ADX28.9、ADR比122％、方向は下降。0.6850ドルが下値ポイント（みんかぶテクニカル）。', 'trend-down', '↓'),
    (4, 'EUR/AUD', 'rank-a', 'A', '直近スコア84・最適。ADX31.9、ADR比116％、方向は上昇。', 'trend-up', '↑'),
    (5, 'EUR/USD', 'rank-b', 'B', '直近スコア70・適。ADX18.1、ADR比119％、方向は下降。11/11は1.11ドルの下値を割り込み1.1083ドル（昨年5月以来の安値）、終値1.1090ドル（ザイFX/DZH）。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/11/11 09:08 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、1日前の数値。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'ドル円が200日線を突破、159.94円（9月2日以来）まで上昇し159.79円で引け',
        'ドル円は東京午前に158.96円まで上げて10月14日の高値158.95円をわずかに更新したが、159円に届かず158.71円まで押した（みんかぶ）。ロンドン時間に159円台へ乗せて159.17円、NY時間は1カ月以上上値を抑えてきた158円台半ば〜159円の水準を上抜けて上昇に弾みがつき、2時過ぎに159.94円（ザイFX/DZH）。'
        '終値は159.79円で前日NY終値158.75円から1円04銭のドル高。160円手前では戻り売り・利食い売りが出て、介入警戒も広がった（ザイFX/DZH）。ユーロ円は177.21円とほぼ横ばい、ポンド円は211.80円から212.62円へ上昇（フィスコ）。',
    ),
    (
        'FRBの利上げ観測が一段と強まる、ゴールドマン・ノムラが来年3月の利上げを予想に追加',
        '10月CPIが予想外に3カ月連続で加速したことを受け、ゴールドマン・サックスは12月の25bp利上げに続き2027年3月の利上げ（FF誘導目標4.25〜4.50%へ）を予想に加えた。ノムラも同様に12月・3月の利上げを予想（フィスコ）。短期金融市場は12月を完全に、来年3月までの2回目も完全に、来年1月までなら70%で織り込む（みんかぶ）。'
        'FRB高官は、ボウマン副議長が「インフレを2％に近づけるためにやるべきことがまだある」（12月利上げ支持には触れず）、グールズビー・シカゴ連銀総裁が「10月CPIは憂慮すべき水準」、ポールソン・フィラデルフィア連銀総裁が「さらなる段階的な利上げが適切」と発言（みんかぶ／フィスコ）。日銀の利上げ織り込みは来年1月までに1回・6月までに2回で、日米の金利差拡大観測がドル円を押し上げた。',
    ),
    (
        'ユーロドルは1.11ドルを割り込み1.1083ドル、昨年5月以来の安値',
        'ユーロドルは10月29日の安値1.1105ドルを下抜け1.1083ドルまで下落、終値1.1090ドル（前日NY終値1.1164ドル、ザイFX/DZH）。市場では「ECBも利上げが意識されるが、米国に比べるとペースや度合いは緩やか」との声。'
        'ユーロの短期金利先物オプションでは、ECBが来年3月中旬まで預金金利2.50%を据え置くと見込む取引が確認された（みんかぶ）。独CPI確報は前月比-0.2%・前年比+2.8%で予想通り。ナーゲル独連銀総裁は「ドイツの成長は第4四半期に加速する見込み」と述べた（みんかぶ）。18:45のラガルドECB総裁の発言内容は今回の3ソースで報道を確認できなかった（要確認）。',
    ),
    (
        'ポンドドルは1.32ドル台へ下落、BOEグリーン委員は「引き締め姿勢の強化が適切」',
        'ポンドドルは21日線（1.3360ドル付近）を下放れ、1.3276ドル（04:03時点）まで下落（みんかぶ）。一方でBOEのグリーン委員はFT紙への寄稿で「賃金上昇率は高すぎ、今後1年3.5%以上で安定する兆し」「先手を打って金融政策の引き締め姿勢を強化することが適切」と述べた（みんかぶ）。'
        'アナリストからは英国債の高利回りがポンドを支えるとの見方の一方、BOEの利上げ幅拡大はすでに織り込み済みで一段高の余地は限られるとの見方も出ている（みんかぶ）。本日16:00の英GDPが次の材料。',
    ),
    (
        '米株はAI関連の買い戻しで大幅高、原油は反発・金は続落',
        'NY株はダウが+0.49%、ナスダックが+1.60%（みんかぶ、終値）。コアウィーブの売上高とEBITDAが予想を上回り通期見通しを引き上げたことで、AI関連株への不安が和らいだ。VIXは17.49と10%低下（みんかぶ）。'
        'WTI原油は86.53ドル（+0.57%）。イランのレザイ事務局長が濃縮ウランの国外持ち出しを認めないと表明し買われた。金は4,000.50ドル（-0.74%）とドル高で続落（みんかぶ）。高市首相は「インフレを招くような経済政策を行うつもりはない」と述べた（みんかぶ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/12木）への引継ぎ：ドル円は159.79円、ユーロドルは1.1090ドルで前日を終えた。ドル高の理由はFRBの利上げ観測（12月・来年3月）と、日銀の利上げペースが遅いことによる日米金利差の拡大。'
    'ドル円の上値は160円で、近づくと政府・日銀の介入警戒が強まる（ザイFX/DZH・みんかぶ）。10:30の浅田日銀審議委員の講演・記者会見で利上げに前向きな発言が出れば円買い、慎重なら159円台後半の維持。'
    '16:00の英GDP（第3四半期速報 前期比予想+0.7%、月次 予想±0.0%）はポンドへの影響が大きい（KissFX）。夜は22:30の米新規失業保険申請件数（予想19.5万件）と、休場明けの米債券市場で27:00の30年債入札。明日11/13は米PPI。'
    'KissFXは「引き続き米ドル買い方向で考えるが、既に160円手前で介入警戒感が高まる」とする。'
    '注記：外為どっとコムのニュース一覧は本文を取得できず、ザイFX・みんかぶ・KissFXで構成した（要確認）。'
)

POINTS_EVENTS = [
    '08:50 🇯🇵 日 国内企業物価指数（10月）前年比 予想+6.5%（KissFX:×）',
    '10:30 🇯🇵 日 浅田日銀審議委員の講演（あいさつ）／記者会見は時刻未定（KissFX:◎・FFに記載なし・要確認）',
    '16:00 🇬🇧 英 第3四半期GDP速報 前期比 予想+0.7%（KissFX:◎）／月次GDP 予想±0.0%（KissFX:○、FF区分:高）',
    '22:30 🇺🇸 米 新規失業保険申請件数 予想19.5万件（KissFX:AA）',
    '23:00 🇺🇸 米 ハマック・クリーブランド連銀総裁の発言（投票権あり、KissFX:AA、FFは22:30・時刻要確認）',
    '24:00 🇺🇸 米 中古住宅販売件数 予想385万件（KissFX:A）／バーFRB理事の発言（KissFX:AA）',
    '27:00 🇺🇸 米 30年債入札（250億ドル、KissFX:S）',
    '28:30 🇪🇺 欧 ラガルドECB総裁の発言（KissFX:◎、FF区分:中）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：160円手前、介入警戒と日米金利差の綱引き',
        '200日線158.70円付近を上抜け、4時間足は上昇トレンドに戻った（みんかぶ）。押し目の目安は159.30円付近（11/11ピボット）と158.70円。160円に近づくと介入警戒で戻り売りが出る（ザイFX/DZH）。米債券市場の休場明けで米金利が動き、30年債入札の結果が27時以降のドル円を動かす。',
    ),
    (
        '円：浅田日銀審議委員の講演（10:30）',
        '日銀の利上げ織り込みは来年1月までに1回（みんかぶ）。浅田委員が12月の利上げに前向きな発言をすれば円買いでドル円の上値が重くなる。KissFXは「金融政策に対する発言があれば反応しやすい」とする。',
    ),
    (
        'ポンド：16:00の英GDPで1.32ドル台の下値を試す',
        'ポンドドルは21日線（1.3360ドル付近）を下放れ1.32ドル台（みんかぶ）。第3四半期GDP速報は前期比予想+0.7%（前回+0.5%）、月次GDPは予想±0.0%（前回+0.1%）。BOEグリーン委員は引き締め強化を主張しており、上振れなら利上げ観測を支えポンド買い、下振れなら1.32ドル台の下値を試す。',
    ),
    (
        'ユーロ：1.11ドル割れ後の戻り売り、28:30ラガルド総裁',
        'ユーロドルは1.1083ドルと昨年5月以来の安値（ザイFX/DZH）。1.11ドルが下値の節目から上値の抵抗に変わった。ECB据え置きを見込むオプション取引も出ており（みんかぶ）、ラガルド総裁が12月利上げに慎重なら一段安。',
    ),
    (
        '市場休場：なし',
        '本日11/12（木）は主要市場の休場なし（KissFXの休場日一覧・ForexFactory JSONで一致）。米債券市場は11/11の休場明けで通常取引。次の休場は11/23日本、11/26米国（KissFX）。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('06:45', '🇳🇿 NZ', '【発表済み】来訪者数 前月比（FFのみ・要確認）', '低', '—', '2.8%'),
    ('08:50', '🇯🇵 日', '国内企業物価指数（10月）前月比／前年比（Kiss/FF一致・前年比）', '×', '+0.3%／+6.5%', '-0.3%／+6.8%'),
    ('08:50', '🇯🇵 日', '対外・対内証券投資（先週）（ザイFX日程のみ・要確認）', '低', '—', '—'),
    ('09:00', '🇦🇺 豪', 'メルボルン研究所 インフレ期待（FFのみ・要確認）', '低', '—', '5.3%'),
    ('09:01', '🇬🇧 英', 'RICS住宅価格指数（Kiss/FF一致）', '×', '-34%（FF -33%）', '-32%'),
    ('10:30', '🇯🇵 日', '浅田日銀審議委員 講演（あいさつ）（KissFX・ザイFX日程、FFに記載なし・要確認）', '◎', '要人発言', '—'),
    ('11:00', '🇯🇵 日', '東京オフィス空室率（10月）（ザイFX日程のみ・要確認）', '低', '—', '1.85%'),
    ('16:00', '🇬🇧 英', '第3四半期GDP【速報値】前期比／前年比（Kiss/FF一致・前期比）', '◎', '+0.7%／+1.9%', '+0.5%／+1.4%'),
    ('16:00', '🇬🇧 英', 'GDP（9月）前月比（Kiss/FF一致）', '○', '±0.0%', '+0.1%'),
    ('16:00', '🇬🇧 英', '鉱工業生産（9月）前月比／前年比（Kiss/FF一致・前月比）', '○', '-0.4%／+2.8%', '+0.8%／+1.6%'),
    ('16:00', '🇬🇧 英', '製造業生産高（9月）前月比／前年比（Kiss/FF一致・前月比）', '○', '-0.5%／+3.8%', '+1.2%／+3.0%'),
    ('16:00', '🇬🇧 英', '商品貿易収支／貿易収支（Kiss/FF一致・商品貿易収支）', '△', '-192.00億／-21.00億ポンド', '-180.07億／-9.20億ポンド'),
    ('16:00', '🇬🇧 英', '建設支出 前月比（FFのみ・要確認）', '低', '0.0%', '-0.2%'),
    ('16:00', '🇬🇧 英', 'サービス業指数 3カ月/3カ月（FFのみ・要確認）', '低', '0.9%', '0.9%'),
    ('16:00', '🇬🇧 英', '企業投資【速報値】前期比（FFのみ・要確認）', '低', '0.4%', '1.7%'),
    ('18:00', '🇪🇺 欧', 'ECB経済報告（月例報告）（Kiss/FF一致）', '△', '—', '—'),
    ('18:03', '🇨🇳 中', 'M2マネーサプライ 前年比（FFのみ・時刻未確定・要確認）', '低', '7.2%', '7.2%'),
    ('18:03', '🇨🇳 中', '新規人民元建て融資（FFのみ・時刻未確定・要確認）', '低', '800億元', '1兆800億元'),
    ('19:30', '🇮🇳 印', '消費者物価指数（10月）（ザイFX日程のみ・要確認）', '低', '6.00%', '5.54%'),
    ('21:00', '🇧🇷 ブ', 'IBGEインフレ率IPCA（10月）（ザイFX日程のみ・要確認）', '低', '—', '4.58%'),
    ('22:30', '🇨🇦 加', '住宅建設許可 前月比（Kiss/FF一致）', '△', '-4.1%（FF -4.0%）', '+8.8%'),
    ('22:30', '🇺🇸 米', '新規失業保険申請件数（Kiss/FF一致）', 'AA', '19.5万件（FF 19.4万件）', '18.9万件'),
    ('23:00', '🇺🇸 米', 'ハマック・クリーブランド連銀総裁 発言（投票権あり）（Kiss/FF一致・FFは22:30、時刻要確認）', 'AA', '要人発言', '—'),
    ('24:00', '🇺🇸 米', '中古住宅販売件数（10月）（Kiss/FF一致）', 'A', '385万件（FF 389万件）', '399万件'),
    ('24:00', '🇺🇸 米', 'バーFRB理事 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('24:00', '🇺🇸 米', 'MBA住宅ローン延滞率（FFのみ・要確認）', '低', '—', '4.37%'),
    ('24:30', '🇦🇺 豪', 'CB景気先行指数 前月比（FFのみ・要確認）', '低', '—', '-0.3%'),
    ('25:15', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('26:00', '🇺🇸 米', '週間原油在庫（Kiss/FF一致）', 'BB', '—（FF -60万）', '-86.5万バレル'),
    ('26:30', '🇩🇪 独', 'ナーゲル独連銀総裁 発言（Kiss/FF一致）', '△', '要人発言', '—'),
    ('27:00', '🇺🇸 米', '30年債入札（250億ドル）（Kiss/FF一致）', 'S', '—', '5.62%／2.5倍（FF）'),
    ('27:10', '🇺🇸 米', 'デイリー・サンフランシスコ連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('27:30', '🇺🇸 米', 'シュミッド・カンザスシティ連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('28:00', '🇺🇸 米', '財政収支（10月）（Kiss/FF一致）', 'C', '-3000億ドル（FF -2986億ドル）', '-269億ドル'),
    ('28:30', '🇪🇺 欧', 'ラガルドECB総裁 発言（Kiss/FF一致）', '◎', '要人発言', '—'),
    ('翌06:30', '🇳🇿 NZ', 'BusinessNZ製造業PMI（Kiss/FF一致）', '△', '—', '56.5'),
    ('翌08:30', '🇺🇸 米', 'ウィリアムズNY連銀総裁 発言（FF・ザイFX日程、KissFX掲載範囲外・要確認）', '低', '要人発言', '—'),
    ('未定', '🇯🇵 日', '浅田日銀審議委員 記者会見（KissFX・ザイFX日程、FFに記載なし・要確認）', '◎', '要人発言', '—'),
]
def _key(r):
    t = r[0]
    if t.startswith('翌'):
        return (30 + int(t[1:3]), int(t[4:6]))
    if not t[:2].isdigit():
        return (99, 99)
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
              <li>なし（KissFXの主要国休場日一覧・ForexFactory JSONで本日の休場記載なし）。米債券市場は11/11の休場明けで通常取引。</li>
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
          <h3>📰 前営業日の相場振り返り（2026-11-11 水）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間（24時以降は翌日）。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はKissFXランク（米国SS〜C、その他◎〜×）を優先し、KissFXにない項目はForexFactory区分。【発表済み】は本日0時〜7時に実施済みの項目。「翌」は翌日（11/13）の日本時間。</p>
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
