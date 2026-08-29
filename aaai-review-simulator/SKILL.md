---
name: aaai-review-simulator
description: Conduct a strict, evidence-bound AAAI-style simulated peer review of an AI or computer-science manuscript, including four specialist reviews, a meta-review, score calibration, and a prioritized revision plan. Use when a user asks to assess submission readiness, simulate AAAI-style reviewers, identify fatal or major paper risks, or plan pre-submission revisions.
---

# AAAI Review Simulator

Use this skill only for non-official manuscript self-assessment. Do not imply affiliation with AAAI or predict actual acceptance.

## Workflow

1. Read the manuscript and any supplied tables, appendix, and rebuttal material before judging it.
2. Select the prompt resource:
   - Use `references/aaai_review_compact_zh.md` for a quick Chinese review.
   - Use `references/aaai_review_full_zh.md` for a comprehensive Chinese review.
   - Use `references/aaai_review_full_en.md` for a comprehensive English review.
3. Follow the selected prompt's evidence constraints. Ground every criticism in supplied material. If evidence is missing, state that it is not sufficiently specified rather than inventing a citation, result, page, or rule.
4. Return the requested reviewer reports, meta-review, ratings, and a prioritized revision plan. Distinguish Fatal, Major, and Minor issues.
5. Keep the tone direct and constructive. Treat ratings as an informal AAAI-style calibration, not an official scale.

## Reference material

- `references/usage_zh.md`: Chinese usage guide and recommended inputs.
- `references/limitations.md` and `references/ethics.md`: scope and responsible-use constraints.
- `references/LICENSE`: upstream MIT license.
