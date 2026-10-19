# Coverage Map - Coventry saturation grid

Saturation means: in every area we serve, someone looking for a cleaner finds Coventry Cleans first on Google, sees a recent review from their own postcode, and has seen us on their local feed this month.

## Areas

| Postcode | Areas | Core profile | Priority services |
|----------|-------|--------------|-------------------|
| CV1 | City centre, Hillfields | Flats, students, offices, Airbnb | End of tenancy, office, short-let turnover |
| CV2 | Walsgrave, Wyken, Stoke, Bell Green | Family homes, UHCW hospital area | Recurring domestic, deep clean |
| CV3 | Cheylesmore, Binley, Willenhall, Finham, Stivichall | Family and professional homes | Recurring domestic, deep clean, end of tenancy |
| CV4 | Canley, Tile Hill, Westwood Heath, Warwick Uni | Student lets, HMOs, new builds | End of tenancy, post-renovation, HMO |
| CV5 | Earlsdon, Coundon, Allesley, Chapelfields | Premium homes, professionals | Recurring domestic, deep clean |
| CV6 | Radford (home base), Holbrooks, Foleshill, Keresley | Dense terraces, landlords, small commercial | End of tenancy, landlord contracts, small office |
| CV7 | Bedworth, Exhall, Keresley End, Meriden | Suburban, small business parks | Office, recurring domestic |
| CV8 | Kenilworth, Ryton, Wolston | Premium homes, commuter | Deep clean, recurring premium |
| CV10-12 | Nuneaton, Bedworth | Volume domestic, industrial units | Office, recurring domestic |
| CV31-34 | Leamington, Warwick | Premium homes, lettings | End of tenancy, premium recurring |

Expansion rule: a new postcode opens only when the adjacent one hits 3 reviews and 5 recurring clients. Depth before width.

## Channel grid

One row per postcode per month in the `coverage` tab. Status per cell: `none`, `started`, `live`, `saturated`.

| Postcode | GBP posts naming area | Reviews naming area | FB/IG posts | Nextdoor | Landing page / FAQ | Landlord/agent partner | Recurring clients | Status |
|----------|------------------------|---------------------|-------------|----------|--------------------|------------------------|-------------------|--------|

Saturated means: 2+ GBP posts a month, 3+ reviews naming the area, 4+ social posts a month, 1 Nextdoor post a month, a live area page, at least one partner, 5+ recurring clients.

## Who fills what

- local-authority: GBP posts, area pages, citations, review naming.
- content-engine: social and Nextdoor by postcode rotation, weighted to the weakest cells.
- prospector: partner column.
- retention-referral: recurring clients column.
- learning-loop: monthly status update and the next month's priority cells.

## Monthly priority

growth-director picks the 3 cells with the highest expected return: a postcode with enquiries but no reviews, or reviews but no content, or a partner but no recurring base. Those 3 cells get the month's spare effort.
