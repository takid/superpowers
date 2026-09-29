---
name: coventry-cleans-payment-chaser
description: Automated payment reminder system for Coventry Cleans. Reads outstanding invoices from QuickBooks (falling back to the Google Drive payment tracker), reconciles the two, builds branded HTML reminder emails, creates Gmail drafts, and writes the reminder state back to the tracker. Use when Taka says "chase payments", "send reminders", "who owes us", "payment chase", or "run the reminder".
---

# Coventry Cleans — Payment Chaser

Implements the chase ladder in `docs/ccos/05-finance-os.md`.

## When to use
"Chase payments" · "Send payment reminders" · "Who owes us money" · "Run the reminder" ·
`/chase-payments` · any request to chase outstanding invoices.

---

## Data sources

**Primary: QuickBooks.** The accounting system of record. Invoices and payments live here.

**Secondary: the Google Drive payment tracker.** Sheet ID
`1D_O1mzukxImLDVs1h5DqyJoi0_QSxfGaBM5sFCEGc78`. Holds the chase state (reminder count,
last reminder sent) that QuickBooks does not track for this ladder.

| Column | Field | Column | Field |
|--------|-------|--------|-------|
| A | Customer Name | H | Status |
| B | Email | I | Days Overdue |
| C | Phone | J | Last Reminder Sent |
| D | Invoice Number | K | Next Reminder Date |
| E | Service Type | L | Reminder Count |
| F | Amount (£) | M | Notes |
| G | Due Date | | |

**Two sources for the same money breaks the one-record-one-place rule.** The tracker exists
only because it holds chase state. Reconcile them every run (Step 2) and report drift. The
long-term fix is chase state in the CRM, with QuickBooks as the only source for amounts.

---

## Execution steps

### Step 1 — Read both sources

**QuickBooks** (correct tool names — do not use hashed IDs, they go stale):
- `mcp__Intuit_QuickBooks__qbo_accounting_get_ar_aging_detail` — outstanding invoices by age
- `mcp__Intuit_QuickBooks__qbo_sales_get_invoices` — invoice detail where needed

**Tracker:**
- `mcp__Google_Drive__read_file_content` with file ID
  `1D_O1mzukxImLDVs1h5DqyJoi0_QSxfGaBM5sFCEGc78`

If QuickBooks returns nothing or errors, continue on the tracker alone and say so in the
report. Never silently fall back.

### Step 2 — Reconcile and report drift

Match on invoice number. Report before drafting anything:

- **In QuickBooks, not in tracker** → chase it, and flag the tracker as incomplete
- **In tracker, not in QuickBooks** → do **not** chase. Flag it. Either it was never
  invoiced properly or it is already settled. Chasing a customer for an invoice that is not
  on the books is the most damaging error this skill can make
- **Amount or due date differs** → trust QuickBooks, flag the discrepancy
- **Paid in QuickBooks, unpaid in tracker** → do not chase. Tracker is stale

### Step 3 — Select what to chase

Chase where **all** of these hold:

- QuickBooks shows the invoice outstanding (or tracker-only with QuickBooks unavailable)
- Status is not `paid`, `cancelled`, `void`, or `disputed`
- Days overdue is greater than 0
- An email address exists
- Reminder Count is below 3
- Last Reminder Sent is not within the last 3 days

That last rule prevents double-chasing when the skill is run twice in a day. Without it,
running the chaser twice sends the same customer two reminders and makes the business look
disorganised.

### Step 4 — Build the email

Template: `reminder-email.html` in this directory. Substitute:

| Token | Source |
|-------|--------|
| `[FIRST_NAME]` | First word of Customer Name |
| `[SERVICE_TYPE]` | Service Type |
| `[INVOICE_NUMBER]` | Invoice Number |
| `[DUE_DATE]` | Due Date |
| `[AMOUNT]` | Amount, prefixed £ if missing |

**Subject:** `Payment Reminder — [INVOICE_NUMBER] | Coventry Cleans`

Ladder position changes the body, per `docs/ccos/05-finance-os.md`:

| Reminder Count | Days overdue | Treatment |
|----------------|--------------|-----------|
| 0 | 1–3 | Standard template |
| 1 | 3–7 | Standard template, payment link if available |
| 2 | 7–14 | Add: "We'd appreciate a response by [due date + 5 days]." **Also flag for a phone call** — at this stage a call collects better than an email |
| 3+ | 14+ | **Do not draft.** Output `APPROVAL NEEDED — [customer] — [n] reminders sent, [days] overdue. Escalation required.` |

At 3+ the decision is Taka's: formal notice, service suspension, or recovery. This skill
does not make that call. It is ESCALATE in `docs/ccos/06-claudia.md`.

### Step 5 — Create Gmail drafts

`mcp__Gmail__create_draft` with:
- `to` — Email
- `subject` — as above
- `htmlBody` — rendered template
- `body` — plain text fallback

Drafts, never sends. A human reads before money is asked for.

### Step 6 — Write the state back

**This step is not optional.** Without it the skill cannot know what it did last time, and
the ladder never advances.

For every customer drafted, update the tracker:
- **J Last Reminder Sent** → today
- **K Next Reminder Date** → per the ladder
- **L Reminder Count** → increment
- **M Notes** → append the ladder stage

Use the `google-workspace` skill for the Sheets write — it carries the cell-range helpers.
If the write cannot be completed, do not claim it was. Output a paste-ready block instead:

```
TRACKER UPDATE REQUIRED — paste into columns J, K, L
Row [n] | [Customer] | J: [date] | K: [date] | L: [count]
```

### Step 7 — Report

```
=== PAYMENT CHASE — [date] ===

SOURCES
QuickBooks:  [ok / unavailable]  outstanding invoices: [n], total £[x]
Tracker:     [ok / unavailable]  rows: [n]

RECONCILIATION
Matched:                 [n]
In QuickBooks only:      [n]  → chased, tracker incomplete
In tracker only:         [n]  → NOT chased, verify these were invoiced
Amount/date mismatches:  [n]  → QuickBooks used

DRAFTS CREATED: [n]
[Customer] | [Invoice] | £[amount] | [days] overdue | reminder [n] → draft created

PHONE CALL RECOMMENDED: [n]
[Customer] | £[amount] | [days] overdue — email alone is not collecting

APPROVAL NEEDED: [n]
[Customer] | £[amount] | [days] overdue | [n] reminders — escalation decision required

SKIPPED: [n]  (paid / no email / chased within 3 days / disputed)

TRACKER WRITE-BACK: [completed / manual update required — see block above]

TOTAL CHASED THIS RUN: £[x]
AGED DEBT OVER 14 DAYS: £[x]   ← weekly number in CCOS 05

NEXT: Gmail Drafts → review → send
```

If nothing qualifies:
```
=== NO ACTION ===
[n] invoices outstanding, £[x] total. None due a reminder today.
Next reminder due: [customer] on [date].
```

---

## Tool reference

| Task | Tool |
|------|------|
| Outstanding invoices | `mcp__Intuit_QuickBooks__qbo_accounting_get_ar_aging_detail` |
| Invoice detail | `mcp__Intuit_QuickBooks__qbo_sales_get_invoices` |
| Read tracker | `mcp__Google_Drive__read_file_content` |
| Write tracker | `google-workspace` skill (Sheets) |
| Create drafts | `mcp__Gmail__create_draft` |

Earlier versions of this skill called `mcp__9952add6__read_file_content` and
`mcp__cf78e8f6__create_draft`. Those hashed names are stale and will fail. Never reintroduce
a hashed connector ID — use the stable names above.

QuickBooks also offers `qbo_sales_send_invoice_reminder`. It is not used here: it sends
QuickBooks' own generic template rather than the Coventry Cleans branded email, and it
sends immediately rather than drafting for review.

---

## Tone rules

- First name only
- No exclamation marks
- No filler. No "just reaching out", no "hope you're well"
- Direct, calm, professional. The tone of a business that expects to be paid and is not
  anxious about it
- Always include the "Already paid? Please ignore this" line
- Never threaten at reminder 1 or 2. Consequences belong at the escalation stage, decided
  by a person
