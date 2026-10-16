# Economics and Finance for Mathematicians

An evolving course for mathematicians learning economics, finance and markets. The lectures build intuition through models, original diagrams, worked examples and trading questions, with every important assumption stated explicitly.

The current seven modules start with macroeconomics and move through bonds, foreign exchange and sovereign risk. Future lectures will expand the asset-pricing and finance material. The course is not limited to a fixed number of classes.

[Syllabus](syllabus.md) · [Complete slide deck](economics_and_finance.pdf) · [Instructor notes](instructor_notes.md) · [Sources](source_map.md)

![Credit, investment and household spending: an original AI-generated teaching illustration](assets/money_bakery.png)

## Current lectures

| Class | Slides | Pages | Speaker notes |
|---|---|---:|---|
| 1 | [Output, income and capital flows](lecture_01.pdf) | 42 | [Notes](lecture_01_notes.md) |
| 2 | [Money, inflation and activity](lecture_02.pdf) | 86 | [Notes](lecture_02_notes.md) |
| 3 | [Bonds and yield curves](lecture_03.pdf) | 37 | [Notes](lecture_03_notes.md) |
| 4 | [Foreign exchange](lecture_04.pdf) | 36 | [Notes](lecture_04_notes.md) |
| 5 | [Open-economy policy and regimes](lecture_05.pdf) | 38 | [Notes](lecture_05_notes.md) |
| 6 | [Currency crises and the euro](lecture_06.pdf) | 28 | [Notes](lecture_06_notes.md) |
| 7 | [Public debt and macro trades](lecture_07.pdf) | 42 | [Notes](lecture_07_notes.md) |

The modules contain more material than a single short talk. The syllabus gives 25–30-minute routes, optional extensions and suggested questions. Lecture 1 develops production, income and external accounts. Lecture 2 introduces rates, inflation, money and IS–LM before the dedicated bond-pricing module.

## Editable sources and build

Each lecture has an editable Beamer `.tex` source, a compiled PDF and slide-indexed speaker notes. `course_theme.tex` provides the shared typography and palette. Charts and economic diagrams remain editable LaTeX/TikZ. The combined PDF has bookmarks for each class and section.

To build all seven PDFs and the combined deck, install a TeX distribution with pdfLaTeX, Beamer, Latin Modern, booktabs, array, graphicx and TikZ, plus Python 3 and pypdf:

```sh
python3 -m pip install -r requirements-build.txt
sh build.sh
```

The build runs locally without fetching market data. Intermediate TeX files stay in `.build/`. The published PDFs are already available above.

## Sources, illustrations and dated data

Krugman, Obstfeld & Melitz, *International Economics: Theory and Policy*, and publicly referenced Bocconi International and Monetary Economics materials guide the international-macro sequence. [The source map](source_map.md) records editions, chapters, page mappings and source URLs. The repository contains original teaching materials; downloaded textbook files and third-party lecture decks are not distributed here.

Examples and unlabelled model curves are hypothetical. Empirical charts use frozen CSV snapshots with observation dates, units and source URLs. Those snapshots describe their stated dates and are not live market views. The notes distinguish accounting identities from causal models and short-run assumptions from long-run benchmarks.

The four teaching illustrations were generated with OpenAI's image-generation tool and depict invented settings. [Image credits](assets/credits.md) and [full prompts](image_prompts.md) document their provenance.

Prepared by Federico Vittorio Cortesi. This course is a work in progress.
