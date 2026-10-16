# Lecture 4 — Foreign exchange

How do returns, expectations and purchasing power price a currency?

## Delivery

Use the core route in `../../syllabus.md`. Pause on the questions and ask for a curve shift, numerical prediction or counterfactual before revealing the next slide. All unlabelled numerical examples and model paths are hypothetical. Rates in pricing formulas use decimals; policy examples and chart labels specify percent or percentage points.

## Slide 1 — Foreign exchange

Open by asking the central question. Encourage predictions before introducing the model. The audience knows mathematics but is meeting economic mechanisms for the first time.

Reference:  [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 2 — Today’s route

The bond class supplied no-arbitrage replication. FX adds the distinction between a locked conversion and a future uncertain spot price. The quote convention remains home currency per foreign unit.

Reference: [Sergeyev, Bocconi 30054, lecture 4](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 5](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14, printed pp. 381–411](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 3 — Currency quotes and contracts

State the question for this section, then ask the group for a prediction before showing the following example.

Reference:  [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 4 — One quote convention throughout

Fix this convention before every numerical calculation. Market pairs can be quoted in the opposite direction. EUR/USD is dollars per euro in market notation, so the US is home in that example. A percent change in the reciprocal quote is not exactly the negative of the original percent change.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 3–9](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 5 — A quotation example

These values are hypothetical. JPY is home and USD foreign. The home-per-foreign quote falls 10%; the reciprocal USD price of one yen rises 11.11%. Always state the currency of a payoff and convert using units rather than a memorised direction.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 3–9](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 6 — Spot, forward and FX swap

Spot settlement conventions depend on currency and calendar. A forward locks the exchange of agreed amounts, subject to counterparty/collateral arrangements. An FX swap has two linked legs. These instruments allow funding and hedging; their existence does not imply exchange-rate uncertainty disappears for an unhedged investor.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 16–18](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 7 — Covered interest parity

State the question for this section, then ask the group for a prediction before showing the following example.

Reference:  [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 8 — Two routes for the same home-currency payoff

Let R_home and R_foreign be matched one-period nominal rates, E the spot quote and F the forward in home currency per foreign unit. Both routes must end on the same date with comparable credit/collateral. Borrowing and lending frictions are temporarily excluded.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 19–34](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 9 — The locked payoff equation

The foreign units purchased are 100/E. Foreign interest increases them by 1+R_foreign. The forward converts at F. Equal matched riskless returns follow from replication. This is a price relation under executable funding and hedge contracts, not an exchange-rate forecast.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 19–34](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 3–8](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 10 — A complete covered-parity calculation

EUR is the home currency. USD has the higher deposit rate, but the forward conversion exactly removes the apparent extra covered return. Each arrow is a cash-flow step, not an assumed future spot rate. The equality is rounded. Real conventions use appropriate day counts, tenors and bid/ask quotes.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 19–34](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 11 — Why covered parity can show a basis

A cross-currency basis reflects a wedge relative to a chosen funding benchmark. Define the exact convention before signing it. Post-crisis evidence relates deviations to hedging demand and limits on arbitrage. Credit and collateral differences must be controlled before attributing every gap to the same mechanism.

Reference: [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 5–8](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [BIS, FX hedging demand and costly balance sheets](https://www.bis.org/publications/working-paper-590-failure-covered-interest-parity-fx-hedging-demand-and-costly-balance-sheets). [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 12 — Uncovered returns and carry

State the question for this section, then ask the group for a prediction before showing the following example.

Reference:  [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 13 — The unhedged foreign payoff

The investment buys foreign deposits and converts the future proceeds at whatever spot rate occurs. Its home return is random even when the foreign deposit payoff is certain. A forward hedge replaces E_{t+1} with a fixed contractual F and changes the economic exposure.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 19–28](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 14 — Uncovered interest parity is an equilibrium assumption

This approximate UIP relation uses the home-per-foreign quote and small rates/FX changes. It is not a no-arbitrage identity because the foreign-currency payoff is risky in home units. Risk-neutral investors, or perfect-substitute assets with no required currency risk premium, can justify it within a model. Empirically UIP is not a reliable standalone forecasting rule.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 26–34](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 9–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 15 — Currency risk premium

This slide defines the sign convention for rho. Positive rho means investors require an expected return advantage from home assets over the converted foreign deposit. Other books define the foreign-asset premium instead, reversing the sign. Belief errors and time variation also matter in tests of UIP.

Reference: [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 9–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 16 — Carry: borrow yen and invest dollars

These are invented one-year rates and quotes. This is a zero-initial-net-investment financed position before margin and fees, so do not describe its P&L divided by zero capital as a finite return on equity. Use yen P&L or normalise by the 150 yen borrowing.

Reference: [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 12–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 17 — A small interest gain can meet a large FX loss

At an unchanged exchange rate the gain is 6 yen, equal to 4% of borrowed yen. With the yen stronger at 135, the loss is 9.75 yen, or 6.5% of the borrowing. The interest advantage does not cover the currency loss. Collateral, stop-outs and financing can make the realised path important too.

Reference: [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 12–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 18 — The carry payoff depends on the exit exchange rate

Show how a fall of only about 3.81% in JPY per USD erases this one-year interest advantage. This is a linear payoff in the future quote, rather than a historical return series. Carry profits in data can coexist with risk premia, crash exposure and distorted expectations.

Reference: [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 12–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 19 — Crash risk can hide behind frequent small gains

The average is positive yet exposure is highly asymmetric. A strategy can have many wins and still fail under leverage or funding stress. The numbers illustrate why average return alone does not prove arbitrage. Empirical carry behaviour is more complex than this two-state example.

Reference: [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 16–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 20 — Expectations and purchasing power

State the question for this section, then ask the group for a prediction before showing the following example.

Reference:  [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 21 — Short-run FX as an asset price

This follows from the exact expected-return equality with certain interest rates and a fixed expected future spot, ignoring a currency risk premium. Holding the expected future quote fixed is crucial. The home quote falls when the home rate rises. No claim is made that observed hikes always appreciate the currency.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 26–33](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 22 — A short-run FX return diagram

An expected foreign payoff of 1.02 foreign units converts at expected future quote 1.10. Paying a lower current E means buying that payoff more cheaply, so its expected home return rises. Raising the home rate from 5% to 7% moves the intersection from E≈1.0686 to E≈1.0486: home appreciation. Expected FX and the premium are held fixed; the curve is not a forecast regression.

Reference: [KOM, 12th Global Edition, ch. 14, printed pp. 397–404](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 23 — The rate and expectation experiments

In the approximate premium model E_t≈E_t^e/[1+R_home−R_foreign−rho], so higher rho weakens the home currency for fixed interest rates and future expected quote. This separates an attractive yield caused by policy restraint from one compensating for currency risk. The direction is conditional, not empirical certainty.

Reference: [Sergeyev, Bocconi 30054, lecture 4, PDF pp. 29–33](https://drive.google.com/file/d/1witR08GiCkzxTwhiX9EBp3G-1FURosQ0/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 16–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 24 — Purchasing power parity

Absolute PPP equates the domestic-currency prices of matched baskets. Law of one price applies to an individual freely traded identical good under strong assumptions; PPP extends an aggregation argument to baskets. Taxes, transport, services and market power create wedges. PPP is not an arbitrage trade in a nontradable consumption basket.

Reference: [Sergeyev, Bocconi 30054, lecture 8, PDF pp. 5–8](https://drive.google.com/file/d/1An0jjGV5noqQjT5vcTD12ASkXcbzXTSI/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 9, PDF pp. 3–12](https://drive.google.com/file/d/1J5xp1sfMmCsNPD6CE9iBpIozd88zey9t/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 25 — Why a cheap haircut is hard to arbitrage

This is a concrete reason PPP can fail even when the exchange-rate quote is correct. Tradable goods also face distribution costs and pricing-to-market. An apparently undervalued currency from a basket comparison need not be mispriced or due to converge soon.

Reference: [Sergeyev, Bocconi 30054, lecture 9, PDF pp. 3–12](https://drive.google.com/file/d/1J5xp1sfMmCsNPD6CE9iBpIozd88zey9t/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 26 — Productivity and local service prices

The Balassa–Samuelson mechanism assumes competitive tradables with the law of one price, domestic wage equalisation and similar service productivity. Higher tradable productivity supports higher wages, raising the price of local services. Overall price-level differences can therefore be equilibrium outcomes rather than simple currency misvaluation.

Reference: [Sergeyev, Bocconi 30054, lecture 9, PDF pp. 19–26](https://drive.google.com/file/d/1J5xp1sfMmCsNPD6CE9iBpIozd88zey9t/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 10, PDF pp. 3–10](https://drive.google.com/file/d/1kpvEx_ifI3P6sfh3K3cZPkyzV0KyqfEH/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 27 — The real exchange rate

The baskets and price-index bases must be specified. q=1 is meaningful only for genuinely matched baskets and compatible units. An index normalised to 100 does not make purchasing power equal at its base date. For log changes, Δlnq=ΔlnE+pi_foreign−pi_home.

Reference: [Sergeyev, Bocconi 30054, lecture 10, PDF pp. 12–18](https://drive.google.com/file/d/1kpvEx_ifI3P6sfh3K3cZPkyzV0KyqfEH/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 28 — Relative PPP and the Fisher effect

Relative PPP assumes a stable long-run real exchange rate. Fisher says nominal rates combine real returns with expected inflation. Together these show why high nominal yields can accompany long-run depreciation, unlike a short-run policy surprise with future FX expectations fixed. Relative PPP is an economic benchmark, not a precise short-horizon prediction.

Reference: [Sergeyev, Bocconi 30054, lecture 8, PDF pp. 8–18](https://drive.google.com/file/d/1An0jjGV5noqQjT5vcTD12ASkXcbzXTSI/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 29 — Real interest differences and real FX expectations

Combine Fisher approximations with the premium definition and q=E Q_foreign/Q_home. Under expected relative PPP, expected Δlnq is zero; only with zero rho do real rates then coincide. This avoids treating global real-interest parity as an unconditional identity. Superscript home/foreign labels refer to the matched real returns here.

Reference: [KOM, 12th Global Edition, ch. 16, printed pp. 480–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 30 — Dornbusch overshooting

State the question for this section, then ask the group for a prediction before showing the following example.

Reference:  [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 31 — A permanent monetary level shock

Distinguish a one-off level increase from permanently faster money growth. Assume stable money demand, foreign conditions and long-run real exchange rate. A one-off level shock raises the eventual price level and nominal exchange rate in proportion under the model, but does not permanently raise inflation.

Reference: [Sergeyev, Bocconi 30054, lecture 7, PDF pp. 14–28](https://drive.google.com/file/d/1K3Oi65qIJ45h_myuee0MRHowOwnMrEfb/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 32 — Prices adjust slowly

The exact time path is invented to illustrate sticky prices, not estimated or a solved calibration. Initially the price index has not moved, so real money supply rises. That lowers the home short rate in the classic money-demand model. As prices catch up, the real-money effect fades.

Reference: [Sergeyev, Bocconi 30054, lecture 7, PDF pp. 25–28](https://drive.google.com/file/d/1K3Oi65qIJ45h_myuee0MRHowOwnMrEfb/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 33 — The exchange rate can overshoot

With the domestic rate temporarily below foreign rates, UIP requires expected home appreciation to equalise expected returns. The spot exchange rate must therefore be weaker than its eventual level. This hypothetical path demonstrates the sign and timing, not a numerical forecast or fully calibrated joint solution. Short-run and long-run comparative statics alone would miss the overshoot.

Reference: [Sergeyev, Bocconi 30054, lecture 7, PDF pp. 25–28](https://drive.google.com/file/d/1K3Oi65qIJ45h_myuee0MRHowOwnMrEfb/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 34 — The overshooting mechanism

Tell the chain in both directions. If the currency only jumped to its long-run level immediately, the low-yielding home asset would lack the appreciation needed under UIP. A risk-premium change or a different policy path could change this result. Overshooting is a model implication under stated assumptions, not a rule that every currency move must reverse.

Reference: [Sergeyev, Bocconi 30054, lecture 7, PDF pp. 25–28](https://drive.google.com/file/d/1K3Oi65qIJ45h_myuee0MRHowOwnMrEfb/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 35 — Exercise: three explanations for a high yield

Ask for a conditional currency response and the evidence that would distinguish the cases. A gives near-term appreciation in the fixed-expectation model. B can raise nominal yields and expected depreciation. C can coincide with immediate weakness despite the high yield. A correct rate forecast need not be a correct FX forecast.

Reference: [Sergeyev, Bocconi 30054, lecture 5, PDF pp. 16–17](https://drive.google.com/file/d/1LfEQIo-QrncbVtc88G2yu5bLUYo-LEMT/view?usp=drivesdk) [Sergeyev, Bocconi 30054, lecture 8, PDF pp. 9–18](https://drive.google.com/file/d/1An0jjGV5noqQjT5vcTD12ASkXcbzXTSI/view?usp=drivesdk) [KOM, 12th Global Edition, ch. 14–16, printed pp. 381–482](https://drive.google.com/file/d/1-UaatD4D8-K1UynWK7AkRZ2fAZ3y04mI/view). PDF page = printed page + 1 in the supplied copy.

## Slide 36 — Further reading

Read the relevant sources after the lecture rather than before a first encounter. The course source map records what was retained, simplified or placed in optional material.

Reference: See [source_map.md](../../docs/source_map.md) and syllabus.md.

