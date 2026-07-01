# Task A: Amazon Affiliate Conversion Sprint

Goal: optimize the highest-intent SmartPetGuide pages for real Amazon affiliate clicks and eventual qualifying purchases.

This is not expected to produce large short-term revenue. Its purpose is to validate the reader-to-Amazon path and support the Amazon Associates milestone.

## Files To Read

- `src/data/products.json`
- `src/components/ProductCard.astro`
- `src/pages/reviews/[slug].astro`
- `src/pages/compare/[slug].astro`
- `src/pages/guides/[slug].astro`
- `src/pages/best/[slug].astro`
- `src/layouts/BaseLayout.astro`
- `MONTH-1-THIRD-PARTY-AUDIT.md`
- `weekly-report.md`
- `pins/pin-plan.md`

## Target Pages

Prioritize these pages:

1. `/compare/lr5-vs-amazon-basics-cost/`
2. `/reviews/litter-robot-5-review/`
3. `/reviews/amazon-basics-litter-box-review/`
4. `/reviews/petlibro-granary-review/`
5. `/compare/wopet-vs-petlibro/`
6. `/best/pet-cameras-no-subscription/`
7. `/guides/best-no-subscription-cameras/`
8. `/reviews/aorkuler-gps-review/`
9. `/best/gps-trackers-no-monthly-fee/`
10. `/guides/are-automatic-feeders-worth-it-for-one-cat/`

If a page does not exist, record it in `docs/monetization/amazon-conversion-log.md` and skip it.

## Implementation Steps

### Step 1: Audit Affiliate Links

For each target page, check all Amazon links for:

- `tag=smartpetgui0a-20`
- `rel="sponsored"`
- direct product link where possible
- search link only when a direct ASIN is unknown
- no fake ASINs
- affiliate disclosure visible near commercial CTAs

Create or update:

- `docs/monetization/amazon-conversion-log.md`

Use this table format:

```md
| Page | Product | Link type | Has tag | rel=sponsored | CTA count | Issue | Next action |
|------|---------|-----------|:--:|:--:|:--:|------|------|
```

### Step 2: Add Buying Decision Modules

Add or reuse a lightweight decision module on the target pages:

- Buy if
- Skip if
- Best alternative
- Cost / reliability / no-subscription angle

Keep the module factual and short. Do not add visible "how to use this site" explanation.

Preferred module copy shape:

```text
Buy if: ...
Skip if: ...
Best alternative: ...
```

### Step 3: Improve CTA Placement

Each target page should have up to three natural affiliate CTA placements:

1. Near the first decision section.
2. After a comparison table or pros/cons section.
3. Near the final verdict.

Avoid stuffing. Do not add more than three affiliate CTAs per product page unless the page already has a local pattern that supports it.

CTA wording examples:

- Check today's Amazon price
- Compare owner reviews on Amazon
- See current price and availability
- Check the 3-year cost on Amazon

### Step 4: Pinterest Experiment Mapping

Update or create `docs/monetization/pinterest-affiliate-experiments.md` with 12 planned pins, mapped only to the target pages.

Angles:

- 3-year cost
- no subscription
- under $100
- buy vs skip
- reliability
- avoid buyer's remorse

Use this table:

```md
| Pin # | Page | Angle | Hook | UTM campaign | Status |
|------:|------|-------|------|--------------|--------|
```

### Step 5: GA4 Event Check

Confirm current event names for:

- `affiliate_click`
- `outbound_click`

If event tracking is missing, add it in the existing style. Do not invent a second analytics system.

## Acceptance Criteria

- `npm run build` passes.
- `docs/monetization/amazon-conversion-log.md` exists.
- Five or more target pages have a clear buying decision module.
- Five or more target pages have verified affiliate CTA placement.
- No new false hands-on claims are introduced.
- All added affiliate links are marked `rel="sponsored"`.
- `progress.md` records the completed files and remaining manual checks.

## Human-Only Tasks

Do not perform these:

- Buying products.
- Generating test orders.
- Asking friends/family to order.
- Checking private Amazon Associates reports unless the user explicitly opens or provides them.

