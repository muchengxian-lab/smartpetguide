# Claude Code Entry Point

This repository is SmartPetGuide, an Astro 5 + Tailwind static site for research-backed smart pet device reviews.

Before executing any new monetization work, read these files in order:

1. `docs/claude-execution-guardrails.md` for the current execution and evidence rules.
2. `docs/month-2-strategy-2026-07-13-to-2026-08-09.md` for the fixed four-week direction and trigger rules.
3. `task_plan.md`, `findings.md`, and `progress.md` for the active planning system.
4. `.claude/CLAUDE.md` for project context.
5. `PROJECT-OVERVIEW.md` for historical background only; do not use its old metrics as current facts.
6. `docs/monetization/README.md` for the current 30-day monetization validation sprint.

## Current Special Sprint

The active business experiment is the SmartPetGuide monetization validation sprint. Task A is complete; Week 10 uses a small-sample Brand Outreach validation rather than broad CRM expansion:

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

Current order:

1. Read the guardrails, active Week 10 plan, 30-day schedule, and CRM.
2. Keep Task A in maintenance mode; do not add conversion infrastructure without a measured gap.
3. Brand Outreach: close Aorkuler once if needed and run only the Homerunpet email-first v2 pilot.
4. Track `Drafted`, `Ready for human`, `Sent-confirmed`, `Replied`, and `Placed` separately.

## Non-Negotiable Rules

- Before any date-sensitive planning or status update, run `Get-Date -Format "yyyy-MM-dd dddd"` in the project shell and use that output as the source of truth. Do not infer weekdays from model memory.
- When the user says today/tomorrow/next week/Friday, convert it to an absolute date in the note you are editing.
- For the current sprint calibration: 2026-07-13 is Monday; the current work week is 2026-07-13 Monday through 2026-07-17 Friday.
- Before saving schedule edits, re-check the current and next-week calendar. Do not repeat the prior drift where July 4 was labeled Friday, July 7 Monday, or July 11 Friday.
- Do not send emails, submit forms, create external accounts, or contact brands. Generate templates and CRM rows only.
- Do not claim hands-on testing unless the repository already contains proof for that specific product.
- Do not sell paid rankings or paid first-place recommendations.
- Sponsored placements, if implemented later, must be explicitly labeled and must not change editorial rankings.
- Preserve the site positioning: research-backed, independently written, based on verified owner reviews, product specs, BSR signals, and marketplace data.
- Run `npm run build` after code or page changes.
- Update `progress.md` after completing a task and update `task_plan.md` status if a sprint item changes.
- Never batch-refresh article `modifiedDate` values. Update dates per page only after a meaningful content or data change, using `src/data/content-dates.json`.
- Do not invent owner quotes or precise statistics. Exact quotes require a traceable URL and source ledger; otherwise use conservative paraphrase.
- After a failed edit, inspect the target file and `git diff` before marking the task failed or retrying.
- Derive counts from source/build output rather than copying an earlier summary.
- Do not use `git add -A`; preserve unrelated and untracked user files.
- Do not mark an email or form as sent unless the user explicitly confirms the external action.
