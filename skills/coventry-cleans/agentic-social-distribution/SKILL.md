---
name: agentic-social-distribution
description: "RETIRED. Superseded by daily-content-machine. Do not invoke. This skill is kept only as a redirect stub; it has no functionality of its own."
---

# RETIRED — use `daily-content-machine`

This skill has been retired. If it has somehow been invoked, stop and use
`daily-content-machine` instead.

## Why

It was a strict subset of `daily-content-machine`: the same brand voice rules, the same
platform table, the same post structure, the same output folders, the same publishing step.
It had no Full Mode and no intelligence scan.

Worse, its description ended with "Always use this skill for any social media or marketing
distribution task" — and so did `daily-content-machine`'s. Two skills claiming the same
trigger meant which one fired was a coin toss, and they carried different content. Same
brief, different output, depending on luck.

It also carried the two defects fixed in `daily-content-machine`:

- Hardcoded hourly prices (`from £15/hr`, `from £18/hr`) that were never checked against
  fully loaded cost
- A "Send to Buffer (via MCP)" step routed at a Buffer MCP server that is not connected and
  never was

## Action required

**Delete this skill from the claude.ai account.** This stub stops it winning the trigger,
but it will keep appearing in the skill list until it is removed at source.

Everything it did now lives in:

- `skills/coventry-cleans/daily-content-machine/SKILL.md` — the skill
- `skills/coventry-cleans/pricing.md` — prices
- `skills/coventry-cleans/publishing.md` — distribution routes
