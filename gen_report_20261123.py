# -*- coding: utf-8 -*-
"""FX日報 2026-11-23（月）生成スクリプト"""
import glob, os

TODAY = '2026-11-23'
WEEKDAY = '月'
PREV_LABEL = '前営業日 2026-11-20 金'

HERO_TITLE_SUB = (
    '前営業日11/20（金）はAI関連株の急落（ナスダック-5.28%、SOX-10.73%）でリスク回避の円買いが強まり、ドル円は159.84円から158.42円まで下げて158.57円で反落。'
    'VIXは37.09へ急上昇。本日11/23（月）は日本が勤労感謝の日で休場、欧英米のPMI速報値と翌06:00のウィリアムズNY連銀総裁の講演が材料。'
)

SUMMARY_HEADLINE = (
    '主役は「AI株安→円買い」。ドル円は158円台半ばで週明け。'
    '今週は25日の米PCEで12月利上げの織り込みを再確認、26日は米感謝祭で薄商い'
)

SUMMARY_BODY = (
    '11/20（金）のドル円は始値159.69円・高値159.84円・安値158.42円・終値158.57円（みんかぶ四本値・ザイFX/DZH終値一致）。'
    '米株はダウ-1.93%、S&amp;P500-3.70%、ナスダック-5.28%で、ダウとS&amp;P500は終値ベースで調整局面入り（みんかぶ）。'
    '米10年債利回りは4.942%（-0.104）と5%を割り込み、日米金利差の縮小もドル円の重し（みんかぶ・ザイFX/フィスコ）。'
    '週明けオセアニア市場のドル円は158.60円前後、レンジ158.51〜158.67円（ザイFX/DZH 06:42）。本日の休場は日本（勤労感謝の日）。'
)

TOP_PAIR_NAME = 'AUD/JPY 🇦🇺🇯🇵'
TOP_PAIR_BODY = (
    '豪ドル円は11/20に始値106.33円から104.73円まで下げ、104.97円引け（みんかぶ四本値、安値はザイFX/DZHと一致）。1日で約1.3%の下落。'
    '下げた理由は2つ。株価急落でリスクに敏感な豪ドルが売られたこと（ザイFX/DZH）と、リスク回避の円買い。加えて11/19の豪雇用統計の悪化で豪ドルは対ドルで年初来安値0.6662ドルを更新済み（みんかぶ）。'
    'CFTCでは豪ドルの売り越しが18万2060枚へ3万307枚増加（11/17時点、みんかぶ）。'
    '4Hランキング1位（スコア71・適、ADX55.8・下降、11/20 10:22生成）。4時間足は下降トレンド。15分・30分足では104.73円（11/20安値）を割るかが戻り売り継続の分かれ目。25日の豪CPIが次の大きな材料。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'VIXスポットは37.09（+8.65、+30.41%、みんかぶ）と急上昇。半導体株指数SOXは-10.73%（ザイFX/フィスコ）。'
    'エヌビディアは「米SECが会計処理を調査」との報道で14%超下落（ザイFX/DZH・みんかぶ）。日経平均は11/20に3,007.56円安の56,436.65円（ザイFX・KissFX）。'
    'ドル円1カ月物オプションの変動率は7.13%→7.49%、25デルタ・リスクリバーサルは円コール優位が+1.46%→+1.81%へ拡大し、円高への備えが加速（ザイFX/フィスコ）。'
    '本日は東京が休場で流動性が薄く、値が飛びやすい。'
)

KEY_EVENTS_COUNT = '7件'
KEY_EVENTS_SUMMARY = (
    'NZ 第3四半期小売売上高(06:45・発表済み)、独 製造業PMI速報(17:30)、欧 製造業PMI速報(18:00)、英 製造業・非製造業PMI速報(18:30)、'
    '米 製造業・非製造業PMI速報(23:45)、米 2年債入札(27:00)、米 ウィリアムズNY連銀総裁(翌06:00)'
)

MARKET_OVERVIEW = (
    '<strong>VIX</strong>：37.09（+8.65、+30.41%）（みんかぶ、NY16:13時点）。investing.comは403で取得できず（要確認）。'
    '<strong>米株（11/20終値）</strong>：ダウ48,147.33ドル（-949.73、-1.93%）、S&amp;P500 6,910.39（-3.70%）、ナスダック22,617.73（-5.28%）、SOX 8,408.59（-10.73%）（みんかぶ・ザイFX/フィスコ・KissFX一致）。'
    '<strong>米債利回り</strong>：2年債4.641%（-0.121）、10年債4.942%（-0.104）、30年債5.330%（みんかぶ）。ザイFX/フィスコは2年4.658%・10年4.948%、KissFXは10年4.950%と引け時刻の差で小差。2-10年差は+30（みんかぶ）。'
    '<strong>ドルインデックス（DXY）</strong>：103.877（-0.018）（ザイFX/フィスコのみ。investing.comは403・要確認）。'
    '<strong>金</strong>：NY金先物12月限3,515.40ドル（-170.10、-4.62%、みんかぶ）。ザイFX/フィスコは3,509.15ドル（-4.78%）で、昨年8月以来の安値・52週安値3,503.35ドルをつけた。株安で利益確定の換金売りが続いた。'
    '<strong>原油</strong>：WTI12月限83.98ドル（+0.93%、みんかぶ）、1月限83.76ドル（+1.60%、ザイFX/フィスコ）。トランプ大統領がイランの提示案を「容認できない」と述べ、対イラン再攻撃への警戒で買い戻された（ザイFX/フィスコ・みんかぶ）。'
    '<br><br><strong>政策金利（11/23確認）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。8中銀とも前週から変更なし、今週も主要国の政策発表はなし（KissFX 11/20クローズ号・前回11/16の公式発表照合）。'
    '<br><br><strong>今週の焦点：</strong> 24日 米消費者信頼感・マックレム加中銀総裁講演、25日 豪CPI・米PCE価格指数（前年比 予想+3.8%、コア+3.2%）・米GDP改定値・ベージュブック、26日 米感謝祭休場・田村日銀委員の懇談会・ECB議事要旨、27日 東京都区部CPI・S&amp;Pの仏格付け見直し（KissFX・みんかぶ・ザイFX）。28日からFRBはブラックアウト期間（みんかぶ）。'
)

RANKING_ROWS = [
    (1, 'AUD/JPY', 'rank-a', 'A', 'スコア71・適。ADX55.8、ADR比90％（5日ADR 80.0pips）、4H方向は下降。11/20は106.33円から104.73円まで下落、104.97円引け（みんかぶ・ザイFX）。株安局面で最も売られやすい組み合わせ。25日の豪CPIが次の材料。', 'trend-down', '↓'),
    (2, 'GBP/JPY', 'rank-b', 'B', 'スコア63・候補。ADX46.3、ADR比75％（5日ADR 108.4pips）、4H方向は下降。11/20は209.20円から207.27円まで下げ207.45円引け（みんかぶ）。英小売売上高の上振れ（前月比+0.7%、予想0.0%）でもポンド円は円買いに押された（みんかぶ）。本日18:30の英PMIが材料。', 'trend-down', '↓'),
    (3, 'USD/CAD', 'rank-b', 'B', 'スコア58・候補。ADX38.0、ADR比71％、4H方向は上昇。11/20終値1.43532（KissFX）。加9月小売売上高は+0.8%（予想+0.7%）で加ドル買い（ザイFX/フィスコ・みんかぶ）。24日のマックレム総裁講演が材料。', 'trend-up', '↑'),
    (4, 'EUR/JPY', 'rank-b', 'B', 'スコア58・候補。ADX39.5、ADR比77％、4H方向はレンジ判定。11/20は173.74円と昨年10月以来の安値、173.92円引け（ザイFX/DZH・みんかぶ）。独仏10年債利回り差は154bpに拡大し仏財政不安が重し（みんかぶ）。', 'trend-range', '→'),
    (5, 'EUR/USD', 'rank-b', 'B', 'スコア57・候補。ADX49.4、ADR比66％、4H方向は下降。11/20は年初来安値1.0953ドル（11/18）手前の1.0957ドルで下げ止まり1.0968ドル引け（ザイFX/DZH）。ナーゲル独連銀総裁は「12月会合で何かをする必要がある」と発言（みんかぶ）。本日17:30〜18:00の独・ユーロ圏PMIが材料。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/11/20 10:22 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため3日前の数値で、11/20の欧米時間の急落は反映されていない。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        'AI関連株の急落でリスク回避：ナスダック-5.28%、SOX-10.73%、VIX 37.09',
        '東京時間に日経平均が3,007.56円安、韓国総合は5%超、台湾加権は6%超下落し（みんかぶ・ザイFX）、欧州でも独DAXが-2.60%（ザイFX/フィスコ）。NYではダウ-949.73ドル、ナスダック-5.28%と下げが広がった（みんかぶ）。'
        '理由は、エヌビディアの好決算とアンソロピックのIPOという好材料を通過した後に「材料出尽くし」の利益確定売りが出たこと。巨額のAI投資をどう収益化するのかという疑問が払拭できていない（みんかぶ）。'
        'さらに「米SECがエヌビディアの会計処理を調査」との報道で同社株が14%超急落した（ザイFX/DZH・みんかぶ）。VIXは37.09（+30.41%、みんかぶ）。',
    ),
    (
        'ドル円は159.84円から158.42円まで下落、158.57円で反落。200日移動平均線を下回る',
        'ドル円は11/19に159.97円まで上げたが160円に届かず、11/20の東京朝に159.84円をつけた後、アジア株急落で円買いが強まった（みんかぶ）。ロンドンでは米10年債利回りの5%割れも重なり200日移動平均線を下回って158.71円付近へ（みんかぶ）。'
        'NYでは5時頃に158.42円まで下げ、終値158.57円（前日比-1.12円、ザイFX/DZH・みんかぶ一致）。'
        'みんかぶは「円はスイスフランを上回る上昇率で、週間でもG10通貨で最も堅調」と伝えた。理由は、リスク回避局面での円の安全通貨としての役割と、日銀の利上げ観測で円を支える金融政策環境（みんかぶ）。',
    ),
    (
        '米ミシガン大の期待インフレ率が大幅に下方修正：大幅利上げ観測が後退し米債利回り低下',
        '11月ミシガン大学消費者信頼感指数（確報値）は51.5（予想51.6、速報値51.0）。1年期待インフレ率は3.7%（予想4.2%、速報値4.3%）と2月以来の低さ、5〜10年期待は3.3%（速報値3.4%）（ザイFX/フィスコ・みんかぶ）。'
        '期待インフレの改善でFOMCの大幅利上げの論拠が弱まり、米国債が買われた。10年債は4.942%（-0.104）、2年債は4.641%（-0.121）（みんかぶ）。'
        '一方、クックFRB理事は「早急に利上げを実施する必要がある」、ポールソン・フィラデルフィア連銀総裁は「連続利上げを検討する用意」と発言し、FRB高官はタカ派一色（みんかぶ）。'
        '12月利上げの織り込みは、20日時点で100%（みんかぶ週末記事）と、NY引け時点で「もはや完全には織り込んでいない」（みんかぶNY概況）で表記が分かれる（要確認）。',
    ),
    (
        'クロス円が全面安：ユーロ円173.74円は1年1カ月ぶり安値、豪ドル円104.73円',
        'ユーロ円は175.35円から173.74円まで下げ173.92円引け（昨年10月以来の安値、ザイFX/DZH・みんかぶ）。ポンド円は207.27円まで下げ207.45円、豪ドル円は104.97円、カナダ円は110.53円引け（みんかぶ四本値）。'
        'ドルストレートは方向感を欠いた。ユーロドルは11/18の年初来安値1.0953ドル手前で買い戻され1.1000ドルまで戻した後、1.0968ドルで引けた（ザイFX/DZH）。ユーロ圏11月消費者信頼感は-16.9（予想-18.0）と改善（ザイFX/フィスコ）。'
        '英10月小売売上高は前月比+0.7%（予想0.0%）と上振れ（みんかぶ）だが、ポンド円は円買いに押された。安全通貨としてスイスフランも買われた（ザイFX/フィスコ）。',
    ),
    (
        '原油は反発、金は4%超の急落：イラン情勢と株安の換金売り',
        'WTIは時間外で80.78ドルまで下げた後、トランプ大統領がイランの提示案を「容認できない」と述べたことで対イラン再攻撃が警戒され、83.76ドル（1月限、+1.60%）で引けた（ザイFX/フィスコ）。'
        'サウジ主導の連合軍によるフーシ派拠点攻撃も伝わった（みんかぶ）。'
        'NY金12月限は3,515.40ドル（-4.62%、みんかぶ）と大幅続落。株安を受けた売りが止まらず、昨年8月以来の安値（ザイFX/フィスコ）。'
        'トランプ大統領は米国外にデータセンターを建設する米企業に巨額の税を課す方針も示した（手法・法的根拠は未提示、みんかぶ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/23月）への引継ぎ：ドル円は158.57円、ユーロドルは1.0968ドル、ユーロ円は173.92円で週を終え、週明けのドル円は158.60円前後（ザイFX/DZH）。'
    '先週はFRBの利上げ観測によるドル高と、AI株安による円買いがぶつかった。金曜は円買いが勝ち、ドル円は200日線を割り込んだ（みんかぶ）。週末（11/21〜22）に相場を動かす新材料は3サイトで確認できず（外為どっとコムは記事本文を取得できず・要確認）。'
    '本日は日本が休場で東京の実需が不在。KissFXは「先週に強まったリスクオフの流れの行方」と「米長期金利の動向」が焦点とする。'
    '23:45の米PMIが弱ければ米金利低下でドル売り・円買いが続き、ドル円の次の下値目安は158.42円（11/20安値）。今週は25日の米PCEで12月利上げの確度を測り、26日の感謝祭以降は薄商いになる（KissFX・ザイFX）。'
)

HOLIDAY_LI = '日本：勤労感謝の日で休場（KissFX・ForexFactory JSON「JPY Bank Holiday」・ザイFX/フィスコ予定表の3ソースで一致）。東京市場の株式・債券は休場で、日経先物の祝日取引もなし（KissFX）。次の休場は11/26（木）米国の感謝祭、27日は米国が短縮取引（KissFX・みんかぶ）。'

POINTS_EVENTS = [
    '【休場】🇯🇵 日本 勤労感謝の日（Kiss/FF/ザイFX一致）',
    '06:45 🇳🇿 NZ 第3四半期小売売上高 前期比 予想+0.5%（Kiss◎・FF区分:低）【発表済み・結果は要確認】',
    '17:30 🇩🇪 独 製造業PMI速報値 予想54.1（Kiss◎・FF区分:中）',
    '18:00 🇪🇺 欧 製造業PMI速報値 予想52.7（Kiss◎）',
    '18:30 🇬🇧 英 製造業PMI・非製造業PMI速報値 予想53.0／53.0（Kiss◎◎・FF区分:中）',
    '23:45 🇺🇸 米 製造業PMI速報値 予想54.5（Kiss AA）・非製造業PMI速報値 予想55.6（Kiss A）（FF区分:中）',
    '27:00 🇺🇸 米 2年債入札 690億ドル（Kiss A・KissFX/みんかぶのみ）',
    '翌06:00 🇺🇸 米 ウィリアムズNY連銀総裁の講演（投票権あり、Kiss AA・FF一致）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        'ドル円：200日線割れと158.42円',
        '11/20は200日移動平均線を下回り158.42円まで下落（みんかぶ・ザイFX）。4時間足は上昇トレンドが崩れかけ、4Hランキングでも見送り（スコア28・ADX16.0）。'
        '15分・30分足では158.42円を割れば下落の継続、159円台を回復できなければ戻り売りが優勢。東京休場で値が飛びやすいため損切り位置を必ず置く。',
    ),
    (
        '円：リスク回避の円買いが主導',
        '円は先週G10で最も堅調（みんかぶ）。CFTCのIMM通貨先物では円の買い越しが11万6317枚（6796枚減、11/17時点、みんかぶ）。米株の下げが続く限り、クロス円（豪ドル円・ポンド円・ユーロ円）は戻り売りが基本。26日には田村日銀委員の懇談会があり、高田委員に続くタカ派発言なら円買い材料（みんかぶ）。',
    ),
    (
        '米国：PMIとウィリアムズ総裁',
        '23:45の米PMIは製造業 予想54.5（前回54.9）、非製造業 予想55.6（前回56.1）（KissFX）。翌06:00のウィリアムズNY連銀総裁は11/13に「過剰に高いインフレへの対処が必要」と発言済み（前回日報）。株安のなかで12月利上げ支持を明言すればドルの下値を支える。',
    ),
    (
        '欧州・英国：PMI',
        'ユーロ圏はフランス財政不安（独仏10年債利回り差154bp、みんかぶ）が重し。27日にS&amp;Pの仏格付け見直し（みんかぶ）。英国は12月利上げの織り込みが93%（英9月GDP後、みんかぶ）で、18:30のPMIが強ければ織り込みが維持されポンド買い。',
    ),
    (
        '市場休場：日本',
        '本日は日本が勤労感謝の日で休場。仲値の需給がなく、東京時間は動意が乏しくなりやすい。欧州勢参入の16〜17時以降に値幅が出やすい。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('06:45', '🇳🇿 NZ', '【発表済み】第3四半期小売売上高 前期比（Kiss/FF一致・結果は要確認）', '◎', '+0.5%', '-0.5%'),
    ('06:45', '🇳🇿 NZ', '【発表済み】第3四半期コア小売売上高 前期比（FFのみ・要確認）', '低(FF)', '+0.8%', '+0.7%'),
    ('07:00', '🇦🇺 豪', '【発表済み】製造業PMI速報値（FFのみ・要確認）', '低(FF)', '—', '49.7'),
    ('07:00', '🇦🇺 豪', '【発表済み】サービス業PMI速報値（FFのみ・要確認）', '低(FF)', '—', '47.8'),
    ('終日', '🇯🇵 日', '勤労感謝の日で休場（Kiss/FF/ザイFX一致）', '—', '—', '—'),
    ('17:15', '🇫🇷 仏', '製造業PMI速報値（Kiss/FF一致・前回はKiss 49.5、FF 49.3で不一致・要確認）', '○', '49.8', '49.5（FF 49.3）'),
    ('17:15', '🇫🇷 仏', '非製造業PMI速報値（Kiss/FF一致・予想Kiss 47.3／FF 47.4、前回Kiss 46.2／FF 48.4で不一致・要確認）', '○', '47.3（FF 47.4）', '46.2（FF 48.4）'),
    ('17:30', '🇩🇪 独', '製造業PMI速報値（Kiss/FF/ザイFX一致）', '◎', '54.1', '54.2'),
    ('17:30', '🇩🇪 独', '非製造業PMI速報値（Kiss/FF一致・予想Kiss 52.3／FF 52.4、前回はKiss・ザイFX 52.5、FF 51.7・要確認）', '○', '52.3（FF 52.4）', '52.5（FF 51.7）'),
    ('18:00', '🇪🇺 欧', '製造業PMI速報値（Kiss/FF一致・前回はKiss・ザイFX 52.7、FF 52.4・要確認）', '◎', '52.7', '52.7（FF 52.4）'),
    ('18:00', '🇪🇺 欧', '非製造業PMI速報値（Kiss/FF一致・予想Kiss 51.9／FF 51.8、前回はKiss・ザイFX 51.4、FF 51.7・要確認）', '○', '51.9（FF 51.8）', '51.4（FF 51.7）'),
    ('18:30', '🇬🇧 英', '製造業PMI速報値（Kiss/FF/ザイFX一致）', '◎', '53.0', '52.8'),
    ('18:30', '🇬🇧 英', '非製造業PMI速報値（Kiss/FF一致・前回はKiss・ザイFX 52.8、FF 53.1・要確認）', '◎', '53.0', '52.8（FF 53.1）'),
    ('22:00', '🇬🇧 英', 'ピル英中銀チーフエコノミスト 発言（Kiss/FF一致）', '△', '要人発言', '—'),
    ('22:30', '🇺🇸 米', 'シカゴ連銀全米活動指数（KissFX・ザイFX予定記事のみ、FFになし・要確認）', 'C', '+0.16', '+0.07'),
    ('22:30', '🇨🇦 加', '第3四半期企業利益 前期比（FFのみ・要確認）', '低(FF)', '—', '+8.7%'),
    ('23:45', '🇺🇸 米', '製造業PMI速報値（Kiss/FF/ザイFX一致・前回はKiss・ザイFX 54.9、FF 56.0・要確認）', 'AA', '54.5', '54.9（FF 56.0）'),
    ('23:45', '🇺🇸 米', '非製造業PMI速報値（Kiss/FF一致・予想はザイFX 55.7、前回はKiss・ザイFX 56.1、FF 57.9・要確認）', 'A', '55.6', '56.1（FF 57.9）'),
    ('27:00', '🇺🇸 米', '2年債入札 690億ドル（KissFX・みんかぶのみ・要確認）', 'A', '—', '—'),
    ('翌06:00', '🇺🇸 米', 'ウィリアムズNY連銀総裁 講演（投票権あり・質疑応答あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
]
CAL_NOTE = (
    '※ 時刻は日本時間（24時以降は翌日）。KissFX・ForexFactory JSONで一致した指標を採用し、片方でのみ確認できた項目や数値が食い違う項目は「（要確認）」を付記。'
    '前回値の食い違いはザイFX/フィスコの予定表（3ソース目）がKissFXと一致したため、KissFXの値を主表示し、FFの値を括弧で併記。'
    '重要度はKissFXランク（米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×）、KissFXにない項目はFF区分（高・中・低）。'
    '【発表済み】は本日0時〜7時に実施済みの項目。「翌」は翌日（11/24火）の日本時間。冬時間のため米東部時間+14時間で換算。investing.comは403で取得できず。'
)

def _key(r):
    t = r[0]
    if t.startswith('翌'):
        return (30 + int(t[1:3]), int(t[4:6]))
    if not t[:2].isdigit():
        return (7, 30)
    return (int(t[:2]), int(t[3:5]))
CAL_ROWS.sort(key=_key)

CAL_ROWS_HTML = '\n'.join(
    f'            <tr><td>{time}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>'
    for time, country, name, importance, forecast, previous in CAL_ROWS
)

FUNDAMENTALS_ROWS = [
    ('FRB', '🇺🇸 USD', '3.75–4.00%', 'var(--red)', 'タカ派',
     '10/28のFOMCで据え置き（10対2）、次回12/9（KissFX）。11/18公表の議事要旨では大半が追加引き締めを適切とし、2名は0.25%超の利上げも視野（みんかぶ）。11/20にクック理事は「早急に利上げが必要」、ポールソン総裁は「連続利上げを検討する用意」（みんかぶ）。一方でミシガン大の期待インフレ率の大幅な下方修正で大幅利上げ観測は後退（ザイFX/フィスコ）。'),
    ('日銀', '🇯🇵 JPY', '1.25%', 'var(--blue)', 'タカ派',
     '10/30会合で1.25%を据え置き（市場予想通り、KissFX）、次回12/18。高田委員のタカ派発言で12月利上げ期待は約85%（みんかぶ週間まとめ）。26日に田村委員の懇談会（KissFX・みんかぶ）。'),
    ('ECB', '🇪🇺 EUR', '2.50%', 'var(--red)', 'タカ派',
     '10/29に預金金利2.50%で据え置き（KissFX）、次回12/17。ナーゲル独連銀総裁は11/20に「12月会合で何かをする必要があると確信」、ペレイラ・ポルトガル中銀総裁は「金利に関して断固たる行動をとる」（みんかぶ）。仏財政不安がユーロの重し。10月会合の議事要旨は26日公表。'),
    ('BOE', '🇬🇧 GBP', '4.00%', 'var(--red)', 'タカ派',
     '11/5に25bp利上げして4.00%（KissFX・前回確認の各報道）、次回12/17。英サービスCPIは前年比+3.7%と予想+3.8%を下回りポンド売り（みんかぶ）。一方10月小売売上高は前月比+0.7%（予想0.0%）と上振れ。12月利上げの織り込みは93%（英9月GDP後、みんかぶ）。'),
    ('RBA', '🇦🇺 AUD', '4.85%', 'var(--red)', 'タカ派（追加利上げは慎重）',
     '11/3に25bp利上げして4.85%（年内5回目、KissFX・報道）、次回12/8。11/19の豪雇用統計の悪化で豪ドルは年初来安値0.6662ドル（みんかぶ）。来年の利下げ転換を見込む声も出ている（みんかぶ）。25日の10月CPIが判断材料。'),
    ('RBNZ', '🇳🇿 NZD', '2.75%', 'var(--red)', 'タカ派寄り',
     '10/28会合で2.75%に据え置き（KissFX）、利上げを主張した委員が3名（前回確認の各報道）。次回は12/9（KissFX）。本日06:45の第3四半期小売売上高が材料。'),
    ('BOC', '🇨🇦 CAD', '2.50%', 'var(--red)', 'タカ派転換',
     '10/28に25bp利上げして2.50%（KissFX）、次回12/9。9月小売売上高は+0.8%（予想+0.7%）、コア+1.0%で加ドル買い（ザイFX/フィスコ・みんかぶ）。24日にマックレム総裁が経済見通しと金融政策について講演（みんかぶ）。'),
    ('SNB', '🇨🇭 CHF', '0.00%', 'var(--muted)', 'ハト派〜中立',
     '9/24に0.00%で据え置き（KissFX）、次回12/10。11/20は安全通貨としてフラン買いが強まり、ドルスイスは0.8377フランまで下落（ザイFX/フィスコ）。'),
]

fundamentals_rows_html = ''
for bank, currency, rate, color, stance, reason in FUNDAMENTALS_ROWS:
    fundamentals_rows_html += f'''            <tr>
              <td>{bank}</td><td>{currency}</td><td><strong>{rate}</strong></td>
              <td style="color:{color};">{stance}</td>
              <td style="font-size:12px;">{reason}</td>
            </tr>
'''

FUNDAMENTALS_PANEL = f'''      <div class="panel full" id="fundamentals">
        <div class="panel-head">
          <h3>🏦 主要中銀ファンダメンタルズ（週次更新）</h3>
          <span>{TODAY} 現在</span>
        </div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>政策金利</th><th>スタンス</th><th>背景・理由</th></tr></thead>
          <tbody>
{fundamentals_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。KissFX（11/20クローズ号の主要国政策金利一覧）、ザイFX・みんかぶの報道、前回更新（11/16）時の各中銀公式発表・海外報道との照合、ロイター配信記事（BOEの3年超ぶり利上げ・RBAの年内5回目の利上げ・FRB/ECB/日銀の据え置き）で確認。前回更新から8中銀とも政策金利の変更なし。外為どっとコムは本文を取得できず。最新情報は各中銀の公式サイトでご確認ください。</p>
      </div>

'''


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
              <li>{HOLIDAY_LI}</li>
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
          <h3>📰 前日の相場振り返り（{PREV_LABEL}）</h3>
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
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">{CAL_NOTE}</p>
      </div>

{FUNDAMENTALS_PANEL}    </div><!-- /content-grid -->

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
