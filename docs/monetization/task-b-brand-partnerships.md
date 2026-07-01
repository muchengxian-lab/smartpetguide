# Task B: Brand Partnerships Sprint

Goal: replace the failed backlink-request outreach with a useful brand-facing offer that can generate replies, samples, affiliate upgrades, or small paid pilots.

Important context: the previous brand outreach asked brands to add SmartPetGuide to press coverage or "As Seen On" pages. It produced one eufy support-ticket reply and no useful partnership. Do not repeat that offer.

## Files To Read

- `backlinks/brand-outreach-template.md`
- `progress.md` around the 2026-06-12 and 2026-06-19 outreach records
- `PROJECT-OVERVIEW.md`
- `MONTH-1-THIRD-PARTY-AUDIT.md`
- `src/data/products.json`
- `src/pages/how-we-research.astro`
- `src/pages/affiliate-disclosure.astro`

## Main Deliverables

1. A brand-facing page:
   - preferred route: `/for-brands/`
   - source file: `src/pages/for-brands.astro`

2. A partnership documentation file:
   - `docs/monetization/brand-partnerships.md`

3. A revised outreach template:
   - update `backlinks/brand-outreach-template.md`
   - keep the old backlink template as "Historical template - do not use as primary"

## Page Requirements: `/for-brands/`

The page should explain:

- SmartPetGuide covers smart pet devices: automatic feeders, self-cleaning litter boxes, water fountains, pet cameras, GPS trackers.
- The research method is based on verified owner reviews, product specs, BSR/marketplace signals, comparison tables, and long-term cost analysis.
- Brand cooperation options:
  - Product visibility snapshot
  - Buyer question analysis
  - Competitor comparison gap analysis
  - Pinterest distribution package
  - Content update with UTM reporting
  - Product data correction request
- Editorial boundary:
  - paid work cannot buy a ranking
  - sponsored placements must be labeled
  - corrections are welcome when factual
  - rankings remain editorial

The page should include a simple contact CTA that uses an email link only. Do not add a form unless the repo already has a form-handling pattern.

Suggested email:

- `press@smartpetguide.net` if already configured in project records
- otherwise use existing contact email from the site

## Documentation Requirements

Create `docs/monetization/brand-partnerships.md` with:

### Priority Brand List

Use this first-pass brand list. Do not fabricate emails. Leave unknown contact fields blank or write `TBD`.

| Brand | Category | Why target | Contact source | Status |
|------|----------|------------|----------------|--------|
| Aorkuler | GPS tracker | Small brand, high-ticket no-subscription angle | TBD | Not contacted |
| Homerunpet | Water fountain | Wireless fountain, useful product story | TBD | Not contacted |
| KittySpout | Water fountain | Stainless steel fountain, hygiene angle | TBD | Not contacted |
| YEAPAW | Water fountain | Premium pumpless steel fountain | TBD | Not contacted |
| Elspet | Litter box | Mid-price automatic litter box | TBD | Not contacted |
| CATLINK | Litter box | Multi-cat data angle | TBD | Not contacted |
| Honey Tour | Pet camera | Robot camera, unique positioning | TBD | Not contacted |
| xpai | Pet camera | Budget 4K no-subscription angle | TBD | Not contacted |
| WOPET | Feeder/camera | Budget feeder and camera line | Existing project list | Previously listed |
| Petlibro | Feeder | High-volume feeder, strong content fit | Existing project list | Previously no reply |
| PETKIT | Feeder/fountain | Smart feeder/fountain portfolio | Existing project list | Previously no reply |
| Catit | Fountain | PIXI hydration tracking angle | Existing project list | Previously no reply |

### Offer Ladder

Use three levels:

1. Free opener: "we found 3 buyer questions/content gaps"
2. Pilot package: `$250-$500`
   - one product visibility snapshot
   - one content update or product note
   - five Pinterest-ready assets or pin briefs
   - UTM reporting after 14 days
3. Deeper package: `$800-$1,500`
   - competitor comparison
   - buyer objection map
   - AI/Google citation readiness
   - content roadmap
   - measured distribution report

### Outreach Sequence

Create templates for:

- D0 opener: 3 buyer questions
- D3 follow-up: offer the mini visibility snapshot
- D7 close-loop: ask whether marketing/partnerships is the right contact
- reply template for "send details"
- reply template for "we only do affiliate"
- reply template for "not interested"

## Outreach Template Rules

The first email must not:

- ask for a backlink
- ask to be added to an "As Seen On" page
- sell a paid package immediately
- claim large traffic
- imply guaranteed sales

The first email should:

- name the product
- give 3 concrete observations or buyer questions
- point to the existing SmartPetGuide mention if relevant
- ask whether a short visibility snapshot would be useful

## Acceptance Criteria

- `src/pages/for-brands.astro` exists and builds.
- `docs/monetization/brand-partnerships.md` exists.
- `backlinks/brand-outreach-template.md` clearly marks the old template as historical and provides the new sequence.
- No false traffic, ranking, or testing claims are introduced.
- `npm run build` passes.
- `progress.md` records the work.

## Human-Only Tasks

Do not send outreach emails.
Do not scrape private contact databases.
Do not submit contact forms.
Do not negotiate paid terms.

