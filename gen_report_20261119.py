# -*- coding: utf-8 -*-
"""FX日報 2026-11-19（木）生成スクリプト"""
import glob, os

TODAY = '2026-11-19'
WEEKDAY = '木'

HERO_TITLE_SUB = (
    '前日11/18（水）はウォラーFRB理事の「12月に0.50%利上げ」発言とタカ派のFOMC議事要旨でドル買いが続き、ユーロドルは1.0953ドルと1年7か月ぶりの安値をつけた。'
    '本日11/19（木）は09:30の豪雇用統計、22:30の米新規失業保険申請件数・フィラデルフィア連銀景況指数、米中ロ首脳会談が材料。'
)

SUMMARY_HEADLINE = (
    'FRBの12月利上げ観測がさらに固まりドル高が続く。'
    '本日は豪雇用統計で豪ドル、22:30の米指標とラガルド総裁でユーロドルの1.09ドル台半ばが試される'
)

SUMMARY_BODY = (
    '11/18（水）のFOMC議事要旨（10/27-28会合分）では、ほぼ全員が次回会合での追加措置が適切と予想し、数名は12月の利上げ幅を0.25%超とするのが妥当と主張した（ザイFX/フィスコ・みんかぶ一致）。'
    'ドル指数は103.85と連日の年初来高値（みんかぶ）。ユーロドルは1.0960ドル、ポンドドルは1.3136ドルまで下げて引けた（ザイFX/フィスコ）。'
    'ドル円は159.13〜159.65円のレンジで方向感が出ず、NY午後は159.3円台（ザイFX/DZH・フィスコ）。本日11/19（木）の主要市場休場はなし。'
)

TOP_PAIR_NAME = 'EUR/USD 🇪🇺🇺🇸'
TOP_PAIR_BODY = (
    'ユーロドルは11/18のロンドンで1.0953ドルと2025年4月以来の安値を更新し、NYは1.0960ドルで引けた（ザイFX/DZH・フィスコ）。'
    '下げた理由は2つ。1つはウォラー理事とFOMC議事要旨で米利上げ観測が強まったドル買い、もう1つはフランスなどユーロ圏周縁国の国債に再び売り圧力がかかったユーロ売り（みんかぶ）。ユーロはG10通貨で最も弱い（みんかぶ）。'
    '4Hデイトレ適性ランキング1位（スコア65・ADX47.2・下降）。15分・30分足では1.0953ドル（11/18安値）が下の節目、1.0981〜1.1000ドル（11/18の戻り高値と東京高値）が戻り売りの目安。'
    '22:30はラガルド総裁の発言と米新規失業保険申請件数・フィラデルフィア連銀景況指数が重なる。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'ダウは50,198.17ドル（-561.25、-1.11%）と大幅続落、S&amp;P500は-0.23%、ナスダックは+0.42%（みんかぶ）。エヌビディアは好決算で上昇して始まったが-2.89%で引けた（みんかぶ）。'
    'VIXは24.55（-0.91）と低下したが20を上回る（みんかぶ）。金先物は3,731.00ドル（-133.20、-3.45%）と急落し、3,800ドル割れは2025年9月以来の安値（ザイFX/フィスコ・みんかぶ）。'
    '本日は米中ロ3か国首脳会談（深セン、KissFX）があり、イラン情勢と原油の材料になる。アンソロピックは本日ナスダックに上場（KissFX・みんかぶ。IPO価格は83ドルとの一部報道あり・要確認）。'
)

KEY_EVENTS_COUNT = '11件'
KEY_EVENTS_SUMMARY = (
    '日 機械受注(08:50)、豪 雇用統計(09:30)、英 ディングラMPC委員(21:15)、南ア SARB政策金利(時刻要確認)、欧 ラガルドECB総裁(22:30)、米 新規失業保険申請件数・フィラデルフィア連銀景況指数(22:30)、'
    '米 ハマック総裁(22:50)、米 ジェファーソンFRB副議長(23:25)、米 景気先行指数(24:00)、米 10年TIPS入札(27:00)、米 バーFRB理事(28:15)'
)

MARKET_OVERVIEW = (
    '<strong>米株（11/18終値）</strong>：ダウ50,198.17ドル（-561.25、-1.11%）、S&amp;P500 7,323.63（-0.23%）、ナスダック24,429.89（+0.42%）、CME日経平均先物58,805円（大証比-445）（みんかぶ）。'
    '欧州株はFTSE100が-1.30%、独DAXが-1.19%、仏CAC40が-0.85%（みんかぶ・ザイFX/DZH）。'
    '<strong>米債利回り</strong>：2年債4.80%（0.00）、10年債5.07%（-0.04）、30年債5.41%（-0.05）、日米金利差2.19%（ザイFX/フィスコ午後2時台）。10年債はウォラー発言で5.12%まで上昇後、原油安と住宅指標で5.05〜5.06%へ低下（ザイFX/フィスコ・DZH）。'
    '米20年債入札は最高落札利回り5.459%（WI 5.459%）、応札倍率2.63倍（前回2.73倍）と低調（みんかぶ・ザイFX/フィスコ）。'
    '<strong>ドルインデックス</strong>：103.84（+0.35、ザイFX/フィスコ午後2時台）。ロンドンで103.852と連日の年初来高値（みんかぶ）。'
    '<strong>金</strong>：NY金先物3,731.00ドル（-133.20、-3.45%）（ザイFX/フィスコ）。FRB高官が追加利上げの必要性を強調し、金利の付かない金が売られた（みんかぶ）。'
    '<strong>原油</strong>：WTI先物82.99ドル（-3.02、-3.51%）（ザイFX/フィスコ）。米週間原油在庫が+338万バレルと予想外の増加、米中ロ首脳会談を前に和平期待で供給ひっ迫懸念が後退（ザイFX/フィスコ・みんかぶ）。'
    '<strong>VIX</strong>：24.55（-0.91、-3.57%）（みんかぶ）。'
    '<br><br><strong>政策金利（11/16確認分を継続）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。'
    '<br><br><strong>今週の焦点：</strong> 19日 米中ロ3か国首脳会談・豪雇用統計・アンソロピック上場（KissFX）、20日 日本全国CPI（KissFX）、20日（金）英・EU首脳会談（みんかぶ）。'
    'CMEフェドウォッチでは12月の0.25%利上げ織り込みが94.9%、0.50%利上げが5.1%（11/18午後時点、みんかぶ）。'
)

RANKING_ROWS = [
    (1, 'EUR/USD', 'rank-a', 'A', 'スコア65・適。ADX47.2、ADR比77％（5日ADR 52.7pips）、4H方向は下降。11/18は1.0953ドルと2025年4月以来の安値（ザイFX/DZH）。米利上げ観測のドル買いと仏・周縁国の国債売りによるユーロ売りが重なる（みんかぶ）。ユーロ圏HICPコア改定値は前年比2.6%と速報2.5%から上方修正（ザイFX/DZH）。22:30のラガルド総裁と米指標が材料。', 'trend-down', '↓'),
    (2, 'USD/CHF', 'rank-a', 'A', 'スコア65・適。ADX40.3、ADR比82％、4H方向は上昇。11/18のNYは0.8416フランまで下げた後、FOMC議事要旨のドル買いで0.8442フランまで上昇（ザイFX/フィスコ）。16:00にスイス貿易収支（KissFXのみ）。', 'trend-up', '↑'),
    (3, 'AUD/JPY', 'rank-b', 'B', 'スコア63・候補。ADX56.4、ADR比78％、4H方向は下降。09:30の豪10月雇用統計は失業率 予想4.7%（前回4.7%）、新規雇用者数 予想+2.50万人（KissFX）／+2.55万人（FF）（前回-3.93万人）。前回の大幅減から回復するかが焦点で、KissFXは「豪ドルへの影響は非常に大きなモノになりやすい」と指摘。株安・金急落のリスク回避は豪ドル円の重し。', 'trend-down', '↓'),
    (4, 'USD/CAD', 'rank-b', 'B', 'スコア59・候補。ADX44.0、ADR比72％、4H方向は上昇。WTI原油は-3.51%の82.99ドルと急落（ザイFX/フィスコ）しており、資源国通貨のカナダドルには売り材料。22:30に鉱工業製品価格・原料価格指数。', 'trend-up', '↑'),
    (5, 'GBP/USD', 'rank-b', 'B', 'スコア57・候補。ADX52.3、ADR比67％、4H方向は下降。11/18は英サービスCPIが前年比3.7%と予想3.8%を下回りポンド売り（みんかぶ）、NYで1.3136ドルまで下落し約1か月ぶりの安値（ザイFX/フィスコ）。10月の年初来安値に並ぶ水準（みんかぶ）。21:15ディングラ委員、23:25ロンバルデリ副総裁（KissFXのみ）の発言。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/11/18 10:44 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、前日の数値。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'FOMC議事要旨はタカ派：ほぼ全員が12月の追加利上げを支持',
        '19日04:00公表の10/27-28会合分の議事要旨で、ほぼ全員の委員が次回会合での追加措置が適切と予想（ザイFX/フィスコ・みんかぶ一致）。数名は12月の利上げ幅を0.25%超とするのが妥当と主張し、一部は10月の0.25%利上げを支持していた（ザイFX/フィスコ・みんかぶ）。'
        '少数は10月の据え置き判断を「紙一重（際どい）」と評価し、圧倒的多数がインフレ見通しに上振れリスクがあると認識（みんかぶ・ザイFX/フィスコ）。多くの参加者はAI投資の拡大をインフレリスクの重要な要因と見ていた（みんかぶ）。'
        'ドル円は159.20円付近から159.40円へ、ユーロドルは1.0980ドルから1.0963ドルへ動きドル買い（ザイFX/フィスコ）。米株は利上げ確信を強める内容にマイナスの反応（みんかぶ）。',
    ),
    (
        'ウォラーFRB理事が「12月に0.50%利上げ」を推奨、ユーロドルは1.0953ドル',
        'ウォラー理事はCNBCのインタビューで、インフレが「間違った方向に向かっている」「インフレが広がっていることを懸念」と述べ、12月FOMCでの0.50%利上げを推奨した（ザイFX/フィスコ・DZH・みんかぶ一致）。'
        '米10年債利回りは5.12%まで上昇し、ユーロドルは1.0953ドルと2025年4月以来1年7か月ぶりの安値、ドル円は159.48円付近まで上昇（ザイFX/DZH）。'
        'その後、原油安と弱い住宅指標で10年債利回りは5.05〜5.06%へ低下し、ドル買いは一服した（ザイFX/フィスコ・DZH）。バー理事も「さらなる利上げが適切になる公算が大きい」と発言したが、反応は限定的（ザイFX/DZH）。',
    ),
    (
        '英CPIは前年比3.6%も、サービスCPIの下振れでポンド売り',
        '英10月CPIは前年比+3.6%（KissFX・FF予想+3.6%、フィスコ予想+3.5%、前回+3.5%）、コアは+2.8%（前回+2.8%）、RPIは+4.2%（ザイFX/フィスコ・DZH）。'
        '一方、英中銀が重視するサービスCPIは前年比+3.7%と前回並みで、予想+3.8%を下回り、ポンドが売られた（みんかぶ）。フィスコは「英国のインフレ鎮静化で英中銀の利上げ観測が後退し、ポンド売りに拍車がかかった」と伝えた。'
        'ポンドドルは1.3176ドル（16時台）からNYで1.3136ドルまで下落し約1か月ぶり安値（みんかぶ・ザイFX/フィスコ）。ポンド円は209円台前半まで下げ、21日線を下抜けた（みんかぶ）。20日（金）の英・EU首脳会談で関係緊密化に合意すれば中長期的なポンドの支えとの見方（みんかぶ）。',
    ),
    (
        'ユーロはG10で最も弱い：仏・周縁国の国債に売り圧力',
        'ユーロドルは1.0955ドル付近、ユーロ円は174円台半ばと2025年10月31日以来の安値まで下落（みんかぶ）。アナリストは、フランスなどユーロ圏周縁国の国債に再び圧力がかかっていることがユーロ相場の重しと指摘（みんかぶ）。'
        'ユーロ圏10月HICP改定値は前年比+4.0%（速報と同じ）、コアは+2.6%（前回+2.5%）（ザイFX/DZH）。'
        'ECBは11月25日に銀行の最低準備率を1%から2%に引き上げることを協議する見通しと関係者の話として伝わった（みんかぶ）。ラガルド総裁は「AI関連企業の株価水準は依然として極めて野心的で、最終的に調整を迫られる公算が大きい」との見方を示した（みんかぶ）。',
    ),
    (
        'エヌビディア好決算も買いが続かず株安、金は3,800ドル割れ、原油も急落',
        'エヌビディアは売上高が予想を大きく上回り、2028年度の増収率見通しを75%増に上方修正（みんかぶ）。東京朝はリスク警戒が後退しドル円は159.65円まで上昇したが、日経平均が高値から1,300円超下げると円買いで159.14円まで下落（みんかぶ）。'
        'NYではエヌビディア株も-2.89%と下げに転じ、ダウは-561.25ドル（みんかぶ）。金先物は-3.45%の3,731.00ドル、WTI原油は-3.51%の82.99ドル（ザイFX/フィスコ）。'
        '米10月住宅着工件数は130.9万戸（予想125万戸）と7月以来の高水準だが、建設許可件数は129.5万戸（予想137.5万戸）と2020年5月以来の低水準（ザイFX/フィスコ）。中古住宅販売成約指数は前月比-4.7%（予想-2.0%）と下振れ（ザイFX/フィスコ・みんかぶ一致）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/19木）への引継ぎ：ドル円は159.3円台、ユーロドルは1.0960ドル、ポンドドルは1.3136ドル付近（ザイFX/フィスコ・DZH）。FOMC議事要旨で12月利上げ観測は一段と固まり、ドル高の地合いが続く。'
    'ただし短期金融市場は12月の0.25%利上げをほぼ織り込み済み（みんかぶ）で、上乗せ材料は0.50%利上げ観測の広がり。22:30の米新規失業保険申請件数（予想19.7万件）とフィラデルフィア連銀景況指数が強ければドル買い、弱ければ米金利低下でドル売り。'
    '09:30の豪雇用統計で豪ドル、米中ロ首脳会談の結果で原油・金・クロス円が動く。KissFXは「米ドルの方向性と米株価指数の調整が続くかどうかがキモ」と指摘。ドル円は160円付近で為替介入への警戒が続く（KissFX）。'
)

POINTS_EVENTS = [
    '08:50 🇯🇵 日 機械受注 前月比 予想+1.5%（Kiss）／+1.3%（FF）で不一致・要確認（Kiss×）',
    '09:30 🇦🇺 豪 失業率 予想4.7%（Kiss/FF/フィスコ一致・Kiss◎・FF区分:高）',
    '09:30 🇦🇺 豪 新規雇用者数 予想+2.50万人（Kiss）／+2.55万人（FF）で不一致・要確認（Kiss◎・FF区分:高）',
    '21:15 🇬🇧 英 ディングラMPC委員の発言（Kiss/FF一致・Kiss△）',
    '時刻未定 🇿🇦 南ア SARB政策金利 予想7.25%据え置き（KissFXは時間未定、フィスコは22:00・要確認・Kiss△）',
    '22:30 🇪🇺 欧 ラガルドECB総裁の発言（Kiss/FF一致・Kiss◎・FF区分:中）',
    '22:30 🇺🇸 米 新規失業保険申請件数 予想19.7万件（Kiss・フィスコ）／19.8万件（FF）で不一致・要確認（KissランクAA）',
    '22:30 🇺🇸 米 フィラデルフィア連銀景況指数 予想+20.0（Kiss）／20.6（FF）／23.2（フィスコ）で不一致・要確認（KissランクA）',
    '22:50 🇺🇸 米 ハマック・クリーブランド連銀総裁の発言（投票権あり）（Kiss/FF一致・KissランクAA）',
    '23:25 🇺🇸 米 ジェファーソンFRB副議長の発言（投票権あり）（Kiss/FF一致・KissランクAA）',
    '24:00 🇺🇸 米 景気先行指数 予想±0.0%（Kiss/FF/フィスコ一致・KissランクA）',
    '27:00 🇺🇸 米 10年インフレ連動債（TIPS）入札 190億ドル（KissFXのみ・要確認・KissランクAA）',
    '28:15 🇺🇸 米 バーFRB理事の発言（投票権あり）（Kiss/FF一致・KissランクAA）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ユーロドル：1.0953ドルの安値',
        '4H下降トレンドで、11/18は1.0953ドルまで下げた後1.0981ドルまで戻して1.0960ドルで引けた（ザイFX/DZH・フィスコ）。15分・30分足では1.0953ドルを割ると下げが広がりやすく、1.0981〜1.1000ドルの戻りは売り場の目安。'
        '仏・周縁国の国債売りが続くかどうか（みんかぶ）と、22:30のラガルド総裁の発言が材料。',
    ),
    (
        'ドル円：159.13〜159.65円のレンジ',
        '11/18は159.13〜159.65円の値幅にとどまった（ザイFX/DZH）。下は前日安値158.87円と200日移動平均線158.81円が重要なサポート（ザイFX/DZH）。上は160円付近で為替介入への警戒が上値を抑える（KissFX・みんかぶ）。'
        'FRBの利上げ観測によるドル買いと、株安によるリスク回避の円買いが打ち消し合っている。どちらかのレンジを抜けた方向に15分足でついていく。',
    ),
    (
        '豪ドル：09:30の豪雇用統計',
        '前回の新規雇用者数は-3.93万人と大幅減（KissFX）。予想は+2.50万人（KissFX）／+2.55万人（FF）。RBAは11/3に4.85%へ利上げ済みで、雇用の回復が確認されれば追加利上げ観測で豪ドル買い、再び減少なら豪ドル売り。'
        'AUD/JPYは4H下降トレンド（ランキング3位）で、株安・金急落のリスク回避も重し。',
    ),
    (
        'リスク要因：米中ロ首脳会談・アンソロピック上場',
        '本日、APEC首脳会議（深セン）で米中ロ3か国首脳会談が開かれる（KissFX）。イラン情勢と原油相場の材料。11/18の原油安は和平期待による（ザイFX/フィスコ）。'
        'アンソロピックは本日ナスダックで取引開始（KissFX・みんかぶ）。みんかぶは「上場後の動向が今後数日間の市場心理を大きく左右する」との指摘を伝えた。株安が続けば円買い・フラン買い。',
    ),
    (
        '市場休場：なし',
        '本日11/19（木）は主要市場の休場なし（KissFXの主要国休場日一覧・ForexFactory JSONで一致）。次の休場は11/23日本、11/26米国（KissFX）。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('00:00', '🇬🇧 英', '【発表済み】ベイリーBOE総裁 発言（前日24:00分・Kiss/FF一致）', '◎（FF高）', '要人発言', '—'),
    ('00:00', '🇺🇸 米', '【発表済み】中古住宅販売保留 前月比（前日24:00分）結果-4.7%', 'A', '-2.0%（FF）', '-7.2%（-7.3%から修正）'),
    ('00:30', '🇺🇸 米', '【発表済み】週間原油在庫 結果+338万バレル', 'BB', '+40万バレル（FF）', '+465.7万バレル'),
    ('02:15', '🇺🇸 米', '【発表済み】デイリー・サンフランシスコ連銀総裁 発言（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('02:30', '🇨🇦 加', '【発表済み】グラベル・カナダ中銀上級副総裁 発言（FFのみ・要確認）', '（FF低）', '要人発言', '—'),
    ('03:00', '🇳🇿 NZ', '【発表済み】ブレマンRBNZ総裁 発言（Kiss/FF一致）', '◎', '要人発言', '—'),
    ('03:00', '🇺🇸 米', '【発表済み】20年債入札 最高落札利回り5.459%・応札倍率2.63倍', 'AA', '—', '応札倍率2.73倍'),
    ('03:35', '🇺🇸 米', '【発表済み】バーFRB理事 発言（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('04:00', '🇺🇸 米', '【発表済み】FOMC議事要旨（10/27-28会合分）', 'SS', '—', '—'),
    ('04:30', '🇺🇸 米', '【発表済み】ウィリアムズNY連銀総裁 発言（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('06:00', '🇺🇸 米', '【発表済み】対米証券投資 ネット長期フロー 結果1553億ドル', 'C', '1607億ドル（FF）', '2850億ドル（2792億ドルから修正）'),
    ('06:15', '🇺🇸 米', '【発表済み】カシュカリ・ミネアポリス連銀総裁 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('06:45', '🇳🇿 NZ', '【発表済み】貿易収支 結果-27.72億NZドル（Kiss/FF一致）', '○', '-16.50億（FF）', '-21.23億（-19.71億から修正）'),
    ('08:50', '🇯🇵 日', '機械受注 前月比（Kiss/FF。予想が不一致・要確認）', '×', '+1.5%（Kiss）／+1.3%（FF）', '+5.2%'),
    ('08:50', '🇯🇵 日', '機械受注 前年比（Kiss/フィスコ。予想が不一致・要確認）', '×', '+13.5%（Kiss）／+15.9%（フィスコ）', '+18.6%'),
    ('08:50', '🇯🇵 日', '対外・対内証券投資（フィスコのみ・要確認）', '—', '—', '—'),
    ('09:30', '🇦🇺 豪', '失業率（Kiss/FF/フィスコ一致）', '◎（FF高）', '4.7%', '4.7%'),
    ('09:30', '🇦🇺 豪', '新規雇用者数（Kiss/FF。予想が不一致・要確認）', '◎（FF高）', '+2.50万人（Kiss）／+2.55万人（FF）', '-3.93万人'),
    ('10:00', '🇨🇳 中', 'SWIFTグローバル支払い 人民元建て（フィスコのみ・要確認）', '—', '—', '3.33%'),
    ('10:10', '🇯🇵 日', '国債買い入れオペ（残存3-5年・5-10年・25年超）（フィスコのみ・要確認）', '—', '—', '—'),
    ('14:00', '🇯🇵 日', '首都圏新築分譲マンション（フィスコのみ・要確認）', '—', '—', '-40.1%'),
    ('16:00', '🇨🇭 ス', '貿易収支（KissFXのみ・要確認）', '×', '—', '+13.5億'),
    ('18:00', '🇪🇺 欧', '経常収支（FFのみ・要確認）', '（FF低）', '166億', '87億'),
    ('20:00', '🇩🇪 独', '独連銀月報（FFのみ・要確認）', '（FF低）', '—', '—'),
    ('20:00', '🇬🇧 英', 'CBI企業動向調査（Kiss/FF一致）', '×', '-29（FF）', '-32'),
    ('21:15', '🇬🇧 英', 'ディングラMPC委員 発言（Kiss/FF一致）', '△', '要人発言', '—'),
    ('未定', '🇿🇦 南ア', 'SARB政策金利＆声明発表（KissFXは時間未定、フィスコは22:00・要確認）', '△', '7.25%据え置き', '7.25%（25bp利上げ）'),
    ('22:30', '🇪🇺 欧', 'ラガルドECB総裁 発言（Kiss/FF一致）', '◎（FF中）', '要人発言', '—'),
    ('22:30', '🇨🇦 加', '鉱工業製品価格 前月比（Kiss/FF。予想が不一致・要確認）', '△', '+0.5%（Kiss）／+0.4%（FF）', '+2.0%'),
    ('22:30', '🇨🇦 加', '原料価格指数 前月比（Kiss/FF。予想が不一致・要確認）', '△', '+1.0%（Kiss）／+0.9%（FF）', '+4.8%'),
    ('22:30', '🇺🇸 米', '新規失業保険申請件数（Kiss/FF/フィスコ。予想はFFのみ19.8万件で不一致・要確認）', 'AA（FF中）', '19.7万件', '20.0万件'),
    ('22:30', '🇺🇸 米', 'フィラデルフィア連銀景況指数（Kiss/FF/フィスコ。予想が不一致・要確認）', 'A（FF中）', '+20.0（Kiss）／20.6（FF）／23.2（フィスコ）', '+20.9'),
    ('22:50', '🇺🇸 米', 'ハマック・クリーブランド連銀総裁 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('23:25', '🇬🇧 英', 'ロンバルデリBOE副総裁 発言（KissFXのみ・要確認）', '△', '要人発言', '—'),
    ('23:25', '🇺🇸 米', 'ジェファーソンFRB副議長 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('24:00', '🇺🇸 米', '景気先行指数 前月比（Kiss/FF/フィスコ一致）', 'A', '±0.0%', '±0.0%'),
    ('24:15', '🇺🇸 米', 'MBA住宅ローン延滞率（FFのみ・要確認）', '（FF低）', '—', '4.37%'),
    ('24:30', '🇺🇸 米', '週間天然ガス貯蔵量（Kiss/FF一致）', 'B', '+250億立方フィート（FF）', '+610億立方フィート'),
    ('25:00', '🇺🇸 米', 'カンザスシティ連銀製造業活動指数（KissFXのみ・要確認）', 'C', '—', '+11'),
    ('26:30', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('27:00', '🇺🇸 米', '10年インフレ連動債（TIPS）入札 190億ドル（KissFXのみ・要確認）', 'AA', '—', '—'),
    ('28:15', '🇺🇸 米', 'バーFRB理事 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('翌06:00', '🇺🇸 米', 'バーキン・リッチモンド連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
]
def _key(r):
    t = r[0]
    if t.startswith('翌'):
        return (30 + int(t[1:3]), int(t[4:6]))
    if t == '未定':
        return (22, 0)
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
        <h3>{TOP_PAIR_NAME}</h3>
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
          <h3>📰 前日の相場振り返り（2026-11-18 水）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間（24時以降は翌日）。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はKissFXランク（米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×）を優先し、KissFXにない項目はForexFactory区分を（FF高・中・低）で表示。予想値の第3ソースとしてザイFX/フィスコの本日のスケジュールも参照。外為どっとコムのニュース一覧はJavaScript描画のため本文を取得できず、ザイFX・みんかぶ・KissFXで確認。【発表済み】は本日0時〜7時に実施済みの項目（00:00の項目は前日11/18夜24:00分）。「未定」の南ア政策金利はフィスコの22:00に合わせて並べた。「翌」は翌日（11/20金）の日本時間。冬時間のため米東部時間+14時間で換算。</p>
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
