---
topic: "我這一生最大的罪，是把人寫成了妖（Bilibili AI 短片）製作技術與作品拆解"
type: "product"
goals: "確認作品出處與作者；釐清影像、生圖與後製用了哪些模型與流程；評估技術能力、限制與爆紅原因"
date: "2026-09-07"
methodology: "Parallel web research via sub-agents. Citations inline per references/citations.md. Confidence levels: High / Medium / Low. Steps 2–5 completed 2026-09-07. Standard depth (no Step 4.5 outline rewrite)."
---

# Research Report — 我這一生最大的罪，是把人寫成了妖

> **Type:** product（兼 technical：生成式影像管線） | **Date:** 2026-09-07 | **Constraints:** 以公開報導、官方模型說明與創作者自述為主；無法取得未公開 prompt 或專案檔。Bilibili 影片頁在本環境回傳 HTTP 412，無法直接刮取，頁面數據依新聞轉述。
>
> **Goals:**
> - 確認這句話出自哪部作品、誰做的、何時上線
> - 釐清「是用哪些技術完成的」：生圖、生影片、聲音、剪輯與角色一致性做法
> - 對照 Seedance 2.5、GPT Image 2 等工具的官方能力與業界用法
> - 說明文學出處（《搜神記》）與爆紅、爭議脈絡
>
> **Assumptions:** type=product（特定作品拆解）+ technical（生成模型與製作管線）；scope=這部約 26 分鐘的 Bilibili AI 短片及其公開承認的工具鏈；horizon=2026-08 上線至 2026-09-07；不做未證實的政治結論。

---

## Product Overview

### Identity, Creator, and Release

這句話不是古書原句，也不是傳統電視劇臺詞。它是 2026 年 8 月一部 AI 古裝短片的片名單，完整標題寫作《我这一生最大的罪，是把人写成了妖……》（繁體常見寫法《我這一生最大的罪，是把人寫成了妖……》）。媒體多簡稱《把人写成了妖》／《把人寫成了妖》；片內或別名作《妖异簿·问苍生》／《妖異簿·問蒼生》。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）把長標題當官方名、短標題當俗稱；同報另一篇評論把片內作品名寫成《妖异簿·问苍生》。[聯合早報（繆宗翰）](https://www.zaobao.com.sg/news/china/story20260825-9566923)（accessed 2026-09-07, confidence: Medium）。多篇報導引用同一 Bilibili 網址 `https://www.bilibili.com/video/BV1rHbY6MEB9/`。[NOWnews](https://www.nownews.com/news/6868562)（accessed 2026-09-07, confidence: High）。一份產業筆記還記下上傳時間 2026-08-17 13:39:57（+08）、片長 26 分 14 秒、畫面 1920×1080；該來源屬 **Low** 層，片長 26 分鐘本身則有多家主流媒體交叉證實。[Neodrop](https://neodrop.ai/post/zt98qIKWm5N)（accessed 2026-09-07, confidence: Low）。

作者是 Bilibili UP 主 **青瓜蛋丶**（報導常寫成青瓜蛋；英文常見 Qinggua Dan）。沒有公開真名、製片公司或傳統演職員表。多家媒體把它寫成一人作業：劇本改自作者幾年前的隨筆，畫面用 ByteDance Seedance 2.5 與 OpenAI GPT Image 2 生成，沒有真人演員與實景拍攝。[聯合新聞網／噓！星聞](https://stars.udn.com/star/story/10091/9713666)（accessed 2026-09-07, confidence: High）；[NOWnews](https://www.nownews.com/news/6868562)（accessed 2026-09-07, confidence: High）；[ETtoday](https://star.ettoday.net/news/3223651)（accessed 2026-09-07, confidence: High）。新榜把該帳號列為 2026 年 8 月 17–23 日 B 站漲粉榜第五，當週新增超過 12 萬粉絲，並稱其為「AI 導演」。[新榜 NewRank](https://newrank.cn/article/detail/34701)（accessed 2026-09-07, confidence: Medium）。西瓜視頻一則標為 2026-08-16 的《问苍生》頁帶有抖音 AI 創作大賽等標籤，這暗示 B 站 8 月 17 日上傳前，可能已有抖音／西瓜賽道版本；該頁快照顯示約 18 萬粉絲、23 支影片。[西瓜視頻](https://m.ixigua.com/dx/7674459865061887267)（accessed 2026-09-07, confidence: Medium）。一份 **Low** 層筆記稱簽名檔為「即梦 AI 超级创作者」並留有商務微信；本報告不當成已核實身份。[Neodrop](https://neodrop.ai/post/zt98qIKWm5N)（accessed 2026-09-07, confidence: Low）。

上線日期以 **2026 年 8 月 17 日、Bilibili** 為共識，聯合早報、UDN、NOWnews、ETtoday、世界新聞網、香港 01、虛詞皆如此寫。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）；[UDN](https://udn.com/news/story/7332/9709067)（accessed 2026-09-07, confidence: High）。聯合早報 9 月 3 日娛樂稿寫明全片標示 **「含AI生成内容」**，無人出演，截稿時仍可看、且仍列在「每周必看」。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: Medium，因標示原文僅一家 Established 媒體完整寫出）。作品被明確標為虛構：B 站簡介（經 UDN、世界新聞網、ETtoday、NOWnews 轉述）寫故事與人物皆虛構，靈異取材東晉干寶《搜神記》漢代災異，再與黃巾起義史事虛構演繹。[UDN](https://udn.com/news/story/7332/9709067)（accessed 2026-09-07, confidence: High）。爆紅後，作者 8 月 18 日在影片下留言被廣泛轉載：他寫「一觉醒来还以为被网暴了」；劇本來自幾年前隨筆；工具是 Seedance 2.5 與 GPT Image 2；並聲明「本片艺术加工成分居多，情节皆为虚构演绎，并非真实历史」，請觀眾辯證看待歷史人物。[UDN](https://udn.com/news/story/7332/9709067)（accessed 2026-09-07, confidence: High）；[ETtoday](https://star.ettoday.net/news/3223651)（accessed 2026-09-07, confidence: High）。

播放量必須按報導日期讀，不能合成一個數。8 月 22 日 NOWnews 寫已破千萬。[NOWnews](https://www.nownews.com/news/6868284)（accessed 2026-09-07, confidence: Medium）。8 月 23 日 15:00，UDN 與世界新聞網同寫 **1,272 萬**；同日 NOWnews 科技稿寫 **1,285–1,286 萬**。[UDN](https://udn.com/news/story/7332/9709067)（accessed 2026-09-07, confidence: High）；[NOWnews](https://www.nownews.com/news/6868562)（accessed 2026-09-07, confidence: High）。8 月 24 日，UDN 噓！星聞寫破 1,300 萬；聯合早報 8 月 25 日評論用同一截止點寫超過 1,300 萬播放、超過 100 萬讚，並曾全站第一。[UDN 噓！星聞](https://stars.udn.com/star/story/10091/9713666)（accessed 2026-09-07, confidence: High）；[聯合早報（繆宗翰）](https://www.zaobao.com.sg/news/china/story20260825-9566923)（accessed 2026-09-07, confidence: High）。8 月 25 日風傳媒寫當日上午 **1,446.9 萬**；虛詞寫近 1,500 萬播放、130 萬讚、逾 100 萬投幣；新浪微博彙整寫 1,473 萬與第 387 期每周必看。[風傳媒](https://www.storm.mg/lifestyle/11159055)（accessed 2026-09-07, confidence: Medium）；[虛詞](https://p-articles.com/heteroglossia/6178.html)（accessed 2026-09-07, confidence: Medium）。Marie Claire 台灣 8 月 27 日更新寫 **1,589.8 萬** 次觀看。[Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: Medium）。8 月 28 日出現衝突：香港 01 寫 **1,447 萬**，低於前幾日若干數字；DailyView 寫 **1,633 萬** 且全站第一。[香港 01](https://www.hk01.com/%E9%9B%BB%E5%BD%B1/60384498/ai%E7%9F%AD%E5%8A%87-%E6%8A%8A%E4%BA%BA%E5%AF%AB%E6%88%90%E4%BA%86%E5%A6%96-%E6%87%B6%E4%BA%BA%E5%8C%85-%E7%B6%B2%E6%B0%91%E5%B0%81%E7%A5%9E%E4%BD%9C10%E5%A4%A7%E9%87%8D%E9%BB%9E%E4%B8%80%E6%96%87%E7%9C%8B%E6%87%82%E9%9A%B1%E5%96%BB)（accessed 2026-09-07, confidence: Medium）；[DailyView](https://dailyview.tw/popular/detail/33698)（accessed 2026-09-07, confidence: Medium）。聯合早報 9 月 3 日稿以 9 月 2 日為截止，寫播放已 **突破 1,800 萬**。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）。沒有來源公布完播率或獨立觀看人數。

### Target Audience

報導描述的實際觀眾，首先是 Bilibili 愛留言、已在看 AIGC 與中長片的使用者，其次是古裝劇與《搜神記》／黃巾史讀者，再次是追蹤 AI 影像技術的人。聯合早報與 UDN 都寫：先被皮膚質感、運鏡、二十六分鐘角色穩定嚇到，討論才轉到劇本與「后人读妖，勿问鬼神，问苍生」這類句子。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）；[UDN](https://udn.com/news/story/7332/9709067)（accessed 2026-09-07, confidence: High）。DailyView 的 KEYPO 掃描（2026-08-21 至 27 日）找到 3,162 筆華語網提及「把人写成妖」，搜尋聚在作者名、別名「问苍生」與跪／黃天等金句，並溢到台灣 Facebook、Instagram、Threads。[DailyView](https://dailyview.tw/popular/detail/33698)（accessed 2026-09-07, confidence: Medium）。ETtoday 與 UDN 轉述大陸留言「电视剧不敢拍的，AI来做」，這暗示還有一群對廣電古裝劇不滿的劇迷。[ETtoday](https://star.ettoday.net/news/3223651)（accessed 2026-09-07, confidence: High）。這顯示它是免費、跨海峽、平台原生的公共文本，不是付費短劇 App 產品。

### Feature Surface

片長約 26 分鐘，無真人出演，標示含 AI 生成內容。敘事是東漢末年蘭台令史調查「妖異」、發現底下是人禍、為了讓人活命只好把人寫成妖，後半接到黃巾起義前夕。文學與史源見下一節。技術面上，它展示的是 2026 年中國消費級影片生成模型剛能支撐的東西：一人、兩套模型、中長敘事、古裝寫實風格、角色在半小時尺度上大致可認。創作者自己把重點放在劇本與「藝術追求」，而不是工具演示。[Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: Medium）。

### Pricing and Packaging

B 站這支片是 **免費公開影片**，不是售票或按集解鎖。UDN、Unwire、DailyView 都轉述截至 8 月 24 日約 **人民幣 100 萬打賞／充電**（Unwire 換成約港幣 113 萬）。[UDN 噓！星聞](https://stars.udn.com/star/story/10091/9713666)（accessed 2026-09-07, confidence: Medium）；[Unwire](https://unwire.hk/2026/08/24/ai-short-film-china-viral/ai/)（accessed 2026-09-07, confidence: Medium）；[DailyView](https://dailyview.tw/popular/detail/33698)（accessed 2026-09-07, confidence: Medium）。虛詞寫的是 **超過 100 萬投幣**，那是站內互動代幣，不能直接等同現金。[虛詞](https://p-articles.com/heteroglossia/6178.html)（accessed 2026-09-07, confidence: Medium）。Marie Claire 把可能的百萬收入歸因於充電加流量分成，並猜測製作成本幾千到約人民幣一萬；沒有帳本，製作成本屬 **Low**。[Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: Low，就現金推算而言）。沒有來源顯示會員牆、院線票或短劇 App 分帳。

### Technology and Architecture

創作者公開點名的只有兩套模型。Marie Claire 引他的留言：「創作方面，主要使用的是seedance2.5視頻生成模型和gpt image2生圖工具」。[Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: High）。同一句「主要使用」被 NOWnews、UDN、中央社、聯合早報、星洲日報、Unwire 重複。[NOWnews](https://www.nownews.com/news/6868562)（accessed 2026-09-07, confidence: High）；[中央社](https://www.cna.com.tw/news/acn/202608250306.aspx)（accessed 2026-09-07, confidence: High）。「主要」不是「僅使用」：剪輯軟體、字體、混音、字幕工具都沒被點名，也不能因此發明它們。

媒體還原的影像鏈是：GPT Image 2 做角色、服裝、場景或關鍵靜幀；靜幀進入 Seedance 2.5 做動作、運鏡與聲音；再由人把約 30 秒級片段接成 26 分鐘。NOWnews 與 Unwire 把這條鏈當報導寫出；INSIDE 同一拆法標成「筆者猜測」。[NOWnews](https://www.nownews.com/news/6868562)（accessed 2026-09-07, confidence: Medium，兩模型屬 High、串接細節屬推論）；[INSIDE](https://www.inside.com.tw/article/42194-why-ai-short-film-ask-the-common-people-hailed-as-the-most-soulful-ai-animation-became-a-cross-strait-sensation)（accessed 2026-09-07, confidence: High，因它老實標猜測）。Seedance 官方單次最長 30 秒，因此 26 分鐘不可能是一次生成。粗算 1,560 秒／30 秒 ≈ **至少約 52 次成功生成**，不含廢片。[ByteDance Seed 2.5 部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）。配音產品、音樂來源、剪輯軟體名稱：公開來源都沒有。觀眾誇「配音很專業」只是觀感。Seedance 本身能在同一次生成裡出對白、音效與環境聲。[星洲日報](https://www.sinchew.com.my/news/20260826/entertainment/7791273)（accessed 2026-09-07, confidence: High 引述觀感、Low 作為流程證據）。

### Integrations and Ecosystem

中國消費端入口是即夢 AI（Jimeng）與豆包專業版；國際面是 Dreamina／CapCut 與 BytePlus API。Seedance 2.5 官方中國表面就是即夢。若「即梦 AI 超级创作者」簽名屬實，只說明帳號掛在即夢創作者計畫，不能證明另用了即夢生圖或即夢 TTS 取代 GPT Image 2。[ByteDance Seed 2.5 部落格](https://seed.bytedance.com/zh/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）。GPT Image 2 走 OpenAI API（`gpt-image-2`）或 ChatGPT Images 2.0；作者沒說他用哪條入口。[OpenAI API — GPT-Image-2](https://developers.openai.com/api/docs/models/gpt-image-2)（accessed 2026-09-07, confidence: High）。影片在 B 站標「含AI生成内容」，對應中國自 2025-09-01 施行的生成合成內容標識辦法，以及 B 站投稿「該視頻使用人工智能合成技術」聲明。[中國政府網](https://www.gov.cn/zhengce/zhengceku/202503/content_7014286.htm)（accessed 2026-09-07, confidence: High）；[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）。廣電總局《微短劇發展管理辦法》自 **2026-09-01** 施行（本片上傳之後），要求 AI 微短劇逐集顯著標識；B 站那枚晶片是否等於微短劇備案標識，本片備案身分未核實。[央廣網](https://news.cnr.cn/kuaixun/20260901/t20260901_527801215.shtml)（accessed 2026-09-07, confidence: High）。

---

## Literary and Historical Sources

### Plot and Themes

多家新聞台依影片簡介寫：故事與人物虛構；怪事標籤取自《搜神記》的「寺壁黃人」「木不曲直」「梁伯夏后」「草作人狀」；再接到東漢末黃巾。[ETtoday](https://star.ettoday.net/news/3223651)（accessed 2026-09-07, confidence: High）；[經濟日報](https://money.udn.com/money/story/5603/9709067)（accessed 2026-09-07, confidence: High）。中央社寫主角蘭台令史裴令史奉命查「妖異」，發現官方的「妖道作祟」底下是饑荒與苛政，為了不把人送廷尉，只好把真相記成妖異；後半接到張角。中央社所引張角句為「若有人問黃天在哪裡，告訴他，黃天不在雲上，黃天在每一個不肯再跪的人頭上」，群眾再喊歷史口號「蒼天已死，黃天當立」。片尾「後人讀妖，勿問鬼神，問蒼生」，字幕「謹以此片，紀念那些沒有被歷史記下名字的人」。[中央社](https://www.cna.com.tw/news/acn/202608250306.aspx)（accessed 2026-09-07, confidence: High）。UDN 與 ETtoday 獨立證實片尾兩句，並引主角句「苦難曾經真實到需要借鬼神開口」。[經濟日報](https://money.udn.com/money/story/5603/9709067)（accessed 2026-09-07, confidence: High）；[ETtoday](https://star.ettoday.net/news/3223651)（accessed 2026-09-07, confidence: High）。

制度前提在娛樂稿裡寫得更完整：牆裡長人、樹上生臉、白衣人入宮、草木做兵，查實則入《妖異簿》，查成人為則交廷尉；關鍵是「廷尉不信妖，廷尉只殺人」。[Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: Medium）。虛詞引上司教訓：寫成「人」就是官逼民反、朝廷失綱、陛下失德；寫成「妖」才有罪名、有出師之名。同文廣為流傳的句子包括「在這個世道裡，人說的話不算數，只有妖說的話，朝廷才會怕」。[虛詞](https://p-articles.com/heteroglossia/6178.html)（accessed 2026-09-07, confidence: Medium）。張角長段演講在虛詞與信望愛有較長逐字，含「你們不是天生該跪／該餓／該被打死之後還要謝官爺留了全屍」；用詞有「官爺」與「官員」之差，不宜把任何一版當拍攝劇本。[虛詞](https://p-articles.com/heteroglossia/6178.html)（accessed 2026-09-07, confidence: Medium）；[信望愛](https://www.fhl.net/nbg/movie/movie109.html)（accessed 2026-09-07, confidence: Medium）。Marie Claire 列出二十餘條金句，超出 CNA／UDN／ETtoday 核對範圍的部分標 **Low**，需對片才能當準確臺詞。[Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: Low，就未經對片的其餘金句而言）。

主角名字有衝突：中央社、UDN、Marie Claire、信望愛寫 **裴令史**；Unwire、ETtoday 導言、虛詞寫 **裴令時**。令史是東漢蘭台令史的官稱（班固曾任）；令時可能是口誤、聽寫錯誤，或劇本裡的私名。本報告未對到成片音軌，不能決。作者 8 月 18 日留言稱劇本改自幾年前隨筆，作品是自己做的；B 站頁無法直抓，用字依新聞轉述。[經濟日報](https://money.udn.com/money/story/5603/9709067)（accessed 2026-09-07, confidence: High）。

分析上（非事實陳述）：這部片的產品功能是史官兩難——寫成人，人死、也等於指控朝廷；寫成妖，人活、卻從「人」的歷史裡被抹掉。標題的懺悔與片尾的「問蒼生」是同一論點的兩個方向。新聞在這條主脊上一致。

### Classical and Historical Intertext

四個災異標籤對得上《搜神記》卷六連續正文；它們是後人標題或描述標籤，不是原書故事名。核對用中國哲學書電子化計劃與維基文庫卷六。[Chinese Text Project，搜神記卷六](https://ctext.org/wiki.pl?chapter=836102&if=en)（accessed 2026-09-07, confidence: High）；[Wikisource 搜神記／第06卷](https://zh.wikisource.org/zh-hant/%E6%90%9C%E7%A5%9E%E8%A8%98/%E7%AC%AC06%E5%8D%B7)（accessed 2026-09-07, confidence: High）。

**寺壁黃人——可核實。** 靈帝熹平二年六月，雒陽訛言虎賁寺東壁有黃人，觀者數萬；到中平元年二月張角兄弟起兵冀州，自號「黃天」。同一事亦見《後漢書》志·五行五。[ctext 搜神記卷六](https://ctext.org/wiki.pl?chapter=836102&if=en)（accessed 2026-09-07, confidence: High）；[ctext 後漢書 五行五](https://ctext.org/hou-han-shu/wu-xing-wu/zh)（accessed 2026-09-07, confidence: High）。古書已把黃人與黃天連在一起，並稱之為訛言。影片加上的是人為動機（施藥、給朝廷看的訊號），那是創作。

**木不曲直——可核實為洪範類名，不是單篇故事名。** 卷六熹平三年右校別作中兩株樗，一枝一夜「作胡人狀」；其後還有槐樹倒植、空樹生人面。正文總結「其於洪範皆為木不曲直」。《後漢書》五行二幾乎同文，並引京房「王德衰，下人將起，則有木生人狀」。[ctext 搜神記卷六](https://ctext.org/wiki.pl?chapter=836102&if=en)（accessed 2026-09-07, confidence: High）。影評裡的「樹上生臉」是壓縮這一組，不是另找一篇叫木不曲直的故事。

**梁伯夏后——可核實，史書與志怪有分叉。** 卷六：光和四年南宮中黃門寺有白衣男子長九尺，自稱「我梁伯夏。後天使我為天子」，解步欲收，忽不見。《後漢書》五行五是光和元年德陽門、中黃門桓賢、自稱「我梁伯夏，教我上殿為天子」，蔡邕把它讀成王莽式陰謀、後應在張角。[ctext 搜神記卷六](https://ctext.org/wiki.pl?chapter=836102&if=en)（accessed 2026-09-07, confidence: High）；[ctext 後漢書 五行五](https://ctext.org/hou-han-shu/wu-xing-wu/zh)（accessed 2026-09-07, confidence: High）。影片裡白衣人說要讓天下人有飯吃，是戲劇擴寫，不是引文。

**草作人狀——可核實。** 卷六光和七年陳留等地路邊生草「悉作人狀，操持兵弩」，舊說「近草妖也。是歲有黃巾賊起」。《後漢書》五行二寫中平元年夏，同事。光和七年與中平元年是同一年改元，不是兩次災異。[ctext 搜神記卷六](https://ctext.org/wiki.pl?chapter=836102&if=en)（accessed 2026-09-07, confidence: High）。

**張角與黃巾——歷史家具是真的，道德翻轉是假的。** 《後漢書》卷七十一：張角號大賢良師，事黃老道，符水治病，三十六方，謠「蒼天已死，黃天當立，歲在甲子，天下大吉」；唐周告密，馬元義車裂，張角稱天公將軍，後病死。范曄用語敵對：「轉相誑惑」「訛言」「蛾賊」。[Wikisource 後漢書／卷71](https://zh.wikisource.org/zh-hans/%E5%BE%8C%E6%BC%A2%E6%9B%B8/%E5%8D%B771)（accessed 2026-09-07, confidence: High）。影片保留符水、大賢良師、三十六方、口號與提前起事，但把黃天放到「不肯再跪的人頭上」。裴令史、《妖異簿》、「人不死妖入檔」、張讓教判決：都不在《後漢書》。作者自己說這是虛構演繹。[經濟日報](https://money.udn.com/money/story/5603/9709067)（accessed 2026-09-07, confidence: High）。

干寶卷六本來就是漢式政治徵兆學：氣亂於中、物變於外，木生人狀預示下人將起。影片做第二次翻轉：接受災異清單當劇情庫，再把每條徵兆寫成必須誤檔為妖的人事。古典裡，寫「妖」是讓天的警告進檔案；影片裡，寫「妖」是讓蒼生溜進一份不接受他們為「人」的檔案。虛詞說這是志怪最老的功能——借鬼神開口——這是批評判斷，不是干寶原話。[虛詞](https://p-articles.com/heteroglossia/6178.html)（accessed 2026-09-07, confidence: Medium）。中央社周圍評論認為真人電視劇恐難過審、志怪殼讓片子能說話；那是接收端判斷，不是作者宣言。[中央社](https://www.cna.com.tw/news/acn/202608250306.aspx)（accessed 2026-09-07, confidence: High）。

> Conflicts noted（文學軸）: 裴令史 vs 裴令時；宮中白衣人日期與人名，搜神記與後漢書不一致；草妖日期光和七年 vs 中平元年夏（同年改元）；張角演講短版穩定、長版用詞漂移；信望愛的張讓／唐周場次僅單源。
> Gaps: 無公開劇本；舊隨筆本文未出土；未能對片核對 Marie Claire 全部金句；B 站頁 HTTP 412。

---

## Technology Landscape

### Overview of Approaches

這部片的技術答案很短，細節卻不能短。**已向作者核實的只有兩件事：靜幀用 GPT Image 2，動態用 Seedance 2.5。** 其餘（剪輯軟體、是否另用 TTS、音樂從哪來、即夢還是 API 登入）都沒有作者原文。下面分開寫兩套模型「能做什麼」，再標哪些是這部片「被證實做了什麼」。

**Seedance 2.5** 是字節跳動 Seed 的閉源商用影片生成模型，中國產品名 Doubao-Seedance，國際名 Dreamina Seedance。官方發布日 **2026-07-31**，不是新聞改寫。[ByteDance Seed, “Introducing Seedance 2.5”](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）— **Primary**。2.5 沒有獨立技術報告；發布文說它延續 2.0 的「統一多模態音畫聯合生成」。前代論文 *Seedance 2.0*（arXiv:2604.14148，2026-04-15）描述同一系統吃文字、圖、音、影片，而不是先出默片再配音。[arXiv 2604.14148](https://arxiv.org/abs/2604.14148)（accessed 2026-09-07, confidence: High）— **Primary**。更早的 Seedance 1.0 報告（arXiv:2506.09113）才公開 DiT 內部：時空解耦層、交錯多模態位置編碼、原生多鏡頭、混合精度與稀疏注意力。[arXiv 2506.09113](https://arxiv.org/abs/2506.09113)（accessed 2026-09-07, confidence: High）。把 2.5 寫成「雙分支 DiT、某某參數量」的三方文是從 1.0／2.0 推論，屬 **Low**。

單次長度 **4–30 秒**，比 2.0 的 4–15 秒長，同一次出同步音訊。可延長成品；部落格寫多輪、可到「數分鐘」且角色與節奏仍穩；產品頁較保守，寫最多延長兩次。[Seed 2.5 英文部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）；[Seedance 2.5 產品頁](https://seed.bytedance.com/en/seedance2_5)（accessed 2026-09-07, confidence: High）。BytePlus ModelArk 教學（更新至 2026-08-31）寫 24 fps、MP4、多種畫幅，並有 `extend video` 與 `return_last_frame` 做鏡頭串接。參考預算有兩處官方互證：**1–30 張圖、最多 10 段參考影片、最多 10 段音訊**；非編輯任務每段影片 2–30 秒，編輯任務 4–30 秒，**影片總長 ≤ 30 秒、音訊總長 ≤ 30 秒**。2.5 可只吃音訊。[BytePlus ModelArk 影片生成教學](https://docs.byteplus.com/en/docs/ModelArk/2298881)（accessed 2026-09-07, confidence: High）— **Primary**。

解析度有衝突。上線當日即夢 UI 與極目新聞記者坐在 App 裡看到的是 **720p**，積分階梯 5／10／15／30 秒對 130／260／390／780 點。[極目新聞 via 網易](https://www.163.com/dy/article/L36N8Q9T053469LG.html)（accessed 2026-09-07, confidence: High）。BytePlus LAS 仍列 2.5 輸出 **僅 480p 或 720p**，並寫 1080p 不支援。[BytePlus LAS](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced)（accessed 2026-09-07, confidence: High）。較後的 ModelArk 對照表卻把 2.5 寫成含 **1080p 10-bit**。CapCut／Dreamina 行銷把 2.5 賣成原生 4K，與開發者合約衝突：4K 寫在 Seedance **2.0**。[BytePlus ModelArk 教學](https://docs.byteplus.com/en/docs/ModelArk/2298881)（accessed 2026-09-07, confidence: Medium，因與 LAS 內部不一致）。本片頁面據稱 1920×1080，若屬實，可能是後製放大、平台轉碼，或走了後來才開的 1080p 路徑——作者沒說。

角色穩定靠參考圖與提示詞，不是角色 ID 資料庫。官方說多張靜幀綁定可保多人外貌與聲音；延長時保主角、環境與節奏。白模／黏土模可鎖走位與燈光；綠幕可換環境。時間戳提示控制鏡內節拍；生成後可改指定區間而不重跑整條。[Seed 2.5 英文部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）。公開 API 阻擋真人臉參考，除非白名單肖像庫；對這部用 GPT Image 2 假臉的古裝片不構成障礙。[BytePlus ModelArk 教學](https://docs.byteplus.com/en/docs/ModelArk/2298881)（accessed 2026-09-07, confidence: High）。「一鏡成片」官方意思是 **30 秒內的多鏡頭起承轉合**，不是 26 分鐘一次渲出。量子位報導即夢產品層有最長約 **3 分鐘** 的超長模式與 Maya／Blender 白模插件，那是產品包裝，不是 API 合約改成 180 秒。[量子位](https://www.qbitai.com/2026/07/464329.html)（accessed 2026-09-07, confidence: Medium）。

定價公開。火山引擎首頁列豆包影片模型 2.5 **¥70／百萬 token**（請求不含影片）與 **¥42／百萬 token**（含影片）。[火山引擎](https://www.volcengine.com/)（accessed 2026-09-07, confidence: High）。即夢消費端按積分：極目新聞上線日記者表為 720p 非會員約每秒 26 點（30 秒 780 點），高於 2.0 VIP 每秒 14 點。[極目新聞](https://www.163.com/dy/article/L36N8Q9T053469LG.html)（accessed 2026-09-07, confidence: High）。

**GPT Image 2** 是 OpenAI 當旗艦的靜幀生成與編輯模型。API ID `gpt-image-2`（預設快照 `gpt-image-2-2026-04-21`）；ChatGPT 品牌名 **ChatGPT Images 2.0**。它 **不是** 影片模型。[OpenAI API — GPT-Image-2](https://developers.openai.com/api/docs/models/gpt-image-2)（accessed 2026-09-07, confidence: High）— **Primary**。公開上線 **2026-04-21**。[OpenAI Developer Community](https://community.openai.com/t/introducing-gpt-image-2-available-today-in-the-api-and-codex/1379479)（accessed 2026-09-07, confidence: High）；[VentureBeat, 21 Apr 2026](https://venturebeat.com/technology/openais-chatgpt-images-2-0-is-here-and-it-does-multilingual-text-full-infographics-slides-maps-even-manga-seemingly-flawlessly)（accessed 2026-09-07, confidence: High）。譜系：2025-03-25 GPT-4o 原生生圖 → 2025-04-23 API `gpt-image-1` → 2025-12-16 `gpt-image-1.5` → 2026-04 `gpt-image-2`。棄用表把舊 GPT Image ID 指向 `gpt-image-2`；`gpt-image-1` 排 2026-10-23 關、`gpt-image-1.5` 排 2026-12-01 關。[OpenAI API — Deprecations](https://developers.openai.com/api/docs/deprecations)（accessed 2026-09-07, confidence: High）。

能力上，官方強調指令遵循、編輯、多語文字、更多畫幅。生成走 `/v1/images/generations`，參考圖與遮罩編輯走 `/v1/images/edits`；品質 `low`／`medium`／`high`／`auto`。對 `gpt-image-2`，`input_fidelity` 不再給使用者調，輸入圖一律高保真。解析度行銷寫「最高 2K」；文件更細：兩邊為 16 倍數、長寬比不超過 3:1、總像素 655,360–8,294,400、最長邊 3840 px；超過約 2560×1440 標實驗性。[OpenAI 生圖指南](https://developers.openai.com/api/docs/guides/image-generation)（accessed 2026-09-07, confidence: High）。角色一致：cookbook 寫臉與身分在編輯、角色連續、多步工作流上較穩，並要使用者在提示裡鎖不變量。同一份指南仍警告模型「可能偶爾難以在多次生成間維持反覆出現的角色或品牌元素」。這是官方上限，不是外評挑剔。[OpenAI cookbook prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)（accessed 2026-09-07, confidence: High）。中文等非拉丁文字：社群公告強調多語文字改進；文件仍說精確排字與清晰度可能失敗。沒有漢代銘文或小楷的官方正確率。[OpenAI Developer Community](https://community.openai.com/t/introducing-gpt-image-2-available-today-in-the-api-and-codex/1379479)（accessed 2026-09-07, confidence: High）。

API 價（本報告讀取時）：圖輸入 $8.00／1M tokens、快取圖輸入 $2.00、圖輸出 $30.00；文字輸入 $5.00、快取文字輸入 $1.25。ChatGPT 端含在訂閱裡，不對使用者按 token 開單。[OpenAI API — Pricing](https://developers.openai.com/api/docs/pricing)（accessed 2026-09-07, confidence: High）。OpenAI 自己的影片產品是 Sora，與 GPT Image 2 分開；業界 2026 年的做法是先在靜幀模型鎖造型，再把圖當首幀、末幀或多圖身分參考餵給影片模型。這是工具能力，不是青瓜蛋的製作說明。

作者 **沒有** 被引述說過：ChatGPT 還是 API、thinking mode、八圖批次、參考圖編輯、2K 輸出、Seedance 首幀語法。NOWnews 把「先 GPT Image 2 做人設再 Seedance 驅動」當事實寫；INSIDE 標猜測。本報告採用 INSIDE 的誠實分層：兩模型名稱 High；靜幀→驅動→剪接的串列是合理重建，不是拍攝日誌。

### Performance and Benchmarks

截至 2026-09-07，Artificial Analysis 影片競技場 **沒有 Seedance 2.5 列**。含音訊的文生影片榜由阿里 Wan 3.0 與 Google Gemini Omni Flash 並列（Elo 1238）；**Dreamina Seedance 2.0 720p 第五（Elo 1222）**。Kling 3.0 1080p Pro 第十（1108）；Veo 3.1 第十四（1091）。圖生影片含音訊榜上，Seedance 2.0 720p 第一（Elo 1197）。[Artificial Analysis Text to Video](https://artificialanalysis.ai/video/leaderboard/text-to-video)（accessed 2026-09-07, confidence: High）；[Artificial Analysis Image to Video](https://artificialanalysis.ai/video/leaderboard/image-to-video)（accessed 2026-09-07, confidence: High）。用 2.0 的 Elo 代理 2.5 屬 **Low**：2.5 賣點是時長與參考深度，競技場幾秒短片測不到。

Seed 對 2.5 的說法是定性的：30 秒能撐多鏡頭弧、轉場與換景變強、油膩感下降、不受控字幕與 BGM 變少；仍承認複雜運動物理與多主體互動不穩。[Seed 2.5 英文部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High，廠商自評）。聯合早報引觀眾：這部片沒有常見嘴型崩、對口型失敗；仍有人覺得「沒有破綻就是最大的破綻」——太乾淨、缺真人髒感，故仍有「AI 味」。瞳孔在強光下收縮、書寫筆畫大致正確，被當成「和 AI 打磨很久」的證據。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High，就觀眾轉述而言）。INSIDE 寫臉、服、光比早期 AI 短片穩，但缺真人微表情，「穿幫」仍常見；這不能拆給 GPT Image 2 或 Seedance 單獨負責。[INSIDE](https://www.inside.com.tw/article/42194-why-ai-short-film-ask-the-common-people-hailed-as-the-most-soulful-ai-animation-became-a-cross-strait-sensation)（accessed 2026-09-07, confidence: Medium）。OpenAI 論壇 2026 年 7 月仍有手指、手臂比例抱怨，屬實務回報 **Low**，且與本片無直接對照。[OpenAI 論壇 issues thread](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/352)（accessed 2026-09-07, confidence: Medium）。

### Community Health and Maturity

Seedance 2.5 上線約五週（相對本片 8 月 17 日上傳約兩週）已是商用，不是研究預覽。中國入口：即夢、豆包專業版，上線日還有扣子、小雲雀。[極目新聞](https://www.163.com/dy/article/L36N8Q9T053469LG.html)（accessed 2026-09-07, confidence: High）。國際：Dreamina／CapCut、BytePlus ModelArk（`dreamina-seedance-2-5-260628`）、LAS。中國 API：火山方舟（`doubao-seedance-2-5-260628`）。權重封閉，無自架。公開 API 擋真人臉參考；生成 URL 24 小時過期；任務留 7 天。[BytePlus ModelArk 教學](https://docs.byteplus.com/en/docs/ModelArk/2298881)（accessed 2026-09-07, confidence: High）。即夢積分讓 2.5 每秒大約兩倍於 2.0，創作者公開說用 2.0 打草稿、2.5 出英雄鏡頭。[網易科技轉載](https://m.163.com/tech/article/L3FTQKIV00097U7T.html)（accessed 2026-09-07, confidence: Medium）。

GPT Image 2 在 ChatGPT 全方案與 API 都可用；thinking 生圖在付費檔。驗證組織才可調 GPT Image API。這部片是成熟度訊號：模型發布約兩週後，有人用它剪出 26 分鐘無人出演敘事。這證明工具夠做長片 **剪輯生產**，不證明原生生成長度已離開 30 秒級。

截至 2026-09-07，搜尋不到作者自己的教程或「幕後」。小紅書／B 站「即夢＋豆包＋剪映 N 小時出片」是通用教學，不是本片的複製日誌，屬 **Low**，不列入已確認堆疊。

### Integration and Compatibility

Seedance 生成是非同步：`POST /contents/generations/tasks` 再輪詢。輸入 `content[]` 可含文字、`image_url`、`video_url`、音訊。控制項含 `generate_audio`（預設 true）、`resolution`、`ratio`、`duration`（4–30 或 `-1` 讓模型選）、浮水印、`return_last_frame`、callback。編輯與延長是一等模式。[BytePlus ModelArk 教學](https://docs.byteplus.com/en/docs/ModelArk/2298881)（accessed 2026-09-07, confidence: High）。符合官方上限的長片管線長這樣：靜幀（GPT Image 2）→ 最多 30 張角色／場景聖經 → 4–30 秒、帶時間戳的多鏡頭提示 → extend 或末幀串動作 → 本地修 → NLE 組裝、必要時重配樂。每段原生音訊 24 fps；若要一條連續配樂，仍得後製混，而不是 50 段各自生成的 BGM 硬接。

> Conflicts noted（技術軸）: 「一鏡」行銷 vs 30 秒合約 vs 即夢約 3 分鐘超長模式 vs 媒體「用 Seedance 2.5 做了 26 分鐘」——只有假設剪接才能同時成立。1080p／4K 各文件互打。NOWnews 把靜幀→驅動當事實，INSIDE 標猜測。Unwire 寫「團隊」先用 GPT Image 2，與一人作業共識衝突，應視為記者套話。打賞人民幣 100 萬 vs 投幣 100 萬不可合併。發布日：多數寫 B 站 8 月 17 日；新榜寫 8 月 13 日《问苍生》；西瓜寫 8 月 16 日。
> Gaps: 無 2.5 技術報告與參數量；無獨立 2.5 Elo；無鏡頭數、廢片率、即夢 vs API；無 NLE／TTS／音樂來源；無製作天數與推論帳單；OpenAI 官方 Images 2.0 部落格本環境未載入；無漢服專項評測。

---

## User and Market Perception

### Review Summary

聯合早報寫：到 2026 年 9 月 2 日播放已破 1,800 萬，觀眾仍稱「神作」，同時承認 AI 痕跡明顯；共識是「是不是 AI 做的不是重點，劇本和臺詞比較重要」。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）。接收分兩波：先驚 26 分鐘臉、服、光、運鏡還能接住；過幾天模型退到背景，人開始轉發金句與史官兩難。[INSIDE](https://www.inside.com.tw/article/42194-why-ai-short-film-ask-the-common-people-hailed-as-the-most-soulful-ai-animation-became-a-cross-strait-sensation)（accessed 2026-09-07, confidence: High）；[虛詞](https://p-articles.com/heteroglossia/6178.html)（accessed 2026-09-07, confidence: High）。微博轉述包括「質感立意都是大劇水準」「這才是真正該上院線的東西」「比這十幾年的正劇都牛」。[世界新聞網](https://www.worldjournal.com/wj/story/121233/9709774)（accessed 2026-09-07, confidence: Medium）。香港評論者李照興稱它是第一部「真的可以拿出來放給人看」的 AI 劇，並說它同時回應了網劇兩大舊怨：工拙、沒故事。[虛詞評論](https://p-articles.com/critics/6186.html)（accessed 2026-09-07, confidence: High）。環球時報英文明訪北京 AI 短劇導演趙亞峰（前短劇編劇）：工具能幫視覺與概念測試，但「畫面越好生成，創作者越要問作品到底想說什麼」。川大研究生、AI 劇愛好者李柏樂對同一報說，奇觀留不住人，這部片用非當代背景仍在問誰有權定義歷史。[Global Times](https://www.globaltimes.cn/page/202608/1369011.shtml)（accessed 2026-09-07, confidence: High）。沒有找到具名 AI 研究員或廣電官員針對本片的評論。

抱怨集中在工藝，不是一場「歷史考據戰」。聯合早報引「沒有破綻就是最大的破綻」：嘴與解剖沒崩，畫面卻太乾淨、缺真人髒感，故仍有 AI 味。INSIDE 與虛詞加：眼神銳度與痛感顆粒仍輸真人，穿幫仍在。Marie Claire 寫部分臺詞仍有 AI 腔，觀眾當可原諒。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）；[風傳媒（張亦聖）](https://www.storm.mg/lifestyle/11159055)（accessed 2026-09-07, confidence: High）。作者在被廣泛轉載的留言裡請人辯證看張角與黃巾、勿把片子當信史。[中央社](https://www.cna.com.tw/news/acn/202608250306.aspx)（accessed 2026-09-07, confidence: High）。這表明主導抱怨是殘餘平滑感，主導文化爭論是過度解讀，不是史實糾錯。

### Why it went viral

INSIDE 的 8 月 26 日重建給三層原因：26 分鐘完整敘事證明 AI 影像已離開幾秒段子；《搜神記》與黃巾與當下的縫隙讓不同政治立場都能進去；句子短到可以不帶片子旅行。聯合早報後續特稿同意順序：先畫面，再「把人寫成妖」，再金句。Marie Claire 寫早期討論是提示詞、成本（粗估幾千到約人民幣一萬）、電影質感；長尾是「內容」。一則 Threads「AI 圖只是工具，讓一千多萬人停下來看的還是內容」與上述各報同向。[INSIDE](https://www.inside.com.tw/article/42194-why-ai-short-film-ask-the-common-people-hailed-as-the-most-soulful-ai-animation-became-a-cross-strait-sensation)（accessed 2026-09-07, confidence: High）；[Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: Medium）。

金句經濟有數據。DailyView KEYPO（8 月 21–27 日）找到 3,162 筆華語網討論，聚類含作者名、片內名，以及「黃天在每一個不肯再跪的人頭上」「你們不是天生該跪」。[DailyView](https://dailyview.tw/popular/detail/33698)（accessed 2026-09-07, confidence: Medium）。跨 Zaobao、CNA、UDN、Storm、Unwire、虛詞反覆出現、因此可當旅行套組的句子包括：標題本身；「人說的話不算數，只有妖說的話朝廷才會怕」；「你們不是天生該跪」；「黃天不在雲上，黃天在每一個不肯再跪的人頭上」；「苦難曾經真實到需要借鬼神開口」；上司那套「寫人＝官逼民反／朝廷失綱／陛下失德，寫妖＝妖道惑眾」；片尾「後人讀妖，勿問鬼神，問蒼生」與獻給沒有名字的人。這表示作品比較像歌詞，不像劇情摘要：可攜句子做了第二波分發。

與 2025–2026 其他爆款 AI 短片比的是種類，不是同一市場。環球時報同文引澎湃：7 月《油條兩半》（逾 110 萬讚、34.2 萬轉）、清明《紙手機》。工商時報寫《紙手機》約 3,000 萬播放、130 萬讚，且被人民日報與央視新聞轉發。[工商時報](https://www.ctee.com.tw/news/20260730700564-430801)（accessed 2026-09-07, confidence: Medium）。那兩部是讓 AI 消失的親情短片。李照興另列 2026 高播：《美猴王》、科幻《三星堆：未來啟示錄》、戰爭短片《坐標》、成本爭議《霍去病》、類型實驗《黑絲女天師》。中央社 9 月 1 日產業稿：2026 上半年抖音上了 22.19 萬部 AI 短片，98.7% 不曾回本，6 月觀眾已厭「AI 臉」。[中央社](https://www.cna.com.tw/news/acn/202609010227.aspx)（accessed 2026-09-07, confidence: High）。對照這堆量，《問蒼生》稀缺的是主題膽量與 26 分鐘完整弧，不是記憶真誠。

### Controversy, censorship, and political readings

謠言與事實要分開。風傳媒、INSIDE、虛詞、UDN 社論都記錄「上線一天被禁」或「即將被禁」的說法；UDN 24 日快評寫有民進黨側帳號指中共下架。[風傳媒（田常）](https://www.storm.mg/article/11159178)（accessed 2026-09-07, confidence: High）；[UDN 重磅快評](https://udn.com/news/story/11091/9709875)（accessed 2026-09-07, confidence: High，黨派評論）。**截至聯合早報 9 月 3 日截稿，片子仍可看，且進了 B 站「每周必看」。** Storm、INSIDE（8 月 26 日下午）、虛詞（25 日）、Unwire（24 日）、中央社（25 日）各自截止點也都寫仍在。本環境 9 月 7 日直抓 B 站回 HTTP 412，是反爬，不能當下架證據。觀眾行為像隨時會禁：聯合早報引「趕緊多看幾遍再下架」，虛詞寫很多人下載。那是觀眾預演，不是官方動作。沒有找到網信辦、廣電或 B 站點名本片下架的聲明。

政治讀法按地理分，多過按喜不喜歡分。大陸側，中央社記網友「電視劇不敢拍的，AI 來做」，比魯迅式諷刺。中央廣播電臺評論把內捲、考公受阻、「躺平」、甚至黃巢迷因讀進張角。[RTI 劉國忠](https://www.rti.org.tw/news?pid=228652&uid=3)（accessed 2026-09-07, confidence: Medium，署名專欄）。環球時報停在較安全框：誰寫歷史、誰的苦難被記住；不把「不是天生該跪」印成政權批判。台灣 UDN 社論把它當「中國創意不全是主旋律」的證據，再對比台灣 AI 短片《油不得你》兩小時內警察上門——那是黨派比較，不是中國政策文件。INSIDE 警告中新社把片子讀成兩岸寓言不是中立事實。香港虛詞強調沒有真人演員必須認領危險臺詞——嘴是合成的，主題因此延長：「人不能說時，找一個非人來說」。反方向的「這是黨批准的農民起義讚歌」存在但次要：張角作為有組織農民領袖在中國教科書本就正確，這被當成「未必自動禁」的制度觀察，**不是**委製或主旋律的證據。作者公開說法是失眠夜的藝術、舊隨筆、兩套工具、請勿當紀錄片。

### Changelog Highlights (last 12 months)

讓一人做出 26 分鐘古裝敘事的，是 2025–2026 一連串 **原生音訊、參考鎖定、單次更長片段**，再加上把片段縫成分鐘的產品包裝。真正的一小時一次生成、可攜角色 ID，到 2026-09-07 仍未出貨。

Seedance 1.0 於 2025-06-11 公開，帶原生多鏡頭默片與 1080p，**沒有原生音訊**。[arXiv 2506.09113](https://arxiv.org/abs/2506.09113)（accessed 2026-09-07, confidence: High）。即夢 2025-08-20 的「智能多幀」是關鍵幀插值包裝（2–10 張圖、幀間 1–6 秒），不是 54 秒原生模型。[雷鋒網](https://www.leiphone.com/category/industrynews/9iFQYmX15zgL8l2I.html)（accessed 2026-09-07, confidence: Medium）。OpenAI 靜幀線：2025-03-25 GPT-4o 原生生圖 → 2025-04-23 API `gpt-image-1` → 2025-12-16 `gpt-image-1.5`（臉與 logo 較能保住）→ 2026-04-21 **GPT Image 2／Images 2.0**（thinking mode、預設高身分保真）。[OpenAI Images 2.0 系統卡](https://deploymentsafety.openai.com/chatgpt-images-2-0)（accessed 2026-09-07, confidence: High）。沒有任何一代給持久角色 ID；身分仍是每次請求的參考圖。

原生音訊是產業拐點。Google Veo 3 於 2025-05-20 I/O 帶對白／音效／環境聲；Veo 3.1（2025-10-15）加參考圖與場景延長，原生仍是 4／6／8 秒，更長是從最後一秒往後跳的包裝（官方文件寫最多約 20 跳／約 148 秒、延長限 720p）。[Google Developers Blog Veo 3.1](https://developers.googleblog.com/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/)（accessed 2026-09-07, confidence: High）。可靈 Video 2.6 於 2025-12-03 做同步音畫、最長 10 秒。[Kuaishou IR](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-video-26-model-simultaneous-audio-visual)（accessed 2026-09-07, confidence: High）。Seedance 1.5 pro 於 2025-12-15／16 補上聯合音畫；仍缺混參、專用延長與超長時長。[Seedance 1.5 pro](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro)（accessed 2026-09-07, confidence: High）。Sora 2 於 2025-09-30 帶對白與 cameo 肖像鎖；消費端 App 2026-04-26 關，API 排 2026-09-24 關且無後繼。[OpenAI Sora discontinuation](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)（accessed 2026-09-07, confidence: High）。

2026 年 2 月，多參考＋原生音＋約 15 秒成為預設競爭組。可靈 3.0／Omni（2026-02-05）：15 秒、一次生成最多六個鏡頭、元素庫 `@` 呼叫。[Kuaishou IR Kling 3.0](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be)（accessed 2026-09-07, confidence: High）。Seedance 2.0（官方英文稿 2026-02-12）：統一多模態、最多 9 圖＋3 影片＋3 音、15 秒高質量多鏡頭音畫。[Seedance 2.0](https://seed.bytedance.com/en/blog/seedance-2-0-official-launch)（accessed 2026-09-07, confidence: High）。即夢約 2026-04 的 Octo／小章魚是畫布資產卡，產品記憶層，不是模型級 ID。

Seedance 2.5 預覽 2026-06-23、正式 2026-07-31：單次 15 秒改 **30 秒**；參考升到 30 圖＋10 影片＋10 音；多輪延長做「數分鐘」。**30 秒是模型原生；分鐘是包裝。** 即夢「超長／約 180 秒」是產品編排，Seed 研究部落格沒承諾 180 秒一次前向傳遞。[Seed 2.5 部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）。截至 2026-09-07 沒有 Seedance 3.0 公開路線圖，也沒有任何一線廠商文件寫「一小時一次生成」。

### Community Health

社區數字像健康爆款，不像網暴。8 月底報導裡留言約 3.8–4.1 萬、讚約 116–135 萬、分享約 26 萬、打賞約人民幣 100 萬。作者「一覺醒來以為被網暴」本身是健康訊號：量看起來像攻，結果是誇。辯論真實存在：以古諷今還是萬年寓言；是不是「零成本」（INSIDE 引產業文：Seedance 單次約 30 秒，26 分鐘至少約 53 次生成再加剪、樂、字幕）；一人公司該不該取代劇組。虛詞轉 BBC 歸因數字：中國百大短片 AI 佔比從 2025 年初約 7% 到 2026 年初約 38%；演員日薪從約人民幣 2 萬掉到 1,200；中國網絡視聽協會 2026 Q1 稱新上微短劇約 95% 是 AI。那些數字描述片子周圍的產業，不是片下留言本身。中央社 9 月 1 日稿顯示國家用「提質減量」、600 億真人短片支持、平台打「高頻 AI 臉」回答過剩——**沒有**監管點名本片。社區興奮、金句驅動、有一點怕禁，並嵌在更大的勞動與監管戰裡；這部片是說明，不是起因。

## Strategic Signals

### Competitive Positioning

這部片站在 **量產 AI 微短劇工廠外面**，這正是重點。它是橫屏、全標 AIGC、26 分鐘、B 站首發的作者短片。它不像三個鄰居市場。抖音首屆 AI 創作大賽（2026-06-10 至 08-20）要 ≥2 分鐘原創 AI 敘事、抖音與即夢雙發、24 小時抖音獨佔窗、獎金池人民幣 400 萬加 2,000 萬即夢積分，評審含賈樟柯、陳思誠等；截至 2026-09-07 **沒找到公開入圍名單，也沒來源把本片放進該賽**。[京報網](https://news.bjd.com.cn/2026/06/10/11798273.shtml)（accessed 2026-09-07, confidence: High）。「未來導演扶持計劃」是真人導演管線，不是 AIGC 賽。[京報網](https://news.bjd.com.cn/2026/04/01/11663360.shtml)（accessed 2026-09-07, confidence: High）。字節 2026 年 AI 敘事體面賽道較像即夢＋百花獎：2,038 件投稿，六項榮譽含 Seedance 2.0 兩人歷史戰爭短片《斷鞘》。[京報網／新華轉載](https://news.bjd.com.cn/2026/08/11/11910527.shtml)（accessed 2026-09-07, confidence: High）。愛奇藝走的是持證 AIGC 工業：《奇譚：紙刃渡荒墟》被稱為首部拿到網絡劇片發行許可證的全流程 AIGC 網絡故事片（60 分鐘以上），平台給 AIGC 額外分成。[新華網](https://www.xinhuanet.com/ent/20260723/e78a10e06b8f46a0a30ce2ecb1a9009d/c.html)（accessed 2026-09-07, confidence: High）。

對 AI demo：Seedance 2.5 發布文賣長敘事並請人看 Seed 自己做的示範短片。那是模型卡，不是本片。觀眾討論幾天內從「這是 AI 嗎」轉成引金句。本片因此是 Seedance 2.5 長敘事賣點的 **敘事能力證明**，不是官方 demo。對傳統古偶：星洲等娛樂稿用「血洗古偶劇」；壹心娛樂楊天真說 2026 劇集開工「據說只有去年的 30%」——那是經紀人口頭估計，不是監管數列。[星洲日報](https://www.sinchew.com.my/news/20260826/entertainment/7791273)（accessed 2026-09-07, confidence: Medium）；[網易楊天真](https://www.163.com/dy/article/L4OTGU8N0556NAUX.html)（accessed 2026-09-07, confidence: Medium）。產業反應乾淨地劈開：劇組側（尤其 Seedance 2.0 之後）是真人短劇就業塌；BBC 中文寫日薪從 5,000–20,000 掉向 1,200、百人棚閒置、劇組從 40–50 人縮到 4–5 人。北大 2025 年報告稱微短劇拉動就業約 203 萬；BBC 把該基數當「被打擊人口」是因果跳躍。[BBC 中文](https://www.bbc.com/zhongwen/articles/cvgdqjvzv9go/simp)（accessed 2026-09-07, confidence: High）。對立句是「劇本仍是靈魂」，也是即夢百花獎與抖音大賽修辭。

**字節跳動／OpenAI 針對本片的評論：沒找到來源。** 工具歸屬來自作者留言，不是兩家公司背書。

### Adoption Signals

圍繞本片的採用是 **方法模仿，尚未見到具名翻拍潮**。簡繁英搜尋到 2026-09-07 沒找到重講《問蒼生》的具名複製品。出現的是：(1) 即夢／豆包／可靈／Seedance 2.5 教程市場，含「劇本→關鍵幀→圖生影片」通用指南（**Low**，不列入本片日誌）；(2) 即夢 2026 創作者成長計劃稱自 2025 年 2 月起 19,000+ 創作者、發出逾 1 億積分，超創為邀請制。UP 公開「即夢 AI 超級創作者」徽章是掛在本片上最硬的官方生態訊號。可比的故事優先 2026 AI 短片：可靈《紙手機》（報導跨平台 4,000 萬+）、蒙太神奇《油條兩半》、百花獎《斷鞘》、愛奇藝持證志怪《紙刃渡荒墟》。平台對 AI 敘事現在是 **邀請＋標籤，不是禁**。B 站 2026-05-15「清朗·整治 AI 應用亂象」把標識升到一等上傳控制。本片合規後被「每周必看」助推：平台會放大標好、留得住的 AI 敘事，即便文本政治偏辣——至少到 9 月初仍如此。[Bilibili 治理公告](https://www.bilibili.com/opus/1202507670848798745)（accessed 2026-09-07, confidence: High）— **Primary**。

### Risk Signals

廣電總局令第 16 號《微短劇發展管理辦法》自 **2026-09-01** 施行（本片上傳之後）。定義是 **連續劇、每集少於 20 分鐘**。專題（政治、軍事、司法、公安等）不論預算都是 I 類，要國家級備案與許可證；AI 作品投資額逾人民幣 80 萬也是 I 類；第 34 條要求 AI 微短劇按國家規則做 **每集顯著提示標識**；第 25 條禁損害國家榮譽、歷史虛無、煽動混亂等。26 分鐘 **單集** B 站片 **不自動等於微短劇**，但若續作成劇、豎屏切、付費分集，就可能進制度；黃巾／官逼民反主題若改成系列，靠近專題風險。[七一網／廣電微信轉令文](https://www.12371.gov.cn/h5/article/1532828209841442816/h5/content_1532828209841442816.html)（accessed 2026-09-07, confidence: High）— **Primary**。四部門《人工智能生成合成內容標識辦法》自 2025-09-01 已要求片頭可見標識與隱式元數據；B 站「含 AI 生成內容」是該規則的平台實作，不是 2026 新品。[中國政府網](https://www.gov.cn/zhengce/zhengceku/202503/content_7014286.htm)（accessed 2026-09-07, confidence: High）。

政治下架在評論文化裡真實，在執法紀錄裡（到 9 月初）未證實。那是容忍快照，不是放行函。商業與勞動風險在周圍產業：視聽協會 2026 Q1 稱約 12.8 萬部微短劇上線、約 12.2 萬（95%+）是 AI。[上海市新聞辦／中國網絡視聽協會](https://www.shio.gov.cn/TrueCMS/shxwbgs/wxdtt/content/2f93a052-95b0-4748-b327-6138bbd2d351.htm)（accessed 2026-09-07, confidence: High）。DataEye（經產業媒體）稱上半年抖音新 AI 短片／漫劇 22.19 萬、破億播放 1,055 部（0.47%）。「98.7% AI 短片不回本」屬單源 **Low**。春晚檔真人短片播放仍可達 AI 短片約 25 倍（TVOAO）。兩件事可同時真：AI 填目錄，真人拿節日流量，這部 B 站片是第三物——作者型 AI，行為像體面短片，不像兩堆貨。

分析上：戰略讀法不是「AI 取代古偶」（協會與春晚流量都反駁），而是 Seedance 級長片段讓即夢超創能送出傳統古偶不會過會的 26 分鐘寓言，而監管剛給同一技術的 **系列形態** 做了盒子。若它系列化、當微短劇變現、或切成 20 分鐘以下，令第 16 號與專題審查成為硬約束。若維持一次性標籤短片，活風險是內容政治，不是微短劇備案。

## Comparative Analysis

### Top Options Head-to-Head

對 2026 年 8 月一個要做約 26 分鐘寫實漢裝、要講中文的大陸個人 UP，綁定約束不是競技場 Elo，而是：能不能無 VPN、無外卡登入付款；模型能不能在出畫的同一輪吐 **中文對白**；每鏡能帶多少角色／服裝靜幀；26 分鐘要縫多少刀；臉與聲音聖經會不會鎖死在一家廠商。以 2026-09-07 的規格，即夢上的 Seedance 2.5 是理性預設。Wan 3.0 是唯一同為 30 秒原生窗的對手，但 8 月初仍偏預覽／邀測。可靈 3.0 與 MiniMax H3 是 15 秒級大陸備援。Veo／Gemini Omni、Runway Gen-4.5、Sora 過不了入口或對白門，或兩者都過不了。

**Seedance 2.5：** 4–30 秒、原生音畫、30 圖＋10 影片＋10 音。中國門在即夢與豆包專業版。解析度文件互打（即夢上線日 720p vs 部分 API／轉售 1080p）。成本訊號：火山示例 5 秒 16:9 約 ¥7.56（720p）；即夢高級會員連續包有報 ¥499／6,160 積分。對本片：**最佳大陸原生匹配**。

**可靈 3.0／Omni：** 3–15 秒、原生音、中文加方言、Omni 最多約 7 張圖。大陸 klingai.com、支付寶／微信。對本片：**可用備援**，方言與元素庫有用，但原生時長一半、聖經更薄，縫的刀更多。

**Google Veo 3.1／Gemini Omni：** Veo 官方原生 4／6／8 秒；Omni Flash 官方 3–10 秒。AA 榜 Omni Flash 與 Wan 3.0 並列文生影片含音第一（Elo 1238）。Gemini API／AI Studio **不是中國支援區**。對本片：**榜首品質、這個 UP 的生產起點不合格**。

**Runway Gen-4.5：** 官方 API 2–10 秒，`gen4.5` schema **沒有 audio 欄**。美元、牆。對本片：**差**。默片短鏡頭，沒有中文對白門。

**MiniMax H3／海螺 3：** 與 Seedance 2.5 同日上線（2026-07-31）。4–15 秒、原生立體聲、最多約 9 圖 3 影片 3 音。官方 API 約 $0.08／秒（768P）。權重有開源（IR 仍託管）。對本片：**最好的便宜大陸替代**，時長與參考不如 2.5，鎖死風險最低。

**阿里 Wan 3.0：** 官方 2–30 秒、30 fps、原生對白／BGM／音效、最多約 20 個多模態參考。北京目錄價 720p ¥0.6／秒、1080p ¥1.2／秒，比 Seedance 公開 720p 示例便宜。英文 API 仍寫 preview；公開百煉文多落在 2026-08-06–13，即 Seedance 2.5 之後、本片上傳前數日。AA 文生影片含音並列第一。對本片：**最接近的能力雙胞胎**；對 8 月初已在渲的個人，入口時點與邀測狀態才是問題。

**Sora：** 消費端已關、API 將關。從不是大陸消費路徑。GPT Image 2 是另一個產品。對本片影片渲染：**出局**。

為何 Seedance 2.5 是理性選擇：2026-07-31 後兩週，它是唯一 **普遍可及的大陸消費模型**，同時具備 30 秒原生、能講中文的原生音、30 張服裝／角色聖經、即夢裡用微信／支付寶。可靈與 H3 活著但 15 秒、參考更少。Wan 3.0 對得上 30 秒且每秒更便宜，但預覽／邀測，片子開剪時才剛出現在百煉。Google、Runway、Sora 過不了登入或付款。競技場 Elo 會指向 Wan 或 Omni，不是指向能在 B 站檔期裡做完 26 分鐘古裝的那一個。

### Decision Matrix

| Option | Native length | Audio | Refs | China access | Cost signal | Lock-in | Fit for this film |
| ------ | ------------- | ----- | ---- | ------------ | ----------- | ------- | ----------------- |
| **Seedance 2.5** | 4–30s；即夢「約 3 分」是產品延長 | 原生聯合音畫 | 30 圖＋10 影片＋10 音 | 是：即夢／豆包／人民幣 | 即夢 720p 約 26 點／秒；API 示例 ¥7.56／5s 720p | 閉源；積分過期；聖經是靜幀不是 ID | **主選。** 2026 年 8 月初唯一普遍可及的 30s＋厚聖經＋中文原生音 |
| **Wan 3.0** | 2–30s；30 fps | 原生對白／BGM／SFX | 約 10 圖＋5 影片＋5 音 | 是（北京區），8 月仍偏 preview／邀測 | 北京 ¥0.6／s 720p、¥1.2／s 1080p | 閉源；阿里帳 | **最接近雙胞胎。** 每秒更便宜、AA Elo 更高；時點可能太晚 |
| **Kling 3.0／Omni** | 3–15s | 原生；中文＋方言 | Omni ≤7 圖 | 是：可靈、支付寶 | 官方 9–12 點／s（720／1080 含音） | 閉源；中／國際積分不互通 | **可用備援。** 刀數約兩倍 |
| **MiniMax H3** | 4–15s | 原生立體聲；含中文 | ≤9 圖、≤3 影片、≤3 音 | 是：海螺 | 官方 $0.08／s 768P | 權重部分開源；IR 仍託管 | **最好的便宜替代與鎖死對沖** |
| **Gemini Omni Flash** | 3–10s | 預設音畫；非英語「未評估」 | 首幀為主 | 否（非中國區；美元） | AA $6／min | Google 帳＋SynthID | 榜首，不是這個 UP |
| **Veo 3.1** | 4／6／8s | 有聲 | 「資產圖」，數量官方表未寫清 | 否（us-central1） | AA $24／min | Vertex／C2PA | 太短、太貴、沒大陸門 |
| **Runway Gen-4.5** | 2–10s | 官方 schema 無 audio | 1 張首幀 | 否 | 12 點／s | App／API 積分分裂 | 差：默片、無中文對白門 |
| **Sora 2** | n/a（退出中） | n/a | n/a | 否 | n/a | 2026-09-24 硬日落、無後繼 | 出局 |

### Migration and Lock-in Risks

閉源大陸消費 App（即夢、可靈、海螺、百煉）都鎖月積分、提示詞語法、參考打包規則。臉與服裝若離線保存 **靜幀聖經** 就可攜；若只存在廠商「元素」裡就不可攜。Seedance 的 30 圖包進不了可靈 Omni 的 7 槽或 H3 的 9 槽，除非重排聖經。原生音 **不會** 給你一條 26 分鐘配樂：五十幾段各自生成的床會在 NLE 裡互打。H3 是這裡唯一公開權重的選項，但質量關鍵的 Context-IR 仍託管，「開源」不是完整逃生口。Wan 3.0 是能力層最不痛的遷移（同 30 秒級、原生音、多模態參考），且 1080p 每秒比 Seedance 720p 示例便宜——若你的百煉帳真的 GA。Google 與 Runway 加 SynthID／C2PA、美元帳、對 VPN 不友善的條款；不是大陸生產遷移。Sora 是強迫遷移且無後繼。若有人要重做這部片：把 GPT 級或即夢靜幀當廠商中立角色聖經；Seedance 2.5（或已 GA 的 Wan 3.0）出對白英雄鏡；H3 做覆蓋與補拍的成本對沖。不要把管線重建在 Veo、Omni、Runway 或 Sora 上，除非製作人已有外卡且不需要可靠的中文原生對白。

> Conflicts noted（Step 3）: 播放量是時間序列快照，不是互相否定，除香港 01 8 月 28 日 1,447 萬低於前幾日若干數字。工具鏈：多數寫兩模型，環球時報另加即夢。下架是記錄在案的謠言；9 月 2–3 日仍在是記錄在案的事實。CNAA「AI 約 95% 的 **部數**」與 TVOAO「春晚 **播放** 真人仍 25 倍」可並存。BBC「兩百萬工作被打」把 2025 拉動就業估計改寫成替代。楊天真 30% 帶「據說」。DataEye 400 億是 2026 **預測**。26 分鐘 vs 令文每集 **少於 20 分鐘**。Seedance 解析度與即夢 3 分鐘模式文件互打。Wan 3.0 preview vs AA 已上榜。
> Gaps: 無字節／OpenAI 對本片聲明；無大賽入圍名單；無具名翻拍；無製作帳單；9 月 3 日之後的在架狀態未從頁面核實；無漢服／中文對白專項分數。

## Implementation Considerations

### Recommended Architecture Patterns

2026 年能做出約 26 分鐘寫實 AI 敘事的路，仍是 **靜幀聖經 → 圖生影片 → 可選延長或末幀串接 → 非線性剪輯**，不是一次模型跑完。對本片，作者說圖來自 GPT Image 2、動來自 Seedance 2.5，再串接成片；他沒點名剪輯軟體、鏡頭時長配比、聲音做法或生成次數。那最後一步就是 NLE，不管叫什麼名字。[NOWnews](https://www.nownews.com/news/6868562)（accessed 2026-09-07, confidence: High）；[ByteDance Seed 2.5 部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）— **Primary**。

官方上限寫得很死。BytePlus LAS 上 `dreamina-seedance-2-5-260628` 生成 **4–30 秒、24 fps MP4、480p 或 720p**；1080p／4K 寫在 2.0 enhanced，不在 2.5。支援首幀、首末幀圖生影片。多模態參考 **1–30 張圖**；音訊參考最多 10 段、每段 2–30 秒、總長 ≤30 秒。`generate_audio` 預設開。`return_last_frame` 就是為了把連續影片縫起來。公開路徑擋真人臉參考。[BytePlus LAS](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced)（accessed 2026-09-07, confidence: High）— **Primary**。Seed 發布文獨立寫參考預算 30 圖＋10 影片＋10 音，並說 30 秒裡已能用時間戳做出起承轉合。GPT Image 2 是靜幀廠：文字加圖進、圖出；`input_fidelity` 不再給調。靜幀聖經在這套堆疊上不是可選：鎖寫實身分（正、側、全身、服裝、表情、場景），再當 Seedance 首幀與 `@Image N` 身分參考。[OpenAI 生圖指南](https://developers.openai.com/api/docs/guides/image-generation)（accessed 2026-09-07, confidence: High）。

影片有三種不該混成一種的官方模式。**圖生影片**（首幀或首末幀）把開場構圖錨在像素上。**多模態參考生影片**在運鏡變時保住卡司與服裝。**影片延長**接著一條已收下的片段。產品頁寫單段 30 秒並支援兩次延長；部落格寫多輪往數分鐘；即夢消費端三方轉述另有約 30–180 秒超長模式。LAS API 仍暴露 4–30 秒加延長，沒有 180 秒欄位。保守架構：生成原生 4–30 秒單位；官方延長只用到身分與光還站得住；要硬重置時用末幀當下一鏡首幀。[Seedance 2.5 產品頁](https://seed.bytedance.com/zh/seedance2_5)（accessed 2026-09-07, confidence: High）。

二十六分鐘是 1,560 秒。官方原生上限 30 秒時，成品至少要約 **52 個生成單位**（每條用滿、不修剪），尚未計重試。[AI Post Hub](https://www.aiposthub.com/ai-short-drama-wen-cangsheng-film-industry/)（accessed 2026-09-07, confidence: High）。平均留下 15 秒則下限約 104。Seed 自己的提示示範已在 30 秒生成裡切鏡；即夢手冊摘要建議時間窗至少三秒。一條 30 秒原生往往是六到十個內部鏡頭，所以用 30 秒多鏡頭組出來的 26 分鐘，時間線上仍可能出現數百個剪輯點。真差不在檔案口號，而在刀在模型裡決定還是在 NLE 裡決定、以及身分准許在 30 秒縫還是每 5 秒縫斷開。

網易創作者彙整：2.5 十五秒有人報 630 即夢積分、2.0 只要 230；密 30 秒提示漏動作會浪費整條貴樣本；因此有人 **2.0 打草稿、2.5 只出英雄鏡**。往三分鐘延長時連戲與聲音變差。[網易智能](https://m.163.com/tech/article/L3FTQKIV00097U7T.html)（accessed 2026-09-07, confidence: High）。理性圖案是混用：對白與必須把對口型騎過去的長鏡頭用 15–30 秒帶時間戳的塊；插入與反應用 4–8 秒首幀 I2V。

聲音是另一個架構決定。原生每段音最便宜拿到屬於這張畫面的嘴型與空間聲，卻是很差的 26 分鐘配樂方法，因為每條邊界都是音色重置。三種實際圖案：(1) 每段原生當現場聲，NLE 抽掉或壓低生成配樂；(2) ADR／TTS 加可選對口型，本片未證實；(3) 連續配樂在模型外鋪。寫實長敘事幾乎一定需要 (3)。不要推論原生 Seedance 對白就是完成聲軌。角色一致：**三十張多模態參考適用**；Octo 相鄰未證實；可靈 Elements 不在已確認工具表。調色與字幕在生成器之後。燒進模型字是錯的長片字幕法。必須留在人身上的：劇本、策展聖經、選 take、為情緒剪、連戲帳、混樂、放字幕、判斷何時 AI 滑是 bug。本片具體未知的是大半張製片紙：NLE、鏡頭配比、聲音鏈、生成次數、帳單、交付解析度如何對上 LAS 720p 上限。

### Common Pitfalls and Gotchas

做一部約 26 分鐘的 Seedance 2.5 古裝片，真正的風險不是「模型會不會出畫面」，而是同一套失敗模式會在五十幾段成功鏡頭上複利。Seed 官方單次最長 30 秒，INSIDE 把 1,560 秒／30 秒算成至少約 53 次成功生成再加廢片；那是這部片的結構約束，不是行銷口號。[INSIDE](https://www.inside.com.tw/article/42194-why-ai-short-film-ask-the-common-people-hailed-as-the-most-soulful-ai-animation-became-a-cross-strait-sensation)（accessed 2026-09-07, confidence: High）；[ByteDance Seed 2.5 英文部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）。下面分開寫兩層：**觀眾對《把人寫成了妖》成片回報了什麼**，以及 **Seedance 2.5／GPT Image 2 作為工具的通用坑**。兩者不能混成一句「這部片也有某某穿幫」。

**本片觀眾實際說出口的，不是換臉、不是嘴型崩。** 聯合早報引彈幕：有人看了近兩分鐘才問「這是用 AI 製作的嗎」；同一篇也寫，觀眾誇 26 分鐘內樣貌、場景、光影大致統一，強光下瞳孔收縮、主角寫字筆畫基本正確，被當成「一定和 AI 打磨了很久」。同報接著寫：不少觀眾仍認為 AI 痕跡明顯，金句是「沒有破綻就是最大的破綻」——影片**未出現**人物變形、嘴型錯位等常見 AI 穿幫，但畫面過於乾淨、光滑，少了真人實拍的瑕疵，反而讓人看出「AI 味」。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）。INSIDE 獨立補一層：臉、服、光比早期 AI 短片穩，但眼神銳利度與痛苦層次仍輸真人，「甚至是某些細節上，穿幫的次數還不在少數」。[INSIDE](https://www.inside.com.tw/article/42194-why-ai-short-film-ask-the-common-people-hailed-as-the-most-soulful-ai-animation-became-a-cross-strait-sensation)（accessed 2026-09-07, confidence: Medium，因未列具體穿幫鏡頭）。澳門力報更具體：部分動作銜接略顯僵硬，群眾場面人物細節不完全一致，某些鏡頭光影與尺度有變化。[澳門力報](https://www.exmoo.com/article/264667.html)（accessed 2026-09-07, confidence: Medium）。香港 01、洞傳媒、力報都把成片策略寫成同一套規避：多用中遠景、剪影、煙霧、低飽和水墨，降低口型、手部與肢體破綻的可讀性。這是記者對成片語言的解讀，**不是作者自述**，也不是 B 站彈幕原文；本環境無法直抓 `BV1rHbY6MEB9`（HTTP 412）。[香港 01](https://www.hk01.com/%E9%9B%BB%E5%BD%B1/60384498/ai%E7%9F%AD%E5%8A%87-%E6%8A%8A%E4%BA%BA%E5%AF%AB%E6%88%90%E4%BA%86%E5%A6%96-%E6%87%B6%E4%BA%BA%E5%8C%85-%E7%B6%B2%E6%B0%91%E5%B0%81%E7%A5%9E%E4%BD%9C10%E5%A4%A7%E9%87%8D%E9%BB%9E%E4%B8%80%E6%96%87%E7%9C%8B%E6%87%82%E9%9A%B1%E5%96%BB)（accessed 2026-09-07, confidence: Medium）；[洞傳媒](https://taiwandomnews.com/%e7%94%9f%e6%b4%bb/92385/)（accessed 2026-09-07, confidence: Low，轉述香港 01 同一觀察）。沒有 mainstream 來源點名本片有漢服形制錯誤、現代物品入鏡、或片內中文亂碼；主導抱怨是殘餘平滑感與微表情，不是考據戰。

**官方自己承認的上限，比教程狠。** Seed 中文發布文把「油膩感」當成前代已知病：2.5「有效弱化了視頻生成中常見的『油膩感』」，並對材質、膚質、眼神、光影、飽和度做系統優化；同文說減少了字幕與背景音樂不受控。英文稿把同一件事寫成「more natural, polished visual quality than commonly seen in AI-generated video」，並 minimize uncontrolled subtitles and background music。收尾兩語種一致承認還有進步空間：複雜運動的物理合理性、極多主體交互場景的穩定性。[ByteDance Seed 中文部落格](https://seed.bytedance.com/zh/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）— **Primary**；[英文同文](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）。OpenAI 圖像指南把 GPT Image 家族（含 `gpt-image-2`）的失敗模式寫進 Limitations：複雜提示可達約兩分鐘延遲；文字渲染「significantly improved」但仍可能在精確排字與清晰度上失敗；身分「may occasionally struggle to maintain visual consistency for recurring characters or brand elements across multiple generations」；版面敏感構圖仍難精確落位。[OpenAI Image generation guide](https://developers.openai.com/api/docs/guides/image-generation)（accessed 2026-09-07, confidence: High）— **Primary**。Cookbook 的對策是把不變量每次重講、字面文字加引號、用 `medium`／`high` 跑小字與密排，並用「change only X / keep everything else」防編輯漂移；它沒有給漢代銘文或小楷正確率。[OpenAI cookbook prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)（accessed 2026-09-07, confidence: High）。

**身分漂移是通用 Seedance／GPT Image 坑，不是本片觀眾的主訴。** OpenAI 自己把跨次生成角色一致性列為官方限制。實務上，Seedance 沒有公開的 Identity-Lock 滑桿或使用者可見 seed lock；一致性靠參考槽怎麼花、以及延長而不是重抽。**Low-tier tutorial：** 若干工具部落格把「Identity-Lock」當功能名賣，ByteDance 材料裡找不到這個開關。[AI Video Sensei](https://aivideosensei.com/guides/seedance-2-5-character-consistency)（accessed 2026-09-07, confidence: Low）。GitHub 上也沒有官方 Seedance 2.5 issue tracker——模型閉源。能找到的是第三方診斷技能：`Emily2040/seedance-2.0` 把「Product or face changes」歸因於 I2V 提示重寫了可見身分或動作過載，把「Identity reference conflicts with continuity source」列成延長失敗；`lukasersil/seedance-25` 把「faces that drift, crowds that look like clones」寫成人人都會撞的修復句。這些是實務清單，不是廠商缺陷資料庫。[GitHub Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0/blob/main/skills/seedance-troubleshoot/SKILL.md)（accessed 2026-09-07, confidence: Medium，就社群觀測而言）；[GitHub lukasersil/seedance-25](https://github.com/lukasersil/seedance-25)（accessed 2026-09-07, confidence: Low）。AIX 財經／搜狐在即夢上六場景實測：單人 30 秒與雙人北宋打鬥裡「沒有隨著鏡頭切換而變臉」，但把 50 槽參考拉滿時，檸檬參考圖最後生成了橙汁——槽位變多，模型仍會把素材角色弄錯。[搜狐／AIX財經](https://www.sohu.com/a/1057749967_116132)（accessed 2026-09-07, confidence: Medium）。Hacker News 在 2.5 發布文下（442 分、255 則）抱怨的是官方 demo 卷，不是本片：連續性錯誤、禮盒前後不一致、背景交通逆向、接吻時手瞬移回身側、整體仍「stiff and unnatural」。[@globular-toast / HN](https://news.ycombinator.com/item?id=49138302)（accessed 2026-09-07, confidence: Medium，就 demo 觀感而言）。對這部用 GPT Image 2 假臉、再餵 Seedance 參考圖的古裝片，身分風險在聖經本身會漂，不在真人臉審核。

**手與解剖：GPT Image 論壇仍在報；本片觀眾幾乎沒拿它當出戲點。** OpenAI Developer Community 2026-07 的 GPT Image 2.0 問題匯總裡，使用者回報六指、上臂過長、肢體被遮擋後重建錯長度；有人覺得 2.0 在解剖上相對 1.5 退步，提示「five fingers only」不穩。[OpenAI forum, GPT Image 2.0 issues](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/353)（accessed 2026-09-07, confidence: Medium）。Seed 官方把複雜接觸與多主體交互列為未解物理問題；GitHub 診斷技能對唇形失敗的第一修復是鎖構圖、縮短對白、指定說話人，對不穩文字則「keep text static」。本片側，聯合早報明確寫**沒看到**常見肢體變形；香港 01／力報的解讀是作者用中遠景把這些失敗藏進煙霧。那是規避成功的證據，不是「模型已經不會畫手」。

**口型同步：官方賣點與本片觀感對得上，通用坑仍在。** Seed 發布文與搜狐轉述都把十余種語言的口型／語速同步當 2.5 升級；聯合早報引觀眾：這部片沒有常見嘴型錯位。GitHub 技能與即夢實測仍把長對白、鏡頭大動、未指定說話人列成唇形失敗條件。通用對策是把英雄對白放進 30 秒原生窗、近景少動、或像本片那樣把說話人推到中遠景與剪影——後者是成片選擇，不是模型保證。

**光影連續與 30 秒／延長落差，是長片製作的真坑，也是本片少數被點名的殘餘。** 力報寫某些鏡頭光影與尺度有變化，這是對**本片**的觀察。通用層，Seed 宣稱多輪延長會保持主體、環境與敘事節奏；產品頁較保守，寫最多延長兩次。搜狐實測把雙人打鬥向後延長 10 秒：外貌、服裝、武器接住了，但結尾的靜止對峙被拉長、新動作沒有情緒過渡——「能夠識別前一段視頻長什麼樣，卻還不能完全理解劇情講到哪里」。[搜狐／AIX財經](https://www.sohu.com/a/1057749967_116132)（accessed 2026-09-07, confidence: Medium）。**Low-tier tutorial：** 18183 寫「三十秒是即夢所有生成模式裡畫質和穩定性都最高的檔位」「延長部分因為插值和續寫可能畫質輕微衰減」，並建議高潮放原生 30 秒、過渡放延長。這與官方「延長保持連貫」的行銷並排，但 18183 不是 Seed 文件。[18183](https://www.18183.com/gonglue/202607/mvll0en8.html)（accessed 2026-09-07, confidence: Low）。GitHub 技能把「Extension quality degrades」的第一修復寫成：用回傳末幀當下一鏡首幀，一次只改一個變量。[GitHub Emily2040](https://github.com/Emily2040/seedance-2.0/blob/main/skills/seedance-troubleshoot/SKILL.md)（accessed 2026-09-07, confidence: Medium）。網易智能彙整創作者經驗：30 秒減少拆段，但漏動作之後整段重抽更貴；Jay Nwabueze 在 Dreamina 看到 2.5 的 15 秒要 630 積分、2.0 只要 230，做法是 2.0 打草稿、2.5 出英雄鏡頭。[網易科技](https://www.163.com/tech/article/L3FTQKIV00097U7T.html)（accessed 2026-09-07, confidence: Medium）。

**「AI 平滑／油膩」是本片觀眾的主訴，也是 Seed 自己點名要壓的東西。** 2.0 社群把蠟質膚、用力過猛的表情、千人一面當退熱後的真實抱怨；2.5 官方用「弱化油膩感」回應。搜狐實測說蠟質明顯減輕、毛孔與明暗較像真人。聯合早報對本片的轉述幾乎是同一病的殘留形態：解剖沒崩，乾淨本身成了破綻。**Low-tier tutorial：** 18183 建議在剪映加 5–8% 膠片顆粒與微銳化來「去油」——這是後期補丁，不是模型保證。[18183](https://www.18183.com/gonglue/202608/14b2vrss.html)（accessed 2026-09-07, confidence: Low）。Hacker News 對官方 demo 的判斷同向：明顯 glitch 少了，但仍「looks wrong」。[@efficax / HN](https://news.ycombinator.com/item?id=49138302)（accessed 2026-09-07, confidence: Medium）。

**積分燃燒與即夢過期，是這條管線的經濟坑，不是觀影坑。** 極目新聞上線日記者坐在即夢 App：2.5、720p、非會員 5／10／15／30 秒對 130／260／390／780 點，約每秒 26 點；對照 2.0 VIP 每秒約 14 點。基礎會員連續包月 41 元／月贈 725 點——不夠一次完整 30 秒 2.5。[極目新聞 via 網易](https://www.163.com/dy/article/L36N8Q9T053469LG.html)（accessed 2026-09-07, confidence: High）。HN 使用者轉述 Twitter：Dreamina 30 秒約 1,440 credits／約 15 美元，與 780 點中國價衝突，應視為不同表面或含稅／會員折扣，不能合成一個數。[@JimsonYang / HN](https://news.ycombinator.com/item?id=49138302)（accessed 2026-09-07, confidence: Low）。即夢官方積分規則：每日免費積分當日 24:00 清零；訂閱積分自發放起 30 天，會員到期或取消則失效／凍結後清零；充值積分有效期兩年；消耗順序是快過期者優先，預設每日免費 → 訂閱 → 充值。延長生成時長標為會員功能。[Dreamina／即夢積分規則](https://lf26-cdn-tos.draftstatic.com/obj/ies-hotsoon-draft/dreamina/bbb8a810-1fd5-4962-a24a-9b01acd3dec4.html)（accessed 2026-09-07, confidence: High）— **Primary**。對 26 分鐘片：成功鏡頭至少約 52×30 秒，尚未計重抽。用 780 點／條粗算，僅成功鏡就約 40,560 點；若走 2.0 草稿＋2.5 英雄鏡，點數曲線完全不同。沒有來源公布青瓜蛋的實際帳單。

**片內中文是 GPT Image／Seedance 的通用弱項；本片沒被觀眾拿來罵標題字。** OpenAI 官方只承認「precise text placement and clarity」仍可能失敗，沒有分語言正確率。VentureBeat／社群公告把多語文字當 2.0 賣點。對立的實務來源：**Low-tier：** 圖叮 2026-04／07 寫大字號少字中文看運氣、小字密集別賭，建議「AI 留白＋後期貼字」；BestHub 類教程給出標題 ≤10 字、文字區 ≤4 的經驗上限，不是官方指標。[圖叮AI](https://tudingai.cn/blog/202607/gpt-image-2-chinese-text-garbled-workarounds/)（accessed 2026-09-07, confidence: Low）；[圖叮 能力邊界](https://tudingai.cn/blog/202604/gpt-image-2-capability-boundaries/)（accessed 2026-09-07, confidence: Low）。Qwen-Image-2.0 技術報告的對照圖把 GPT Image 2 的中文海報評成主標題以外常不可讀——這是競爭對手論文，當對立證據而非中立基準。[arXiv 2605.10730](https://arxiv.org/abs/2605.10730)（accessed 2026-09-07, confidence: Medium）。Seed 自己說 2.5 減少了不受控字幕；GitHub 技能仍把運動中的小字／logo 列成必崩項。對東漢卷宗、招牌、題字：穩妥做法是靜幀裡少生成可讀長句，或後期疊字。聯合早報對本片「寫字筆畫基本正確」是讚書寫動作，不是讚牆上文案 OCR。

**歷史服裝錯誤與現代物洩漏，是古裝管線的提示詞病，不是本片已核實的穿幫清單。** 沒有 mainstream 影評點名本片把明制馬面裙或拉鍊穿進東漢。通用層，漢服教程反覆寫的坑是：只寫「古裝／hanfu」會得到無朝代影樓裝、唐廓型加明繡、左衽（斂服）、運動鞋／手錶／現代耳環、西方骨相。**Low-tier tutorial，標明以免誤當史據：** [AI 工具指南](https://aitoolsguidebook.com/zh/articles/hanfu-character-prompts/)（accessed 2026-09-07, confidence: Low）；[FlowPix](https://www.flowpixai.com/ai-art/ai-painting-hanfu-gufeng.html)（accessed 2026-09-07, confidence: Low）；[圖叮 形制避坑](https://tudingai.cn/blog/202606/ai-generate-ecommerce-batch-bl-27edbe/)（accessed 2026-09-07, confidence: Low）。Seedance 側，官方與較乾淨的提示指南都要求給參考圖寫角色（哪張管身分、哪張管場景），並明示排除項，否則參考圖背景、路人、logo 會漏進成片。Morphic 把「Reference text appears in video」列成未排除文字遷移；Tryonr 把「刪除無人機與前景軌道、其餘保持不變」當清穿幫公式——皆 **Low-tier**，但與官方「其餘保持不變」的編輯語法同向。[Morphic Seedance 2.5 指南](https://morphic.com/resources/how-to/seedance-2-5-guide)（accessed 2026-09-07, confidence: Low）；[Tryonr](https://tryonr.com/zh/blog/seedance-2-5-video-editing-extend)（accessed 2026-09-07, confidence: Low）。搜狐實測裡，工業機械臂鏡頭開頭無故出現提示詞沒要求的鋼筆特寫，再靠局部編輯換成手機——這是「模型自己加現代物」的通用例子，與本片無直接對照。

**五十幾段原生音床互打，是長片剪輯的結構坑。** Seedance 預設 `generate_audio: true`（BytePlus／多數表面；部分轉售把預設寫成 false，屬文件衝突）。每段 MP4 內建對白、環境聲、有時還有 BGM。官方 2.5 宣稱減少不受控 BGM，但 LinkedIn 實務串仍寫負面提示「no music」壓不住，只好做分軌或後期剝樂；有人把「同一套合成床」當成 AI 廣告的新指紋。[Justinas Vosylius / LinkedIn](https://www.linkedin.com/posts/justinas-vosylius_generativeai-aivideo-genai-activity-7493583013293809664-5Br9)（accessed 2026-09-07, confidence: Low）。GitHub 技能把「Audio phase restarted」列成延長／接片失敗：完成的對白或音樂相位沒被記下，下一段會重開。Flixpress 比較延長與末幀串接時寫：兩幀對得上，房間底噪、聲線、配樂重啟仍會露出接縫。[Flixpress](https://flixpress.com/seedance-2-5-extension-vs-last-frame-chaining-which-keeps-a-60-second-video-consistent/)（accessed 2026-09-07, confidence: Low）。作者沒公布 NLE 或是否關原生音；觀眾誇「配音很專業」不能當流程證據。結構上，26 分鐘若保留每段原生 BGM，接點會打架；若要一條連續配樂，必須在剪輯器重鋪，而不是指望 50 段各自生成的床對上調。

**API 產物 URL 24 小時過期，是開發者坑；真人臉參考封鎖對這部假臉片幾乎不相干。** BytePlus LAS 明文：Seedance 2.x **不支援直接上傳含真人臉的參考圖或影片**；要用肖像須走白名單素材庫、授權上傳後以素材 ID 呼叫。生成預簽名鏈接「valid for 24 hours」。[BytePlus LAS](https://docs.byteplus.com/en/docs/Byteplus_LAS/video_gen_enhanced)（accessed 2026-09-07, confidence: High）— **Primary**。DEV 實務文在 2.5 回傳裡看到 `X-Tos-Expires=86400`；任務 ID 另留約 7 天，但檔案不在。[DEV Community](https://dev.to/codesugar_lin_037a57b06a4/seedance-25-api-the-official-endpoint-and-6-gotchas-a22)（accessed 2026-09-07, confidence: Medium）。本片角色是 GPT Image 2 生成臉，官方真人臉閘門不是障礙；若有人把「長得像張晚意／陳曉」的截圖當參考圖反餵 API，才可能撞審核。聯合早報只記觀眾覺得主角「有幾分相似」，沒有說作者用了真人劇照。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High，就觀感轉述而言）。

把這些壓回這部片的製作含義：觀眾已經證明，2026 年 8 月用 Seedance 2.5＋GPT Image 2 可以把換臉、崩嘴、明顯六指壓到「不讓人出戲」；他們沒有證明油膩感、群眾臉、光影跳、延長後的劇情節奏、以及五十段音床能在一次生成裡消失。官方承認的失敗模式（複雜物理、多主體、跨次角色一致性、精確中文排字）仍然是排片時要主動避開或後期修的東西，而不是被這部神作取消的東西。

> Conflicts noted（pitfalls）: 即夢 780 點／30 秒 vs HN 轉述 Dreamina 1,440 credits／~$15；`generate_audio` 預設 true（官方／多數 API）vs 部分轉售文件寫 false；官方「延長保持主體與節奏」vs 搜狐實測「畫面接住、劇情斷拍」vs Low-tier「延長畫質衰減」；OpenAI 多語文字賣點 vs 圖叮「中文仍賭運氣」vs Qwen 論文對照圖；香港 01「用中遠景掩蓋口型破綻」是記者推論，聯合早報則寫觀眾沒看到嘴型錯位——兩者可並存（掩蓋成功），但不能當成作者自述。GitHub 無官方 issue，只有第三方技能庫。
> Gaps: B 站頁 HTTP 412，無彈幕原文庫；無作者製作日誌、廢片率、即夢 vs API、是否關原生音；無本片漢服形制或現代物穿幫的逐鏡清單；無獨立 Seedance 2.5 Elo；OpenAI 無分語言文字正確率；延長「最多兩次」產品頁 vs 部落格「數分鐘」vs 即夢約 180 秒超長模式未在本軸逐一核對。

### Security and Compliance

> ⚠️ 本節整理公開法規與產品安全說明，供研究用，不是法律意見，也不是對本片的合規認定。

截至 2026-09-07，這裡找到的官方來源 **沒有** 點名本片被禁、下架或行政處罰。聯合早報寫到 9 月 2 日仍可看、仍在每周必看。[聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）。本環境打不開 B 站觀看頁（HTTP 412），其後狀態未再獨立核實。

上傳時已適用四部門《人工智能生成合成內容標識辦法》（國信辦通字〔2025〕2 號），2025-09-01 施行。顯式標識（觀眾看得見）與隱式元數據分開；影片開頭幀與播放器周圍要顯著提示；使用者發表合成內容須聲明；禁止惡意刪改隱匿標識。[中國政府網](https://www.gov.cn/zhengce/zhengceku/202503/content_7014286.htm)（accessed 2026-09-07, confidence: High）— **Primary**。強制國標 GB 45438-2025 同行。B 站實作：投稿開【創作聲明】選【該視頻使用人工智能合成技術】；2026-05-15 治理帖把 AI 標識升到一等頁，漏標可補標、打回、下架。[嗶哩嗶哩治理小分隊](https://www.bilibili.com/opus/1202507670848798745)（accessed 2026-09-07, confidence: High）。聯合早報寫完成片顯示「含 AI 生成內容」晶片。公開來源沒顯示隱式元數據是否活進發布的 MP4。

廣電總局令第 16 號《微短劇發展管理辦法》2026-09-01 施行（本片上傳後十五天）。第 2 條定義是情節連續的 **劇集，每集不超過二十分鐘**。單支 26 分鐘片長過每集上限，也不是通常意義的劇集——這是最硬的公開理由，不把許可與每集編號機器自動套上。第 33(3) 條仍要分發者對「具有微短劇特徵」的較短 UGC 做內容管理；第 34 條要 AI 微短劇每集顯著提示。若它被認定為微短劇，專題（政治、軍事、司法、公安等）可進 I 類；第 25 條含歪曲歷史人物、宣揚歷史虛無等禁則。那些規則只適用先被認定為微短劇的作品。[國家廣播電視總局](https://www.nrta.gov.cn/art/2026/7/31/art_113_73785.html)（accessed 2026-09-07, confidence: High）— **Primary**。2023 年《生成式人工智能服務管理暫行辦法》仍適用對中國公眾提供與使用生成式 AI。[中國政府網](https://www.gov.cn/zhengce/zhengceku/202307/content_6891752.htm)（accessed 2026-09-07, confidence: High）。

Seedance 2.x 不支援直接上傳含真人臉的參考；生成 URL 24 小時過期；任務 id 留約 7 天；`watermark` 預設 false。[BytePlus LAS](https://docs.byteplus.com/en/docs/byteplus_las/video_gen_enhanced)（accessed 2026-09-07, confidence: High）。本片是 GPT Image 2 虛構臉，真人臉門預期不響。OpenAI 圖帶 C2PA 與 SynthID；C2PA 可被轉碼剝掉。任何靜幀被重編碼成 Seedance 參考、再進 NLE、再進 B 站，應假設 C2PA 頭已丟。[OpenAI Help Center](https://help.openai.com/en/articles/8912793-provenance-signals-content-credentials-synthid-in-openai-generated-content)（accessed 2026-09-07, confidence: High）。

《搜神記》與《後漢書》作者卒於四、五世紀。中國著作權法第 23 條自然人財產權為有生之年加五十年，早已屆滿；第 22 條人身權不受期限。[國家版權局](https://www.ncac.gov.cn/xxfb/flfg/flfg_532/202103/t20210309_50530.html)（accessed 2026-09-07, confidence: High）。沒找到對本片古典引文的權利人主張。訓練資料義務在提供者側（暫行辦法第 7 條）；上傳者不是訓練者。完成片是否構成視聽作品取決於人的獨創貢獻；報導描述人類劇本與剪輯，但沒有對本片的公開判決。

2025–2026 清朗行動把「用 AI 歪曲歷史人物／二創經典」當執法類別。2026-09-02 第二階段結果點名 B 站等升級偵測；典型案例是《三國》《西遊》低質流量帳，不是這部 B 站寓言。[國家網信辦](https://www.cac.gov.cn/2026-09/02/c_1790099041364574.htm)（accessed 2026-09-07, confidence: High）。類別存在，不證明本片在類別裡。沒有來源記錄點名本片的處分。沒有點名，也不等於正面放行函。

---

## Key Findings

According to [聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）與 [UDN](https://udn.com/news/story/7332/9709067)（accessed 2026-09-07, confidence: High），「我這一生最大的罪，是把人寫成了妖」不是古書原句，而是 2026 年 8 月 17 日 Bilibili UP 主青瓜蛋丶上傳的約 26 分鐘 AI 古裝短片片名單（片內名《妖異簿·問蒼生》）。全片標「含 AI 生成內容」、無人出演。作者留言把劇本認成幾年前隨筆改寫，並聲明情節虛構。播放量按日期讀：8 月 23 日約 1,272 萬，9 月 2 日突破 1,800 萬。這表示提問裡的「罪」首先是一部作品的標題。

According to [Marie Claire 台灣](https://www.marieclaire.com.tw/entertainment/tvshow/95568)（accessed 2026-09-07, confidence: High）引述的作者留言，影像 **主要** 用兩套模型完成：OpenAI **GPT Image 2** 生圖，字節跳動 Seed **Seedance 2.5** 生影片。NOWnews、中央社、聯合早報交叉轉述同一公式。[NOWnews](https://www.nownews.com/news/6868562)（accessed 2026-09-07, confidence: High）。Seed 官方單次原生 **4–30 秒**，參考最多 30 圖／10 影片／10 音，可延長但不是 26 分鐘一次渲出。[Seed 2.5 部落格](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)（accessed 2026-09-07, confidence: High）。This suggests 技術答案是「兩模型加人類剪輯」，不是「一個神奇按鈕」。剪輯軟體、TTS 品牌、音樂來源、即夢還是 API，作者都沒點名。

According to [Chinese Text Project 搜神記卷六](https://ctext.org/wiki.pl?chapter=836102&if=en)（accessed 2026-09-07, confidence: High）與 [後漢書](https://ctext.org/hou-han-shu/wu-xing-wu/zh)（accessed 2026-09-07, confidence: High），片中「寺壁黃人」「木不曲直」「梁伯夏后」「草作人狀」對得上漢代災異紀錄，且古書自己已把它們接到黃巾。影片做第二次翻轉：把徵兆寫成必須誤檔為妖的人事。中央社與 UDN 核對的片尾是「後人讀妖，勿問鬼神，問蒼生」。[中央社](https://www.cna.com.tw/news/acn/202608250306.aspx)（accessed 2026-09-07, confidence: High）。This suggests 核心技術有兩層：生成模型是筆；志怪曲筆才是文法。

According to [Artificial Analysis](https://artificialanalysis.ai/video/leaderboard/text-to-video)（accessed 2026-09-07, confidence: High）與各廠官方頁，2026 年 8 月初一個大陸個人 UP 若要做講中文的寫實古裝長片，Seedance 2.5 是理性預設：當時唯一普遍可及、同時具備約 30 秒原生、中文向原生音、30 張服裝聖經、即夢裡人民幣支付的消費模型。Wan 3.0 規格最近、每秒更便宜、AA Elo 更高，但 8 月初仍偏邀測。可靈與 MiniMax H3 約 15 秒。Veo／Runway／Sora 過不了牆或對白門。This suggests 選型邏輯是「誰能在檔期裡做完」，不是「誰在榜上第一」。

According to [聯合早報](https://www.zaobao.com.sg/entertainment/story20260903-9619222)（accessed 2026-09-07, confidence: High）與 [INSIDE](https://www.inside.com.tw/article/42194-why-ai-short-film-ask-the-common-people-hailed-as-the-most-soulful-ai-animation-became-a-cross-strait-sensation)（accessed 2026-09-07, confidence: High），爆紅順序是先畫面、再劇本、再金句；觀眾共識是「AI 不是重點」。殘餘抱怨是太乾淨的「AI 味」。下架是跨媒體記錄的謠言；9 月 2–3 日仍在架是記錄的事實。網信辦清朗行動把「AI 二創經典」當執法類別，但 9 月 2 日典型案例點的是三國／西遊流量帳，不是本片。[國家網信辦](https://www.cac.gov.cn/2026-09/02/c_1790099041364574.htm)（accessed 2026-09-07, confidence: High）。令第 16 號定義是每集少於 20 分鐘的劇集；26 分鐘單片不自動套進去。This suggests 它證明標好的作者型 AI 短片仍可被平台助推，不是證明禁區已開。

## Strategic Recommendations

1. **把技術答案寫成三層，不要寫成兩個 App 名。** 已證實：GPT Image 2 靜幀＋Seedance 2.5 動態。合理重建：靜幀聖經 → 4–30 秒 I2V／多鏡頭提示 → 延長或末幀串 → 人類 NLE，粗算至少約 52 次成功生成。未知：剪輯軟體、聲音混、帳單。證據：[Marie Claire](https://www.marieclaire.com.tw/entertainment/tvshow/95568)、[Seed 官方](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)。若有人問「用哪些技術完成的」，先答這三層。

2. **若要做同類片子：先鎖離線靜幀聖經，再用大陸可登入的 30 秒級音畫模型出對白英雄鏡。** 即夢 Seedance 2.5 仍是主選；百煉 Wan 3.0 若帳號已 GA，是最不痛的能力遷移；海螺 H3 當成本對沖。不要把管線建在 Veo、Runway 或已日落的 Sora 上，除非已有外卡且不需要可靠中文原生對白。積分策略採網易實務：便宜模型打草稿、2.5 出英雄鏡。

3. **不要把這部片當微短劇工業樣板，也不要在未讀令第 16 號前把它改成系列變現。** 它是 B 站作者型單片，不像抖音大賽短片、不像愛奇藝持證網絡故事片。若切成每集 <20 分鐘或做成連續劇，黃巾主題靠近專題 I 類風險。證據：[NRTA 令第 16 號](https://www.nrta.gov.cn/art/2026/7/31/art_113_73785.html)。令文第 2 條本身是 High。

4. **讀政治時分開三件事：文本結構、觀眾寓言、官方執法。** 文本是志怪曲筆（High）。觀眾說「電視劇不敢拍的，AI 來做」（High）。官方執法：到 9 月初沒有點名下架（High 就「未找到點名處分」；Low 若讀成「已獲放行」）。不要用「已被禁」的社交帖當事實。

5. **把本片當「剪輯生產已可行、原生時長仍是 30 秒級」的標定物，而不是「電影已被模型取代」。** 觀眾仍讀出 AI 滑。Seed 承認複雜物理與多主體不穩。勞動側真人短劇劇組在縮，春晚檔真人播放仍可遠高於 AI 短片。兩邊都引用。

## Risks and Uncertainties

- **資料缺口：** 無公開劇本、舊隨筆、製作日誌、鏡頭數、NLE 名稱、TTS／配樂來源、即夢 vs API、帳單。B 站頁 HTTP 412。9 月 3 日之後在架狀態未從頁面核實。作者真名未核實。
- **低信心主張：** 製作成本「不到萬元」；打賞人民幣 100 萬與投幣 100 萬被部分稿件混用；環球時報在兩模型之外另寫即夢；本片據稱 1920×1080 與 LAS 2.5 720p 上限如何對上。
- **未解衝突：** 裴令史 vs 裴令時；B 站 8 月 17 日 vs 新榜 8 月 13 日／西瓜 8 月 16 日；Seedance 解析度與延長次數各文件互打；NOWnews 把靜幀→驅動當事實、INSIDE 標猜測。
- **領域風險：** 「AI＋翻轉歷史人物」是清朗執法類別；本片主題落在該光譜上。令第 16 號對系列形態已上線。閉源積分制把角色聖經鎖在廠商元素裡就不可攜。Sora 已證明影片產品可硬日落。
- **偏誤：** 英文覆蓋薄；部分兩岸稿件把片子當政治證據。本報告雙引，不把任一營的讀法當作者意圖。作者公開意圖是虛構、辯證、藝術追求。

## Next Steps

- 若作者或即夢放出幕後：核對鏡頭數、延長與否、聲音鏈、是否 Octo／白模。
- 對片核對金句、主角讀音（令史／令時）、四個災異如何 staging。
- 獨立再抓 B 站頁，更新 9 月 3 日之後的在架與播放量。揮發主題應在 30 天內重跑。
- 若問題轉成「我要做一部」：用本報告矩陣選模型，先做 3 分鐘對話場測角色鎖與中文對白。
- 本請求已回答：出處、兩套已點名模型、官方能力上限、為何 26 分鐘仍要人類剪輯、文學互文、爆紅與禁言謠言的分層。未公開的 prompt 與專案檔不是公開網能補的。

---

*研究快照日期：2026-09-07。網頁會變。監管、播放狀態與模型價目屬揮發資訊。*
