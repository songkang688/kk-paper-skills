# FnyPro-1 Stage 00 Wave 3 — Agent G Cleaning Log (shard 1)

Agent: Wave 3 Agent G (text cleaner, shard 1). Stage 00 only; no Style DNA written; no sub-agents spawned.

Scope: 7 assigned Paper_IDs (01, 05, 07, 08, 12, 16, 31). All 7 examined and cleaned; none skipped.

Outputs:
- `fnypro1/stage00/wave3/G/clean_corpus/<Paper_ID>.md` (7 files)
- `fnypro1/stage00/wave3/G/section_map_partial.csv` (anchors are line numbers `L<n>` in the corresponding clean_corpus file)
- this log

## Global cleaning policy (applied to all 7 papers)

1. **English only.** Content taken exclusively from `**Original:**` blocks of the bilingual readers. All Chinese translations, reader navigation tables, glossaries, and reading notes excluded. Chinese translations were consulted (not copied) only as a cross-check when reconstructing garbled equations.
2. **Headers/footers/front matter.** Running headers, page footers, venue/DOI lines, manuscript-received dates, corresponding-author footnotes, and e-mail lines stripped. Funding footnotes kept only when they are the paper's de facto acknowledgment (papers 08, 31).
3. **Dual-column disorder.** Logical reading order reconstructed by rejoining sentence fragments split across columns/pages. Unrecoverable gaps marked inline with `[...]` rather than invented text.
4. **Broken formulas.** Fragmented or font-corrupted equations reassembled from context and standard forms; every reconstructed equation is flagged inline with an HTML comment asking for PDF verification. No formula content was invented where the fragments gave no basis; such spots are marked as lost.
5. **References.** Retained only when the extraction was verbatim (papers 16, 31 — reflowed one entry per line). Excluded with an explanatory stub when reader-condensed, truncated, or line-interleaved with body text (papers 01, 05, 07, 08, 12).
6. **Captions vs. body.** Figure/table captions segregated into a trailing appendix in every paper. Raw numeric table rows that leaked into body blocks were excluded (values live in the PDF tables).
7. **Authorial style preserved.** Original grammar quirks and typos kept verbatim (they are style signal for later stages); only unambiguous extraction artifacts fixed (split words, ligature debris, spacing like "20 04", garbled glyphs). Every such fix is listed in the header comment of the paper's clean file.
8. **Provenance.** Each clean file opens with an HTML comment recording source, exclusions, fixes, and preserved quirks, keyed to source block IDs (S###) from the readers.

## Per-paper notes

### 01_WaveShaped_TIP2020_Smoke_Density_Estimation
- Issues: venue header lines, drop-cap, reader-condensed reference list, condensed author bios, caption/body mix.
- Actions: headers stripped; captions to appendix; references and bios excluded (non-verbatim, S109–S111 flagged uncertain by the reader); equations reformatted. A superlative-comparative phrase and other authorial wording preserved.
- Canonical gaps: Discussion missing (folded into Section V subsections); Acknowledgments absent from extraction.

### 05_NewtonInterpolation_PR2025_smoke_semantic_segmentation
- Issues: severe two-column interleaving, fragmented equations, reference list interleaved line-by-line with Conclusions and bios, numeric table rows in body.
- Actions: reading order rebuilt; equations (1)–(18) reassembled with lost superscripts restored (flagged); references excluded (S077–S081 unreliable); OCR splits fixed (e.g. spaced-out words, "state-ofthe-art").
- Canonical gaps: Discussion missing. Elsevier back-matter (CRediT, Declaration, Data availability) mapped to Other.

### 07_CGRNet_TIP2021_Gated_Recurrent_Smoke_Semantic_Segmentation
- Issues: split title/byline, drop-cap artifact, column truncation, heavily garbled GRU and loss/metric equations, truncated reference list.
- Actions: title reconstructed; equations (1)–(11) rebuilt from fragments (flagged, verify against PDF); `[...]` markers where text is lost; references excluded (only [1]–[13] extracted, S094–S095 flagged uncertain).
- Canonical gaps: Discussion missing; Acknowledgments absent; subsection IV.D heading lost in extraction (headings jump C→E) — content partially lost, flagged.

### 08_Deep_Smoke_Segmentation_Neurocomputing2019
- Issues: preprint layout with Introduction/RelatedWork interleaving, one duplicated paragraph, manuscript/funding text glued into intro, shattered equations, captions glued into body, references interleaved with the Limitations subsection.
- Actions: deduplicated; body text recovered from caption blocks; equations (5)–(8) reconstructed (flagged); references excluded (S091/S094/S095 unreliable).
- Canonical gaps: Discussion merged — the "Limitations" subsection inside Results serves as discussion (recorded in CSV).

### 12_CNN_Transformer_Complementary_PR2023_Medical_Segmentation
- Issues: one swapped introduction paragraph (S009 before S008, detected via citation order), five cross-page sentence joins, subsection titles glued into paragraphs, fragmented equations, ligature/hyphenation artifacts.
- Actions: paragraph order restored; glued headings split out; equations (1)–(7), (10), (12)–(14) reconstructed (flagged); references excluded (reader states full entries are PDF-only); author bios retained in appendix with two OCR spacing fixes. Recurring authorial typo ("long-rang") preserved.
- Canonical gaps: Results and Discussion merged under the original heading "4. Experiments and discussion" (recorded in CSV).

### 16_MultiScale_MultiOrder_IS2018_Smoke_Recognition
- Issues: headings glued into preceding paragraphs, a garbled equation reference with the formula content lost, missing "4.1"/"4.1.1" headings, running headers, embedded numeric table data, several cross-page joins.
- Actions: headings unglued; equations (1),(2),(4),(5),(7),(9)–(12),(14) reconstructed (flagged); missing headings noted as inferred; references RETAINED verbatim and reflowed; bios retained. Authorial typos ("Datesets", "Comparision") preserved; unambiguous OCR splits fixed.
- Canonical gaps: Discussion missing.

### 31_SubOriented_Histograms_LBP_KSII2016_Smoke
- Issues: single-column but with a fully glued header block (title/authors/affiliations/dates in one blob), font-encoding-corrupted equations on pp. 4–9 (doubled glyphs), table OCR dumps, figure-panel debris in body, bios glued to the reference tail.
- Actions: header disentangled; equations (1)–(6),(11)–(13) reconstructed (flagged); table dumps excluded (captions kept); front-page funding/preliminary-version footnote kept as the paper's acknowledgment (typo "extanded" preserved); references RETAINED verbatim and reflowed; bios unglued into an appendix. An in-text table-number likely-typo preserved and noted.
- Canonical gaps: no separate RelatedWork (survey folded into Introduction); Discussion missing.

## Cross-paper observations (for downstream agents; not style conclusions)

- Extraction quality clusters by publisher pipeline: the two KSII/Elsevier papers with verbatim reference lists (16, 31) also had the most legible body text; the IEEE TIP extractions (01, 07) consistently lost or condensed their reference lists.
- Font-encoding corruption of math (doubled/garbled glyphs) appears in the older papers (16, 31); the newer Elsevier papers (05, 12) instead show fragment-scatter of equations across blocks. All reconstructed equations are flagged inline and need one PDF verification pass.
- Recurring structural pattern in this shard: no standalone Discussion section in 6 of 7 papers (merged into Results or absent); only paper 12 declares the merge in its own heading.
- Author-biography blocks are the most contamination-prone region: glued to reference tails (31), reader-condensed (01), or interleaved with references (05).

## Items requiring next-agent resolution

1. PDF verification of all equations flagged "reconstructed" (papers 05, 07, 08, 12, 16, 31 — inline HTML comments mark each one).
2. Verbatim reference lists for papers 01, 05, 07, 08, 12 must be sourced from the PDFs if needed downstream (excluded here as non-verbatim).
3. Paper 07 subsection IV.D: heading and part of the content lost in extraction; needs PDF recovery.
4. Paper 16: confirm the inferred "4.1"/"4.1.1" heading titles against the PDF; recover the lost formula referenced as Eq. (13).
5. Paper 31: truncated sentence in the smoke-detection results (marked `[...]`) needs PDF recovery.
