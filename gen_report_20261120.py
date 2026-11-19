# -*- coding: utf-8 -*-
"""FX日報 2026-11-20（金）生成スクリプト"""
import glob, os

TODAY = '2026-11-20'
WEEKDAY = '金'
PREV_LABEL = '2026-11-19 木'

HERO_TITLE_SUB = (
    '前日11/19（木）は米フィラデルフィア連銀景況指数6.3（予想20.1）など米指標の下振れとアンソロピック上場後の米株急落（ダウ-1,101ドル）でドル買いが後退し、ドル円は160円手前の159.97円で反落した。'
    '豪雇用統計は-4.35万人と大幅減で、豪ドルは年初来安値。本日11/20（金）は08:30の全国CPI、16:00の英小売売上高、22:25のウォラーFRB理事、24:00のミシガン大学消費者信頼感指数が材料。'
)

SUMMARY_HEADLINE = (
    '米指標の下振れと米株急落でドル高は一服、リスク回避の円買いと豪ドル売りが目立つ。'
    '本日は08:30全国CPIで円、22:25ウォラー理事で米利上げ観測の強さが試される'
)

SUMMARY_BODY = (
    '11/19（木）のNYは、フィラデルフィア連銀製造業景況指数が6.3（予想20.1）、新規失業保険申請件数が20.3万件（予想19.8万件）、景気先行指数が前月比-0.3%（予想0.0%）とそろって下振れ（ザイFX/フィスコ・みんかぶ一致）。'
    '米株はダウが-1,101.11ドル（-2.19%）と急落し、VIXは28.57（+16.37%）（みんかぶ）。米10年債利回りは5.050%に低下（みんかぶ）。'
    'ドル円は159.97円まで上げた後159.61円で引け、ユーロドルは1.0969ドル、ポンドドルは1.3094ドルまで下落（ザイFX/フィスコ）。本日11/20（金）の主要市場休場はなし。'
)

TOP_PAIR_NAME = 'AUD/JPY 🇦🇺🇯🇵'
TOP_PAIR_BODY = (
    '豪ドル円は11/19の豪10月雇用統計で新規雇用者数-4.35万人（予想+2.5万人）、失業率4.9%（予想4.7%）と大幅に悪化し、107.10円から106.22円まで急落した（みんかぶ）。豪ドルは対ドルでも0.6662ドルと1月5日の年初来安値0.6663ドルを割り込んだ（みんかぶ）。'
    '下げの理由は2つ。1つはRBAの利上げ期待がほぼ払しょくされ、一部で来年の利下げ期待まで出てきたこと（みんかぶ）、もう1つはNYでダウ-2.19%・VIX28.57と株安のリスク回避が強まり円が買われたこと（みんかぶ）。'
    '4Hデイトレ適性ランキング1位（スコア65・ADX56.0・下降、11/19生成分）。15分・30分足では106.22円（11/19安値）が下の節目で、戻りは107円付近（雇用統計前の水準）が売りの目安。08:30の全国CPIで円が動く。'
)

RISK_LEVEL = 'HIGH'
RISK_BODY = (
    'ダウは49,097.06ドル（-1,101.11、-2.19%）、S&amp;P500は7,175.83（-2.02%）、ナスダックは23,879.20（-2.25%）と大幅安、CME日経平均先物は57,955円（大証比-1,785、-3.08%）（みんかぶ）。'
    'VIXは28.57（+4.02、+16.37%）と急上昇（みんかぶ）。アンソロピックは初値111.50ドル（IPO価格83ドル）で始まったが、上場直後から株価指数がそろって下落した（みんかぶ）。'
    'イランは米軍の海上封鎖の強行突破を計画し、石油輸出を妨害すれば中東の石油施設を攻撃すると警告（ファルス通信、みんかぶ経由）。週末を控えたポジション調整にも注意。'
)

KEY_EVENTS_COUNT = '8件'
KEY_EVENTS_SUMMARY = (
    '日 全国CPI(08:30)、米 ポールソン・フィラデルフィア連銀総裁(08:30)、英 小売売上高(16:00)、欧 ラガルドECB総裁(17:30・FFは17:15)、'
    '米 ウォラーFRB理事(22:25)、加 小売売上高(22:30)、米 ミシガン大学消費者信頼感指数 確報値(24:00)、米 クックFRB理事(26:15)'
)

MARKET_OVERVIEW = (
    '<strong>米株（11/19終値）</strong>：ダウ49,097.06ドル（-1,101.11、-2.19%）、S&amp;P500 7,175.83（-2.02%）、ナスダック23,879.20（-2.25%）、CME日経平均先物57,955円（大証比-1,785）（みんかぶ）。'
    'AMDは空売りを公表したヘッジファンドが輸出規制違反疑惑を指摘して-7.72%、エヌビディアは-3.30%（みんかぶ）。'
    '欧州株は独DAXが-1.06%、仏CAC40が-0.81%、英FTSE100が-0.93%。プーチン大統領がEUとウクライナに妥協の用意がないとして停戦協議を退け、域内資産が売られた（ザイFX/フィスコ）。'
    '<strong>米債利回り</strong>：2年債4.768%（-0.036）、10年債5.050%（-0.018）、30年債5.405%（-0.005）（みんかぶ、NY16:29）。序盤は上昇したが、株安で安全資産の米国債が買われ低下に転じた（みんかぶ・ザイFX/フィスコ）。'
    '<strong>ドルインデックス</strong>：103.85（-0.01、ザイFX/フィスコ午後2時台）。日中高値103.97。テクニカルではRSI（14日）70.2と買われ過ぎ領域（みんかぶ）。'
    '<strong>金</strong>：NY金先物12月限3,685.50ドル（-56.40、-1.51%）と続落（みんかぶ）。株安とドル高が圧迫（みんかぶ）。'
    '<strong>原油</strong>：WTI先物1月限82.44ドル（+0.13、+0.16%）（みんかぶ）。序盤84.88ドルまで上げた後に伸び悩み。フィスコは「続落」と報じており、限月の違いによる差（要確認）。トランプ大統領が対イラン紛争解決を急がないと発言（ザイFX/フィスコ）。'
    '<strong>VIX</strong>：28.57（+4.02、+16.37%）（みんかぶ）。'
    '<br><br><strong>政策金利（11/16確認分を継続）：</strong> FRB 3.75〜4.00％、日銀 1.25％、ECB 預金金利2.50％、BOE 4.00％、RBA 4.85％、RBNZ 2.75％、BOC 2.50％、SNB 0.00％。11/19の南ア準備銀行は7.25%で据え置き（ザイFX/フィスコ）。'
    '<br><br><strong>来週の予定：</strong> 11/23（月）日本休場、11/26（木）米国休場（感謝祭）（KissFX）。次回の金融政策発表は12/8豪、12/9米・加・NZ、12/10スイス、12/17英・欧、12/18日本（KissFX）。'
)

RANKING_ROWS = [
    (1, 'AUD/JPY', 'rank-a', 'A', 'スコア65・適。ADX56.0、ADR比81％（5日ADR 72.2pips）、4H方向は下降。11/19は豪雇用統計の大幅悪化（新規雇用者数-4.35万人・失業率4.9%）で107.10円から106.22円まで急落（みんかぶ）。RBA利上げ期待がほぼ消え、株安のリスク回避も重なる。08:30の全国CPIで円の方向が決まりやすい。', 'trend-down', '↓'),
    (2, 'EUR/JPY', 'rank-b', 'B', 'スコア60・候補。ADX48.8、ADR比69％、4H方向は下降。11/19はロンドンで176.07円まで上げた後、NYで175.18円まで下落（みんかぶ・ザイFX/フィスコ）。仏独10年債利回り格差は150bp（みんかぶ）とフランス財政への懸念が続く。17:30（FFは17:15・要確認）のラガルド総裁の講演が材料。', 'trend-down', '↓'),
    (3, 'GBP/JPY', 'rank-b', 'B', 'スコア58・候補。ADX52.8、ADR比68％、4H方向は下降。11/19は日英金利差拡大観測の後退で210.49円から209.24円まで下落（ザイFX/フィスコ）。16:00の英小売売上高（前月比 予想±0.0%、前回-0.4%）でポンドが大きめに動きやすい（KissFX）。', 'trend-down', '↓'),
    (4, 'EUR/USD', 'rank-b', 'B', 'スコア56・候補。ADX51.9、ADR比65％、4H方向は下降。11/19はロンドンで1.1010ドルまで戻した後、NYで1.0969ドルまで下落して引けた（みんかぶ・ザイFX/フィスコ）。米指標の下振れでもユーロは買われず、上値の重さが続く（みんかぶ）。', 'trend-down', '↓'),
    (5, 'AUD/USD', 'rank-b', 'B', 'スコア55・候補。ADX59.4、ADR比65％、4H方向は下降。11/19は豪雇用統計の悪化で0.6662ドルまで下げ、1月5日の年初来安値0.6663ドルを割り込んだ（みんかぶ）。豪中銀の来年利下げ期待も一部で出ている（みんかぶ）。', 'trend-down', '↓'),
]

RANKING_ROWS_HTML = '\n'.join(f'''            <tr>
              <td><span class="rank-badge {badge_class}">{letter}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>''' for rank, pair, badge_class, letter, desc, trend_class, arrow in RANKING_ROWS)

RANKING_NOTE = (
    '※ 4時間足ランキングは2026/11/19 10:19 JST生成分。本日分は未更新（GitHub Actions側の更新待ち）のため、前日の数値。'
    'スコア・ADX・ADR比は候補選定の補助指標であり、売買推奨ではない。'
)

TOPICS = [
    (
        '米指標がそろって下振れ：フィラデルフィア連銀指数6.3、失業保険申請は20.3万件',
        '22:30のフィラデルフィア連銀製造業景況指数は6.3と予想20.1、前回20.9を大きく下回った。新規失業保険申請件数は20.3万件（予想19.8万件、前回20.2万件に上方修正）、失業保険継続受給者数は176.3万人（予想170.3万人）と雇用も弱かった（ザイFX/フィスコ・みんかぶ一致）。'
        '24:00の景気先行指数も前月比-0.3%（予想0.0%）と予想外のマイナス（ザイFX/フィスコ）。'
        'ドル円は朝方、日米金利差拡大観測で159.97円まで上昇したが、指標の下振れと米長期金利の低下でドル買いが後退し、160円手前では当局の円安是正介入への警戒も重なり159.61円で引けた（ザイFX/フィスコ）。',
    ),
    (
        'アンソロピック上場も米株は急落：ダウ-1,101ドル、VIXは28.57',
        'アンソロピックはナスダックに上場し、初値111.50ドルとIPO価格83ドルを34%上回った（みんかぶ）。ロンドン時間は上場への期待で米株先物が堅調となり、円売りでドル円は159.95円付近、ポンド円は210.66円まで上昇した（みんかぶ）。'
        'しかし取引開始の瞬間に株価指数はそろって下落し、ダウは-1,101.11ドル（-2.19%）、ナスダックは-2.25%で引けた（みんかぶ）。市場では「AI投資をいかに収益化するかという疑問は依然残っている」との指摘が出た（みんかぶ）。'
        'AMDはヘッジファンドのハンターブルックが空売りと輸出規制違反疑惑を公表して-7.72%（みんかぶ）。VIXは+16.37%の28.57に上昇し、金先物も-1.51%の3,685.50ドルと続落（みんかぶ）。',
    ),
    (
        '豪雇用統計がサプライズの悪化、豪ドルは年初来安値',
        '09:30の豪10月雇用統計は新規雇用者数-4.35万人（予想+2.5万人、前回-3.93万人）と2か月連続の大幅減、失業率は4.9%（予想4.7%）と一気に0.2%悪化した（みんかぶ）。正規雇用者数も-0.29万人（みんかぶ）。'
        '豪ドルは対ドルで0.6720ドル台から0.6662ドルまで下げ、1月5日の年初来安値0.6663ドルをわずかに割り込んだ。豪ドル円は107.10円から106.22円まで大幅安（みんかぶ）。'
        'RBAは11/3に4.85%へ利上げしたばかりだが、追加利上げ期待はほぼ払しょくされ、一部で来年の利下げ期待が出てきた（みんかぶ）。NZドルはドル高でやや軟調も落ち着いた動き。ブレマンRBNZ総裁は燃料高と通貨安でインフレ圧力が広がるリスクを警戒と発言（みんかぶ）。',
    ),
    (
        'ユーロとポンドは戻り売り：ユーロドル1.1010ドルから1.0969ドル、ポンドドルは1.3094ドル',
        'ロンドン時間はドル安に振れ、ユーロドルは1.1010ドル、ポンドドルは1.3173ドルまで戻した（みんかぶ）。しかしNYではユーロドルが1.1005ドルから1.0969ドル、ポンドドルが1.3164ドルから1.3094ドルまで下落した（ザイFX/フィスコ）。'
        'フィスコは「英中銀の利上げ観測後退でポンド売りが続いた」と伝えた。一方みんかぶは、市場は来年にかけて英中銀のあと3〜4回の利上げを織り込んでおり、利下げに転じればポンドの下押し圧力が強まるとのアナリストの見方を伝えている。'
        'ユーロはフランス財政への懸念が重しで、仏独10年債利回り格差は150bp（みんかぶ）。エコノミストは「フランスは2030年までにGDP比3%の財政調整が必要で、外部圧力がない限り実現は困難」と指摘（みんかぶ）。',
    ),
    (
        '米中ロ首脳会談は無難に通過、FRB高官はAIのインフレ圧力に言及',
        '初の米中ロ3か国首脳会談では習主席が米中関係の前向きな勢いを維持すると発言し、市場は総じて無難に通過と受け止めた（みんかぶ）。ドル円は159.70円台に高止まりし、会談への反応は薄かった（みんかぶ）。'
        'クシュナー氏は「ロシアは欧州との多国間協議に応じることに合意」と述べた（みんかぶ）一方、フィスコはプーチン大統領がEUとウクライナに妥協の用意がないとして停戦協議を退けたと報じ、欧州株が続落（ザイFX/フィスコ）。報道の内容に食い違いがある（要確認）。'
        'ジェファーソンFRB副議長は「AIブームが経済全体の需要を押し上げ、短期的なインフレ圧力を高めている」、グールズビー・シカゴ連銀総裁は「現時点でスタグフレーションは見られない」と発言（みんかぶ）。植田日銀総裁は「為替変動が物価に影響を及ぼしやすくなっていることに留意」「デフレに戻るリスクはある程度低下」と述べた（みんかぶ）。',
    ),
]

TOPICS_HTML = '\n'.join(f'''          <div class="topic">
            <div class="topic-title">【トピック{i+1}】{title}</div>
            {body}
          </div>''' for i, (title, body) in enumerate(TOPICS))

HANDOVER = (
    '本日（11/20金）への引継ぎ：ドル円は159.61円、ユーロドルは1.0969ドル、ポンドドルは1.31ドル付近で引けた（ザイFX/フィスコ・みんかぶ）。米指標の下振れと株安でドル高は一服したが、ドル円は159円台を維持している（みんかぶ）。'
    'オプション市場では介入が差し迫っているとの見方が弱まり、短期的な円高に備える需要が後退した（みんかぶ）。ただし160円台は引き続き上値が重いとの見方（みんかぶ）。'
    '08:30の全国CPIは予想+2.5%（前回+2.1%）で、上振れなら12/18の日銀会合での利上げ観測が強まり円買い。22:25のウォラー理事は11/18に「12月に0.50%利上げ」を推奨しており、前日の弱い米指標を受けてもタカ派姿勢を維持するかが焦点。'
    'KissFXは「米ドルの方向性と米株価指数の調整が続くかどうかがキモ」と指摘。週末金曜日のため、NY午後は持ち高調整の動きに注意。'
)

HOLIDAY_LI = 'なし（KissFXの主要国休場日一覧・ForexFactory JSONで本日の休場記載なし）。次の休場は11/23（月）日本、11/26（木）米国。'

POINTS_EVENTS = [
    '08:30 🇯🇵 日 全国消費者物価指数 予想+2.5%（Kiss/フィスコ一致・Kiss◎）、除生鮮 予想+2.3%（Kiss/FF一致）',
    '08:30 🇺🇸 米 ポールソン・フィラデルフィア連銀総裁の発言（投票権あり）（Kiss/FF一致・KissランクAA）',
    '16:00 🇬🇧 英 小売売上高 前月比 予想±0.0%（Kiss/FF一致・Kiss◎・FF区分:中）、前年比 予想+1.7%（Kiss/フィスコ一致）',
    '17:30 🇪🇺 欧 ラガルドECB総裁の発言（KissFXは17:30、FFは17:15で時刻不一致・要確認・Kiss◎・FF区分:中）',
    '22:25 🇺🇸 米 ウォラーFRB理事の発言（投票権あり）（Kiss/FF一致・KissランクAA）',
    '22:30 🇨🇦 加 小売売上高 前月比 予想+0.7%（Kiss/FF一致・Kiss◎）',
    '24:00 🇺🇸 米 ミシガン大学消費者信頼感指数 確報値 予想51.5（Kiss）／51.7（FF）／53.3（フィスコ）で不一致・要確認（KissランクA・FF区分:中）',
    '26:15 🇺🇸 米 クックFRB理事の発言（投票権あり）（Kiss/FF一致・KissランクAA）',
]
POINTS_EVENTS_HTML = '\n'.join(f'              <li>{e}</li>' for e in POINTS_EVENTS)

OTHER_POINTS = [
    (
        '豪ドル円：106.22円の安値',
        '4H下降トレンドでランキング1位。11/19は豪雇用統計の悪化で107.10円から106.22円まで急落した（みんかぶ）。RBAの利上げ期待が消えた豪ドル売りと、株安による円買いが同じ方向に働いている。'
        '15分・30分足では106.22円を割ると下げが広がりやすく、107円付近までの戻りは売り場の目安。08:30の全国CPIと東京時間の日経平均（CME先物は57,955円）が材料。',
    ),
    (
        'ドル円：159.28〜159.97円のレンジ、160円手前の介入警戒',
        '11/19は東京午前の159.28円付近を安値に、NYで159.97円まで上昇したが160円には届かず159.61円で引けた（みんかぶ・ザイFX/フィスコ）。160円手前では当局の円安是正介入への警戒が上値を抑える（ザイFX/フィスコ）。'
        '4Hランキングでは10位（ADX12.7・レンジ・見送り）と方向感が乏しい。08:30の全国CPIが上振れなら円買い、22:25のウォラー理事がタカ派ならドル買い。レンジを抜けた方向に15分足でついていく。',
    ),
    (
        'ポンド：16:00の英小売売上高',
        '前月比 予想±0.0%（前回-0.4%）、前年比 予想+1.7%（前回+0.8%）（KissFX・フィスコ）。KissFXは「発表でポンドが大きめに動きやすい」と指摘。'
        'ポンドドルは11/19に1.3094ドルまで下げ（ザイFX/フィスコ）、英中銀の利上げ観測が後退する中で下値を探る流れ。弱い結果ならGBP/JPY（4H下降・ランキング3位）の戻り売り。',
    ),
    (
        'リスク要因：米株の調整とイラン情勢',
        'ダウは-2.19%、VIXは28.57と警戒感が大きく上昇（みんかぶ）。株安が続けば円買い・豪ドル売り。'
        'イランは米軍の海上封鎖を数十隻規模のタンカー船団で強行突破する計画で、妨害されれば中東の石油施設を攻撃すると警告した（ファルス通信、みんかぶ経由）。原油が急伸すれば資源国通貨とインフレ観測を通じて米金利に波及する。',
    ),
    (
        '市場休場：なし',
        '本日11/20（金）は主要市場の休場なし（KissFXの主要国休場日一覧・ForexFactory JSONで一致）。来週は11/23（月）日本、11/26（木）米国が休場（KissFX）。',
    ),
]
OTHER_POINTS_HTML = '\n'.join(f'''              <li><strong>{title}</strong>：{body}</li>''' for title, body in OTHER_POINTS)

CAL_ROWS = [
    ('00:00', '🇺🇸 米', '【発表済み】景気先行指数 前月比（前日24:00分）結果-0.3%', 'A', '±0.0%', '±0.0%'),
    ('00:30', '🇺🇸 米', '【発表済み】週間天然ガス貯蔵量（結果は未確認）', 'B', '+250億立方フィート（FF）', '+610億立方フィート'),
    ('00:46', '🇺🇸 米', '【発表済み】MBA住宅ローン延滞率（FFのみ・要確認）', '（FF低）', '—', '4.37%'),
    ('02:30', '🇺🇸 米', '【発表済み】グールズビー・シカゴ連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('04:15', '🇺🇸 米', '【発表済み】バーFRB理事 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('06:00', '🇺🇸 米', '【発表済み】バーキン・リッチモンド連銀総裁 発言（投票権なし）（Kiss/FF一致）', 'BB', '要人発言', '—'),
    ('08:30', '🇯🇵 日', '全国消費者物価指数 前年比（Kiss/フィスコ一致）', '◎', '+2.5%', '+2.1%'),
    ('08:30', '🇯🇵 日', '全国消費者物価指数 除生鮮 前年比（Kiss/FF一致）', '◎（FF低）', '+2.3%', '+2.1%'),
    ('08:30', '🇺🇸 米', 'ポールソン・フィラデルフィア連銀総裁 発言（投票権あり）（Kiss/FF一致）', 'AA', '要人発言', '—'),
    ('09:01', '🇬🇧 英', 'GfK消費者信頼感調査（Kiss/FF一致）', '×（FF低）', '-22', '-24'),
    ('10:00', '🇨🇳 中', '1年物ローンプライムレート（FF/フィスコ一致）', '（FF低）', '3.00%', '3.00%'),
    ('10:00', '🇨🇳 中', '5年物ローンプライムレート（FF/フィスコ一致）', '（FF低）', '3.50%', '3.50%'),
    ('11:00', '🇳🇿 NZ', 'クレジットカード支出 前年比（FFのみ・要確認）', '（FF低）', '—', '6.9%'),
    ('16:00', '🇬🇧 英', '小売売上高 前月比（Kiss/FF一致）', '◎（FF中）', '±0.0%', '-0.4%'),
    ('16:00', '🇬🇧 英', '小売売上高 前年比（Kiss/フィスコ一致）', '◎', '+1.7%', '+0.8%'),
    ('16:00', '🇬🇧 英', '小売売上高 除自動車 前月比／前年比（KissFXのみ・要確認）', '◎', '+0.1%／+1.8%', '-0.7%／+0.8%'),
    ('16:00', '🇬🇧 英', '公共部門純借入額（FFのみ・要確認）', '（FF低）', '180億ポンド', '245億ポンド'),
    ('16:00', '🇩🇪 独', '生産者物価指数 前月比（Kiss/FF。予想が不一致・要確認）', '×（FF低）', '+1.0%（Kiss）／+0.9%（FF）', '+1.9%'),
    ('16:00', '🇩🇪 独', '生産者物価指数 前年比（KissFXのみ・要確認）', '×', '+7.3%', '+6.7%'),
    ('16:02', '🇨🇳 中', '海外直接投資 年初来前年比（FFのみ・要確認）', '（FF低）', '—', '-4.3%'),
    ('17:30', '🇪🇺 欧', 'ラガルドECB総裁 発言（KissFXは17:30、FFは17:15で時刻不一致・要確認）', '◎（FF中）', '要人発言', '—'),
    ('20:30', '🇮🇳 印', '外貨準備高（フィスコのみ・要確認）', '—', '—', '—'),
    ('20:30', '🇮🇳 印', '主要産業生産高（フィスコのみ・要確認）', '—', '—', '+7.9%'),
    ('22:00', '🇩🇪 独', 'ナーゲル独連銀総裁 発言（Kiss/FF一致）', '△（FF低）', '要人発言', '—'),
    ('22:25', '🇺🇸 米', 'ウォラーFRB理事 発言（投票権あり）（Kiss/FF一致）', 'AA（FF低）', '要人発言', '—'),
    ('22:30', '🇨🇦 加', '小売売上高 前月比（Kiss/FF一致）', '◎（FF低）', '+0.7%', '+1.2%'),
    ('22:30', '🇨🇦 加', '小売売上高 除自動車 前月比（Kiss/FF一致）', '◎（FF低）', '+0.7%', '+1.2%'),
    ('24:00', '🇺🇸 米', 'ミシガン大学消費者信頼感指数 確報値（Kiss/FF/フィスコ。予想が不一致・要確認）', 'A（FF中）', '51.5（Kiss）／51.7（FF）／53.3（フィスコ）', '51.0'),
    ('24:00', '🇺🇸 米', 'ミシガン大学 期待インフレ率 確報値（FFのみ・要確認）', '（FF中）', '—', '4.3%'),
    ('24:00', '🇪🇺 欧', '消費者信頼感指数 速報値（FF/フィスコ。予想・前回が不一致・要確認）', '（FF低）', '-18（FF）／-18.2（フィスコ）', '-18（FF）／-17.9（フィスコ）'),
    ('26:15', '🇺🇸 米', 'クックFRB理事 発言（投票権あり）（Kiss/FF一致）', 'AA（FF低）', '要人発言', '—'),
]

CAL_NOTE = (
    '※ 時刻は日本時間（24時以降は翌日）。KissFX・ForexFactory JSONで一致した指標を採用し、片方または単独ソースでのみ確認できた項目は「（要確認）」を付記。'
    '重要度はKissFXランク（米国 SS&gt;S&gt;AA&gt;A&gt;BB&gt;B&gt;C、その他 ◎&gt;○&gt;△&gt;×）を優先し、ForexFactory区分を（FF高・中・低）で併記。予想値の第3ソースとしてザイFX/フィスコの本日のスケジュールも参照。'
    '外為どっとコムのニュース一覧はJavaScript描画のため本文を取得できず、ザイFX・みんかぶ・KissFXで確認。investing.comは取得不可（403想定）のため未使用。'
    '【発表済み】は本日0時〜7時に実施済みの項目（00:00の項目は前日11/19夜24:00分）。ラガルド総裁はフィスコでは「欧州銀行会議で基調講演」（時刻記載なし）。冬時間のため米東部時間+14時間で換算。'
)
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
