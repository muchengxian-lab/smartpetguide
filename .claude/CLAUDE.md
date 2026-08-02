# SmartPetGuide — 宠物智能设备英文内容站

## Claude Code Monetization Sprint

30 天变现验证 sprint 已于 2026-07-29 完成 D30 分轨裁决：Task A `Keep — maintenance only`、Brand Outreach `Pause — cold outbound`、Editorial/Guest Post `Continue cautiously`。下表保留历史执行结构：

| Track | 定位 | 周期 |
|------|------|------|
| Task A: Amazon Affiliate | 后台基建 | Week 1 前 3 天，一次性完成 |
| Brand Outreach（B+C 合并） | 唯一主动外联 | Week 1-4 |

Claude Code 在执行任何相关工作前必须先读：

1. 根目录 `CLAUDE.md`
2. `docs/claude-execution-guardrails.md` — Week 13 防错与验收规则
3. `docs/month-2-strategy-2026-07-13-to-2026-08-09.md` — 四周方向、目标与触发条件
4. `task_plan.md` 顶部 Week 13 活跃区与当天排班
5. `docs/monetization/README.md` — 合并决策说明
6. `docs/monetization/30-day-schedule.md` — 合并版逐日排期
7. `docs/monetization/task-c-pet-tech-visibility-audit.md` — 原始 Task C（已合并，保留供参考）
8. `docs/monetization/task-b-brand-partnerships.md` — 原始 Task B（已合并，保留供参考）

当前顺序：Week 12 已收盘，7/7 排班完成；执行 Green、增长结果 Adjust。Week 13 只按 8/3-8/9 排班执行 Month 2 收盘：Feeder Reliability 是唯一内容验证簇，Pretty Happy Pets 是既有编辑关系轨道，`EXP-44C79107` 是唯一 Active 且 Review 8/9。新 URL 0，不重复 8/1 GEO/llms/crawler 检查，不重复已入队 URL Inspection，不增加归因工具或第二实验。Pretty Happy Pets 7/28 跟进已 `Sent-confirmed`，不得再次主动跟进；Round 4 剩余三封继续 Hold。

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

Week 13 为 2026-08-03 周一至 2026-08-09 周日。Week 12 收盘：114 页；GSC 最新完整 7 天为 0 clicks / 9 impressions / position 22.6，对照前期 0 / 14 / 19.0；Page Indexing 总表仍为 28 indexed / 23 unindexed、crawled-not-indexed 9，但报告最后更新 7/24，URL 级证据为 4 indexed / 1 pending。重定向错误 4 的验证仍“已开始”；Product/Merchant/Review 撤标后的归零不得回滚或反推普通索引。GA4 7/24-7/30 为 33 sessions / 20 engaged / 143 events / 0 key events，Direct 不计自然/引荐获取。Pinterest 近 7 天为 2,003 impressions / 9 engagements / 0 outbound；近 30 天不同采集路径的 11,617 / 65 / 4 outbound 只作背景。Semrush 仍沿用 7/17 的 12 RD / 28 backlinks / 20 keywords / AS 2。GEO 79/100、100/100 基础事实层和 12/12 crawler 是 readiness，不是增长 uplift。PHP 仍按最后已验证状态处于编辑/兽医审稿；Round 4 Batch A 最新已验证 0/2。
90 天目标：150-180 页 / 60-100 索引 / 25-40 引用域名 / GEO Score 85+。

## 核心策略

- 主线从内容生产切换为索引、外部权威和现有页加固
- Week 13 新页面固定为 0；只有安全/事实一致性审计证明具体缺口时最多最小修复 1 个现有页
- 每周 3-5 小时编辑型外链/PR，区分发送、回复、接受和落链
- GEO 只做现有页的 identity/source/date/answerability，不再开技术 GEO 冲刺
- Pinterest 只维护，出站点击破 0 前不恢复铺量
- Round 4 Batch A 已发送且 0/2 回复；BarkyTech / Purely Wholesome / PetsAnalysis 继续 Hold，不因零回复机械发送
- 自动化修复不在本仓库执行；只读取 `docs/ai-signal-automation-optimization-handoff-2026-07-19.md` 了解边界

## 工作流

任何执行先遵守 `docs/claude-execution-guardrails.md`。每天最多 3 个 P0；修改 2-3 项后做一次 diff/build/status 检查。

Week 13 开工使用 `docs/claude-week13-execution-prompt-template.md`；Week 12 及更早模板仅作历史。收工前逐项完成当前模板的文件同步矩阵，不得只改页面而漏更计划/进度，也不得只改日志而漏验收源码和线上状态。

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
