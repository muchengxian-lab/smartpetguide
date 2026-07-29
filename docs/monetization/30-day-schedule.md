# 30-Day Monetization Schedule（合并版）

Start point: D0 为文档设置日 2026-06-29。
如果执行推迟，保持 D 编号顺序，日期顺延。Claude Code 执行 build/document/code 任务。Human-only 任务已标明，不得自动化。

## 合并逻辑

Task B（品牌合作）和 Task C（可见性审计）打的是同一批品牌、同一种触点，分开外联会自我竞争。合并为单一「Brand Outreach」轨道：

- 一个入口页 `/for-brands/`
- 一个价值主张：「我们发现你的产品在市场上被忽略了 3 个信号」
- 一个阶梯：免费可见性快照 → 付费深度审计（$199/$499/$1,200）

Task A（Amazon 联盟）降级为后台基建——花 3 天一次性做完页面优化，不期望 30 天内有可量化的收入信号。

## 执行顺序

1. **Task A（后台基建）** — ✅ D1-D3 已完成（2026-06-29）
2. **Brand Outreach（B+C 合并）** — ✅ D4-D30 已完成；7/29 最终裁决为暂停冷外联，仅保留触发式再评估

## 执行进度

- **已完成阶段**：D0-D30（2026-06-29 ~ 2026-07-29，部分阶段压缩执行）
- **最终里程碑**：7 个实际联系品牌中 1 个回复（Aorkuler，1/7 = 14.3%）；其认可交付质量但暂不实施。付费 beta、预算讨论、实施信号均为 0。
- **D30 实时核对**：截至 7/29 20:22，Homerunpet 仍只有我方 7/15 邮件；Round 4 Batch A 仍为 0/2 回复；Pretty Happy Pets 最新是我方 7/28 跟进，共享 DOCX 显示 0 条新评论、上次修改在 13 天前。
- **最终裁决**：Task A `Keep — maintenance only`；Brand Outreach `Pause — cold outbound`，只在暖线索、明确预算/痛点或 60-90 天后的实质触发下再评估；Editorial/Guest Post `Continue cautiously`，只推进已有审稿/回复，不扩发送量。
- **日期校准**：2026-07-26 是周日；下一工作周为 2026-07-27 周一至 2026-08-02 周日。D 编号代表阶段，不等于自然日。

## Operating Rules

- 一次只做一个构建任务
- 保留编辑独立性：不卖排名、不伪造实测、不编数据
- `npm run build` 在 Astro/组件/页面变更后执行
- 每天结束时更新 `progress.md`
- 里程碑完成后更新 `task_plan.md`

## Daily Schedule

| Day | 建议日期 | Track | Claude Code 任务 | Human 任务 | 产出 / 验收 |
|---:|------|------|------|------|------|
| D0 | 2026-06-29 | Setup | ✅ 创建 sprint 文档和入口点 | 无 | `docs/monetization/` 存在，task_plan 有 sprint 索引 |
| D1 | 2026-06-29 | **A** | ✅ 审核目标页面的联盟链接，创建 `amazon-conversion-log.md`；标注搜索链接需确认 ASIN 的项 | 确认需要手动查 ASIN 的链接 | 联盟链接审核表存在 |
| D2 | 2026-06-29 | **A** | ✅ 前 3 个高优先级 review 页面添加购买决策模块（Petlibro/AmazonBasics/LR5）；`npm run build` | 无 | 3 页已改善 |
| D3 | 2026-06-29 | **A** | ✅ 2 个 guide 页面加底部产品推荐 CTA；确认 `rel="sponsored"`；更新 `progress.md` | 无 | 5+ 页已改善，Task A 后台基建完成 |
| D4 | 2026-06-29 | Outreach | ✅ 创建 `/for-brands/` 页面（免费快照 + $199/$499/$1,200 阶梯 + 编辑边界）；`npm run build` | 审核页面定位和联系邮箱 | `/for-brands/` 页面存在且构建通过 |
| D5 | 2026-06-29 | Outreach | ✅ 创建 `pet-tech-audit-template.md`（12 节审计模板） | 无 | 审计模板存在 |
| D6 | 2026-06-29 | Outreach | ✅ 创建 `brand-outreach-crm.md`，种子 12 行品牌数据（不编造邮箱）；重写 `backlinks/brand-outreach-template.md`，标记旧模板为历史 | 无 | CRM 存在 + 新外联序列替换旧版 |
| D7 | 2026-06-29 | Outreach | ✅ 创建一个 repo-based 样本迷你审计（Aorkuler）；标注「repo-based sample only」 | 选择 Aorkuler 或其他小品牌作为首个外联目标 | 样本审计存在 |
| D8 | 2026-06-29 | Outreach | ✅ QA 全部交付物：页面/模板/CRM/样本审计；检查无付费排名承诺；`npm run build` | 审核定价（$199/$499/$1,200）和首批 5 个优先品牌 | Brand Outreach 交付包就绪 |
| D9 | 2026-07-01 | Outreach | ✅ 准备外联发送包：D0 开场邮件 + D3 跟进 + D7 闭环模板 | **发送第一波：4/5 品牌** | CRM 状态已更新 |
| D10 | — | Outreach | 跳过（发送无问题，无模板修复需求） | — | — |
| D11 | 2026-07-01 | Follow-up | ✅ 为 Wave 1 准备 D3 跟进草稿（4 品牌） | **按正确日历：7/4 周六 D3 跟进；若已提前发送则只更新 CRM** | CRM 跟进日期校正 |
| D12 | 2026-07-01 | Measure | ✅ 创建 `weekly-metrics-log.md`；GA4 affiliate_click/outbound_click 跟踪正常但零触发 | 已手动检查 GA4 source/medium | 度量日志就绪 |
| D13 | 2026-07-03 | Outreach | ✅ 准备第二波外联包（Homerunpet/CATLINK/Honey Tour/WOPET/Petlibro） | **已发送 WOPET + Petlibro；剩余 3 品牌查联系方式** | CRM 更新 |
| D14 | 2026-07-06 | Follow-up | ✅ 准备 D3 文案 + 写入 CRM | ✅ **已发送 WOPET/Petlibro D3** | CRM 已更新 ✅ |
| D15 | 2026-07-08 | Follow-up | ✅ D7 闭环 + check-in 文案 | ✅ **KittySpout/YEAPAW/Elspet D7 已发 + Aorkuler check-in 已发** | CRM 已更新 ✅ |
| D16 | 2026-07-08 | Content | 如果 Aorkuler 或其他品牌询问详情，准备一页试点方案/定制审计大纲 | 人工回复/推进 | 试点方案模板存在 |
| D17 | 2026-07-09 | Outreach | 根据 Wave 1 回复情况改进外联 v2；准备备选标题行 | 无 | 外联 v2 就绪 |
| D18 | 2026-07-10 | Review | 第 2 周复盘：回复数、意向信号、模板效果、是否补发 Wave 2 剩余 3 品牌 | 决定是否继续按相同节奏推进 | 第 2 周决策记录 |
| D19 | 2026-07-10 | Follow-up | 为 WOPET/Petlibro 准备 D7 闭环 | **发送 Wave 2 D7 闭环** | CRM 状态更新 |
| D20 | 2026-07-13 | Review | 复核 1/6 回复、邮箱 1/4、表单 0/2；不扩 10 个 CRM 占位 | 确认 Homerunpet email-first v2 小试点 | 小样本决策记录 |
| D21 | 2026-07-15 | Outreach | Aorkuler 无回复时做最后一次轻量收口；向 Homerunpet 发 v2 D0 | 人工发送 | CRM 更新 |
| D22 | 2026-07-17 | Review | ✅ Aorkuler 验证交付质量但无实施需求；Homerunpet 等待回复；Guest Post 已交稿 | ✅ Week 11 Continue，但不扩大 Brand 名单 | 第 3 周决策已记录 |
| D23 | 2026-07-21 | Outreach | Round 4 Batch A：定制 GlobalPETS + The Upper Pawside 两个资产角度 | 人工审核并发送 2 封 | 2 封 Sent-confirmed；记录角度与时间 |
| D24 | 2026-07-22 | Measure | 监看 Pretty Happy Pets Google Doc 与 Round 4 首批反馈 | 仅处理真实评论/回复 | 不主动催稿，不扩 Brand 名单 |
| D25 | 2026-07-24 | Review | 比较 Round 4 首批的回复、编辑问题与零反馈 | 决定剩余 3 封 Continue / Revise / Hold | 不把发送数量当成果 |
| D26 | 2026-07-25 | Editorial | 若 PHP 有评论则修订；若对方提案到达则独立审核 | 人工确认修改或选题决定 | 不承诺 reciprocal/dofollow |
| D27 | 2026-07-26 | Review | ✅ 已汇总 GA4 归因、编辑合作、Homerunpet 与 Round 4 信号 | ✅ Week 12 维持资源比例，战术收敛为单集群/单实验/外联止损 | Week 11 收盘已写入周报、计划和 metrics |
| D28 | 2026-07-27 | Review | ✅ 已比较 Aorkuler 正向 not-now、Homerunpet 0 reply、Batch A 0/2 replies 与 PHP 审稿无更新；当前可复制的是证据型交付/编辑关系，不是发送量 | ✅ 用户已确认：`EXP-44C79107` 已激活为唯一 Active；PHP 一次轻量跟进已 `Ready for human` | ✅ 生命周期重建为 38 total / Active 1 / Backlog 31；editorial 进展未混入 Brand 回复率；未扩名单、未发送邮件 |
| D29 | 2026-07-28 | Cleanup | ✅ 最终文档清理、GSC Indexing/Enhancements 诊断、Review/Product schema 合规修复与重定向原因桶核对完成 | ✅ Pretty Happy Pets 一次轻量跟进已在原线程实际发送，`Sent-confirmed` | ✅ `146b9fb` 已部署；26/26 防回归通过；重定向错误新验证待定 4/失败 0；5 个 URL 精准请求重抓；不扩写内容、不重复发信 |
| D30 | 2026-07-29 | Decision | ✅ 30 天总结完成：Amazon 基建、Brand 回复/意向、Editorial 关系、GA4 商业事件与下一步已分轨复盘 | ✅ Task A Keep（maintenance only）；Brand Outreach Pause（cold outbound）；Editorial/Guest Post Continue cautiously | ✅ 最终结论同步至 schedule、CRM、Round 4、metrics、月度战略、task plan、findings 与 progress；不把编辑合作计入 Brand 成功 |

## D30 最终裁决（2026-07-29）

| 轨道 | 30 天证据 | 裁决 | 下一步与重开条件 |
|------|------|------|------|
| Task A — Amazon 联盟基建 | 5 个决策模块、2 个 guide CTA、26 个产品 affiliate tag、模板 `rel="sponsored"` 与 GA4 事件代码均保留；最新已验证 GA4 基线仍为 `affiliate_click=0`、`outbound_click=0`、key events=0 | **Keep — maintenance only** | 不追加 CTA、不因零事件返工。周五继续轻量观察；只有真实点击或明确页面缺口才进入现有页优化 |
| Brand Outreach | 7 个实际联系品牌中 1 个回复（14.3%）；Aorkuler 认可报告但不实施；Homerunpet 14 天 0 reply；付费 beta / 预算 / 实施信号均为 0 | **Pause — cold outbound** | PETKIT/Catit 和新名单不发送。暖入站、明确预算/痛点、产品/渠道实质变化，或 Aorkuler 60-90 天后出现新触发时再评估；不是按日期自动重启 |
| Editorial / Guest Post | Pretty Happy Pets 已接受选题并进入 editorial + veterinary review；稿件已交、7/28 已做一次跟进，但尚无评论、发布或落链。Round 4 Batch A 为 0/2 | **Continue cautiously** | PHP 只处理真实评论、提案、采用或发布消息；Round 4 剩余 3 封继续 Hold；没有编辑反馈时不扩量、不重复跟进 |

**边界：**编辑接受、审稿和未来可能的 guest post 是关系/权威信号，不是 Brand 付费验证。`EXP-44C79107` 仍是唯一 Active 实验，D30 不新增实验或归因工具。

## 周里程碑

### Week 1（D0-D7）：建基建 + 建触点
- D1-D3：Task A 后台基建一次性完成（5+ 页决策模块、联盟链接审核、`rel="sponsored"` 合规）
- D4-D7：Brand Outreach 交付包（`/for-brands/` 页面、审计模板、CRM、样本审计、新外联序列）
- 不做任何外联

### Week 2（D8-D14）：第一波外联 + 跟进
- D8-D9：QA 交付包 → 人类发送第一波 5 封
- D10-D14：D3/D7 跟进 + 第二波 5 封
- 关键信号：有没有任何一个品牌回复了

### Week 3（D15-D21）：深入学习 + 调整
- 对回复者深入跟进（定制审计大纲/试点方案）
- 根据回复/沉默情况调整外联文案
- CRM 扩容（如有正向信号）

### Week 4（D22-D30）：复盘 + 决策
- 逐周信号对比
- 「为什么没回复」诊断（如适用）
- 最终 keep/kill/iterate 决策

## 成功指标（现实主义版）

| Track | 14 天信号 | 30 天信号 | 决策规则 |
|------|------|------|------|
| **Brand Outreach** | 10+ 封邮件发出，≥1 封真实回复 | 1 个付费 beta 或 3 个认真回复（"发我更多"/"这个有用"） | 有任何品牌显示预算或明确痛点 → 继续；零回复 → 反思定价/目标/触点 |
| **Task A（后台）** | 5+ 页改善，审核日志存在 | 基础设施就绪，不做收入预期 | 长期保留，不因无短期数据而中止 |

## 冷外联预期管理

- B2B 冷邮件典型回复率：**1-3%**
- 发 10 封 → 预期 0-1 封回复
- 发 20 封 → 预期 0-2 封回复
- **30 天内最重要的不是收入，而是「有没有任何一个品牌说『这个有用』」**
- 如果 20 封零回复：问题可能在定价、目标选择或触点方式，需要诊断而非放弃

## 时间紧张时的砍项顺序

优先砍：
1. 第三波外联（D25）
2. CRM 扩容（D20）
3. Pinterest 实验映射（已移除出主日程）

不砍：
1. GSC URL 检查
2. 重大页面更改后的 Sitemap 重提交
3. 每周信任/声明一致性检查
4. `npm run build` 验证
