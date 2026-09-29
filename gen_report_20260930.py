# -*- coding: utf-8 -*-
"""FX日報 2026-09-30（水）生成スクリプト"""
import glob, os

TODAY = '2026-09-30'
WEEKDAY = '水'

HERO_TITLE_SUB = (
    '前営業日9/29（火）はNY市場で米10年債利回りが5.291％と2007年以来の高水準に達してドル買いが進み、ユーロドルは1.1312ドルと昨年5月以来の安値を付けた。'
    'ドル円は日米当局の円安けん制に上値を抑えられ、156円98銭〜157円72銭で157円29銭引け。RBAは0.25％利上げの4.60％としたが、総裁会見で据え置きも検討したと明かされ豪ドルが下落した。'
    '本日9/30（水）は月末・四半期末の最終営業日（カナダは休場）。10:30の豪CPI、21:15のADP雇用統計、21:30のPCEコア・デフレーターと米GDP確報値が焦点となる。'
)

SUMMARY_HEADLINE = (
    '米10年債利回り5.29％でドルが全面高、ドル円は当局けん制で157円台に張り付く。本日は月末・四半期末に豪CPI、ADP、PCEが集中'
)

SUMMARY_BODY = (
    '9/29（火）のドル円は東京昼過ぎに157円21銭まで下げた後、NY時間に米10年債利回りが5.291％まで上昇して157円72銭まで戻したが、日通し高値を超えられず157円29銭で引けた（前営業日比10銭安）。'
    '片山財務相が「一般的に言って円の過小評価は懸念材料」と述べ、日米当局の緊密な連携を強調したことが上値を抑えている。'
    '米消費者信頼感指数は81.9（予想89.0）と2014年4月以来の低水準、JOLTS求人件数は707.9万件（予想722.8万件）と3月以来の低水準となり、米10年債利回りは5.22％台へ低下した。'
    'ユーロドルは1.1312ドルの年初来安値を更新し、終値は1.1342ドルだった。'
    '本日9/30（水）は21:15のADP雇用統計、21:30のPCEコア・デフレーターと第2四半期GDP確報値で10月の米追加利上げ観測が動く。'
)

TOP_PAIR_BODY = (
    'ドル円は157円29銭前後（朝7時時点、円建てCME先物報道ベース）。上値は日米当局の円安けん制で157円台後半が抑えられ、下値は米10年債利回り5％台前半〜後半のドル買いで156円台後半が支えられている。'
    '本日は21:15のADP雇用統計（予想+7.4万人、前回+3.8万人）と21:30のPCEコア・デフレーター（前月比予想+0.3％、前回+0.2％）が米金利を動かす最大材料となる。'
    '前日は弱い米指標でも米10年債利回りは5.24％までしか下がらず、ドル高の地合いは崩れていない。'
    '4時間足の直近ランキング（9/29 08:52 JST時点・本日分は未更新）ではUSD/JPYがスコア67・判定「適」・ADX24.2・方向はレンジだった。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    '月末・四半期末のフィキシング（日本時間24時）に加え、19:00には財務省の為替介入実績（8/27〜9/28分）の公表が予定されている（KissFXのみ・要確認）。'
    '10:30の豪CPIはRBAの追加利上げ判断に直結する。米国時間はADP、PCE、GDP確報値が21:15〜21:30に集中し、深夜にはFRB高官発言が続く。カナダは祝日で流動性が細る。'
)

KEY_EVENTS_COUNT = '7件'
KEY_EVENTS_SUMMARY = (
    '豪CPI(10:30) / 介入実績公表(19:00・要確認) / 米ADP雇用統計(21:15) / 米PCE・GDP確報値(21:30) / '
    '米シカゴPMI(22:45) / 米週間原油在庫(23:30) / クックFRB理事発言(10/1 04:25・要確認)'
)

MARKET_OVERVIEW = (
    '前営業日は米長期金利の急上昇がドル全面高を主導した。米10年債利回りは5.291％、30年債利回りは2002年以来の水準まで上昇し、'
    'ユーロドルは1.1312ドル（昨年5月29日以来）、ポンドドルは1.3202ドル（6月下旬以来）、豪ドル米ドルは0.6966ドル（7月30日以来）まで下落した。'
    'ドル円だけは日米当局の円安けん制で上値が抑えられ、156円98銭〜157円72銭の約74pipsにとどまった。'
    'WTI原油はサウジの主要パイプライン修復と米戦略石油備蓄の追加放出で89ドル台まで下落したが、米金利の上昇は止まらなかった。'
    'ドル円1カ月物のインプライド・ボラティリティは9.02％から8.91％へ低下し、リスクリバーサルは円コール優位が続く。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、BOE 3.75％、ECB 2.50％、RBA 4.60％（9/29に0.25％利上げ・みんかぶの東京為替概況ベースで他ソース未確認・要確認）。'
    'ウィリアムズNY連銀総裁は「年内にあと1回の利上げが適切となり得る」と述べ、9月に利上げした以上は性急に動く必要はないとも発言した。'
    '<br><br><strong>今週の焦点：</strong> 9月30日の月末・四半期末（米ADP・PCE・GDP確報値、豪CPI、介入実績公表）、10月1日の日銀短観・ISM製造業、10月2日の米雇用統計（9月分）。'
)

RANKING_ROWS = [
    (1, 'AUD/JPY', 'rank-a', 'A', '直近スコア71・適。ADX32.7、ADR比94.5％、方向は下降。10:30の豪CPI（予想+4.1％、前回+3.5％）が最大の材料。総裁会見後に109円83銭まで下落済み', 'trend-down', '↓'),
    (2, 'USD/JPY', 'rank-a', 'A', '直近スコア67・適。ADX24.2、ADR比112.0％、方向はレンジ。21:15のADPと21:30のPCE、19:00の介入実績公表で値幅が出る', 'trend-range', '→'),
    (3, 'EUR/JPY', 'rank-b', 'B', '直近スコア62・候補。ADX20.6、ADR比99.4％、方向は下降。ユーロドルの年初来安値更新で178円台前半まで下落', 'trend-down', '↓'),
    (4, 'GBP/JPY', 'rank-b', 'B', '直近スコア61・候補。ADX26.0、ADR比88.4％、方向は下降。15:00の英GDP改定値と18:30のFPC議事録が材料', 'trend-down', '↓'),
    (5, 'EUR/USD', 'rank-b', 'B', '直近スコア59・候補。ADX35.7、ADR比69.5％、方向は下降。1.1312ドルの年初来安値を割り込むかが焦点で、21:00の独CPI速報値が材料', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/9/29 08:52 JST生成分（本日分は未更新のため前営業日データ・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、重要イベント前後はスプレッド拡大と急変に注意する。'
)

TOPICS = [
    (
        '米10年債利回りが5.291％まで上昇、2007年以来の高水準でドル全面高',
        '米10年債利回りは5.291％と2007年初旬以来の高水準に達し、30年債利回りも2002年以来の水準まで上昇した。'
        '高インフレの長期化を警戒した長期金利の上昇でドル買いが優勢となり、ユーロドルは1.1312ドルと昨年5月29日以来の安値、'
        'ポンドドルは1.3202ドルと6月下旬以来の安値、豪ドル米ドルは0.6966ドルと7月30日以来の安値まで下落した。'
        'ドル指数は7月29日以来のドル高水準となった。',
    ),
    (
        'RBAが0.25％利上げの4.60％へ、総裁会見で据え置きも検討と判明し豪ドル下落',
        '13:30にRBAは政策金利を市場予想通り4.35％から4.60％へ引き上げ、声明で「インフレ率は依然として高止まりしている」「必要に応じて政策金利をさらに引き上げる」と表明した。'
        'しかし14:30のブロック総裁会見で今回は0.25％利上げと据え置きの両方を検討したと明かされ、想定よりハト派と受け止められた。'
        '豪ドル米ドルは0.7020ドル前後から0.6978ドルへ、豪ドル円は110円50銭前後から109円83銭へ下落した。',
    ),
    (
        '米消費者信頼感指数とJOLTSが大幅悪化、ドル円は157円台で反応限定',
        'コンファレンスボードの9月消費者信頼感指数は81.9（予想89.0、8月88.6）と2014年4月以来の低水準、8月JOLTS求人件数は707.9万件（予想722.8万件、7月733.5万件）と3月以来の最低となった。'
        '求人件数の失業者1人当たりは1.01件（7月1.06件）へ悪化した。米10年債利回りは5.265％前後から5.24％、さらに5.22％台へ低下したが、ドル円は157円45銭近辺にとどまり反応は限定的だった。'
        'ウィリアムズNY連銀総裁が「年内にあと1回の利上げが適切となり得る」と述べたことも、ドルの下げを抑えた。',
    ),
    (
        '片山財務相が円の過小評価を問題視、日米当局が円安けん制を継続',
        '片山財務相は「日米財務当局は緊密にコミュニケーションを維持しており、一般論として円の過小評価は問題である点を米国とも再確認した」と述べた。'
        'ドル円は東京時間に157円21銭〜157円58銭、NY時間に156円98銭〜157円72銭で推移し、日通し高値157円72銭を上抜けられなかった。'
        'アナリストは日銀が10月に2会合連続で利上げする可能性を金利市場が通常より高く織り込んでいると指摘している。',
    ),
    (
        '原油が反落しWTIは89ドル台へ、ユーロは景況感悪化とラガルド発言で売られる',
        'サウジアラビアの主要パイプライン修復が進んだことと米戦略石油備蓄の追加放出で、NY原油先物は反落し89ドル台前半まで下げた。'
        'ホルムズ海峡再開を巡ってはイランが米国にイラン港閉鎖の解除などを条件に求め、トランプ政権はイランの核保有を認めない立場を崩さず、見解の隔たりが残っている。'
        'ユーロ圏9月景況感指数が予想外に悪化し、前日のラガルドECB総裁発言でECBの利上げ観測が後退したことからユーロ売りが優勢となり、ユーロ円は178円11銭まで下落した。'
        'バーナム英首相が労働党大会でEU離脱は害の方が大きかったと述べたことも、ポンドドルの下げ（1.3252ドルから1.3202ドル）の一因としてザイFXが伝えた（要確認）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（9/30水）への引継ぎ：ドル円は157円29銭、ユーロドルは1.1342ドル、ユーロ円は178円40銭、WTI原油は89ドル台で前営業日を終えた。'
    '東京時間は8:50の日本鉱工業生産・小売売上高と10:30の豪CPIが円と豪ドルを動かし、'
    '欧州時間は21:00の独CPI速報値、米国時間は21:15のADP雇用統計と21:30のPCEコア・デフレーター・米GDP確報値が10月の米追加利上げ観測を左右する。'
    'ドル円は日米当局のけん制で157円台後半が抑えられ、米10年債利回り5％台前半のドル買いが下値を支える構図が続く。'
)

POINTS_EVENTS = [
    '08:50 🇯🇵 日本 鉱工業生産・速報値（前月比 予想+1.3％/+1.4％、前回-0.2％/+0.1％）',
    '10:30 🇦🇺 豪州 消費者物価指数（前年比 予想+4.1％、前回+3.5％）',
    '19:00 🇯🇵 日本 外国為替平衡操作実施状況の公表（8/27〜9/28分・要確認）',
    '21:00 🇪🇺 ドイツ 消費者物価指数・速報値（前月比 予想+0.5％、前回+0.2％）（要確認）',
    '21:15 🇺🇸 米国 ADP雇用統計（予想+7.4万人、前回+3.8万人）',
    '21:30 🇺🇸 米国 PCEコア・デフレーター（前月比 予想+0.3％、前回+0.2％）・個人所得・個人支出',
    '21:30 🇺🇸 米国 第2四半期GDP確報値（予想+1.5％、前回+1.5％）',
    '22:45 🇺🇸 米国 シカゴ購買部協会景気指数（予想51.0〜51.2、前回47.1）',
    '23:30 🇺🇸 米国 週間原油在庫（EIA）',
    '10/1 04:25 🇺🇸 米国 クックFRB理事 発言（投票権あり・要確認）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        '豪CPIはRBAの追加利上げ判断に直結',
        'KissFX・ForexFactoryともに豪CPI（前年比）の予想は+4.1％（前回+3.5％）、前月比は+0.5％（前回+1.0％）。RBAは前日に「必要に応じて追加利上げ」と表明した一方、総裁が据え置きも検討したと明かしている。'
        '予想を上回れば追加利上げ観測で豪ドル買い、下回れば据え置き観測が強まり豪ドル売りとなる。豪ドル円・豪ドル米ドルは10:30に値幅が出る。',
    ),
    (
        'ドル円は米金利のドル買いと日米当局のけん制の綱引き',
        '米10年債利回りは5.22〜5.29％で推移し、ドル円は157円台後半で抑えられ、156円台後半で支えられている。'
        '21:15のADPと21:30のPCEコア・デフレーターが上振れれば米10年債利回りが5.29％を再び試しドル円は157円台後半、下振れなら米追加利上げ観測が後退し156円台への下落が優勢となる。'
        '19:00の介入実績公表（要確認）で介入の有無が確認されれば、円買いの反応も出る。',
    ),
    (
        'ユーロドルは1.1312ドルの年初来安値の防衛が焦点',
        '前営業日にユーロドルは1.1312ドルまで下落し、昨年5月29日以来の安値を付けた。ユーロ圏9月景況感指数の悪化とラガルドECB総裁のハト派寄り発言でユーロが売られている。'
        '21:00のドイツCPI速報値（予想前月比+0.5％、前回+0.2％）が予想を上回ればECBの利上げ観測が戻りユーロ買い、下回れば安値更新となる。',
    ),
    (
        '月末・四半期末フローで日中の値動きが荒くなる',
        '本日は9月末・四半期末の最終営業日で、日本時間24時のロンドン・フィキシングに絡む実需フローが出る。カナダは祝日で休場となり、米国時間の流動性が薄くなる。'
        '米国時間は10/2の雇用統計を控え、ADP・PCE・GDP確報値の結果が米金利を通じてドル全体を動かす。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

# ── 経済指標カレンダー（KissFX × ForexFactory JSON 照合。片方のみは「要確認」） ──
CAL_ROWS = [
    ('00:00', '🇬🇧 英', 'マンMPC委員 発言（要確認）', '中', '要人発言', '—'),
    ('00:00', '🇺🇸 米', 'ボウマンFRB副議長 発言（投票権あり）（要確認）', '高', '要人発言', '—'),
    ('00:30', '🇬🇧 英', 'テイラーMPC委員 発言（要確認）', '中', '要人発言', '—'),
    ('01:40', '🇺🇸 米', 'バーFRB理事 発言（投票権あり）（要確認）', '中', '要人発言', '—'),
    ('02:00', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（要確認）', '中', '要人発言', '—'),
    ('02:20', '🇨🇦 加', 'グラベル加中銀副総裁 発言（要確認）', '低', '要人発言', '—'),
    ('02:30', '🇺🇸 米', 'ムサレム・セントルイス連銀総裁 発言（要確認）', '中', '要人発言', '—'),
    ('03:00', '🇺🇸 米', 'ウィリアムズNY連銀総裁 発言（投票権あり）（要確認）', '高', '要人発言', '—'),
    ('04:00', '🇺🇸 米', 'ウォラーFRB理事 発言（投票権あり）（要確認）', '中', '要人発言', '—'),
    ('05:30', '🇺🇸 米', 'API週間原油在庫（要確認）', '低', '—', '—'),
    ('08:50', '🇯🇵 日', '鉱工業生産・速報値（前月比）', '低', '+1.4%（FF）/ +1.3%（Kiss）', '+0.1%（FF）/ -0.2%（Kiss）'),
    ('08:50', '🇯🇵 日', '小売売上高（前年比）', '低', '+3.3%（FF）/ +3.2%（Kiss）', '+4.0%'),
    ('08:50', '🇯🇵 日', '百貨店・スーパー販売額（要確認）', '低', '—', '+1.4%'),
    ('09:00', '🇳🇿 NZ', 'ANZ企業景況感', '低', '—', '53.7'),
    ('10:30', '🇦🇺 豪', '消費者物価指数（前年比）', '高', '+4.1%', '+3.5%'),
    ('10:30', '🇦🇺 豪', '消費者物価指数（前月比）（要確認）', '高', '+0.5%', '+1.0%'),
    ('10:30', '🇦🇺 豪', 'トリム平均CPI（前月比）（要確認）', '高', '+0.3%', '+0.5%'),
    ('10:30', '🇦🇺 豪', '住宅建設許可件数', '低', '-1.6%（FF）/ -1.0%（Kiss）', '-3.6%'),
    ('10:30', '🇦🇺 豪', '民間部門信用（前月比）', '低', '+0.5%', '+0.6%'),
    ('10:30', '🇨🇳 中', '製造業PMI', '低', '50.1', '49.8'),
    ('10:30', '🇨🇳 中', '非製造業PMI', '低', '49.2', '49.0'),
    ('10:45', '🇨🇳 中', 'RatingDog製造業PMI', '低', '51.7', '51.5'),
    ('10:45', '🇨🇳 中', 'RatingDogサービス業PMI', '低', '51.3', '51.4'),
    ('14:00', '🇯🇵 日', '住宅着工戸数（前年比）', '低', '+6.9%（FF）/ +7.0%（Kiss）', '+8.2%'),
    ('15:00', '🇬🇧 英', '第2四半期GDP・改定値（前期比）', '低', '+0.4%', '+0.4%'),
    ('15:00', '🇬🇧 英', '第2四半期経常収支', '低', '-256億（FF）/ -255億（Kiss）', '-221億'),
    ('15:00', '🇪🇺 独', '輸入物価指数（前月比）', '低', '+0.6%（FF）/ +0.7%（Kiss）', '+0.2%'),
    ('15:00', '🇪🇺 独', '小売売上高（前月比）', '低', '+1.6%（FF）/ +1.5%（Kiss）', '-3.4%'),
    ('15:45', '🇪🇺 仏', '消費者物価指数・速報値（前月比）', '低', '-0.5%', '+0.7%'),
    ('15:45', '🇪🇺 仏', '消費者支出（前月比）', '低', '0.0%', '+0.5%'),
    ('16:55', '🇪🇺 独', '失業者数', '低', '0.0万人（FF）/ +0.10万人（Kiss）', '+0.4万人'),
    ('17:00', '🇨🇭 スイス', 'UBS景気予測（要確認）', '低', '—', '12.1'),
    ('18:00', '🇪🇺 伊', '消費者物価指数・速報値（前月比）（要確認）', '低', '+0.2%', '+0.5%'),
    ('18:30', '🇬🇧 英', 'FPC議事録・声明（要確認）', '中', '—', '—'),
    ('18:42', '🇪🇺 独', '10年債入札（要確認）', '低', '—', '3.39'),
    ('19:00', '🇯🇵 日', '外国為替平衡操作実施状況の公表（8/27〜9/28分）（要確認）', '高', '—', '—'),
    ('21:00', '🇪🇺 独', '消費者物価指数・速報値（前月比）（FFは15:29表記のため時刻要確認）', '中', '+0.5%', '+0.2%'),
    ('21:15', '🇺🇸 米', 'ADP雇用統計', '中', '+7.4万人', '+3.8万人'),
    ('21:30', '🇺🇸 米', 'PCEコア・デフレーター（前月比）', '高', '+0.3%', '+0.2%'),
    ('21:30', '🇺🇸 米', '個人所得（前月比）', '低', '+0.5%', '+0.4%'),
    ('21:30', '🇺🇸 米', '個人支出（前月比）', '低', '+0.8%', '+0.2%'),
    ('21:30', '🇺🇸 米', '第2四半期GDP・確報値', '高', '+1.5%', '+1.5%'),
    ('21:30', '🇺🇸 米', 'GDPデフレーター・確報値', '中', '+6.4%', '+6.4%'),
    ('21:30', '🇺🇸 米', '卸売在庫・速報値（前月比）', '低', '+0.5%（FF）/ +0.4%（Kiss）', '+1.3%'),
    ('21:30', '🇺🇸 米', '財貿易収支（要確認）', '低', '-1163億', '-1188億'),
    ('22:00', '🇨🇭 スイス', 'SNB四半期報告（要確認）', '低', '—', '—'),
    ('22:45', '🇺🇸 米', 'シカゴ購買部協会景気指数', '低', '51.2（FF）/ 51.0（Kiss）', '47.1'),
    ('23:30', '🇺🇸 米', '週間原油在庫', '低', '-190万バレル（FF）/ —（Kiss）', '+296.9万バレル（Kiss）/ +300万バレル（FF）'),
    ('23:30', '🇨🇭 スイス', 'チュディンSNB理事 発言（要確認）', '低', '要人発言', '—'),
    ('26:30 (10/1 02:30)', '🇺🇸 米', 'バーキン・リッチモンド連銀総裁 発言（投票権なし）（要確認）', '中', '要人発言', '—'),
    ('28:25 (10/1 04:25)', '🇺🇸 米', 'クックFRB理事 発言（投票権あり）（要確認）', '高', '要人発言', '—'),
]

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
        <em>水曜日</em>
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
              <li>🇨🇦 カナダ市場休場（先住民との和解の日・KissFX/ForexFactory一致）</li>
              <li>9月月末・四半期末の最終営業日（フィキシング周辺のフローに注意）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-09-29）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">※ 時刻は日本時間です。KissFX・ForexFactory JSONで一致した指標を採用し、片方のみで確認できた項目は「（要確認）」を付記。重要度はForexFactory区分（KissFXのランクは画像表記のため取得不可）。</p>
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
