---
name: growth-os
description: Use when running, reviewing, or scheduling any Coventry Cleans growth, sales, marketing, operations, or cash activity - new enquiries, quotes, follow-ups, content, reviews, scheduling, invoicing, hiring, weekly numbers, or "what should we do next"
---

# Growth OS

## Overview

Growth OS is the operating layer for Coventry Cleans. Eleven role agents run the business day to day. Every action they take lands in one ledger. One learning agent reads that ledger each week and rewrites the playbooks the other agents run from. That is the whole loop: **act → record → score → rewrite playbook → act better.**

Nothing compounds without the ledger. An action that is not recorded did not happen.

**Core principle:** Agents run free on everything routine. Taka is on the loop, not in it, and only for three things: money leaving the business, first contact with a private individual who has not asked to hear from us, and hiring. See `gates.md`.

## The agents

| Agent | Owns | Fires on |
|-------|------|----------|
| growth-director | Allocation, bottleneck, dispatch | Daily 07:00, weekly, any metric moving 20%+ |
| lead-responder | First reply inside 5 minutes | New enquiry on any channel |
| quote-closer | Quote → booking | Quote sent, no booking |
| prospector | B2B pipeline (hunter) | Daily 09:00 |
| local-authority | Google Business, SEO, GEO, citations | Daily 10:00, new review |
| content-engine | Daily posts across platforms | Daily 08:00 |
| reputation | Review asks and replies | Job completed, new review |
| ops-dispatcher | Cleaner rota, capacity, job confirmations | Booking made, 17:00 daily |
| retention-referral | Recurring clients, churn, referrals | Job completed, 30/60/90 days |
| cash-collector | Invoices, chasing, DSO | Job completed, daily 11:00 |
| capacity-recruiter | Cleaner supply | Utilisation above 85% |
| learning-loop | Playbook rewrites, experiments | Monday 06:30, on trigger |

Agent definitions live in `agents/`. Each one names its inputs, its autonomy tier, what it writes to the ledger, and who it hands off to.

## How to run it

1. **Identify the trigger** (time, event, or Taka's request).
2. **Read the playbook** for the agent at `skills/growth-os/playbooks/<agent>.md`. The `Current best` section is the law. Never act from memory of an old version.
3. **Dispatch the agent** with the trigger, the playbook, and the relevant ledger rows. Nothing else. Use superpowers:dispatching-parallel-agents when several triggers are independent.
4. **Agent acts, then writes ledger rows** in the schema at `ledger/README.md`.
5. **Anything gated** goes to the approvals tab, not to Taka's chat, unless it is urgent.
6. **Report** in the format at the end of this file.

Supporting files:
- `scoreboard.md` - the numbers, formulas, targets, and where data lives
- `feedback-loop.md` - the closed loop, experiment rules, playbook rewrite rules
- `gates.md` - what runs free, what queues, auto-decisions on silence
- `coverage-map.md` - Coventry saturation grid by postcode and channel
- `schedule.md` - the cadence and the scheduled-task prompts to paste

## Hands off to existing skills

Do not rebuild what already exists. Agents call these by name:
- `anthropic-skills:daily-content-machine` - content-engine
- `anthropic-skills:daily-hunter` - prospector
- `anthropic-skills:coventry-cleans-payment-chaser` - cash-collector
- `anthropic-skills:morning` - growth-director daily brief (pass `Sections: Growth OS`)
- `anthropic-skills:competitor-intel` - learning-loop, monthly

## Red flags

| Thought | Reality |
|---------|---------|
| "I'll just reply to this lead myself" | Use lead-responder. Its playbook has the current best reply. |
| "No need to log this one" | Unlogged work cannot be learned from. Log it. |
| "The playbook says X but Y feels better" | Run Y as an experiment under feedback-loop rules. Do not freelance. |
| "Taka should sign this off" | Check gates.md. If it is not listed, it is not gated. |
| "Let's add another tool" | Simple systems that run beat clever ones that stall. |

## Report format

```
GROWTH OS - [date] - [trigger]
Agents run: [list]
Ledger rows written: [n]
Bottleneck this week: [stage] ([metric] vs target)
Needs Taka: [n] items in approvals (or "none")
Next scheduled run: [agent] at [time]
```
