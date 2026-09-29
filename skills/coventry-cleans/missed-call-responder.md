# Enquiry Call Responder — Runbook

Implements the response rules in `docs/ccos/01-sales-os.md`: no enquiry goes unanswered, and
nothing arrives without Taka knowing inside minutes.

Built and activated 2026-09-29. **Status: LIVE and verified.**

---

## Why this exists

A call that nobody returns is a lead you already paid to generate, lost at the moment of
highest intent. The business number is a mobile, so before this existed an unanswered call
left no trace at all.

Daniel, the Vapi assistant, answers the call. This scenario makes sure what he learns reaches
Taka immediately rather than sitting in a dashboard nobody opens.

---

## What it does

```
Caller rings the business number
      │
      ▼
Daniel (Vapi) answers and handles the enquiry
      │
      ▼
Vapi end-of-call-report  ──►  Make webhook
                                   │
      ┌────────────────────────────┴───────────────────────────┐
      │                                                        │
  Route 1: LIVE NOW                             Route 2: gated off
  Email to coventrycleans@gmail.com             SMS back to the caller
  · caller number, tap-to-call link             · only on abandoned calls
  · name, ended reason, duration                · needs Twilio credentials
  · what they wanted (Vapi summary)             · needs sms_enabled = "true"
  · recording + Vapi call record links
  └─► responds "received"
```

Route 1 needs no credentials and is running now.

---

## The components

| Thing | Value |
|-------|-------|
| Make scenario | `CC Enquiry Call Responder (Daniel)`, id **9888931** — **ACTIVE** |
| Webhook | id **4404017** |
| **Webhook URL** | `https://hook.eu2.make.com/laa06r5azz38mx2akm8gqbs457a7byxb` |
| Team / org | 1346028 / 3024838, zone eu2 |
| Gmail connection | 13925583 |
| Response body on success | `received` |

**A slot was freed by deactivating `CC LinkedIn Company Post` (9627462).** The Make plan allows
two active scenarios. See the consequence below.

---

## Verified, 2026-09-29

Not assumed. Actually tested:

1. Real POST to the webhook with a representative Vapi `end-of-call-report` payload → response
   `received`, HTTP 200
2. Email confirmed arriving in `coventrycleans@gmail.com` at 22:35:42Z, subject
   `Enquiry call — +447700900123 — customer-ended-call`, with the number, the 96s duration and
   the full enquiry summary rendering correctly

**A warning worth keeping.** An earlier test via Make's own "run scenario" returned
`status: SUCCESS` and sent nothing. `scenarios_run` feeds the scenario's input interface, not
the webhook body, so `message.type` was empty, the filter correctly declined to match, and the
run "succeeded" having done nothing. **Always test by POSTing to the webhook URL, and always
confirm the outcome at the destination.** This is the same trap as the nine orphaned webhooks
in `publishing.md`.

---

## What Taka still needs to do

### 1. Point Daniel at this webhook

In the Vapi dashboard, on the **Daniel** assistant, set the server URL (webhook) to:

```
https://hook.eu2.make.com/laa06r5azz38mx2akm8gqbs457a7byxb
```

and make sure the `end-of-call-report` server message is enabled. Katie's reports go to a
different webhook, so the two do not collide.

### 2. Point the business number at Daniel

Route 07544 308764, or a dedicated number, to Daniel so calls get answered rather than missed.
Until this is done the scenario is live but nothing triggers it.

### 3. Make one real test call

Ring the number, talk to Daniel, hang up, and confirm the email arrives with a sensible
summary. Do not trust it until you have seen that once.

### 4. Decide where replies land — before enabling the SMS leg

An automated text inviting a reply, with nobody reading replies, is worse than sending
nothing. Settle this first.

---

## Turning the SMS leg on, later

Route 2 is deliberately inert. It fires only when the payload carries `sms_enabled` equal to
the string `"true"`, which nothing currently sends. That keeps the scenario from erroring
before Twilio exists.

To enable it:

1. Get a Twilio account and a UK number
2. In Make, open scenario 9888931, module 5 (`Make a request`), and replace:

| Placeholder | Replace with |
|-------------|--------------|
| `REPLACE_TWILIO_ACCOUNT_SID` in the **URL** | Account SID |
| `REPLACE_TWILIO_ACCOUNT_SID` in **authUser** (advanced) | Account SID |
| `REPLACE_TWILIO_AUTH_TOKEN` in **authPass** (advanced) | Auth Token |
| `REPLACE_TWILIO_SENDER_NUMBER` in the **From** field | Your Twilio number, E.164 |

3. Edit the route 2 filter to match the abandoned-call condition you want without the
   `sms_enabled` gate

**Enter credentials in Make, never in a chat message or a commit.** The Auth Token grants full
account access.

### The SMS copy

> Coventry Cleans here. Sorry we missed your call. Reply with your postcode and what needs
> cleaning, and we'll come back to you with a price today.

Direct, no filler, no exclamation marks, identifies the sender, one clear next step. No price,
per `pricing.md` Rule 1 — a price in a text is a quote you have not surveyed. Under 160
characters so it sends as one segment.

---

## Consequence: LinkedIn posting is now manual

`CC LinkedIn Company Post` (9627462) is **deactivated**, not deleted. Its webhook
`qpdjapddd3a4kmf19xlcx4zp7c8p6flg` still accepts POSTs and now silently discards them, exactly
like the other orphaned hooks.

`daily-content-machine` must treat LinkedIn as draft-only until that scenario is reactivated.
Recorded in `publishing.md`.

Reactivating it means deactivating something else, unless the Make plan is upgraded. With the
job-completion trigger and the Facebook and Instagram routes all queued behind the same
two-scenario limit, the upgrade is close to unavoidable.

---

## What this does not do yet

- **No CRM record.** The enquiry does not create a Lead in Clarify, so nothing tracks whether
  it converted, and the response SLA in 01 still cannot be measured. This is the next build and
  it is what turns an alert into a measurable funnel. See `docs/ccos/reference/data-model.md`
- **No qualification capture into a record.** Daniel's summary is prose in an email. The nine
  qualification fields in 01 are not captured as structured data. Vapi can return
  `structuredData` against a schema — Katie already does this for recruitment. Giving Daniel a
  schema of the nine fields would make enquiries queryable rather than readable
- **No dedup.** Three calls from one number produce three emails
- **No hours awareness.** Emails send at 2am the same as 2pm
