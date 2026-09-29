# Reference — Connecteam Audit

Pulled live 2026-09-29 via Composio. Company `jxbzkmsqtlebglxm`, Coventry Cleans.

---

## Correction: the productive-hour ratio cannot be measured from here

`CONNECTEAM_GET_JOBS` returned `[]`. `CONNECTEAM_GET_SCHEDULERS` returned `[]`.

Both empty. There is no job data and no schedule data in Connecteam, so the hope recorded in
[02 Operations OS](../02-operations-os.md) — that the ratio might be a query against existing
check-in data — is wrong. It still needs measuring from scratch.

**Connecteam is currently a staff directory, not an operations system.** It holds ten people
and nothing about the work they do.

That is the real state of Operations OS: **no queryable system of record for jobs or
schedules exists anywhere.** Scheduling lives in Taka's head, in messages, or on paper. Every
downstream number — utilisation, on-time rate, jobs per cleaner, overrun by service code, the
productive-hour ratio, and therefore the entire margin model — has no data source.

This is now the largest structural gap in CCOS. It sits above the pricing work in importance,
because pricing accuracy depends on the time standards that only job data can validate.

---

## The team: 9 cleaners plus Taka

| Name | Role | Start | Worker type | Pay type | Employment |
|------|------|-------|-------------|----------|------------|
| Taka Nharara | Manager / owner | — | Employee | Hourly | Full Time |
| Funmilayo Mary Lebile | Operative, On-Site Cleaning Staff | 01/08/2025 | *missing* | *missing* | *missing* |
| Uchechukwu Nnamdi Umeagukwu | Janitorial Lead | 25/08/2025 | *missing* | *missing* | *missing* |
| Favour Ekwulugwo | *no title* | *missing* | *missing* | *missing* | *missing* |
| Angelica Ekwulugwo | *no title* | 05/11/2025 | *missing* | Hourly | *missing* |
| Felicia Dzatoh | Operative | 01/06/2026 | Employee | Hourly | Part Time |
| Jenice Anokye | Operative | *missing* | *missing* | *missing* | *missing* |
| Pauline Runyowa | *no title* | *missing* | Employee | Hourly | Part Time |
| Kupakwashe Majakwara | *no title* | *missing* | *missing* | Hourly | Part Time |
| Gisela Nataniel | *no title* | *missing* | Employee | Hourly | Part Time |

Everyone reports directly to Taka. Nobody reports to a Team Leader, which confirms the
structural point in [00 Architecture](../00-architecture.md): with nine cleaners all
escalating to the CEO, the CEO is the operations manager.

Uchechukwu is titled **Janitorial Lead**, so the Team Leader role partly exists in name. It
carries no reporting lines.

---

## ACT NOW: a wage rate steps up in two days

Three cleaners are in the 18-to-20 National Minimum Wage band rather than the 21-and-over
National Living Wage:

| Name | Date of birth | Age today | Note |
|------|---------------|-----------|------|
| **Kupakwashe Majakwara** | 01/10/2005 | 20 | **Turns 21 on 1 October 2026 — two days away.** Her statutory floor rises to the 21+ rate from that date |
| Angelica Ekwulugwo | 01/07/2007 | 19 | 18-20 band |
| Favour Ekwulugwo | 10/06/2008 | 18 | 18-20 band |

Two cleaners have no date of birth recorded at all (Jenice Anokye, Gisela Nataniel), so their
age band is unverified and their correct wage floor is unknown.

**Consequence for the cost model.** `pricing.md` assumes a single £12.71 rate for everyone. If
under-21s are paid the lower statutory band, blended labour cost is below £12.71 and margins
are slightly better than modelled. If they are all paid £12.71 regardless, then three people
are paid above their statutory floor — a legitimate choice, but it should be a deliberate one.

Either way the cost model should use **actual blended pay**, not one assumed rate. Verify
current NMW and NLW rates for each band; they change every April.

---

## Compliance gaps

The custom fields in use are: Title, Employment Start Date, Department, Branch, Direct
manager, Responsibility, Birthday, Gender, Worker Type, Pay Type, Overtime Eligibility,
Employment Type.

**Nothing tracks:**

| Missing | Why it matters |
|---------|----------------|
| **Right to work check and expiry** | A legal obligation with civil penalties per worker, and the defence is the documented check. There is no field for it, so for nine cleaners there is no record here at all. [03 Cleaner OS](../03-cleaner-os.md) calls this non-negotiable |
| **DBS status and date** | Required for healthcare and vulnerable-person work. Without it, that market is closed and the vetting claim cannot be evidenced |
| **Certification level** | The six-level Academy has nowhere to live, so progression cannot be tracked or paid against |
| **Quality score history** | The CC Quality Score has no home |
| **Training completed / due** | No record of who has been trained on what |

Add these as Connecteam custom fields. There is no API tool to create custom fields, so it is
a manual job in the Connecteam admin — worth an hour.

## Data hygiene

- **5 of 9 cleaners have no Employment Start Date** (Favour, Jenice, Pauline, Kupakwashe,
  Gisela). Tenure and 90-day retention cannot be calculated, so two KPIs in the dictionary are
  currently uncomputable
- **6 of 9 have no Worker Type recorded.** This is the employment status documentation. Given
  the risk flagged in 03 and 05, an undocumented classification is the weak point — if
  challenged, "Employee" is recorded for three cleaners and blank for six
- **4 of 9 have no Pay Type**
- **Gisela Nataniel has no email address**
- **2 of 9 have no date of birth**, so their wage floor is unverified
- Most cleaners have no Title, and several have no Department

None of this is unusual for a growing business. All of it is cheap to fix and expensive to
leave, because the missing fields are precisely the ones that matter under scrutiny.

---

## What to do, in order

1. **Fix Kupakwashe's rate before 1 October.** Two days. This is a payroll action, not a
   systems one
2. **Add the five missing custom fields** and backfill right to work for all nine cleaners.
   This is the legal exposure
3. **Backfill start dates, worker type, pay type, dates of birth, and Gisela's email.** An hour
   of admin that unlocks the retention KPIs and documents the employment position
4. **Decide how job and schedule data gets captured.** Either turn on Connecteam's scheduler
   and time clock so jobs exist as records, or accept that Operations OS has no data source and
   the margin model stays an assumption. This is the big one
5. **Give Uchechukwu real reporting lines** if the Janitorial Lead title is meant to mean
   something, so cleaners stop escalating to the CEO

---

## Tools used

| Job | Tool | Result |
|-----|------|--------|
| Cleaners | `CONNECTEAM_GET_USERS` | 10 users, paging total 10 |
| Jobs | `CONNECTEAM_GET_JOBS` | **empty** |
| Schedules | `CONNECTEAM_GET_SCHEDULERS` | **empty** |
| Custom fields | `CONNECTEAM_GET_CUSTOM_FIELDS` | Not yet pulled |
| Smart groups | `CONNECTEAM_GET_SMART_GROUPS` | Not yet pulled. Six group ids appear on users: 14235601 (all), 14235602, 14235604, 14235610, 14235612, 14235613 |

No credentials, tokens, kiosk codes, device ids or personal contact details are recorded in
this file. Names and roles only, because the operational findings need them.
