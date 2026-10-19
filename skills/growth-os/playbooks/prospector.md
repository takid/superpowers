# prospector playbook

## Current best

**Weekly focus rotation (seed):** Mon letting agents, Tue landlords and HMO operators, Wed offices and business parks, Thu care and healthcare, Fri Airbnb and short-let hosts plus post-renovation contractors.

**Qualification:** daily-hunter score 6+ only. Business contact details only.

**Outreach variants (seed, use daily-hunter templates):**
- Agents and landlords: `pr-agent-v1` = Template 3 (partnership, fixed rates, 24-48h turnaround, photos on completion).
- Offices and care: `pr-office-v1` = Template 1 (specific observation, two services, flexible scheduling).
- Pain point found: `pr-pain-v1` = Template 2.

**Personalisation rule:** the first sentence must contain something only true of them. No first sentence, no send.

**Follow-up (seed):** +4 days different angle (case study), +10 days last touch (offer a free site walk-round). +14 days silent: `no_reply`.

**Partner offer for agents (seed):** fixed rate card by bedrooms, priority slots, one invoice a month, checklist and photos per property.

## Live experiment

- Hypothesis: offering a free site walk-round in the first message lifts reply rate over a 10-minute call ask.
- Control: `pr-agent-v1` call ask. Test: `pr-agent-v2` walk-round ask.
- Segment: b2b-agent. Metric: reply rate. Min sample: 30 per arm. Rule: +15% relative.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
