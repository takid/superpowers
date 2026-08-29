# Claudia System Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the seven reliability gaps in the Claudia ops system from the 29/08/2026 build spec: broken filesystem writes, manual quote-status updates, false "no contact" flags, duplicate Connecteam shifts, the dead conversion report, count-only approval nudges, and the WhatsApp/Chrome profile fight.

**Architecture:** Claudia is a local Claude agent on the Coventry Cleans Windows workstation (real profile: `D:\Users\CoventryCleans`), driving `cov-cleans-mcp` (filesystem + lead tools), Connecteam, WhatsApp via Chrome, the cc-social-scheduler Postgres app, and a supervisor list of `.mjs` scripts. Fixes are a mix of MCP-server code changes, skill/instruction changes, and supervisor-script changes.

**Tech Stack:** Node.js (`.mjs` scripts + MCP servers, `node --test` for tests), Windows/PowerShell, Prisma + Postgres (cc-social-scheduler).

**IMPORTANT — this plan must run ON the workstation.** The Claudia runtime is not in any GitHub repo (checked: `superpowers`, `coventry-cleans-crm`, `coventry-cleans-crm-2026`, `cc-social-scheduler`, `backup-repository`, `ai-setup`), so remote sessions cannot see its source. Every task therefore starts with a locate step; run those for real — do not guess paths. Task order is by dependency, not spec order (spec item number noted per task).

---

### Task 0: Locate the Claudia system and put it under version control

**Files:**
- Discover: MCP config + Claudia scripts/skills root (referred to as `$CLAUDIA_ROOT` below)
- Create: `$CLAUDIA_ROOT\.git` (new private repo)

- [ ] **Step 1: Find the MCP config and the cov-cleans-mcp source**

Run in PowerShell:

```powershell
Get-ChildItem "$env:APPDATA\Claude","$env:USERPROFILE\.claude","$env:USERPROFILE\.mcp.json" -Recurse -Include claude_desktop_config.json,.mcp.json,settings.json -ErrorAction SilentlyContinue |
  Select-String -Pattern "cov-cleans-mcp" -List
```

Open the matching config; note the `command`/`args` entry for `cov-cleans-mcp` — its script path is the server source. The directory holding it (plus the supervisor scripts like `conversion-report.mjs` and Claudia's skills) is `$CLAUDIA_ROOT`. If the scripts live in more than one directory, note each; the steps below say which piece they touch.

- [ ] **Step 2: Find the supervisor list**

```powershell
Get-ChildItem $CLAUDIA_ROOT -Recurse -Include *.mjs,*.json,*.ps1,*.md | Select-String -Pattern "conversion-report" -List
```

The file that references `conversion-report.mjs` alongside other scripts is the supervisor list. Note its path for Tasks 5 and 6.

- [ ] **Step 3: Initialise a private git repo so every later task can commit**

```powershell
cd $CLAUDIA_ROOT
git init
# Keep secrets out before the first commit:
Add-Content .gitignore ".env`n*.secret*`n*token*`nnode_modules/"
git add -A
git commit -m "chore: snapshot Claudia system before 2026-08-29 fixes"
```

Optionally push to a new private GitHub repo (e.g. `takid/claudia-system`) so future remote sessions can work on this code directly. Every "Commit" step below commits in this repo.

---

### Task 1 (spec #7): Fix the cov-cleans-mcp write-tool path allowlist

All filesystem writes are broken because the allowlist is hardcoded to `C:\Users\CoventryCleans\...` while the real profile is on `D:`. Do this first — later tasks need working writes.

**Files:**
- Modify: the `cov-cleans-mcp` server source found in Task 0 (the allowlist constant)
- Test: `$CLAUDIA_ROOT\tests\allowlist.test.mjs` (create)

- [ ] **Step 1: Locate the hardcoded paths**

```powershell
Get-ChildItem $CLAUDIA_ROOT -Recurse -Include *.mjs,*.js,*.ts,*.json | Select-String -Pattern "C:\\\\Users\\\\CoventryCleans"
```

Every hit is a candidate; fix the allowlist in code, and re-root any config entries.

- [ ] **Step 2: Replace the hardcoded list with a derived one**

In the server, replace the constant (keeping any extra roots the old list had, re-rooted onto the profile dir):

```js
import os from "node:os";
import path from "node:path";

// Derive write roots from the real profile dir (D:\Users\CoventryCleans on this
// machine) instead of a hardcoded drive. CLAUDIA_FS_ROOT overrides for testing.
const PROFILE_ROOT = process.env.CLAUDIA_FS_ROOT ?? os.homedir();
const ALLOWED_WRITE_ROOTS = [PROFILE_ROOT].map((p) => path.resolve(p).toLowerCase());

export function isAllowedWritePath(target) {
  const resolved = path.resolve(target).toLowerCase(); // Windows paths are case-insensitive
  return ALLOWED_WRITE_ROOTS.some(
    (root) => resolved === root || resolved.startsWith(root + path.sep)
  );
}
```

Export `isAllowedWritePath` and use it in every write/edit/delete tool handler (it may already be a single shared check — keep that shape).

- [ ] **Step 3: Write the test**

`tests/allowlist.test.mjs`:

```js
import test from "node:test";
import assert from "node:assert/strict";

process.env.CLAUDIA_FS_ROOT = "D:\\Users\\CoventryCleans";
const { isAllowedWritePath } = await import("../src/allowlist.mjs"); // adjust to real path

test("allows paths under the real profile", () => {
  assert.equal(isAllowedWritePath("D:\\Users\\CoventryCleans\\Documents\\x.txt"), true);
});
test("is case-insensitive", () => {
  assert.equal(isAllowedWritePath("d:\\users\\coventrycleans\\notes.md"), true);
});
test("rejects other drives and prefix tricks", () => {
  assert.equal(isAllowedWritePath("C:\\Users\\CoventryCleans\\x.txt"), false);
  assert.equal(isAllowedWritePath("D:\\Users\\CoventryCleansEvil\\x.txt"), false);
});
```

- [ ] **Step 4: Run tests, then verify end-to-end**

Run: `node --test tests/` — expect PASS. Restart the MCP server (restart the Claude app or Cowork session), then ask Claudia to write a scratch file under `D:\Users\CoventryCleans` via its write tool. Expect success.

- [ ] **Step 5: Commit** — `git commit -am "fix: derive cov-cleans-mcp write allowlist from real profile dir"`

---

### Task 2 (spec #1): Auto-write quote status on send/approval

**Files:**
- Modify: whichever component sends quotes — a `cov-cleans-mcp` tool (preferred) or the quote skill's SKILL.md

- [ ] **Step 1: Locate the quote-send flow**

```powershell
Get-ChildItem $CLAUDIA_ROOT -Recurse -Include *.mjs,*.js,*.md | Select-String -Pattern "send_quote|quote sent|quotation" -List
```

- [ ] **Step 2 (if quotes are sent by a tool): fire the lead update inside the handler**

In the send-quote handler, after the send succeeds, call the same internal function `update_lead` uses — never leave it to the model:

```js
// after send succeeds
await updateLeadRecord(leadId, { status: "quoted", value: quoteTotal });
```

Do the same in the quote-approval path if it is a separate handler. If the handler doesn't currently receive `leadId`, add it to the tool's input schema as required.

- [ ] **Step 2 (if quotes are sent by skill instruction only): make the update a non-optional step**

Add to the quote skill immediately after the send step:

```markdown
## After sending or approving ANY quote (non-optional)
In the same turn, call `update_lead` with:
- lead_id: the lead this quote belongs to
- status: "quoted"
- value: the quoted total in GBP (number, no £ symbol)
Never defer this. If update_lead fails, retry once, then flag it in the daily summary.
```

- [ ] **Step 3: Verify** — send a test quote to coventrycleans@gmail.com; confirm the lead row shows `status=quoted` with the right value, with no manual step.

- [ ] **Step 4: Commit** — `git commit -am "feat: auto-update lead to quoted with value on quote send/approval"`

---

### Task 3 (spec #2): Contact-recovery pass before flagging "no contact"

**Files:**
- Create: `$CLAUDIA_ROOT\lib\extract-contacts.mjs`
- Test: `$CLAUDIA_ROOT\tests\extract-contacts.test.mjs`
- Modify: the lead-triage skill/script that sets the "no contact" status

- [ ] **Step 1: Write the failing test**

```js
import test from "node:test";
import assert from "node:assert/strict";
import { extractContacts } from "../lib/extract-contacts.mjs";

test("finds spaced UK mobile", () => {
  assert.deepEqual(extractContacts("call me on 07700 900123 ta").phones, ["07700900123"]);
});
test("finds +44 mobile and email", () => {
  const r = extractContacts("Reach Jo on +44 7700 900456 or jo@example.co.uk");
  assert.deepEqual(r.phones, ["+447700900456"]);
  assert.deepEqual(r.emails, ["jo@example.co.uk"]);
});
test("no false positives on money, dates, invoice numbers", () => {
  const r = extractContacts("Invoice INV-2026-0829, total £170.00, due 29/08/2026");
  assert.deepEqual(r.phones, []);
  assert.deepEqual(r.emails, []);
});
```

- [ ] **Step 2: Run it to make sure it fails** — `node --test tests/extract-contacts.test.mjs` → FAIL (module not found).

- [ ] **Step 3: Implement `lib/extract-contacts.mjs`**

```js
// UK mobiles: 07xxx xxxxxx or +44 7xxx xxxxxx, tolerant of spaces/dots/dashes/brackets.
const UK_MOBILE_RE = /(?:\+44[\s.-]?7\d{3}|\(?07\d{3}\)?)[\s.-]?\d{3}[\s.-]?\d{3}/g;
const EMAIL_RE = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g;

export function extractContacts(text) {
  const phones = [...new Set(
    (text.match(UK_MOBILE_RE) ?? []).map((p) => p.replace(/[^\d+]/g, ""))
  )];
  const emails = [...new Set((text.match(EMAIL_RE) ?? []).map((e) => e.toLowerCase()))];
  return { phones, emails };
}
```

- [ ] **Step 4: Run tests to verify they pass** — `node --test tests/extract-contacts.test.mjs` → PASS.

- [ ] **Step 5: Wire into triage**

In the skill/script that flags "no contact", insert before the flag is set:

```markdown
## Before flagging any lead "no contact" (non-optional)
Run the full source email/call body through `lib/extract-contacts.mjs`
(`node -e` one-liner or the helper tool). If it returns any phone or email:
save it to the lead, do NOT flag "no contact", and continue outreach with the
recovered contact instead. Only flag "no contact" when the extractor returns
nothing from every source message on the lead.
```

- [ ] **Step 6: Commit** — `git commit -am "feat: recover phones/emails from source text before flagging no-contact"`

---

### Task 4 (spec #3): Duplicate-booking guard for Connecteam shifts

**Files:**
- Create: `$CLAUDIA_ROOT\lib\shift-guard.mjs`
- Test: `$CLAUDIA_ROOT\tests\shift-guard.test.mjs`
- Modify: the shift-creation flow (Connecteam tool handler or booking skill) — locate with `Select-String -Pattern "connecteam" -List`

- [ ] **Step 1: Write the failing test**

```js
import test from "node:test";
import assert from "node:assert/strict";
import { findDuplicateShift } from "../lib/shift-guard.mjs";

const existing = [
  { id: "s1", clientName: "Mrs. O'Brien", startTime: "2026-09-01T09:00:00+01:00" },
];

test("same client, same slot (case/punctuation differ) is a duplicate", () => {
  const hit = findDuplicateShift(existing, { clientName: "mrs obrien", startISO: "2026-09-01T09:30:00+01:00" });
  assert.equal(hit?.id, "s1");
});
test("same client next day is not a duplicate", () => {
  assert.equal(findDuplicateShift(existing, { clientName: "Mrs. O'Brien", startISO: "2026-09-02T09:00:00+01:00" }), null);
});
test("different client same slot is not a duplicate", () => {
  assert.equal(findDuplicateShift(existing, { clientName: "J Patel", startISO: "2026-09-01T09:00:00+01:00" }), null);
});
```

- [ ] **Step 2: Run it to make sure it fails** — `node --test tests/shift-guard.test.mjs` → FAIL.

- [ ] **Step 3: Implement `lib/shift-guard.mjs`**

```js
const normalize = (s) =>
  s.toLowerCase().normalize("NFKD").replace(/[^a-z0-9]+/g, " ").trim();

// Same client + start within 1h counts as the same slot.
export function findDuplicateShift(existingShifts, { clientName, startISO }) {
  const target = normalize(clientName);
  const targetStart = new Date(startISO).getTime();
  return (
    existingShifts.find(
      (s) =>
        normalize(s.clientName ?? s.title ?? "") === target &&
        Math.abs(new Date(s.startTime).getTime() - targetStart) < 60 * 60 * 1000
    ) ?? null
  );
}
```

- [ ] **Step 4: Run tests to verify they pass** — `node --test tests/shift-guard.test.mjs` → PASS.

- [ ] **Step 5: Wire into shift creation**

If shifts are created by a tool handler: fetch that day's shifts from Connecteam first, run `findDuplicateShift`, and on a hit return an error naming the existing shift id/time instead of creating — with an explicit `force: true` input to override. If creation is skill-driven, add the equivalent non-optional pre-check step to the skill: list the day's shifts, run the guard, and only create on no hit or explicit "create anyway" from Taka.

- [ ] **Step 6: Verify** — attempt to double-book an existing test shift; expect the block/warning naming the original. Commit: `git commit -am "feat: block duplicate Connecteam shifts (same client + slot)"`

---

### Task 5 (spec #4): Retire or fix conversion-report.mjs

**Files:**
- Modify or delete: `conversion-report.mjs`; Modify: the supervisor list found in Task 0

- [ ] **Step 1: Diagnose why output is zero**

Run `node conversion-report.mjs` by hand and log the data-loading step (source path/URL + row count). Two likely causes: it reads a `C:\Users\...` path (fixed data location — Task 1's grep will have flagged it) or it points at a stale/empty source.

- [ ] **Step 2: Decide — fix if a real quote source exists, otherwise retire**

**Fix path:** repoint the loader at the live quote data (the quotations store that Task 2 now keeps current), and make emptiness loud so the supervisor surfaces failure instead of silent zeros:

```js
if (rows.length === 0) {
  console.error(`conversion-report: 0 quote rows from ${SOURCE}; refusing to emit an empty report`);
  process.exit(1);
}
```

Verify: run it; expect real quote counts and a conversion percentage that matches a manual spot-check of last month's quotes.

**Retire path (if there is no live source to wire to):** remove its entry from the supervisor list and `git rm conversion-report.mjs`. Dead automation is worse than none.

- [ ] **Step 3: Commit** — `git commit -am "fix: wire conversion report to live quote data (or: chore: retire dead conversion report)"`

---

### Task 6 (spec #5): Same-day nudge for stale "needs_approval" posts

**Files:**
- Create: `$CLAUDIA_ROOT\stale-approval-nudge.mjs` (or extend the existing social supervisor script)
- Modify: the supervisor list (add/replace the count-only check)

The queue is cc-social-scheduler's `Post` table: `status = needs_approval`, `updatedAt` is the last status change (`@updatedAt`), so it's the "sat since" proxy.

- [ ] **Step 1: Query posts stale past 24h**

With DB access (Prisma client from the scheduler project):

```js
const stale = await prisma.post.findMany({
  where: { status: "needs_approval", updatedAt: { lt: new Date(Date.now() - 24 * 3600 * 1000) } },
  orderBy: { updatedAt: "asc" },
  select: { id: true, title: true, scheduledFor: true, updatedAt: true },
});
```

Without DB access, use the app's API — `GET /api/posts?status=needs-approval` (note the hyphen in the API status) — and filter on `updatedAt` in the script.

- [ ] **Step 2: Send an actionable ping, not a count**

Only when `stale` is non-empty, send via the same channel Claudia's other nudges use, one line per post:

```
⚠️ 2 posts stuck in approvals >24h:
• "Bank holiday deep-clean offer" — waiting 31h, scheduled Mon 18:30 → approve: <scheduler URL>/approvals
• "Before/after: oven rescue" — waiting 26h, scheduled Tue 12:00 → approve: <scheduler URL>/approvals
```

De-dupe so each post pings at most once per day: keep `{ postId: lastNudgedISO }` in a small state JSON next to the script and skip posts nudged in the last 24h.

- [ ] **Step 3: Verify** — set a test post to `needs_approval`, backdate `updatedAt` 25h in the DB, run the script: expect one ping naming that post; run again: expect silence (de-dupe). Note: `updatedAt` resets on any edit — acceptable; add a dedicated `approvalRequestedAt` column later only if this proves too fuzzy.

- [ ] **Step 4: Commit** — `git commit -am "feat: nudge on posts stuck in needs_approval past 24h"`

---

### Task 7 (spec #6): One owner for the WhatsApp Chrome session

Root cause: `open_whatsapp` and the `chrome` MCP server launch/attach Chrome with the same `--user-data-dir`; Chrome's ProcessSingleton lock means the second one fails or hijacks the window, so the send-confirmation step never sees the page it expects.

**Files:**
- Modify: wherever `open_whatsapp` spawns Chrome (its MCP server source or config found in Task 0)

- [ ] **Step 1: Confirm the shared profile**

Grep both servers' configs/source for `--user-data-dir` (and for a bare launch with no flag, which means the default profile — same conflict).

- [ ] **Step 2: Give WhatsApp its own dedicated profile**

In `open_whatsapp`'s launch args, add:

```
--user-data-dir=%LOCALAPPDATA%\claudia\whatsapp-profile
```

(expand `%LOCALAPPDATA%` in code: `path.join(process.env.LOCALAPPDATA, "claudia", "whatsapp-profile")`, `fs.mkdirSync(..., { recursive: true })` before first launch). This makes each tool sole owner of its own Chrome session; the profile persists the WhatsApp Web login, so it costs one QR re-scan on first run and never contends with the `chrome` MCP again. (Alternative if preferred: delete `open_whatsapp` and drive web.whatsapp.com through the `chrome` MCP session — one owner either way. The dedicated profile is the smaller change.)

- [ ] **Step 3: Verify the actual failure is gone** — in one Claudia session, use the `chrome` MCP on any page AND send a WhatsApp message via `open_whatsapp`: both must hold their own windows, and the send-confirmation check must report the message as sent.

- [ ] **Step 4: Commit** — `git commit -am "fix: dedicated Chrome profile for open_whatsapp to end profile lock contention"`

---

## Self-review notes

- Spec coverage: spec items 1–7 map to Tasks 2, 3, 4, 5, 6, 7, 1 respectively; Task 0 is enabling work.
- Paths marked `$CLAUDIA_ROOT` are deliberately discovered in Task 0/locate steps, not guessed — the runtime is not in git yet. Once Task 0's repo is pushed to GitHub, future fixes can be implemented remotely against real source instead of via locate-first plans.
