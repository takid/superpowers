# CCOS — Coventry Cleans Operating System

Version 1.0

CCOS is the operating system for Coventry Cleans. It is not a folder of SOPs. It is
the set of rules, records, and routines that let the business run the same way on a
Tuesday in February as it does on the day the owner is standing over it.

The test of CCOS is simple. Taka should be able to leave for fourteen days and the
business should still take enquiries, quote them, schedule them, clean to standard,
invoice, chase, and report. If any of those stop, the module covering that step is
not finished.

## The principle

Most cleaning companies fail to scale because the business lives in the owner's head.
Pricing is a feel. Scheduling is a memory. Quality is a phone call. Every new customer
adds load to one person.

CCOS moves each of those out of the head and into a system that a competent person or
an AI agent can run from the written rule. The company stops being a cleaning company
with systems. It becomes a systems company that delivers cleaning.

## The modules

| # | Module | Owns | File |
|---|--------|------|------|
| 00 | Architecture | Structure, roles, operating cadence, where decisions get made | [00-architecture.md](00-architecture.md) |
| 01 | Sales OS | Lead to booked job. Response, qualification, pricing, follow-up, conversion | [01-sales-os.md](01-sales-os.md) |
| 02 | Operations OS | Booked job to completed job. Scheduling, dispatch, delivery standards, quality | [02-operations-os.md](02-operations-os.md) |
| 03 | Cleaner OS | Recruitment, onboarding, training, certification, pay, performance, retention | [03-cleaner-os.md](03-cleaner-os.md) |
| 04 | Customer OS | Completed job to recurring customer. Retention, reviews, upsell, referral, win-back | [04-customer-os.md](04-customer-os.md) |
| 05 | Finance OS | Pricing, margin, payroll cost, cash, VAT, employment status, the numbers that decide | [05-finance-os.md](05-finance-os.md) |
| 06 | Claudia | The intelligence layer. Exactly what she owns, recommends, and must never do | [06-claudia.md](06-claudia.md) |

Two shared references sit underneath all of them:

- [reference/data-model.md](reference/data-model.md) — the records every module reads and writes
- [reference/kpi-dictionary.md](reference/kpi-dictionary.md) — one definition per number, so a figure means the same thing everywhere

## How to read this

Each module has the same four parts.

1. **What it owns** — the boundary. If two modules both claim a decision, one of them is wrong.
2. **The rules** — what happens, in what order, with what thresholds. Written so someone with no context can follow it.
3. **The records** — what gets written down, and where. A step that leaves no record did not happen.
4. **Definition of done** — how you know the module is actually built, not just described.

## Build order

Do not build twelve systems at once. Build in this order, because each one funds and
feeds the next.

**Phase 1, weeks 1 to 4. Stop the leaks.**
Sales OS response rules and the pricing grid. Finance OS true labour cost and the
margin floor. These two together stop you selling work that loses money and losing
work you already paid to generate. Nothing else matters until these are live.

**Phase 2, weeks 5 to 8. Make delivery repeatable.**
Operations OS service standards and the job record. Cleaner OS onboarding and Level 1
certification. Now a job can be handed to someone other than you.

**Phase 3, weeks 9 to 12. Turn jobs into assets.**
Customer OS retention sequence and recurring conversion. This is where the revenue
model changes from transactions to a book of recurring customers.

**Phase 4, ongoing. Put the brain on top.**
Claudia. Only after 01 to 05 exist in writing, because an intelligence layer over an
undefined business produces confident nonsense.

Expansion and franchising are deliberately out of scope for v1.0. They are a
consequence of 01 to 06 working, not a parallel project. Revisit at 150 recurring
customers or £250k annual recurring revenue, whichever comes first.

## Version control

CCOS is a living document. Every change to a rule gets committed with a reason.
When a rule changes because of something that happened in the business, say what
happened in the commit message. In two years that history is worth more than the
document.
