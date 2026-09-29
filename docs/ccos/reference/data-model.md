# Reference — The Data Model

The records every module reads and writes. Build these in whatever system you are using.
The shape matters more than the tool.

## The rule

One record, one place, one owner.

The most common failure in a small service business is the same information living in four
places and disagreeing with itself. A customer's key address in the CRM, their gate code in
a WhatsApp thread, their allergy note in the cleaner's head, and their real price in an
email from last March. When that happens, no report is trustworthy and
[06 Claudia](../06-claudia.md) cannot function at all.

Every field below has exactly one home. Everything else reads from it.

## Core entities

```
LEAD ──converts to──> CUSTOMER ──has many──> PROPERTY
  │                       │                      │
  └──has many──> QUOTE ───┘                      │
                    │                            │
                    └──won, creates──> JOB <─────┘
                                        │
                        ┌───────────────┼───────────────┐
                        │               │               │
                  QUALITY SCORE      INVOICE        COMPLAINT
                        │
                    CLEANER
```

## Lead

Created at first contact. Never deleted, whatever the outcome. The lost leads are half the
value of this table.

| Field | Notes |
|-------|-------|
| Lead ID | |
| Created date and time | Timestamp, not date. You need it for response time |
| First response date and time | The SLA measurement in 01 |
| Channel | Phone, WhatsApp, web form, Google Business, email, social, referral, walk-up |
| Source | Which campaign, which page, which referring customer. Never blank |
| Name, phone, email | |
| Postcode | Drives area tier and routing |
| Service wanted | |
| Property size | Bedrooms and bathrooms, or floor area for commercial |
| Frequency wanted | |
| Condition | Light, standard, neglected |
| Access notes | |
| Date needed | |
| Pets and occupants | |
| How they found us | Asked directly. Differs from tracked source often enough to matter |
| Status | New, qualifying, quoted, won, lost, nurture |
| Lost reason | Required when status is lost. In their words, not a category alone |
| Contact log | Every contact, both directions, with timestamp |
| Converted to customer ID | |

## Customer

| Field | Notes |
|-------|-------|
| Customer ID | |
| Name, phone, email, billing address | |
| Type | Domestic, landlord, agent, commercial, short let |
| Acquisition date and source | Carried from the lead. Needed for acquisition cost |
| Status | Active, at risk, dormant, released |
| Payment method | Direct debit, stored card, bank transfer, invoice terms |
| Payment terms | For commercial accounts |
| Assigned cleaner | The continuity rule in 02 depends on this |
| Recurring schedule | Frequency, day, time window |
| Current agreed price | One place. This is the field that ends pricing arguments |
| Price last reviewed | Date. Drives the annual review |
| Lifetime revenue and lifetime contribution | Calculated |
| Current monthly value | Calculated |
| Communication preferences and opt-outs | Respected absolutely |
| Review status | Asked, left, platform, date |
| Referrals given | |
| Notes | |

## Property

Separate from Customer, because landlords and agents have many, and because the property
facts belong to the address, not the payer.

| Field | Notes |
|-------|-------|
| Property ID, customer ID | |
| Address and postcode | |
| Type and size | Bedrooms, bathrooms, floor area, floors |
| Access method | Key number, key safe, customer present, agent collection |
| Key number | Never the address on the fob. See key control in 02 |
| Parking notes | Saves more time than any other single field |
| Pets | |
| Rooms excluded or restricted | |
| Products to avoid | Allergies, surfaces, preferences |
| Known issues | Learned on site, added by cleaners |
| Standard time allowed | The time standard for this specific property |
| Condition band | Reviewed periodically |
| Photos | Reference shots of how it should be left |

## Quote

| Field | Notes |
|-------|-------|
| Quote ID, lead or customer ID, property ID | |
| Service code | |
| Date sent, valid until | |
| Recurring price, one-off price, first clean price | All three where they apply |
| Hours allowed, cleaners required | |
| Inclusions and exclusions | |
| Add-ons offered and priced | |
| Contribution margin at quoted price | Calculated. This is what checks the floor before sending |
| Status | Sent, followed up, accepted, declined, expired |
| Follow-up log | Which step, when |
| Outcome reason | |

## Job

The centre of the model. Everything operational and financial hangs off it.

| Field | Notes |
|-------|-------|
| Job ID, customer ID, property ID | |
| Service code, scheduled date, time window | |
| Assigned cleaner or cleaners | |
| Recurring series ID | Links the visits in a schedule |
| Time allowed | From the standard |
| Check-in, check-out timestamps | Actual, from the app |
| Actual duration | Calculated. The overrun data in 02 depends on it |
| Checklist completion | Per item, not a single tick |
| Photos | Before and after, per the service standard |
| Cleaner notes | |
| Exceptions | No access, overrun, damage, out of scope request, unsafe |
| Status | Scheduled, in progress, complete, cancelled, no access |
| Price charged | |
| Labour cost | Fully loaded, from actual hours |
| Materials cost, travel cost | |
| Contribution and contribution margin | Calculated |
| Quality score | |
| Invoice ID | |

## Cleaner

| Field | Notes |
|-------|-------|
| Cleaner ID, name, contact | |
| Start date, status | |
| Engagement type | Employed or self-employed. See 03 and 05 |
| Right to work: document, check date, expiry | Retained. Non-negotiable |
| DBS status and date | Where applicable |
| Certification level, date achieved, assessor | |
| Training completed and outstanding | |
| Availability | Days, hours, constraints |
| Preferred areas | |
| Transport | Affects routing directly |
| Pay rate and progression step | |
| Assigned customers | For the continuity rule |
| Quality score history | |
| Absence and no-show log | |
| One to one notes | |
| Exit date and exit interview notes | |

## Invoice

| Field | Notes |
|-------|-------|
| Invoice ID, customer ID, job ID or job IDs | |
| Issue date, due date, amount | |
| Status | Draft, sent, paid, overdue, disputed, written off |
| Payment method and date paid | |
| Chase stage | Which rung of the ladder in 05 |
| Chase log | |

## Complaint

| Field | Notes |
|-------|-------|
| Complaint ID, customer ID, job ID, cleaner ID | All four. This is how patterns surface |
| Raised date, channel, description | |
| Acknowledged timestamp | Against the two hour rule |
| Resolution and resolution date | |
| Re-clean required, cost of resolution | |
| Root cause | Scope sold wrong, time allowed, capability, products, expectation, customer unreasonable |
| Follow-up completed | The day 7 check. The step everyone skips |
| Status | Open, resolved, closed |

## Quality Score

| Field | Notes |
|-------|-------|
| Job ID, cleaner ID, date | |
| Customer rating | 30% |
| Inspection result | 25% |
| Checklist completion | 15% |
| Complaints | 15% |
| On-time performance | 10% |
| Photo evidence | 5% |
| Total score, band | |
| Inspector, inspection notes | Where inspected |

## Build notes

**Start smaller than this.** Lead, Customer, Property, Job, Cleaner will carry the business
a long way. Add Quote, Invoice, Complaint, and Quality Score as the modules that need them
come online. A data model nobody fills in is worse than a simple one everybody does.

**Timestamps, not dates**, on anything you will measure speed against. Response time and
overrun both need the time of day.

**Calculated fields stay calculated.** Never type a contribution margin into a field. The
moment a calculated number can be typed over, it will be, and the report stops meaning
anything.

**Every record gets an ID from day one**, even in a spreadsheet. Migrating a business into
a real system later is straightforward with IDs and painful without them.
