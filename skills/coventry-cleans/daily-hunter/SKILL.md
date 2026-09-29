---
name: daily-hunter
description: Find high-value cleaning service leads in Coventry and surrounding areas. Use this skill whenever the user mentions lead generation, finding cleaning clients, daily hunter, prospecting for cleaning business, searching for commercial cleaning opportunities, care homes needing cleaners, estate agents, landlords, Airbnb hosts, or any request to find new business opportunities for Coventry Cleans. Also trigger when user says "run daily hunter", "find leads", "search for clients", or "prospect today".
---

# Daily Hunter - Lead Generation for Coventry Cleans

This skill helps systematically find and qualify high-value cleaning service leads in Coventry and surrounding areas.

## Target Client Profile

### High-Priority Client Types
- Care homes and nursing facilities
- Commercial offices (50+ employees)
- Estate agents and letting agencies
- Landlords with multiple properties
- Airbnb/short-term rental hosts
- Retail stores and shops
- Post-renovation/construction projects

### Service Requirements
- Commercial cleaning contracts
- Deep cleaning services
- End-of-tenancy cleaning
- Post-renovation cleaning
- Recurring contracts (weekly/bi-weekly)

### Qualification Criteria
**Budget Signals** (£120+ per visit or recurring contracts):
- Large square footage (2000+ sq ft for commercial)
- Multiple properties under management
- Premium locations (city center, business parks)
- Established businesses with online presence
- Recent funding/expansion announcements

**Urgency Indicators**:
- Recent move-ins or relocations
- Renovation completions
- Negative reviews mentioning cleanliness
- Job postings for cleaning staff
- No current cleaning service listed
- Complaints about previous cleaners
- New business openings

### Exclusions
- One-off domestic home cleans
- Small residential properties (<2 bedrooms)
- Price-shopping individuals
- DIY/self-service requests

## Research Workflow

### Step 0: Deduplicate before searching (mandatory)

**Do this first, every run.** Without it the skill re-surfaces the same care homes and
agencies week after week, and outreach double-contacts the same person. A facilities manager
who gets three near-identical approaches from Coventry Cleans in a month has learned
something about how we operate, and it is not what we want them to learn.

**Read the contact log** at `leads/contact-log.md` (create it on first run) plus the last
30 days of daily reports in `leads/daily-hunter/`.

Build an exclusion list of every organisation already:
- Contacted in the last **90 days**, at any stage
- Marked `not interested`, `no contact`, or `do not approach` — these are permanent
- Already a customer, or holding a live quote

Exclude those from every search result before scoring. If a lead surfaces that is already on
the log, say so in the report rather than silently dropping it — a second sighting on a new
urgency signal is useful intelligence, it just is not a new lead.

### Step 0b: Write to the contact log (mandatory)

Every lead that reaches outreach gets a line, appended the same run:

```
| Date | Organisation | Contact | Channel | Stage | Outcome | Next action | Next date |
```

Stage is one of: `researched`, `contacted`, `replied`, `quoted`, `won`, `lost`, `do not approach`.

**A run that produces leads but writes nothing to the log has not finished.** The log is the
only reason the next run is smarter than this one. Until the CRM holds this (see below), the
file is the system of record.

**Target state:** this belongs in Clarify, the connected CRM, as a Lead record per
`docs/ccos/reference/data-model.md` — with source, channel, score, and full contact history.
The markdown log is the interim. Do not let it become permanent.

### Step 1: Strategic Search Planning

Before starting research, plan your search approach:

1. **Identify 3-5 search angles** for the day based on:
   - Day of week (e.g., Monday = new business registrations)
   - Seasonal opportunities (e.g., end of tenancy in summer)
   - Recent local news (new developments, business openings)

2. **Prioritize platforms** by lead quality:
   - **Tier 1**: LinkedIn (decision makers), Rightmove/Zoopla (landlords)
   - **Tier 2**: Google Maps (new businesses), Facebook Groups (local)
   - **Tier 3**: Gumtree, Bark, Checkatrade (job postings)

### Step 2: Platform-Specific Research

Use web search strategically for each platform:

#### LinkedIn Research
Search queries:
- "Facilities Manager Coventry care home"
- "Estate Agent Coventry new job"
- "Property Manager Warwickshire"
- "Operations Manager cleaning Coventry"

Look for:
- Recent job changes (new facilities managers)
- Posted job listings for cleaners
- Expansion announcements
- Complaint posts about cleaning services

#### Rightmove/Zoopla (Landlord Leads)
Search queries:
- "lettings Coventry new listings"
- "Coventry estate agents most properties"
- "portfolio landlord Coventry"

Look for:
- Agencies with 20+ active listings
- Recently let properties (end-of-tenancy needed)
- New build developments
- High-end rental properties (£1000+/month)

#### Google Maps (New/Underserved Businesses)
Search queries:
- "care homes Coventry recently opened"
- "new offices Coventry 2024"
- "Airbnb Coventry superhosts"
- "retail stores Coventry no cleaner reviews"

Look for:
- Businesses opened in last 6 months
- Poor cleanliness reviews
- No mention of cleaning service
- Multiple locations (chain potential)

#### Facebook Groups & Local Forums
Search queries:
- "Coventry landlords looking for cleaner"
- "Coventry business owners cleaning recommendation"
- "Warwickshire estate agents group"

Look for:
- Posts requesting cleaner recommendations
- Complaints about current cleaners
- Property management discussions

#### Job Boards (Bark, Checkatrade, Gumtree)
Search queries:
- "commercial cleaning wanted Coventry"
- "office cleaner needed Warwickshire"
- "care home cleaning contract"

Look for:
- Active job postings
- Budget mentioned in listing
- Recurring contract opportunities

### Step 3: Lead Qualification & Scoring

For each potential lead found, score against these criteria:

**High-Value Signals** (+3 points each):
- Commercial/care home/estate agent
- £120+ budget indicated
- Recurring contract mentioned
- Multiple properties/locations
- Urgency indicator present

**Medium-Value Signals** (+1 point each):
- Professional website
- Established business (2+ years)
- Good location (Coventry city center)
- Active social media
- Professional listing photos

**Disqualifying Signals** (exclude):
- One-off domestic clean only
- Budget under £80
- DIY/price-shopping language
- Student accommodation (unless commercial)
- Competitor already mentioned positively

**Minimum Score**: 6 points to qualify as a lead

### Step 4: Contact Intelligence Gathering

For qualified leads, gather:

**Required Information**:
1. Business/property name
2. Decision maker name (if findable)
3. Email address (prioritize business email)
4. Phone number (business line preferred)
5. LinkedIn profile (decision maker)
6. Business address

**Research Tactics**:
- Check "About" pages for team/contact info
- LinkedIn search: "[Business Name] [Role]" (e.g., "Sunrise Care Home Manager")
- Use format: firstname.lastname@businessdomain.com
- Check Companies House for directors
- Google "[Business Name] contact" or "team"

### Step 5: Lead Profile Creation

For each qualified lead, create this profile:

```
LEAD #[Number]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 Business: [Name]
🏢 Type: [Care Home/Office/Estate Agent/etc.]
📧 Contact: [Email] | 📱 [Phone]
👤 Decision Maker: [Name, Title]
🔗 LinkedIn: [URL if found]
🌐 Website: [URL]

💰 QUALIFICATION SCORE: [X]/12
   - Client Type: [Match reason]
   - Budget Signal: [Why they can afford £120+]
   - Urgency: [Why they need service now]
   
📝 WHY THEY'RE A STRONG FIT:
[2-3 sentences explaining specific reasons this lead is valuable for Coventry Cleans. Be specific about what you found in research.]

✉️ SUGGESTED OUTREACH:

[Platform: Email/LinkedIn/WhatsApp]

Subject: [Personalized subject line]

[Draft personalized message using template below]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Outreach Message Templates

### Template 1: New Business/Recent Change
```
Hi [Name],

I noticed [specific observation - e.g., "your new care home opened last month" / "you recently joined as Facilities Manager"].

At Coventry Cleans, we specialize in [their specific need] for [their business type] across Coventry and Warwickshire. We work with [similar clients - e.g., "3 other care homes in the area" / "several estate agents managing 50+ properties"].

Would you be open to a quick 10-minute call this week to discuss how we could support [Business Name] with:
• [Specific service 1 relevant to them]
• [Specific service 2 relevant to them]
• Flexible scheduling around your operations

Best regards,
[Your name]
Coventry Cleans
[Phone] | [Email]
```

### Template 2: Problem/Pain Point Identified
```
Hi [Name],

I came across [specific pain point - e.g., "some reviews mentioning cleaning concerns" / "your recent post looking for cleaner recommendations"].

We've helped [similar business type] in Coventry overcome [specific issue] through [solution]. For example, [brief case study or result].

Would it be worth a brief conversation to see if we could help [Business Name] with [their specific need]?

I'm available [2 specific time slots] this week.

Best,
[Your name]
Coventry Cleans
```

### Template 3: Strategic Partnership (Estate Agents/Landlords)
```
Hi [Name],

I noticed [Agency Name] manages [number] properties across Coventry. We're looking to partner with a select few agencies to provide priority end-of-tenancy and deep cleaning services.

Benefits for your agency:
• Fixed rates for all your properties (no quoting delays)
• 24-48hr turnaround on end-of-tenancy cleans
• Direct coordination with your lettings team
• Consistent quality across all units

Currently working with [competitor or similar agency if any]. Would you be interested in discussing a partnership?

Best,
[Your name]
```

## Daily Output Format

Generate a daily summary with this structure:

```
📊 DAILY HUNTER REPORT - [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 SEARCH FOCUS TODAY:
[1-2 sentences on search strategy used]

📈 RESULTS:
• Businesses researched: [number]
• Qualified leads found: [number]
• High-priority leads: [number with score 9+]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Individual lead profiles as formatted above]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 FOLLOW-UP PRIORITIES:
1. [Highest priority lead - why]
2. [Second priority - why]
3. [Third priority - why]

📋 NOTES FOR TOMORROW:
[Any patterns noticed, platforms that worked well, ideas for next search]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Best Practices

1. **Quality over quantity**: 3-5 highly qualified leads > 20 weak leads
2. **Personalization is key**: Generic outreach gets ignored
3. **Vary platforms daily**: Don't burn out one source
4. **Track what works**: Note which search queries yield best results
5. **Time appropriately**: Research in morning, outreach in afternoon
6. **Follow urgency**: Prioritize time-sensitive opportunities
7. **Build on successes**: If one care home responds, find similar ones

## Research Ethics & Compliance

- Only use publicly available information
- Respect robots.txt and platform terms of service
- Don't scrape personal contact info from private groups
- Use business contact details only
- Follow GDPR guidelines for data storage
- Unsubscribe anyone who requests it

**UK cold B2B outreach rules.** Marketing email to a corporate subscriber (a limited
company, LLP, or public body at a business address) is permitted without prior consent, but
every message must:

- Identify Coventry Cleans clearly as the sender, with a real postal address and contact details
- Carry a simple, working way to opt out, honoured immediately and permanently
- Not disguise or conceal who sent it

Sole traders and individuals are treated differently and are safer approached by phone or in
person than by cold email. When unsure whether a target is a corporate subscriber, do not
cold email it.

Anyone who opts out goes on the contact log as `do not approach`, permanently. That entry is
never overridden by a later urgency signal.

## Execution Instructions

When user triggers this skill:

1. **Confirm search parameters**:
   - "I'll search for [client types] in Coventry today. Focus on [current priority]?"

2. **Execute research**:
   - Use web_search tool for each platform
   - Apply qualification criteria systematically
   - Score each lead objectively

3. **Gather contact intelligence**:
   - Research decision makers
   - Find verified contact details
   - Check LinkedIn for context

4. **Create lead profiles**:
   - Format using template above
   - Include specific personalization points
   - Draft tailored outreach messages

5. **Deliver daily report**:
   - Provide formatted summary
   - Highlight top priorities
   - Suggest follow-up strategy

6. **Optional: Create spreadsheet**:
   - If user requests, create Excel tracker
   - Include all leads with scores
   - Add columns for follow-up status
