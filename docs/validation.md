# Delivery checks — 15 October 2026

309 slide pages across seven modules. All pages were rendered and visually reviewed. Changed pages were rendered again after the final layout edits.

- Class 1: 42 pages; editable source, compiled PDF and slide-indexed notes agree.
- Class 2: 86 pages; editable source, compiled PDF and slide-indexed notes agree.
- Class 3: 37 pages; editable source, compiled PDF and slide-indexed notes agree.
- Class 4: 36 pages; editable source, compiled PDF and slide-indexed notes agree.
- Class 5: 38 pages; editable source, compiled PDF and slide-indexed notes agree.
- Class 6: 28 pages; editable source, compiled PDF and slide-indexed notes agree.
- Class 7: 42 pages; editable source, compiled PDF and slide-indexed notes agree.

All seven decks compile with pdfLaTeX without errors or overfull boxes. The combined PDF preserves class and section bookmarks. Representative calculations were independently recomputed: project NPV, bond prices, IS–LM intersections, covered parity, carry P&L, DV01 sizing, trade values and exact debt-ratio changes. Frozen summer data contain no duplicate series/date rows; the FX cross-rate arithmetic is consistent.

Market observations retain dates and official source URLs. Native yield conventions and local observation times differ across jurisdictions; no causal capital-flow claim is inferred from their co-movement. Textbook and course figures were used for reference; the delivered plots, examples and teaching illustrations are original.

## GitHub publication

The course title is Economics and Finance for Mathematicians. All seven decks were rebuilt, and all seven updated title slides were rendered and checked. Slide content and page counts are otherwise unchanged. The shared theme is now `../theme/course_theme.tex`; the combined deck is `../dist/economics_and_finance.pdf`. The public build script also regenerates the combined deck and bookmarks. Third-party textbook and reference lecture files, build logs, local archives and ZIP bundles are excluded from Git.

## Folder reorganization

Every lecture now has a source, PDF and notes under `lectures/lecture_XX/`. Shared files are grouped into `assets/`, `data/`, `docs/` and `theme/`; the combined PDF is in `dist/`. All seven sources rebuilt successfully with the updated paths and no overfull boxes or LaTeX errors. All 309 page texts matched the preceding version, and the published PDFs retain their preceding byte-identical contents. Markdown file links were checked. The local `reference_courses/` folder is excluded by `.gitignore`; its finance-course links are not part of the public files.
