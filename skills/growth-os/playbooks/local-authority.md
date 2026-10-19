# local-authority playbook

## Current best

**GBP post `la-gbp-v1` (seed):** 60-100 words. Line 1 names the service and area the way someone would say it to a phone ("Looking for an end of tenancy cleaner in Canley, CV4?"). One visible price. One trust line (insured, local team, checklist). One CTA with the number. No hashtags, no emojis.

**Service rotation:** end of tenancy, deep clean, office, post-renovation, recurring domestic. Weighted to the month's priority cells.

**Area page template `la-page-v1` (seed):** H1 "[Service] in [Area], Coventry [Postcode]". Sections: what's included, pricing logic with the from-price, three local references, who it's for, a 5-question FAQ written as spoken questions, a review quote naming the area, CTA. 600-900 words. Schema: LocalBusiness plus FAQPage.

**Citation set to keep identical to GBP:** Yell, Checkatrade, Bark, Thomson Local, Bing Places, Apple Maps, Nextdoor business page, Facebook page, Yelp.

**Review naming line (given to reputation):** "If you can mention [area] and the [service] in the review, it helps other people nearby find us."

**Top 10 tracked terms (seed):** end of tenancy cleaning coventry, deep cleaning coventry, cleaner coventry, office cleaning coventry, house cleaning coventry, cleaning company coventry, end of tenancy clean cv4, cleaner earlsdon, cleaner kenilworth, after builders clean coventry.

## Live experiment

- Hypothesis: GBP posts that open with a spoken question get more GBP actions than posts that open with the service name.
- Control: `la-gbp-v1`. Test: `la-gbp-v2` service-name opener.
- Metric: GBP actions per post (from insights). Min sample: 10 posts per arm. Rule: +15% relative.

## Learned

- 2026-10-19 - Seeded.

## Retired

None.
