# Coventry Cleans — Published Pricing

**Single source of truth for every price that appears in public.** Social posts, ads,
quotes, the website, Google Business. No skill hardcodes a price. Every skill reads this
file.

Cost model built: **2026-09-29**, from a stated cleaner rate of £12.71/hr.
Live rates read from coventrycleans.co.uk on 2026-09-29.

---

## The live rate card

From the website, which is the correct and authoritative source:

| Frequency | Rate | Direction |
|-----------|------|-----------|
| Weekly housekeeping | from £23/hr | Cheapest — correct |
| Fortnightly | from £25/hr | |
| One-off | from £27/hr | Dearest — correct |

**The tiering runs the right way.** Recurring is cheaper, one-off is dearer, which is exactly
the logic in `docs/ccos/01-sales-os.md`. The website was already doing this properly.

Published per-visit examples, consistent with £23/hr:

| Property | Per session | Implied hours |
|----------|-------------|---------------|
| 3-bed semi, weekly | £55–70 | 2.4–3.0 hr |
| 4-bed detached, weekly | £85–110 | 3.7–4.8 hr |

**Confirmed by Taka, 2026-09-29:** weekly £23, fortnightly £25, one-off £27. Search snippets
had suggested a page might show £23 against fortnightly; the card above is authoritative. If
any page shows otherwise, that page is wrong and should be corrected to match.

Survey-priced services — deep clean, end of tenancy, office, short let — are quoted after a
free survey rather than published. That is the correct approach for condition-driven work and
matches `docs/ccos/02-operations-os.md`. They still need an internal grid so quotes are
consistent; see below.

---

## VERDICT 1: the social skills advertised a price that does not exist

**This is free to fix and should be fixed today.**

| | Standard clean |
|---|---|
| Advertised in every social post | **£15/hr** |
| Cheapest real rate, anywhere on the site | **£23/hr** |
| Gap | **35% below the cheapest real price** |

The £15 was never a Coventry Cleans price. The website has always been right; the skills
were carrying a figure from nowhere.

Every enquiry arrives anchored to £15 and gets quoted £23. That does three things, all bad:

1. **Kills conversion at the quote stage.** The customer is not comparing £23 against the
   market, they are comparing it against the £15 you promised. A 53% jump reads as a
   bait-and-switch even when the £23 is fair
2. **Attracts the wrong enquiries.** £15 draws price-shoppers who were never going to pay
   £23. You are paying to generate leads that cannot convert
3. **Damages trust at exactly the wrong moment** — the point where they were deciding
   whether to let a stranger into their home

Fix the advertised number to match reality today. It costs nothing and it is almost
certainly worth more than any campaign running this quarter. See Rule 3 below.

## VERDICT 2: every tier is above cost, none reaches the floor

Against £18.67 labour-only and ~£20.30 all-in per charged hour:

| Tier | Rate | Contribution, labour only | **Contribution, all-in** |
|------|------|---------------------------|--------------------------|
| Weekly | £23 | 18.8% | **11.7%** |
| Fortnightly | £25 | 25.3% | **18.8%** |
| One-off | £27 | 30.9% | **24.8%** |

Nothing is loss-making. But the hard floor is 30% and the target is 40%, so **all three tiers
sit below the floor on an all-in basis.** Weekly at 11.7% leaves almost nothing for overhead,
your own time, or a quiet month.

To reach the 30% floor: weekly £29, fortnightly £29, one-off £29 per charged-hour equivalent.
To reach the 40% target: £34.

Break-even sits at a productive ratio of 0.70 on the weekly tier. Above that you make
something; below it you do not. Measuring the real ratio is now urgent, because weekly is
close enough to the line that the answer matters.

## VERDICT 3: the frequency discount is applied twice

This is the subtle one, and it is why weekly is the thinnest tier.

A weekly property is less dirty than a fortnightly one, so it takes **fewer hours**. The
customer already pays less per visit for that reason alone. Then the rate card gives them a
**lower hourly rate on top**. Two discounts for one benefit.

The result is that your most valuable customers — the weekly recurring ones, the ones with the
highest lifetime value and the lowest acquisition cost — carry your worst margin.

**The fix: hold the hourly equivalent flat across frequencies and let the shorter duration be
the customer's saving.** A weekly 3-bed at 2.5 hours and a fortnightly 3-bed at 3 hours,
both at the same rate, already gives the weekly customer a cheaper visit without giving away
margin. Present it per visit, so the comparison the customer makes is £58 against £69, not
£23 against £25.

## VERDICT 4: survey-priced services need an internal grid

Deep clean, end of tenancy, office and short let are quoted after survey, which is correct.
But "we'll quote it" is not a pricing method — without an internal grid, two similar
properties get two different prices depending on who quoted and what mood they were in.

Build the internal grid from time standard × condition band × rate, per the deep clean
section below. Do not publish it. Use it on every quote.

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

One rate across all frequencies, per Verdict 3. The customer's saving comes from the shorter
time a regularly cleaned property needs, not from a second discount on the rate.

| Property | Weekly hrs | Fortnightly hrs | Weekly at floor £29 | Fortnightly at floor £29 | **Weekly at target £34** | **Fortnightly at target £34** |
|----------|-----------|-----------------|--------------------|--------------------------|--------------------------|-------------------------------|
| 1 bed, 1 bath | 1.5 | 2.0 | £44 | £58 | **£51** | **£68** |
| 2 bed, 1 bath | 2.0 | 2.5 | £58 | £73 | **£68** | **£85** |
| 3 bed, 1–2 bath | 2.5 | 3.0 | £73 | £87 | **£85** | **£102** |
| 4 bed, 2 bath | 3.5 | 4.5 | £102 | £131 | **£119** | **£153** |

Set the hours from observed jobs, not from this table. The hours are the pricing mechanism,
so getting them wrong is the same as getting the price wrong.

**What closing the gap is worth.** Take a weekly 3-bed currently around £60 a visit. At the
£29 floor it is £73; at the £34 target, £85.

| Move | Per visit | Per year, 52 visits | **Across 50 weekly customers** |
|------|-----------|--------------------|-------------------------------|
| To the floor | +£13 | +£676 | **+£33,800** |
| To the target | +£25 | +£1,300 | **+£65,000** |

No new leads. No new cleaners. No extra marketing. This is the largest single gain available
to the business, and it is larger on weekly customers than any other group precisely because
their margin is currently the thinnest.

Take the floor first if the target feels like too big a step. Staged over two annual reviews
gets you to target with far less attrition than one jump.

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

## What skills may publish, right now

**Never publish £15/hr or £18/hr again.** Neither was ever a Coventry Cleans price.

Skills may publish:

- **Per-visit prices derived from the live rate card** — £55–70 for a 3-bed weekly session,
  £85–110 for a 4-bed weekly session. These come straight off the website, so the business
  already honours them
- **Service and proof with no price at all** — always safe, still generates enquiries

Skills may **not** publish:

- Any hourly rate, for any service (Rule 1). The website may show one; social posts should
  not, because a post is where the £12/hr cash-cleaner comparison gets made
- Any figure for deep clean, end of tenancy, office or short let. Those are survey-priced and
  a published number becomes a promise you cannot keep on a neglected property
- Any price below the floor once the new grid is live

**The website is the source.** If a skill and the website disagree, the website wins and this
file gets corrected. That rule is what stopped the £15 problem being caught for months.

## When this file changes

1. Re-measure the productive ratio and materials cost
2. Re-run the cost model at current statutory rates
3. Update the tables and the date at the top
4. Re-upload the affected skills so published copy matches
5. Note the change and the reason in the commit

Prices are Tier 3 in `docs/ccos/00-architecture.md`. CEO only.
