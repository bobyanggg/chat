#!/usr/bin/env python3
"""Assemble Tokyo+Yuzawa 2027 plan.geo.json from city research + Phase 1/3 facts."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path("/workspace/trips/tokyo-yuzawa-2027")
tokyo = json.loads((ROOT / "research-tokyo.json").read_text())
yuzawa = json.loads((ROOT / "research-yuzawa.json").read_text())

# Hand-filled coords (Nominatim is weak on Japanese names).
COORDS = {
    "成田機場": (35.7720, 140.3929),
    "京橋飯店": (35.6769, 139.7706),
    "一番街": (35.6812, 139.7671),
    "日本橋": (35.6825, 139.7744),
    "東京車站": (35.6812, 139.7671),
    "淺草寺": (35.7148, 139.7967),
    "新仲見世": (35.7118, 139.7946),
    "晴空塔": (35.7101, 139.8107),
    "東京國立博物館": (35.7188, 139.7765),
    "上野公園": (35.7148, 139.7714),
    "阿美橫丁": (35.7105, 139.7745),
    "新宿御苑": (35.6852, 139.7100),
    "都廳展望室": (35.6896, 139.6917),
    "回憶橫丁": (35.6934, 139.6995),
    "ガーラ湯沢駅": (36.9500, 138.8035),
    "GALA湯澤滑雪場": (36.9525, 138.8055),
    "NASPAニューオータニ 溫泉": (36.9348, 138.7972),
    "CoCoLo湯沢／ぽんしゅ館": (36.9360, 138.8093),
    "越後湯澤站（發車）": (36.9360, 138.8093),
    "越後湯澤站": (36.9360, 138.8093),
}


def apply_coords(stop):
    name = stop.get("name", "")
    for key, (lat, lon) in COORDS.items():
        if key in name or name in key:
            stop["lat"], stop["lon"] = lat, lon
            return stop
    return stop


def days_by_date(blob):
    return {d["date"]: d for d in blob["days"]}


td, yd = days_by_date(tokyo), days_by_date(yuzawa)

# --- 2/21: morning arrival half-day (JX800 pattern 12:35 NRT) ---
d21 = deepcopy(td["2027-02-21"])
d21["travel_day"] = True
d21["label"] = "成田抵達・東京車站／日本橋半日"
d21["note"] = (
    "晨班（星宇 JX800 冬型 08:25 TPE → 12:35 NRT，as of 2026-10-25 時刻表）落地後 "
    "入國＋N'EX 約 60 分，約 14:30–15:00 到京橋。15:00 前抵＝半日。不買票。"
)
d21["timeline"] = [
    {"t": "08:25-12:35", "what": "星宇 JX800 桃園→成田（冬型時刻；2027 班表 T-14 再核）",
     "kind": "hop", "verify": "est", "map": False, "tag": "pinned",
     "note": "直飛約 3 h 10。入國＋取行李預留 45–70 分。"},
    {"t": "13:20-14:25", "what": "N'EX 成田機場→東京站 約 60 分 大人約 ¥3,070（JR 東日本官網價型）",
     "kind": "hop", "verify": "est", "note": "指定席；週末＋連假後可能滿。備援京成 Skyliner 至日暮里再轉山手線。"},
    {"t": "14:25-15:00", "what": "步行 東京站→京橋飯店入住", "kind": "hop", "verify": "est"},
    {"t": "15:00-15:40", "what": "京橋／八重洲飯店入住、換 Suica／PASMO",
     "kind": "free", "tag": "pinned"},
    {"t": "15:40-16:50", "what": "東京車站一番街／GRANSTA 散步（免票、室內）",
     "kind": "free", "tag": "opener",
     "note": "營業律例 as of 2026-10-17，見原城日。"},
    {"t": "16:50-18:00", "what": "晚餐 · 八重洲／一番街", "kind": "meal",
     "tag": "swap→GRANSTA八重洲餐廳"},
    {"t": "18:10-18:40", "what": "日本橋夜景（可選）", "kind": "free", "tag": "skippable"},
]
d21["stops"] = [
    {"name": "成田機場", "query": "Narita Airport Terminal 2, Japan"},
    {"name": "東京車站", "query": "Tokyo Station, Japan", "mode": "train"},
    {"name": "京橋飯店", "query": "Mitsui Garden Hotel Kyobashi, Tokyo, Japan", "mode": "walk"},
    {"name": "一番街", "query": "東京駅一番街, 東京都千代田区", "mode": "walk"},
    {"name": "日本橋", "query": "Nihonbashi Bridge, Chuo-ku, Tokyo, Japan", "mode": "walk"},
]
d21["ribbon"] = "成田 →N'EX60′→ 東京站 →步行8′→ 京橋飯店 →步行8′→ 一番街 →步行12′→ 日本橋"
d21["late_cut"] = "落地晚於 15:00 → 砍日本橋，只留飯店＋一番街晚餐。"
d21["rain_alt"] = "主線已在室內（N'EX＋一番街）。雨大取消日本橋。"

# --- 2/27 merge Yuzawa morning + Tokyo afternoon ---
y27, t27 = deepcopy(yd["2027-02-27"]), deepcopy(td["2027-02-27"])
d27 = {
    "date": "2027-02-27",
    "tz": "Asia/Tokyo",
    "city": "湯澤 → 東京",
    "label": "午前溫泉・新幹線回東京・新宿半日",
    "travel_day": True,
    "rain_alt": "天氣差或趕車 → 取消短滑，只留溫泉＋ぽんしゅ館室內。抵東京後若雨：砍新宿御苑，改都廳展望室＋伊勢丹室內。",
    "late_cut": "10:30 還沒上纜車 → 不滑。新幹線晚於 14:30 抵東京站 → 砍御苑（冬季最後入園 16:00），行李進飯店後直奔都廳。",
    "ribbon": "NASPA溫泉 →接駁3′→ ぽんしゅ館 →新幹線70–80′→ 東京站 →步行8′→ 京橋飯店 →地鐵25–35′→ 新宿御苑 →地鐵→ 都廳",
    "walking_km": {"total": 4.2, "how": "湯澤站內 1.0 + 御苑 2.0 + 都廳 0.4 + 站步行×1.3（est）"},
    "note": "移動日：行李先解決再活動。錨點 ≤2（溫泉＋御苑）；都廳 skippable。上越新幹線 2026-27 冬臨時時刻截至 2026-10-17 未公布，以下為季型 70–80 分。",
    "timeline": [
        {"t": "08:00-08:30", "what": "湯澤飯店退房・行李放櫃或隨身上車",
         "kind": "free", "tag": "pinned"},
        {"t": "08:40-10:20", "what": "午前溫泉（NASPA 或站前旅館風呂）",
         "kind": "anchor", "tag": "opener", "price": "住宿客含；日歸大人¥1,500",
         "note": "三日滑雪後的恢復槽。短滑僅在行李已存且能 11:30 下山時才換。"},
        {"t": "10:40-12:00", "what": "午餐＋伴手禮 · CoCoLo／ぽんしゅ館",
         "kind": "meal", "tag": "skippable"},
        {"t": "12:20-13:50",
         "what": "上越新幹線 越後湯澤→東京 指定席 大人約¥7,330 · 約70–80分",
         "kind": "hop", "verify": "est", "price": "約¥7,330",
         "note": "2/27 週六指定席必訂。Smart-EX 開賣 2027-01-27 10:00 JST。票價 NAVITIME as of 2026-03-16。"},
        {"t": "13:50-14:20", "what": "步行 東京車站→京橋飯店寄行李／入住",
         "kind": "hop", "verify": "est"},
        {"t": "14:20-14:50", "what": "京橋飯店寄行李", "kind": "free", "tag": "pinned"},
        {"t": "14:50-15:25", "what": "地鐵 丸之內線 至新宿御苑前 約25–35分",
         "kind": "hop", "verify": "est"},
        {"t": "15:25-16:20", "what": "新宿御苑",
         "kind": "anchor", "tag": "opener",
         "price": "入場費 ⚠️ 本輪未核到官網數字（T-14 查 policies.env.go.jp）",
         "note": "冬季 9:00–16:30、最後入園 16:00（as of 2026-10-17）。晚到就砍，改都廳。"},
        {"t": "16:30-17:20", "what": "東京都廳第一本廳舍展望室（可選）",
         "kind": "anchor", "price": "免費", "tag": "skippable",
         "note": "9:30–22:00 as of 2026-10-17。室內、免費。"},
        {"t": "17:40-19:00", "what": "晚餐 · 回憶橫丁／新宿西口巷弄",
         "kind": "meal", "tag": "swap→伊勢丹美食層"},
    ],
    "stops": [
        {"name": "NASPAニューオータニ 溫泉", "query": "NASPA New Otani, Yuzawa, Niigata"},
        {"name": "CoCoLo湯沢／ぽんしゅ館",
         "query": "Ponshukan CoCoLo Yuzawa, Echigo-Yuzawa Station, Niigata", "mode": "bus"},
        {"name": "越後湯澤站（發車）", "query": "Echigo-Yuzawa Station 越後湯沢駅, Niigata"},
        {"name": "東京車站", "query": "Tokyo Station, Japan", "mode": "train"},
        {"name": "京橋飯店", "query": "Mitsui Garden Hotel Kyobashi, Tokyo, Japan", "mode": "walk"},
        {"name": "新宿御苑", "query": "新宿御苑, 東京都", "mode": "transit"},
        {"name": "都廳展望室",
         "query": "Tokyo Metropolitan Government Building South Observatory, Shinjuku",
         "mode": "transit"},
        {"name": "回憶橫丁", "query": "Omoide Yokocho, Shinjuku, Tokyo, Japan", "mode": "walk"},
    ],
}

d28 = deepcopy(td["2027-02-28"])
d28["timeline"] = [
    {"t": "T−4h30", "what": "京橋飯店退房", "kind": "free", "tag": "pinned",
     "note": "國際線 T−3 h 到航廈。例：NRT 15:30 起飛 → 約 11:00 離飯店。"},
    {"t": "T−4h20", "what": "步行 京橋飯店→東京車站", "kind": "hop", "verify": "est"},
    {"t": "T−3h50", "what": "N'EX 東京站→成田機場 約 60 分", "kind": "hop", "verify": "est"},
    {"t": "T−3h00", "what": "成田國際航廈報到", "kind": "free", "tag": "pinned"},
]
d28["stops"] = [
    {"name": "京橋飯店", "query": "Mitsui Garden Hotel Kyobashi, Tokyo, Japan"},
    {"name": "東京車站", "query": "Tokyo Station, Japan", "mode": "walk"},
    {"name": "成田機場", "query": "Narita Airport Terminal 2, Japan", "mode": "train"},
]
d28["ribbon"] = "京橋飯店 →步行8′→ 東京站 →N'EX60′→ 成田機場"

days = [
    d21,
    deepcopy(td["2027-02-22"]),
    deepcopy(td["2027-02-23"]),
    deepcopy(yd["2027-02-24"]),
    deepcopy(yd["2027-02-25"]),
    deepcopy(yd["2027-02-26"]),
    d27,
    d28,
]

for d in days:
    d["tz"] = "Asia/Tokyo"
    d["stops"] = [apply_coords(s) for s in d.get("stops", [])]
    # 2/24 first stop is GALA station — add Tokyo Station origin for the train hop
    if d["date"] == "2027-02-24":
        d["stops"] = [
            apply_coords({"name": "東京車站", "query": "Tokyo Station, Japan"}),
            *d["stops"],
        ]
        # arriving GALA station already has mode train

GF = (
    "https://www.google.com/travel/flights?q="
    "Flights%20from%20TPE%20to%20NRT%20on%202027-02-21%20returning%202027-02-28%20for%202%20adults"
)
SKY = (
    "https://www.skyscanner.net/transport/flights/tpe/nrt/270221/270228/"
    "?adultsv2=2&cabinclass=economy&rtn=1&preferdirects=true&currency=TWD&locale=zh-TW"
)
KAYAK = "https://www.kayak.com/flights/TPE-NRT/2027-02-21/2027-02-28/2adults?sort=bestflight_a"

plan = {
    "trip": "雪泥鴻爪 — 東京・湯澤 2027",
    "lang": "zh",
    "tz": "Asia/Tokyo",
    "cover": {
        "zh": "雪泥鴻爪",
        "en": "Traces in the Snow",
        "sub": "應似飛鴻踏雪泥 — 蘇軾《和子由澠池懷舊》",
        "credit": "—— 蘇軾（公版）",
        "kick": "東京・湯澤 2027",
        "kick_en": "TOKYO · YUZAWA 2027",
    },
    "prefs": {
        "theme": "illustrated",
        "pictures": "stock",
        "travel_style": "public",
        "lodging": "hotel · mid-range, refundable；湯澤可改溫泉旅館",
        "scenery": ["city", "mountain"],
        "pace": 3,
        "budget": "mid",
        "notes": (
            "assumed origin TPE（繁中提問、未寫出發地，取台灣最大國際門戶桃園）；"
            "護照中華民國；2 成人；大眾運輸；中檔可退房；主題 illustrated／stock；"
            "無生圖能力。日期取 2027-02-21（日）→ 02-28（日）覆蓋「2/22 那週」，"
            "並接上台灣 228 連假前段（2/28 和平紀念日、3/1 補假未納入除非加一天）。"
        ),
    },
    "meta": {
        "dates": "2027-02-21 → 2027-02-28",
        "party": "2 成人，中華民國護照，不自駕",
        "route": "台北桃園 → 成田 → 東京 → 湯澤 → 東京 → 成田 → 台北",
        "budget_total": "約 TWD 11–13 萬／兩人（含來回機票、中檔住宿、滑雪券＋租借、新幹線）",
        "fx": "1 TWD = 4.87 JPY（open.er-api.com, 2026-10-17 — frankfurter 無 TWD）",
        "generated": "2026-10-17",
        "self_check": (
            "自检:发现并修复 9 处 — "
            "(1) 2/27 東京與湯澤兩份日程撞日，合併為一移動日、錨點壓到 2；"
            "(2) 2/21 晨班 12:35 抵成田＝半日而非零觀光，把散步提前到下午；"
            "(3) 2/23 天皇誕生日改排上野室內、滑雪改平日 24–26 避開雪場人潮；"
            "(4) 2/22 月曜閉館博物館全部拿掉；"
            "(5) GALA 南區 2026-27 關閉寫進滑雪日；"
            "(6) 保險必須加滑雪特定活動，一般旅平險常除外；"
            "(7) 湯澤座標手填，避免 Nominatim 誤指秋田湯澤；"
            "(8) 直通谷川號 2026-27 PDF 未出，備援改越後湯澤＋接駁；"
            "(9) 匯率改 open.er-api（frankfurter 無 TWD）。"
        ),
        "headless_note": (
            "無互動確認：出發地依繁中推斷為 TPE；骨架自選「東京 3 晚＋湯澤 3 晚＋東京 1 晚」。"
            "本次沒有生圖能力，頁面用內建插畫素材（仍是成品頁，只是不如定制圖貼合）；"
            "有 OpenRouter key 的話放進 themes/.auth_header 再告訴我，就能為這趟生成。"
        ),
    },
    "decisions": [
        "骨架選東京 3 晚（21–24）→ 湯澤 3 晚（24–27）→ 東京 1 晚（27–28）。滑雪放週三至週五，避開 2/23 天皇誕生日雪場人潮。",
        "國際線飛成田不飛羽田：晨班星宇／華航進成田約中午到，當日還能進東京；價在 JAL／星宇 2027-02 月曆約 TWD 1.5 萬起。備援羽田／松山。",
        "雪場主場 GALA（站內直結）。本季南區關閉、場地變小；風停改岩原或湯澤高原，不空等。",
        "不住天天換飯店。大件 2/23 晚宅急便東京→湯澤，車上只留過夜包＋滑雪衣。",
        "自检:发现并修复 9 处 — 見 meta.self_check。",
    ],
    "checklist": [
        {
            "item": "確認免簽證入境條件（台灣護照、身分證字號、來回機票＋住宿證明）",
            "deadline": "出發前核對（規則可能變）",
            "price": "免簽證 90 日觀光",
            "link": "https://www.koryu.or.jp/tw/visa/taipei/exemption/",
            "note": "日本台灣交流協會；BOCA 同步 90 日。護照效期須覆蓋停留。入境可能問行程／財力。",
        },
        {
            "item": "旅遊門診（疫苗／預防用藥諮詢，本計畫不開處方）",
            "deadline": "出發前 4–6 週＝2027-01-10 前；已更近就本週約",
            "price": "依診所",
            "link": "https://wwwnc.cdc.gov/travel/destinations/traveler/none/japan",
            "note": "議程：常規疫苗＋麻疹（CDC Level 1, 2025-05-28）；A 肝（多數旅客考慮）；B 肝（60 歲以下未接種）；日本腦炎（冬山區短住通常不需要，仍問醫師）。",
        },
        {
            "item": "旅遊保險（必須含休閒滑雪／單板；一般旅平險常把雪上運動除外）",
            "deadline": "現在（有地震＋雪季門檻；世界一動再買可能被除外）",
            "price": "依保單",
            "link": "https://www.cathay-ins.com.tw/cathayins/personal/travel/activities/",
            "note": "向承辦人講明「日本雪場內休閒滑雪／單板」。保留雪場事故證明。急難電話填進保單後再寫進 brief。",
        },
        {
            "item": "雪季／地震危害閘門：GALA 營運＋JMA 警報",
            "deadline": "T-7 與每日出門前；免費取消截止日前可改期",
            "price": "—",
            "link": "https://gala.co.jp/winter/",
            "note": "官方季：2026-12-19～2027-05-05 計畫滑走。弱雪年可能提前收。強風／暴雪改室內溫泉。住宿保持可退到閘門。",
        },
        {
            "item": "來回機票 TPE↔NRT（或 TPE/TSA↔HND）2 成人",
            "deadline": "現在比價；可退／可改優先",
            "price": "約 TWD 15,000–18,000／人來回（JAL 2027-02 月曆 TWD 15,023 起；星宇 TWD 14,629 起；as of 2026-10-17）",
            "link": GF,
            "link_text": "Google Flights",
            "note": "fast-flights 3.1 API 對不上舊掃描器，Google 格點失敗。第二來源：JAL＋星宇官網月曆。無瀏覽器。2/21–28 當日價可能因假日偏高。",
        },
        {
            "item": "東京京橋／八重洲飯店 3 晚 2027-02-21→02-24（可退）",
            "deadline": "現在訂可退；出發前 2–3 週再比一次",
            "price": "約 ¥18,000–25,000／晚（Ikyu as of 2026-10-17，非 2027 實價）",
            "link": "https://www.booking.com/searchresults.html?ss=Mitsui+Garden+Hotel+Kyobashi+Tokyo&checkin=2027-02-21&checkout=2027-02-24&group_adults=2&no_rooms=1&order=review_score_and_price",
        },
        {
            "item": "湯澤飯店 3 晚 2027-02-24→02-27（可退）",
            "deadline": "現在訂可退",
            "price": "NASPA 一泊二食大人 ¥21,800 起（官網 as of 2026-10）；站前東映／雙葉查 Booking",
            "link": "https://www.booking.com/searchresults.html?ss=Echigo-Yuzawa+Niigata&checkin=2027-02-24&checkout=2027-02-27&group_adults=2&no_rooms=1&lang=zh-tw",
        },
        {
            "item": "東京京橋 1 晚 2027-02-27→02-28（可退）",
            "deadline": "現在訂可退",
            "price": "約 ¥18,000–27,000／晚（週六可能偏高）",
            "link": "https://www.booking.com/searchresults.html?ss=Mitsui+Garden+Hotel+Kyobashi+Tokyo&checkin=2027-02-27&checkout=2027-02-28&group_adults=2&no_rooms=1&order=review_score_and_price",
        },
        {
            "item": "Smart-EX 指定席：東京→ガーラ湯沢或越後湯澤（2027-02-24）",
            "deadline": "開賣 2027-01-24 10:00 JST",
            "price": "大人指定席約 ¥7,330（NAVITIME as of 2026-03-16）",
            "link": "https://smart-ex.jp/",
            "note": "天皇誕生日翌日早班可能滿。備援：上越新幹線至越後湯澤＋GALA 免費接駁約 10 分。",
        },
        {
            "item": "Smart-EX 指定席：越後湯澤→東京（2027-02-27 午後）",
            "deadline": "開賣 2027-01-27 10:00 JST",
            "price": "量級同去程",
            "link": "https://smart-ex.jp/",
        },
        {
            "item": "GALA WEB 纜車券（2/24 全日或 4 小時、2/25–26 全日）",
            "deadline": "出發前數日",
            "price": "全日 WEB 大人 ¥7,500／窗口 ¥8,000（gala.co.jp as of 2026-10-17）",
            "link": "https://gala.co.jp/winter/hours-pricing/",
            "note": "南區 2026-27 關閉。超早割已完售。",
        },
        {
            "item": "東京晴空塔網上入場券（2027-02-22）",
            "deadline": "出發前數日",
            "price": "天望デッキ大人 ¥1,800 起（官網 as of 2026-10-17）",
            "link": "https://www.tokyo-skytree.jp/ticket/",
        },
        {
            "item": "宅急便：東京飯店→湯澤飯店（2/23 晚交件）",
            "deadline": "2027-02-23 晚、依飯店截止",
            "price": "按件計（不編造）",
            "link": "https://www.kuronekoyamato.co.jp/",
        },
        {
            "item": "護照影本 ×2＋保單／機票雲端備份；出國登錄",
            "deadline": "出發前",
            "price": "免費",
            "link": "https://www.boca.gov.tw/sp-abre-main-1.html",
            "note": "領事事務局出國登錄或 LINE @boca.tw。",
        },
        {
            "item": "T-14 再核：錨點時刻與票價、警示燈號、免簽規則、GALA 積雪",
            "deadline": "T-14 · 2027-02-07",
            "note": "淺草寺、東博、晴空塔、新宿御苑、GALA 營業、新幹線時刻、JAL／星宇當日價。",
        },
        {
            "item": "T-7 再核：東京／湯澤預報，套用寒冷／強風規則",
            "deadline": "T-7 · 2027-02-14",
            "note": "湯澤 2 月平年雨雪日占比高。強風停纜→ NASPA／ぽんしゅ館。",
        },
        {
            "item": "T-3 再核：JR 東日本延誤、雪場關閉、機票已在錢包",
            "deadline": "T-3 · 2027-02-18",
            "note": "https://www.jreast.co.jp/ ＋ gala.co.jp 營運。",
        },
        {
            "item": "T-1：eSIM 可收簡訊、現金、卡未鎖、雪具租借時間",
            "deadline": "T-1 · 2027-02-20",
            "note": "eSIM 約 TWD 300–500／週。現金約 TWD 4,000–6,000 等值日圓（小店／食堂）。",
        },
    ],
    "legs": [
        {
            "type": "international flight",
            "date": "2027-02-21",
            "carrier": "星宇航空 JX800（冬型）／備援華航 CI100",
            "from": "TPE",
            "to": "NRT",
            "dep": "08:25",
            "arr": "12:35",
            "price": "TWD 14,600–18,000／人來回（兩人合計約 TWD 29,000–36,000）",
            "bags": "經濟艙通常含 1×23 kg；以訂位艙等為準（Basic 可能僅手提）",
            "link": GF,
            "note": (
                "來源：星宇官網 2027-02 月曆 TWD 14,629 起；JAL 2027-02 月曆 TPE–NRT "
                "TWD 15,023 起（例 2027-02-12–17）；長榮其他 2027 日期 TWD 17,860 起。"
                "as of 2026-10-17。Google 格點掃描失敗（fast-flights 3.1 API）。無瀏覽器。"
                "時刻為 2026-10-25 起冬型，2027-02 班表 T-14 再核。不可退廉價艙勿先鎖。"
            ),
            "backup": (
                "華航 CI100 冬型 09:30 TPE→13:30 NRT（2026-10-29 起）。"
                "或松山 TSA→羽田 HND（市區到市區；Kayak 寫 2 月均價偏高）。"
                "Skyscanner: " + SKY
            ),
        },
        {
            "type": "international flight",
            "date": "2027-02-28",
            "carrier": "星宇／華航 成田午後回桃園（與去程同一張來回票）",
            "from": "NRT",
            "to": "TPE",
            "dep": "15:00",
            "arr": "18:10",
            "price": "含在去程來回價",
            "bags": "同去程",
            "link": GF,
            "note": (
                "回程鐘點 Google 第一頁不顯示；上列 15:00 為規劃用午後視窗，不是已核班表。"
                "訂位後用 T−3 h 到航廈改寫 2/28。第二來源同去程官網月曆。"
            ),
            "backup": "改晚班則 2/28 整天是機場日；改羽田則改單軌／京急。",
        },
        {
            "type": "shinkansen",
            "date": "2027-02-24",
            "carrier": "JR 東日本 上越新幹線 たにがわ／とき",
            "from": "東京",
            "to": "ガーラ湯沢（或越後湯澤）",
            "dep": "08:00",
            "arr": "09:30",
            "price": "大人指定席約 ¥7,330（約 TWD 1,500；NAVITIME as of 2026-03-16）",
            "bags": "合計三邊 >160 cm 的箱子在上越線通常沒東海道那種強制指定席，仍建議不要拖大箱；用宅急便",
            "link": "https://smart-ex.jp/",
            "note": "直通ガーラ湯沢 2025-26 冬每日有；2026-27 臨時 PDF 截至 2026-10-17 未出。時刻為季型。可退／改依 JR 規定。",
            "backup": "東京→越後湯澤（約 70–80 分）＋ GALA 免費接駁約 10 分。",
        },
        {
            "type": "shinkansen",
            "date": "2027-02-27",
            "carrier": "JR 東日本 上越新幹線",
            "from": "越後湯澤",
            "to": "東京",
            "dep": "12:20",
            "arr": "13:50",
            "price": "大人指定席約 ¥7,330（約 TWD 1,500）",
            "bags": "overnight 包上車",
            "link": "https://smart-ex.jp/",
            "note": "週六指定席必訂。開賣 2027-01-27 10:00 JST。",
            "backup": "下一班とき／たにがわ；不要為了多滑一小時趕末班。",
        },
    ],
    "days": days,
    "hotels": tokyo["hotels"] + yuzawa["hotels"],
    "budget": [
        {"cat": "來回機票", "per_person": "TWD 15,000–18,000",
         "total": "TWD 30,000–36,000",
         "note": "JAL＋星宇官網月曆 as of 2026-10-17；2/21–28 當日可能更高"},
        {"cat": "東京住宿 4 晚", "per_person": "TWD 9,000–13,000",
         "total": "TWD 18,000–26,000",
         "note": "¥18,000–25,000／晚×4；兩人一室。Ikyu 帶寬 as of 2026-10-17"},
        {"cat": "湯澤住宿 3 晚", "per_person": "TWD 7,000–14,000",
         "total": "TWD 14,000–28,000",
         "note": "站前中檔或 NASPA 一泊二食。含餐則下面餐費可少"},
        {"cat": "新幹線來回", "per_person": "TWD 3,000",
         "total": "TWD 6,000", "note": "¥7,330×2 as of 2026-03-16"},
        {"cat": "GALA 纜車 2.5–3 日", "per_person": "TWD 4,600–4,600",
         "total": "TWD 9,200", "note": "WEB ¥7,500×3 as of 2026-10-17"},
        {"cat": "雪具租借", "per_person": "TWD 4,000",
         "total": "TWD 8,000", "note": "2025-26 季型 ¥6,500／日×3；2026-27 未公布"},
        {"cat": "餐食（東京為主）", "per_person": "TWD 6,000–8,000",
         "total": "TWD 12,000–16,000", "note": "湯澤若一泊二食可再少"},
        {"cat": "地鐵／N'EX／門票", "per_person": "TWD 3,500",
         "total": "TWD 7,000", "note": "含晴空塔、東博、N'EX"},
        {"cat": "保險＋eSIM", "per_person": "TWD 1,500–2,500",
         "total": "TWD 3,000–5,000", "note": "滑雪附加險另計"},
        {"cat": "緩衝 12%", "per_person": "TWD 6,500",
         "total": "TWD 13,000", "note": "含卡國外交易費 1.5–3%、日圓波動、假日漲價"},
    ],
    "brief": {
        "visa": (
            "免簽證 90 日觀光（持有效台灣護照且載有身分證字號）· 免費 · 當場入境審查、無預先申請。"
            "護照須在停留期間有效（未規定剩餘 6 個月）。備來回機位、住宿、行程、財力備詢。"
            "不得有償工作。直飛 TPE–NRT，無第三國入境、無拆票轉機。"
            "來源：koryu.or.jp 免簽證頁、BOCA 免簽證表（更新 2026-10-07）· as of 2026-10-17。"
        ),
        "emergency": (
            "1 當地：警察 110 · 急救／消防 119（UK FCDO getting-help · as of 2026-08-28）。\n"
            "2 台灣：外交部緊急聯絡中心 0800-085-095（國內）；海外 +886-800-085-095（verify at boca.gov.tw）。\n"
            "3 最近館：台北駐日經濟文化代表處，東京都港區白金台 5-20-2，"
            "03-3280-7811；急難 080-1009-7179／夜間警衛 03-3280-7917；"
            "領務 週一–五 09:00–11:30、13:00–16:00（roc-taiwan.org/jp · as of 2026-10-17）。湯澤同轄區（新潟）。\n"
            "4 保險：保單協助電話＋保單號（你買完再填）。先打電話再送醫；要明細收據。\n"
            "5 護照遺失：先報案留收據 → 代表處緊急旅行文件（照片＋影本＋報案）→ 再處理出境。\n"
            "6 東京 ER：聖路加國際病院 中央區明石町 9-1，03-3541-5151（救命救急中心；as of 2026-10-17）。"
            "湯澤：先打 025-780-6543 湯澤町保健醫療中心，或 119；魚沼基幹病院 025-777-3200（南魚沼市浦佐，車程視雪況）。"
            "藥局＝薬局／ドラッグストア。"
        ),
        "safety": (
            "警示: 灰色提醒（第一級）· 外交部領事事務局 · as-of 2025-12-30"
            "（第二來源：美國 Level 1 Exercise Normal Precautions · as-of 2025-05-14；"
            "英國 FCDO 無額外 alert · as-of 2026-08-28）。福島縣「返回困難區域」避免；本行程不經過。\n"
            "① 詐騙：酒吧／夜店帳單灌水、飲料下藥刷卡（FCDO：東京娛樂區夜間）。\n"
            "② 扒手：電車高峰、淺草仲見世、新宿西口。女乘客注意癡漢；大聲喊、找車掌。\n"
            "③ 計程車：用 GO／Uber 或站內計程車排班；不要跟大廳攬客。成田／羽田坐官方排班或 N'EX／單軌。\n"
            "④ 天黑後：新宿歌舞伎町、澀谷中心街酒客多；本行程夜路走飯店圈或地鐵門到門。湯澤站前冬天路滑，穿防滑靴。\n"
            "⑤ 出事：先報案（報案號是理賠鑰匙）→ 代表處／保險。\n"
            "⑥ 法律：偽麻黃鹼感冒藥／部分止痛藥入境違法；肉製品不可帶；現金申報門檻 >¥1,000,000。"
        ),
        "health": (
            "1 疫苗：常規＋麻疹；A 肝多數旅客考慮；B 肝 60 歲以下未接種建議；"
            "日本腦炎僅長期／農村／露營才考慮（2 月雪場短住通常不需要）。黃熱病：不建議、入境不要求（CDC 更新 2025-04-23）。"
            "門診日期：出發前 4–6 週。本計畫不開處方。\n"
            "2 病媒：登革（CDC 列；2 月低）；日本腦炎夏季農村；鉤端螺旋體（洪水／淡水）。雪場主要是凍傷、跌倒、紫外線。\n"
            "3 水與食物：自來水可飲（JNTO educational travel · as of 2026-10-17）。"
            "CDC 頁未寫死可飲。TravelHealthPro 因血吸蟲提醒勿涉溪湖淡水——不是自來水。神社手水舍不要喝。\n"
            "4 狂犬病：日本犬隻病例不常見；勿摸野動物；咬傷先沖 15 分再 ER。\n"
            "5 衛生警示：CDC Level 1 麻疹 · 2025-05-28 · https://wwwnc.cdc.gov/travel/destinations/traveler/none/japan"
        ),
        "holidays": (
            "日本：2027-02-23 天皇誕生日（火曜祝日）— 雪場與新幹線擠、部分店休；"
            "東博按律例應開（月曜休、普通月曜 2/22 休、祝日火曜開）。來源 date.nager.at 2027/JP。\n"
            "台灣：2027-02-28 和平紀念日（日）於 3/1（一）補假，連假 2/27–3/1（人事總處 116 年辦公日曆）。"
            "本行程 2/28 回台，不使用 3/1。農曆春節 2/4–10 已過。"
        ),
        "weather": (
            "東京 2/21–28：5 年檔最高中位 11.4°C、最低 2.0°C、降雨日約 20%、最濕 49.7 mm；"
            "氣候模式均溫最高 10.4／最低 1.0、日雨 1.9 mm。"
            "湯澤（新潟町，非秋田）：5 年檔最高 4.2°C、最低 −3.7°C、降水日約 70%；"
            "氣候模式最高 2.2／最低 −5.0、日降水 6.5 mm（冬季多為雪）。"
            "氣象廳湯澤平年 2 月最深積雪 202 cm、降雪合計 288 cm（1991–2020）。"
            "· 5-yr normals + climate model · Open-Meteo as-of 2026-10-17。"
        ),
        "money": (
            "1 DCC：刷卡選日圓，不要機台自動換成台幣（一次 3–8%）。\n"
            "2 卡國外交易費：旅遊卡 0%；一般卡 1.5–3% → 緩衝列已加。\n"
            "3 ATM：7-Eleven／郵局較吃國外卡；銀行大廳機、遮 PIN；單次上限現場看、費用 check on arrival。\n"
            "4 現金：帶約 TWD 4,000–6,000 等值日圓（小食堂、神社、部分湯澤店）。入境申報門檻 >¥1,000,000。\n"
            "5 接受：Visa／Mastercard 廣；UnionPay／Alipay+ 大城市可以、雪場食堂不一定。Suica 可當小額電子錢。"
        ),
        "connectivity": (
            "eSIM 約 TWD 300–500／7 日（Airalo／eSIM 商城；出發前買）。插頭 A／B 型 100 V。"
            "數位安全：eSIM 仍要收得到家門號簡訊（銀行 2FA）；Find My＋SIM PIN；"
            "護照／保單雲端＋離線；公共 Wi-Fi 不網銀。"
        ),
        "insurance": (
            "要有海外醫療＋醫療運送。滑雪／單板常在除外清單——必須加「特定活動」或條款點名滑雪。"
            "國泰特定活動險頁有列滑雪但須洽據點；富邦網路旅平險與快樂旅平卡通路不同。"
            "買完核對：目的地日本、等待期、滑雪是否列名、急難電話。"
            "雪場事故要留經營者證明。門檻：有地震＋雪季，現在買。"
        ),
        "baggage": (
            "去程大件進東京飯店。2/23 晚宅急便東京→湯澤（翌日達），新幹線只帶過夜包＋雪衣。"
            "回程 2/26 晚再寄東京趕不上 2/27 車就隨身。GALA 有置物與宅配櫃檯。"
            "N'EX／新幹線不要賭超大置物櫃。"
        ),
        "season": (
            "地震全年（JMA／USGS）· 沿海知高地；湯澤在內陸山區，仍可能停駛新幹線。\n"
            "雪季／雪崩：2 月是上越雪國主季，不是尾聲。GALA 計畫滑到 2027-05-05，但弱雪年會提早收"
            "（2026 年滑走 4/17 結束）。南區本季關閉。保險現在買；雪場住宿保持可退；T-7 看積雪與風停。"
            "來源：gala.co.jp hours-pricing、JMA 平年、SnowJapan 歷年積雪 · as of 2026-10-17。"
        ),
        "lookalikes": (
            "湯澤有秋田湯澤市、山形、神奈川——本行程是新潟縣南魚沼郡湯沢町／越後湯澤。"
            "飯店搜尋寫 Echigo-Yuzawa, Niigata。成田 NRT 與羽田 HND 不要混；松山 TSA 是另一座出發機場。"
        ),
    },
    "unverified": sorted(set(
        tokyo.get("unverified", []) + yuzawa.get("unverified", []) + [
            "2027-02-21／02-28 實際航班號與回程鐘點未鎖；去程用 2026-10-25 起 JX800 冬型。",
            "Google Flights 格點掃描失敗（fast-flights 3.1 無 FlightData）。",
            "新宿御苑門票金額未核到官網。",
            "2026-27 冬 JR 直通ガーラ湯沢時刻表未公布。",
        ]
    )),
}

(ROOT / "plan.geo.json").write_text(
    json.dumps(plan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
)
print("wrote", ROOT / "plan.geo.json", "days", len(plan["days"]))
