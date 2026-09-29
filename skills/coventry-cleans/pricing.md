# Coventry Cleans — Published Pricing

**Single source of truth for every price that appears in public.** Social posts, ads,
quotes, the website, Google Business. No skill hardcodes a price. Every skill reads this
file.

Last verified against cost model: **NEVER — see blocker below**

---

## BLOCKER: these prices are unverified against cost

The figures below were carried over from the published copy in `daily-content-machine`
and `agentic-social-distribution`. They have never been checked against a fully loaded
cost per productive hour.

**Do not publish the hourly figures again until the check below is done.**

### The check

```
fully loaded hourly cost = base hourly rate
                         × (1 + 0.1207)        holiday accrual, irregular hours
                         × (1 + employer NI)    verify current rate and threshold
                         + pension              employer minimum on qualifying earnings

true cost per charged hour = fully loaded hourly cost / productive hour ratio
```

The productive hour ratio is charged hours divided by paid hours. Travel, setup, and gaps
between jobs are paid and not charged. If it is 0.80, every charged hour carries 25% more
cost than the loaded rate suggests.

Then: `contribution margin = (price per hour − true cost per charged hour) / price per hour`

Compare against the margin floor in `docs/ccos/05-finance-os.md`.

### Why this is urgent

On a National Living Wage base, the loaded cost alone lands close to the £15/hr that has
been advertised — before materials, travel, overhead, or profit. The standard-clean rate
may be at or below cost. Every post carrying it anchors the Coventry market against you
and is expensive to walk back.

Verify the current National Living Wage rate for the cleaner's age band. It rises each
April.

---

## Rule 1: never publish an hourly rate

Publish per visit and per job. Never £/hr.

An hourly rate invites the comparison you cannot win — the private cleaner at £12 an hour,
cash, no insurance, no cover, no standard. See the objection handling in
`docs/ccos/01-sales-os.md`. Competing on hourly rate against cash work loses, and the
customer won that way leaves at the first price rise.

Per-visit pricing also lets you improve the productive hour ratio and keep the gain,
instead of handing it back as a lower bill.

## Rule 2: lead with the recurring price

Recurring first, one-off second and higher. Always. This applies to marketing copy as much
as to quotes.

## Rule 3: "from" means the cheapest real job you will actually do

Not an aspiration. If nobody has ever had that price, it is bait and it costs you trust at
the quote stage when the real number arrives.

---

## Current published figures

| Service | Published as | Status | Replace with |
|---------|--------------|--------|--------------|
| Standard / regular clean | from £15/hr | **UNVERIFIED — suspend** | Per visit, by bedrooms and bathrooms, recurring price first |
| Deep clean | from £120 | Unverified, per-job so structurally correct | Per job, by size and condition band |
| Office clean | from £18/hr | **UNVERIFIED — suspend** | Per visit, by floor area and frequency |
| End of tenancy | not published | — | Per job, by size, with oven and carpets as named add-ons |
| Airbnb / short let | not published | — | Fixed turnaround fee per property size, linen as add-on |

Until the cost check is done, publish **service and proof without a price** rather than a
price that may be below cost. A post that says what we do and why we are trusted still
generates enquiries. A post with a loss-making price generates loss-making jobs.

---

## When this file changes

1. Re-run the cost check
2. Update the table and the verification date at the top
3. Re-upload the affected skills so the published copy matches
4. Note the change and the reason in the repo commit

Prices are Tier 3 in `docs/ccos/00-architecture.md`. CEO only.
