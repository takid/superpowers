# Coventry Cleans — Published Pricing

**Single source of truth for every price that appears in public.** Social posts, ads,
quotes, the website, Google Business. No skill hardcodes a price. Every skill reads this
file.

Cost model built: **2026-09-29**, from a stated cleaner rate of £12.71/hr.

---

## VERDICT: all three published prices are below or at cost

| Published price | Cost per charged hour | Outcome |
|-----------------|----------------------|---------|
| Standard clean, £15/hr | £18.67 labour alone | **Loss of ~£3.70 per hour sold** |
| Office clean, £18/hr | £18.67 labour alone | **Loss of ~£0.70 per hour sold** |
| Deep clean, £120 | £112–149 labour for a 6–8hr job | **Break-even at best, loss if it overruns** |

Every hour sold at these prices makes the business poorer. Volume makes it worse, not
better. All three are **suspended** until repriced.

---

## The cost model

**Inputs.** Cleaner base rate £12.71/hr. This is the National Living Wage, so there is no
headroom beneath it — the floor moves up every April and takes the cost model with it.

**Verify before relying on this:** the current NLW rate for the cleaner's age band, the
employer National Insurance rate and secondary threshold, and the pension qualifying
earnings band. All move, usually in April. Take the tax positions through the accountant.

### Employed cleaner, per paid hour

| Layer | Running cost |
|-------|--------------|
| Base rate | £12.71 |
| + holiday accrual, 12.07% (5.6 weeks, irregular hours) | £14.24 |
| + employer National Insurance, ~11% effective | £15.81 |
| + pension, ~2.2% effective on qualifying earnings | £16.16 |

**Fully loaded: ~£16.16 per paid hour.** Effective NI and pension percentages depend on
annual earnings; a part-time cleaner sits a little lower, full-time a little higher. Range
is roughly £15.80 to £16.35.

### Per charged hour

Travel, loading, setup and gaps between jobs are paid and not billed. Divide by the
productive hour ratio:

| Productive ratio | Cost per charged hour |
|------------------|----------------------|
| 0.90 (9 hours billed in 10 paid) | £17.96 |
| **0.866 (6 hours billed in 7 paid)** | **£18.67** |
| 0.80 (8 in 10) | £20.20 |

**Working figure: £18.67 per charged hour, labour only.**

### Materials and travel on top

The figure above is labour alone. Contribution margin in `docs/ccos/05-finance-os.md` also
deducts materials, consumables, and travel cost. Add those and the true direct cost per
charged hour lands nearer **£20 to £21**.

Measure your actual productive ratio and materials cost per job. Both are guesses until
then, and they are the two numbers that most move the answer.

### The self-employed case does not rescue it

If cleaners are genuinely self-employed at £12.71 with no on-costs: £12.71 ÷ 0.866 =
**£14.67 per charged hour.** Against £15 charged, that is 2% margin. Still not a business.

**And paying a self-employed contractor exactly minimum wage is itself a warning sign.** A
genuinely self-employed cleaner sets their own rate and prices above NMW because they carry
their own holiday, pension, sick time and downtime. Paying the employee wage floor to
someone treated as self-employed is evidence the relationship is really employment. See
`docs/ccos/03-cleaner-os.md` and take advice.

---

## The floor and the target

```
price per charged hour = direct cost per charged hour / (1 − target contribution margin)
```

On £18.67 labour-only cost:

| Contribution margin | Price per charged hour |
|--------------------|------------------------|
| 30% — hard floor | £26.67 |
| **40% — target** | **£31.12** |
| 50% — premium positioning | £37.34 |

**Hard floor: £26.70 per charged hour equivalent. Target: £31.**

Below the floor the answer is no, per `docs/ccos/01-sales-os.md`. Not a smaller discount. No.

---

## Rule 1: never publish an hourly rate

Publish per visit and per job. Never £/hr.

An hourly rate invites the one comparison you cannot win — the £12/hr cash cleaner. It also
means any gain you make on route density gets handed straight back to the customer as a
smaller bill, instead of becoming margin.

## Rule 2: lead with the recurring price

Recurring first, one-off second and higher. Always. Marketing copy as much as quotes.

## Rule 3: "from" means the cheapest real job you will actually do

Not an aspiration. If nobody has had that price, it is bait, and it costs you trust at the
quote stage when the real number lands.

---

## Per-visit grid

Structure to fill in once the productive ratio and materials cost are measured. Hours are
the time standard from the service standard in `docs/ccos/02-operations-os.md` — set them
from observed jobs, not from hope.

### CC-HOME-01 Regular clean — recurring, price shown per visit

| Property | Time allowed | At floor (£26.70/hr eq.) | **At target (£31/hr eq.)** |
|----------|--------------|--------------------------|----------------------------|
| 1 bed, 1 bath | 2.0 hr | £53 | **£62** |
| 2 bed, 1 bath | 2.5 hr | £67 | **£78** |
| 3 bed, 1–2 bath | 3.0 hr | £80 | **£93** |
| 4 bed, 2 bath | 4.0 hr | £107 | **£124** |

Quote the fortnightly figure first. Weekly may carry a small per-visit reduction for the
density benefit; monthly carries none, because a monthly property is dirtier each visit and
takes longer.

**First clean is priced separately**, at deep or intermediate rate, and said plainly at
quote stage.

### CC-HOME-02 Deep clean — one-off, per job

Price from hours and condition band, never bedrooms alone. A neglected two-bed can take
longer than a tidy four-bed.

| Condition band | Multiplier on standard hours |
|----------------|------------------------------|
| Light | 1.0 |
| Standard | 1.3 |
| Neglected | 1.7 |

A 3-bed deep clean at 6 hours standard condition: 6 × 1.3 × £31 = **£242**. Against the
£120 currently published, that is the scale of the gap. Photograph before quoting.

### CC-HOME-03 End of tenancy, CC-COM-01 Office, CC-STR-01 Short let

Same method: time standard × rate, with named add-ons for ovens, carpets, windows and
internal cupboards. Office work is priced per visit by floor area and frequency. Commercial
and contract work is quoted only after a site visit.

---

## Repricing the existing book

Do not apply new prices to existing customers overnight. Per
`docs/ccos/05-finance-os.md`:

1. New customers get the new grid from today. This stops the bleeding immediately
2. Existing customers get a scheduled review with proper written notice
3. Increase toward the floor first, then the target. A customer at £15/hr going to £31
   overnight will leave; staged over two reviews, most will stay
4. Expect to lose some. Let them go. Capacity released from a loss-making customer is
   capacity for a profitable one
5. The ones who leave were never profitable, so losing them improves the business
   immediately

---

## Until the grid is filled

Publish **service and proof without a price**. A post that says what we do and why we are
trusted still generates enquiries. A post carrying £15/hr generates loss-making jobs and
anchors the market against you.

## When this file changes

1. Re-measure the productive ratio and materials cost
2. Re-run the cost model at current statutory rates
3. Update the tables and the date at the top
4. Re-upload the affected skills so published copy matches
5. Note the change and the reason in the commit

Prices are Tier 3 in `docs/ccos/00-architecture.md`. CEO only.
