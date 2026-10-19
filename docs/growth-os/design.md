# Growth OS design note

Date: 2026-10-19

## What it is

A growth operating layer for Coventry Cleans, built inside the superpowers plugin so it loads wherever the plugin does. Eleven role agents, one entry skill, one ledger, one learning agent that rewrites the playbooks the others run from.

## Why this shape

- **Agents as files, not code.** The plugin already treats `agents/*.md` and `skills/*/SKILL.md` as first-class. No runtime to maintain. Taka can edit a playbook in a text editor and the next run picks it up.
- **One ledger, append only.** Every outcome in one table is what makes variant-level learning possible. Spread across six tools it would never be compared.
- **Playbooks are the memory.** The learning loop rewrites `Current best`; the agents read it at dispatch. That is the compounding mechanism. No vector store, no fine-tuning, no extra service.
- **Bottleneck allocation.** Spare effort goes to one funnel stage a week. A local service business does not have the volume to improve six things at once.
- **Depth before width.** Coverage map expands to a new postcode only when the adjacent one is saturated. Saturation is defined in numbers, not vibes.
- **Gates, not bottlenecks.** Under 2% of actions wait for Taka, every one of them auto-resolves on silence, and the list is short enough to fit on one screen. The brief said "no human bottlenecks"; money leaving the business and consumer electronic marketing without consent are the two places where that would be a liability rather than a growth lever.

## What is deliberately not built

- A dashboard app. The scoreboard tab plus the morning brief section is enough until the ledger has eight weeks of data.
- A CRM. The ledger plus Gmail plus the calendar is the CRM for now. The ledger schema is CRM-shaped so it can be imported later.
- Paid ads automation. Ads are gated. Organic and referral come first because they compound and cost nothing.

## Dependencies on connected tools

| Need | Tool | Status |
|------|------|--------|
| Ledger, scoreboard, approvals | Google Sheets via Drive MCP | connected |
| Enquiries, replies, invoices | Gmail MCP | connected |
| Jobs, site visits | Google Calendar MCP | connected |
| Posts | Buffer MCP | needs auth each session |
| Invoices, payment links | QuickBooks MCP | connected |
| Cleaner rota | Connecteam | export or Zapier feed |
| Rankings | Semrush MCP | connected |
| WhatsApp, Facebook messages | none | drafted and flagged `channel_manual` until a connector exists |

## Rollout

1. Week 0: create the Growth Ledger sheet, record its ID in `ledger/README.md`, fill the senior cleaner list and the end of tenancy price table in the playbooks.
2. Week 1: run stand-up, lead-responder sweep, content, cash by hand once each to check the handoffs. Set baselines.
3. Week 1 end: create the scheduled tasks from `schedule.md`.
4. Week 2: first learning-loop run. Experiments start.
5. Week 8: every `seed` rule should have been replaced or confirmed by a cited rule.

## Testing

`tests/growth-os/validate.sh` checks structure: every agent has a file, a playbook with four sections, valid frontmatter, and is listed in the skill. Behavioural testing follows `skills/writing-skills` once the first week of ledger rows exists.
