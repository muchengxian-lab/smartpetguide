# GEO Audit Report: SmartPetGuide

> **Current audit:** 2026-08-01. Latest manual score: **79/100**. The June 18 and July 1 sections below are retained as historical snapshots; their page counts, Review/Product schema notes, and platform metrics are not current facts.

## August 1, 2026 Monthly Re-Audit

### Current Score

| Category | Score | Weight | Weighted | Change vs 7/1 | Evidence |
|------|:--:|:--:|:--:|:--:|------|
| AI Citability | **84** | 25% | 21.0 | +12 | 100/100 content pages have FAQ structure and source/method cues after the review-template fix; all page types expose a standalone decision pattern; 14/38 eligible guides have Quick Answer |
| Brand Authority | **54** | 20% | 10.8 | +2 | The Wikidata/entity footprint was last verified on 7/1 and editorial relationship work exists, but the last verified Semrush baseline is still only 12 referring domains and no new guest-post placement is confirmed |
| Content E-E-A-T | **88** | 20% | 17.6 | +6 | Chengxian Yang is visible on 100/100 content pages, `/about/#author` and `/how-we-research/` disclose identity, method, affiliate boundary, non-hands-on scope, source types, and uncertainty |
| Technical GEO | **92** | 15% | 13.8 | +2 | 12/12 declared AI User-Agents returned HTTP 200; robots, llms, sitemap, HTTPS, canonical and Vercel delivery remain healthy; llms assets refreshed to 8/1 |
| Schema & Structured Data | **84** | 10% | 8.4 | +1 | 100/100 dated content pages have Article + FAQPage + BreadcrumbList; one qualifying guide has HowTo; third-party Amazon ratings are no longer misrepresented as first-party Review/Product/Offer schema |
| Platform Optimization | **74** | 10% | 7.4 | -1 | Pinterest has impressions and on-platform engagement but 7-day outbound remains 0; no verified YouTube/LinkedIn or new AI citation outcome |
| **Overall GEO Score** |  |  | **79.0 → 79/100** | **+5** | Target 80 narrowly missed; the limiting factor is external authority/outcomes, not technical crawlability |

> This is a consistent manual readiness score, not a Google, OpenAI, or third-party ranking metric. It is useful for month-over-month gap tracking only.

### Full-Site Evidence

| Check | Result | Decision |
|------|:--:|------|
| Dated content inventory | **100** = Best 10 / Breed 7 / Compare 15 / Guides 42 / Reviews 26 | Matches `content-dates.json`; 114 pages generated and 113 indexable URLs remain the site-level counts |
| Identity | **100/100** pages show Chengxian Yang | PASS; named author links to `/about/#author` |
| Date | **100/100** have registered `dateModified` and one H1 | PASS; dates were not batch-refreshed during this audit |
| Core schema | **100/100** Article + FAQPage + BreadcrumbList | PASS; Review/Product schema stays intentionally absent on all 26 affiliate reviews |
| Source/method cue | **81/100 before → 100/100 after** | Review template was the only structural gap: 7/26 reviews had a visible data-source cue before; all 26 now show common research basis, non-hands-on boundary, and methodology link |
| Answerability | Best 10/10 top pick; Compare 15/15 winner; Review 26/26 verdict; Breed 7/7 Quick Answer; Guide 42/42 FAQ and 14 Quick Answers | PASS; do not mechanically expand Quick Answer coverage |
| HowTo | **1** qualifying guide | PASS; only the feeder-jamming page currently matches the explicit numbered-fix rule |
| AI crawler access | **12/12 HTTP 200** | PASS; Server is Vercel and no Cloudflare-specific blocking headers were observed |
| `llms.txt` / `llms-full.txt` | **200 but stale before audit; refreshed to 2026-08-01** | Corrected old page counts, author identity, research boundary, schema state, and key July updates |

### Changes Made

1. Added a visible research-basis and non-hands-on boundary to the Review template without restoring third-party Review/Product schema or refreshing all review dates.
2. Updated `/how-we-research/` to distinguish owner reports from controlled evidence, marketplace snapshots from real-time proof, and provisional new-product coverage from established reliability.
3. Refreshed both llms assets with current counts, author, methodology, schema boundary, feeder calibration, and travel-failover facts.
4. Corrected this report so the historical 7/1 Review Schema gain is no longer presented as current implementation.

### Remaining Gaps and Decision

- **No critical technical GEO issue.** Do not add more crawler directives, new schema types, or new URLs for score-chasing.
- **Brand authority remains the main ceiling.** The Pretty Happy Pets draft is still under review and does not count as placement or backlink; the last Semrush baseline is historical until refreshed.
- **Source cue is not claim-level proof.** The 7/28 evidence audit still identified seven low-source guides; handle them only when query/index/usage evidence or a safety issue prioritizes a page, not as a batch rewrite.
- **Quick Answer stays 14/38.** Page types already expose verdicts, winners, top picks, FAQs, and breed answers. Additional Quick Answers require a real user-question gap.
- **Score 79 does not trigger a strategy change.** Continue Month 2's existing focus on indexing, editorial authority, and existing-page evidence. Re-score quarterly unless a major identity/schema/platform change occurs.

---

## Historical Baseline — June 18 and July 1, 2026

**Audit Date:** 2026-06-18
**URL:** https://smartpetguide.net
**Business Type:** Publisher (Affiliate Content Site)
**Pages Analyzed:** 5 sampled (Homepage, Review, Best List, Compare, Guide) + Sitemap (98 URLs — 404 页不计入 sitemap，实际全站 99 页)
**Skill:** geo-audit v2026.02 (WebFetch native — preflight fixed)

---

## Executive Summary

**Overall GEO Score: 70/100 (Good)**

SmartPetGuide has strong technical GEO infrastructure and comprehensive Schema coverage. The site outperforms most young content sites in AI readiness. Two previous critical gaps (llms.txt, Organization Schema) have been resolved. The primary constraint remains Brand Authority, which is expected for a < 2-month site and will improve with outreach and time.

### Score Breakdown

| Category | Score | Weight | Weighted Score |
|---|---|---|---|
| AI Citability | 65/100 | 25% | 16.25 |
| Brand Authority | 48/100 | 20% | 9.6 |
| Content E-E-A-T | 78/100 | 20% | 15.6 |
| Technical GEO | 90/100 | 15% | 13.5 |
| Schema & Structured Data | 80/100 | 10% | 8.0 |
| Platform Optimization | 70/100 | 10% | 7.0 |
| **Overall GEO Score** | | | **69.95 → 70/100** |

### Score Improvement Log

| Date | Score | Change | Key Actions |
|------|:--:|:--:|------|
| 2026-06-18 (initial) | 62 | — | Pre-fix baseline |
| 2026-06-18 (post-fix) | 70 | +8 | llms.txt + llms-full.txt + Organization Schema |
| **2026-07-01 (monthly re-audit)** | **74** | **+4** | Review Schema 增强 + 评价摘要 2→4 + llms-full.txt 更新 + guide citation cue 全覆盖 + 首页 social proof + 85 Pin + Wikidata 存活 |

---

## Critical Issues (Fix Immediately)

*None.* No domain-level blockers. All AI crawlers allowed. All pages return 200. llms.txt is live.

## High Priority Issues (Fix Within 1 Week)

| # | Issue | Status |
|---|-------|:--:|
| 1 | No llms.txt / llms-full.txt | ✅ Fixed 6/18 |
| 2 | Missing Organization Schema on homepage | ✅ Fixed 6/18 |

## Medium Priority Issues (Fix Within 1 Month)

| # | Issue | Severity | Recommended Fix |
|---|-------|----------|-----------------|
| 3 | No citation cues (timestamp + data source) on guides | Medium | Add date-tagged data source line to guide pages. Reviews already have "Data sourced from Amazon.com, June 2026" — extend to guides. |
| 4 | No Wikipedia / Wikidata entity | ~~Medium~~ | ✅ Fixed 6/19 — Q140290653 created |
| 5 | sitemap.xml returns 404 | ~~Medium~~ | ✅ Fixed 6/21 — vercel.json redirect `/sitemap.xml` → `/sitemap-index.xml` 308 |
| 6 | No individual author bio pages | Medium | Review pages author is "SmartPetGuide Team" — create 1-2 named author profiles with credentials for top pages. |
| 7 | Guides lack verdict/conclusion sentences | Medium | Reviews have strong verdict blocks (confirmed). Guides and compare pages would benefit from similar standalone conclusions. |

## Low Priority Issues (Optimize When Possible)

| # | Issue | Recommended Fix |
|---|-------|-----------------|
| 8 | No YouTube / Reddit brand presence | Claim handles; add to Schema sameAs when active |
| 9 | Statistics embedded in paragraph text | Extract key data points into standalone sentences |
| 10 | No Gemini-specific bot in robots.txt | Add `User-agent: GoogleOther` or similar |

---

## Category Deep Dives

### AI Citability (65/100)

**Confirmed:** Verdict blocks present on all 26 review pages. Data source annotation present. FAQ sections with proper heading hierarchy. "What Verified Owners Actually Say" sections with explicit data provenance.

**Missing:** Guide pages and compare pages lack equivalent standalone conclusion sentences. Citation cues (date + source format) not consistently applied outside reviews.

**Quick win:** Add one-para conclusion + data source footnote to top 10 guide pages. Princeton KDD data: +115% AI citation from "Cite Sources" strategy.

### Brand Authority (48/100)

**Platform presence:**

| Platform | Status |
|----------|:--:|
| Pinterest | ✅ @muchengxian, 5 Board, 62 Pin |
| Medium | ✅ @muchengxian, 3 canonical posts |
| Flipboard | ✅ @755g287 |
| Wikipedia | ❌ |
| Wikidata | ✅ Q140290653（6/19 创建） |
| Reddit | ⚠️ u/honest_pet_reviews (养号中) |
| YouTube | ❌ |
| LinkedIn | ❌ |

Expected score for < 2-month site. Wikidata entity created 6/19 — should boost Brand Authority +10 points at next re-audit.

### Content E-E-A-T (78/100)

| Signal | Status |
|--------|:--:|
| Author attribution in Schema | ✅ Person + Organization |
| How We Research page | ✅ |
| Affiliate Disclosure | ✅ |
| Privacy Policy | ✅ |
| Veterinary disclaimer in footer | ✅ |
| Products We Don't Recommend | ✅ |
| Published/modified dates | ✅ |
| "What Owners Actually Say" data provenance | ✅ |
| Individual author profiles | ❌ |
| External citations/recognition | ❌ (expected for new site) |

Strong EEAT foundation. The main gap is personal author profiles — replacing "SmartPetGuide Team" with 1-2 named authors would push this to 85+.

### Technical GEO (90/100)

**AI Crawler Access (confirmed via WebFetch):**

| Crawler | Engine | Status |
|---------|--------|:--:|
| GPTBot | ChatGPT | ✅ |
| ChatGPT-User | ChatGPT | ✅ |
| PerplexityBot | Perplexity | ✅ |
| Google-Extended | Google AI Overviews | ✅ |
| CCBot | Common Crawl | ✅ |
| anthropic-ai | Claude | ✅ |
| * (wildcard) | All others | ✅ |

**Infrastructure:**

| Check | Status |
|-------|:--:|
| llms.txt | ✅ Live (confirmed via WebFetch) |
| llms-full.txt | ✅ Live |
| HTTPS enforced | ✅ |
| Sitemap (98 URLs) | ✅ sitemap-index.xml + sitemap-0.xml |
| Canonical URLs | ✅ |
| PageSpeed | ✅ 86 mobile / 99 desktop |
| RSS Feed | ✅ /rss.xml |

The top score in this category. Only minor issues: /sitemap.xml returns 404, and no Gemini-specific bot directive.

### Schema & Structured Data (80/100)

**Schema coverage (confirmed):**

| Page Type | Schema Types |
|-----------|-------------|
| Homepage | Organization (1 ld+json tag confirmed) |
| Reviews | Review + Product + FAQPage + BreadcrumbList |
| Best Lists | Article + FAQPage + BreadcrumbList |
| Compare | Article + FAQPage + BreadcrumbList |
| Guides | Article + FAQPage + BreadcrumbList |

**5 Schema types across all 98 pages.** Review Schema includes reviewRating, itemReviewed (Product), author, publisher. Article Schema includes headline, description, datePublished, dateModified, author (Person with sameAs), publisher (Organization with sameAs).

Missing: HowTo Schema on step-by-step guides (e.g., cleaning guide).

### Platform Optimization (70/100)

| Platform | Optimization Status |
|----------|:--:|
| Google AI Overviews | Google-Extended ✅, structured content ✅, llms.txt ✅ |
| ChatGPT/Bing | GPTBot ✅, Schema coverage supports entity recognition |
| Claude | anthropic-ai ✅, llms.txt ✅, content quality high |
| Perplexity | PerplexityBot ✅, FAQ content matches citation patterns |
| Gemini | No specific bot, covered by wildcard |
| Pinterest | Active presence, sameAs in Schema |
| Medium | 3 articles, sameAs in Schema |

---

## Quick Wins

1. **Add verdict paragraph to top 5 guide pages** (15 min) — Extend the review verdict pattern to guides
2. **Fix sitemap.xml 404** (2 min) — Redirect to sitemap-index.xml
3. ~~Submit Wikidata entity~~ ✅ Q140290653 created 6/19
4. **Add Gemini bot to robots.txt** (1 min) — `User-agent: GoogleOther` + `Allow: /`

---

## 30-Day Action Plan

### Week 1: Content Enhancement
- [ ] Add conclusion paras to top 10 guide pages
- [ ] Add data source footnote to all guide pages
- [ ] Fix sitemap.xml redirect

### Week 2: Entity Building
- [ ] Submit Wikidata entity
- [ ] Create 1 named author profile (About page or new /team/ page)
- [ ] Add GoogleOther to robots.txt

### Week 3: Platform Expansion
- [ ] Activate Reddit (u/honest_pet_reviews — 已养号，可开始放链接)
- [ ] Reserve YouTube channel handle
- [ ] Add HowTo Schema to step-by-step guides (cleaning, maintenance)

### Week 4: Audit & Verify
- [ ] Re-run geo-audit, target score: 75+
- [ ] Verify Wikidata entity approved
- [ ] Check GSC for AI crawler activity in crawl stats

---

## Appendix: Pages Analyzed

| URL | Title | Key Findings |
|-----|-------|-------------|
| / | SmartPetGuide — Best Smart Pet Devices, Honestly Reviewed | Organization Schema ✅, 6 AI bots whitelisted ✅ |
| /reviews/litter-robot-5-review/ | LR5 Review — Is WasteID Worth $799? | Verdict ✅, Data source ✅, FAQ ✅, Review Schema ✅ |
| /best/self-cleaning-litter-boxes/ | 7 Best Self-Cleaning Litter Boxes of 2026 | Comparison table ✅, FAQ ✅ |
| /llms.txt | llms.txt | ✅ 200 OK, complete site structure listing |
| /robots.txt | robots.txt | ✅ 6 AI crawlers + wildcard = full access |
| /sitemap-index.xml | sitemap-index.xml | ✅ 1 sub-sitemap → 98 URLs total |

---

*Report generated by geo-audit workflow. WebFetch native mode — preflight bypass enabled via skipWebFetchPreflight. Scoring formula: GEO = AI Citability×0.25 + Brand×0.20 + EEAT×0.20 + Technical×0.15 + Schema×0.10 + Platform×0.10.*

---

## July 1, 2026 Monthly Re-Audit

### Score Breakdown (7/1)

| Category | Score | Weight | Weighted | Δ from 6/18 | Rationale |
|------|:--:|:--:|:--:|:--:|------|
| AI Citability | 72 | 25% | 18.0 | +7 | llms-full.txt updated to 112 pages + new categories. Guide citation cues 33/33 guides (100%). All guides have date-tagged data source footnotes. Robot vacuum test category expands topical coverage. /for-brands/ page not cited by AI yet but structured for future citation. |
| Brand Authority | 52 | 20% | 10.4 | +4 | Wikidata Q140290653 still alive (verified 7/1). Pinterest 34→85 Pin (5 Board). Review count climbed to 4 GSC评价摘要. 0 new backlinks — still the weakest dimension. |
| Content E-E-A-T | 82 | 20% | 16.4 | +4 | No-Fee GPS + Aorkuler reviews now have whatOwnersSay (praise/complaints). 3 reviews have Quick Decision modules. Homepage has social proof bar (112 pages, 26 products, 85K+ reviews). All review pages have author + date + data source + affiliate disclosure. Catit PIXI verdict strengthened with concrete numbers. |
| Technical GEO | 90 | 15% | 13.5 | 0 | At ceiling. All pages 200. Sitemap 109 URLs discovered (7/1). CleanUrls + trailingSlash consistent. No 404s, no redirect chains. |
| Schema & Structured Data | 83 | 10% | 8.3 | +3 | Review Schema enhanced with reviewRating/url/author/publisher sameAs (6/28). GSC 评价摘要 2→4. BreadcrumbList 12 有效. Product Schema 2 有效. Rating count ≥10 requirement met for more products. |
| Platform Optimization | 75 | 10% | 7.5 | +5 | Pinterest 85 Pin, 5 Board with category-focused structure. Medium 3 canonical articles. Product Hunt DA90+ dofollow. Crunchbase/Hotfrog/IndieHackers profiles live. Flipboard magazine on hold. |
| **Overall** | | | **74.1 → 74** | **+4** | |

### Key Changes Since 6/18

| Change | Impact |
|------|------|
| Review Schema 增强（reviewRating + url + sameAs） | GSC 评价摘要 2→4，更多页面符合 Rich Results |
| llms-full.txt 更新（101→112 页 + 新品类） | AI 爬虫发现新内容，覆盖更多查询 |
| 33 篇指南全部加 citation cue | AI citability + 引用率提升 |
| No-Fee GPS + Aorkuler whatOwnersSay | EEAT 增强，真实用户信号 |
| 首页 social proof 数字条 | 品牌信任信号 |
| Pinterest 34→85 Pin | 平台信号增强 |
| Quick Decision 模块（buyIf/skipIf/bestAlternative）| 结构化决策信息，AI 可提取 |
| 6/28 Review Schema reviewRating 增强 | 评价摘要覆盖率提升 |

### Remaining Gaps (unchanged from 6/18)

- No backlinks acquired (Brand Authority ceiling)
- No named individual author profiles (EEAT sub-optimal)
- No YouTube/Reddit brand presence (Platform)
- Sitemap still showing 109 of 112 pages (3 non-content pages excluded)

### Next Re-Audit Target

- **Target: 80 by 8/1** — Requires: 2-5 backlinks, 1 named author profile, Pinterest 100+ Pin, sitemap >110 discovered pages, GSC 索引突破 30+

---
*July 1, 2026 re-audit. Conducted manually against 6/18 baseline using same scoring framework.*
