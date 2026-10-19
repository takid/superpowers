# Scoreboard

One sheet, one tab per week, filled by growth-director every Monday 07:00 from the ledger. Every number has a formula and a source. No number without a source goes on the board.

## Where data lives

| Store | What | Access |
|-------|------|--------|
| Google Sheet `Growth Ledger` | Tabs: `ledger`, `scoreboard`, `experiments`, `approvals`, `coverage` | Google Drive MCP (`read_file_content`, `update_file`). Create it on first run if missing and record the file ID in `ledger/README.md`. |
| Google Sheet payment tracker `1D_O1mzukxImLDVs1h5DqyJoi0_QSxfGaBM5sFCEGc78` | Invoices and chasing | cash-collector reads and updates |
| Gmail `cleaning@coventrycleans.co.uk` | Enquiries, quotes, replies | Gmail MCP |
| Google Calendar | Jobs, site visits | Calendar MCP |
| Connecteam | Cleaner rota, job sheets | Via Zapier/Make webhook or manual export |
| Buffer | Scheduled posts | Buffer MCP (needs auth in the session) |

## The funnel

```
Reach → Enquiry → Replied in time → Quoted → Booked → Completed → Paid → Reviewed → Repeat/Referred
```

The bottleneck is the stage with the largest gap between actual and target rate. growth-director puts the week's spare effort there and nowhere else.

## Metrics

| # | Metric | Formula | Source | Starting target | Compounding rule |
|---|--------|---------|--------|-----------------|------------------|
| 1 | Enquiries / week | count(ledger, action=enquiry) | ledger | baseline week 1 | +10% every 4 weeks |
| 2 | Speed to lead (median min) | median(first_reply_at - enquiry_at) | ledger | under 5 min in hours, under 30 min out of hours | hold |
| 3 | Quote rate | quoted / enquiries | ledger | 80% | hold |
| 4 | Close rate | booked / quoted | ledger | 35% | +2 pts every 4 weeks until 50% |
| 5 | Average job value | sum(value) / booked | ledger | track | +5% per quarter via mix |
| 6 | Recurring share | recurring bookings / bookings | ledger | 40% | +5 pts per quarter |
| 7 | Revenue / week | sum(value, completed) | ledger | baseline | +10% every 4 weeks |
| 8 | Capacity utilisation | booked hours / available cleaner hours | Connecteam + calendar | 75 to 85% | trigger recruiter above 85% |
| 9 | Reviews / week and rating | count, mean | Google Business | 3 per week, 4.8+ | hold |
| 10 | Google Business actions | calls + directions + site clicks | GBP insights | baseline | +10% every 4 weeks |
| 11 | Cash: DSO (days) | mean(paid_at - invoiced_at) | payment tracker | under 7 domestic, under 30 commercial | hold |
| 12 | Churn (recurring) | lost recurring / active recurring, monthly | ledger | under 5% | hold |
| 13 | Referral share | enquiries with source=referral / enquiries | ledger | 15% | +3 pts per quarter |
| 14 | B2B pipeline value | sum(value, stage in quoted, proposal) | ledger | baseline | +15% per month |

## Rules

- Week 1 sets baselines. No target is set before a baseline exists.
- A metric that misses target two weeks running is the learning-loop's first job that Monday.
- A metric that beats target by 20%+ gets its target raised the same week. Growth is not allowed to coast.
- Vanity numbers (likes, followers, impressions) are recorded in the ledger but never on the scoreboard. They do not pay cleaners.

## Weekly scoreboard tab layout

```
week_start | metric | actual | target | delta | trend_4wk | bottleneck_flag | note
```
