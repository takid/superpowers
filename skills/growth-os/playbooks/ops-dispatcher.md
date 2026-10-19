# ops-dispatcher playbook

## Current best

**Assignment (seed):** nearest available cleaner to the postcode first; end of tenancy, post-renovation and first visits for new recurring clients go to the senior list. Same cleaner for every recurring visit unless unavailable.

**Senior list:** _Taka to fill_

**Client confirmation `od-confirm-v1` (seed):**
> Hi [first name], you're booked for a [service] on [date], arrival between [window]. [Cleaner first name] will be with you. Please have [parking / keys / hot water] sorted and anything fragile put away. Price [£X], payable on the day by [method]. 24 hours' notice for changes. Coventry Cleans, 07544 308764.

**Day-before reminder `od-remind-v1`:** one line, window, cleaner first name.

**Cleaner acknowledgement cutoff:** 18:30 the day before. Reassign at 18:31.

**Issue codes for job_completed notes:** late, access, complaint, extra-work, damage, no-show-client.

**Utilisation bands:** below 60% demand problem, 60-85% healthy, above 85% for 14 days triggers capacity-recruiter.

## Live experiment

- Hypothesis: naming the cleaner in the confirmation reduces day-of cancellations.
- Control: `od-confirm-v1` with name. Test: `od-confirm-v2` without name.
- Metric: cancellations within 24h / bookings. Min sample: 30 per arm. Rule: control holds unless test is better by 15%.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
