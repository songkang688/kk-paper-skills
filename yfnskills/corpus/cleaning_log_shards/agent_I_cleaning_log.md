# FnyPro-1 Stage 00 Wave 3 — Agent I Cleaning Log (shard 3)

**Agent:** Wave 3 Agent I (text cleaner, shard 3)
**Scope (8 Paper_IDs):** 02, 03, 04, 09, 10, 13, 19, 21 (full stems below)
**Outputs:** `wave3/I/clean_corpus/<Paper_ID>.md` (8 files), `wave3/I/section_map_partial.csv`, this log.
**Constraint applied:** Stage 00 only; no Style DNA written. Tier B papers 09 and 10 were cleaned but no style claims were made about them.

## Method

1. Each raw `/workspace/<STEM>.md` is a bilingual "reader" export: per-sentence blocks with an anchor ID, page number, an `Original:` English block, a Chinese translation block, and `Source:` lines. A parser (`/tmp/agentI/parse_reader.py`) extracted English-only blocks with their IDs/pages into `/tmp/agentI/parsed/<STEM>.txt`, stripping NUL bytes (papers 04 and 13 contained 2 NUL bytes each, both inside already-broken formula blocks; nothing else was lost).
2. Reading order, section structure, equations, captions and references were then manually reconstructed per paper. All anchors cited below and in the CSV are block IDs (Sxxx = sentence/paragraph blocks, Cxxx = caption blocks, Fxxx = figure anchors) from the parsed files.
3. Clean files use: H1 title + metadata lines; H2 = canonical section (Title, Abstract, Introduction, RelatedWork, Methods, Results, Discussion, Conclusion, Acknowledgments, References, Other); H3/H4 = original headings/subheadings; blockquotes (`>`) = figure/table captions; inline `[NOTE: ...]` = reconstruction/uncertainty flags. No Chinese text remains in any clean file (verified by grep for CJK codepoints).

## Per-paper log

### 02_CCENet_PR2022_Cubic-cross_convolutional_attention_smoke_segmentation
- Cleanest paper of the shard: all numbered headings survived as anchors.
- Fixed: heading normalization (1./2./3.1.1 etc. under canonical H2), captions to blockquotes, contribution list re-split.
- References: source contains a condensed summary block (S100) instead of itemized entries; preserved verbatim with a note rather than inventing entries.
- Declaration of Competing Interest and author biographies moved to Other.

### 03_Lightweight_PR2023_smoke_semantic_segmentation
- Severe dual-column disorder. Keywords block glued to "1. Introduction" (S004). Almost no real heading anchors survived; four "headings" were formula debris (S040/S043/S046/S053).
- Introduction/RelatedWork rebuilt by re-ordering interleaved fragments; contribution list re-split.
- Methods: Eqs. (1)–(8) reassembled from fragments; reconstruction flagged inline where the source was ambiguous.
- Results: loss-weight ablation table truncated in source; only confirmed values included, truncation flagged.
- Conclusions (5.) was interleaved line-by-line with reference entries inside S074; both were disentangled. References itemized individually. Co-first-author footnote (S007), Declaration, and bios moved to Other.

### 04_SAGINN_TIP2024_Smoke_Semantic_Segmentation
- Contained 2 NUL bytes (inside broken formula blocks) — read directly, not skipped.
- Drop-cap artifact "I. INTRODUCTION F" + "IRE" normalized. Contribution-like text mixed into Related Work reordered.
- Methods III (A–E): Eqs. (1)–(17) reassembled from scattered fragments (false-heading debris S033/S035 were pieces of Eq. (4)); flagged inline.
- References: 72 entries reconstructed from a two-column interleave that also mixed author-biography text; bios moved to Other.

### 09_MultiStage_GroupInteraction_TIP2026_Realtime_Smoke_Segmentation (Tier B)
- Intro paragraph order restored (S007→S008→S012→S013→S014→S015+S009→S010→S011). Mid-sentence truncation after "including DSS" (S007) flagged — the model enumeration after it is missing from the extraction.
- Related Work A/B/C headings were glued mid-block; subsection B's closing text was spliced into S023 with C's closing text — untangled.
- Methods: every displayed equation (1)–(22) was fragmented at column breaks; reassembled (1D DFT/iDFT normalization factors appeared only as bare "1" — noted). C004 was body text mislabeled as a caption (Section III overview).
- Results: C011 was body text (Fig. 9 analysis). TABLE VI caption garbled ("...DIFFERENT SSmoke SEGMEN...TATION METHOD") — reconstructed with note. Conclusion future-work paragraph recovered from a block glued to the TABLE VII caption (S078).
- References: 50 entries; [12]–[50] two-column interleaved. The seam between [14] "A lightweight network for..." / [33] AOSVSSNet / [34] VTrUNet was ambiguous; resolved using the body text (VTrUNet [34] = LandSat imagery) and noted inline. [35] ENet's venue fragment ("Proc. CVPR, Jun. 2016") is suspicious (ENet is an arXiv preprint) — transcribed as recovered with note.
- Duplicated caption prefixes ("Fig. 1. Fig. 1.") deduplicated. Chinese caption anchors (F010/F011) replaced by the English caption text that was present in C012/C013. No style claims made (Tier B).

### 10_FrequencySpace_TCE2025_Lightweight_Smoke_Segmentation (Tier B)
- S010 was a duplicated copy of the first Introduction paragraph glued to Kang Li's affiliation footnote (first-page header/footer artifact): duplicate dropped, footnote moved to Other.
- Related Work C's paragraphs were split across S023/S027/S021/S022 (out of page order) — reassembled.
- Methods: Eqs. (2), (4), (10)–(15) fragmented; reassembled with inline notes (2D DFT/iDFT form; GMDF per-channel group extraction; HFAM gated fusion). C003 was body text mislabeled as a caption (Section III-A overview).
- Results: loss-function text (Section III-E) and experiment text (IV-A/B/C) were interleaved within single blocks (S043/S044/S046/S050) — re-sorted into their sections. Real-time analysis paragraphs were interleaved with reference blocks (S084/S085) — extracted back into IV-F.
- Conclusion split across S088+S079+S080 with the limitation paragraph glued to the TABLE VII caption (S081) — reassembled.
- References: 56 entries reconstructed from two-column interleave that also contained body text. Venue oddities preserved as printed with notes ([24] EfficientNet page range "10578–11247"; [47] "Int. Conf. Learn. Reinforcement"). No style claims made (Tier B).

### 13_BiDirectional_BoundaryAware_TIP2024_Skin_Lesion_Segmentation
- Contained 2 NUL bytes (inside the shattered Bi-AG equation blocks) — read directly, not skipped.
- Structure largely intact (all headings survived), but equations were the worst in the shard: Eqs. (3)–(5) were shattered into ~15 one-token blocks (S047–S064: "ϕc (xCNN) h1 = LN", "Reshape", "Down", "α = σ", "ReLU", ...). Reassembled following the alignment procedure described in the surrounding prose and the standard additive attention-gate form; the exact nesting order in Eq. (3) is a best-effort reconstruction, flagged inline.
- Eq. (8) reverse-attention argument lost at a column break — reconstructed as σ(UP(P_{i+1})) per the standard formulation, flagged.
- Eqs. (13)–(14) scrambled (ACC numerator order; Dice denominator contained "TN") — normalized to standard metric definitions with a note.
- Internal inconsistency preserved as printed and noted: Section III-C overview assigns P6 to the CNN decoder and P5 to the PD, but the PD subsection says the PD produces P6.
- "BiFBP-Net" typos preserved as printed (noted). Duplicated captions (C00x duplicating F00x English captions) deduplicated; Chinese anchor headings replaced by the English [CAPTION] text present in the source.
- References: the source markdown contains ONLY a placeholder ("[1]–[N] Full bibliographic entries appear in the PDF"). Stub note kept; entries were NOT invented. In-text citations [1]–[72] remain resolvable only against the original PDF.
- Author biographies moved to Other.

### 19_HighOrder_LTP_IS2016_Smoke_Detection
- Methods: LBP/LTP equations reconstructed from scrambled fragments; Eqs. (6), (7), (12) were missing from the extraction and reconstructed from the standard LTP formulation, flagged. C004 was body text belonging to S038 and merged back.
- Results: "4.1" heading absent (setup text glued under "4. Experiments"); the glued in-text heading "4.2. Experimental results for smoke detection" was trusted over the shorter anchor variant. A formula missing its π symbol transcribed as-is and flagged.
- References separated from interleaved author-bio text and itemized; bios moved to Other.

### 21_LBP_LBPV_FireSafety2011_Video_Smoke_Detection
- Cleanest structure: sections 1–7 intact; formulas clean.
- Nonstandard top-level sections 2–4 (LBP / Histogram sequence / Classification) all mapped to canonical Methods. This paper has a genuine standalone "6. Discussion" — the only paper in the shard where Discussion and Conclusion are separate authored sections.
- No separate Related Work: literature survey lives in 1.1/1.2 and was kept under Introduction.

## Cross-paper observations (structural only — no style claims for Tier B 09/10)

- All eight are single- or two-column reconstructions; the IEEE papers (04, 09, 10, 13) suffer column-break equation fragmentation; the Elsevier papers (02, 03, 19, 21) fare better except 03 and 19.
- Recurrent extraction failure modes: (a) glued section titles at block starts ("A. Smoke Detection Early smoke detection..."); (b) body paragraphs mislabeled as figure captions (C004 in 09, C003/C011 in 10, C002 in 13, C004 in 19); (c) two-column interleaved reference lists (04, 09, 10, and partially 03/19); (d) duplicated caption prefixes; (e) table contents absent everywhere (only captions survive).
- Boundary-aware weighted BCE+IoU loss with ω = 1 + ε·|AP31×31(G) − G| and ε = 5 appears verbatim in papers 09 and 10 (both cite F3Net); paper 13 uses a related weighted BCE+IoU hybrid. This is a topical/lineage fact, not a style claim.
- Venue/collaborator confound: papers 09 and 10 share authors (Kang Li, Feiniu Yuan, Chunmei Wang) and heavily overlapping reference lists; 02/03/04/13/19/21 also share Feiniu Yuan. Any downstream stylistic inference must control for this.
