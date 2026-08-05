# Feeder Reliability Pitch-Readiness Audit

**Audit date:** 2026-08-04

**Resolved:** 2026-08-05

**Status:** Approved asset angle — citation corrected and production-verified

**External action:** None. This is not a queued or sent pitch.

## Verdict

The strongest existing candidate asset is:

`https://smartpetguide.net/guides/feeder-portion-size-guide/`

The candidate editor-facing angle is:

> **Before Calling Your Cat Food-Obsessed, Calibrate the Feeder: Why One “Portion” Is Not a Standard Measure**

The `cat-breaking-into-automatic-feeder` page supplies the reader problem that surfaced in GSC, but it is not the evidence destination for this pitch. Its current owner-research wording and several behavioral, nutrition, RFID, and brand-specific claims do not have a page-level source ledger. Do not pitch that page as original data or cite it as proof.

The portion guide initially failed final source verification on one point: its WOPET F01 Plus table and FAQ say approximately 5 g with the small wheel and 10 g with the large wheel, while the linked F01 Plus quick-start PDF only stated that one portion is about 10 g. On 2026-08-05, both visible WOPET citations were replaced with the official F01 Plus support page that explicitly supports the two-wheel distinction. The corrected page was then rebuilt, deployed, and verified on production. This specific source blocker is resolved.

## Why This Angle Is Linkable

The portion guide gives an editor a replicable procedure instead of a brand ranking or an unsupported failure rate:

1. Dispense 10 portions of the household's normal kibble.
2. Weigh the total and divide by 10 to establish working grams per portion.
3. Divide a food-label or veterinarian-based daily gram target by meals per day, then by the measured grams per portion.
4. Check the projected daily total after rounding to the feeder's available whole-portion setting.

The browser-side calculator exposes the measured grams, nearest setting, projected daily grams, and difference from target. It does not generate a calorie target and warns against automatically rounding up a result below half a portion.

## Evidence Chain

| Evidence | What it supports | Boundary |
|---|---|---|
| [PETLIBRO official portion guide](https://ca.petlibro.com/pages/how-much-is-in-one-feeding-portion-plaf001-002-101-102-plaf003-004-plaf005-006-103-203-plaf008-plaf107-plaf108-plaf301) | Granary models express one portion at about 20 ml / 1/12 cup | Manufacturer approximation for named models only |
| [WOPET F01 Plus support page](https://test.wopet.com/support-center/user-guide-of-wopet-pioneer-automatic-pet-feeder/) | Small wheel about 5 g; large wheel about 10 g; food can cause slight differences | Correct official source now used in both visible SmartPetGuide citations |
| Historical WOPET quick-start PDF | States only that one portion is about 10 g | Removed from the target page on 2026-08-05 because it did not support the two-wheel distinction |
| [PETKIT Fresh Element SOLO P570 manual](https://instructions.petkit.com/D4_V1.2_20220713.pdf) | A fixed-volume serving is listed at about 10 g; pellet properties and hopper level can affect output | Named model only |
| [AAHA feeding article](https://www.aaha.org/resources/5-ways-to-know-how-much-to-feed-your-pet/) + [nutrition guidance](https://www.aaha.org/wp-content/uploads/globalassets/02-guidelines/2021-nutrition-and-weight-management/resourcepdfs/nutritiongl_table6.pdf) | Package directions are a starting point; weighing food in grams improves precision over cups | Feeding targets still belong to the food label and veterinarian |
| SmartPetGuide 10-dispense calculator | Converts a household measurement into a whole-portion schedule and displays rounding error | Arithmetic tool, not medical advice |

## Candidate Pitch Paragraph — Use Only for a Matched Future Opportunity

An automatic feeder's “one portion” is not a standard unit: one manufacturer may describe it by volume, another by grams, and another may offer different dispensing wheels. Before an owner increases food, replaces the feeder, or assumes a cat's food-seeking behavior is purely behavioral, there is a simple check they can reproduce at home—dispense 10 portions, weigh the total, and calculate the real grams delivered by that feeder-and-kibble combination. SmartPetGuide's cited guide includes three model-specific manufacturer examples and a calculator that shows the daily error introduced by whole-portion rounding.

## Claim Guardrails

Allowed:

- “One portion is not a universal number of grams.”
- “Output can vary by feeder mechanism and kibble.”
- “A 10-dispense test gives a household-specific working measurement.”
- “Use the food label or veterinarian for the daily target.”

Do not claim:

- that underfeeding is the usual cause of feeder break-ins;
- a universal calorie target, meal frequency, or safe percentage increase;
- a feeder break-in, jam, or failure rate;
- that SmartPetGuide analyzed a stated number of owners for this finding;
- that a named feeder is break-in-proof or that a brand-wide RFID/anti-theft behavior is verified.

## Distribution Decision

- The angle was not sent on 2026-08-04; the citation blocker was resolved and production-verified on 2026-08-05.
- The portion URL may now be cited for this narrow calibration method when there is a real matched editor request or a separately approved outreach batch. Approval of the asset does not itself authorize sending.
- Round 4's three unsent targets remain Hold; this audit does not reopen them.
- Reuse the angle only when an editor asks for feeder, portion-control, pet-obesity, or practical consumer-service topics, or when a future approved outreach batch has a clearly matched publication.
- Round 4 status, email status, and index-request status remain unchanged; no new pitch was sent as part of this fix.

## Readiness Fix — Completed 2026-08-05

1. Completed: both visible WOPET source links now use the verified official F01 Plus support page.
2. Completed: the claim, FAQ, calculator, and PETLIBRO/PETKIT examples were left unchanged.
3. Completed: only this page's `modifiedDate` was updated, to 2026-08-05.
4. Completed: `npm.cmd run verify`, Vercel production readiness, HTTP 200, correct-link presence, old-PDF absence, date, and calculator presence all passed.
