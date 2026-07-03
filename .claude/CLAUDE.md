# SmartPetGuide — 宠物智能设备英文内容站

## Claude Code Monetization Sprint

当前 30 天变现验证 sprint（2026-06-29 合并版）。三轨道合并为两轨道：

| Track | 定位 | 周期 |
|------|------|------|
| Task A: Amazon Affiliate | 后台基建 | Week 1 前 3 天，一次性完成 |
| Brand Outreach（B+C 合并） | 唯一主动外联 | Week 1-4 |

Claude Code 在执行任何相关工作前必须先读：

1. 根目录 `CLAUDE.md`
2. `docs/monetization/README.md` — 合并决策说明
3. `docs/monetization/30-day-schedule.md` — 合并版逐日排期
4. `docs/monetization/task-a-amazon-affiliate-conversion.md` — Task A 详细需求
5. `docs/monetization/task-c-pet-tech-visibility-audit.md` — 原始 Task C（已合并，保留供参考）
6. `docs/monetization/task-b-brand-partnerships.md` — 原始 Task B（已合并，保留供参考）

推荐顺序：先执行 A（后台基建，3 天做完不等结果），再执行 Brand Outreach（`/for-brands/` → 免费快照 → 付费审计 $199/$499/$1,200，一个品牌只收一封邮件）。

禁止自动发邮件、提交外部表单、联系品牌、伪造联系人/流量/销售数据，禁止把付费合作写成编辑推荐排名。

## 日期校准（每次会话必读）

- **项目起点**：2026-05-19 周一（Day 1）
- **当前日期**：根据系统日期计算，会话开始时自动校准
- **Week 计算**：(当前日期 - 5/19) / 7 天 = Week N（5/19-5/25=Week 1, 5/26-6/1=Week 2, 6/2-6/8=Week 3, 6/9-6/15=Week 4, 6/16-6/22=Week 5, ...）
- **星期几**：从 5/19=周一 推算（5/19→周一, 5/26→周一, 6/2→周一, 6/9→周一, 6/16→周一）

> ⚠️ **不再使用 Day 编号**（Day 编号已严重漂移不可信），改用实际日期+Week 编号。
> 每次会话开始时，根据系统日期重新计算今天星期几、Week 几。
> 写进度日志时使用实际日期（如 `6/18 周四`），不用 Day 编号。

**域名：** https://smartpetguide.net
**技术栈：** Astro 5 + Tailwind CSS v3，纯静态生成
**部署：** Vercel（`vercel.com/muchengxian-labs-projects/smartpetguide`），GitHub push 自动部署
**数据源：** `src/data/products.json`（26款产品，6品类）
**设计系统：** Forest + Honey 编辑杂志风（Fraunces + Atkinson Hyperlegible）

## 当前阶段

Week 8（2026-07-04 周五）。114 页在线，Pinterest 87 Pin / 5 Board，GSC 索引 14 / 点击 4，GEO Score 74。实验 Pin 10/12。变现 sprint D0-D17 已执行，外联 6/10 品牌已发，Aorkuler 已回复+快照已发。
90 天目标：150-180 页 / 60-100 索引 / 25-40 引用域名 / GEO Score 85+。

## 核心策略

- 边等边建，不等 SEO 数据回馈
- A20/B50/C30 内容分级（不做全 A 级精雕）
- KD<20 优先，大词等 6 个月后再说
- 每周 5-8 篇长尾内容 + 10 个 outreach 外链建设

## 工作流

写文章前调用 `seo-content-optimizer` → `article-content` 写 → `verify` 验证
设计改动用 `frontend-design`
Amazon 调研用 `agent-browser`
任何代码改动走 `superpowers:brainstorm` → `superpowers:write-plan` → `superpowers:execute-plan`

## 关键文件

- `src/data/products.json` — 产品数据库
- `src/pages/reviews/` — 评测页面
- `src/pages/compare/` — 对比页面
- `src/pages/best/` — Best 列表
- `src/pages/guides/` — 指南页面
- `SKILLS.md` — 21 个已配置 Skills 清单
- `task_plan.md` / `findings.md` / `progress.md` — 项目规划三件套
