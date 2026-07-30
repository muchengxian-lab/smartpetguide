# SmartPetGuide — 宠物智能设备英文内容站

## Claude Code Monetization Sprint

30 天变现验证 sprint 已于 2026-07-29 完成 D30 分轨裁决：Task A `Keep — maintenance only`、Brand Outreach `Pause — cold outbound`、Editorial/Guest Post `Continue cautiously`。下表保留历史执行结构：

| Track | 定位 | 周期 |
|------|------|------|
| Task A: Amazon Affiliate | 后台基建 | Week 1 前 3 天，一次性完成 |
| Brand Outreach（B+C 合并） | 唯一主动外联 | Week 1-4 |

Claude Code 在执行任何相关工作前必须先读：

1. 根目录 `CLAUDE.md`
2. `docs/claude-execution-guardrails.md` — Week 12 防错与验收规则
3. `docs/month-2-strategy-2026-07-13-to-2026-08-09.md` — 四周方向、目标与触发条件
4. `task_plan.md` 顶部 Week 12 活跃区与当天排班
5. `docs/monetization/README.md` — 合并决策说明
6. `docs/monetization/30-day-schedule.md` — 合并版逐日排期
7. `docs/monetization/task-c-pet-tech-visibility-audit.md` — 原始 Task C（已合并，保留供参考）
8. `docs/monetization/task-b-brand-partnerships.md` — 原始 Task B（已合并，保留供参考）

当前顺序：Task A 只维护；GA4 唯一实验、GSC 7/28 实时 9 URL 分诊、Shopping/Enhancements 下降诊断、Review/Product schema 合规修复与 7/29 D30 裁决均已完成。7/30 Feeder Reliability coverage-gap 也已完成：jamming 与 portion/calibration 无需重复修改，主旅行指南已补足 offline schedule、断电/联网多故障和人工照看兜底。下一步只按 7/31 排班读取新数据。Pretty Happy Pets 跟进已 `Sent-confirmed`，不得重复发送；Round 4 剩余三封继续 Hold。

禁止自动发邮件、提交外部表单、联系品牌、伪造联系人/流量/销售数据，禁止把付费合作写成编辑推荐排名。

## 日期校准（每次会话必读）

- **项目起点**：2026-05-19（历史 Day 1；不要再从该日期手算星期）
- **当前日期**：根据系统日期计算，会话开始时自动校准
- **Week/星期**：只使用系统日期和 `task_plan.md` 当前排班，不再用 Day 编号或项目起点推算

> ⚠️ **不再使用 Day 编号**（Day 编号已严重漂移不可信），改用实际日期+Week 编号。
> 每次会话开始时，根据系统日期重新计算今天星期几、Week 几。
> 写进度日志时使用实际日期（如 `6/18 周四`），不用 Day 编号。

**域名：** https://smartpetguide.net
**技术栈：** Astro 5 + Tailwind CSS v3，纯静态生成
**部署：** Vercel（`vercel.com/muchengxian-labs-projects/smartpetguide`），GitHub push 自动部署
**数据源：** `src/data/products.json`（26款产品，6品类）
**设计系统：** Forest + Honey 编辑杂志风（Fraunces + Atkinson Hyperlegible）

## 当前阶段

Week 12 为 2026-07-27 周一至 2026-08-02 周日。7/26 Snapshot 10：114 页；完整 7 天 GSC Performance 为 0 clicks / 19 impressions / position 21.7，3 个月 307 impressions / 4 clicks；GA4 最近 7 天 29 active / 28 new / 36 page views / 121 events，affiliate/outbound/key events 0；Pinterest 30 天 801 impressions / 0 outbound；Semrush 沿用 7/17 的 12 RD / 28 backlinks / 20 keywords / AS 2。7/28 实时 GSC Indexing 为 28 indexed / 23 unindexed、crawled-not-indexed 9；修复前 Shopping/Enhancements 为 Product 1/0、Merchant 1/0、Breadcrumb 10/0、Review 2/0，人工处置与安全问题均为 0。Review/Product 合规修复已移除评测页第三方评分/联盟 Offer 富结果标记，Google 重抓后 Product/Merchant/Review 数量下降属于预期。7/30 Feeder Reliability coverage-gap 已完成 3/3，并只实质修改主旅行指南 1 页。Pretty Happy Pets 仍在编辑/兽医审稿，一次轻量跟进已由用户实际发送；Round 4 Batch A 0/2 回复。
90 天目标：150-180 页 / 60-100 索引 / 25-40 引用域名 / GEO Score 85+。

## 核心策略

- 主线从内容生产切换为索引、外部权威和现有页加固
- Week 12 新页面固定为 0；只有 coverage-gap 证明具体缺口时最多加固 1 个现有页
- 每周 3-5 小时编辑型外链/PR，区分发送、回复、接受和落链
- GEO 只做现有页的 identity/source/date/answerability，不再开技术 GEO 冲刺
- Pinterest 只维护，出站点击破 0 前不恢复铺量
- Round 4 Batch A 已发送且 0/2 回复；BarkyTech / Purely Wholesome / PetsAnalysis 继续 Hold，不因零回复机械发送
- 自动化修复不在本仓库执行；只读取 `docs/ai-signal-automation-optimization-handoff-2026-07-19.md` 了解边界

## 工作流

任何执行先遵守 `docs/claude-execution-guardrails.md`。每天最多 3 个 P0；修改 2-3 项后做一次 diff/build/status 检查。

Week 12 开工使用 `docs/claude-week12-execution-prompt-template.md`；Week 11 模板仅作历史。收工前逐项完成当前模板的文件同步矩阵，不得只改页面而漏更计划/进度，也不得只改日志而漏验收源码和线上状态。

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
