# content-engine playbook

## Current best

**Mode (seed):** Full Mode Mon, Wed, Fri. Quick Mode Tue, Thu, Sat aimed at the weakest coverage cell. Sunday: one Behind the Scenes post only.

**Format weighting (seed, until attribution data exists):** Case Study, Quick Tip, Tutorial get double weight. Story Poll and Reaction single weight.

**Attribution rule:** an enquiry row with `ref_row_id` pointing at a post row counts as one enquiry for that post's format and hook type. Formats are re-weighted monthly by enquiries per post.

**Postcode rotation:** overridden by coverage map. Weakest social cell gets 2 of every 5 posts.

**Variant naming:** `ce-<format>-v<n>`, e.g. `ce-casestudy-v1`.

**Hard rules (from brand):** old-school professional, visible price where relevant, one postcode per post, CTA every post, no emojis except Instagram.

## Live experiment

- Hypothesis: posts with a specific price outperform posts with "from £X" on enquiries per post.
- Control: `ce-quicktip-v1` from-price. Test: `ce-quicktip-v2` exact price for a named property size.
- Metric: attributed enquiries per post. Min sample: 10 posts per arm. Rule: +15% relative.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
