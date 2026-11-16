# -*- coding: utf-8 -*-
"""FX日報 2026-11-17（火）生成スクリプト"""
import glob, os

TODAY = '2026-11-17'
WEEKDAY = '火'

HERO_TITLE_SUB = (
    '前日11/16（月）はAI関連株の急落でナスダックが-2.49%、VIXは23.00へ急上昇。リスク回避の円買いと介入警戒でドル円は159.36円まで下げた。'
    'ユーロドルは1.0991ドルと節目の1.10ドルを割り込み、2025年4月以来の安値。本日11/17（火）は22:30の米小売売上高と、米株引け後のエヌビディア決算が中心材料。'
)

SUMMARY_HEADLINE = (
    'ドル円は160円の壁と株安の円買いで159円台半ばへ押し戻された。ユーロドルは1.10ドル割れでドル高は継続。'
    '本日は米小売売上高とエヌビディア決算で、株とドルの両方が動く'
)

SUMMARY_BODY = (
    '11/16（月）のドル円は東京朝の159.89円が高値（みんかぶ）、NYで159.36円まで下げて引けた（ザイFX/フィスコ）。'
    '米11月NY連銀製造業景気指数は7.8（予想18.0、前回25.5）と大きく下振れ（みんかぶ・ザイFX/フィスコ一致）。'
    'ダウは-1.41%、ナスダックは-2.49%と大幅安、VIXは23.00（+18.81%）（みんかぶ）。'
    'ウォーシュFRB議長の講演はAIの影響が中心で、金融政策への言及はなかった（みんかぶ・ザイFX/DZH一致）。本日11/17（火）の主要市場休場はなし。'
)

TOP_PAIR_BODY = (
    'ドル円は11/16の東京朝に159.89円をつけた後、東京午後に159.36円まで下落（みんかぶ）。NYでも159.67円から159.36円まで下げて引けた（ザイFX/フィスコ）。'
    '下げた理由は3つ。アジア株・米株のハイテク売りによるリスク回避の円買い、米NY連銀製造業景気指数の大幅な下振れと原油安による米長期金利の低下、160円手前での介入警戒（ザイFX/フィスコ・みんかぶ）。'
    '一方、FRBの追加利上げ観測（市場は来年までにあと3回超を想定、みんかぶ）で日米金利差は縮まらず、下値は堅い。'
    '4時間足は上昇トレンドを維持。15分・30分足では159.35円（11/16安値）を割るかが分かれ目。上値はボリンジャーバンド2σ上限の160.01円（みんかぶ）。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'VIXは23.00（+3.63、+18.81%）へ急上昇（みんかぶ）。ナスダック-2.49%、S&amp;P500-1.92%と株安が加速し、リスク回避の円買いが出た（みんかぶ・ザイFX/DZH）。'
    '本日は米株引け後にエヌビディア決算。過去10四半期の決算後の株価変動はいずれも10%未満だが、今回はフアン前CEO解任後の初決算でより大きな変動が意識されている（みんかぶ）。'
    'ドル円は160円付近で介入警戒が続く。週末にイラン革命防衛隊がバーレーンを攻撃したと伝わり（みんかぶ・ザイFX/フィスコ）、中東情勢も重し。'
)

KEY_EVENTS_COUNT = '11件'
KEY_EVENTS_SUMMARY = (
    '豪 ブロックRBA総裁(07:50)、豪 RBA議事録(09:30)、英 雇用統計(16:00)、独 ZEW景況感(19:00)、米 小売売上高・輸入物価(22:30)、'
    '米 ウォラーFRB理事(23:10)、米 鉱工業生産(23:15)、米 ハマック総裁(23:30)、米 ウィリアムズ総裁(28:25)、米 エヌビディア決算(米株引け後)'
)

MARKET_OVERVIEW = (
    '<strong>VIX</strong>：23.00（+3.63、+18.81%）（みんかぶ、NY16:13時点）。'
    '<strong>米株（11/16終値）</strong>：ダウ51,608.17ドル（-739.38、-1.41%）、S&amp;P500 7,416.59（-1.92%）、ナスダック24,509.76（-2.49%）（みんかぶ）。ダウは一時835ドル安。SOX指数は午後2時台で-4.53%（ザイFX/フィスコ）。'
    'エヌビディア決算とアンソロピックのIPOを控え、AI関連株の持ち高調整が続いた（みんかぶ・ザイFX/DZH）。'
    '<strong>米債利回り</strong>：2年債4.832%（-0.010）、10年債5.129%（-0.006）、30年債5.473%（+0.008）（みんかぶ）。株安と原油安で低下したが、利上げ観測で下げは小幅。'
    '<strong>ドルインデックス</strong>：103.59（+0.18、ザイFX/フィスコ午後2時台）。ロンドン時間に年初来高値を更新（みんかぶ）。'
    '<strong>金</strong>：NY金先物12月限3,853.00ドル（-33.30、-0.86%）（みんかぶ）。米利上げ見通しと株安で反落。'
    '<strong>原油</strong>：WTI12月限85.72ドル（-2.84、-3.21%）（みんかぶ）。イランのバーレーン攻撃があったが、供給過剰に焦点が集まり続落（ザイFX/フィスコ）。'
    '<br><br><strong>政策金利（前日11/16確認分を継続）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。'
    '<br><br><strong>今週の焦点：</strong> 17日 米小売売上高・エヌビディア決算、18日 FOMC議事要旨（10/27-28会合分）・英CPI、19日 米中・米中ロ首脳会談（深セン、ホワイトハウス発表で米中13:45・米中ロ15:00 JST、みんかぶ）、20日 日本CPI（KissFX）。'
    '英2年債利回りは5%付近へ上昇し、市場は12/17の英MPCでの利上げを約8割織り込む（みんかぶ）。'
)

RANKING_ROWS = [
    (1, 'USD/CHF', 'rank-a', 'A', 'スコア81・最適。ADX44.4、ADR比107％（5日ADR 63.3pips）、4H方向は上昇。11/16は0.8373フランへ下げた後0.8403フランまで上昇（ザイFX/フィスコ）。SNBは0.00%、FRBの利上げ観測で金利差が広がりドル買いが続く。', 'trend-up', '↑'),
    (2, 'EUR/USD', 'rank-a', 'A', 'スコア79・適。ADX34.4、ADR比101％、方向は下降。11/16は1.10ドルを割り1.0991ドルで引け、2025年4月以来の安値（ザイFX/フィスコ）。理由は欧米の金利差拡大観測とフランス国債の続落（仏10年債利回りは再び5%に接近）。ストラテジストは1.08ドルへの下落を指摘（みんかぶ）。19:00の独ZEWが材料。', 'trend-down', '↓'),
    (3, 'USD/CAD', 'rank-a', 'A', 'スコア75・適。ADX44.7、ADR比96％、方向は上昇。11/16のカナダ10月CPIは前月比+0.2%（予想+0.3%）、前年比+3.1%（予想+3.2%）と下振れ（みんかぶ）、BOCの追加利上げ観測を弱める内容。原油3%安もカナダドルの重し。マックレム総裁は来年6月に退任（みんかぶ）。', 'trend-up', '↑'),
    (4, 'GBP/USD', 'rank-b', 'B', 'スコア74・適。ADX47.2、ADR比93％、方向は下降。11/16は1.3205ドルから1.3177ドルへ下落（ザイFX/フィスコ）。10月の支持帯1.32ドルを割り、10月の年初来安値1.3135ドルが次の目安（みんかぶ）。16:00の英雇用統計と18日の英CPIが材料。', 'trend-down', '↓'),
    (5, 'AUD/USD', 'rank-b', 'B', 'スコア72・適。ADX49.1、ADR比91％、方向は下降。豪ドル円は株安で107.30円まで下落（ザイFX/DZH）。07:50のブロックRBA総裁発言と09:30のRBA議事録（11/3の利上げ会合分、6対3の票割れ）が材料。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/11/16 08:26 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、前日の数値。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'AI関連株の急落：ナスダック-2.49%、VIXは23.00へ急上昇。リスク回避の円買いが広がる',
        'ダウは-739.38ドル（-1.41%）の51,608.17ドル、S&amp;P500は-1.92%、ナスダックは-2.49%と大幅安。ダウは一時835ドル安（みんかぶ）。'
        '理由は、今週のエヌビディア決算とアンソロピックのIPO（最大904億ドル調達の見通し）を控えた持ち高調整。エヌビディアやアルファベット、アマゾンなどAI関連株が指数を押し下げた（みんかぶ）。'
        '東京時間からアジア株のハイテク売りが目立ち、円買いのきっかけになった（みんかぶ）。VIXは23.00（+18.81%）（みんかぶ）。'
        'クロス円は全面安で、ユーロ円175.22円、ポンド円210.08円、豪ドル円107.30円、カナダドル円111.44円まで下落（ザイFX/DZH）。',
    ),
    (
        'ドル円は159.36円まで下落。NY連銀指数の大幅下振れ・原油安・介入警戒が重なる',
        'ドル円は東京朝の159.89円を高値に、東京午後に先週末の押し目159.52円を割り159.36円まで下げた（みんかぶ）。'
        '高田日銀審議委員が「機動的な利上げを行う局面」「中立金利に近づけるペースを速める新たな局面」と述べたことも円買いを支えた（みんかぶ）。ただしタカ派で知られる委員のため、直後の反応は限定的（みんかぶ）。'
        'NYでは米11月NY連銀製造業景気指数が7.8（予想18.0、前回25.5）と大きく下振れ。原油安で長期金利が下がりドル売りが出て、159.67円から159.36円まで下げて引けた（ザイFX/フィスコ）。'
        '日本の7-9月期GDP速報は前期比0.0%（予想+0.1%）、年率-0.1%（予想+0.2%）とマイナス成長だったが、日銀の利上げ期待に変化はないとされる（みんかぶ）。',
    ),
    (
        'ユーロドルは節目の1.10ドルを割り1.0991ドル、2025年4月以来の安値',
        'ユーロドルは1.1019ドルから1.0991ドルまで下げて引けた（ザイFX/フィスコ）。ユーロは全面安（ザイFX/フィスコ）。'
        '理由は2つ。FRBの追加利上げ観測による欧米金利差の拡大観測と、域内の債務・政局懸念でフランス国債が続落し、仏10年債利回りが再び5%に接近したこと（ザイFX/フィスコ）。'
        '市場では「ECBも利上げするが、米国よりペースや度合いが緩やか」との予想が多い（ザイFX/DZH）。ブイチッチECB副総裁は「2027年の追加利上げを織り込むのは不合理ではない」と述べたが、ユーロ買いは続かなかった（みんかぶ）。'
        'オプション市場では1.10ドル割れが続く展開を見込むポジションが増えている（みんかぶ）。ユーロ円は10月の年初来安値175.05円付近に接近（みんかぶ）。',
    ),
    (
        'ウォーシュFRB議長はAIの講演で金融政策に触れず。ハマック総裁は段階的な利上げを支持',
        'ウォーシュ議長は講演で、FRBがAIの米経済への影響について3つのシナリオ（生産性向上による好況、雇用喪失との相殺、期待外れによる株安と景気減速）の検討を始めたと説明。金融政策への言及はなかった（みんかぶ・ザイFX/DZH一致）。'
        'ハマック・クリーブランド連銀総裁は「小幅かつ段階的な利上げ」を改めて支持（みんかぶ）。シュミッド・カンザスシティ連銀総裁も「インフレは高すぎる、FRBはやるべきことがまだたくさんある」と述べた（みんかぶ）。'
        '先週の米CPI上振れとFRB高官のタカ派発言で、市場は来年までにあと3回超の利上げを見込む（みんかぶ）。',
    ),
    (
        'カナダCPIは下振れ、原油は3%安。マックレムBOC総裁は来年6月に退任',
        'カナダ10月CPIは前月比+0.2%（予想+0.3%）、前年比+3.1%（予想+3.2%、前回+3.1%）と予想を下回った（みんかぶ）。BOCの12/9追加利上げ観測を弱める内容。'
        'WTI原油12月限は85.72ドル（-3.21%）で続落（みんかぶ）。週末にイランがバーレーンを攻撃したと伝わったが、供給過剰に焦点が集まった（ザイFX/フィスコ・みんかぶ）。'
        'マックレム・カナダ中銀総裁は、7年の任期が満了する来年6月に退任する（みんかぶ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/17火）への引継ぎ：ドル円は159.36円、ユーロドルは1.0991ドルで引けた（ザイFX/フィスコ）。ドル高の地合い（ドル指数は年初来高値圏）は続いているが、ドル円だけは株安の円買いと介入警戒で上値が重い。'
    '本日22:30の米10月小売売上高は前月比 予想+0.1%（前回+0.8%）、除自動車 予想+0.4%（前回+0.9%）（KissFX・FF一致）。上振れなら12月利上げ観測が強まりドル買い、下振れなら前日のNY連銀指数に続く弱さでドル売り。'
    'その後23:10のウォラー理事（大幅利上げに言及した理事、みんかぶ）、23:30のハマック総裁の発言。米株引け後のエヌビディア決算は株価を通じてクロス円を動かす。'
    'KissFXは「米ドル・日本円・ユーロの方向性、為替介入への警戒、AI投資への不安」を焦点に挙げる。明日18日はFOMC議事要旨と英CPI。'
)

POINTS_EVENTS = [
    '07:50 🇦🇺 豪 ブロックRBA総裁の発言（Kiss/FF一致・Kiss◎・FF区分:高）',
    '09:30 🇦🇺 豪 RBA議事録（11/2-3会合分）（Kiss/FF一致・Kiss◎）',
    '11:00 🇳🇿 NZ RBNZ 期待インフレ率（FFのみ・要確認・FF区分:高）前回2.34%',
    '16:00 🇬🇧 英 雇用統計：失業率 予想4.7%、平均賃金(3か月) 予想3.5%（Kiss◎・前回失業率はKiss 4.4%、FF・フィスコ 4.7%で不一致・要確認）',
    '19:00 🇩🇪 独 ZEW景況感調査 予想28.8（Kiss/FF一致・Kiss○）',
    '22:30 🇺🇸 米 小売売上高 前月比 予想+0.1%／除自動車 予想+0.4%（Kiss/FF一致・KissランクS）',
    '23:10 🇺🇸 米 ウォラーFRB理事の発言（Kiss/FF一致・KissランクAA）',
    '23:15 🇺🇸 米 鉱工業生産 予想+0.1%（Kiss）／0.0%（FF）で不一致・要確認（KissランクA）',
    '23:30 🇺🇸 米 ハマック・クリーブランド連銀総裁の発言（Kiss/FF一致・KissランクAA）',
    '28:25 🇺🇸 米 ウィリアムズNY連銀総裁の発言（Kiss/FF一致・KissランクAA）',
    '米株引け後 🇺🇸 米 エヌビディア決算（KissFXのみ・KissランクS）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：小売売上高と159.35円',
        '4時間足は上昇トレンドだが、11/12・11/13に160円台で押し戻され、11/16は159.36円まで下げた（ザイFX・みんかぶ）。15分・30分足では159.35円を割ると下げが広がりやすく、守れば押し目買いの水準。'
        '22:30の小売売上高が上振れれば米金利上昇でドル買い、ただし160円手前は介入警戒で上値が重い。米大手銀ストラテジストは年末までに152円への下落を予想（みんかぶ）。',
    ),
    (
        'ユーロドル：1.10ドル割れの定着',
        '11/16は1.0991ドルで引けた（ザイFX/フィスコ）。1.10ドルを下抜けると明確な支持水準が見当たらず、下げが加速しやすい（みんかぶテクニカル）。日足RSIは32.2と売られ過ぎ水準に接近（みんかぶ）。4Hランキング2位。戻りは1.1030ドル前後（11/16 NY高値1.1031ドル、ザイFX/フィスコ）が売り場の目安。',
    ),
    (
        '豪ドル：ブロック総裁とRBA議事録',
        'RBAは11/3に25bp利上げして4.85%、6対3の票割れだった（前日確認分）。議事録で追加利上げに前向きな委員の数が材料。豪ドル円は株安で107.30円まで下落しており（ザイFX/DZH）、エヌビディア決算後の株価にも左右される。',
    ),
    (
        'ポンド：雇用統計と英CPI',
        '市場は12/17の英MPCでの利上げを約8割織り込む（みんかぶ）。16:00の雇用統計で賃金の伸びが鈍れば、利上げ期待の後退でポンド売り。ポンドドルは10月安値1.3135ドルが次の目安（みんかぶ）。',
    ),
    (
        '市場休場：なし',
        '本日11/17（火）は主要市場の休場なし（KissFXの主要国休場日一覧・ForexFactory JSONで一致）。次の休場は11/23日本、11/26米国（KissFX）。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('02:00', '🇺🇸 米', '【発表済み】ウォーシュFRB議長 発言（前日26:00開始分・金融政策への言及なし）', '高', '要人発言', '—'),
    ('04:15', '🇺🇸 米', '【発表済み】ハマック・クリーブランド連銀総裁 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('05:00', '🇳🇿 NZ', '【発表済み】RBNZ金融安定報告書（FF。Kissは前日29:00表記で一致）', '低', '—', '—'),
    ('06:45', '🇳🇿 NZ', '【発表済み】食品価格指数 前月比（FFのみ・要確認）', '低', '—', '0.0%'),
    ('07:50', '🇦🇺 豪', 'ブロックRBA総裁 発言（Kiss/FF一致）', '◎（FF高）', '要人発言', '—'),
    ('08:10', '🇺🇸 米', 'バーキン・リッチモンド連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('08:30', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('09:30', '🇦🇺 豪', 'RBA議事録（11/2-3会合分）（Kiss/FF一致）', '◎', '—', '—'),
    ('11:00', '🇳🇿 NZ', 'RBNZ 期待インフレ率 2年先（FFのみ・要確認）', '（FF高）', '—', '2.34%'),
    ('13:30', '🇯🇵 日', '第3次産業活動指数 前月比（Kiss/FF/フィスコ一致）', '×', '+0.1%', '-0.1%'),
    ('16:00', '🇬🇧 英', 'ILO失業率（Kiss/FF一致・前回はKiss 4.4%、FF・フィスコ 4.7%で不一致・要確認）', '◎', '4.7%（FF・フィスコ）', '4.7%（Kiss 4.4%）'),
    ('16:00', '🇬🇧 英', '失業保険申請件数（Kiss/FF一致）', '◎', '2.54万件（FF）', '3.03万件'),
    ('16:00', '🇬🇧 英', '平均賃金 3か月前年比（FFのみ・要確認）', '（FF中）', '3.5%', '3.7%'),
    ('19:00', '🇩🇪 独', 'ZEW景況感調査（Kiss/FF一致・フィスコ予想28.2）', '○', '28.8', '28.1'),
    ('19:00', '🇪🇺 欧', 'ZEW景況感調査（Kiss/FF一致）', '△', '19.1（FF）', '18.5'),
    ('19:00', '🇪🇺 欧', '欧州委員会 経済見通し（FFのみ・要確認）', '（FF低）', '—', '—'),
    ('19:00', '🇨🇦 加', '中古住宅販売件数 前月比（KissFXのみ・要確認）', '△', '—', '-2.3%'),
    ('21:30', '🇺🇸 米', 'ムサレム・セントルイス連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('22:15', '🇨🇦 加', '住宅着工件数（Kiss/FF一致・予想はKiss 24.00万件、FF 24.1万件）', '○', '24.00万件', '24.89万件'),
    ('22:15', '🇺🇸 米', 'ADP週次雇用者数（FFのみ・要確認）', '（FF低）', '—', '1.98万人'),
    ('22:30', '🇨🇦 加', '国際証券取扱高（Kiss/FF一致）', '×', '148.5億（FF）', '-173.1億'),
    ('22:30', '🇺🇸 米', '小売売上高 前月比（Kiss/FF一致・フィスコ予想+0.2%）', 'S', '+0.1%', '+0.8%'),
    ('22:30', '🇺🇸 米', '小売売上高 除自動車 前月比（Kiss/FF一致）', 'S', '+0.4%', '+0.9%'),
    ('22:30', '🇺🇸 米', '輸入物価指数 前月比（Kiss/FF/フィスコ一致）', 'BB', '+0.7%', '+1.1%'),
    ('23:10', '🇺🇸 米', 'ウォラーFRB理事 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('23:15', '🇺🇸 米', '鉱工業生産 前月比（Kiss/FF一致・予想はKiss・フィスコ +0.1%、FF 0.0%で不一致・要確認）', 'A', '+0.1%（FF 0.0%）', '+0.7%'),
    ('23:15', '🇺🇸 米', '設備稼働率（Kiss/FF一致）', 'B', '76.8%', '76.9%'),
    ('23:30', '🇺🇸 米', 'ハマック・クリーブランド連銀総裁 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('24:00', '🇺🇸 米', '企業在庫 前月比（Kiss/FF/フィスコ一致）', 'C', '+0.5%', '+0.4%'),
    ('24:00', '🇺🇸 米', 'NAHB住宅市場指数（Kiss/FF/フィスコ一致）', 'C', '29', '29'),
    ('24:50', '🇳🇿 NZ', 'GDT乳製品価格指数（FFのみ・要確認）', '（FF低）', '—', '3.0%'),
    ('28:25', '🇺🇸 米', 'ウィリアムズNY連銀総裁 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('29:30', '🇺🇸 米', 'API週間石油在庫（FFのみ・要確認）', '（FF低）', '—', '—'),
    ('米株引け後', '🇺🇸 米', 'エヌビディア決算（KissFXのみ・要確認）', 'S', '大手企業決算', '—'),
    ('翌06:45', '🇳🇿 NZ', '第3四半期 生産者物価指数 産出 前期比（Kiss/FF一致）', '○', '+1.1%（FF）', '+1.6%'),
    ('翌06:45', '🇳🇿 NZ', '第3四半期 生産者物価指数 投入 前期比（FFのみ・要確認）', '（FF低）', '+1.5%', '+2.9%'),
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
          <h3>📰 前日の相場振り返り（2026-11-16 月）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間（24時以降は翌日）。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。重要度はKissFXランク（米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×）を優先し、KissFXにない項目はForexFactory区分を（FF高・中・低）で表示。予想値の第3ソースとしてザイFX/フィスコの本日のスケジュールも参照。【発表済み】は本日0時〜7時に実施済みの項目。「翌」は翌日（11/18水）の日本時間。冬時間のため米東部時間+14時間で換算。</p>
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
