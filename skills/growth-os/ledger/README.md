# Ledger

Single append-only table. Google Sheet `Growth Ledger`, tab `ledger`. File ID: _record here on first run_.

## Schema

| Column | Type | Rule |
|--------|------|------|
| row_id | string | `YYYYMMDD-<agent>-<seq>` |
| ts | ISO datetime | When the action happened, Europe/London |
| agent | enum | One of the 11 agents |
| action | enum | `enquiry`, `reply`, `quote`, `follow_up`, `booking`, `job_completed`, `invoice`, `reminder`, `review_ask`, `review_reply`, `post`, `gbp_post`, `outreach`, `rota_change`, `renewal_offer`, `referral_ask`, `hire_step`, `outcome` |
| channel | enum | `email`, `whatsapp`, `phone`, `web_form`, `gbp`, `facebook`, `instagram`, `linkedin`, `tiktok`, `nextdoor`, `referral`, `direct` |
| segment | string | `<client_type>/<postcode>/<service>` e.g. `domestic/CV5/deep-clean`, `b2b-agent/CV6/end-of-tenancy` |
| variant | string | Playbook variant ID, e.g. `lr-first-reply-v2` |
| contact_ref | string | Email, phone, or CRM ID. Never the name alone. |
| value_gbp | number | Quoted or booked value, blank if none |
| outcome | enum | Only on `action=outcome` rows: `replied`, `quoted`, `booked`, `lost`, `completed`, `paid`, `reviewed`, `renewed`, `churned`, `referred`, `no_reply` |
| ref_row_id | string | For outcome rows: the row they close |
| note | string | One line. No essays. |

## Example rows (`ledger/example.csv`)

See the file. Two enquiries, one quoted and booked, one that went silent.

## Rules

- Append only. Corrections are new rows with `note: corrects <row_id>`.
- One row per action. A reply to three leads is three rows.
- Personal data stays minimal: contact_ref only, no addresses, no card details, no notes about the person.
- Outcome rows are written by whichever agent sees the outcome first.
- `no_reply` is written when the owning agent's wait window closes (lead-responder 48h, quote-closer 7 days, prospector 14 days).
