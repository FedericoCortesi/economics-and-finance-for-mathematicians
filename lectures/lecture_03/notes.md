# Lecture 3 — Bonds and yield curves

Pricing cash flows, measuring risk and reading market expectations

## Delivery

This expanded module is designed for several short meetings. Use the routes in `../../syllabus.md`. Model paths and unlabelled numbers are original hypothetical examples. Keep the observation date and quote convention visible when reading empirical charts. The source textbooks and course decks inform the explanations; their pages and proprietary figures are not redistributed.

## Slide 1 — Bonds and yield curves

The opening illustration shows an invented investor exchanging capital for a claim, a workshop using productive machinery, and envelopes symbolizing future payments. The smaller envelopes suggest coupons and the larger final envelope suggests principal repayment; neither their number nor size specifies a pricing example. The picture introduces the distinction between real productive activity and the dated financial claim. It is an original AI-generated illustration, not evidence about a real issuer.

Illustration: generated 16 October 2026 with the built-in OpenAI image-generation tool. Asset: `../../assets/bond_workshop.png`. Full prompt: `../../docs/image_prompts.md`.

The finance perspective starts with a claim to dated cash flows and the price of replicating that claim. This lecture then distinguishes a promised yield from an investment return, a forward price from a forecast, and a rate view from a sized trade. The expanded module can be split into short meetings. Retain i for nominal rates, r for real rates and bar i for the policy target from Lecture 2.

## Slide 2 — Today’s route

Treat the sections as modular, rather than rushing all slides into one talk. Start each example by asking for a sign prediction, then calculate. The optional final block introduces state prices and compounding conventions. A detailed 25–30-minute route is in the syllabus.

## Slide 3 — Cash flows and prices

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 4 — A bond is a dated payment contract

This invented three-year bond pays annual coupons of 4 and principal of 100 at maturity. Define F as face value, c as the coupon rate and C as the coupon amount. A quoted price is the amount exchanged today for this contract. The coupon rate is written into the contract; the market yield adjusts as prices change. Ignore default, taxes, transaction costs and accrued interest for the initial examples.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 5 — Prices and cash-flow symbols

Use lower-case p for an asset price, leaving P for the aggregate price level from Lecture 2. T is remaining time, measured in years, not a calendar year label. The time argument t is omitted when there is no risk of confusion. A discount factor is a price per unit payment, so it has no face-value scale. We will use F exclusively for face value here and lower-case f for an interest-rate forward.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 6 — Rate symbols and horizons

These conventions extend Lecture 2: i is nominal, r is real and bar i is the policy target. Spot and forward rates specify the interval being priced; a YTM is the internal rate of return of the promised coupon schedule. Do not write f as F, since F is face value. The mathematical examples use annual effective compounding. Empirical par quotes retain their source conventions, and fitted continuous zero rates are converted explicitly when plotted as annual effective rates.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md. Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 7 — A zero-coupon bond

A zero pays only face value at maturity. A two-year buyer pays 90.70295 now for 100 in two years, under the stated annual compounding convention. The 5% return compounds for two years; it is not a total return of 5%. The same relation can be inverted to obtain the spot rate from the zero’s price. Treasury bills are short zero-coupon instruments; ordinary Treasury notes and bonds usually pay coupons.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md. [TreasuryDirect, bills](https://www.treasurydirect.gov/marketable-securities/treasury-bills/).

## Slide 8 — A discount factor prices one future unit

The first equation is the unit price of a certain payment at one date. The second adds the prices of the dated units needed to reproduce every cash flow. For known default-free cash flows, this is the natural no-arbitrage pricing relation. Different dates can have different spot rates. For risky payments, simply discounting expected cash flows with the Treasury zero curve generally misses risk pricing; the optional state-price block explains why.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md. Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 9 — Replication gives the pricing intuition

Jensen’s arbitrage section motivates replication before valuation formulas. If a coupon bond is more expensive than a portfolio reproducing every payment, buy the replicating portfolio and sell the expensive claim. If it is cheaper, reverse the positions. This ideal argument assumes executable borrowing and shorting, consistent collateral and negligible costs. In practice bid–ask spreads and financing create bounds, so an apparent price gap is not automatically a risk-free profit.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 10 — A coupon bond is a basket of zeros

Each zero unit pays one currency unit, not one whole 100-face bond. The three positions reproduce the original bond exactly. The bond’s final payment includes its last coupon plus principal. This is why coupon bonds and zero-coupon curves are linked. Real Treasury STRIPS separate eligible principal and coupon claims, though tax and liquidity differences can matter. No-arbitrage prices the schedule before we introduce a single summary YTM.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md. Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 11 — Worked price with a flat curve

The exact value is 97.27675197 per 100 face. Here every annual spot rate equals 5%, so the flat-curve valuation also equals a YTM calculation at 5%. The below-par price compensates for coupons that are lower than the required rate. The nominal face value does not change when the market price changes. Ask whether a 6% coupon under the same yield would trade above or below 100.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 12 — Market price determines yield to maturity

YTM is the internal rate of return solving this equation. With positive future cash flows and i greater than −1, price is strictly decreasing in i, giving a unique yield for a positive price in the usual range. A flat spot curve makes YTM equal the common spot rate; otherwise it is only a bond-specific summary. It is not the coupon rate and does not give a guaranteed one-year investment return. Real quotation conventions may use semiannual bond-equivalent yields.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 13 — Coupon, yield and return

The return expression assumes a one-year horizon with one coupon paid at its end. If there are intervening coupons, account for their reinvestment or measure the value of all cash flows at the horizon. H is a nominal investment return, while r remains a real rate. Current yield C/p is only the coupon-income component, not total return. The uncertainty in the future resale price is the first important bridge to asset pricing.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 14 — A 5% yield can produce a one-year loss

The initial price is 61.39132535. The later price discounts the unchanged face value over nine remaining years at the new 6% yield. The holding-period return is negative despite an initial YTM of 5%. This is an invented rate scenario, not a forecast. A one-year investor does not receive the 100 principal at the sale date. Passage of time and the shift in yield both matter.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 15 — What holding to maturity locks in

For a zero with no default, the terminal payoff is fixed in its own currency, and holding from purchase to maturity realizes the quoted annual effective yield. A coupon bond has a fixed contractual schedule, but realizing its YTM as a compound terminal-wealth return requires reinvesting coupons at that yield. An investor matching a particular liability cares about its currency, amount and date. Nominal certainty is not certainty of future purchasing power.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 16 — Risk-free depends on the investor’s horizon

This horizon distinction appears in both supplied courses. A long bond can be safe for one particular nominal liability and risky for a short investment horizon. A bill has little near-term price exposure yet cannot lock a ten-year reinvestment path. These are different risks, not contradictory claims. We revisit the liability perspective after duration and convexity.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md. Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 17 — Bills and auctions

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 18 — Treasury bills are short zero-coupon claims

Bills are used for short-term cash management. TreasuryDirect lists weekly issuance for the regular shorter terms and every four weeks for 52-week bills. A bill may be sold at a discount or at par. Avoid repeating the old reference course’s narrower maturity list or historical denomination numbers. A short Treasury promise can still have inflation risk or currency risk for a particular holder.

Reference: [TreasuryDirect, bills](https://www.treasurydirect.gov/marketable-securities/treasury-bills/). Rodemeier, Financial Markets and Institutions (Fall 2022), Lecture 4, pp. 10–16. Current rules are checked against TreasuryDirect, rather than the historical course examples.

## Slide 19 — How the auction clears

Use the official auction rules for current mechanics. A lower required discount rate means willingness to pay a higher price for a bill. Competitive bids are therefore accepted in increasing rate order. The highest accepted rate is the stop-out rate. All successful bidders obtain the uniform auction price implied by that rate, subject to the security’s quotation convention. The next pages isolate this mechanism with invented numbers.

Reference: [TreasuryDirect, auction process](https://www.treasurydirect.gov/auctions/how-auctions-work/). Rodemeier, Financial Markets and Institutions (Fall 2022), Lecture 4, pp. 10–16. Current rules are checked against TreasuryDirect, rather than the historical course examples.

## Slide 20 — Two ways to submit a bid

For bills, competitive bids specify the bank-discount rate. A TreasuryDirect account uses noncompetitive bidding; competitive participation goes through an eligible bank, broker or dealer. The published limits are 10 million dollars noncompetitive per auction and 35% of the offering for a competitive bidder, with further rules governing awards. Those institutional details are context rather than a trading recommendation. The uniform price is not the rate written in each winning bid.

Reference: [TreasuryDirect, auction process](https://www.treasurydirect.gov/auctions/how-auctions-work/).

## Slide 21 — An invented bill auction

The invented order book uses 28-day bills. First allocate 20 million across eligible noncompetitive bidders, leaving 80 million for competitive bids. Ask who receives how much before showing the answer. Lower rate bids mean higher willingness to pay. The example is deliberately different from the older course’s auction numbers.

Reference: [TreasuryDirect, auction process](https://www.treasurydirect.gov/auctions/how-auctions-work/). Rodemeier, Financial Markets and Institutions (Fall 2022), Lecture 4, pp. 10–16. Current rules are checked against TreasuryDirect, rather than the historical course examples.

## Slide 22 — The cutoff bidder receives a partial fill

After A and B receive 60 million, 20 million remains of the competitive 80 million. C is the marginal bidder and receives two-thirds of the requested face value. D is above the clearing rate and receives nothing. C’s rationing is not a different price. The 20 million noncompetitive award plus these competitive awards totals the 100 million offering.

Reference: [TreasuryDirect, auction process](https://www.treasurydirect.gov/auctions/how-auctions-work/).

## Slide 23 — One price for every successful bidder

All successful bidders in the invented auction, including noncompetitive bidders, pay the price associated with the stop-out rate. The discount quote uses face value and a 360-day basis. It is a market quotation, not the annual effective return used in our earlier spot examples. The 28-day interval starts at issue, not auction day. Treasury rounds published per-100 prices; multiplying large face amounts can therefore produce small rounding differences.

Reference: [TreasuryDirect, bills](https://www.treasurydirect.gov/marketable-securities/treasury-bills/). [TreasuryDirect, auction process](https://www.treasurydirect.gov/auctions/how-auctions-work/).

## Slide 24 — Actual four-week auction: 15 October 2026

These are frozen official TreasuryDirect API observations, checked against the result release. The auction occurs on 15 October, but the 28-day investment runs from 20 October to 17 November. The reported investment rate is 4.068%. Bid-to-cover is reported directly: do not divide total tendered by total accepted indiscriminately, because published total accepted can include additional SOMA awards outside the announced public offering. The data table also preserves an eight-week bill and the two note/bond auction cases.

Reference: [TreasuryDirect result release](https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20261015_2.pdf). Data: ../../data/lecture_03_auction_results_2026-10.csv.

## Slide 25 — The same bill has different rate quotations

Use F=100 and p=99.688889. The holding return is about 0.31208% over 28 days, not 4.068% over 28 days. The discount rate divides the interest amount by face value; the investment rate divides by the purchase price. This short-term investment-rate formula uses simple 365-day annualization for this 28-day example and is not the annual effective compounded return. Longer bills can have additional bond-equivalent-yield conventions. The exact daily dates and quotation labels stay in the source data.

Reference: [TreasuryDirect, bills](https://www.treasurydirect.gov/marketable-securities/treasury-bills/). Rodemeier, Financial Markets and Institutions (Fall 2022), Lecture 4, pp. 10–16. Current rules are checked against TreasuryDirect, rather than the historical course examples.

## Slide 26 — Coupon bonds also have clean and dirty prices

This is an invented between-coupon quote. Accrued interest compensates the seller for the coupon accrual up to settlement; it is not an extra final principal payment. The present value of future cash flows equals the full or dirty price. Our simple annual examples sit on coupon dates, so accrued interest is zero. Actual notes and bonds often quote a clean price and a semiannual bond-equivalent yield. Keep those conventions separate from our annualized teaching formulas.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md.

## Slide 27 — Curves and forwards

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 28 — A yield curve is one date, many maturities

Every point is a yield priced at the same observation time t, for a different remaining horizon. A curve can rise, fall, flatten or have a hump. A one-year point and a ten-year point do not show what the policy rate is today and in ten years. Interpreting the slope requires forward pricing and risk assumptions. These two smooth curves are invented teaching functions, not interpolated observations.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 29 — US Treasury par curve: all published tenors

The dots are the 14 published Treasury tenor observations, not 14 individual bond execution prices. A line only joins those points. Values include 4.17% at one month, 4.77% at two years, 5.10% at ten years and 5.43% at thirty years. The official Treasury par curve is itself estimated from market inputs. This panel retains the source quote convention; it is not substituted for the annual-effective zero curve in our pricing equations. Observation dates are frozen rather than described as live.

Reference: [US Treasury par rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610); [Fed fitted nominal curve](https://www.federalreserve.gov/data/nominal-yield-curve.htm); [ECB curve methods](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html). Inputs: ../../data/lecture_03_yield_curves_2026-10-16.csv.

## Slide 30 — The short end deserves a closer look

Short maturities are compressed on a thirty-year linear axis. Show the same points on a two-year scale before drawing conclusions about the front end. One, one-and-a-half, two, three, four and six-month maturities are all included, followed by one and two years. These are source-native par/CMT quotations, not a projected sequence of meeting decisions.

Reference: [US Treasury par rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610); [Fed fitted nominal curve](https://www.federalreserve.gov/data/nominal-yield-curve.htm); [ECB curve methods](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html). Inputs: ../../data/lecture_03_yield_curves_2026-10-16.csv.

## Slide 31 — Euro-area AAA: 358 fitted maturities

This is much denser than the former ten-point selection. The ECB publishes a smooth fitted curve at monthly maturities. Those points are model outputs estimated from a selected AAA euro-area central-government bond sample, not 358 independent executable instruments and not all euro sovereign issuers. The latest successful retrieval returned 14 October, so no 15 October value is fabricated. The ten-year par value is about 3.4781%, and thirty-year about 3.7160%. Compare dates and conventions before comparing it with the US panel.

Reference: [US Treasury par rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610); [Fed fitted nominal curve](https://www.federalreserve.gov/data/nominal-yield-curve.htm); [ECB curve methods](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html). Inputs: ../../data/lecture_03_yield_curves_2026-10-16.csv.

## Slide 32 — The zero-coupon (spot) yield curve

A zero-coupon or spot curve is a collection of single-payment discount rates, one for each maturity, at the same observation date. It is not the YTM curve of arbitrary coupon bonds. Its discount factors price any known dated payment in the same currency and credit class. Here T is remaining years, F is face value and p is the price of that single payment. Annual-effective compounding is the teaching convention.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15. [Federal Reserve curve methods](https://www.federalreserve.gov/data/nominal-yield-curve.htm).

## Slide 33 — STRIPS and estimated spot rates

STRIPS stands for Separate Trading of Registered Interest and Principal of Securities. Each separated principal/coupon claim is a zero-coupon security with its own single payment and maturity. Zero-coupon bonds are the broader payoff category. The Fed Gürkaynak–Sack–Wright curve shown next estimates a smooth discount function from selected off-the-run coupon notes and bonds; it does not fit a cross-section of STRIPS quotes. A hypothetical ZCB yield can therefore be inferred even without a directly traded zero at every maturity. STRIPS can trade at different yields because of liquidity, financing and tax effects.

Reference: [TreasuryDirect STRIPS](https://www.treasurydirect.gov/marketable-securities/strips/); [Federal Reserve sample and fitting methods](https://www.federalreserve.gov/data/nominal-yield-curve.htm).

## Slide 34 — Fitted zero-coupon spot yields

The curves show model-implied yields on hypothetical zero-coupon bonds, not a set of traded STRIPS. The common date is 9 October because the Fed Gürkaynak–Sack–Wright data are updated weekly with a lag. The US curve is evaluated monthly from published Svensson parameters over one to thirty years; the 30 annual source-grid points are marked. The euro curve uses the ECB’s published monthly zero rates on that same date. Both continuous-compounding rates z are converted to annual effective rates by exp(z)−1. This conversion changes the displayed numerical percentage, and these are zero rates, so they should not be mistaken for the earlier par quotes. The Fed fit uses off-the-run coupon securities and excludes bills, floating-rate notes, on-the-run and first-off-the-run notes and bonds.

Reference: [US Treasury par rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610); [Fed fitted nominal curve](https://www.federalreserve.gov/data/nominal-yield-curve.htm); [ECB curve methods](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html). Inputs: ../../data/lecture_03_yield_curves_2026-10-16.csv.

## Slide 35 — Spot, par and YTM are different objects

The distinction is essential when using dense online data. A spot curve prices individual dated payments. A par curve reports the hypothetical coupon rates that make bonds price at par under a coupon-frequency convention. A YTM is a summary for a particular bond. The Fed and ECB provide multiple fitted outputs; the labels must survive the download. Smoothing helps describe the cross-section, while fit assumptions, sample liquidity and data revisions remain relevant.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md. [US Treasury par rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610); [Fed fitted nominal curve](https://www.federalreserve.gov/data/nominal-yield-curve.htm); [ECB curve methods](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html). Inputs: ../../data/lecture_03_yield_curves_2026-10-16.csv.

## Slide 36 — A non-flat curve discounts dates differently

This two-year example has annual coupons and is valued on a coupon date. It prices two separately replicated payment dates. A single YTM can summarize the resulting price, but it is not a substitute for building the zero curve consistently across instruments. The next page infers one discount factor from a coupon price and an already known shorter discount factor.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md. Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 37 — Bootstrapping a two-year discount factor

The first coupon costs 4.80 to replicate. The remaining 95.20 buys the final 105 payment, so d(2)=95.2/105=0.9066667. The corresponding annual-effective two-year spot rate is about 5.01997%. This is an original hypothetical bootstrap, not a fit to the market snapshot. More complicated real bootstraps also account for coupon schedules, settlement, day counts and interpolation. Ask why the bond’s 5% par coupon differs from its two-year spot rate.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 38 — A forward loan is agreed today

For simplicity, the loan starts one year from today and ends a year later. A lender locks the future reinvestment rate; a borrower locks the future financing rate. This is a contractual rate, not a guess about what a new one-year loan will cost next year. A forward-starting agreement can have zero value today at the fair implied rate even though its future principal transfers are substantial.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 39 — Two ways to lock a two-year payoff

Both routes fix the final payoff today. The second route uses a forward, not a future rate left unknown. This distinction is what lets no-arbitrage relate them exactly. If borrowing and lending are executable on those matched terms, differing locked payoffs allow a self-financing arbitrage. The unsecured retail borrowing rate is not automatically the same as the collateralized zero-curve funding rate.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 40 — Exact no-arbitrage across the two routes

This is an exact relation for annual effective rates and one-year then one-year intervals under the matched trading assumptions. It does not require a theory of expected future policy rates. In discount-factor form, 1+f(1,2)=d(1)/d(2). A spread between theoretical and quoted forwards must first be checked for bid–ask, collateral, credit and funding differences.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 41 — Worked forward rate

The second-year rate must exceed 5% because the first year earns only 4%, while the total two-year locked return matches 5% compounded twice. The exact implied forward is 6.009615%. A common rough calculation, 2 times 5 minus 4 equals 6%, is only a small-rate approximation. Start with the compounded-payoff relation rather than teaching the approximation as an identity.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 42 — Replicating the forward with two zeros

The short one-year zero finances the initial purchase of the two-year zero. At year 1 the investor must pay 100 on the short position; at year 2 the long position receives 106.0096. Both initial prices are 96.153846. This exactly reproduces lending 100 over year 1 to year 2 at the forward rate. The cash-flow signs refer to the investor implementing the synthetic lender. Shorting and financing assumptions are explicit.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 43 — A mispriced forward creates a locked profit

The initial value is zero, the principal flows at year 1 cancel, and the year-2 net payment is positive. This is an invented inconsistency, not an observed opportunity. The proof requires the same currency, dates, credit and collateral terms, together with executable lending and borrowing and no offsetting costs. An attractive expected trading return with downside risk is a different concept from this deterministic arbitrage.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 44 — A forward is a price; a forecast is a belief

This is where we leave exact replication and enter asset pricing under uncertainty. A forward is a contractual rate fixed today. The physical expectation of next year’s short rate averages future outcomes under actual-world beliefs. Risk compensation and nonlinear pricing can separate them. The next section rebuilds the former unexplained decomposition one step at a time.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 45 — Expectations and term premia

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 46 — Rolling over leaves the second rate unknown

These are two hypothetical future short-rate outcomes, not forecasts. The two-year zero locks nominal final wealth, while rolling one-year instruments exposes the investor to the year-2 rate. Therefore their actual outcomes need not be equal. Only adding the forward contract removes the rate uncertainty and gives the earlier exact arbitrage relation. Their expected returns can differ when risk is priced.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 47 — Exact compounding across maturities

For whole-year periods and consistent annual-effective conventions, the relation is exact. The long zero yield is a geometric, not arithmetic, average of the locked one-year forward returns. Logs turn that geometric relation into an arithmetic average of log gross rates. At low rates, the arithmetic average of the simple forwards is a useful approximation. Nothing in this algebra has yet introduced expected future policy or a term premium.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 48 — A premium for each forward interval

Define mu_k as today’s physical expectation of the one-year spot rate at future date t+k, and phi_t(k)=f_t(k,k+1)−mu_k. This is an exact definition of a rate wedge in matched annual-effective conventions. The wedge is often called a forward term premium. Its interpretation can include uncertainty/convexity effects and model conventions; it is not automatically an expected holding-period excess return. No-arbitrage determines f from current discount factors but does not identify mu or phi separately. At k=0 the current one-year rate is known, so phi_t(0)=0. Setting all future wedges to zero adds an expectations-hypothesis assumption.

Reference: [Federal Reserve, forward term premia](https://www.federalreserve.gov/pubs/feds/2005/200533/200533pap.pdf); Bodie, Kane & Marcus, Investments, ch. 15.

## Slide 49 — An explicit expected short-rate path

The five invented values are physical expectations formed today for successive one-year market rates. They are not market forward contracts. Their simple arithmetic mean does not exactly price a five-year zero under annual-effective compounding. The next pages add a horizon-specific forward wedge, then compound the resulting locked forward gross returns. These are assumed paths for illustration, not estimated forecasts.

Reference: Bodie, Kane & Marcus, Investments, ch. 15.

## Slide 50 — Why a term premium can appear

The risk is not merely that a bond has a long maturity. The value of its return in the investor’s bad states matters. Inflationary shocks can reduce nominal bond values when investors need protection; recessionary shocks can make safe bonds valuable hedges. Demand from pension funds matching liabilities or changes in bond supply can also affect required compensation. A term premium can be positive or negative and can change over time. Jensen’s older liquidity-preference discussion is therefore broadened rather than treated as a universal positive-premium law.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 51 — Premiums can differ across future years

Rows are successive annual intervals beginning at k=0. The expected one-year rates are 4, 3.5, 3, 3, 3 percent. The forward wedges are 0, 0.4, 0.6, 0.8, 1 percentage points. Adding within a row gives forward rates 4, 3.9, 3.6, 3.8, 4 percent. Adding the components of one rate is distinct from aggregating returns across time, which requires multiplication. The current interval has no forecast uncertainty and its wedge is zero. All numbers are invented.

Reference: Bodie, Kane & Marcus, Investments, ch. 15; [Fed forward premium definition](https://www.federalreserve.gov/pubs/feds/2005/200533/200533pap.pdf).

## Slide 52 — Compound the forward rates, period by period

Substitute the exact per-forward decomposition f=mu+phi into the no-arbitrage product of locked forward gross returns. The n-year annual-effective spot yield is the geometric mean of those gross returns minus one. This relation does not replace the expectation of a random compounded rollover payoff with a product of expectations. The mu/phi split is not observable from a yield curve alone. Exactly averaging is valid for the logarithms of the locked gross forwards, as shown on the preceding compounding slide.

Reference: Bodie, Kane & Marcus, Investments, ch. 15; [Fed forward term premia](https://www.federalreserve.gov/pubs/feds/2005/200533/200533pap.pdf).

## Slide 53 — Worked five-year compounded yield

The product of the five locked gross forwards is 1.2084796319; taking its fifth root and subtracting one gives 3.85989209%. With the same assumed physical expected rates but all forward wedges set to zero, the geometric rate is 3.29922723%. That second calculation is an expectations-hypothesis scenario, not the expected return from a random rollover strategy. One observed spot curve cannot identify physical expectations and forward premia separately.

Reference: original worked example using the no-arbitrage relation; Bodie, Kane & Marcus, Investments, ch. 15.

## Slide 54 — Three objects to keep separate

The official dot plot and its interpretation are in Lecture 2’s policy-feedback section. Do not put a June dot next to an October forward and call the difference a clean term-premium estimate. Dates, horizons, participants, instruments and pricing conventions differ. A term-structure model is needed to translate relevant information into an expectations component. This is the main interpretation lesson of the dot plot and the decomposition. The same distinctions matter when reading a newspaper claim that the bond market expects a particular policy decision.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md. [Federal Reserve, 17 June 2026 SEP, pp. 2 and 4](https://www.federalreserve.gov/monetarypolicy/files/fomcprojtabl20260617.pdf). Inputs: ../../data/fed_dots_june2026.csv.

## Slide 55 — Policy cuts and rising spot yields

All numbers are invented. The current policy target falls 25 bp, but the one-year spot quote falls only 10 bp; a one-year market yield need not equal the overnight policy setting. The expected one-year rate for the second year rises from 3% to 3.4%, while its forward wedge rises from 0.5 to 1 percentage point. Thus the second-year locked forward rises 3.5% to 4.4%. Exact compounding gives a two-year spot increase from 3.74969879% to 4.14969995%, or 40.00011568 bp. The assumptions specify why the spot yield rises; a policy cut alone does not identify a trade.

Reference: original hypothetical scenario; Bodie, Kane & Marcus, Investments, ch. 15.

## Slide 56 — Duration and convexity

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 57 — Price sensitivity to a yield change

The experiment fixes the bond’s promised payments and remaining maturity while varying its discount yield. For this ten-year zero, that yield is precisely the ten-year spot point on the term structure. For coupon bonds, YTM summarizes prices generated by all relevant spot discount factors; a YTM derivative is a one-parameter sensitivity and does not describe every possible curve twist. The graph holds face value and remaining maturity fixed. It is a cross-section of possible current prices as the required yield varies, not a time path with the bond aging. The slope is negative, but it changes with the yield. A tangent gives the first-order approximation, and curvature explains its error for larger moves. All rates are nominal; this local i is the bond yield, not a new real-rate notation.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 58 — Modified duration is the normalized slope

Modified duration is local sensitivity to the selected yield parameter. It normalizes the derivative by the price, so multiplying duration by a decimal rate change approximates the proportional price change. If duration is eight, a 50-basis-point rise implies about −4%. It assumes fixed cash flows and an unchanged credit/liquidity setting. For a coupon bond, a change in its single YTM is a one-parameter repricing; a general curve twist requires more risk information.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 59 — A zero’s duration follows by differentiation

Differentiate while fixing maturity and face value. The face value cancels from proportional sensitivity, so the duration of a zero does not depend on whether F is 100 or 1,000. Modified duration is slightly below the ten-year payment time under annual compounding. This is distinct from Macaulay duration, which equals exactly T for a zero. The derivative is with respect to a decimal annual-effective rate.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 60 — Coupon duration weights the payment dates

The three-year 4% coupon bond at 5% yield has price 97.27675197. Each weight is CF_k/(1.05^k p), and the weights sum to one. Macaulay duration is the present-value-weighted payment time, 2.88437972 years. Coupons bring part of the value forward, so this is less than three years. This weighted-time interpretation gives intuition before dividing by 1+i to obtain modified sensitivity.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 61 — Macaulay and modified duration

For annual payments the derivative of each discounted cash flow generates k/(1+i), giving this relation. With m coupon periods per year and a nominal annual YTM, the corresponding factor is 1+i/m. Keep the coupon-frequency convention explicit before importing a quoted duration. Duration is a cash-flow-timing measure and a sensitivity only after the chosen normalization is specified.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 62 — Dollar value of one basis point: DV01

DV01 is market shorthand for Dollar Value of 01, where 01 denotes 0.01 percentage point or one basis point. It is also called the price value of a basis point, PVBP. It converts the dimensionless proportional-rate sensitivity into currency per basis point. For a USD one-million position with modified duration eight, 1e6×8×0.0001=800 dollars per basis point. In another currency, quote the same sensitivity in that currency. V is the current market value of the position, not its face value. A positive DV01 quoted for a long bond measures the approximate loss for a one-basis-point yield rise, or gain for a one-basis-point fall. In later trade tables, signed DV01 is positive for long and negative for short, with P&L approximately minus signed DV01 times the yield move in basis points. The 1 million and duration eight are hypothetical risk inputs.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

Additional reference: [New York Fed research, DV01 as dollar value of a basis point](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1070.pdf).

## Slide 63 — A ten-basis-point move

This is the first-order monetary calculation for the preceding position. The signs reverse for a short position. The symmetry is a property of the tangent approximation, not of the full bond-price function. We now use the Taylor expansion to make the missing curvature term explicit.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 64 — Duration comes from a Taylor expansion

For this smooth bond-price function, Taylor’s theorem around the initial yield gives the local expansion. Retaining only the first derivative gives the duration rule. Retaining the second derivative gives the duration-plus-convexity rule. The remainder depends on higher derivatives and the shock size, so the quadratic is still an approximation. This price convexity is not the same object as the Jensen adjustment that arises when averaging uncertain future rates in a term-structure model.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 65 — Convexity normalizes the second derivative

Divide the Taylor expansion by the initial price. Since d²[CF_k(1+i)^(−k)]/di² equals k(k+1)CF_k(1+i)^(−k−2), every positive fixed payment contributes positive curvature for i>−1. The second-order term is positive for either sign of the rate change. This is not a claim that every security has positive effective convexity: embedded call or prepayment options can change the cash flows when rates change.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 66 — A zero’s convexity is explicit

The ten-year zero’s modified duration is 9.5238095 and convexity is 99.7732426 under annual-effective compounding. The positive second derivative has a direct calculus proof, rather than being a general intuition asserted without assumptions. Face value cancels from both normalized sensitivities. Use a decimal shock: one percentage point is 0.01, whose square is 0.0001.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 67 — Exact, tangent and quadratic repricing

The horizontal variable is percentage points for readability; the calculation converts it to decimals. The vertical axis is proportional price change in percent. The duration line is tangent at zero. The quadratic adds positive curvature for both signs of the move. For large shocks it can still deviate, and the approximation must not be extrapolated beyond a sensible neighborhood. This is an original native TikZ plot, not a reproduced course or book figure.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 68 — Work out a one-percentage-point move

All calculations use the same ten-year zero initially yielding 5%. Read the exact numbers from the table, independently generated from the price formula. The convexity correction is about +0.499 percentage points of price return for either sign of the one-point yield move. It reduces the estimated loss when yields rise and increases the estimated gain when yields fall. The correction is not an additional coupon or guaranteed profit.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 69 — The asymmetry has economic meaning

With positive convexity, the tangent lies below the exact price function. Relative to the same starting price, a symmetric yield decrease therefore creates a larger gain than the loss from the corresponding increase. This does not create a free trading strategy: prices, yields, duration, credit and financing differ across instruments. Callable bonds and mortgage-backed securities can have negative effective convexity because the borrower can shorten the cash-flow schedule when rates fall.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 70 — Sensitivity is conditional on the experiment

The exact derivative is conditional on the parameter being changed. A bond’s YTM can move because of Treasury rates, credit spreads or liquidity, while a portfolio is exposed to several maturity points. Key-rate durations distinguish where the curve moves. Convexity handles the nonlinear part of one specified shift; it does not eliminate cash-flow uncertainty, funding risk, option exercise or rebalancing needs. The next trade deliberately changes the curve slope.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 71 — A liability changes what counts as risky

A ten-year zero’s market value can move strongly while remaining a precise cash-flow hedge for an equal nominal liability on its maturity date. When discount rates move, the matched asset and liability values move together. A short bill avoids most immediate mark-to-market risk but does not fix the future rate needed to fund a long liability. This finance perspective is different from asking which bond will rally next week. A full immunization problem is an optional extension, not a guarantee from the word duration alone.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 72 — A bond fund usually keeps exposure beyond one maturity

This describes a generic rolling bond fund, not every fund or target-maturity product. A fund’s portfolio value and distributions depend on changing yields, reinvestment and its management rules. It generally has no promise to redeem a unit at a fixed face value on one specified date. A target-maturity fund can behave differently. Both instruments can be useful for different purposes; the point is to identify the contract and the risk rather than treating a displayed yield as a guaranteed personal return.

Reference: Bodie, Kane & Marcus, Investments, 11th ed. (2018), ch. 14, pp. 432–448. Jensen, Financial Economics (2023), Part 15A, pp. 6–14. Rodemeier, Financial Markets and Institutions (2022), Lecture 3, pp. 3–27, 35–50. Bibliography: ../../docs/source_map.md. Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 73 — Hedging and market cases

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 74 — News lab: income horizon or price trade?

The accessible opening of the column distinguishes investors attracted to the stream of bond income from those making a price/rate view. Use only that verified opening as the source, rather than claiming the full paid article has been read. Ask two students to describe a ten-year payment-matching investor and a one-year trader buying the same bond. Their mark-to-market exposure is identical, but the way it relates to their objectives differs. The source article and MIT access guide are linked in the reading list.

Reference: [WSJ, Telis Demos, bond-strategy column, 8 October 2026](https://www.wsj.com/finance/investing/choosing-the-right-bond-strategy-for-todays-high-yield-world-0c4b6a78). The accessible opening motivates the question; the exercise is original.

## Slide 75 — News lab: buying during a Treasury sell-off

The FT headline and opening were verified through its authorized syndicated Yahoo Finance version; the direct FT page requires access that this tool could not confirm. Do not claim MIT authentication or full-text access was completed. No article screenshots, full text or proprietary flow datasets are redistributed. The discussion asks what horizon, duration and expected yield path would make a purchase sensible for a given objective. A high observed yield does not by itself identify a future price rally or an expected excess return.

Reference: [Financial Times, Harriet Clarfelt and Kate Duguid, 13 October 2026](https://www.ft.com/content/6fa735a2-a590-4461-b092-920ba489e7a8). Headline and opening verified through the FT’s syndicated Yahoo Finance version. Full FT text may require MIT SSO.

## Slide 76 — Two real auctions, two different questions

The remaining terms are nine years ten months and twenty-nine years ten months because these are reopenings. The ten-year note’s coupon is 4.625%, while its high auction yield is 5.300%; the thirty-year bond’s coupon is 5.125%, while its high yield is 5.618%. The offering is the announced public amount; additional awards can make total accepted differ. A high absolute yield and strong bidding relative to expectations can coexist. Bid-to-cover is informative but needs comparison with similar auctions and the pre-auction market.

Reference: [TreasuryDirect 7 October results](https://www.treasurydirect.gov/TA_WS/securities/search?format=json&auctionDate=2026-10-07); [8 October results](https://www.treasurydirect.gov/TA_WS/securities/search?format=json&auctionDate=2026-10-08). ../../data/lecture_03_auction_results_2026-10.csv.

## Slide 77 — An auction tail needs a market benchmark

A when-issued quote is the pre-settlement market yield for the security being auctioned. A positive tail means the auction cleared at a higher yield, hence lower price, than that contemporaneous benchmark. A negative difference is often called a stop-through. The example is invented; it is not a claim about the 7 October auction, since a matched deadline when-issued observation was not verified. A comparison with last month’s auction yield cannot measure this tail.

Reference: [TreasuryDirect, auction process](https://www.treasurydirect.gov/auctions/how-auctions-work/). Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 78 — A curve view needs two maturity scenarios

The two-year yield falls by 50 basis points and the ten-year yield falls by ten. Both bond prices therefore rise, but the relative response depends on position size and duration. The joining segments only summarize the two scenario points, not a fitted thirty-year market curve. These are matched bond-yield risk inputs for the P&L exercise, rather than mixing the official par and zero datasets.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 79 — This scenario is a bull steepening

Bull describes falling yields and rising fixed-cash-flow prices. Steepening describes an increase in the selected long-minus-short yield spread, here from 30 to 70 basis points. A steepening can also occur with rising yields, so the two words describe different dimensions. We use i_2 and i_10 as shorthand for the two bond-yield inputs, not to redefine the spot-versus-YTM distinction.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 80 — Expressing the relative view

Buying the short maturity and shorting the long maturity expresses a steeper long-minus-short yield spread when the legs are sized by DV01. The short ten-year leg loses in this particular bull-steepening scenario, since that bond also rallies. The expected gain comes from a sufficiently larger DV01-adjusted rally in the two-year leg. Equal market values or equal face values generally give different sensitivities.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 81 — Match DV01, rather than market values

The two-year long has DV01=1,000,000 times 1.8 times 0.0001=180 currency units per basis point. Matching that magnitude requires only 225,000 market value of the duration-eight ten-year bond. Its signed DV01 is −180 because the position is short. This is a market-value hedge, not a notional or face-value equality. It is approximately neutral to a small parallel yield move at inception.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 82 — Work out the scenario profit and loss

P&L is minus signed DV01 times the yield change in basis points. The long leg gains 9,000 and the short leg loses 1,800. For equal absolute DV01 q, combined first-order P&L is q times the change in the long-minus-short yield spread, giving 180 times 40=7,200. This is a specified conditional scenario, not an arbitrage. Actual financing and short-sale mechanics can materially affect the result.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 83 — A small parallel move cancels at first order

The equal and opposite DV01 exposures cancel the local level move under this simplified two-point repricing. That cancellation is first order and local, not an exact invariance for large shocks. The two bonds have different convexity, carry, roll-down and funding costs. Their sensitivities also evolve as time passes and yields change, so a live hedge requires monitoring and often rebalancing.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 84 — Counterfactual: the curve flattens

The two-year fall is now smaller than the ten-year fall, so the ten-year minus two-year spread narrows by 40 basis points. The short long-duration leg loses more than the long two-year leg gains. This is why forecasting a general rate cut is not enough to define the curve trade. It must be a relative view that differs from what is already priced, with position sizing and horizon specified.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 85 — Price impact of the policy-cut scenario

Revisit the exact compounded two-year scenario. Its spot-yield rise is 40.00011568 bp, rounded to 40 bp for mental arithmetic. An assumed one-million position with modified duration 1.8 loses about 7,200 at first order. With assumed convexity five, add 40, giving −7,160. These are hypothetical local risk inputs, not a claim to have calibrated a particular security. This calculation includes neither financing nor carry.

Reference: original example; Bodie, Kane & Marcus, Investments, ch. 16.

## Slide 86 — Questions before taking the trade

Ask each student to state a trade in these concrete terms. A model-based term-premium estimate, an auction headline and a central-bank dot are useful evidence, but none alone identifies a profitable position. The counterfactual should include adverse yield shape changes and a plausible funding constraint. This closes the core teaching route; the next section is optional mathematics for readers who want the underlying asset-pricing framework.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md. Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 87 — Optional foundations

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 88 — General forward intervals

This generalizes the one-year forward calculation to any two positive remaining times with T2>T1. The ratio is the gross locked growth over the interval; the power annualizes it. It follows from a portfolio of two zeros. For actual FRAs, futures and swaps, use contractual day counts and settlement conventions; futures convexity adjustments and collateral differences can separate their quotes from this ideal forward.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 89 — Continuous and annual-effective spot rates

Here z is a continuously compounded nominal zero rate, used only to document the source convention. It is not a new name for the real rate r. A source quote of 5% continuous corresponds to an annual-effective rate exp(0.05)−1=5.12711%, not exactly 5%. This transformation does not change a discount factor or produce a market move. The data CSV retains both the source percentage and the converted percentage.

Reference: [US Treasury par rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610); [Fed fitted nominal curve](https://www.federalreserve.gov/data/nominal-yield-curve.htm); [ECB curve methods](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html). Inputs: ../../data/lecture_03_yield_curves_2026-10-16.csv.

## Slide 90 — The par coupon comes from discount factors

Set the dirty price equal to face value, price each payment with the zero curve, and solve for the annual par coupon. With fractional coupon periods, the denominator includes the relevant accrual fractions and conventions. This makes the distinction between the spot curve and the par curve explicit. It also explains why a smoothly estimated spot curve can generate a different-looking par curve from the same underlying discount factors.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 91 — Optional: ACM estimates

The black line is the ACM model’s fitted ten-year yield, not a specific Treasury’s YTM. The rust line is its estimated term premium. The teal line is computed as fitted yield minus term premium, corresponding to the model’s remaining/risk-neutral-yield component. It should not be described as a directly surveyed average forecast. Model-specific nonlinear and convexity conventions matter. The fitted yield also differs slightly from the source GSW yield; both are retained in the CSV. The historical chart illustrates that the premium can change and need not be positive.

Reference: [New York Fed, Treasury term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs), Adrian–Crump–Moench model. Inputs: ../../data/lecture_03_acm_decomposition.csv.

## Slide 92 — ACM components use a model convention

At the final frozen month-end, fitted yield is 5.258961%, premium 0.885008% and the remaining component 4.373953%. The displayed two-decimal sum is rounded. In the ACM framework the remaining/risk-neutral yield reflects the modeled expected-rate component with model conventions, not a directly observed public expectation. The measured GSW ten-year zero yield on this date is 5.283562%, showing the small model fitting difference. These are September model estimates, not a live October decomposition.

Reference: [New York Fed, Treasury term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs), Adrian–Crump–Moench model. Inputs: ../../data/lecture_03_acm_decomposition.csv.

## Slide 93 — Two states: equal average payoff, different price

This optional example introduces state pricing rather than assuming a universal discount rate for expected cash flows. State prices are q_good=0.4 and q_bad=0.56153846, both positive. Hence a certain one-unit payment costs q_good+q_bad=1/1.04, while A costs 100q_good=40 and B costs 100q_bad=56.153846. Their physical expected payoffs are both 50, but B insures the bad state. This is an original finite-state construction; it does not claim these numbers describe the market or appear in the reference courses.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 15, pp. 467–486. Jensen, Financial Economics (2023), Parts 14 and 15B. Bibliography: ../../docs/source_map.md.

## Slide 94 — A stochastic discount factor prices states

In the preceding finite-state example, q_s=probability_s times m_s, with m_good=0.8 and m_bad=1.123076923. The covariance decomposition is exact algebra. A payoff that arrives when m is high has a larger current price for the same expected payoff and thus a lower required expected return. A certain one-unit payoff has price E[m], so its gross risk-free return is 1/E[m]=1.04. Under suitable no-arbitrage assumptions, positive state prices support such a discount factor. This is a bridge to future asset-pricing classes, rather than a full equilibrium derivation.

Reference: John H. Cochrane, Asset Pricing, revised ed., ch. 1; optional original two-state construction. See ../../docs/lecture_03_readings.md.

## Slide 95 — Optional liability hedge: match value and duration

Assume a flat 5% curve and assets initially worth the liability PV, 100/1.05^10. The one-year and twenty-year zeros have Macaulay durations equal to their maturities. These market-value weights give an asset Macaulay duration of ten, matching the liability; the shared 1.05 normalization also matches modified duration. This cancels a small parallel-yield sensitivity at inception, while cash-flow dates and convexity still differ. Future reinvestment and rebalancing are needed. The example adapts the course’s immunization mechanism using different maturities, amounts and rates.

Reference: Bodie, Kane & Marcus, Investments, 11th ed., ch. 16, pp. 496–508. Jensen, Financial Economics (2023), Part 16, pp. 3–13. Bibliography: ../../docs/source_map.md.

## Slide 96 — Reading

Introduce the section question and ask for an economic prediction before calculating. The section can be a separate short meeting.

## Slide 97 — Reading and next questions

The textbook is Investments, 11th edition, 2018: chapter 14 on prices/yields, chapter 15 on the term structure and chapter 16 on duration, convexity and management. Jensen’s 2023 Financial Economics Parts 14–16 guide replication, realized returns and risk management. Rodemeier’s 2022 Financial Markets and Institutions Lectures 3–4 guide valuation and auctions; their old market examples and institutional facts are checked against current official pages. Krugman–Obstfeld–Melitz chapter 14 remains useful for matched asset-return comparisons in international finance. The newspaper links are reading prompts, not reproduced articles. The user’s AI-trade article is kept in the local reference backlog for a later Lecture 2 discussion.

Reference: See ../../docs/lecture_03_readings.md and ../../docs/source_map.md.

