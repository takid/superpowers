# lead-responder playbook

## Current best

**Speed (seed):** reply inside 5 minutes 07:00-21:00, inside 30 minutes outside. Never leave an enquiry to the morning.

**Price book (from brand rules; Taka confirms end of tenancy table):**
| Service | Price |
|---------|-------|
| Standard / recurring clean | from £15/hr, 3 hr minimum |
| Deep clean | from £120 |
| Office clean | from £18/hr |
| End of tenancy | by bedrooms, quote from the table in Taka's price sheet |

**First reply, variant `lr-first-reply-v1` (seed, domestic):**
> Hi [first name], thanks for getting in touch. We cover [area] regularly. For a [service] on a [bedrooms]-bed it's [price or "from £X"]; that includes [two inclusions]. I can do [slot 1] or [slot 2]. Does either work? If you can tell me roughly the condition and whether there's parking, I'll confirm the price straight back. Coventry Cleans, 07544 308764.

**First reply, `lr-first-reply-v1` (seed, landlord or agent):**
> Hi [first name], thanks for the enquiry about [address or area]. We do a lot of end of tenancy work in [postcode] for landlords and agents, with a checklist-based clean and photos on completion. For a [bedrooms]-bed it's typically [price]. When does the property become empty? I can hold a slot that week. Coventry Cleans, 07544 308764.

**Qualifying questions:** bedrooms and bathrooms, condition, date, parking or access. Max three per message.

**Channel rule (seed):** reply on the channel they used. Phone enquiries get a WhatsApp or text summary within 10 minutes of the call.

**Always:** visible price when the price book allows, two slots, first name, no exclamation marks.

## Live experiment

- Hypothesis: a price in the first reply closes more than "I'll send a quote".
- Control: `lr-first-reply-v1` with "from £X". Test: `lr-first-reply-v2` with the exact price-book figure and the two inclusions.
- Segment: domestic, all postcodes. Metric: close rate (booked / enquiries). Min sample: 30 per arm or 14 days.
- Start: first run. Rule: test wins at +15% relative.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
