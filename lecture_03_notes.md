# Lecture 3 — Bonds and yield curves

How do dated payments, expectations and risk premia produce a yield?

## Delivery

Use the core route in `syllabus.md`. Pause on the questions and ask for a curve shift, numerical prediction or counterfactual before revealing the next slide. All unlabelled numerical examples and model paths are hypothetical. Rates in pricing formulas use decimals; policy examples and chart labels specify percent or percentage points.

## Slide 1 — Bonds and yield curves

Open by asking the central question. Encourage predictions before introducing the model. The audience knows mathematics but is meeting economic mechanisms for the first time.

Reference:  [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 2 — Today’s route

Begin with cash-flow dates and the investor’s opportunity cost. Build up to yields, forwards and term premia before considering a trade. Ask for the sign of each price change before calculating it.

Reference: [Sergeyev, Bocconi 30054, lecture 4](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 5](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 3 — Bonds and the yield curve

State the question for this section, then ask the group for a prediction before showing the following example.

Reference:  [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 4 — A bond is a schedule of promised payments

Define the instrument before predicting a ten-year yield. A promise can involve default risk; later idealised pricing examples hold cash flows fixed. F and P need not be equal. Q remains the consumer price index, so it cannot be confused with P.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 5 — A coupon rate applies to face value

Define c for bonds separately from the earlier consumption coefficient, which belongs to a different model and section. Emphasise the section context; c here is a labelled coupon rate. Actual Treasury notes/bonds pay semiannually; this teaching instrument pays annually.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 6 — The three-year cash-flow timeline

Use F=1000 and annual coupon 40 from the preceding slide. There are three coupon payments, and principal is paid once. The initial price is an outflow. This is an original diagram with invented values.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 7 — Face value and the price quote are different

Define the quotation convention rather than asserting a universal 1000 denomination. A clean quoted price may differ from the cash paid after accrued interest. TreasuryDirect purchases begin at 100-dollar increments.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 8 — A zero-coupon bond has one future payment

This is a valuation in a consistent annual yield convention. Zero coupon means no interim coupon, not zero investment return. The yield is nominal and tied to its horizon. For a zero-coupon bond, spot yield equals its YTM.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 9 — Discounting a face value of 1,000

The exact value is 907.029478. All numbers are hypothetical and repayment is assumed. No coupon-reinvestment issue exists for a held-to-maturity zero-coupon instrument.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 10 — A coupon bond discounts every dated payment

F and coupon rate c were defined before the formula. A YTM is a price summary for a specified schedule, not an assumption that the whole term structure is flat. No-arbitrage pricing more generally uses individual dated discount factors.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 11 — The coupon-bond calculation

This continues the same three-year, F1000 example. The result is 972.7675. Coupon rate is contractual; YTM changes as market price changes. Realised return may differ if sold before maturity or if interim coupon reinvestment differs.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 12 — Higher discount yields mean lower bond prices

The original plot uses P=100/(1+yield)^5. Prices and yields move inversely holding positive cash flows fixed. A different expected cash-flow schedule, default outlook or option structure can complicate the relationship.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 13 — Duration measures local yield sensitivity

Yield changes in this formula use decimals. Modified duration is −(1/P)dP/dyield; curvature explains why larger moves need convexity terms. This is a small-move approximation at fixed cash flows, not an exact large-move P&L guarantee.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 14 — Treasury bills pay face value without periodic coupons

The 98-to-100 example is hypothetical and has no specified remaining maturity, so it cannot imply an annualised yield. Actual bill bank-discount quotations use a different denominator/day-count convention. TreasuryDirect purchases start at 100 of face value.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 15 — The yield curve is one date with many maturities

The curve is invented and compares nominal zero-coupon yields in one currency on one observation date. A ten-year yield concerns a ten-year payoff, rather than a rate guaranteed to prevail ten years from today.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 16 — Yield curves can have different shapes

Preserve the initial shapes but postpone causal interpretation until forward rates and term premium have been introduced. Distinguish these theoretical spot curves from official par curves in the dated snapshot.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 17 — US and euro-area curve snapshot

The selected source-native par data are frozen in the accompanying CSV. The US two-year is 4.77%, ten-year 5.10%; the 2s10s spread is 33 bp. The EUR sample is AAA euro-area government issuers. Differences do not measure a hedge-adjusted arbitrage profit or directly identify expected rates versus term premia.

Reference: [US Treasury, October 2026 curve data](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610). [ECB, Yield-curve methods](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 18 — Spot, forward and coupon-bond yields

The labels distinguish horizons and contractual objects rather than force arbitrary symbol memorisation. A forward is agreed today. An unknown future realised short rate is not already fixed. All rates here are nominal with matched annual compounding.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 19 — Two ways to lock a two-year payoff

The second route requires an enforceable forward-start reinvestment contract agreed now. Investing next year at whatever rate then prevails is a different, risky strategy. Comparable credit/collateral and frictionless borrowing/lending are assumed.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 20 — No-arbitrage makes the locked payoffs match

This is replication with matching cash-flow dates. The forward is determined by discount factors D(0,1)/D(0,2)−1. The equality needs executable contracts and consistent conventions; it does not assume the future spot rate is known.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 21 — Calculating the implied forward

Exact forward is 6.009615%. One-year investment gives 104, which earns the locked forward to give 110.25. Rounding the forward may produce a fractional-cent difference. None of these numbers is current market data.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 22 — A locked forward is not a guaranteed forecast

No-arbitrage gives a relation among prices, not a proof that forward equals expected future short rate. Investor risk preferences and hedging demand matter. This distinction is the bridge to the term-premium decomposition.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 23 — A long yield contains a path and a premium

Define term premium in words before writing a summation. It can be negative when duration is a valuable hedge. It is not simply a default spread or expected inflation. Decomposing an actual observed yield requires a model.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 24 — Writing the yield decomposition mathematically

This is the same stylised approximation as in the prior explanation, with the observation date suppressed on the left and premium for readability. Annual one-period rates are matched to an n-year zero yield. Coupon-bond YTM and exact compounding require more detailed treatment.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 25 — Today's rate and a ten-year yield can move differently

This is a conditional explanation, not an automatic reaction to cuts. Changes must be relative to prior pricing, and both decomposition terms are unobserved. The final exercise supplies assumed changes so the price effect can be computed.

Reference: [Bank of England, Yield curves](https://www.bankofengland.co.uk/statistics/yield-curves/terminology-and-concepts). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 26 — Exercise: a cut today with a bond sell-off

The assumed changes are relative to prior market pricing. A more persistent inflation outlook could raise later expected policy rates despite a near-term cut. Distinguish a supplied scenario from evidence that this was the cause of an observed market move.

Reference: [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 27 — The decomposition gives the answer

Apply the yield move approximately to the duration-8 bond’s YTM, assuming its spread and cash flows do not change. A benchmark zero yield and a coupon-bond YTM are not identical objects. The small-move estimate excludes carry, convexity, costs and any cash-flow changes.

Reference: [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 28 — A curve-slope exercise

State the question for this section, then ask the group for a prediction before showing the following example.

Reference:  [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 29 — A curve view needs two maturity forecasts

Before: two-year yield 4.2%, ten-year 4.5%. Scenario: two-year 3.7%, ten-year 4.4%. The following trade uses local duration on representative bonds. These are original hypothetical values, not the official snapshot and not predicted future policy rates.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 30 — This is a bull steepening

One basis point is 0.01 percentage point: the slope moves from 30 to 70 basis points, widening by 40 basis points. A curve can also steepen with rising yields (bear steepening), so the slope description alone does not give direction.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 31 — Expressing the relative view with bonds

Shorting means selling a borrowed bond and later repurchasing it. Borrow availability, financing, margin, coupon compensation and transaction costs matter. This is an educational conditional position, not a recommendation. Equal face values or market values do not equalise rate risk.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 32 — DV01 puts the two legs on comparable terms

Use the positive magnitude of DV01 for each bond before signing a position. A long loses approximately DV01 dollars when its yield rises by one basis point; a short gains that amount. Modified duration was defined earlier. A parallel hedge is local and does not hedge every term-structure shock.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 33 — Exercise: choose the size of the short leg

Use a single currency and representative instruments with the stated durations. DV01s are magnitudes; position signs differ. Ask for V_short=180/(8×0.0001)=225000. Sizes are market values, not face values. These durations and yields are hypothetical.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 34 — Equal DV01 requires unequal market values

Signed DV01 here is exposure convention: a positive long DV01 loses when yield rises. First-order parallel sensitivity sums to zero. Equal DV01 hedges the specified local parallel shift only, not twists, curve reshaping, convexity or spread moves.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 35 — Work out the scenario profit and loss

The long gains because its yield falls; the short loses because its yield also falls, but less. A uniform 10-bp rally would cancel at first order. The scenario profit follows from the supplied yield changes; correctly calling a policy cut alone does not establish these changes.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 36 — Counterfactual: what would make this trade lose?

Ask for a numeric counterexample: two-year yield falls 10 bp while ten-year falls 50 bp. The same position loses 7200 at first order. Further risks include borrow squeeze, margin, spread risk, changing DV01 and convexity. If presenting live trading context, this requires current independently verified prices and financing.

Reference: [TreasuryDirect, Pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/). [New York Fed, Term premia](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). [KOM, 12th Global Edition, ch. 14, printed pp. 390–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 37 — Further reading

Read the relevant sources after the lecture rather than before a first encounter. The course source map records what was retained, simplified or placed in optional material.

Reference: See source_map.md and syllabus.md.

