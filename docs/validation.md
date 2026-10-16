# Delivery checks — 16 October 2026

370 slide pages across seven teaching modules. The revised Lecture 3 has 98 pages, with matching editable Beamer source, slide-indexed notes and course outline. Its six short-meeting routes are in the syllabus and reading list.

## Lecture 3 revision

- pdfLaTeX completed two final passes with no errors, warnings or overfull boxes.
- All 98 pages were rendered to PNG and visually inspected. The final auction allocation edits were rendered and checked again. Formula, empirical-chart, supplied-image and Taylor-comparison pages were also inspected individually at full preview size.
- Independently recomputed zero/coupon prices, holding return, bootstrap discount factor, exact forward replication and hypothetical arbitrage payoff; auction allocation and bill day-count quotations; analytic duration/convexity against finite differences; Taylor approximation errors; DV01 sizing and both trade scenarios; state prices and immunization weights.
- The 1,100 curve rows have unique series/date/maturity keys. Counts are 14 Treasury par tenors, 358 ECB par maturities, 349 monthly US zero points, 30 annual US source-grid zero points and 349 monthly EUR zeros. All continuous-to-annual conversions reconcile.
- The US Svensson evaluation reproduces all 30 published annual source quotes within 0.00011 percentage points. Fitted points are clearly distinguished from independent market observations.
- All 81 ACM monthly decompositions reconcile to their fitted yield. The 71 June Fed dots reproduce the official distribution and medians. Quote conventions, source dates and model assumptions remain explicit.
- Actual auctions are separated from invented allocation and when-issued examples. The supplied chart's incorrect BLS credit is corrected in its visible caption.
- Local Markdown links in the changed course entry points, reading list, revision map and Lecture 3 notes resolve.

## Course integrity and publication

| Module | Pages | Status |
|---|---:|---|
| 1 | 42 | Source, PDF and notes unchanged |
| 2 | 86 | Source, PDF and notes unchanged |
| 3 | 98 | Rebuilt and checked in this revision |
| 4 | 36 | Source, PDF and notes unchanged |
| 5 | 38 | Source, PDF and notes unchanged |
| 6 | 28 | Source, PDF and notes unchanged |
| 7 | 42 | Source, PDF and notes unchanged |

The other six modules' PDFs, sources and individual notes are byte-identical to the preceding published revision. Their earlier compile and visual checks remain applicable. The assembled 370-page PDF has class/section bookmarks, and every page's extracted text matches its standalone lecture counterpart. Representative combined pages were rendered as an assembly check.

The two finance courses were inspected privately. Their Drive links, downloaded reference decks/book text, raw research and the future Lecture 2 article backlog remain in `reference_courses/`, excluded by `.gitignore`. Only original teaching content, the explicitly requested supplied chart and processed public-source data are published. News prompts use verified accessible openings, with full-text/MIT-access limitations recorded in the reading list. The source ZIP excludes private references and build intermediates.

## Earlier course checks

Before this revision, all seven decks (309 pages) compiled and were rendered and reviewed. Representative macro, FX, debt and portfolio calculations were checked. The folder reorganization preserved those PDFs byte-for-byte and updated their build paths. This revision changes only the bond module and related course documentation/data, then reassembles the complete PDF.
