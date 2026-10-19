# cash-collector playbook

## Current best

**Invoice timing (seed):** same morning as completion, before 11:00. Domestic due on receipt. Commercial default 14 days unless the client record says otherwise.

**Reminder schedule (seed):** reminder 1 at due +3 days, reminder 2 at due +10 days, reminder 3 queued for Taka at due +17 days. Payment chaser templates and tone apply.

**Sanity check before sending:** name matches invoice, amount matches tracker, invoice not marked paid in the last 48 hours.

**Commercial 30+ days:** growth-director gets a line; Taka or the account owner calls. No automated fourth touch.

**Payment methods on every invoice:** bank transfer with invoice number as reference, payment link when QuickBooks is connected.

## Live experiment

- Hypothesis: a payment link on the invoice cuts domestic days-to-pay versus bank details only.
- Control: bank details only. Test: link plus bank details.
- Metric: days-to-pay, domestic. Min sample: 30 per arm. Rule: test wins if 2+ days faster on the median.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
