---
topic: "US stocks: hold to late December vs sell by late November (historical seasonality)"
type: "financial"
goals: "Compare historical November vs December US equity returns, win rates, and left-tail risk to decide whether a cash-need-by-year-end holder is better selling around November 30 or holding through December 31. Secondary lens: Nasdaq/semiconductors (SOXX) and calendar anomalies (Santa Claus rally, tax-loss selling)."
date: "2026-09-13"
methodology: "Parallel web research via sub-agents across custom seasonal axes (broad indexes, tech/semis, tails, calendar anomalies, sector/style, FX overlay, holiday liquidity, exception years, cash-need decision, academic critique). Citations inline per references/citations.md. Confidence: High / Medium / Low."
---

# Research Report — US Stocks: Late November vs Late December Exit

> **Type:** financial (custom seasonal axes) | **Date:** 2026-09-13 | **Constraints:** US listed equities; historical monthly/window returns; decision framed for an investor who must raise cash by end of December 2026
>
> **Goals:**
> - Compare long-run November vs December average returns and win rates for broad US indexes
> - Check whether Nasdaq / semiconductors follow the same pattern
> - Compare volatility and worst-case drawdowns in each month
> - Separate well-documented calendar effects from folklore
> - Translate the history into a sell-Nov-30 vs hold-to-Dec-31 choice

> **Assumptions:** type=financial with custom seasonality axes. “Better” mixes average return, hit rate, and left-tail risk. Scope is US equities, with a secondary SOXX/semiconductor lens from a prior cash-need context. Horizon is long-run history, not a 2026 return forecast. Index returns are in USD. This is historical research, not personalized investment advice.

> **Existing reports:** `research/financial-us-treasury-buyback-market-reaction-2026-08-20.md` is unrelated. Started fresh.

> **Methodology note:** Step 1 auto-scoped. Financial.md funding/valuation axes were replaced with calendar-return axes. Steps 2–4 used parallel web agents. Step 5 reconciles sample-window conflicts before recommending.

---

## Broad US Equity Seasonality (November vs December)

According to the [Stock Trader’s Almanac](https://www.stocktradersalmanac.com/Alert/20241024_1.aspx) (accessed 2026-09-13, confidence: High), November is the best S&P 500 month since 1950 and the best Russell 1000 and Russell 2000 month since 1979, with average gains of about 1.8% for the Dow and S&P 500 and about 2.5% for the Russell 2000. The same firm’s later December notes report that December ranks third for the Dow and S&P 500 since 1950, averaging 1.6% and 1.5% in the [2024 edition](https://www.stocktradersalmanac.com/Alert/20241126_1.aspx) (accessed 2026-09-13, confidence: High) and 1.5% and 1.4% in the [2025 edition](https://www.stocktradersalmanac.com/Alert/20251113_1.aspx) (accessed 2026-09-13, confidence: High). Those Almanac figures are presented as calendar-month index moves and should be read as price returns unless a total-return series is specified.

LPL Research, citing Bloomberg, reports a closely matching post-1950 S&P 500 pattern. In December 2024 LPL wrote that November’s long-run average is around 1.8% and that December is the second-best month since 1950, with a 1.6% average gain and the highest share of positive months, at about 74% ([LPL via AdvisorAnalyst](https://advisoranalyst.com/2024/12/04/is-the-santa-claus-rally-still-coming-to-town.html/), accessed 2026-09-13, confidence: High). By December 2025 the same shop’s updated figures were a 1.4% December average and a 73% win rate, with the average gain 2.9% in up Decembers and the average loss 2.6% in down Decembers ([LPL via AdvisorAnalyst, 2025](https://advisoranalyst.com/2025/12/04/chart-check-into-year-end.html/), accessed 2026-09-13, confidence: High). Nasdaq Dorsey Wright put December’s S&P 500 average at 1.7%—with November the only stronger month—and December’s win rate at 77%, and reported a December 25th-percentile return of +0.2% (the best “bad” outcome of any month) ([Nasdaq Dorsey Wright](https://dorseywright.nasdaq.com/research/bigwire/2025/12/01/12-01-2025/december-return-tendencies-strong-month-ahead), accessed 2026-09-13, confidence: High).

The longest S&P 500 price sample reverses the post-1950 mean ranking. Yardeni Research, using Standard & Poor’s and Haver Analytics from 1928 through October 2023, reports an average S&P 500 percent change of 1.0% in November and 1.3% in December; December also has the fewest down observations of any month in that chart (26), compared with 37 down Novembers ([Yardeni Research PDF](https://archive.yardeni.com/pub/stmktreturns.pdf), accessed 2026-09-13, confidence: High). Ciccone and Etebari’s CRSP study from January 1926 through December 2006 found that on the value-weighted CRSP index, December’s mean total return was 1.79% versus November’s 1.65%, and December’s win rate was 81.48% versus November’s 70.37%. November’s median, however, exceeded December’s (2.55% versus 1.83%), which indicates a more left-skewed November ([Ciccone and Etebari, 2008](https://scholars.unh.edu/cgi/viewcontent.cgi?article=1022&context=account_facpub), accessed 2026-09-13, confidence: High).

Sources disagree once the metric and sample are specified. In postwar S&P 500 price data used by the Almanac, LPL, and Dorsey Wright, November’s mean is usually larger and December’s win rate is usually higher. In the longest S&P price sample and the longest CRSP value-weighted total-return sample, December’s mean and win rate both exceed November’s. A Low-tier SPY reconstruction for 1994–2026 tilts the other way again: November +2.6% versus December +0.9% ([ChartRow](https://www.chartrow.com/visuals/seasonality), accessed 2026-09-13, confidence: Low). This suggests that “November beats December on average” is mainly a postwar and especially a recent-sample result, while the century-long value-weighted record still gives December the edge on both mean and hit rate.

Dorsey Wright reports that almost all of the average December net gain occurs in the second half of the month: the S&P 500 was positive in 60% of first halves versus 80% of second halves since 1950, and the Russell 2000 was positive in only 46% of first halves versus 84% of second halves since 1978 ([Nasdaq Dorsey Wright](https://dorseywright.nasdaq.com/research/bigwire/2025/12/01/12-01-2025/december-return-tendencies-strong-month-ahead), accessed 2026-09-13, confidence: High). LPL’s December price-progression charts make the same point: since 1950 the index has tended to hover near flat in the first half and to lift around the 11th trading day ([LPL, 2024](https://advisoranalyst.com/2024/12/04/is-the-santa-claus-rally-still-coming-to-town.html/), accessed 2026-09-13, confidence: High).

> Conflicts noted: Post-1950 sources generally rank November ahead of December on average return, while Yardeni 1928–2023 and CRSP 1926–2006 rank December ahead on the mean. CFRA is quoted both as calling December the best month since 1945 ([CNBC, 2022](https://www.cnbc.com/2022/12/05/december-tends-to-be-strong-for-the-market-how-our-stocks-have-done.html), accessed 2026-09-13, confidence: Medium) and as trailing only November ([Bloomberg, 2025](https://www.bloomberg.com/news/articles/2025-11-25/us-stocks-strong-december-history-seen-tested-by-ai-malaise), accessed 2026-09-13, confidence: Medium). Sources mix price-only and total return.
>
> Gaps: No official S&P Dow Jones Indices November/December total-return table. No CRSP update after 2006. No Established-tier median-versus-mean table for the S&P 500 over 1950–present.

---

## Nasdaq, Technology, and Semiconductors

Across the Nasdaq Composite, the Nasdaq-100, GICS technology, and US semiconductor benchmarks, the historical pattern is that November has been the stronger month and December the weaker one. According to CNBC’s recap of the Stock Trader’s Almanac, the Nasdaq Composite has averaged a gain of nearly 2% in November since the index’s 1971 start, making November the second-best calendar month for Nasdaq ([CNBC](https://www.cnbc.com/2023/10/31/something-for-the-bulls-november-is-typically-the-best-month-for-the-stock-market.html), accessed 2026-09-13, confidence: High). Nasdaq’s Composite factsheet states that Technology was 63.51% of the Composite as of 30 June 2026, so Composite results are already a tech-heavy series ([Nasdaq Composite factsheet](https://indexes.nasdaqomx.com/docs/FS_COMP.pdf), accessed 2026-09-13, confidence: High).

The Nasdaq-100 and QQQ amplify that November-over-December gap. tastylive reported that Nasdaq-100 futures averaged −0.71% in December over the prior 10 years (second-worst month) and +0.42% over 20 years (fifth-worst), and that both the S&P 500 and Nasdaq-100 had averaged negative December returns over the past decade even though stocks were up in six of those 10 Decembers ([tastylive](https://www.tastylive.com/news-insights/december-market-trends-stocks-gold-typically-perform-year-end), accessed 2026-09-13, confidence: Medium). A Low-tier monthly-return series for the Nasdaq-100 from 1986 through 2025 implies November averages of about +2.4% with a 68% win rate and December averages of about +1.6% with only a 53% win rate; the 2016–2025 window yields November about +3.8% versus December about −0.1% ([History of Market NDX](https://historyofmarket.com/api/ndx/monthly.json), accessed 2026-09-13, confidence: Low).

Semiconductor vehicles cannot be spliced into one long sample without caveats. Nasdaq’s PHLX Semiconductor Sector Index (SOX) began 1 December 1993 ([Nasdaq PHLX SOX](https://indexes.nasdaq.com/index/overview/SOX), accessed 2026-09-13, confidence: High). iShares states that SOXX’s fund inception is 10 July 2001, and an SEC risk factor states that SOXX tracked three different indexes over time, so history tracking the current NYSE Semiconductor Index is only available since 21 June 2021 ([iShares SOXX](https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf), accessed 2026-09-13, confidence: High); [SEC Form 424B2](https://www.sec.gov/Archives/edgar/data/70858/000191870426001927/form424b2.htm) (accessed 2026-09-13, confidence: High). Low-tier seasonality sites still show a larger November than December: SeasOptima’s 22-year SOXX study reports November +3.47% (67% win rate) and December +1.98% (62%) ([SeasOptima SOXX](https://www.seasoptima.com/en/seasonality/ishares-semiconductor-etf-soxx), accessed 2026-09-13, confidence: Low).

Named exception years invert or exaggerate that average. Official Nasdaq Composite price returns are November 2018 +0.34% and December 2018 −9.48%, and November 2022 +4.37% and December 2022 −8.73% ([Nasdaq Composite factsheet](https://indexes.nasdaqomx.com/docs/FS_COMP.pdf), accessed 2026-09-13, confidence: High). Official Nasdaq-100 price returns are November 2018 −0.26% and December 2018 −8.91%, and November 2022 +5.48% and December 2022 −9.06% ([Nasdaq-100 factsheet](https://indexes.nasdaq.com/docs/FS_NDX.pdf), accessed 2026-09-13, confidence: High). 2008 is the opposite exception: the Composite fell 10.67% in November and rose 5.41% in December ([StatMuse](https://www.statmuse.com/money/ask/nasdaq-returns-by-month-2008), accessed 2026-09-13, confidence: Medium). The Almanac calls November 2000 Nasdaq’s second-worst month on record at −22.9% ([Stock Trader’s Almanac](https://www.stocktradersalmanac.com/Alert/20241024_1.aspx), accessed 2026-09-13, confidence: High).

This suggests that a rule of “hold tech into late December” has historically left more return on the table in November than it has reliably captured in December, while “sell by late November” has sometimes avoided December air-pockets—at the cost of missing the Almanac’s still-positive long-run December rank for the Composite.

> Conflicts noted: Long-run Almanac ranks (Nasdaq December is third-best since 1971) conflict with 10- and 20-year Nasdaq-100 studies that treat December as one of the worst months. SOXX November averages conflict sharply across short-window vendors; both still rank November above December.
>
> Gaps: No peer-reviewed paper tests November-versus-December seasonality specifically for Nasdaq, QQQ, SOX, SOXX, or SMH. No official 1993–present PHLX SOX November versus December average.

---

## Volatility, Drawdowns, and Worst Years

Across long S&P 500 samples, December is the less frequent down month and, on average, the quieter month. Yardeni counts 26 down Decembers versus 37 down Novembers from 1928–2023; when the month is down, the average loss is about −3.2% in December versus −4.0% in November ([Yardeni Research](https://archive.yardeni.com/pub/stmktreturns.pdf), accessed 2026-09-13, confidence: High). Dorsey Wright reports that even the 25th-percentile December return since 1950 is about +0.2% ([Nasdaq Dorsey Wright](https://dorseywright.nasdaq.com/research/bigwire/2025/12/01/12-01-2025/december-return-tendencies-strong-month-ahead), accessed 2026-09-13, confidence: High).

Those “high floor” statistics describe the typical year, not the left tail. The worst December on the modern S&P 500 record is December 2018. Morningstar’s total-return figure is −9.03%, the 11th-worst any calendar month from 1969–2018 and the worst December since the Depression ([Morningstar](https://www.morningstar.com/columns/rekenthaler-report/how-rare-was-decembers-stock-market-loss), accessed 2026-09-13, confidence: High). Dow Jones Market Data called it the worst December for the S&P 500 and Dow since 1931; the Nasdaq Composite’s −9.5% was its worst December on record ([Fox Business](https://www.foxbusiness.com/markets/dow-sp-500-having-worst-month-since-1931-as-grinch-hits-wall-st), accessed 2026-09-13, confidence: High). December 1931 is the benchmark those 2018 stories measure against, with printed losses ranging from −13.43% to −14.53% depending on the series ([StatMuse](https://www.statmuse.com/money/ask/s-and-p-500-1931-monthly-returns), accessed 2026-09-13, confidence: Medium); [USA Today](https://www.usatoday.com/story/money/2018/12/20/dow-jones-fed-rate/2373928002/), accessed 2026-09-13, confidence: High).

November’s worst modern S&P months are usually a bit shallower than December 2018, except November 1973 at about −11% ([StatMuse](https://www.statmuse.com/money/ask/s-and-p-500-monthly-returns-for-1973), accessed 2026-09-13, confidence: Medium). Named crisis pairs: 1987 saw the crash in October, November still fell about −8.5%, then December rebounded +7.28%; 2008 November about −7.0% and December about +1.0% on SPY total return; 2018 November +1.9% and December −8.8%; 2022 November +5.6% and December −5.8% ([ChartRow](https://chartrow.com/visuals/seasonality), accessed 2026-09-13, confidence: Medium). Tech’s left tail is fatter: the Nasdaq Composite fell −21.67% in November 2000 and another −6.56% in December 2000 ([StatMuse](https://www.statmuse.com/money/ask/nasdaq-monthly-returns-1999-to-2000), accessed 2026-09-13, confidence: Medium).

November, not December, is the higher-vol month in the studies that split the calendar. An academic options paper documents lower December realized volatility, especially in the second half of the month ([Harbourfront summary of SSRN 5121679](https://harbourfronts.com/volatility-risk-premium-seasonality-across-calendar-months/), accessed 2026-09-13, confidence: Medium). Vasconomics, using VIX levels from 1990 through August 2023, ranks October, September, and November as the three highest average VIX months; the sample maximum is 62.64 in November 2008 ([Vasconomics](https://vasconomics.com/post/volatility_seasonality/), accessed 2026-09-13, confidence: Medium).

CFRA’s Sam Stovall found that when the S&P 500 gained 5% or more in November (14 times since 1945), December’s rise and its frequency of advance were both below average ([Kiplinger](https://www.kiplinger.com/investing/stocks/601831/stock-market-today-113020-dow-closes-out-best-month-since-1987), accessed 2026-09-13, confidence: High). No second-sourced long-sample frequency of “December fully erases a positive November” was found. A single-source count on ChartRow’s 1994–2025 SPY grid: 25 positive Novembers; 8 of those 25 were followed by a down December, and 3 of 25 (2015, 2018, 2022) fully erased the November gain (confidence: Low).

This suggests the risk evidence does not line up with return folklore in a single direction. December is usually the lower-vol, higher-floor window, and famous crash months (October 1929, October 1987, October 2008, March 2020) are not Decembers. The case for selling by late November is the fat December left tail in specific years—1931, 2018, 2002, 2022—plus Nasdaq’s weaker December hit rate. The case against selling November is 1987 and 2008, when November was the leftover crash month and December was the repair.

> Conflicts noted: December 1931 and 2018 prints differ by series (price vs total return). December win rates disagree by sample: 77% since 1950, 72% for 1990–2025, 66% for 1994–2026 SPY.
>
> Gaps: No official PHLX SOX worst-November/December ranked list. No journal-grade S&P 500 realized-vol table by calendar month that is not an ETF-blog or options paper.

---

## Calendar Anomalies and Market Microstructure

The standard US “Santa Claus rally” is not “December” and is not “after Christmas.” Yale Hirsch coined the term in the 1972 Stock Trader’s Almanac as the last five trading days of December plus the first two trading days of January ([Nippani, Washer, and Johnson, 2015](https://www.financialplanningassociation.org/article/journal/MAR15-yes-virginia-there-santa-claus-rally-statistical-evidence-supports-higher-returns-globally), accessed 2026-09-13, confidence: High). Later Almanac and LPL updates commonly cite about +1.3% since 1950, positive in roughly 78–80% of years, versus a typical seven-session return near +0.3% ([Stock Trader’s Almanac](https://stocktradersalmanac.com/Newsletter/1224.aspx), accessed 2026-09-13, confidence: High); [LPL Research](https://www.lpl.com/research/blog/the-santa-claus-rally-ends-on-the-naughty-list.html) (accessed 2026-09-13, confidence: High). Washer, Nippani, and Johnson (2016) find the rally stronger in small-cap portfolios and identify the three most important days as the last December session and the first two January sessions ([Managerial Finance](https://doi.org/10.1108/MF-10-2015-0280), accessed 2026-09-13, confidence: High).

A cash need on December 31 therefore does not miss the entire Santa Claus window, but it does miss a material, academically flagged piece of it. The holder who stays through year-end captures the five December sessions. The holder does not capture the two January sessions that those papers identify as among the strongest.

Patel (2023) uses S&P 500 and Nasdaq from 2000–2021 and finds Santa-day mean returns economically larger but not statistically significant (S&P dummy +0.080, p = 0.431) ([Patel, Journal of Accounting and Finance](https://doi.org/10.33423/jaf.v23i1.5943), accessed 2026-09-13, confidence: High). SmartAsset notes the 2010–2020 average Santa Claus move was only +0.38% ([SmartAsset](https://smartasset.com/financial-advisor/santa-claus-rally-2020), accessed 2026-09-13, confidence: Medium). Treat 1950–present averages as Established descriptive history, not as a statistically stable post-2000 anomaly.

Hirsch’s “best six months” rule is in the market November 1–April 30. Almanac 2024: Nov–Apr S&P 500 up 77.0% of years, average +7.1% since 1950 ([Almanac](https://www.stocktradersalmanac.com/Alert/20241107.aspx), accessed 2026-09-13, confidence: High). Bouman and Jacobsen (2002) find the Halloween dummy in 36 of 37 countries; the United States monthly dummy is 0.93 percentage points with t = 1.95, and after giving January its own dummy the US t falls to 1.61 ([AER](https://www.aeaweb.org/articles?id=10.1257%2F000282802762024683), accessed 2026-09-13, confidence: High). Neither paper is a late-November versus late-December trading rule. Both months sit inside the historically stronger winter half-year.

Tax-loss selling is a cross-sectional story, not an index-level December weather report. Givoly and Ovadia (1983), Lakonishok and Smidt (1986), Grinblatt and Moskowitz (2004), and Poterba and Weisbenner (2001) document that prior losers are sold in November–December and rebound at the turn of the year ([Poterba and Weisbenner](https://scottweisbenner.web.illinois.edu/RESEARCH/PAPERS/JF_JanuaryEffect_Feb2001_353-368.pdf), accessed 2026-09-13, confidence: High). A semiconductor that is up a lot on the year is not a tax-loss candidate. Academic evidence implies that name faces less tax-loss selling pressure in December; winners’ turnover spikes in January, not December. No sources found for an academic study that isolates US semiconductor indexes as a December seasonal versus the S&P 500.

Window dressing is documented as a motive (Lakonishok, Shleifer, Thaler, and Vishny, 1991) but Hu, McLean, Pontiff, and Wang (2014) find no evidence of window dressing in daily institutional trades ([RFS](https://doi.org/10.1093/rfs/hht057), accessed 2026-09-13, confidence: High). Do not treat window dressing as an established cause of the index-level December rally.

> Conflicts noted: Almanac/LPL treat a ~1.3% / ~79% seven-day edge as real; Patel (2023) finds 2000–2021 excess positive but insignificant. Darrat et al. (2011) found last-two-weeks-of-December outperformance in 11 of 34 countries but not in the US, which conflicts with LPL/NDW US back-half figures. US Halloween t is only 1.95 and loses 10% significance once January is partialled out.
>
> Gaps: No source decomposes the official seven Santa Claus days into average return by day in a complete published table. No sources found for semiconductor-specific December versus S&P 500 sample stats.

---

## Landscape: Sector and Style Differences

The academic and broker literature is much thicker on the six-month Halloween window than on a clean November-versus-December split. Jacobsen and Visaltanachoti (1926–2006) find that 48 of 49 industries earned more in winter than in summer; the gap is large in production sectors and almost absent in Food, Consumer, and Utilities ([The Financial Review, 2009](https://assets.super.so/e46b77e7-ee08-445e-b43f-4ffd88ae0a0e/files/391fe6b4-03bc-4cba-a97a-557f433e833b.pdf), accessed 2026-09-13, confidence: High). CFRA’s Stovall rotation (cyclicals November–April; staples and healthcare May–October) is about that half-year, not a December sell signal ([CNBC](https://www.cnbc.com/2022/10/31/heres-a-way-to-juice-returns-to-play-the-seasonally-strongest-six-months-of-the-year.html), accessed 2026-09-13, confidence: High).

Bank of America, as reported in October 2025, published the longest broker November sector table located (since 1927): consumer discretionary +3.14%, S&P technology +3.1%, industrials +3.02%, healthcare +2.52%, Russell 2000 +2.64%. The published excerpts do not give standalone December sector means ([Business Insider / BofA](https://www.businessinsider.com/where-to-invest-stock-market-sp500-tech-healthcare-industrial-bofa-2025-10), accessed 2026-09-13, confidence: High). CFRA, via Reuters (December 2021), is the longest December sector ranking located (since 1990): utilities were the top December sector at +1.9%; information technology was the weakest at +0.67% ([Reuters / CFRA](https://whbl.com/2021/12/31/defensive-stocks-may-be-ripe-for-reversal-after-stellar-december/), accessed 2026-09-13, confidence: High).

A ChartRow ETF-era table (1999–2026, Medium confidence, computed from public prices) shows November stronger than December in absolute terms for discretionary, technology, healthcare, financials, staples, and energy. Utilities are the exception: November +0.8% versus December +0.9%. Technology’s November-to-December step-down is the largest (XLK +2.7% to +0.4%; December hit rate 56%). Small caps (IWM) November +3.6% versus December +1.1%. Growth (IWF) December +0.4% versus value (IWD) +1.1% ([ChartRow](https://chartrow.com/visuals/seasonality), accessed 2026-09-13, confidence: Medium).

This suggests “sell late November versus hold December” depends on what you hold. The economic case for exiting in late November is strongest in large-cap growth and technology. The case for holding through December is strongest in small caps, and only if the holding period includes the second half of the month. The popular “December = defensives” claim is a relative-leadership statement, not a statement that those sectors earn more in December than in November. December 2024 and December 2025 both failed the defensive-leadership template ([Breckinridge](https://www.breckinridge.com/insights/december-2025-market-commentary), accessed 2026-09-13, confidence: High).

> Conflicts noted: Absolute versus relative December (utilities lead versus the S&P but are not a large absolute December winner). BofA S&P November +1% since 1927 is much lower than ChartRow SPY November +2.6% (1994–2026).
>
> Gaps: No bulge-bracket December sector-average table to pair with BofA’s November 1927–2025 figures. ChartRow IWD/IWF is the only numeric November-versus-December value/growth split.

---

## Landscape: USD/TWD and Dollar Year-End Overlay

For a Taiwan / TWD cash need, the November–December FX overlay is a small, noisy, and only weakly documented add-on. TickerLeague’s long-run USD/TWD heatmap (TWD per USD) puts November at about −0.2% and December at about −0.3% ([TickerLeague](https://tickerleague.com/forex/usdtwd/seasonality), accessed 2026-09-13, confidence: Medium). Wang Yen-Neng’s 2022 NCCU thesis covering 1989–2021 reports TWD depreciation in May, July, and August; November and December are not among the months flagged as significant ([Airiti](https://www.airitilibrary.com/Publication/alDetailedMesh?docid=U0004-G0107932145), accessed 2026-09-13, confidence: High).

The CBC treats “seasonal factors” as a trigger for smoothing, not as a published calendar ([CBC, Foreign Exchange Management 2024](https://www.cbc.gov.tw/dl-215904-c9e0617865d84ecf887d70d7f9cf8b67.html), accessed 2026-09-13, confidence: High). DXY, by contrast, has a long December-softness record: Seasonax’s 50-year study finds the index down in 34 of 50 years, averaging just under −1% ([Seasonax](https://www.seasonax.com/forex-seasonality-the-us-dollar-drop-at-the-end-of-the-year/), accessed 2026-09-13, confidence: High). That G10 pattern is only partially transmitted into USD/TWD after CBC intervention.

This suggests converting already-realized USD proceeds in late December has historically been a small TWD-cash negative versus converting in late November if the NT dollar tracks a soft G10 dollar. That FX haircut is an order of magnitude smaller than typical December equity or single-year USD/TWD swings, and it can reverse under dollar-smile fear-mode ([Eurizon SLJ](https://www.eurizonsljcapital.com/dollar-smile/), accessed 2026-09-13, confidence: High).

> Conflicts noted: Long-run commercial USD/TWD averages conflict with the last five complete years, in which November was much weaker than December. December 2024 DXY strength conflicts with the long-run December-weakness average.
>
> Gaps: No official CBC table of November versus December USD/TWD average changes. No peer-reviewed paper that isolates late-November versus late-December conversion of US-equity proceeds into TWD.

---

## Landscape: Holiday Liquidity and Forced-Sale Risk

US equity liquidity compresses in two known windows: a short Thanksgiving half-day, then a multi-session late-December drought. NYSE and Nasdaq close early at 1:00 p.m. ET the Friday after Thanksgiving and, in 2026, on Thursday, December 24. December 31 is a full session ([NYSE Holidays](https://www.nyse.com/markets/hours-calendars), accessed 2026-09-13, confidence: High).

Russell Investments: US equity volume typically runs about 80% of normal the day before Thanksgiving and about 45% of normal the day after; global equities run 45–70% of normal from December 23 through New Year’s Day ([Russell Investments](https://russellinvestments.com/content/ri/uk/en-gb/insights/russell-research/2025/11/holiday-trading-effect.html), accessed 2026-09-13, confidence: High). Reuters reported Christmas Eve 2025 volume of 7.61 billion shares versus a 16.21 billion 20-session average (~47%) ([Reuters](https://www.reuters.com/business/futures-dip-shortened-christmas-eve-trading-2025-12-24/), accessed 2026-09-13, confidence: High). Russell’s execution advice is to finish large events in the first half of December or the second week of January.

The Almanac’s last-day Nasdaq fact is real: “On the last trading day of the year, NASDAQ has been down in nineteen of the last twenty-five years after having been up twenty-nine years in a row from 1971 to 1999” ([Almanac](https://www.stocktradersalmanac.com/Alert/20251113_1.aspx), accessed 2026-09-13, confidence: High). Quantifiable Edges independently documented the 1971–1999 streak and then 15 declines in the next 18 years through 2018 ([Quantifiable Edges](https://quantifiableedges.com/last-day-of-the-year-history-and-why-traders-need-an-open-mind-adaptability/), accessed 2026-09-13, confidence: High).

SOXX is liquid in normal conditions (~7.0 million 30-day average volume, 0.02% median spread as of 11 September 2026) ([iShares SOXX](https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf), accessed 2026-09-13, confidence: High). Yahoo daily volume for SOXX in 2025: Christmas Eve 1.72 million, December 26 1.86 million, December 31 2.95 million, versus ~5.8 million average in December 1–19 ([Yahoo Finance](https://finance.yahoo.com/quote/SOXX/history/), accessed 2026-09-13, confidence: High). Christmas Eve SOXX volume was about 30% of that fund’s own mid-December average—thinner than the all-exchange tape.

Under T+1 (effective 28 May 2024), a December 31 trade does not put spendable cash in the account that same day. A holder who needs withdrawn cash on 31 December 2026 has a last regular-way sale date of Wednesday, 30 December 2026, not the 31st close.

> Conflicts noted: Russell’s Dec. 23–New Year band (45–70% of normal) is milder than NYSE-only Christmas Eve prints (~one-third). Christmas Eve is historically up on price and dead on volume; last-day-of-year Nasdaq is historically down on price.
>
> Gaps: No multi-decade average of December 31 ADV as a percent of annual ADV. No quantified market-impact study of forced SOXX sales in the Dec. 23–31 window. Almanac last-day Nasdaq frequency is well sourced; average last-day return magnitude was not in the free pages.

---

## Deep Dive: Exception Years and 2026 Context

The November–December “hold through year-end” pattern is a Signal (historical frequency), not a Forecast. Using SPY month-end total returns, ChartRow’s 1994–2025 table shows eight years in which November was positive and December was negative. The four with a strong November (about +5% or more) are 1996 (+7.3% / −2.4%), 2002 (+6.2% / −5.7%), 2022 (+5.6% / −5.8%), and 2024 (+6.0% / −2.4%) ([ChartRow](https://chartrow.com/visuals/seasonality), accessed 2026-09-13, confidence: Medium). Official confirmation for 2024: S&P Dow Jones Indices November +5.73% price / +5.87% with dividends ([S&P DJI](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202411.pdf), accessed 2026-09-13, confidence: High); December 2024 S&P total return −2.38% ([Gateway](https://www.gia.com/december-2024-market-recap/), accessed 2026-09-13, confidence: High). 2018 is the textbook modest-November / crash-December: +1.9% / −8.8%.

Counterexamples: 2023 November +9.1% / December +4.6%; 2020 +10.9% / +3.7%; 1998 +5.6% / +6.5% ([ChartRow](https://chartrow.com/visuals/seasonality), accessed 2026-09-13, confidence: Medium). A strong November does not mechanically fail.

Calendar terminology: in Almanac usage, 2025 was the post-election year; **2026 is a midterm year**. Treating 2026 as a post-election December is a category error ([Almanac](https://www.stocktradersalmanac.com/Alert/20251113_1.aspx), accessed 2026-09-13, confidence: High). In the last 18 midterm years, December ranked #3 S&P 500 (+1.2%) and #7 Nasdaq (−0.3% since 1974); Russell 2000 midterm Decembers since 1982 averaged only +0.3% ([Almanac](https://www.stocktradersalmanac.com/Alert/20221117_1.aspx), accessed 2026-09-13, confidence: High).

Late-2025 house forecasts (LPL 7,300–7,400; CFRA 7,400) are already below the 10 September 2026 S&P close of 7,591.75 ([Reuters](https://www.reuters.com/business/sp-500-dow-futures-attempt-recovery-ahead-inflation-report-2026-09-10/), accessed 2026-09-13, confidence: High). LPL’s December 2025 easing assumption is in tension with the September 2026 rates tape (hike odds, multi-year-high yields). Those are Forecasts, not a December 2026 Signal. The closest historical rhymes among exception years are 2024 (strong November, then a December fade on the Fed path) and 2018 (December collapse after a policy-rate shock). Those are analogies, not probabilities.

> Conflicts noted: Price vs total return vs average-price series. Santa Claus Rally vs calendar December (failed seven-day windows in 2024–26 are not the same as failed calendar Decembers). Almanac post-election December averages are vintage-dependent.
>
> Gaps: No CFRA table of post-election-year December S&P returns. No dedicated Nasdaq/SOXX month-by-month exception list for the same Nov/Dec breaks. No LPL/CFRA forecast dated after May 2026 that updates 7,300–7,400 for the September 2026 tape.

---

## Deep Dive: A Year-End Cash-Need Decision

This is historical decision analysis for a holder who must convert equity to cash by December 31, not a perpetual investor who can ride January. The hard constraint changes the usual “stay invested” story in three ways. First, the Santa Claus window includes two January sessions the deadline forgoes. Second, a sale of a winner in November or December realizes the gain in the same tax year. Third, under T+1, a December 31 trade does not put spendable cash in the account that same day.

Skipping December historically gave up on the order of 1.4–1.7% of S&P mean and a 74–77% monthly win rate, with Dorsey Wright’s 25th-percentile floor still +0.2% ([Nasdaq Dorsey Wright](https://dorseywright.nasdaq.com/research/bigwire/2025/12/01/12-01-2025/december-return-tendencies-strong-month-ahead), accessed 2026-09-13, confidence: High). After a positive November, LPL has December averaging only 0.83%, versus 2.78% after a negative November ([LPL via Cingari](https://www.foxbusiness.com/markets), accessed 2026-09-13, confidence: Medium — figure from LPL via 2 Dec 2023 commentary). A mid-December exit historically captured the weak half (~0.1% to a slight loss; 50–60% win rate) and surrendered the strong half (~+1.5% to +1.7%; 78–80% win rate) ([Schaeffer’s](https://www.schaeffersresearch.com/), accessed 2026-09-13, confidence: Medium); [LPL, 2024](https://advisoranalyst.com/2024/12/04/is-the-santa-claus-rally-still-coming-to-town.html/) (accessed 2026-09-13, confidence: High).

Chen and Singal (2003) isolate winners over 1988–2000: about +2.2% in the last five December days excluding the last trading day of the year, then −0.9% in the first five January days, attributed to postponed tax-gain selling ([FAJ](https://doi.org/10.2469/faj.v59.n4.2548), accessed 2026-09-13, confidence: High). A cash-need holder of a winner cannot take the January deferral.

Framed only as what the published record implied on average:

Sell ~30 November forgoes one historically strong month. Execution and settlement are the cleanest. Tax on a winner is the same as later 2026 sales.

Sell mid-December, before the Christmas thin tape, sat on the wrong side of the half-month split. Versus late November, the incremental published mean is small. Versus year-end, this is where most of the December Signal is surrendered.

Hold toward 31 December (in practice 30 December if cash must settle that day) is the action the seasonal Signal favors on expected return for a broad index. It is the only one that historically collected the strongest half-month of the year. It does not collect the two January Santa days, takes the most implementation risk, and still faces a −9% December (2018). For Nasdaq/SOXX the same ranking is weaker because December’s recent mean and hit rate are poorer.

> Conflicts noted: Almanac December means disagree slightly by vintage (+1.4% vs +1.6% vs Dorsey Wright +1.7%). LPL’s last-five-year sample contradicts long-sample second-half dominance. Almanac last-day-of-year bearishness conflicts with “hold through the close on the 31st.” Tax-year (trade date) conflicts with cash-in-hand (T+1).
>
> Gaps: No standard published split of the 1.3% Santa mean into last-five-December-days-only versus first-two-January-days-only with a current sample. No broker series that marks 30 Nov, ~18–22 Dec, and 30/31 Dec on one total-return index.

---

## Deep Dive: Is the Seasonal Edge Statistically Real?

The academic record does not support treating a US “hold into late December versus sell by late November” premium as a statistically reliable, after-cost, post-publication fact.

Bouman and Jacobsen (2002) find the winter dummy positive in 36 of 37 countries, but the United States is the weak case: 0.93 percent per month with t = 1.95. When they add a January dummy, the US Halloween t falls to 1.61. Their own 1973–1996 US trading-rule appendix produced 11.61% a year versus 11.37% for buy-and-hold; Jensen’s alpha t is 1.10 ([AER](https://www.aeaweb.org/articles?id=10.1257/000282802762024683), accessed 2026-09-13, confidence: High). Maberly and Pierce (2004) show that inserting dummies for October 1987 and August 1998 knocks the US winter coefficient to insignificance, and that the Halloween dummy is insignificant in S&P 500 futures in every specification they run ([Econ Journal Watch](https://econjwatch.org/articles/stock-market-efficiency-withstands-another-challenge-solving-the-sell-in-may-buy-after-halloween-puzzle), accessed 2026-09-13, confidence: High).

Sullivan, Timmermann, and White (2001) apply White’s Reality Check to 9,452 calendar trading rules on a century of DJIA data. Isolated rules look spectacular; the Reality Check p-value on the best rule is 0.20 in-sample and above 0.93 out of sample ([Journal of Econometrics](https://doi.org/10.1016/S0304-4076(01)00077-X), accessed 2026-09-13, confidence: High). Harvey, Liu, and Zhu argue that a newly claimed predictor should clear a t of about 3.0; the US Halloween t of 1.95 does not approach that bar ([NBER w20592](https://www.nber.org/papers/w20592), accessed 2026-09-13, confidence: High).

Dichtl and Drobetz find that once each market is dated from the introduction of a liquid fund that actually lets an investor implement the switch, the Halloween effect “decreased or virtually vanished,” and Hansen’s Superior Predictive Ability test implies Sell-in-May never offered statistically significant outperformance versus buy-and-hold ([Finance Research Letters](https://doi.org/10.1016/j.frl.2013.10.001), accessed 2026-09-13, confidence: High). Schwert and Marquering, Nisser, and Valla document that published calendar anomalies disappear, reverse, or attenuate after publication ([Schwert](https://www.billschwert.com/hbfech15.pdf), accessed 2026-09-13, confidence: High); [Applied Financial Economics](https://doi.org/10.1080/09603100500400361) (accessed 2026-09-13, confidence: High). Patel (2023) concludes the Santa Claus Rally “does not exist” in US stock returns over 2000–2021 on frequentist tests ([JAF](https://doi.org/10.33423/jaf.v23i1.5943), accessed 2026-09-13, confidence: High).

Lakonishok and Smidt (1988) relocate the interesting mass to a few days around month-end and year-end, not to a six-week “November is special, December is optional” rule ([RFS](https://doi.org/10.1093/rfs/1.4.403), accessed 2026-09-13, confidence: High). Jacobsen and Zhang (2021) and Andrade, Chhaochharia, and Fuerst (2013) still find a global half-year Halloween dummy out of sample; that is about November–April versus May–October, not about exiting before December, and it sits in unresolved conflict with Dichtl and Drobetz.

The statistical verdict for this axis is therefore negative. After costs, after data-mining corrections, and after post-publication samples, US November/December outperformance is not a result one should treat as an established trading edge. Descriptive history (December is usually up; November is usually a bit larger in postwar means) can still inform a cash-need timeline without being a timed alpha claim.

> Conflicts noted: Jacobsen and co-authors plus Haggard and Witte argue Halloween is real and robust; Maberly and Pierce, Lucey and Zhao, and Dichtl and Drobetz argue the US effect is outliers, January in disguise, or insignificant once implementable. Washer/Nippani/Johnson find a long-sample Santa effect; Patel finds a 2000–2021 US null.
>
> Gaps: No primary paper runs a pre-registered, snooping-adjusted test of the exact decision “sell by late November versus hold through late December” on US large-cap total returns, net of costs and taxes, with a holdout sample after 2002.

---

## Key Findings

According to the Almanac, LPL, and Nasdaq Dorsey Wright, postwar S&P 500 November averages about 1.7–1.8% and December about 1.4–1.7%, with December’s win rate the highest of any month at about 73–77% ([Almanac](https://www.stocktradersalmanac.com/Alert/20251113_1.aspx); [LPL](https://advisoranalyst.com/2024/12/04/is-the-santa-claus-rally-still-coming-to-town.html/); [Dorsey Wright](https://dorseywright.nasdaq.com/research/bigwire/2025/12/01/12-01-2025/december-return-tendencies-strong-month-ahead), accessed 2026-09-13, confidence: High). Yardeni 1928–2023 and CRSP 1926–2006 reverse the mean ranking in favor of December ([Yardeni](https://archive.yardeni.com/pub/stmktreturns.pdf); [Ciccone and Etebari](https://scholars.unh.edu/cgi/viewcontent.cgi?article=1022&context=account_facpub), accessed 2026-09-13, confidence: High). This suggests both months are historically strong; the “November is better” claim is sample-dependent and should not be treated as a single number.

According to official Nasdaq factsheets and Almanac recaps, November has been the stronger month for Nasdaq, technology, and spliced SOXX samples, while the last 10–20 years have been much harsher for Nasdaq-100 December—including official Composite prints of −9.48% in December 2018 and −8.73% in December 2022 ([Nasdaq Composite factsheet](https://indexes.nasdaqomx.com/docs/FS_COMP.pdf); [CNBC](https://www.cnbc.com/2023/10/31/something-for-the-bulls-november-is-typically-the-best-month-for-the-stock-market.html), accessed 2026-09-13, confidence: High). This suggests a semiconductor holder faces a weaker historical case for “always hold December” than a broad S&P holder.

According to Yardeni, Dorsey Wright, and Morningstar, December is usually the quieter, higher-floor month, but December 2018’s −9.03% total return is the modern left-tail warning, and 2022 fully offset a strong November ([Yardeni](https://archive.yardeni.com/pub/stmktreturns.pdf); [Morningstar](https://www.morningstar.com/columns/rekenthaler-report/how-rare-was-decembers-stock-market-loss), accessed 2026-09-13, confidence: High). This suggests average-return seasonality and path risk do not point the same way.

According to Hirsch, Nippani/Washer/Johnson, LPL, and Dorsey Wright, December’s average is back-loaded and the official Santa Claus window includes two January days that a December 31 cash need misses ([Almanac](https://stocktradersalmanac.com/Newsletter/1224.aspx); [Nippani et al.](https://www.financialplanningassociation.org/article/journal/MAR15-yes-virginia-there-santa-claus-rally-statistical-evidence-supports-higher-returns-globally); [Dorsey Wright](https://dorseywright.nasdaq.com/research/bigwire/2025/12/01/12-01-2025/december-return-tendencies-strong-month-ahead), accessed 2026-09-13, confidence: High). Tax-loss selling, meanwhile, is a loser-stock story; a winning semiconductor is not the name being dumped for losses ([Poterba and Weisbenner](https://scottweisbenner.web.illinois.edu/RESEARCH/PAPERS/JF_JanuaryEffect_Feb2001_353-368.pdf), accessed 2026-09-13, confidence: High).

According to Bouman and Jacobsen, Sullivan/Timmermann/White, Maberly and Pierce, Dichtl and Drobetz, and Patel (2023), the US Halloween dummy is barely significant, fails several robustness cuts, and the 2000–2021 Santa Claus window is statistically indistinguishable from noise ([AER](https://www.aeaweb.org/articles?id=10.1257/000282802762024683); [Patel](https://doi.org/10.33423/jaf.v23i1.5943), accessed 2026-09-13, confidence: High). This suggests the history is useful as a timeline and risk map, not as a timed alpha strategy.

---

## Strategic Recommendations

1. **Do not treat “hold to late December” as a statistically proven edge.** — The US winter dummy was already t = 1.95 in the discovery sample and fails several later tests. Evidence: [Bouman and Jacobsen](https://www.aeaweb.org/articles?id=10.1257/000282802762024683); [Patel 2023](https://doi.org/10.33423/jaf.v23i1.5943). If a recommendation rests on Almanac means alone, say so: those are descriptive history, confidence High for the published averages, Low as a 2026 forecast.

2. **If the holding is Nasdaq / SOXX and cash is due 31 December, history does not reward waiting the extra month the way a broad S&P story does.** — November has been the fatter tech month; recent Nasdaq-100 Decembers have been near zero or negative; 2018 and 2022 were air-pockets after positive or strong Novembers. Evidence: [Nasdaq factsheets](https://indexes.nasdaqomx.com/docs/FS_COMP.pdf); [tastylive](https://www.tastylive.com/news-insights/december-market-trends-stocks-gold-typically-perform-year-end). This is the recommendation that matches a semiconductor cash-need, confidence Medium (official exception years High; long-run SOXX averages Low-tier).

3. **If the holding is broad US large-cap and the owner can tolerate a 2018-style month, the long-sample Signal still slightly favors collecting December’s second half rather than selling on 30 November.** — December’s hit rate and 25th-percentile floor are the best of any month; almost all of the average sits after the 11th trading day. Evidence: [Dorsey Wright](https://dorseywright.nasdaq.com/research/bigwire/2025/12/01/12-01-2025/december-return-tendencies-strong-month-ahead); [LPL](https://advisoranalyst.com/2024/12/04/is-the-santa-claus-rally-still-coming-to-town.html/). Do not sell in mid-December thinking that captures “half the month.”

4. **Do not plan a large SOXX sale in the Christmas-to-New-Year tape.** — Volume can fall to ~30% of that fund’s own mid-December average; last-day Nasdaq has been down in 19 of the last 25 years; T+1 means a 31 December trade is not same-day cash. Evidence: [Yahoo SOXX history](https://finance.yahoo.com/quote/SOXX/history/); [Almanac](https://www.stocktradersalmanac.com/Alert/20251113_1.aspx); [Russell](https://russellinvestments.com/content/ri/uk/en-gb/insights/russell-research/2025/11/holiday-trading-effect.html). Practical window: late November through about 18–22 December, or wait until the second week of January if the cash date can move.

5. **Ignore USD/TWD seasonality as a timing input.** — No academic Nov/Dec effect; published averages are tenths of a percent; CBC smoothing and FINI flows dominate. Evidence: [Wang thesis](https://www.airitilibrary.com/Publication/alDetailedMesh?docid=U0004-G0107932145); [CBC](https://www.cbc.gov.tw/dl-215904-c9e0617865d84ecf887d70d7f9cf8b67.html). Convert when the equity sale is done, not to catch a December dollar dip.

---

## Risks and Uncertainties

- Data gaps: no official S&P DJI November/December total-return table; no CRSP update after 2006; no peer-reviewed Nasdaq/SOXX November-versus-December test; no published split of the Santa Claus +1.3% into December-only versus January-only with a current sample; no multi-decade December 31 ADV series.
- Low-confidence claims: ChartRow/SeasOptima/Forecaster seasonality sites; SOXX long-run monthly averages; the 32% “December follows a positive November with a loss” frequency; ChartRow IWD/IWF value-versus-growth split.
- Unresolved conflicts: whether November or December has the higher long-run S&P mean; whether December 2018 is −8.8% or about −9% to −10% depending on series; whether Halloween remains real globally after SPA tests; whether 2023’s Santa Claus window was up or down across secondary recaps.
- Domain risks: 2026 is a midterm year, not a post-election December; late-2025 easing forecasts conflict with the September 2026 hike-odds tape; SOXX has a 3-for-1 split scheduled after 4 November 2026, which does not change percentage returns if adjusted but will change share counts and option strikes; a single-name or single-ETF sale in a thin tape can gap independently of index seasonality.

---

## Next Steps

- If the cash date is firm, pick an execution window (late November, or first half of December ending before 24 December) rather than a seasonal bet.
- If the holding is SOXX, pull the broker’s own month-end total-return series from 2001–2025 for November versus December as a one-hour check on the Low-tier vendor averages.
- Re-read LPL/CFRA 2026 outlooks after the next FOMC; the late-2025 7,300–7,400 year-end targets are already stale versus the 10 September 2026 close.
- Optional: export this report to PDF if needed (`pandoc` or `md-to-pdf`).
- This research enables a timeline choice (when to sell a cash-need US equity position). It does not enable a signed 2026 December return call.
