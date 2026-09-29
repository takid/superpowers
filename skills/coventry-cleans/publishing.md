# Coventry Cleans — Publishing Routes

**Single source of truth for how content reaches a platform.** No skill invents a
distribution method. Every skill reads this file.

Verified against the live Make account on 2026-09-29 (org 3024838, team 1346028,
zone eu2).

---

## There is no Buffer MCP server

Both social skills previously instructed "use the Buffer MCP server to schedule posts."
No such server is connected. That step could never execute. It has been removed.

There **is** a Make webhook named "My Buffer Scheduler", but it is not attached to any
scenario. See the trap below.

---

## The trap: nine enabled webhooks attached to nothing

Make lets a webhook stay enabled after its scenario is deleted or was never built. The URL
still accepts a POST and still returns a success response. Nothing happens. Nothing is
published. No error is raised.

**A skill that posts to one of these will report success and publish nothing.** Only the
two routes marked LIVE below are wired to an active scenario.

---

## Route table

| Platform | Route | Status |
|----------|-------|--------|
| **LinkedIn** | Webhook `qpdjapddd3a4kmf19xlcx4zp7c8p6flg` → scenario "CC LinkedIn Company Post" (9627462) | **LIVE.** Active, 7 executions. Handles text posts and image posts via a router |
| **Google Business** | Webhook `n3k1137yomo82ma9mpzut6n9tb8wn8vn` → scenario "Katie Recruitment Call Report" (7693094), googlebusiness branch | **LIVE, but test before relying on it.** Scenario is active and carries a `google-my-business / createAPost` module. It is a dual-purpose scenario also handling Vapi call reports, so the payload must hit the right router branch |
| Facebook | Webhook "Facebook Post Publisher Webhook" `bg3bt5t8qzk0pmchc5674yq4fvq00sct` | **DEAD.** No scenario attached. Do not post to it |
| Instagram | Webhook "Instagram Photo Publisher Webhook" `8eai0ngvgzy0977n68zvc031okotoy41` | **DEAD.** No scenario attached |
| Buffer | Webhook "My Buffer Scheduler" `0rbxlnmfrxb7vtwg24600dnf6emmakgo` | **DEAD.** No scenario attached |
| Google Business (duplicate) | Webhook "MY Google Business" `573scovstt2g8fryhn9y2iwd09h21us1` | **DEAD.** No scenario attached. Confusing duplicate of the live route above — retire it |
| Nextdoor | No route exists | Manual posting only |

Base URL for all of the above: `https://hook.eu2.make.com/<udid>`

### Other orphaned webhooks in the account

Enabled, attached to no scenario, doing nothing. Listed so nothing builds on them by
mistake:

- `CleanShub — Job Completed` (`lnd6mqy019swexc0sggdgbzimwylgtvq`) — half-built. This is
  exactly the job-completion trigger Customer OS needs for completion notifications and
  the 48-hour conversion contact. Worth finishing.
- `KatieToCRM Webhook` (`c2x68w3y4ey1ryx3lyf67887aroiyh9c`)
- `KatieOutbound` (`c7xm24v2rhvtunl6khnpel68rl5y396u`)
- `TaskadeConnect` (`qwzmu3j6cgpu24glxteepvirn7a45hnm`)
- `End-of Call-Report` — marked gone by Make. Dead entirely.

---

## Rules for skills

1. **Publish only to a route marked LIVE.** Everything else is a draft saved to file, and
   the skill must say plainly that it needs manual posting.
2. **Never report a post as published** unless the webhook returned a response confirming
   the downstream module ran. A bare 200 from an orphaned hook is not confirmation.
3. **Report per platform**, never in aggregate. "6 posts scheduled" hides the fact that
   four went nowhere.
4. **Draft everything to file first**, then attempt the route. If the route fails the work
   is not lost.

## Correct reporting format

```
LinkedIn      → 2 published via Make (confirmed)
Google Business → 1 published via Make (confirmed)
Facebook      → 3 drafted, MANUAL POSTING REQUIRED (no live route)
Instagram     → 2 drafted, MANUAL POSTING REQUIRED (no live route)
Nextdoor      → 1 drafted, MANUAL POSTING REQUIRED (no route exists)
```

---

## To make Facebook and Instagram live

Two options. Both are decisions for Taka, not something a skill does on its own.

**Option A. Build the Make scenarios.** Attach the two existing orphaned webhooks to
scenarios with Facebook Pages and Instagram Business modules. The webhooks and their URLs
already exist, so nothing downstream changes once wired.

**Option B. Use Buffer properly.** Buffer has an API. Wire "My Buffer Scheduler" to a
scenario that calls it, and route Facebook and Instagram through Buffer as originally
intended.

Option A is fewer moving parts and one less subscription. Option B gives a scheduling
queue and a calendar view.

Until one is done, Facebook and Instagram are manual. Say so honestly in every run report
rather than implying they went out.
