# 雪泥鴻爪 — 東京・湯澤 2027-02-21→28

問的是「2/22 那週東京／湯澤還有雪可滑嗎」。答案寫在 `plan.geo.json` 的 `brief.season`：東京沒有穩定滑雪雪；湯澤／GALA 2 月下旬通常還在主季。

打開順序：

1. `trip.html`（或同內容的 `trip-illustrated.html`）— 可訂連結的行程頁
2. `gates.ics` — 出發前閘門（匯入行事曆）
3. `trip.kml` — 離線地圖

來源檔是 `plan.geo.json`。改行程只改這份，再跑：

```
python3 .cursor/skills/trip-planner/scripts/route_tools.py check plan.geo.json
python3 .cursor/skills/trip-planner/scripts/plan_lint.py plan.geo.json --strict
python3 .cursor/skills/trip-planner/scripts/render_plan.py plan.geo.json -o trip.html --lang zh
```

本環境沒有 `themes/`（插畫主題渲染器沒有跟著 skill 進來），所以成品是 `render_plan.py` 的素頁，不是 illustrated 插畫頁。

餐廳／活動表在 repo 的 `japan-trip/Tokyo Trip Plan.md` 與 `japan-trip/Yuzawa Trip Plan.md`。
