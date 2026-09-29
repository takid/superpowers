# 02a — Turning Connecteam into the Operations System

How to move Connecteam from a staff directory to the system of record for Operations OS.

Audited 2026-09-29. Companion to [02 Operations OS](02-operations-os.md) and
[reference/connecteam-audit.md](reference/connecteam-audit.md).

---

## The headline

**This is a Connecteam configuration job, not an automation job.** Every tool Composio exposes
for Connecteam is read-only apart from creating and archiving users. There is no API to create a
shift, a job code, a scheduler or a time clock entry. So nothing here can be built by an agent —
it is admin work in the Connecteam console, after which the API can read what it produces.

The good news is that you have built more than the audit first suggested.

---

## What already exists

### Forms — 10, and several are substantial

| Form | Fields | What it is |
|------|--------|-----------|
| Pre-Contract Office Cleaning Site Assessment & Walkthrough Checklist | 89 | The commercial survey |
| Pre-Contract Site Walkthrough – Office Cleaning Checklist | 85 | **Near-duplicate of the above** |
| The Ridings Checklist | 34 | Site-specific clean checklist |
| Zero Hours Contract of Employment | 32 | Employment contract |
| Zero Hours Contract of Employment | 32 | **Exact duplicate** |
| Garden Organic – Site Visit Checklist | 30 | Site-specific |
| Tools & Detergents Checklist (Deep Clean – 1 Bedroom) | 23 | Equipment and products |
| 79b Wyley Road – Pre-Clean Assessment Checklist | 20 | Site-specific |
| One-Off Deep Clean Service Agreement | 16 | Customer agreement |
| One-Off Deep Clean Service Agreement (Extended) | 16 | **Near-duplicate** |

That 89-field office walkthrough is real work and exactly what
[01 Sales OS](01-sales-os.md) means by never quoting commercial from a phone call.

**Two problems with the set.**

**Three duplicate pairs.** Two office walkthroughs, two deep clean agreements, two identical
zero-hours contracts. Nobody knows which is current, so people pick the one they find. Retire
one of each and put the version date in the name.

**The checklists are per-site, not per-service.** The Ridings, 79b Wyley Road, Garden Organic.
That does not scale: every new customer needs a new form, and there is no standard to train
against or inspect against. [02 Operations OS](02-operations-os.md) wants one standard per
service — CC-HOME-01, CC-HOME-02, CC-HOME-03 and so on — with the property-specific detail on
the property record instead.

### The employment basis is documented, and the cost model is right

A **Zero Hours Contract of Employment** exists. That means cleaners are engaged as employed
workers, not self-employed contractors, so holiday accrual at 12.07%, employer National
Insurance and pension all genuinely apply. The cost model in
[05 Finance OS](05-finance-os.md) is built on exactly that basis, so it is correct.

It also means the misclassification exposure flagged in [03 Cleaner OS](03-cleaner-os.md) is
smaller than feared. The remaining gap is administrative: Worker Type is recorded for only
three of nine cleaners, so the position is contracted but not consistently logged.

### Custom fields and smart groups exist as scaffolding

Fields: Birthday, Gender, Title, Employment Start Date, Team, Department, Branch, Direct
manager, Employee ID, Responsibility, Worker Type, Pay Type, Overtime Eligibility, Employment
Type.

**Smart groups are defined but nearly all empty:**

| Group | Users |
|-------|-------|
| CoventryConnect | 10 |
| Female | 7 |
| Male | 2 |
| CovCleans | 2 |
| All admins group | 1 |
| **On-Site Cleaning Staff** | **1** — should be 9 |
| Supervisory Team | 0 |
| Scheduling & Coordination | 0 |
| Team 1 / 2 / 3, Branch 2 / 3, Other | 0 |

The structure you would want is already named. Nobody is in it. Right now the only groups
carrying real membership are everyone, and gender.

---

## What is missing: the spine

| Missing | Consequence |
|---------|-------------|
| **No Time Clock instance** | No clock in or out. No actual hours. So no productive-hour ratio, no on-time arrival rate, no actual job durations |
| **No Scheduler instance** | No shifts. No schedule, no capacity view, no day blocking |
| **No Jobs (job codes)** | Nothing to attribute time to. No cost or duration per service |
| **Task boards empty** | No exception tracking |

`CONNECTEAM_GET_JOBS` takes an `instanceIds` parameter — "scheduler or time clock". There is no
instance, which is why jobs came back empty. Jobs hang off an instance, so the instance comes
first.

---

## The build order

### Step 1. Turn on Time Clock

**The single highest-value switch in the business.** Clock in and out gives actual hours against
paid hours, which is the productive-hour ratio, which is the assumption the entire margin model
in 05 rests on. Right now the floor of £29 and target of £34 per charged hour depend on a
guess of 0.866 that nothing can test.

It also gives on-time arrival, the service failure customers forgive least.

### Step 2. Create Jobs as a two-level structure

`GET_JOBS` supports sub-jobs nested under a parent, which maps exactly onto what CCOS needs:

```
Parent job = the service code          Sub-job = the customer or site
─────────────────────────────          ───────────────────────────────
CC-HOME-01 Regular clean          ├─ Mrs X, CV5
                                  ├─ Mr Y, CV3
CC-HOME-02 Deep clean             ├─ 79b Wyley Road
CC-HOME-03 End of tenancy         ├─ ...
CC-COM-01 Office standard         ├─ The Ridings
                                  ├─ Garden Organic
CC-STR-01 Short let turnaround    └─ ...
```

Time clocked against a sub-job rolls up to the service code. That is what produces contribution
margin by service code, overrun rate by service code, and validated time standards. It is the
join between Operations and Finance that does not currently exist.

### Step 3. Turn on Scheduler

Shifts assigned to cleaners against jobs. This is where the geographic day blocking in 02
becomes real rather than a policy, and where capacity and utilisation become visible.

### Step 4. Convert per-site checklists to per-service standards

Build one form per service code carrying the nine sections in 02: scope, equipment, products,
PPE, sequence, room checklists, time standard, photo requirements, handover. Keep the
site-specific forms for the accounts that genuinely need bespoke work, and move the
property-specific detail onto the property record.

Start with CC-HOME-01 and CC-HOME-03, because end of tenancy carries the deposit-dispute risk.

### Step 5. Retire the duplicates and populate the groups

Three duplicate pairs to retire. Then put the nine cleaners into **On-Site Cleaning Staff**, and
put Uchechukwu into **Supervisory Team** — he is titled Janitorial Lead and reports nowhere, so
the group is the first step toward the reporting line that stops cleaners escalating to the CEO.

### Step 6. Task boards for exceptions

The exceptions table in 02 — no access, overrun, damage, out-of-scope requests — needs somewhere
to land. Task boards are empty and are the natural home.

---

## Two things to check before starting

**Plan tier.** Time Clock and Scheduler sit in Connecteam's operations features and may need a
paid tier above the current plan. Price it before committing to the sequence, because steps 1
to 3 all depend on it.

**API read coverage.** Composio's Connecteam tools cover users, jobs, schedulers, forms, task
boards, custom fields and smart groups. **There is no timesheet or shift-read tool in the set.**
So once Time Clock is running, getting hours out for the productive-ratio calculation may need
Connecteam's own API directly, a scheduled export, or manual reporting. Confirm that before
assuming the numbers will flow automatically — otherwise you will have the data in Connecteam
and no way to compute with it.

---

## What this unlocks, in order of value

1. **Productive-hour ratio** → validates or corrects the margin floor, the target, and the
   £33,800-to-£65,000 repricing gain. Everything in 05 currently rests on a guess
2. **Actual durations by service** → validates the time standards every price is built from
3. **On-time arrival rate** → the complaint driver customers forgive least
4. **Utilisation and capacity** → whether to hire, and when
5. **Contribution margin by service code** → which service lines actually make money
6. **Checklist completion and photo evidence** → two of the six inputs to the CC Quality Score

Items 1 and 2 are why this ranks above further pricing work. Pricing accuracy depends on time
standards, and time standards depend on this.
