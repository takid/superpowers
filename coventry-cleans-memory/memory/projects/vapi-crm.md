# Vapi, calls and CRM

## Done
- Call screening deployed (25 Sep): Daniel answers all calls, Katie removed, cold callers blocked from reaching Taka.
- Design spec: docs/superpowers/specs/2026-09-24-vapi-call-breakdown-design.md.
- Taskade backup taken 24 Sep (_archive/taskade-backup-2026-09-24/).

## Broken or unfinished
1. **Vapi → Taskade webhook returning 404** for 3+ weeks. Calls aren't reaching CRM.
2. **Phase 2 GO-LIVE (8 Sep) never ran.** Sales Pipeline and Quotations tables hold 0 rows. 37 leads sit in _scripts/phase2-backfill-data.json.
3. **Follow-up cadence (2h / 24h / 48h / 5d)** reads 02-sales/pipeline/leads.json, which holds 0 leads, so nothing is chased.
4. **Taskade CRM is publicly readable and deletable.** Remediation doc: 08-company/admin/2026-09-24-taskade-public-exposure-remediation.md. Fix this first.
5. **Make.com scenario "Katie Recruitment Call Report"** still emails every Vapi end-of-call report, including real customer enquiries, because Vapi still points at Katie's webhook. Daniel's scenario exists but ran twice.

## Fix order
1. Lock down Taskade. 2. Repoint Vapi server URL to Daniel's webhook (Taka supplies URL), then remove Katie's email route (keep its GBP posting). 3. Decide if the 37 leads are current and load into the real Leads Database. 4. Point follow-up cadence at the live source.

Real Leads Database is the one used by the MCP servers and dashboards. Not the Sales Pipeline table.
