---
topic: "我這一生最大的罪，是把人寫成了妖（Bilibili AI 短片）製作技術與作品拆解"
type: "product"
goals: "確認作品出處與作者；釐清影像、生圖與後製用了哪些模型與流程；評估技術能力、限制與爆紅原因"
date: "2026-09-07"
methodology: "Parallel web research via sub-agents. Citations inline per references/citations.md. Confidence levels: High / Medium / Low. Step 2 completed 2026-09-07; Steps 3–5 pending."
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

_Pending Step 3 — reception, controversy, and industry reaction._

### Changelog Highlights (last 12 months)

_Pending Step 3 — model releases that made this film possible (Seedance 2.0→2.5, GPT Image lineage)._

### Community Health

_Pending Step 3._

## Strategic Signals

### Competitive Positioning

_Pending Step 3 — China AIGC short-drama landscape and comparable AI films._

### Adoption Signals

_Pending Step 3._

### Risk Signals

_Pending Step 3 — labeling rules, possible takedown talk, political-reading risk._

## Comparative Analysis

### Top Options Head-to-Head

_Pending Step 3 — Seedance 2.5 vs Kling 3 vs Veo / Gemini Omni vs Runway for this use case._

### Decision Matrix

| Option | Performance | DX  | Community | Cost | Lock-in | Notes |
| ------ | ----------- | --- | --------- | ---- | ------- | ----- |
| _TBD_  |             |     |           |      |         |       |

### Migration and Lock-in Risks

_Pending Step 3._

## Implementation Considerations

### Recommended Architecture Patterns

_Pending Step 4 — long-form AI film assembly from 4–30s clips._

### Common Pitfalls and Gotchas

_Pending Step 4._

### Security and Compliance

_Pending Step 4 — AI content labels, micro-drama rules, face-reference bans._

---

## Key Findings

_Populated at Step 5._

## Strategic Recommendations

_Populated at Step 5._

## Risks and Uncertainties

_Populated at Step 5._

## Next Steps

_Populated at Step 5._
