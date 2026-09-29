# 05 — Finance OS

## What it owns

The numbers that decide. True cost of delivery, the margin floor every price in
[01 Sales OS](01-sales-os.md) must clear, cash collection, the VAT position, and the
reporting that tells you what is actually happening rather than what it feels like.

Every figure in this module needs verifying against current rates before you price from
it. Wage floors, National Insurance thresholds, and the VAT registration threshold change,
usually in April. Set a calendar reminder each spring to re-run the cost model, and take
the tax positions through your accountant rather than from any document, this one included.

## The rule that makes this work

You do not know your margin until you know your true cost per productive hour.

Most cleaning companies price against what competitors charge, pay their cleaners an hourly
rate, subtract one from the other, and believe the difference is profit. It is not, and the
gap is large enough to be the difference between a business that compounds and one that
works hard for nothing.

Two things get missed. First, the on-costs sitting on top of the hourly rate. Second, the
hours you pay for that are not charged to anybody.

## True cost per productive hour

**Built 2026-09-29.** The live model is in
[`skills/coventry-cleans/pricing.md`](../../skills/coventry-cleans/pricing.md), which is the
single source for every price that appears in public. This section explains the method and
records the result.

**Step 1. On-costs on the hourly rate.**

| Layer | What it is | Coventry Cleans, per paid hour |
|-------|-----------|-------------------------------|
| Base hourly rate | National Living Wage for the age band. Verify each April | **£12.71** |
| Holiday pay | 5.6 weeks statutory, accruing at 12.07% of hours worked for irregular-hours staff | £14.24 |
| Employer National Insurance | Above the secondary threshold. Rate and threshold both move. Verify | £15.81 |
| Pension | Employer minimum on qualifying earnings once auto-enrolment is triggered | £16.16 |
| Sick, training, and induction time | Paid hours generating no revenue | + your actual |

**Fully loaded: ~£16.16 per paid hour**, against a £12.71 headline. Range £15.80 to £16.35
depending on annual earnings, since the effective NI and pension percentages move with hours
worked.

**The base rate is the National Living Wage, so there is no headroom beneath it.** The cost
floor rises every April whether prices do or not. That makes the annual price review later in
this module structural, not optional.

**Step 2. Productive hours, not paid hours.**

A cleaner paid for a seven hour day does not clean for seven hours. Travel between jobs,
loading and unloading, setup and pack-down, and short gaps between bookings all consume
paid time that no customer is charged for.

```
True cost per productive hour  =  fully loaded hourly cost  /  productive hour ratio
```

If the productive ratio is 0.80, every charged hour carries 25% more cost than the loaded
rate suggests. This is exactly why route density in
[02 Operations OS](02-operations-os.md) is a finance decision, not a logistics preference.
Improving the productive ratio raises margin on work you already have, without raising a
single price.

**Coventry Cleans, working figures:**

| Productive ratio | Cost per charged hour |
|------------------|----------------------|
| 0.90 | £17.96 |
| **0.866 — current assumption** | **£18.67** |
| 0.80 | £20.20 |

**The 0.866 is an assumption, not a measurement, and it is the weakest number in the whole
model.** It is also the one most within your control. Measuring it is an Operations
responsibility: log check-in and check-out against paid hours for two full weeks and divide.
Until that is done, every margin figure downstream carries the same uncertainty.

**Step 3. The other direct costs.**

Materials and consumables per job. Equipment depreciation and replacement. Vehicle costs,
fuel, insurance, and maintenance, or mileage paid. Laundry where you supply linen. Card and
payment processing fees. Those belong against the job, not in overhead, because they scale
with volume.

## Job-level contribution

Every job, every time:

```
Revenue
  less  fully loaded labour for the hours actually worked
  less  materials and consumables
  less  travel cost attributable to the job
  =     contribution
```

Contribution margin is contribution divided by revenue. Track it by service code and by
customer. Two things surface immediately, and both are usually surprising:

- **One service line is carrying the others.** Often deep cleans and end of tenancy look
  profitable on price but are not, because they routinely overrun. The overrun data from
  02 is what proves it.
- **Some named customers are unprofitable.** Not marginal. Loss-making. Distance,
  overruns, or a price set years ago and never revisited.

## The margin floor

**Set at 30% contribution. Target 40%.**

| | Per charged-hour equivalent |
|---|---|
| Direct cost, labour only | £18.67 |
| Direct cost, all-in with materials and travel | ~£20.30 |
| **Hard floor, 30% contribution** | **£29** |
| **Target, 40% contribution** | **£34** |

Below the floor, the answer is no. This has to be an absolute rule rather than a judgement
call, because every below-floor job arrives with a good reason attached: it fills a gap, it
might lead to more, the customer is nice, it is better than an empty slot. An empty slot
costs you the wage. A loss-making job costs you the wage plus the loss plus the capacity
that a profitable job needed.

### Where the business actually sits, 2026-09-29

Live rate card: weekly £23/hr, fortnightly £25, one-off £27.

| Tier | Rate | Contribution, labour only | **All-in** | vs floor |
|------|------|---------------------------|-----------|----------|
| Weekly | £23 | 18.8% | **11.7%** | £6 short |
| Fortnightly | £25 | 25.3% | **18.8%** | £4 short |
| One-off | £27 | 30.9% | **24.8%** | £2 short |

**Nothing is loss-making. Nothing reaches the floor either.** Weekly at 11.7% leaves almost
nothing for overhead, the CEO's time, or a quiet month. Break-even on the weekly tier sits at
a productive ratio of 0.70, which is close enough to the current assumption that measuring it
matters.

### The frequency discount is being applied twice

A weekly property is less dirty than a fortnightly one, so it takes **fewer hours**, and the
customer already pays less per visit for that reason alone. Giving them a **lower hourly rate
on top** is a second discount for the same benefit.

The consequence: the customers with the highest lifetime value and the lowest acquisition cost
— weekly recurring — carry the worst margin in the business. That is backwards.

**The fix:** hold one rate across all frequencies and let the shorter duration be the
customer's saving. Present per visit, so the comparison is £73 against £87 rather than £23
against £25. Grid in
[`pricing.md`](../../skills/coventry-cleans/pricing.md).

**What closing the gap is worth.** A weekly 3-bed from roughly £60 a visit to the £29 floor is
£676 a year per customer, or £33,800 across fifty. At the £34 target, £65,000. No new leads,
no new cleaners, no extra marketing spend. It is the largest single gain available to the
business, and it is largest on weekly customers precisely because their margin is thinnest.

**Discount authority.** Tier 2 in [00 Architecture](00-architecture.md) allows a limited
discount. Anything that breaks the floor is Tier 3, CEO only, and should be rare enough to
be memorable.

**Annual price review.** Every customer, every year, on a schedule. Costs rise every April
whether or not you put prices up. A book of customers on three-year-old pricing is a slow
margin collapse that nobody notices until it is severe. Give notice, explain briefly, hold
the increase. Expect to lose a small number and let them go.

## VAT

The single most important financial decision this business will face in the next two years.
Get advice on it early, not in the month you cross.

**The problem.** Once taxable turnover passes the registration threshold on a rolling
twelve month basis, registration is compulsory. Verify the current threshold with your
accountant; it has been £90,000 since April 2024 but it moves.

For commercial customers this is largely neutral, because a VAT-registered business
reclaims what you charge. For domestic customers it is not neutral at all. They cannot
reclaim anything. So on the day you register you face a direct choice on every domestic
price: raise prices by 20% and become materially more expensive than every unregistered
local competitor, or absorb it and take 20% off the top of your domestic revenue.

Absorbing it will typically remove more than your entire net margin. This is why so many
small cleaning companies stall just below the threshold and never grow again. That is a
real trap, and the wrong answer, because it caps the business permanently to avoid one
difficult year.

**The right answer is to plan the crossing rather than drift into it.**

1. **Know your rolling twelve month total, monthly.** Not the tax year. The rolling twelve
   months. Know how many months of headroom you have at current run rate.
2. **Shift the mix before you cross.** Every pound of commercial, landlord, agent, and
   contract revenue is a pound where VAT does not hurt you, because those customers reclaim
   it. Building that side of the book ahead of the threshold is the strategic move, and it
   is the strongest financial argument for the landlord and commercial push in
   [04 Customer OS](04-customer-os.md).
3. **Model both sides before the date.** What registration does to domestic pricing, what
   you can reclaim on materials, equipment, vehicle, and costs, and where the net actually
   lands. The reclaim side is real and is usually underestimated.
4. **Cross decisively.** Plan the price change, tell customers before it happens with a
   proper explanation, and expect some attrition. Crossing while growing is survivable.
   Crossing by accident, mid-year, with no plan, is what does the damage.
5. **Take advice on the schemes available.** Flat rate and cash accounting have different
   consequences for a labour-heavy business. This is an accountant's question and the
   answer depends on your actual cost profile.

## Employment status, financially

The cost consequence of the status question in
[03 Cleaner OS](03-cleaner-os.md). If cleaners are engaged as self-employed and that
treatment is later found to be wrong, the exposure is back-dated income tax and National
Insurance, holiday pay, and penalties, typically across several years and every affected
worker. It lands when the business is large enough to be worth examining, which is exactly
when you have the least appetite for it.

Whichever model you run, run it deliberately, with advice, and make sure the way the
operation actually works matches the way the contracts describe it.

## Cash

Profit is an opinion until it is collected. In a business paying wages weekly or
fortnightly, cash timing matters more than margin percentage.

**Collection rules.**

- **Recurring domestic goes on Direct Debit or stored card, collected automatically.** This
  is not a convenience, it is the difference between a business and a debt collection
  operation. A hundred recurring customers paying manually is a full-time chasing job
  nobody has time for.
- **One-off domestic is paid on completion or in advance.** Deposits on deep cleans, end of
  tenancy, and anything above a threshold you set.
- **Commercial and agent accounts** get proper payment terms, invoiced promptly, with a
  credit limit and a stop rule. Large accounts are where cash gets stretched.
- **Invoice the same day the job completes.** Every day of delay is a day added to the end.

**The chase ladder.** Automate it. The payment chaser workflow already in use should follow
this shape:

| Age | Action |
|-----|--------|
| Due date | Polite automated reminder |
| +3 days | Second reminder, payment link included |
| +7 days | Phone call from a person |
| +14 days | Formal notice, service suspension warning |
| +21 days | Service suspended pending payment |
| +30 days | Final notice, then recovery |

Apply it evenly. Selective enforcement teaches your slowest payers exactly how long they
can take.

**Cash runway.** Know at all times how many weeks of wages you could cover from current
cash if collections paused. Below a floor you set, that is the constraint of the month in
00 and nothing else gets attention.

## The reporting rhythm

**Weekly, 15 minutes.** Cash in, cash out, aged debt over 14 days, next week's wage bill,
bank balance against the runway floor.

**Monthly, 2 hours.**
- P&L against plan
- Contribution margin by service code
- Contribution margin by customer, bottom ten reviewed
- Revenue per cleaner and per productive hour
- Recurring revenue and its share of total
- Churn and its revenue impact
- Cost per acquisition by channel, against lifetime value
- Rolling twelve month turnover against the VAT threshold

**Quarterly.** Full pricing review against current costs. Customer profitability review.
Capacity and investment plan for the next quarter.

## Unit economics

The four numbers that determine whether growth makes you richer or just busier.

- **Customer acquisition cost.** Total sales and marketing spend divided by new customers
  won. By channel, or it tells you nothing actionable.
- **Customer lifetime value.** Average monthly contribution multiplied by average lifespan
  in months. Use contribution, not revenue. Revenue-based lifetime value is a number that
  flatters and misleads.
- **The ratio.** Lifetime value divided by acquisition cost. Below 3, growth is expensive
  and fragile. Well above 3 with capacity spare means you are under-investing in marketing.
- **Payback period.** Months to recover acquisition cost from contribution. In a cash-tight
  business this matters more than the ratio, because it tells you how fast you can afford
  to grow.

**Churn compounds against you.** At 10% monthly churn the average customer lasts ten months.
At 5% they last twenty. Halving churn doubles lifetime value without winning a single new
customer, and it costs far less than the marketing required to achieve the same result.
That is why [04 Customer OS](04-customer-os.md) is a finance project as much as a customer
one.

## The records

- Bookkeeping current to within one week, always
- Every job carrying its revenue, hours, labour cost, and materials
- Aged debtors, reviewed weekly
- Rolling twelve month turnover, updated monthly
- Cost model with the date it was last verified against current rates
- Price grid with the date it was last reviewed

## Definition of done

- [x] True cost per productive hour is calculated, written down, and dated — 2026-09-29
- [ ] The productive hour ratio is measured, not assumed — **currently assumed at 0.866**
- [ ] Materials and consumables cost per job is measured, not estimated
- [x] A margin floor exists — 30%, target 40%
- [ ] Every service code has a known contribution margin — regular clean only so far
- [ ] The frequency discount is applied once, not twice
- [ ] Survey-priced services have an internal quoting grid
- [ ] A margin floor exists and has been applied to refuse at least one job
- [ ] Recurring domestic customers pay automatically, not manually
- [ ] The chase ladder runs without anyone deciding to start it
- [ ] Rolling twelve month turnover is reviewed monthly against the VAT threshold
- [ ] A VAT crossing plan exists before you are within six months of the threshold
- [ ] Acquisition cost and lifetime value are known by channel
- [ ] Cash runway in weeks is known and has a floor
