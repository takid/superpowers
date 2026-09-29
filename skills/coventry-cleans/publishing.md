# Coventry Cleans — Publishing and Integration Routes

**Single source of truth for how anything reaches an external system.** No skill invents a
route. Every skill reads this file.

Verified against the live accounts 2026-09-29.

---

## Composio is the integration layer

Connected and callable: **connecteam, facebook, gmail, google_maps, googledocs, googledrive,
googlesheets, instagram, linkedin, openai, quickbooks, vapi, vercel**.

This replaces most of what was previously routed through Make webhooks. Composio has no
active-scenario limit, needs no webhook plumbing, and the tools are called directly.

**Make is now only used for what Composio cannot do:** receiving inbound Vapi call reports,
and posting to Google Business Profile.

**Clarify is not in use.** Earlier notes recommending it as the CRM are wrong. Lead and
customer records live in Google Sheets via Composio until something better is chosen.

---

## Social publishing — all via Composio

| Platform | Tool | Status |
|----------|------|--------|
| **Facebook** | `FACEBOOK_CREATE_POST`, `FACEBOOK_CREATE_PHOTO_POST` | **LIVE.** Page `Coventry Cleans`, id `439312599272453`, with CREATE_CONTENT rights. Also supports scheduling via `FACEBOOK_GET_SCHEDULED_POSTS` / `FACEBOOK_RESCHEDULE_POST` |
| **Instagram** | `INSTAGRAM_CREATE_MEDIA_CONTAINER` then `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` | **LIVE.** Two steps, in that order. Requires a publicly reachable image URL — Instagram fetches it, so a local file or data URI will not work. Check `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT` before batches |
| **LinkedIn** | `LINKEDIN_CREATE_LINKED_IN_POST`, `LINKEDIN_CREATE_ARTICLE_OR_URL_SHARE` | **LIVE**, connected as Taka Nharara (`vF6dNfwX3u`). **Caveat below** |
| **Google Business** | Make webhook `n3k1137yomo82ma9mpzut6n9tb8wn8vn` | **LIVE.** Not available through Composio. Payload contract below |
| Nextdoor | No route | Manual posting only |

### LinkedIn caveat: person versus company page

The Composio connection authenticates **Taka's personal profile**. The retired Make scenario
posted to the **company page**. Those are different destinations and the audience is different.

Before treating LinkedIn as fully solved, confirm which one
`LINKEDIN_CREATE_LINKED_IN_POST` actually writes to — check `LINKEDIN_GET_COMPANY_INFO` for the
organisation URN and test one post. B2B content aimed at facilities managers and landlords
belongs on the company page; personal-profile posting reaches a different and often better
audience, but it is a deliberate choice, not a default.

### Google Business payload contract

Read from the live Make scenario blueprint, so this is what the router actually matches:

```json
{
  "platform": "googlebusiness",
  "title": "Short post title",
  "caption": "The post body. This becomes the GBP summary."
}
```

`platform` must be exactly `googlebusiness` or the router sends it down the Vapi branch and
nothing posts. The scenario replies with the body `accepted` after publishing — **that string
is the confirmation.** A 200 without it means the post did not go out.

Link (`https://www.coventrycleans.co.uk/`), `LEARN_MORE` CTA, `en-GB`, and the GBP location are
hardcoded in the scenario, not settable per payload.

---

## Data routes — via Composio

| Job | Tool | Notes |
|-----|------|-------|
| Log a lead | `GOOGLESHEETS_SPREADSHEETS_VALUES_APPEND` | Append-only. The lead log |
| Update a tracker row | `GOOGLESHEETS_UPSERT_ROWS` | **This is what makes the payment chaser's write-back possible** |
| Read a sheet | `GOOGLESHEETS_VALUES_GET` | |
| Find a sheet | `GOOGLESHEETS_SEARCH_SPREADSHEETS`, `GOOGLESHEETS_GET_SHEET_NAMES` | |
| Cleaners | `CONNECTEAM_GET_USERS` | Company `jxbzkmsqtlebglxm`, Coventry Cleans. **Verified live** |
| Jobs | `CONNECTEAM_GET_JOBS` | The real job data for Operations OS |
| Schedules | `CONNECTEAM_GET_SCHEDULERS` | |
| Invoices and AR | QuickBooks tools | Also available on its own MCP connector |

**Connecteam is the live source for cleaners and jobs.** Operations OS and Cleaner OS should
read from it rather than assuming a system needs building. It is also the only place the
productive-hour ratio can realistically be measured from.

---

## Make — what remains

| Route | Status |
|-------|--------|
| **Enquiry calls (Daniel)** | Webhook `laa06r5azz38mx2akm8gqbs457a7byxb` → scenario `CC Enquiry Call Responder (Daniel)` (9888931). **LIVE and verified.** Vapi end-of-call-report in, enquiry email out, responds `received`. See [missed-call-responder.md](missed-call-responder.md) |
| **Google Business** | Webhook `n3k1137yomo82ma9mpzut6n9tb8wn8vn` → scenario `Katie Recruitment Call Report` (7693094). **LIVE.** Dual-purpose, also handles Katie's recruitment call reports |
| Katie recruitment reports | Same scenario as above. **LIVE** |

Base URL: `https://hook.eu2.make.com/<udid>`

### The orphaned-webhook trap still applies

Nine webhooks in the Make account are enabled and attached to no scenario. They accept a POST,
return success, and discard the payload silently. Among them: `Facebook Post Publisher`,
`Instagram Photo Publisher`, `My Buffer Scheduler`, a duplicate `MY Google Business`,
`CleanShub — Job Completed`, `KatieToCRM`, `KatieOutbound`, `TaskadeConnect`.

**Do not post to any of them.** Facebook and Instagram now go through Composio, so those two
hooks can be deleted. `CleanShub — Job Completed` is worth finishing as the job-completion
trigger for Customer OS, though a Composio route may be simpler.

Also dead: the LinkedIn Make scenario (9627462) was deactivated to free an active slot, and
there is no Buffer MCP server — that publishing step never existed.

### The Make plan limit is no longer pressing

Two active scenarios, both in use (Daniel, and Katie/GBP). Because social publishing moved to
Composio, the limit now only constrains new inbound webhooks rather than blocking three
channels.

---

## Rules for skills

1. **Prefer Composio.** Direct tool calls, no webhook indirection, no scenario limit.
2. **Publish only to a route marked LIVE.** Everything else is a draft saved to file, and the
   skill says plainly that it needs manual posting.
3. **Never report a post as published on a bare success.** For Google Business, look for
   `accepted`. For Composio, check `successful: true` and the returned post id. A 200 from an
   orphaned Make hook means nothing happened.
4. **Report per platform**, never in aggregate. "6 posts scheduled" hides four that went nowhere.
5. **Draft everything to file first**, then publish. A failed route must not lose the work.

### Never store credentials in this repo

`FACEBOOK_LIST_MANAGED_PAGES` returns a page access token in its response. Tokens, Auth
Tokens and API keys are never written to a file here, never put in a commit, and never pasted
into chat. Reference the page **id** (`439312599272453`), not its token.

---

## Correct reporting format

```
PUBLISHED
Facebook        → 3 via Composio (post ids returned)
Instagram       → 2 via Composio (container + publish confirmed)
LinkedIn        → 2 via Composio (destination: person / company — state which)
Google Business → 1 via Make (confirmed "accepted")

MANUAL POSTING REQUIRED
Nextdoor        → 1 drafted → social-media/posts/nextdoor/
```
