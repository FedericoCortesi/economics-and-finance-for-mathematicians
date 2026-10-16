# Lecture 2 — review map

The revised deck has **86 slides**. This table maps the annotated 69-slide version to the revised pages. The LaTeX remains editable, and the speaker notes follow the new numbering.

| Original page / comment | Revised page(s) | What changed |
|---|---:|---|
| 4 / comment 5 | 6–7 | General ZCB discount formula, face value 100, worked price and inverse price/yield curve. |
| 5 / comments 1–4 | 8 | Removed the separate loan-rate row. Uses i for nominal, r for real, and ī for the chosen policy target, as confirmed. |
| 7 / comment 6 | 9–11 | Separates exact realised purchasing power, exact logarithms, first-order Fisher approximation and expected inflation. |
| 7 / comment 7 | 13–17 | Saving/investment equilibrium, the real benchmark, a long-run Fisher plot and the distinction from short-run policy causality. |
| 9 / comment 8 | 13–15 | Replaces the vague statement with numerical saving and investment curves, a larger-harvest example and better-projects example. |
| 10 / comment 9 | 18–20 | Answers where extra money comes from: a supply shortfall needs none; bank money creation and faster turnover are other channels. |
| 20 / comment 10 | 30–31 | Explains routine short-rate implementation and exceptional long-yield targeting, illustrated by the BoJ’s 2016 policy. |
| 22 / comment 11 | 33–34 | Shows why purchasing power M/P matters for transaction liquidity. Distinguishes this stock from output over a period. |
| 23 / comment 12 | 35, 52 | Conventional money-market axes M/P and i, plus a money-demand shift. |
| 25 / comment 13 | 37 | Physics analogy, derivatives, intersections and shifts. Quantitative functional-form choices remain explicit assumptions. |
| 38 / comment 14 | 49–52 | Who chooses the monetary setting, portfolio adjustment via bond sales, and the positive LM derivative. |
| 42 / comment 15 | 72–76 | Rate-target alternative moved to the end of the core lecture, together with all experiments that depend on it. |
| 53 / comment 16 | 65 | Explicitly a possible Taylor-style rule a central banker might follow. |
| 54 / comment 17 | 66–67 | Original Phillips relationship and expectations-shift plot retained. |
| 50 / comment 18 | 61–62 | Adds the US post-Covid inflation/policy chart immediately after the catch-up example. |

## Opening additions

- **Slide 2:** a short-run/long-run caveat before any model. The standard long-run benchmark has a zero output gap, with no fixed calendar duration. Results depend on which prices, quantities and expectations can adjust. Real shocks can move potential output and the neutral real rate.
- **Slide 3:** an original AI-generated illustration connects bank credit, investment in a bakery oven and household spending. The saved asset and full prompt are in `../assets/money_bakery.png` and `image_prompts.md`.
- The preceding 84-slide content is retained in the same order. All its page numbers after the title move forward by two.

## Notation

- **i:** nominal market rate; **r:** real rate; **ī:** chosen policy target; **r\*:** neutral/full-employment real benchmark.
- **P:** aggregate price level in this deck. The ZCB price is **p₀**; **F=100** is face value.
- Classic fixed-money IS–LM solves for market i. Under rate targeting, the policy line implements i=ī for the stated experiment. The common theme and other lectures are unchanged.

## Data and theory distinctions

The post-Covid chart uses BLS CPI and the Federal Reserve target upper bound via FRED, January 2020–September 2026, retrieved 15 October 2026. It uses trailing 12-month CPI inflation and month-end policy observations. October 2025 CPI is missing in the source and is left as a gap. Observed inflation is not expected inflation, so the difference between these lines is not an ex ante real rate. Inputs and transformations are frozen in `../data/us_inflation_policy_2020_2026.csv`.

The textbook references are ch. 16, printed pp. 459–462 and 480–482 (Fisher and short/long run), ch. 19, pp. 647–648 (saving/investment equilibrium), and ch. 15, pp. 423–426 (real money balances and money-market adjustment). Full URLs are in `source_map.md` and the slide-indexed notes.
