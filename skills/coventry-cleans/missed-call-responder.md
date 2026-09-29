# Missed Call Responder — Runbook

Implements the missed-call rule in `docs/ccos/01-sales-os.md`: every missed call gets a
response inside five minutes.

Built 2026-09-29. **Status: built, valid, NOT ACTIVE.** See Blocker below.

---

## Why this exists

A missed call is a lead you already paid to generate, arriving at the moment of highest
intent. Left alone it goes to whoever answers next. It is the cheapest recoverable loss in
the business and the fastest automation to build.

---

## What it does

```
Missed call event
      │
      ▼
Make webhook  ──────────────────────────────┐
      │                                      │
      ├─► Email alert to coventrycleans@      │  LIVE, no setup needed
      │   gmail.com with the number,          │
      │   time, and a tap-to-call link        │
      │   └─► respond 200                     │
      │                                      │
      └─► SMS back to the caller via Twilio   │  Needs credentials + flag
          (only when send_sms = "true")       │
```

The email leg works the moment the scenario is active, with no credentials. It gets a
missed call in front of Taka in seconds instead of whenever the phone is next picked up.

The SMS leg is deliberately gated so the scenario cannot error before Twilio is configured.

---

## The components

| Thing | Value |
|-------|-------|
| Make scenario | `CC Missed Call Responder`, id **9888931** |
| Webhook | id **4404017** |
| **Webhook URL** | `https://hook.eu2.make.com/laa06r5azz38mx2akm8gqbs457a7byxb` |
| Team / org | 1346028 / 3024838, zone eu2 |
| Gmail connection | 13925583 (already in use by the Katie scenario) |

---

## Payload contract

POST JSON to the webhook URL:

```json
{
  "event": "missed_call",
  "from": "+447700900123",
  "to": "+447544308764",
  "at": "2026-09-29T14:03:00Z",
  "status": "no-answer",
  "send_sms": "false"
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `from` | yes | The caller. Used for the SMS recipient and the tap-to-call link. E.164 format |
| `to` | no | Which of your numbers they rang |
| `at` | no | When. Free text or ISO timestamp |
| `status` | no | `no-answer`, `busy`, `failed` |
| `send_sms` | yes for SMS | The string `"true"` enables the SMS leg. Anything else and only the email fires |

`send_sms` is a string, not a boolean. The filter compares text.

---

## BLOCKER: Make plan is at its active-scenario limit

Activation returned `Maximum number of active scenarios has been exceeded`. Two scenarios
are currently active:

| Scenario | Executions | Carries |
|----------|-----------|---------|
| `CC LinkedIn Company Post` (9627462) | 7 since August | LinkedIn posting only |
| `Katie Recruitment Call Report` (7693094) | 32 | Vapi call reports **and** Google Business posting |

**Do not deactivate the Katie scenario.** It is doing two jobs, and one of them is the only
working Google Business publishing route.

Three ways forward:

1. **Deactivate `CC LinkedIn Company Post`, activate this.** Free, immediate. Costs
   automated LinkedIn posting, which has run 7 times in two months. **Recommended** — a
   missed call is a lost customer; a LinkedIn post is optional.
2. **Upgrade the Make plan.** Costs money, keeps everything. The right answer once more than
   two automations matter, which is soon.
3. **Merge this into the Katie scenario as a third router branch.** Free and no plan change,
   and it is the pattern that scenario already uses. But it couples missed calls to
   recruitment and GBP posting, and a mistake there breaks two working things at once. Only
   worth it if 1 and 2 are both unacceptable.

---

## Setting it up

### Step 1. Free an active slot

Per the blocker above, then activate scenario 9888931.

### Step 2. Get the missed-call event to the webhook

This is the part that depends on telephony, and the business number
(07544 308764) is a mobile, so **nothing currently detects a missed call**. Options:

**A. Twilio number in front of the mobile.** Buy a Twilio UK number, forward it to the
mobile, and set the call status callback to the webhook URL. Twilio fires `no-answer` when
nobody picks up. This is the robust answer and it also gives you a sending number for the
SMS leg, call records, and a number you can put in ads without exposing a personal mobile.

**B. Vapi answers instead.** Katie already exists. Point the business number at a
sales-configured Vapi assistant so calls are answered rather than missed, and have its
end-of-call report POST here. Better customer experience, more configuration work, and
Katie's current prompt is built for recruitment screening rather than enquiries.

**C. Phone automation app.** An Android automation app can POST on missed call. Cheapest,
least reliable, dies when the phone does. Fine as a stopgap.

Option A is the one to build. It is a prerequisite for the SMS leg anyway.

### Step 3. Wire Twilio into the scenario

In Make, open scenario 9888931, module 5 (`Make a request`), and replace four placeholders:

| Placeholder | Replace with |
|-------------|--------------|
| `REPLACE_TWILIO_ACCOUNT_SID` in the **URL** | Your Account SID |
| `REPLACE_TWILIO_ACCOUNT_SID` in **authUser** (advanced settings) | Your Account SID |
| `REPLACE_TWILIO_AUTH_TOKEN` in **authPass** (advanced settings) | Your Auth Token |
| `REPLACE_TWILIO_SENDER_NUMBER` in the **From** form field | Your Twilio number, E.164 |

**Enter these in Make, never in a chat or a commit.** The Auth Token is a credential with
full account access.

### Step 4. Turn the SMS on

Start sending `"send_sms": "true"` in the payload. Until then only the email fires, which is
the safe default.

### Step 5. Test before trusting it

1. Post the sample payload with `send_sms` set to `"false"`. Confirm the email arrives
2. Post again with `"true"` to a phone you own. Confirm the SMS arrives
3. Ring the business number from another phone, do not answer, and confirm the whole chain
   fires end to end

**Do not treat a 200 from the webhook as proof.** Make returns 200 the moment it accepts the
payload. Check the execution history in Make and confirm the modules actually ran. Nine
webhooks in this account are enabled and attached to nothing; they all return 200 too.

---

## The SMS copy

> Coventry Cleans here. Sorry we missed your call. Reply with your postcode and what needs
> cleaning, and we'll come back to you with a price today.

Follows the brand rules: direct, no filler, no exclamation marks, identifies the sender, and
gives one clear next step. No price, per `pricing.md` Rule 1 — a price in an SMS is a quote
you have not surveyed.

Under 160 characters, so it sends as a single segment.

---

## What this does not do yet

- **No CRM record.** The missed call does not create a Lead in Clarify, so nothing tracks
  whether it converted. That is the next build, and it is what turns this from a useful alert
  into a measurable part of the funnel. See `docs/ccos/reference/data-model.md`
- **No dedup.** Three missed calls from the same number in ten minutes send three texts. Add
  a data store keyed on caller number with a cooldown once volume justifies it
- **No hours awareness.** It replies at 2am the same as 2pm. The copy is written to be
  acceptable either way, but an out-of-hours variant would read better
- **No reply handling.** When the customer texts back, nothing routes it. Their reply goes to
  the Twilio number and sits there unless you forward it. Decide where replies land before
  going live, or the automation creates a worse silence than the one it fixed

That last one matters. An automated text inviting a reply, with nobody reading the replies,
is worse than no text at all.
