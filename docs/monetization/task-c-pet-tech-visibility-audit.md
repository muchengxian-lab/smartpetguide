# Task C: Pet Tech Visibility Audit Service

Goal: create a sellable B2B service that uses SmartPetGuide's research, SEO, GEO, and product comparison capabilities before the consumer site has mature organic traffic.

This is the fastest potential cash-flow track. Execute this first unless the user says otherwise.

## Files To Read

- `GEO-AUDIT-REPORT.md`
- `MONTH-1-THIRD-PARTY-AUDIT.md`
- `PROJECT-OVERVIEW.md`
- `src/pages/how-we-research.astro`
- `src/pages/pet-tech-statistics.astro`
- `public/llms.txt`
- `public/llms-full.txt`
- `src/data/products.json`

## Main Deliverables

1. A service page:
   - route: `/for-brands/pet-tech-visibility-audit/`
   - source file: `src/pages/for-brands/pet-tech-visibility-audit.astro`

2. Audit template:
   - `docs/monetization/pet-tech-audit-template.md`

3. Outreach CRM:
   - `docs/monetization/audit-outreach-crm.md`

4. One sample mini-audit:
   - `docs/monetization/sample-mini-audit-aorkuler.md`
   - If Aorkuler feels unsuitable after reading the repo, choose one of: Homerunpet, KittySpout, YEAPAW, Elspet, CATLINK, Honey Tour, xpai.
   - Do not use eufy as the sample. eufy/Anker already replied via support-ticket path and is not the best early target.

## Service Page Requirements

Position the service as:

`Pet Tech Visibility Audit`

The page should sell a practical audit for pet tech brands that sell smart feeders, self-cleaning litter boxes, fountains, pet cameras, GPS trackers, or adjacent devices.

Include three packages:

1. Lite Audit - `$199`
   - 5-7 page snapshot
   - Google visibility gaps
   - AI citation readiness
   - Amazon owner-review pain points
   - 3 quick content opportunities

2. Standard Audit - `$499`
   - 12-15 page audit
   - competitor comparison
   - buyer objection map
   - FAQ/Schema recommendations
   - 30-day content roadmap
   - optional 30-minute walkthrough

3. Implementation - `$1,200+`
   - audit plus implementation support
   - content briefs
   - comparison-page copy
   - FAQ/Schema updates
   - product positioning notes

Editorial boundary:

- This is a consulting/research service.
- It does not buy SmartPetGuide rankings.
- It does not guarantee positive reviews.
- Sponsored or paid placements must be labeled if published.

CTA:

- email link to `press@smartpetguide.net` if available
- otherwise existing project contact email

## Audit Template Requirements

Create `docs/monetization/pet-tech-audit-template.md` with these sections:

1. Brand and product snapshot
2. Category and competitor set
3. Current Google visibility
4. Current AI citation readiness
5. Product-page and Schema readiness
6. Amazon/owner-review pain points
7. Buyer objections and missing FAQs
8. Competitor content gaps
9. Recommended page updates
10. 30-day content roadmap
11. Measurement plan
12. Priority action list

Use placeholder text where data must be gathered manually. Do not fabricate search volume, traffic, or sales data.

## Outreach CRM Requirements

Create `docs/monetization/audit-outreach-crm.md` with a table:

```md
| Brand | Category | Product | Website | Contact source | 3 observed findings | Outreach status | Next follow-up | Notes |
|------|----------|---------|---------|----------------|---------------------|-----------------|----------------|------|
```

Seed at least 12 rows using brands already present in the repository:

- Aorkuler
- Homerunpet
- KittySpout
- YEAPAW
- Elspet
- CATLINK
- Honey Tour
- xpai
- WOPET
- Petlibro
- PETKIT
- Catit

Do not invent websites or emails if not already known. Use `TBD`.

## Sample Mini-Audit Requirements

Create one sample mini-audit using only repo-known facts and clearly labeled assumptions.

Recommended sample: Aorkuler.

Include:

- product/category
- known SmartPetGuide coverage
- buyer angle: no subscription / off-grid / no phone required
- likely competitor set: Tractive, no-fee tracker, AirTag-style trackers
- 3 buyer questions to validate
- 3 content opportunities
- suggested next action for the brand

Do not claim to have searched the live web unless you actually do so and cite sources. If no web research is performed, label it "repo-based sample only".

## Acceptance Criteria

- service page exists and builds at `/for-brands/pet-tech-visibility-audit/`
- audit template exists
- CRM exists with at least 12 seeded rows
- sample mini-audit exists
- page and docs preserve editorial independence
- `npm run build` passes
- `progress.md` records the work

## Human-Only Tasks

Do not:

- send emails
- submit forms
- contact brands
- promise rankings
- promise AI citations
- quote private data not in the repo

