# retention-referral playbook

## Current best

**Offer policy (seed):** recurring at price-book hourly rate, same cleaner, fixed day. No introductory discounts. Referral offer: one free hour on the referrer's next clean once the referred client's first job is paid.

**+30 day `rr-30-v1` (seed):**
> Hi [first name], it's been a month since the [service] in [area]. A lot of clients keep it that way with a fortnightly or monthly visit, same cleaner each time, at £15 an hour. Want me to pencil in a regular slot? Coventry Cleans.

**+60 day `rr-60-v1`:** seasonal hook and two slots.

**+90 day `rr-90-v1`:** "Last note from me. If you ever need a hand with [service] again, we're on 07544 308764."

**Referral ask `rr-ref-v1` (seed, after a clean month):**
> Hi [first name], glad [cleaner name] is keeping things in order. If a neighbour or friend in [area] needs a cleaner, pass on 07544 308764 and we'll take an hour off your next visit once their first clean's done. Coventry Cleans.

**Save attempt `rr-save-v1`:** ask why, then offer a frequency or scope change. No discount. Log the reason code: price, moving, quality, schedule, no longer needed.

**Frequency cap:** one message per client per week across all agents.

## Live experiment

- Hypothesis: the +30 day recurring offer converts better when it names the cleaner who did the job.
- Control: `rr-30-v1`. Test: `rr-30-v2` with cleaner name.
- Metric: renewed / sent. Min sample: 30 per arm. Rule: +15% relative.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
