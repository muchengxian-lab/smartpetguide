# Claude Code Entry Point

This repository is SmartPetGuide, an Astro 5 + Tailwind static site for research-backed smart pet device reviews.

Before executing any new monetization work, read these files in order:

1. `.claude/CLAUDE.md` for legacy project context.
2. `PROJECT-OVERVIEW.md` for the full project history.
3. `task_plan.md`, `findings.md`, and `progress.md` for the active planning system.
4. `docs/monetization/README.md` for the current 30-day monetization validation sprint.

## Current Special Sprint

The active business experiment is the SmartPetGuide monetization validation sprint. Original three tracks merged into two (2026-06-29):

| Track | 定位 | 周期 |
|------|------|------|
| Task A: Amazon Affiliate | 后台基建，一次性完成 | Week 1 前 3 天 |
| Brand Outreach（B+C 合并） | 唯一主动外联轨道 | Week 1 ~ Week 4 |

Key files:

0. `docs/monetization/30-day-schedule.md` — 合并版逐日排期
1. `docs/monetization/README.md` — 合并决策说明
2. `docs/monetization/task-a-amazon-affiliate-conversion.md` — Task A 详细需求
3. `docs/monetization/task-b-brand-partnerships.md` — 原始 Task B（已合并，保留供参考）
4. `docs/monetization/task-c-pet-tech-visibility-audit.md` — 原始 Task C（已合并，保留供参考）

Recommended order:

0. Read the 30-day schedule and README
1. Task A: Amazon Affiliate（后台基建，3 天做完不等结果）
2. Brand Outreach: `/for-brands/` 页面 → 免费快照 → 付费审计（$199/$499/$1,200）
   - 只外联一次，一个品牌只收一封邮件
   - 当前 GSC 仅 3 次点击，30 天核心指标不是收入，是「有没有品牌回复」

## Non-Negotiable Rules

- Before any date-sensitive planning or status update, run `Get-Date -Format "yyyy-MM-dd dddd"` in the project shell and use that output as the source of truth. Do not infer weekdays from model memory.
- When the user says today/tomorrow/next week/Friday, convert it to an absolute date in the note you are editing.
- For the current sprint calibration: 2026-07-03 is Friday; the next work week is 2026-07-06 Monday through 2026-07-10 Friday.
- Before saving schedule edits, re-check the current and next-week calendar. Do not repeat the prior drift where July 4 was labeled Friday, July 7 Monday, or July 11 Friday.
- Do not send emails, submit forms, create external accounts, or contact brands. Generate templates and CRM rows only.
- Do not claim hands-on testing unless the repository already contains proof for that specific product.
- Do not sell paid rankings or paid first-place recommendations.
- Sponsored placements, if implemented later, must be explicitly labeled and must not change editorial rankings.
- Preserve the site positioning: research-backed, independently written, based on verified owner reviews, product specs, BSR signals, and marketplace data.
- Run `npm run build` after code or page changes.
- Update `progress.md` after completing a task and update `task_plan.md` status if a sprint item changes.
