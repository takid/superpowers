---
name: competitor-intel
description: >
  Run deep competitor intelligence for Coventry Cleans. Use this skill whenever Taka mentions a competitor, asks what other cleaning companies are doing, wants to analyse rival businesses, or says anything like "check what [company] is up to", "who are our competitors", "what ads are they running", "analyse their social media", "what's [competitor] doing on Facebook/Instagram/Google", "run competitor analysis", "spy on competitors", "weekly competitor check", "what are other cleaners doing in Coventry", or "what should we do about [competitor]". Also trigger when the user asks about market positioning, competitive gaps, or wants to know how to outmanoeuvre a rival. Always use this skill for any competitive research, market intelligence, or rival monitoring task — even if the user doesn't explicitly say "competitor".
---

# Competitor Intel — Coventry Cleans

This skill helps Taka systematically track, analyse, and outmanoeuvre cleaning competitors in Coventry and Warwickshire. The goal is always intelligence that leads to action — not just information.

## When This Runs

Two modes:

**Deep Dive Mode** — Full analysis of one or more named competitors. Use when Taka names a specific company or asks for a detailed breakdown.

**Weekly Sweep Mode** — Lightweight recurring scan across all known competitors. Use when Taka says "run the weekly check", "Monday sweep", or asks for a general competitive update.

If the user hasn't specified, ask: "Do you want a full deep dive on a specific competitor, or the weekly sweep across all of them?"

---

## Known Coventry Cleaning Competitors (Seed List)

Start here when no specific competitor is named. Search to discover others.

- Merry Maids Coventry
- Fantastic Cleaners Coventry
- Bright & Beautiful Coventry
- Local independent cleaning companies (search: "cleaning company Coventry" on Google Maps)
- Oven cleaning specialists in Coventry
- End of tenancy specialists in Coventry

Expand this list dynamically based on what you find.

---

## PILLAR 1: Competitor Advertising Methods

**What to find:**
- Active Google Ads (search the competitor name + target service keywords, note if ads appear)
- Facebook/Instagram ads (check their Facebook page → "Page Transparency" → "See All Ads")
- Any paid promotions on local directories (Bark, Checkatrade, Yell, etc.)

**Search queries to use:**
- `[Competitor Name] Coventry cleaning services` (check if they appear in paid positions)
- `"[Competitor Name]" Facebook ads`
- `site:facebook.com/ads [competitor name]`

**What to capture:**
- Ad headlines and body copy (exact wording matters)
- Their CTA (what action they're pushing people towards)
- Their main offer or hook (discount, guarantee, free quote, etc.)
- Platforms they're active on vs. absent from
- Estimated frequency (one-off campaign vs. always-on)
- Whether they use video, static images, or carousel
- Any retargeting signs (ads that follow users around)

**Why this matters:** Their ad spend tells you what's working in the market. If they're running the same ad for months, it's profitable. If they've just launched something new, they're testing.

---

## PILLAR 2: Lead Generation Channels

**What to find:**
- Their top traffic-driving web pages (use SimilarWeb free data or search volume clues)
- Keywords they rank for organically (search: `site:[competitordomain.co.uk]` and note what pages surface)
- Keywords they're bidding on (search their core service keywords and watch for their paid listings)
- Lead capture methods on their website: contact forms, quote calculators, discount pop-ups, phone-first, WhatsApp buttons, live chat

**Search queries to use:**
- `[Competitor] cleaning quote Coventry`
- `[Competitor] end of tenancy Coventry`
- `[Competitor] reviews`

**What to capture:**
- Top 5 pages on their site (homepage, services, quote page, blog, location page)
- Which service gets most prominent placement
- Lead magnets in use: ebooks, checklists, free quotes, first clean discounts
- Whether they use landing pages separate from their main site
- Review volume and recency (Google, Trustpilot, Checkatrade)

**Why this matters:** Where they invest to generate leads shows where the market is active. Gaps in their coverage are opportunities to dominate.

---

## PILLAR 3: Social Media Presence

**Platforms to check:** Facebook, Instagram, LinkedIn, TikTok, Nextdoor

For each active platform, capture:

- **Posting frequency** — daily, weekly, sporadic?
- **Content types** — before/afters, team photos, tips, promotional offers, video walkthroughs, testimonials?
- **Engagement quality** — are people actually commenting and sharing, or just likes?
- **Top 3 posts this month** — what performed best and why (emotional hook, offer, local relevance, timing)
- **Response behaviour** — how they handle comments, complaints, and reviews
- **Collaborations** — do they use influencers, local partnerships, or community groups?
- **UGC (user-generated content)** — do customers post for them?

**Search queries to use:**
- `[Competitor Name] Facebook`
- `[Competitor Name] Instagram cleaning`
- `[Competitor Name] TikTok`
- `[Competitor Name] Nextdoor Coventry`

**Why this matters:** Social is free visibility. If they're dominant on one platform, Coventry Cleans needs to own a different one — or out-execute them on theirs.

---

## PILLAR 4: Weekly Monitoring Schedule

When running the weekly sweep, follow this cadence:

| Day | Task |
|---|---|
| Monday | Pull social media performance across all known competitors — new posts, top content |
| Wednesday | Check for new ads or promotions launched this week |
| Friday | Summarise any new content, blogs, or campaigns published |
| Flag immediately | New product/service launch, major discount campaign, viral post, negative PR event |

For the Monday sweep, check:
- Facebook pages (new posts since last Monday)
- Instagram profiles (scroll last 7 days)
- Google Business profiles (new posts, new reviews)

For Wednesday ad check:
- Re-run Google searches for core keywords and note paid ad positions
- Check Facebook Ad Library: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=GB&q=[competitor]`

For Friday content summary:
- Check their blog/news page for new articles
- Check their Google Business for new posts
- Note any seasonal or timely campaign they've launched

---

## OUTPUT FORMAT

Every competitor analysis must use this exact structure. One section per competitor.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏢 COMPETITOR: [Name]
📍 Location: [Coventry / Area served]
🌐 Website: [URL]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📣 ADVERTISING
• What they did: [specific ad, offer, or campaign]
• Where: [Google Ads / Facebook / Instagram / Bark, etc.]
• Why it likely worked: [psychological or commercial reason]
• What Coventry Cleans should do: [specific action]

📈 LEAD GENERATION
• What they did: [top page, lead magnet, keyword focus, etc.]
• Where: [channel/platform]
• Why it likely worked: [reason]
• What Coventry Cleans should do: [specific action]

📱 SOCIAL MEDIA
• What they did: [content type, campaign, top post]
• Where: [Facebook / Instagram / TikTok / etc.]
• Why it likely worked: [reason]
• What Coventry Cleans should do: [specific action]

⚡ IMMEDIATE OPPORTUNITIES:
[2-3 bullet points of gaps, vulnerabilities, or moves Coventry Cleans can make RIGHT NOW]

🛡️ THREATS TO WATCH:
[1-2 bullet points if they're doing something that could hurt us]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After all competitors, add a **MARKET SUMMARY** section:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 COVENTRY MARKET SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 What the market is doing: [1-2 sentences on trends]
🚪 Gaps nobody is owning: [specific opportunities]
🎯 Priority move for Coventry Cleans this week: [single clearest action]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Research Execution Guidelines

1. **Always look for evidence, not assumptions.** If you can't find a competitor's Facebook ad, say so — don't guess. What's *absent* is also intelligence.

2. **Be specific with what you find.** "They're running a 10% discount ad with the headline 'Book Your Coventry Clean Today'" is 10x more useful than "they're running ads."

3. **Think commercially.** Don't just describe — interpret. Why would a cleaning company make this specific move? What does it tell us about their strategy?

4. **Check the Facebook Ad Library every time.** It's the most reliable free source for ad intelligence: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=GB`

5. **Google their name + "reviews"** to understand their reputation. A competitor with 4.2 stars and 80 reviews is a different threat than one with 4.9 stars and 200 reviews.

6. **Look at their Google Business profile.** Posts, photos, Q&A, and review responses are all visible and highly revealing.

7. **When uncertain, flag it.** Say "couldn't confirm this" rather than speculate. Taka makes real business decisions based on this intel.

---

## Coventry Cleans Competitive Advantage Lens

When writing recommendations, always filter through what Coventry Cleans actually stands for:

- **Trusted. Thorough. Consistent.**
- Premium positioning — not the cheapest, the most reliable
- Local authority — deep Coventry roots, not a national franchise
- Systems-led — professional operations, not ad hoc

If a competitor is doing something, ask: *can Coventry Cleans do it better, do it differently, or own a space they're ignoring?*

---

## Execution Steps

1. Confirm mode: Deep Dive (specific competitor) or Weekly Sweep (all known)?
2. Search each competitor using the research queries above
3. Check Facebook Ad Library for active ads
4. Review their social media profiles for recent activity
5. Assess their website for lead generation setup
6. Format findings using the output template above
7. End with the Market Summary and one clear priority action for Coventry Cleans
