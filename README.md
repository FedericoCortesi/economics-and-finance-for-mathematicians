# Economics and Finance for Mathematicians

An evolving course for mathematicians learning economics, finance and markets. The lectures build intuition through models, original diagrams, worked examples and trading questions, with every important assumption stated explicitly.

The current seven modules start with macroeconomics and move through bonds, foreign exchange and sovereign risk. Future lectures will expand the asset-pricing and finance material. The course is not limited to a fixed number of classes.

[Syllabus](syllabus.md) · [Complete slide deck](dist/economics_and_finance.pdf) · [Instructor notes](docs/instructor_notes.md) · [Sources](docs/source_map.md)

![Credit, investment and household spending: an original AI-generated teaching illustration](assets/money_bakery.png)

## Current lectures

| Class | Slides | Pages | Speaker notes |
|---|---|---:|---|
| 1 | [Output, income and capital flows](lectures/lecture_01/lecture_01.pdf) | 42 | [Notes](lectures/lecture_01/notes.md) |
| 2 | [Money, inflation and activity](lectures/lecture_02/lecture_02.pdf) | 86 | [Notes](lectures/lecture_02/notes.md) |
| 3 | [Bonds and yield curves](lectures/lecture_03/lecture_03.pdf) | 37 | [Notes](lectures/lecture_03/notes.md) |
| 4 | [Foreign exchange](lectures/lecture_04/lecture_04.pdf) | 36 | [Notes](lectures/lecture_04/notes.md) |
| 5 | [Open-economy policy and regimes](lectures/lecture_05/lecture_05.pdf) | 38 | [Notes](lectures/lecture_05/notes.md) |
| 6 | [Currency crises and the euro](lectures/lecture_06/lecture_06.pdf) | 28 | [Notes](lectures/lecture_06/notes.md) |
| 7 | [Public debt and macro trades](lectures/lecture_07/lecture_07.pdf) | 42 | [Notes](lectures/lecture_07/notes.md) |

The modules contain more material than a single short talk. The syllabus gives 25–30-minute routes, optional extensions and suggested questions. Lecture 1 develops production, income and external accounts. Lecture 2 introduces rates, inflation, money and IS–LM before the dedicated bond-pricing module.

## Repository layout

```text
lectures/lecture_01/   LaTeX source, PDF and notes for Lecture 1
lectures/lecture_02/   The same structure for each lecture through 07
assets/               Shared illustrations and their credits
data/                 Frozen source tables for empirical charts
docs/                 Source map, combined notes, outline and image prompts
theme/                Shared Beamer theme
dist/                 Combined course PDF
scripts/              PDF assembly
reference_courses/    Local reference links and materials (Git-ignored)
```

Each lecture folder contains `lecture_XX.tex`, `lecture_XX.pdf` and `notes.md`. `syllabus.md` remains at the top level as the course entry point. Local reference links are intentionally absent from a fresh clone.

## Editable sources and build

Each lecture has an editable Beamer `.tex` source, a compiled PDF and slide-indexed speaker notes. `theme/course_theme.tex` provides the shared typography and palette. Charts and economic diagrams remain editable LaTeX/TikZ. The combined PDF has bookmarks for each class and section.

To build all seven PDFs and the combined deck, install a TeX distribution with pdfLaTeX, Beamer, Latin Modern, booktabs, array, graphicx and TikZ, plus Python 3 and pypdf:

```sh
python3 -m pip install -r requirements-build.txt
sh build.sh
```

Run the build from the repository root. The build runs locally without fetching market data. Intermediate TeX files stay in `.build/`. The published PDFs are already available above.

## Sources, illustrations and dated data

Krugman, Obstfeld & Melitz, *International Economics: Theory and Policy*, and publicly referenced Bocconi International and Monetary Economics materials guide the international-macro sequence. [The source map](docs/source_map.md) records editions, chapters, page mappings and source URLs. The repository contains original teaching materials; downloaded textbook files and third-party lecture decks are not distributed here.

Examples and unlabelled model curves are hypothetical. Empirical charts use frozen CSV snapshots with observation dates, units and source URLs. Those snapshots describe their stated dates and are not live market views. The notes distinguish accounting identities from causal models and short-run assumptions from long-run benchmarks.

The four teaching illustrations were generated with OpenAI's image-generation tool and depict invented settings. [Image credits](assets/credits.md) and [full prompts](docs/image_prompts.md) document their provenance.

Prepared by Federico Vittorio Cortesi. This course is a work in progress.
