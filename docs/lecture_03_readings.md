# Lecture 3 — readings, sources and teaching routes

Updated 16 October 2026. These sources support original explanations, calculations and editable plots. The private reference-course links and downloaded books/decks are kept outside the public repository.

## Finance courses and textbook

| Reference inspected | Relevant sections | Use in Lecture 3 |
|---|---|---|
| Christian Skov Jensen, *Financial Economics*, Spring 2023 | Part 2: time value; Part 14: arbitrage; Part 15A, pp. 6–14: bonds, YTM and realized returns; Part 15B: term structure and forwards; Part 16, pp. 3–13: risk management, duration, immunization and convexity | Begin with replication and dated payments; distinguish returns from yields; develop a risk-sized position |
| Matthias Rodemeier, *Financial Markets and Institutions*, Fall 2022, course 30006 | Lecture 3, pp. 3–27 and 35–50: interest, valuation, zeros, YTM and price sensitivity; Lecture 4, pp. 10–16: bills, auctions and quotation conventions; formula sheet | Auction mechanism and valuation intuition. Historical institutional facts and market examples are refreshed from official sources |
| Zvi Bodie, Alex Kane and Alan J. Marcus, *Investments*, 11th edition, McGraw-Hill Education, 2018 | Ch. 14, pp. 432–448: prices, yields and returns; ch. 15, pp. 467–486: term structure, forwards and expectations; ch. 16, pp. 496–508: duration and convexity, followed by bond-portfolio management | Main fixed-income companion; alternative explanations and deeper algebra |
| Paul Krugman, Maurice Obstfeld and Marc Melitz, *International Economics: Theory and Policy*, 12th Global Edition | Ch. 14, printed pp. 390–411 in the supplied copy | Asset-return comparisons and international-finance bridge; see the [course-wide edition map](source_map.md) |
| John H. Cochrane, *Asset Pricing*, revised edition, ch. 1; [official teaching page](https://www.johnhcochrane.com/35904-asset-pricing) | Prices as expected discounted state-contingent payments | Optional original two-state example and stochastic discount factor |

The course PDFs informed the mechanisms and sequencing. Their figures, slide text and book pages are not reproduced. The auction order book, bond amounts, rates, state payoffs and hedge maturities in the teaching examples are original constructions. The supplied newspaper chart is the explicitly credited exception described below.

## Current primary sources and frozen inputs

All inputs were retrieved on 16 October 2026. Observation dates differ deliberately and remain visible on slides. The build works offline from the frozen tables.

| Chart or example | Source and exact snapshot | Delivered input |
|---|---|---|
| US par curve and front-end zoom, slides 29–30 | [US Treasury daily par/CMT table](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610), 15 Oct 2026, all 14 published tenors | [Curve CSV](../data/lecture_03_yield_curves_2026-10-16.csv) |
| EUR AAA par curve, slide 31 | [ECB monthly maturity grid](https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.?startPeriod=2026-10-14&endPeriod=2026-10-15&format=csvdata), latest verified observation 14 Oct, 358 fitted maturities from 3 months to 30 years; [methodology](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html) | Same curve CSV |
| Common-date zero curves, slide 32 | 9 Oct 2026: [Federal Reserve Gürkaynak–Sack–Wright data](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv), [methods](https://www.federalreserve.gov/data/nominal-yield-curve.htm); [ECB zero grid](https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.?startPeriod=2026-10-09&endPeriod=2026-10-09&format=csvdata). Each curve has 349 monthly maturity points from 1 to 30 years; 30 annual US source points are also preserved | Same curve CSV, 1,100 rows across all series |
| Actual bill auction, slides 24–25 | [TreasuryDirect four-week result release](https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20261015_2.pdf), 15 Oct; issue 20 Oct, maturity 17 Nov; [API](https://www.treasurydirect.gov/TA_WS/securities/search?format=json&type=Bill&auctionDate=2026-10-15) | [Auction CSV](../data/lecture_03_auction_results_2026-10.csv), four securities including the eight-week bill |
| Note and bond reopenings, slide 79 | TreasuryDirect results for [7 Oct](https://www.treasurydirect.gov/TA_WS/securities/search?format=json&auctionDate=2026-10-07) and [8 Oct](https://www.treasurydirect.gov/TA_WS/securities/search?format=json&auctionDate=2026-10-08) | Same auction CSV |
| Bills and auction rules, slides 18–23 | [Bill terms and denominations](https://www.treasurydirect.gov/marketable-securities/treasury-bills/), [auction process](https://www.treasurydirect.gov/auctions/how-auctions-work/), checked 16 Oct | Dated explanatory notes; invented auction separated from observed results |
| ACM decomposition, slides 52–53 | [New York Fed term-premium model](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs), [published chart data](https://www.newyorkfed.org/medialibrary/media/research/data_indicators/acmPlot_data.csv), 81 monthly observations Jan 2020–Sep 2026 | [ACM CSV](../data/lecture_03_acm_decomposition.csv) |
| June dots, slides 54–56 | [Fed SEP, 17 June 2026](https://www.federalreserve.gov/monetarypolicy/files/fomcprojtabl20260617.pdf), Table 1 (PDF p. 2), Figure 2 (PDF p. 4) | [71 individual dots](../data/lecture_03_fed_dots_june2026.csv); supplied Yahoo Finance image plus editable data-based replot |

**Curve interpretation.** Monthly fitted points are outputs of a smooth model, not hundreds of independent executable quotes. The Fed fit is based on selected off-the-run coupon securities, excluding bills, FRNs, on-the-run and first-off-the-run issues. The ECB panel uses a selected AAA government-bond sample, not every euro-area sovereign. For the common-date zero comparison only, continuous yields z are converted to annual-effective i = exp(z) − 1. Source-native par quotes are kept separate. Currency, credit, liquidity, local observation times and fitting samples differ; the US/EUR yield gap is not a hedged trading return.

**Decomposition interpretation.** The expected-short-rate-plus-premium equation is a model-based approximation under matched rate conventions, not an accounting identity. The ACM component shown as “modeled path” is the model's risk-neutral yield/path component, calculated as fitted yield less estimated term premium. It is not an independently observed survey average. At 30 Sep the fitted yield is 5.258961%, estimated premium 0.885008%, and remaining component 4.373953%. The GSW yield, 5.283562%, is a different fit and is not substituted into that model sum.

**Dot-plot credit.** The user supplied a Yahoo Finance graphic that incorrectly attributes the data to the US Bureau of Labor Statistics. The slide caption identifies the Federal Reserve as the source. Its distribution was checked against the official June SEP; the supplied image itself is unchanged. Official rounded medians are 3.8%, 3.6%, 3.4%, 3.1%. June is a historical communication example, not the latest October outlook. Anonymous policy assessments are neither probability-weighted forecasts nor market forward contracts.

**Auction interpretation.** Public offering, additional awards, competitive bids and total accepted need not share one denominator. Use Treasury's reported bid-to-cover; do not divide totals that include additional SOMA awards indiscriminately. Bill discount rates, short-bill simple investment rates, coupon rates and annual-effective yields are different quotes. A tail requires a matched when-issued yield at the deadline; slide 80 supplies an invented benchmark rather than claiming an observed October tail.

## Newspaper discussion via MIT

1. Telis Demos, **[Choosing the Right Bond Strategy for Today’s High-Yield World](https://www.wsj.com/finance/investing/choosing-the-right-bond-strategy-for-todays-high-yield-world-0c4b6a78)**, *Wall Street Journal*, 8 October 2026. Slide 77 asks whether the investor needs dated income or is making a resale-price forecast. Only the accessible opening was used; the classroom exercise is original.
2. Harriet Clarfelt and Kate Duguid, **[Investors brave US Treasury rout to lock in highest yields in decades](https://www.ft.com/content/6fa735a2-a590-4461-b092-920ba489e7a8)**, *Financial Times*, 13 October 2026. The headline/opening was verified through the [FT's syndicated Yahoo Finance version](https://finance.yahoo.com/markets/currencies/articles/investors-brave-us-treasury-rout-040028283.html). Slide 78 separates entry yield, holding horizon and further price losses. Full FT access was not confirmed.

MIT provides [WSJ access instructions](https://libguides.mit.edu/news/wsj) and [FT access instructions](https://libguides.mit.edu/news/ft). WSJ uses an MIT-email subscription account; FT uses the institution's account/SSO workflow. No account was created and no MIT authentication was completed during preparation. Read the full articles through your own subscription before expanding the discussion. No paid full text or article screenshot is distributed.

## Six 25–30-minute routes

| Meeting | Slides | Time and question |
|---|---|---|
| 1. Prices versus returns | 4–8 (8 min), 9–14 (13 min), 15–16 (5 min) | Can a bond yielding 5% lose money in one year? |
| 2. Bills and auctions | 18–20 (7 min), 21–23 (9 min), 24–26 (10 min) | Who gets filled, at what price, and what does the quoted rate mean? |
| 3. Curves and replication | 28–33 (8 min), 34–39 (11 min), 40–42 (8 min) | Which future lending return can two zeros lock in? |
| 4. Expectations and premia | 44–46 (7 min), 47–53 (12 min), 54–58 (9 min) | Can a policy cut coexist with rising long yields? |
| 5. Bond risk | 60–64 (9 min), 65–69 (10 min), 70–74 (9 min) | How do first and second derivatives translate a rate view into money? |
| 6. Cases and a curve trade | 77–80 (8 min), 81–85 (11 min), 86–89 (8 min) | What does a DV01-matched steepener gain or lose under competing scenarios? |

Slide 75 is an additional horizon discussion. Slides 91–96 are an optional mathematical meeting: general forwards, compounding, par coupons, state prices and liability immunization. Slide 98 points to these readings. Timing assumes pauses for sign predictions and calculations; trim the route rather than rushing through it.
