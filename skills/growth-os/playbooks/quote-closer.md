# quote-closer playbook

## Current best

**Sequence (seed):** FU1 +24h, FU2 +3 days, FU3 +7 days, then `no_reply`. One message per step, same channel as the quote.

**FU1 `qc-fu1-v1` (seed):**
> Hi [first name], just checking the quote for the [service] came through. I've still got [slot 1] and [slot 2] free if either suits. Coventry Cleans.

**FU2 `qc-fu2-v1` (seed):**
> Hi [first name], [concrete reason: "we're booking up for the end of the month" / "if the tenancy ends on the [date], the [day] slot is the last one that works"]. Shall I hold it for you? Coventry Cleans.

**FU3 `qc-fu3-v1` (seed):**
> Hi [first name], I'll close this one off unless you'd like me to hold a slot. No problem either way. Coventry Cleans.

**Price objection (seed):** never discount. Offer scope: "We can leave the oven out and bring it to £X, or split it over two visits." Then the trust line: "The price covers a proper job with a checklist, insured, and we come back if anything's missed."

**"Getting other quotes" (seed):** "Fair enough. Two things worth checking on any quote: is it insured, and do they send the checklist. Happy to hold a slot until [day]."

**Booking confirmation must include:** date, arrival window, price, what's included, access, payment terms, cancellation line (24h notice).

**Lost reason codes:** price, timing, went elsewhere, no longer needed, no reply.

## Live experiment

- Hypothesis: a scarcity reason in FU2 beats a plain reminder.
- Control: `qc-fu2-v1` scarcity. Test: `qc-fu2-v2` social proof ("we did two end of tenancy cleans on [street/area] last week").
- Segment: all. Metric: booked after FU2 / FU2 sent. Min sample: 30 per arm. Rule: +15% relative.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
