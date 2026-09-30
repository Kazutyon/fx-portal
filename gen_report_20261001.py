# -*- coding: utf-8 -*-
"""FX日報 2026-10-01（木）生成スクリプト"""
import glob, os

TODAY = '2026-10-01'
WEEKDAY = '木'

HERO_TITLE_SUB = (
    '前営業日9/30（水）のドル円は156円38銭〜157円53銭で157円41銭引け。東京午前は月末フローと原油安・米金利低下で156円38銭まで下落したが、NY時間に米10年債利回りが5.296％へ上昇して157円台へ戻した。'
    '米PCEコア（前年比+3.0％、予想+3.3％）が下振れて10月利上げ確率は70％から35％へ低下したが、米GDP確報値・ADP・シカゴPMIは予想を上回り、ドル売りは続かなかった。'
    '本日10/1（木）は月初・四半期初めで、8:50の日銀短観、23:00の米ISM製造業景況指数と多数のFRB高官発言が焦点となり、翌10/2に米雇用統計を控える。'
)

SUMMARY_HEADLINE = (
    'PCE下振れでも米10年債利回りは5.30％に上昇しドル円は157円台を維持。本日は日銀短観・米ISM・FRB高官発言、明日は米雇用統計'
)

SUMMARY_BODY = (
    '9/30（水）のドル円は東京午前に157円46銭から156円38銭へ下落し、月末フロー主導の円買いとなった。東京午後に157円台へ反発し、21:30の米PCEコア・デフレーター（前年比+3.0％、予想+3.3％）で156円台後半へ押し戻されたが、米10年債利回りが5.296％へ上昇して157円41銭で引けた。'
    'ADP雇用者数は+9.0万人（予想+7.0万人）、米第2四半期GDP確報値は+2.2％（予想+1.5％）、シカゴPMIは58.8（予想51.2）と強く、FRBの追加利上げ観測は根強い。'
    '財務省は8/27〜9/28の為替介入額がゼロ円だったと公表した。'
    '本日10/1（木）は8:50の日銀短観（大企業製造業DI予想+25）と23:00の米ISM製造業景況指数（予想54.8〜55.0）が最大の材料で、10/2の米雇用統計前にドル円は157円台での攻防となる。'
)

TOP_PAIR_BODY = (
    'ドル円は157円38銭前後（朝7時台、みんかぶ東京為替ベース）。上値は日米当局の円安けん制が意識される157円台半ば、下値は米10年債利回り5.2％台のドル買いで156円台前半が支えられている。'
    '8:50の日銀短観（大企業製造業DI予想+25、前回+22）が予想を上回れば日銀の利上げペース加速観測で円買い、下回れば円売りとなる。'
    '21:30の米新規失業保険申請件数（予想20.0万件）と23:00のISM製造業景況指数（予想54.8〜55.0、前回54.6）が米金利を通じてドル円を動かす。'
    '4時間足ランキング（9/30 08:04 JST生成・本日分は未更新）ではUSD/JPYはスコア59・判定「候補」・ADX20.1・方向はレンジだった。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    '日銀短観（8:50）は日銀の利上げペースの判断材料となる。米国時間は21:30の新規失業保険申請件数、23:00のISM製造業景況指数、22:30のラガルドECB総裁発言に加え、ウォラー、ジェファーソン、ボウマン、クック、ウィリアムズと投票権を持つFRB高官の発言が続く。'
    '香港・中国は祝日で休場（中国は10/7まで）のため、アジア時間の流動性が細る。翌10/2の米雇用統計を控えたポジション調整も出る。'
)

KEY_EVENTS_COUNT = '8件'
KEY_EVENTS_SUMMARY = (
    '日銀短観(08:50) / 豪貿易収支(10:30) / スイスCPI(15:30) / ベイリーBOE総裁発言(17:00) / 米新規失業保険申請件数(21:30) / '
    'ラガルドECB総裁発言(22:30) / 米ISM製造業景況指数(23:00) / ウォラーFRB理事発言(23:00)'
)

MARKET_OVERVIEW = (
    '前営業日は米PCEの下振れと米長期金利の上昇が交錯した。米10年債利回りは5.296％（+0.059）、30年債利回りは5.638％（+0.072）まで上昇し、2年債利回りは4.893％（+0.017）で2-10年スプレッドは+40bpへスティープ化した。'
    'PCE価格指数（前年比+3.4％、予想+3.7％）とコアPCE（前年比+3.0％、予想+3.3％）が下振れ、10月利上げの織り込みは一時70％から35％へ低下したが、来年までの累計1.00％ポイントの利上げ観測は変わっていない。'
    'ユーロドルは1.1322〜1.1380ドルで1.1330ドル引けとなり、16カ月ぶりの安値圏を維持した。ポンドはロンドン時間に英GDP確報値の上方改定で1.3301ドルまで上昇し、ポンド円は208円81銭で引けた。'
    'WTI原油は90.42ドル（+1.04）と反発し、米国とイランの協議停滞が支えとなった。NYダウは下落しナスダックは約1％上昇し、VIXは16.43（+2.37％）だった。金は4186.70ドル（+0.17％）で続伸した。'
    '<br><br><strong>政策金利：</strong> FRB 3.75〜4.00％、日銀 1.25％、BOE 3.75％、ECB 2.50％、RBA 4.60％（9/29利上げ・みんかぶ報道ベースで他ソース未確認・要確認）、RBNZ 2.75％、BOC 2.25％、SNB 0.00％（9/24の結果は複数ソースで未確認・要確認）。'
    '<br><br><strong>今週の焦点：</strong> 10月1日の日銀短観・米ISM製造業景況指数、10月2日の米雇用統計（9月分）。'
)

RANKING_ROWS = [
    (1, 'AUD/JPY', 'rank-a', 'A', '直近スコア78・適。ADX38.5、ADR比99.8％、方向は下降。9/30は109円88銭始値から108円89銭まで下落し109円35銭引け。10:30の豪貿易収支（予想+20.0億豪ドル、前回+19.23億豪ドル）が材料', 'trend-down', '↓'),
    (2, 'EUR/JPY', 'rank-a', 'A', '直近スコア65・適。ADX26.0、ADR比95.2％、方向は下降。9/30は177円34銭まで下げ178円35銭引け。22:30のラガルドECB総裁発言と独仏のインフレ上振れによるECB利上げ観測が材料', 'trend-down', '↓'),
    (3, 'AUD/USD', 'rank-b', 'B', '直近スコア64・候補。ADX39.3、ADR比78.4％、方向は下降。トレンドは強いがADRは5年平均の78％にとどまる。23:00の米ISMで米金利が動く', 'trend-down', '↓'),
    (4, 'USD/JPY', 'rank-b', 'B', '直近スコア59・候補。ADX20.1、ADR比107.3％、方向はレンジ。8:50の日銀短観と23:00の米ISMで値幅が出る', 'trend-range', '→'),
    (5, 'GBP/JPY', 'rank-b', 'B', '直近スコア59・候補。ADX29.2、ADR比80.0％、方向は下降。9/30は206円89銭から208円81銭へ反発。17:00のベイリーBOE総裁発言が材料', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/9/30 08:04 JST生成分（本日分は未更新のため前営業日データ・要確認）。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、重要イベント前後はスプレッド拡大と急変に注意する。'
)

TOPICS = [
    (
        '米PCEが予想を下回り10月利上げ確率は70％から35％へ低下、ただし米10年債利回りは5.296％へ上昇',
        '21:30発表の8月PCE価格指数は前年比+3.4％（予想+3.7％）、コアPCEは前月比+0.2％（予想+0.3％）・前年比+3.0％（予想+3.3％）と下振れた。'
        '短期金融市場の10月利上げ確率は一時70％程度から35％程度へ低下し、米大手証券は次回利上げ予想を10月から12月へ後退させた。'
        'ただしインフレ期待は根強く、来年までの累計1.00％ポイントの利上げ織り込みは変わらず、10年債利回りは5.30％台へ上昇して5.296％（+0.059）で引けた。'
        'ドル円は156円台後半へ下落した後、157円41銭へ買い戻された。',
    ),
    (
        '米GDP確報値・ADP・シカゴPMIは予想を大幅に上回る',
        '第2四半期GDP確報値は前期比年率+2.2％（予想+1.5％）、個人消費は+3.8％（予想+3.4％）、ADP雇用者数は+9.0万人（予想+7.0万人、前回+3.6万人に下方修正）、シカゴPMIは58.8（予想51.2、前回47.1）と強い結果が並んだ。'
        'PCEの下振れ分のドル売りはこれらの強い指標と長期金利の上昇に打ち消され、ドル指数の下落は限定的だった。'
        'エコノミストは、今後の米経済指標が強く10月に利上げして追加引き締めを示唆する場合、ユーロドルは1.10ドルまで下落すると指摘している。',
    ),
    (
        '東京は月末フローで円買い、ドル円は157円46銭から156円38銭へ下落後に反発',
        '東京午前に原油安と米債利回り低下でドル売りが進み、ドル円は月末フロー主導で157円46銭付近から156円38銭付近まで下落した。'
        '東京午後には円買いが一巡して157円台へ反発し、ロンドン時間は156円台後半〜157円付近で推移した。'
        '19:14に財務省は8/27〜9/28の為替平衡操作（介入）の実績をゼロ円と公表した。'
        '1週間物ドル円のインプライド・ボラティリティは10.25％で、円コール・オーバー（円高ヘッジ需要）が拡大した。',
    ),
    (
        '英GDP確報値の上方改定でポンドドルは1.3301ドルへ、ユーロは独仏債利回り格差拡大で上値が重い',
        '15:00の英第2四半期GDP確報値が上方改定され、ポンドドルは1.3223ドル付近から1.3301ドルまで上昇し、ポンド円は206円89銭から208円91銭まで上昇した。'
        '月末・四半期末の実需の買い戻しも押し上げ要因となった。エコノミストはエネルギー価格の上昇が長引けばBOEが追加利上げに動くとの見方が強まりやすいと指摘している。'
        'バーナム英首相は英・EU首脳会議に向けEUへの再加盟を含む選択肢を協議する意向を示し、関係改善期待もポンドの支援材料となった。'
        'ユーロはフランス・イタリア・ドイツ各州のCPI上振れでECB利上げ観測が高まったが、フランスの財政懸念で独仏10年債利回り格差が120bpと14年ぶりの水準に拡大し、ユーロポンドは0.8577付近から0.8540付近へ下落した。',
    ),
    (
        'WTI原油は90.42ドルへ反発、米国とイランの協議停滞が支え',
        'NY原油先物11月限は90.42ドル（+1.04ドル、+1.16％）で引けた。時間外取引で88.58ドルまで下げたが、イランのアラグチ外相がホルムズ海峡の開放などの条件を米国に提示し、米国から回答を受け取った後のイランの反応がなく協議が停滞していることが相場を支え、通常取引序盤に91.96ドルまで上昇した。'
        '金は4186.70ドルで続伸し、予想を下回るPCEが支援要因となったがドル高と米債利回りの上昇で上げ一服となった。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（10/1木）への引継ぎ：ドル円は157円41銭、ユーロドルは1.1330ドル、ユーロ円は178円35銭、ポンド円は208円81銭、豪ドル円は109円35銭で前営業日を終えた。'
    '東京時間は8:50の日銀短観（大企業製造業DI予想+25）と日銀会合の主な意見、10:30の豪貿易収支が円と豪ドルを動かし、'
    '欧州時間は17:00のベイリーBOE総裁発言、米国時間は21:30の新規失業保険申請件数、22:30のラガルドECB総裁発言、23:00の米ISM製造業景況指数が焦点となる。'
    '米10年債利回りが5.3％近辺の高水準にある限りドル円の下値は支えられ、上値は日米当局の円安けん制で抑えられる構図が続く。'
)

POINTS_EVENTS = [
    '08:50 🇯🇵 日本 第3四半期日銀短観（大企業製造業DI 予想+25、前回+22／先行き 予想+22、前回+17／大企業非製造業DI 予想+36、前回+37）',
    '08:50 🇯🇵 日本 日銀金融政策決定会合における主な意見（9/17・18開催分）',
    '10:30 🇦🇺 豪州 貿易収支（予想+20.0億豪ドル、前回+19.23億豪ドル）',
    '15:30 🇨🇭 スイス 消費者物価指数（前月比 予想±0.0％、前回+0.4％）',
    '17:00 🇬🇧 英国 ベイリーBOE総裁 発言',
    '21:30 🇺🇸 米国 新規失業保険申請件数（予想20.0万件（Kiss）/ 20.1万件（FF）、前回19.7万件）',
    '22:30 🇪🇺 ユーロ圏 ラガルドECB総裁 発言',
    '23:00 🇺🇸 米国 ISM製造業景況指数（予想55.0（Kiss）/ 54.8（FF）、前回54.6）',
    '23:00 🇺🇸 米国 ウォラーFRB理事 発言（投票権あり）',
    '26:30 (10/2 02:30) 🇺🇸 米国 ジェファーソンFRB副議長 発言（投票権あり）',
    '28:00 (10/2 04:00) 🇺🇸 米国 ボウマンFRB副議長 発言（投票権あり）',
    '28:30 (10/2 04:30) 🇺🇸 米国 クックFRB理事・ウィリアムズNY連銀総裁 発言（投票権あり）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        '日銀短観は日銀の利上げペースの判断材料',
        'エコノミスト予想では大企業製造業DIは+25（前回+22）、先行きは+22（前回+17）。みんかぶによると、エコノミストは植田総裁が政策環境の変化に言及して従来より速いペースでの利上げを示唆しており、今回の短観がその見方を後押しする内容になり得ると指摘している。'
        'DIが予想を上回れば日銀の利上げ加速観測でドル円は157円を割り込み、下回れば日銀の追加利上げ観測が後退して円売りが優勢となる。',
    ),
    (
        '米ISMと雇用統計前のFRB高官発言でドル円の方向が決まる',
        'PCEの下振れで10月利上げ確率は35％まで低下したが、GDP・ADP・シカゴPMIが強く、累計1.00％ポイントの利上げ織り込みは変わっていない。'
        '23:00のISM製造業景況指数（予想54.8〜55.0）が予想を上回れば米10年債利回りは5.3％台を維持してドル円は157円台半ばを試し、下回れば米金利低下でドル円は156円台前半への下落が優勢となる。'
        'ウォラー、ジェファーソン、ボウマン、クック、ウィリアムズと投票権を持つ高官の発言が続き、10月利上げ観測が再び動く。',
    ),
    (
        'ユーロドルは16カ月ぶりの安値圏、22:30のラガルドECB総裁発言が材料',
        'ユーロドルは1.1322〜1.1380ドルで推移し、16カ月ぶりの安値圏にある。独仏伊のCPI上振れでECB利上げ観測は高まっているが、独仏10年債利回り格差が120bpと14年ぶりに拡大しフランスの財政懸念がユーロの上値を抑えている。'
        'ラガルド総裁が追加利上げに前向きな発言をすればユーロドルは1.14ドル台へ反発し、利上げに慎重な発言ならば安値更新となる。',
    ),
    (
        '月初・四半期初めのフローと香港・中国休場で流動性が偏る',
        '本日は10月の月初・四半期初めの最初の営業日で、新規の資金フローが出る。香港と中国は祝日で休場（中国は10/7まで）のため、アジア時間の流動性が細り、短観発表後の値動きが大きくなる。'
        '米国時間は翌10/2の雇用統計を控え、ISMの結果を受けたポジション調整が出る。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

# ── 経済指標カレンダー（KissFX × ForexFactory JSON 照合。片方のみは「要確認」） ──
CAL_ROWS = [
    ('02:30', '🇺🇸 米', 'バーキン・リッチモンド連銀総裁 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('04:25', '🇺🇸 米', 'クックFRB理事 発言（FFのみ・要確認）', '低', '要人発言', '—'),
    ('04:30', '🇺🇸 米', 'トランプ大統領 発言（FFのみ・要確認）', '中', '要人発言', '—'),
    ('06:10', '🇺🇸 米', 'グールズビー・シカゴ連銀総裁 発言（投票権なし）', '低', '要人発言', '—'),
    ('06:45', '🇳🇿 NZ', '住宅建設許可件数', '低', '—', '-4.3%'),
    ('07:00', '🇺🇸 米', 'カシュカリ・ミネアポリス連銀総裁 発言（投票権あり）', '中', '要人発言', '—'),
    ('08:01', '🇨🇳 中', '中国 祝日（市場休場・10/7まで。Kiss「香港と中国は休場」/ FF Bank Holiday）', '低', '—', '—'),
    ('08:50', '🇯🇵 日', '第3四半期日銀短観 大企業製造業 業況判断DI', '中', '+25', '+22'),
    ('08:50', '🇯🇵 日', '第3四半期日銀短観 大企業製造業 先行き（Kissのみ・要確認）', '中', '+22', '+17'),
    ('08:50', '🇯🇵 日', '第3四半期日銀短観 大企業非製造業 業況判断DI', '中', '+36', '+37'),
    ('08:50', '🇯🇵 日', '第3四半期日銀短観 大企業非製造業 先行き（Kissのみ・要確認）', '中', '+30', '+28'),
    ('08:50', '🇯🇵 日', '第3四半期日銀短観 設備投資計画（Kissのみ・要確認）', '中', '+12.3%（Kiss）/ +12.2%（みんかぶ）', '+11.5%'),
    ('08:50', '🇯🇵 日', '日銀金融政策決定会合における主な意見（9/17・18開催分）', '低', '—', '—'),
    ('09:30', '🇯🇵 日', '製造業PMI・確報値（FFのみ・要確認）', '低', '54.1', '54.1'),
    ('10:30', '🇦🇺 豪', '貿易収支', '低', '+20.0億豪ドル', '+19.2億豪ドル'),
    ('10:30', '🇦🇺 豪', 'RBA金融安定性レビュー（FFのみ・要確認）', '低', '—', '—'),
    ('15:00', '🇬🇧 英', 'ネーションワイド住宅価格（前月比）', '低', '±0.0%', '+0.2%'),
    ('15:30', '🇨🇭 スイス', '消費者物価指数（前月比）', '中', '±0.0%', '+0.4%（FF）/ +1.0%（Kiss）要確認'),
    ('15:30', '🇨🇭 スイス', '小売売上高（前年比）', '低', '+2.1%（FF）/ —（Kiss）', '+2.3%'),
    ('15:30', '🇦🇺 豪', '商品価格（前年比）（FFのみ・要確認）', '低', '—', '+15.5%'),
    ('16:15', '🇪🇺 西', '製造業PMI（FFのみ・要確認）', '低', '50.2', '49.5'),
    ('16:30', '🇨🇭 スイス', '製造業PMI', '低', '56.3', '57.1'),
    ('16:45', '🇪🇺 伊', '製造業PMI（FFのみ・要確認）', '低', '50.1', '49.6'),
    ('16:50', '🇪🇺 仏', '製造業PMI・改定値', '低', '50.3', '50.3'),
    ('16:55', '🇪🇺 独', '製造業PMI・改定値', '低', '53.8', '53.8'),
    ('17:00', '🇪🇺 ユーロ圏', '製造業PMI・改定値', '低', '52.7', '52.7'),
    ('17:00', '🇬🇧 英', 'ベイリーBOE総裁 発言', '中', '要人発言', '—'),
    ('17:00', '🇪🇺 伊', '失業率（FFのみ・要確認）', '低', '5.8%', '5.8%'),
    ('17:30', '🇬🇧 英', '製造業PMI・改定値', '低', '52.0', '52.0'),
    ('18:00', '🇪🇺 ユーロ圏', '失業率', '低', '6.4%', '6.4%'),
    ('18:03', '🇪🇺 西', '10年債入札（FFのみ・要確認）', '低', '—', '3.96%'),
    ('18:18', '🇪🇺 仏', '10年債入札（FFのみ・要確認）', '低', '—', '4.23%'),
    ('18:30', '🇺🇸 米', 'チャレンジャー人員削減予定数', '低', '—', '-38.5%'),
    ('19:35', '🇪🇺 独', 'ナーゲル独連銀総裁 発言', '低', '要人発言', '—'),
    ('21:00', '🇬🇧 英', 'マンMPC委員 発言', '低', '要人発言', '—'),
    ('21:30', '🇺🇸 米', '新規失業保険申請件数', '中', '20.0万件（Kiss）/ 20.1万件（FF）', '19.7万件'),
    ('22:05', '🇺🇸 米', 'バーキン・リッチモンド連銀総裁 発言（投票権なし）', '低', '要人発言', '—'),
    ('22:05', '🇺🇸 米', 'コリンズ・ボストン連銀総裁 発言（投票権なし）', '低', '要人発言', '—'),
    ('22:05', '🇺🇸 米', 'シュミッド・カンザスシティ連銀総裁 発言（投票権なし）', '低', '要人発言', '—'),
    ('22:30', '🇨🇦 加', '製造業PMI（FFのみ・要確認）', '低', '—', '53.0'),
    ('22:30', '🇪🇺 ユーロ圏', 'ラガルドECB総裁 発言', '中', '要人発言', '—'),
    ('22:45', '🇺🇸 米', '製造業PMI・改定値', '低', '57.0（Kiss）/ 56.9（FF）', '57.0'),
    ('23:00', '🇺🇸 米', 'ISM製造業景況指数', '高', '55.0（Kiss）/ 54.8（FF）', '54.6'),
    ('23:00', '🇺🇸 米', 'ISM製造業 支払価格（FFのみ・要確認）', '低', '72.9', '71.1'),
    ('23:00', '🇺🇸 米', '建設支出（前月比）', '低', '±0.0%', '-0.5%'),
    ('23:00', '🇺🇸 米', 'ウォラーFRB理事 発言（投票権あり）', '中', '要人発言', '—'),
    ('23:15', '🇺🇸 米', '新車販売台数（FFのみ・要確認）', '低', '1,630万台', '1,680万台'),
    ('23:30', '🇺🇸 米', '週間天然ガス貯蔵量', '低', '+630億立方フィート（FF）/ —（Kiss）', '+530億立方フィート'),
    ('23:50', '🇬🇧 英', 'ピルMPC委員 発言（Kissのみ・要確認）', '低', '要人発言', '—'),
    ('24:30 (10/2 00:30)', '🇨🇭 スイス', 'シュレーゲルSNB総裁 発言（Kissのみ・要確認）', '低', '要人発言', '—'),
    ('26:30 (10/2 02:30)', '🇺🇸 米', 'ジェファーソンFRB副議長 発言（投票権あり）（Kissのみ・要確認）', '中', '要人発言', '—'),
    ('28:00 (10/2 04:00)', '🇺🇸 米', 'ボウマンFRB副議長 発言（投票権あり）（Kissのみ・要確認）', '中', '要人発言', '—'),
    ('28:30 (10/2 04:30)', '🇺🇸 米', 'クックFRB理事 発言（投票権あり）（Kissのみ・要確認）', '中', '要人発言', '—'),
    ('28:30 (10/2 04:30)', '🇺🇸 米', 'ウィリアムズNY連銀総裁 発言（投票権あり）（Kissのみ・要確認）', '中', '要人発言', '—'),
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
              <li>🇭🇰 香港・🇨🇳 中国市場休場（祝日・中国は10/7まで。KissFX/ForexFactory一致）</li>
              <li>10月月初・四半期初めの最初の営業日（新規フローに注意）</li>
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
          <h3>📰 前営業日の相場振り返り（2026-09-30）</h3>
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
