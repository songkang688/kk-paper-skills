# FnyPro-1 Stage 00 Wave 3 — Agent H Cleaning Log (text cleaner, shard 2)

Agent: Wave 3 Agent H. Scope: 7 Paper_IDs (06, 11, 17, 18, 20, 30, 36 — full stems below).
Inputs: `/workspace/<STEM>.md` bilingual readers (English `**Original:**` blocks only; no Chinese text in any output).
Outputs: `wave3/H/clean_corpus/<Paper_ID>.md` (7 files), `wave3/H/section_map_partial.csv`, this log.
Method: scripted extraction of all `**Original:**` blocks with reader anchors + page numbers
(`/tmp/extract_originals.py`), then per-paper manual reconstruction. Zero CJK characters were found in
any extracted Original block (verified by script); the "Chinese contamination" in paper 18 manifests as
machine-translated reference text inside scrambled Original blocks, handled by exclusion (below).

Conventions used in all clean files:
- Canonical 11-section skeleton (Title, Abstract, Introduction, RelatedWork, Methods, Results,
  Discussion, Conclusion, Acknowledgments, References, Other) present in every file; absent sections
  carry an explicit absence note instead of invented content.
- Every paragraph carries an HTML comment with its source anchors (`src: SXXX`), including exact
  cross-block seams for reconstructed paragraphs.
- Suspected SOURCE typos are preserved as printed and flagged in comments (never silently corrected).
  Extraction/OCR artifacts (hyphenation breaks, missing spaces, glyph substitutions) ARE corrected.
- Table numeric rows and figure-diagram debris excluded as non-prose; captions kept caption-only.
- Garbled display equations: normalized when the intended form is unambiguous; otherwise flagged
  "refer to PDF" — never speculatively invented.

---

## 06_MIFNet_PR2025_multi-scale_interactive_fusion_smoke_segmentation (Tier A3, 0.75)

Extraction quality: HIGH. Reading order preserved; main defects were section-title glue and
table interruptions.

- Section-title glue: 14 headings unglued from body blocks (3.1.1, 3.1.2, 4.1.1, 4.1.2, 4.3.1–4.3.4,
  4.4.1–4.4.3, Declaration of competing interest, Acknowledgments, Data availability, References).
- Column/page-break merges: S023+S024, S030+S031, S034+S035, S046+S047, S059+S060, S066→S069,
  S070+S071, S074+S076, S082+S086, S088+S091, S094+S096 (duplicated lead-ins/overlaps resolved
  conservatively, noted in-file).
- Excluded table numeric rows: S067, S068, S075, S083–S085, S089, S090, S095.
- OCR fixes: "con centration"→"concentration", "envi ronments"→"environments", "SYN70 K"→"SYN70K",
  caption double periods ("Fig. 1. ."), "types:1)" spacing, stray periods after citation brackets.
- Garbled equations flagged (not reconstructed): Eqs. (2), (3), (4), (6).
- Known loss: final sentence of S016 truncated in extraction ("…Section 5 offers [truncated]").
- No standalone Discussion (noted); Results contains both experimental setup (4.1) and results
  (4.3/4.4) as source-distinct subsections.

## 11_Confidence_Prior_PR2021_Image_Dehazing (context: PR 2021, unnumbered headings)

Extraction quality: MEDIUM. Unnumbered headings, heavy caption/body mixing, many garbled equations.

- Large internal duplication in S011 (column re-read) removed.
- Body prose mislabeled as captions restored to body: C002, C004, C009, C011, C015, C016, C027.
- ~18 split-sentence seams merged (S034→S036 … S102→S105 series; documented in-file).
- Discussion/Conclusion merge resolved: S102 (Experiments tail) + S105 (limitations inside
  Conclusions, table-header debris removed, truncation flagged) split into canonical Discussion.
- Table-header debris ("DCP CAP DHL … Ours") removed from S097 and S105.
- OCR fixes: "CIEDE20 0 0"→"CIEDE2000", "RoblesKelly"→"Robles-Kelly", "endto-end", "channelminimized",
  "hazefree", "attentionbased", "postprocessing", "0.0 0 01", bio "20 04"→"2004", "Xi ׳an"→"Xi'an".
- Preserved as printed (suspected source typos): "natual" (heading), "halo aircrafts", "Fatal [12]",
  "uncorrected".
- Garbled equations flagged: Eqs. (8)–(12), (14), (16), (20)–(23), (25)–(29), (34)–(35); readable
  ones normalized ((1)–(7), (13), (15), (17)–(19), (24), (30)–(33)).
- Known loss: S095 ends mid-sentence; RESIDE subset description lost in extraction.

## 17_DoubleMapping_PR2012_Video_Smoke_Detection (sole-author; STRICT policy per instruction)

Extraction quality: MEDIUM-LOW (matches core_corpus warning). Severe dual-column scrambling; ligature
glyph corruption (¼ = ; ð Þ ( ); 4 >; r ≤). Per instruction, ONLY clean intact Original blocks or
unambiguously reconstructible runs were kept.

- Kept intact blocks: S001–S003, S005, S010, S015, S023, S025, S032, S036, S042, S047, S053.
- Salvaged coherent runs from scrambled blocks with exact cross-block seams: S011→S009, S037→S035,
  S043→S041, S043→S044, S048→S051, S054→S052 (conclusion), plus ~10 within-Methods seams
  (documented in-file).
- EXCLUDED: all garbled equations (Eqs. (1)–(5), (7)–(17), (24)–(34) debris), pure formula blocks
  S028/S029, ROC-axis debris S038, table rows S049/S050, pseudo-code debris in S048, truncated
  reference list body (only [1], [2] + fragment survive — flagged LOW, refer to PDF).
- Body prose mislabeled as captions restored: C002, C016.
- Acknowledgments separated from the column-scrambled conclusions block (S054).
- Preserved as printed: "extractly", "false farms", "above than", "opeation", "down loaded",
  "great than".
- Flagged: conflicting duplicate Keywords blocks S006 vs S007.
- No standalone RelatedWork (survey embedded in §1) and no standalone Discussion.

## 18_DualGuided_FrequencyPrototype_TMM2024_FewShot_Segmentation (co-corresponding; refs EXCLUDED)

Extraction quality: MEDIUM with the worst reference-section damage in the shard. Heaviest
reconstruction effort (~25 exact cross-block seams).

- Per instruction, the ENTIRE reference list (S081–S086, S088) is EXCLUDED from clean text: the
  Original blocks there are column-scrambled and contaminated with machine-translated reference
  text. Refer to PDF for references.
- The Conclusion paragraph was RESCUED from inside scrambled reference block S081 (it was glued
  between reference entries) and placed under canonical Conclusion.
- Introduction/Methods/Results untangled from severe dual-column interleaving; every reconstructed
  paragraph lists its seam chain (e.g., S011→S014→S012; S050→S051→S053→S054→S055;
  S057→C009→C010→C011→C012). Displaced II.C heading and lead-in reassembled from S026.
- Body prose mislabeled as captions restored: C009–C012, C018–C020, C026–C027.
- Missing-space artifacts repaired throughout (e.g., "localprototypesfromthesupportimage",
  "ForclassC,theIoUisdefinedas"); IEEE bullet glyph "r"→"-".
- Equation handling: S065/S066 fragments excluded; Eq. (1), (4), (5) kept with partial-garble flags;
  (6)–(24) normalized where readable.
- Acknowledgments built from the IEEE first-page funding footnote (S006); no separate section exists.
- Known risk: one numeric value may be missing at the S071→S074 seam (flagged in-file).

## 20_GP_Smoke_Detection_IEEEAccess2017 (Tier A1, 1.00)

Extraction quality: HIGH — cleanest paper of the shard. Reading order intact; equations
pre-normalized to ASCII in the reader; complete reference list [1]–[41].

- Only structural work needed: merged S012+S013 (paragraph across p1–p2 break); assembled front
  matter; subsection headings normalized.
- Excluded nothing except figure/table images (captions kept, all six have English originals).
- Display equations (6), (7), (9), (12)–(14), (16), (17) were never extracted as standalone blocks
  (referenced in prose); flagged refer-to-PDF. All extracted equations ((1)–(5), (8), (10), (11),
  (15), (18)–(21)) kept as pre-normalized.
- Preserved as printed + flagged: "Gaussian Progress Regression" (S019), "occurred were obtained"
  (S078), "Bordatz" (S085/S086, vs correct "Brodatz" in S090 — inconsistency is in the source),
  "Datesets" (Table 1 caption).
- Reference anomalies flagged: [1] and [3] have identical authors/title but different journals
  (likely misprinted/mis-extracted [1] — the intro cites them for different content); [9]
  "vol. 4" suspected dropped digit (Pattern Recognition vol. 44).
- No standalone Discussion; funding footnote (S005) used as Acknowledgments.

## 30_DualEncoded_Curvelet_KSII2019_Smoke_Recognition (Tier A2, 0.90)

Extraction quality: MEDIUM. Prose in reading order, but ALL display equations (1)–(14) arrived with
scattered sub/superscripts, and blocks split mid-sentence at citation boundaries.

- Equations (1)–(14) RECONSTRUCTED (marked in-file): admissibility windows (1)–(2), frequency window
  (3), digital Curvelet coefficients (4), LBP-on-coefficients (5), histogram (6), aggregation (7),
  Dual-LBP (8), CLBP_C/CLBP_M (9)–(10), final feature concat (11), RBF kernel (12), GKO piecewise
  (13), DR/FAR/ERR (14). All are standard forms unambiguously matching the scattered debris and
  surrounding prose ("log2(min(w,h))−3" verified by "scale is 4 for a 128×128 image").
  EXCEPTION: the variance-definition summand in S077 is NOT fully recoverable — flagged, refer to
  PDF / cited ref [31].
- Equation numbers split across block seams rejoined: "(4)", "(5)", "(6)", "(14)".
- Citation-boundary sentence splits rejoined: S023/S024, S024/S025, S025/S026, S027/S028, S030/S031,
  S033/S034, S065/S066, S074/S075/S076, S094/S095.
- Figure debris stripped from body: Fig. 2 angle labels in S045; Fig. 4 axis ticks in S078.
- Table numeric rows inside caption blocks C005, C007, C009, C010 excluded; captions kept.
- Byline/affiliations de-interleaved (S002/S003 had e-mails and affiliations shuffled).
- Preserved as printed: "fire-like object", "Texture feature features", "an BP neural network",
  "multimodel", "a holistic features", "coefficent", "cocatenated", "is encoded textures",
  "shorten the classifying time", [15] mangled author names ("L. S, L. MW, and C. AC").
- OCR/extraction fixes: "[10]presented" respaced; abstract re-merged from 3 blocks; conclusion
  re-merged from 3 blocks; Yuan bio re-merged from 2 blocks.

## 36_FeatureAggregation_TCE2025_SuperResolution (Tier A1, 1.00)

Extraction quality: HIGH for prose; the reference section arrived as glued multi-entry blocks.

- Reference list split from glued blocks (S056–S065) into individual entries [1]–[61].
- SOURCE-level citation-number mismatches preserved as printed and flagged: text cites "IMDN [13]"
  (list: IMDN=[33], [13]=vast-receptive-field attention), "RLFN [42]" (list: RLFN=[46],
  [42]=Layer normalization), "SAFMN [7]" (list: SAFMN=[35], [7]=attention retractable transformer),
  and "Adam [57]"/"Cosine Annealing [58]" appear swapped vs list ([57]=SGDR, [58]=Adam). [59]
  (DRRN) is never cited in the extracted text. These are consistent internal mismatches, not
  extraction damage.
- Reader anchor anomaly: "I. INTRODUCTION" heading and first paragraph BOTH carry anchor S007
  (S006 skipped in reader numbering) — noted for downstream anchor-based tooling.
- Enumerated contribution list re-split (S012). Ablation item numbering irregularity (first item
  lacks the "1)" prefix while later items are "2)"/"3)") preserved as printed.
- Preserved as printed: "Extensive experiential results" (abstract), "undergone the same operations",
  "which result in", "state-of-art", "these compared approaches".
- Equations (1)–(20) pre-normalized inline in reader; all readable; kept as-is.
- Acknowledgments extracted from the first-page manuscript footnote (S011); metadata portion of the
  same footnote kept under Other.

---

## Cross-paper observations (for downstream agents; NOT Style DNA)

1. Extraction-quality gradient tracks venue/PDF generation: IEEE-born PDFs (20, 36) are near-clean;
   Elsevier PR papers (06, 11, 17) degrade with age (2012 worst: ligature glyphs ¼/ð Þ, scrambled
   columns); TMM 2024 (18) is modern but its two-column text layer interleaves badly; KSII (30)
   single-column keeps prose order but shreds equation typography.
2. Recurring source-level slips survive across venues and years (see per-paper "preserved as printed"
   lists) — kept verbatim so later style/idiolect analysis is not biased by silent correction.
3. Reference-section damage modes differ: truncation (17), scrambling + machine-translation
   contamination (18), glued multi-entry blocks (36), internal numbering errors (20 [1]/[3]; 36
   citation-number mismatches). Downstream citation-graph work should use the PDFs for 17 and 18.
4. Caption blocks (CXXX) frequently contain displaced body prose in papers 11, 17, 18 — anchor-based
   consumers must not assume CXXX ⇒ caption text.
5. Funding footnotes serve as de-facto Acknowledgments in all IEEE/KSII papers of this shard
   (18, 20, 30, 36); only PR papers (06, 11) and 17 have explicit Acknowledgment sections.
