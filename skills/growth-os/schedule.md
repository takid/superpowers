# Schedule

Times are Europe/London. Minimum interval on scheduled tasks is hourly, so the enquiry sweep runs hourly and real-time replies rely on Gmail and WhatsApp triggers through Zapier or Make.

## Cadence

| Time | Run | Agent |
|------|-----|-------|
| Every hour, 07:00-21:00 | Enquiry sweep: unanswered enquiries older than 5 min | lead-responder |
| 06:30 Monday | Learning loop | learning-loop |
| 07:00 daily | Stand-up: scoreboard glance, bottleneck, dispatch list, morning brief with `Sections: Growth OS` | growth-director |
| 08:00 daily | Content machine (Full Mode Mon/Wed/Fri, Quick Mode other days to the weakest coverage cell) | content-engine |
| 09:00 daily | Daily hunter | prospector |
| 10:00 daily | Google Business post, review check, citation check | local-authority |
| 11:00 daily | Invoices for yesterday's completed jobs, reminders due | cash-collector |
| 14:00 daily | Quote follow-ups due | quote-closer |
| 17:00 daily | Tomorrow's rota confirmations, gaps, cleaner reminders | ops-dispatcher |
| 18:00 daily | Review asks for today's completed jobs, 30/60/90 day touches | reputation, retention-referral |
| First Monday monthly | Competitor intel, coverage map update, strategy note | learning-loop, growth-director |
| On trigger | Utilisation above 85% for 2 weeks | capacity-recruiter |

## Scheduled-task prompts

Create one scheduled task per row with the prompt below. Each starts from a fresh session, so the prompt names the skill and agent.

**Stand-up (07:00 daily)**
```
Use the superpowers:growth-os skill. Run growth-director for the daily stand-up: read the scoreboard and ledger, name the bottleneck, list today's dispatches, surface open approvals, then produce the morning brief with Sections: Growth OS. Do not ask questions; use playbook defaults.
```

**Enquiry sweep (hourly)**
```
Use the superpowers:growth-os skill. Run lead-responder: find every enquiry in Gmail and WhatsApp exports without a reply older than 5 minutes, reply per the playbook Current best, log each to the ledger. Report count and median response time.
```

**Learning loop (Monday 06:30)**
```
Use the superpowers:growth-os skill. Run learning-loop for the last 7 and 28 days: decide live experiments, rewrite playbook Current best sections, write the scoreboard tab, start next experiments, hand growth-director the weekly allocation.
```

**Content (08:00 daily)**
```
Use the superpowers:growth-os skill. Run content-engine: read coverage-map weakest cells and the content-engine playbook, then run anthropic-skills:daily-content-machine in the mode the playbook specifies. Log every post as a ledger row with its variant ID.
```

**Cash (11:00 daily)**
```
Use the superpowers:growth-os skill. Run cash-collector: invoice yesterday's completed jobs, then run anthropic-skills:coventry-cleans-payment-chaser for reminders due. Log rows. Queue any third reminder to approvals.
```

Cron (UTC in winter, adjust with CRON_TZ=Europe/London): stand-up `52 6 * * *`, hourly sweep `0 7-21 * * *`, learning loop `23 6 * * 1`, content `52 7 * * *`, hunter `52 8 * * *`, cash `52 10 * * *`.
