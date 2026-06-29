# SmartPetGuide Monetization Validation Sprint

Owner: Claude Code / DeepSeek execution stack
Start date: 2026-06-29
Sprint length: 30 days
Primary goal: validate faster monetization paths without weakening SmartPetGuide's independent editorial trust.

## Why This Exists

SmartPetGuide already has content, product data, Pinterest assets, GA4 tracking, review templates, comparison pages, and a research methodology. The current bottleneck is not content production. The bottleneck is commercial validation:

- Can readers click affiliate CTAs and eventually buy?
- Can brands respond to a useful, low-friction partnership offer?
- Can the site's research/GEO capability be sold as a service before organic traffic matures?

## 合并决策（2026-06-29）

原始三轨道（A/B/C）经可行性评估后合并为两轨道：

| 原始 | 合并后 | 原因 |
|------|------|------|
| Task A: Amazon Affiliate | **Task A: 后台基建**（降级，3 天一次性完成） | 当前 GSC 仅 3 次点击，30 天内不可能有可量化收入信号；但基础设施应该现在就建好 |
| Task B: Brand Partnerships | **Brand Outreach（B+C 合并）** | B 和 C 打的是同一批 12 个品牌，分开外联会自我竞争，价值主张也高度重叠 |
| Task C: Visibility Audit | ↑ 合并入 Brand Outreach | 免费可见性快照 → 付费深度审计（$199/$499/$1,200），一个入口一个阶梯 |

## 执行顺序

1. **Task A（后台基建）** — Week 1 前 3 天，一次性完成页面优化，不等结果
2. **Brand Outreach（B+C 合并）** — Week 1 后段 ~ Week 4，唯一主动外联轨道

## Track Files

- `30-day-schedule.md` — 合并版 30 天逐日排期
- `task-a-amazon-affiliate-conversion.md` — Task A 详细需求（页面优化+决策模块+CTA）
- `task-b-brand-partnerships.md` — 原始 Task B 需求（已合并，保留供参考）
- `task-c-pet-tech-visibility-audit.md` — 原始 Task C 需求（已合并，保留供参考）
- `brand-outreach-crm.md` — 合并后的统一外联 CRM（待创建）
- `pet-tech-audit-template.md` — 12 节审计模板（待创建）
- `amazon-conversion-log.md` — 联盟链接审核日志（待创建）

## 外联策略（合并后）

**一个品牌只收一封邮件。** 顺序如下：

1. D0 开场：3 个具体的买家问题/内容缺口，指向已有 SmartPetGuide 提及
2. D3 跟进：提供免费可见性快照
3. D7 闭环：确认对接人是否正确

品牌回复后，再根据回复内容决定推免费快照还是付费审计。

## Shared Context To Read First

Read these before changing files:

- `PROJECT-OVERVIEW.md`
- `task_plan.md`
- `MONTH-1-THIRD-PARTY-AUDIT.md`
- `weekly-report.md`
- `src/data/products.json`
- `src/layouts/BaseLayout.astro`
- `src/components/ProductCard.astro`
- `src/pages/reviews/[slug].astro`
- `src/pages/guides/[slug].astro`
- `src/pages/compare/[slug].astro`
- `src/pages/best/[slug].astro`
- `backlinks/brand-outreach-template.md`

## Global Constraints

Do:

- Keep all claims research-backed.
- Use "analyzed", "reviewed owner feedback", "compared", "researched", and "verified owner reviews".
- Preserve affiliate disclosure and `rel="sponsored"` for affiliate links.
- Add documentation for every new monetization asset.
- Run `npm run build` after code/page changes.

Do not:

- Send emails.
- Submit forms.
- Contact brands.
- Create external accounts.
- Fabricate emails, testimonials, sales, traffic, rankings, or review counts.
- Reintroduce "hands-on", "tested", or "we tested" wording unless there is specific proof.
- Accept or imply paid ranking manipulation.

## Sprint Success Criteria

By the end of 30 days, the project should have:

- A live or ready-to-ship `/for-brands/` page with free snapshot → paid audit ladder.
- A reusable 12-section audit template.
- A unified brand outreach CRM with 12+ seeded rows.
- A revised brand outreach template that gives value before asking.
- One repo-based sample mini-audit.
- Five affiliate-focused pages improved with decision modules and verified CTAs.
- An Amazon link tracking log.

**关键成功指标：有没有任何一个品牌说「这个有用，发我更多」。**

## Manual Work Queue

Claude Code should create assets and templates only. The human operator handles:

- Sending emails.
- Replying to brands.
- Logging into support portals.
- Publishing Pinterest pins if CAPTCHA blocks automation.
- Verifying Amazon Associates orders.
- Making final pricing or negotiation decisions.
