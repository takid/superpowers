# Coventry Cleans — Skills

Versioned source of truth for the Coventry Cleans Claude skills.

## Why these live here

The skills run from `~/.claude/skills/synced/<bucket>/`, pulled down from the claude.ai
account at session start. That directory is **ephemeral** — it is wiped when the container
recycles, and edits made there do not propagate back to the account.

So this repo holds the real source. The workflow is:

1. Edit here
2. Commit and push
3. Re-upload the changed skill to claude.ai so it survives

Without step 3, a fix works for one session and then disappears.

## Contents

| Path | Status |
|------|--------|
| `pricing.md` | Single source of truth for every published price. Cost model built |
| `publishing.md` | Single source of truth for every external route. **Composio-first** |
| `missed-call-responder.md` | Runbook for the live enquiry call responder |
| `daily-content-machine/` | **Fixed.** Canonical social and content skill |
| `agentic-social-distribution/` | **Retired.** Redirect stub — delete at source |
| `coventry-cleans-payment-chaser/` | **Fixed.** QuickBooks primary, correct tool IDs, write-back |
| `daily-hunter/` | **Fixed.** Deduplication and contact log added |
| `competitor-intel/` | Unchanged. No defects found |

## What was fixed, and why it mattered

**1. Hardcoded prices, possibly below cost.**
Both social skills published `from £15/hr` and `from £18/hr` on every post. Neither had ever
been checked against fully loaded labour cost — base rate plus 12.07% holiday accrual plus
employer NI plus pension, divided by the productive hour ratio. On a National Living Wage
base that check lands close to £15 before materials, travel, overhead or profit.

Fixed by removing every hardcoded price into `pricing.md`, suspending the two hourly rates
pending the cost check, and adding the rule that no skill hardcodes a price.

**2. Advertising an hourly rate at all.**
An hourly rate invites the one comparison the business cannot win: the £12/hr cash cleaner.
`pricing.md` now requires per-visit and per-job pricing, recurring price first.

**3. Service priority inverted.**
`daily-content-machine` ranked recurring domestic **last** of five, while recurring
customers are the asset the business is built on. Reordered: recurring first, commercial and
landlord second, with end of tenancy and deep clean positioned as the doors into both.

**4. Two skills claiming the same trigger.**
`daily-content-machine` and `agentic-social-distribution` both ended their descriptions with
"Always use this skill for any social media or marketing distribution task." Which one fired
was luck, and they carried different content. `agentic-social-distribution` was a strict
subset, so it is retired to a stub. **Delete it from the account** — the stub stops it
winning the trigger but it stays in the list until removed at source.

**5. A publishing step that could never run.**
Both skills instructed "use the Buffer MCP server." No Buffer MCP server is connected. That
step was dead on every run.

**6. Nine live webhooks attached to nothing.**
The Make account has 11 webhooks. Only two are wired to an active scenario. The other nine —
including `Facebook Post Publisher`, `Instagram Photo Publisher`, `My Buffer Scheduler` and a
duplicate `MY Google Business` — are enabled, accept a POST, return success, and discard it.
Anything posting to them reports success and publishes nothing.

`publishing.md` documents which two routes are real (LinkedIn, Google Business), forbids
posting to the rest, and requires per-platform reporting so a silent no-op cannot hide in an
aggregate count.

**7. Stale connector IDs in the payment chaser.**
It called `mcp__9952add6__read_file_content` and `mcp__cf78e8f6__create_draft`. Those hashed
names no longer resolve. Replaced with the stable `mcp__Google_Drive__` and `mcp__Gmail__`
names, plus a standing rule never to reintroduce a hashed ID.

**8. The payment chaser trusted a hand-maintained sheet.**
QuickBooks is connected and holds the actual invoices, but the skill read a Google Sheet a
human had to keep current, then ended by asking that human to update it again. Now
QuickBooks is primary, the sheet holds chase state only, and the two are reconciled every
run — so drift between the books and the tracker surfaces instead of hiding. Critically, an
invoice in the tracker but **not** in QuickBooks is no longer chased.

**9. No write-back anywhere.**
Every skill ended at a document or a draft. Nothing updated state, so no run could know what
the last run did. The chaser now writes reminder count and dates back to the tracker, and
the hunter now maintains a contact log.

**10. The hunter had no deduplication.**
It re-surfaced the same organisations every run with no memory of prior contact, risking
triple-approaching the same facilities manager. Added a mandatory exclusion pass over a
90-day contact log, permanent `do not approach` handling, and UK cold B2B outreach rules
(sender identity, working opt-out, corporate subscribers only).

## Outstanding — not fixed here

These are build work, not defects:

- **Leads have no system of record.** Composio is the integration layer and **Clarify is not
  in use**, so the lead log goes to Google Sheets via
  `GOOGLESHEETS_SPREADSHEETS_VALUES_APPEND`. Until it exists, the response SLA and cost per
  acquisition cannot be measured. This is the next build.
- **Connecteam is connected and used by no skill.** It holds the real cleaners, jobs and
  schedules, and is the only realistic place to measure the productive-hour ratio the entire
  margin model rests on.
- **`CleanShub — Job Completed` webhook is orphaned.** Half of the job-completion trigger
  Customer OS needs for the 48-hour conversion contact. A Composio route may beat finishing
  the Make one.
- **Qualification capture is prose, not data.** Daniel returns a summary, not the nine
  structured fields. Vapi can return `structuredData` against a schema — Katie already does
  for recruitment.
- **LinkedIn destination unconfirmed.** The Composio connection is Taka's personal profile;
  the retired Make scenario posted to the company page. Confirm which before trusting it.

## Blocker

`pricing.md` carries an unverified cost position. The standard-clean and office hourly rates
are suspended until the cost check in that file is run. Until then, publish service and proof
without a price rather than a price that may be below cost.
