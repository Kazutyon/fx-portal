import glob
import datetime

TODAY = '2026-09-21'
WEEKDAY = '月'

HERO_SUB = (
    '前週末9/18（金）の日銀金融政策決定会合で、政策金利は市場予想通り0.25%引き上げられ1.25%となった'
    '（1995年以来約31年ぶりの高水準、新金利は9/24から適用）。ただし9人中2人の委員が据え置きを主張する反対票を投じ、'
    '賛成7・反対2の分裂決定となった。植田総裁は会見で「物価が2%目標を超えて上振れするリスクが顕在化し、政策の局面は変化した」と述べる一方、'
    '次回利上げの具体的な時期には言及せず、東京・ロンドン市場ではハト派的と受け止められ円売りが優勢となり、ドル円は157円33銭まで上昇した。'
    'その後NY時間には日銀がレートチェックを実施したとの報道が伝わり、実弾為替介入への警戒感が急速に高まったことで、'
    'ドル円は欧州時間高値158円05銭（9/3以来の高値、200日移動平均158円42銭が上値抵抗）から反落し、'
    'NY引けは156円88銭（前営業日比+91銭）となった。ウォルシュFRB議長のインフレ警戒発言を受けて米長期金利の上昇も一服し、'
    'ドルの上値は抑えられた。VIXは14.81（前日比-3.95%）、米10年債利回りは4.99〜5.00%（日中一時5.04%、2007年以来の高水準）、'
    '米2年債利回りは4.74%（2024年7月以来の高水準）、ドルインデックス（DXY）は100.2前後、金は4,410ドル前後、'
    'WTI原油は96.74ドル（前日比+0.69%）となっている（前週末9/18・9/19時点、週末を挟むため直近の取引最終値）。'
    '本日9/21（月）は敬老の日で日本市場が休場（9/21〜23、日経225先物・オプションは祝日取引あり）となり、'
    'KissFXも「注目度の高い米国指標の発表はない」と明記する閑散日で、19:30のグールズビー・シカゴ連銀総裁、'
    '24:00のラガルドECB総裁、24:20（要確認）のマックレムBOC総裁の発言が主な材料となる。'
)

SUMMARY_H3 = (
    '日銀が0.25%利上げで政策金利1.25%に（反対2）。日銀のレートチェック報道でドル円は158円05銭から156円88銭へ反落。'
    '本日は敬老の日で日本市場が休場、経済指標は閑散'
)

SUMMARY_P = HERO_SUB

FOCUS_CURRENCY_H3 = 'USD/JPY \U0001F1FA\U0001F1F8\U0001F1EF\U0001F1F5'
FOCUS_CURRENCY_P = (
    '4Hデイトレ適性ランキング1位（本日06:43時点データ、スコア76・適、ADX29.4で上昇トレンド、直近5日ADRは5年平均の104.3%）。'
    '前週末9/18はBOJの0.25%利上げ（1.25%、反対2）を受けた円売りと、NY時間の日銀レートチェック報道を受けた円買いが交錯し、'
    '欧州時間高値158円05銭からNY引け156円88銭まで反落した。本日は敬老の日で日本市場が休場となり国内勢の商いは薄くなりやすく、'
    '200日移動平均線158円42銭を意識した水準感と、円買い介入への警戒が引き続き相場の背景にある。'
)

RISK_LEVEL = 'MEDIUM'
RISK_P = (
    '本日は敬老の日で日本市場が休場となり、国内勢不在で商いが薄くなりやすい一日となる。経済指標はKissFX・ForexFactoryともに'
    '「注目度の高い米国指標の発表はない」水準の閑散日で、19:30のグールズビー・シカゴ連銀総裁、24:00のラガルドECB総裁、'
    '24:20（要確認）のマックレムBOC総裁など要人発言が中心となる。一方で前週末に強まった日銀のレートチェック実施報道を受けた'
    '為替介入への警戒感は継続しており、薄商いの中でドル円が200日移動平均線158円42銭に接近する場面では値動きが拡大しやすい点に'
    '注意が必要である。'
)

KEY_COUNT = '8件'
KEY_COUNT_P = (
    '敬老の日で日本市場休場 / 英ライトムーブ住宅価格指数 / グールズビー・シカゴ連銀総裁発言 / ラガルドECB総裁発言 / '
    'マックレムBOC総裁発言（要確認） 等（本日は注目度の高い米指標の発表なし）'
)

# ── ranking table (top5 from data/daytrade-ranking.json, generated_at 2026-09-21 06:43 JST) ──
RANKING_ROWS = [
    ('A', 'rank-a', 'USD/JPY', 'ランキング1位（スコア76・適）。ADX29.4で上昇トレンド、直近5日ADRは5年平均の104.3%', 'trend-up', '↑'),
    ('B', 'rank-b', 'GBP/JPY', 'ランキング2位（スコア66・適）。ADX33.3でレンジ、直近5日ADRは5年平均の94.3%', 'trend-range', '→'),
    ('B', 'rank-b', 'AUD/JPY', 'ランキング3位（スコア63・候補）。ADX35.4で上昇トレンド、直近5日ADRは5年平均の76.7%', 'trend-up', '↑'),
    ('B', 'rank-b', 'EUR/JPY', 'ランキング4位（スコア60・候補）。ADX32.1でレンジ、直近5日ADRは5年平均の85.7%', 'trend-range', '→'),
    ('B', 'rank-b', 'NZD/USD', 'ランキング5位（スコア54・候補）。ADX37.8で下降トレンド、直近5日ADRは5年平均の68.3%', 'trend-down', '↓'),
]

MARKET_ENV_P = (
    '前週末9/18（金）は日銀が0.25%利上げ（1.25%、反対2）を決定し東京市場では一時157円33銭まで円安が進んだが、'
    'NY時間に日銀のレートチェック実施が報じられると実弾介入への警戒感が急速に高まり、ドル円は欧州時間高値158円05銭'
    '（200日移動平均158円42銭が上値抵抗）から反落しNY引けは156円88銭となった。ウォルシュFRB議長のインフレ警戒発言を'
    '受けて米長期金利の上昇は一服し、NY金先物は4,410ドル前後の高値圏で推移した。本日9/21（月）は敬老の日で日本市場が'
    '休場となり国内勢の商いは薄くなりやすく、経済指標もKissFX・ForexFactoryともに「注目度の高い米国指標の発表はない」'
    '閑散日で、19:30のグールズビー・シカゴ連銀総裁、24:00のラガルドECB総裁、24:20（要確認）のマックレムBOC総裁など'
    '要人発言が中心となる。薄商いの中でドル円が200日線158円42銭に接近する場面では、介入警戒を背景に値動きが拡大しやすい'
    '点には注意が必要である。'
    '<br><br><strong>政策金利：</strong> 米FRB 3.75〜4.00%（タカ派、9/16FOMCで0.25%利上げ・全会一致） / '
    '日銀 1.25%（タカ派、9/18会合で0.25%利上げ・反対2） / '
    '英BOE 3.75%（中立〜ハト派、9/17据え置き・6対3の分裂投票でハト派的と受け止められポンド安）'
)

RANKING_FOOTNOTE = (
    '※ 4Hデイトレ適性ランキングは2026-09-21 06:43 JST時点のデータ。数値は目安であり、実際のエントリーは各自のルールで'
    '判断してください。本日は敬老の日で日本市場が休場のため国内勢の商いが薄くなりやすく、通常のトレンドフォローに加え'
    '介入警戒によるスプレッド拡大・値動き拡大に注意してください。'
)

# ── 前週末の相場振り返り (2026-09-18〜09-20) ──
REVIEW_TOPICS = [
    ('【トピック1】日銀、0.25%利上げで政策金利1.25%に（反対2、1995年以来の高水準）',
     '9月18日の日銀金融政策決定会合で、政策金利は市場予想通り0.25%引き上げられ1.25%となった'
     '（1995年以来約31年ぶりの高水準、新金利は9/24から適用）。ただし9人中2人の委員が据え置きを主張する反対票を投じ、'
     '賛成7・反対2の分裂決定となった。植田総裁は会見で「物価が2%目標を超えて上振れするリスクが顕在化し、政策の局面は'
     '変化した」と述べる一方、次回利上げの具体的な時期には言及せず、東京・ロンドン市場ではハト派的と受け止められ円売りが'
     '優勢となり、ドル円は157円33銭まで上昇した。'),
    ('【トピック2】日銀のレートチェック実施報道で介入警戒が急上昇、ドル円は158円05銭から156円88銭へ反落',
     '9月18日のNY市場で、日銀が為替のレートチェックを実施したとの報道が伝わり、政府・日銀による実弾為替介入への'
     '警戒感が急速に高まった。この報道を受けてドル円は欧州時間高値158円05銭（9/3以来の高値、200日移動平均158円42銭が'
     '上値抵抗として機能）から反落し、NY市場終値は156円88銭（前営業日NY終値155円97銭比+91銭）となった。'),
    ('【トピック3】ウォルシュFRB議長のインフレ警戒発言で米長期金利の上昇が一服',
     'ウォルシュFRB議長がインフレに対する強い警戒感を示す発言を行い、市場想定に沿う内容として好感された。この結果、'
     '米長期金利の上昇が一服しドルの上値も抑えられた。市場の一部アナリストからは、米財務省による国債買い入れ倍増計画の'
     '継続がドルの信認を損なう懸念があるとの見方も伝えられている（個別アナリストの分析であり市場コンセンサスではない'
     '点に留意・要確認）。'),
    ('【トピック4】NY金先物が続伸、原油安・米長期金利低下でインフレ懸念後退',
     '9月19日（土）時点の報道で、NY金先物が続伸したと伝えられた。原油価格の下落と米長期金利の低下によりインフレ懸念が'
     '和らいだことが背景とされている。直接のFXイベントではないが、リスク心理・金利観測の材料として市場が注視した。'),
]

HANDOVER = (
    '本日（9/21月）への引継ぎ：前週末9/18（金）は日銀が0.25%利上げで政策金利を1.25%に引き上げたが反対2の分裂決定で'
    'ハト派的と受け止められ、東京市場でドル円は157円33銭まで円安が進んだ。その後NY時間には日銀のレートチェック実施が'
    '報じられ実弾介入への警戒感が急速に高まり、ドル円は欧州時間高値158円05銭から反落しNY引けは156円88銭となった。'
    'ウォルシュFRB議長のインフレ警戒発言で米長期金利の上昇は一服し、NY金先物は続伸した。本日9/21（月）は敬老の日で'
    '日本市場が休場となり国内勢の商いが薄くなりやすい中、200日移動平均線158円42銭を挟んだ水準感と円買い介入への警戒が'
    '引き続き相場の背景となる。経済指標は閑散で、19:30のグールズビー・シカゴ連銀総裁、24:00のラガルドECB総裁、'
    '24:20（要確認）のマックレムBOC総裁など要人発言が本日の焦点となる。'
)

# ── 経済指標カレンダー（全件、KissFX × ForexFactory 2ソース照合） ──
CALENDAR_ROWS = [
    ('終日', '\U0001F1EF\U0001F1F5 日本', '⚠️ <strong>敬老の日（日本祝日）— 東京市場（株式・銀行）休場、日経225先物・オプションは祝日取引あり</strong>（KissFX・ForexFactory一致）', '◎', '—', '—', True),
    ('08:01', '\U0001F1EC\U0001F1E7 英', 'ライトムーブ住宅価格指数【前月比／前年比】（KissFX・ForexFactory一致、値の対応関係に相違あり・要確認）', '低', '-2.0%／-1.0%(Kiss)', '-2.0%(FF)', False),
    ('12:00', '\U0001F1F3\U0001F1FF NZ', 'クレジットカード支出【前年比】（ForexFactoryのみ・要確認）', '低', '—', '+5.3%', False),
    ('19:00', '\U0001F1EA\U0001F1FA 欧', '独連銀（ブンデスバンク）月報（ForexFactoryのみ・要確認）', '低', '—', '—', False),
    ('19:30', '\U0001F1FA\U0001F1F8 米', 'グールズビー・シカゴ連銀総裁（投票権なし） 発言（KissFX・ForexFactory一致）', '要人発言', '—', '—', False),
    ('21:30', '\U0001F1FA\U0001F1F8 米', 'シカゴ連銀全米活動指数（KissFXのみ・要確認）', '低', '-0.04', '-0.06', False),
    ('24:00', '\U0001F1EA\U0001F1FA 欧', 'ラガルドECB総裁 発言（KissFX・ForexFactory一致）', '要人発言', '—', '—', False),
    ('24:20', '\U0001F1E8\U0001F1E6 加', 'マックレムBOC総裁 発言（KissFX24:20・ForexFactory24:05で時刻相違・要確認）', '要人発言', '—', '—', False),
]

CALENDAR_FOOTNOTE = (
    '※ 時刻はJST。KissFX（主・ランク付き、https://kissfx.com/article/fxdays20260921.html）とForexFactoryの機械可読カレンダー'
    '（ff_calendar_thisweek.json、ET→JST変換済み。economic_calendar_forexfactory.pyで正規化）の2つの独立ソースで照合済み。'
    '両ソースで一致した指標はそのまま掲載し、片方のソースにしか掲載がない指標、または予想値・前回値・時刻がソース間で相違する'
    '指標には「（要確認）」を付しています。本日は敬老の日で日本市場が休場です（9/21〜23、日経225先物・オプションは祝日取引'
    'あり）。KissFXは「本日は注目度の高い米国の経済指標の発表はない」と明記しています。指標の網羅性は保証できないため、'
    '発表直前に各社カレンダーで再確認してください。'
)

# ── 主要中銀ファンダメンタルズ（月曜のみ・週次更新） ──
FUNDAMENTALS_ROWS = [
    ('FRB', '\U0001F1FA\U0001F1F8 USD', '3.75–4.00%', 'var(--red)', 'タカ派',
     '9/16のFOMCで0.25%利上げを全会一致（12対0）で決定、2023年7月以来の利上げ。ウォーシュ議長は「インフレ率は依然高水準で、'
     '今回の措置は2%目標の早期達成を後押しする」と発言。SEP（経済見通し）では多数の委員が年内さらに1回以上の利上げを予想し、'
     '2026年末の政策金利中央値は4.10%。次回FOMCは10/27-28。'),
    ('日銀', '\U0001F1EF\U0001F1F5 JPY', '1.25%', 'var(--blue)', 'タカ派',
     '9/18会合で0.25%利上げを決定（賛成7・反対2）、1995年以来約31年ぶりの高水準で新金利は9/24から適用。植田総裁は'
     '「物価が2%目標を超えて上振れするリスクが顕在化し、政策の局面は変化した」と述べ、連続利上げや0.5%の大幅利上げも'
     '「物価情勢次第で排除できない」と言及。9/18のNY時間には日銀のレートチェック実施が報じられ、実弾為替介入への警戒感も'
     '高まっている。次回会合は10/29-30（要確認）。'),
    ('ECB', '\U0001F1EA\U0001F1FA EUR', '2.50%', 'var(--red)', 'タカ派',
     '9/10理事会で預金ファシリティ金利を2.25%から2.50%へ0.25%利上げ（全会一致、主要リファイナンス金利2.65%）、9/16発効。'
     '中東情勢の緊迫化に伴うエネルギー高でユーロ圏インフレが長期化するとの見方が背景。ラガルド総裁は「中東紛争がインフレに'
     '圧力をかけ続け、目標を大幅に上回る状態が長期化する見通し」と発言。次回理事会は10/29。'),
    ('BOE', '\U0001F1EC\U0001F1E7 GBP', '3.75%', 'var(--muted)', '中立〜ハト派',
     '9/17のMPCで6対3の分裂投票により据え置きを決定。3委員は0.25%利上げを主張し利下げ支持はゼロと、投票構成自体は'
     'タカ派寄りだったが、ベイリー総裁のコメントを含め総合的にハト派的な内容と受け止められポンドが下落した。'
     '次回会合は11/5。'),
    ('RBA', '\U0001F1E6\U0001F1FA AUD', '4.35%', 'var(--red)', 'タカ派寄り中立',
     '8月会合で全会一致により据え置き。ブロック総裁は追加利上げの可能性を排除しない姿勢を維持している。'
     '次回会合は9/28-29（今週開催予定・本レポート作成時点で未開催）。'),
    ('RBNZ', '\U0001F1F3\U0001F1FF NZD', '2.75%', 'var(--red)', 'タカ派',
     '9/2の金融政策委員会で0.25%利上げを決定、2.25%→2.50%（7/8）→2.75%（9/2）と3会合連続の利上げとなった。声明では'
     '「インフレ率を2%目標の中間値に戻しつつ成長・雇用を支える」としつつ、「将来のOCR経路は未定でタイミングは極めて'
     '不確実」とも付言している。次回会合は10/28（要確認）。'),
    ('BOC', '\U0001F1E8\U0001F1E6 CAD', '2.25%', 'var(--muted)', '中立',
     '9/2会合で市場予想通り据え置き（7会合連続）。中東情勢の継続と米加通商交渉の決裂で不確実性が高い一方、4-6月期の'
     '成長は予想より強く内需・輸出が堅調で、経済には需給ギャップ（供給過剰）も指摘されている。次回会合は10/28。'),
    ('SNB', '\U0001F1E8\U0001F1ED CHF', '0.00%', 'var(--muted)', 'ハト派〜中立',
     '2025年6月の利下げ以降、6/18会合を含め4会合連続でゼロ金利政策を維持。2026年通年のインフレ見通しは0.6%と低水準に'
     'とどまっている。次回会合は9/25（今週開催予定）で、ロイター調査ではエコノミスト全員一致で据え置きが予想されている。'),
]

# ─────────────────────────────────────────────────────────

DAYS = {'Monday': '月', 'Tuesday': '火', 'Wednesday': '水', 'Thursday': '木', 'Friday': '金', 'Saturday': '土', 'Sunday': '日'}

report_files = sorted(glob.glob('reports/*.html'), reverse=True)
sidebar_items = ''
for f in report_files[:10]:
    name = f.split('/')[-1].replace('.html', '')
    try:
        d = datetime.date.fromisoformat(name)
        wd = DAYS[d.strftime('%A')]
        label = f'{name}（{wd}）'
    except Exception:
        label = name
    sidebar_items += f'<li><a href="{name}.html">{label}</a></li>\n'

key_events_li = '\n'.join(
    f'              <li>{item}</li>' for item in [
        '終日 \U0001F1EF\U0001F1F5 日本 敬老の日で市場休場',
        '08:01 \U0001F1EC\U0001F1E7 英国 ライトムーブ住宅価格指数',
        '19:30 \U0001F1FA\U0001F1F8 米国 グールズビー・シカゴ連銀総裁 発言',
        '24:00 \U0001F1EA\U0001F1FA 欧州 ラガルドECB総裁 発言',
        '24:20 \U0001F1E8\U0001F1E6 カナダ マックレムBOC総裁 発言（要確認）',
    ]
)

ranking_rows_html = ''
for badge, badge_class, pair, desc, trend_class, arrow in RANKING_ROWS:
    ranking_rows_html += f'''            <tr>
              <td><span class="rank-badge {badge_class}">{badge}</span></td>
              <td><strong>{pair}</strong><br><span style="color:var(--muted);font-size:12px;">{desc}</span></td>
              <td><span class="{trend_class}">{arrow}</span></td>
            </tr>
'''

review_html = ''
for title, body in REVIEW_TOPICS:
    review_html += f'''          <div class="topic">
            <div class="topic-title">{title}</div>
            {body}
          </div>
'''

calendar_rows_html = ''
for time_jst, country, name, importance, forecast, previous, important in CALENDAR_ROWS:
    badge = ' <span class="badge-important">★重要</span>' if important else ''
    if important:
        calendar_rows_html += f'            <tr><td><strong>{time_jst}</strong></td><td>{country}</td><td><strong>{name}</strong>{badge}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>\n'
    else:
        calendar_rows_html += f'            <tr><td>{time_jst}</td><td>{country}</td><td>{name}</td><td>{importance}</td><td>{forecast}</td><td>{previous}</td></tr>\n'

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
  <p>{HERO_SUB}</p>
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
{sidebar_items}      </ul>
    </div>
  </aside>

  <!-- Main -->
  <main class="main">

    <header class="hero">
      <div>
        <p class="eyebrow">AUXEN FX PORTAL — AI Daily Report</p>
        <h2>FX日報 {TODAY}（{WEEKDAY}）<span class="badge-live">最新</span></h2>
        <p class="sub">{HERO_SUB}</p>
      </div>
      <div class="date-card">
        <span>Report Date</span>
        <strong>{TODAY}</strong>
        <em>{WEEKDAY}曜日</em>
      </div>
    </header>

    <div class="summary-grid" id="summary">
      <div class="card highlight">
        <p class="label">一言まとめ</p>
        <h3>{SUMMARY_H3}</h3>
        <p>{SUMMARY_P}</p>
      </div>
      <div class="card">
        <p class="label">最注目通貨</p>
        <h3>{FOCUS_CURRENCY_H3}</h3>
        <p>{FOCUS_CURRENCY_P}</p>
      </div>
      <div class="card">
        <p class="label">Market Risk</p>
        <h3 style="color:var(--red)">{RISK_LEVEL}</h3>
        <p>{RISK_P}</p>
      </div>
      <div class="card">
        <p class="label">本日の重要指標</p>
        <h3>{KEY_COUNT}</h3>
        <p>{KEY_COUNT_P}</p>
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
            <div class="block-title">\U0001F6AB 本日の市場休場</div>
            <ul class="points-list">
              <li>⚠️ <strong>敬老の日（日本祝日）</strong>: 日本市場は9/21（月）〜23（水）まで休場（東京証券取引所・銀行休業）。国内勢不在で流動性が大幅低下しやすい。日経225先物・オプションは祝日取引あり。</li>
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">\U0001F4CC 必見経済指標（時刻順）</div>
            <ul class="points-list">
{key_events_li}
            </ul>
          </div>
          <div class="points-block">
            <div class="block-title">\U0001F441 その他注目点</div>
            <ul class="points-list">
              <li><strong>日銀、0.25%利上げで政策金利1.25%に（反対2、1995年以来の高水準）</strong>：9/18会合で市場予想通り0.25%利上げを決定したが、9人中2人が据え置きを主張する反対票を投じた。植田総裁は「政策の局面は変化した」と述べつつ次回時期には言及せず、ハト派的と受け止められ円売りが優勢となった。</li>
              <li><strong>日銀のレートチェック報道で介入警戒が急上昇、ドル円は158円05銭から156円88銭へ反落</strong>：NY時間に日銀がレートチェックを実施したとの報道が伝わり、実弾為替介入への警戒感が急速に高まった。200日移動平均線158円42銭を上値に反落し、NY引けは156円88銭となった。</li>
              <li><strong>ウォルシュFRB議長のインフレ警戒発言で米長期金利の上昇が一服</strong>：市場想定に沿うタカ派的発言が好感され米長期金利の上昇は一服、ドルの上値も抑えられた。NY金先物は4,410ドル前後の高値圏で続伸した。</li>
              <li><strong>本日は敬老の日で日本市場が休場、経済指標は閑散</strong>：KissFX・ForexFactoryともに本日「注目度の高い米国指標の発表はない」水準の一日で、19:30グールズビー・シカゴ連銀総裁、24:00ラガルドECB総裁、24:20（要確認）マックレムBOC総裁など要人発言が中心となる。</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="panel" id="ranking">
        <div class="panel-head">
          <h3>\U0001F30F 今日の市場環境</h3>
          <span>地合い・センチメント</span>
        </div>
        <div class="report-body" style="margin-bottom:20px;">
          {MARKET_ENV_P}
          </div>

        <div class="panel-head" style="margin-top:4px;">
          <h3>\U0001F3C6 通貨ランキング</h3>
          <span>本日の優先順</span>
        </div>
        <table class="fx-table">
          <thead>
            <tr><th>ランク</th><th>ペア</th><th>4H</th></tr>
          </thead>
          <tbody>
{ranking_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:10px;">{RANKING_FOOTNOTE}</p>
      </div>

      <div class="panel wide" id="review">
        <div class="panel-head">
          <h3>\U0001F4F0 前週末の相場振り返り（2026-09-18〜09-20）</h3>
          <span>週末の主要トピック</span>
        </div>
        <div class="report-body">
{review_html}          <div class="handover">
            <strong>{HANDOVER}</strong>
          </div>
        </div>
      </div>

      <div class="panel full" id="calendar">
        <div class="panel-head">
          <h3>\U0001F4C5 本日の経済指標カレンダー（全件）</h3>
          <span>KissFX × ForexFactory 2ソース照合済み（要確認あり）</span>
        </div>
        <table class="fx-table" style="font-size:0.9em;">
          <thead>
            <tr><th>時刻(JST)</th><th>国</th><th>指標名</th><th>重要度</th><th>予想</th><th>前回</th></tr>
          </thead>
          <tbody>
{calendar_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin-top:12px;">{CALENDAR_FOOTNOTE}</p>
      </div>

      <div class="panel full" id="fundamentals">
        <div class="panel-head">
          <h3>\U0001F3E6 主要中銀ファンダメンタルズ（週次更新）</h3>
          <span>{TODAY} 現在</span>
        </div>
        <table class="fx-table">
          <thead><tr><th>中銀</th><th>通貨</th><th>政策金利</th><th>スタンス</th><th>背景・理由</th></tr></thead>
          <tbody>
{fundamentals_rows_html}          </tbody>
        </table>
        <p style="font-size:11px;color:var(--muted);margin:12px 0 0;">※ {TODAY}時点。各中銀の公式発表・公式サイトと複数の報道ソースで確認済み。前回更新（9/14）から日銀が1.00%→1.25%、FRBが3.50〜3.75%→3.75〜4.00%へそれぞれ利上げ。RBA（9/28-29）・SNB（9/25）は今週開催予定で本レポート作成時点では未開催のため直近据え置き水準を掲載しています。最新情報は各中銀の公式サイトでご確認ください。</p>
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
</html>"""

with open(f'reports/{TODAY}.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'reports/{TODAY}.html generated ({len(CALENDAR_ROWS)} calendar rows)')
