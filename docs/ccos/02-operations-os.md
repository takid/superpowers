# 02 — Operations OS

## What it owns

Booked job to completed job at standard. Scheduling, routing, dispatch, the service
standards themselves, safety and compliance, quality measurement, and complaints.

It does not own who the cleaners are or how good they are. That is
[03 Cleaner OS](03-cleaner-os.md). Operations takes the people it is given and gets the
work done to standard.

## The two rules that make this work

**Same cleaner, same customer.** On recurring domestic work, the same cleaner every
visit unless something makes it impossible. Continuity is the biggest single driver of
retention in domestic cleaning. The customer stops explaining where things live, the
cleaner gets faster on a property they know, and the relationship becomes the reason
they do not switch to the cheaper quote that lands in their inbox. Breaking continuity
casually is how you lose customers who never complained about anything.

**Density beats distance.** Margin in this business is made in the gaps between jobs,
not during them. A cleaner doing four jobs in one postcode earns you more than a cleaner
doing three jobs across the city and being paid the same hours. Every scheduling decision
is a density decision.

## Scheduling

**Geographic day blocking.** Assign postcode clusters to days and hold the pattern.
Customers in CV5 get offered CV5 days. New enquiries get steered into the day their area
already runs. Say it plainly at booking: this area is served on Tuesdays and Thursdays.
Most customers accept it, and the ones who insist on a different day should be priced for
the disruption or declined.

The exception is commercial and short-let work, which runs on the client's clock, not
yours. Keep it separate from the domestic route map.

**Capacity planning.** Know three numbers at all times:

- Available cleaner hours this week
- Booked hours this week
- Utilisation: booked divided by available

**There is no system of record for jobs or schedules.** Audited 2026-09-29:
`CONNECTEAM_GET_JOBS` and `CONNECTEAM_GET_SCHEDULERS` both returned empty. Connecteam holds ten
people and nothing about the work they do — it is a staff directory, not an operations system.
Full findings in [reference/connecteam-audit.md](reference/connecteam-audit.md).

**This is the largest structural gap in CCOS.** Utilisation, on-time rate, jobs per cleaner,
overrun by service code and the productive-hour ratio all have no data source, which means the
margin model in 05 rests on an assumption that cannot currently be tested. It ranks above
further pricing work, because pricing accuracy depends on time standards only job data can
validate.

First decision: either turn on Connecteam's scheduler and time clock so jobs become records,
or accept that this module has no data and say so plainly rather than reporting numbers nobody
can source.

**Measure the productive hour ratio. This is the outstanding job in this module.**
[05 Finance OS](05-finance-os.md) currently assumes 0.866 — roughly six billed hours in seven
paid — and every margin figure in the business rests on that guess. It is the weakest number
in the model and the one most within your control.

To measure it: two weeks of check-in and check-out against paid hours, then divide billed by
paid. **The data does not exist yet** — see the audit above — so this needs capturing from
scratch before it can be calculated. If the real figure is
0.80 the margin floor rises from £29 to £31 per charged-hour equivalent, and the weekly tier
is closer to break-even than anyone currently believes.

Utilisation below target means you are paying for idle capacity. Above target means you
have no slack for illness, overruns, or a same-day enquiry from a good customer. Both are
expensive. Set a target band and schedule into it deliberately rather than filling until
it breaks.

**Buffers.** Every route carries travel time and a contingency block. Scheduling a day
with no slack guarantees that one bad job makes the rest of the day late, and lateness is
the complaint customers remember longest.

**The booking horizon.** Recurring jobs are scheduled forward for at least twelve weeks.
A recurring customer with no future dates in the diary is a one-off customer who has not
noticed yet.

## The job pack

No cleaner arrives at a property without this. Every field comes from the customer and
job records in [reference/data-model.md](reference/data-model.md).

1. Address, postcode, parking notes, and how to get in
2. Access method: key, key safe code, customer present, agent collection
3. Service code and the full scope for that job
4. Time allowed and the finish window
5. Customer preferences and anything to avoid. Rooms not to enter, products not to use,
   the dog, the shift worker asleep upstairs
6. Known issues from previous visits
7. Photo requirements for this service
8. Who to call and when to escalate

A cleaner who has to phone and ask a question the office should have sent is a system
failure, not a cleaner failure. Count those calls. They are a direct measure of how well
this module is built.

## Service standards

Every service has a written standard with a code. These are the delivery equivalent of a
recipe: a competent trained person should produce the same result from the document
without asking what is meant.

| Code | Service |
|------|---------|
| CC-HOME-01 | Residential standard clean |
| CC-HOME-02 | Deep clean |
| CC-HOME-03 | End of tenancy |
| CC-COM-01 | Office standard |
| CC-COM-02 | Commercial deep clean |
| CC-PROP-01 | Landlord and property management turnaround |
| CC-STR-01 | Short let and Airbnb turnaround |

Each standard document contains the same nine sections, in the same order:

1. **Scope.** What is included, stated positively. What is excluded, stated explicitly.
2. **Equipment.** Exactly what to bring. A cleaner short of one item improvises, and
   improvisation is where damage claims come from.
3. **Products.** Named products, named dilutions, named surfaces. Never "suitable cleaner".
4. **PPE and safety.** What must be worn and when.
5. **Sequence.** Room by room, top down, dry before wet, exit route last. The sequence is
   not preference. It is what stops recontamination and what makes the time standard
   achievable.
6. **Room checklists.** Tickable. Specific. "Skirting boards wiped" not "room cleaned".
7. **Time standard.** The expected duration for a standard-condition property of each size.
   This is the number every price in 01 is built on.
8. **Photo requirements.** Which shots, before and after, for this service.
9. **Handover.** What the cleaner does at the end. Lock-up, key return, customer note,
   completion record.

**End of tenancy and short-let turnarounds carry the most risk** and should be written
first after CC-HOME-01. End of tenancy because a deposit dispute puts you in the middle
of a landlord and tenant argument, and photographic evidence is the only thing that
settles it. Short lets because the next guest arrives whether you finished or not.

## Safety and compliance

This is not paperwork. It is what lets you win contracts domestic-only competitors
cannot, and what stops one bad afternoon becoming an uninsured claim.

- **COSHH assessments** for every chemical in use, accessible to the cleaner using it.
- **Risk assessments and method statements** for commercial sites. Most offices, schools,
  and healthcare settings will ask. Having them ready is a competitive advantage at
  tender stage, not an overhead.
- **Lone working procedure.** Domestic cleaners work alone in strangers' homes. A check-in
  and check-out record, and a rule for what happens when someone does not check out.
- **Key control.** Keys are numbered, never labelled with an address. The number-to-address
  map lives in the system, not on the fob. A lost labelled key is a liability you cannot
  insure your way out of.
- **Insurance.** Public liability, employers' liability where you employ, treatment risk,
  and key cover. Check the limits against what commercial clients actually require before
  you bid, not after.
- **Vetting.** Right to work checks on everyone. DBS checks where the work involves
  healthcare, vulnerable people, or unsupervised access. Put the vetting position in your
  marketing, because it is a genuine trust advantage over cash-in-hand competitors.

## Quality

**The CC Quality Score.** Every completed job produces one. Weights as set:

| Metric | Weight |
|--------|--------|
| Customer rating | 30% |
| Inspection result | 25% |
| Checklist completion | 15% |
| Complaints | 15% |
| On-time performance | 10% |
| Photo evidence | 5% |

| Band | Score | What happens |
|------|-------|--------------|
| Elite | 90 to 100 | Recognised. Eligible for lead roles, premium accounts, and bonus |
| Good | 80 to 89 | Standard. No action |
| Improvement | 70 to 79 | Team Leader conversation within a week. Specific, written, one thing to fix |
| Intervention | Below 70 | Formal: retraining, supervised visit, and a review date. Not a warning, a plan |

Score the job, not the person, then look at the pattern across jobs. A single low score is
usually a property or a day. Three low scores on the same cleaner is a training gap. Three
low scores on the same property across different cleaners is a mispriced job or an
unreasonable customer, and that is a Sales problem, not a cleaning one.

**Inspections.** Every new cleaner's first three jobs. Every cleaner at least monthly.
Every new customer's first and third visit. Every job on a contract account at a frequency
the contract specifies. Unannounced, sometimes. The purpose is calibration, and cleaners
should be told that plainly so it is not experienced as distrust.

## Complaints

Speed matters more than being right.

1. **Acknowledge within 2 hours.** Not a resolution, an acknowledgement from a person.
2. **Resolve or re-clean within 48 hours.** Free re-clean is the default for a genuine
   standard failure. Do not argue about a re-clean that costs less than the review it
   prevents.
3. **Log it against the job, the cleaner, and the customer.** All three.
4. **Root cause it at the weekly.** Which of these was it: wrong scope sold, not enough
   time allowed, cleaner capability, wrong products, unclear customer expectation, or
   customer being unreasonable. Each one has a different fix and a different owner.
5. **Follow up after the fix.** A week later. This is where complaints turn into loyalty,
   and it is the step everyone skips.

A customer whose complaint was handled well is measurably more loyal than one who never
complained. That is not a consolation, it is a mechanism, and it only works if step 5
actually happens.

## Exceptions

Write the rule once so nobody improvises at 07:40 on a Tuesday.

| Exception | Rule |
|-----------|------|
| No access on arrival | Wait a set period, call and message the customer, call the office, then leave. Charge per the cancellation policy. Log it. Two no-access events on the same customer triggers a conversation about access |
| Cleaner sick | Office reschedules or covers. The customer hears from the office before their slot, never after. Never leave a customer to discover it |
| Job overruns by more than 20% | Cleaner completes to standard where possible and reports it. Overrun is logged against the job. Repeated overruns on one service code means the time standard or the price is wrong. Feed it back to Sales, do not absorb it silently |
| Damage or breakage | Stop, photograph, report immediately, do not attempt repair. Office contacts the customer the same day. Honesty first is always cheaper than discovery later |
| Customer asks for out-of-scope work | Cleaner may do small courtesies. Anything meaningful gets quoted by the office. Cleaners never agree prices |
| Unsafe property or situation | Cleaner leaves. No exceptions, no negotiation, full pay for the visit. Office deals with the customer |

That last one is not generosity. A cleaner who fears losing pay will stay in a situation
they should have walked away from, and that is the incident that ends up with a solicitor.

## The records

- **Job record.** Every field in the data model, completed on every job. Check-in,
  check-out, checklist, photos, notes, exceptions.
- **Quality score.** Calculated per job, held against job, cleaner, and customer.
- **Inspection log.** Date, inspector, score, what was said, what was agreed.
- **Complaint log.** Open and closed, with root cause category.
- **Key register.** Number, holder, customer, date issued, date returned.
- **Exceptions log.** Feeds the weekly meeting in 00.

## The numbers

| Number | Watch for |
|--------|-----------|
| On-time arrival rate | The complaint driver customers forgive least |
| Utilisation | Idle capacity below target, no resilience above it |
| Jobs per cleaner per day | Rising means density improving, or corners being cut. Check against quality |
| Average quality score | Trend matters more than level |
| Complaint rate per 100 jobs | The honest measure of whether the standards work |
| Re-clean rate | Direct cost of quality failure |
| Overrun rate by service code | Where pricing and reality have drifted apart |
| Continuity rate | Percentage of recurring visits done by the customer's usual cleaner |

## Definition of done

- [ ] CC-HOME-01 and CC-HOME-03 exist as full written standards with time standards and photo rules
- [ ] Postcode clusters are assigned to days and new bookings are steered into them
- [ ] Every cleaner receives a complete job pack before every job, without being asked
- [ ] Quality scores are calculated on every completed job, not on the memorable ones
- [ ] Inspections happen on a schedule, not when something feels wrong
- [ ] Every exception in the table above has a written rule the team knows
- [ ] Keys are numbered and unlabelled, with a register that reconciles
- [ ] COSHH and lone working procedures exist and the cleaners have actually seen them
