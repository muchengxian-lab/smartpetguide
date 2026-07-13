# Claude Execution Guardrails

> 生效日期：2026-07-13。用途：减少 Claude 在任务执行、事实引用、日期、状态同步和批量修改上的重复错误。每次开始 SmartPetGuide 任务前读取。

## Week 10 方向

- 主目标：让现有页面获得索引、引用、回复和分发，不追求任务数量或页面数量。
- 时间权重：外链/编辑型分发 35-40%；GSC 与现有页加固 25-30%；战略 GEO/VOC 20-25%；Pinterest 只维护。
- 新页面默认 0；只有 GSC 查询或跨来源 VOC 明确触发时才新增，单周最多 2 页。
- GEO 只做现有页的 `identity + source + date + quickAnswer + answerability`，不再启动新的技术 GEO 冲刺。

## Week 9 暴露的问题

| 问题 | 实际表现 | 下周防错规则 |
|------|------|------|
| 日期与阶段漂移 | 旧指令仍写 Week 9；历史上曾把星期写错 | 每次先运行 `Get-Date -Format "yyyy-MM-dd dddd"`；所有排期写绝对日期，不从 Day/Week 公式推算星期 |
| 当前指令互相冲突 | `.claude/CLAUDE.md` 仍要求每周 5-8 篇和 10 个 outreach，与 Week 10 方向冲突 | `task_plan.md` 顶部活跃区和本文件优先；历史计划只作背景 |
| 状态/数字漂移 | `quickAnswer` 实际 13/38，汇总仍写 8/38；CRM 顶部停在 D3 | 汇总数字必须用 Git、源码、构建或当前 CRM 明细复算；同一任务结束时同步当前事实文件 |
| 批量日期失真 | 模板改动曾把约 100 页 `modifiedDate` 一次刷新到 7/10 | 只有页面内容发生实质变化才更新该页日期；禁止按模板类型统一刷新日期；日期从 `content-dates.json` 逐页维护 |
| VOC 证据过度表达 | 曾写入无可核验来源的 owner quotes 和 70-90%、30-50% 等精确数字 | 原话必须有 URL、采集日期和 source ledger；否则只做保守转述；数字必须能追溯到明确来源或标为 editorial scenario |
| 编辑结果误判 | `are-self-cleaning-litter-boxes-worth-it` 被标记 Edit 失败，实际内容已落地 | 工具报错后先查目标文件、`git diff` 和构建结果，再判定成功/失败；不凭工具消息直接写状态 |
| 计数手工猜测 | llms 页面分类数、索引页数和页面总数发生过漂移 | 页面数从 build/dist/sitemap 计算；内容字段从源码检索；私有指标只用当次后台快照，不补猜测值 |
| 外部动作口径混写 | “邮件文案已备”“人工已发”“收到回复”曾出现在不同文件的不同状态 | 固定使用 `Drafted`、`Ready for human`、`Sent-confirmed`、`Replied`、`Placed`；没有用户确认不得写 Sent |
| 一次任务过密 | 同时处理过多小项后出现遗漏和重复修复 | 每天最多 3 个 P0；完成 2-3 个任务后做一次 diff/build/status 检查 |

## 开工检查

1. 运行 `Get-Date -Format "yyyy-MM-dd dddd"`。
2. 运行 `git status --short`，记录已有改动和未跟踪文件；不要覆盖或顺手提交不属于当前任务的文件。
3. 读取 `task_plan.md` 顶部活跃区、`progress.md` 最近日志、`findings.md` 最近决策；涉及商业外联时再读 CRM 和 30 天排期。
4. 写清今天最多 3 个 P0、目标 URL/文件和验收标准，再开始修改。
5. 若旧文档与当前计划冲突，按以下顺序裁决：实时后台/用户确认 > Git/源码/build > `task_plan.md` 活跃区 > `progress.md` 页面级记录 > 周报与历史文档。

## 内容与证据规则

- 不把单条 Reddit、YouTube、Amazon 评论写成事实；High claim 至少需要跨来源重复或官方规格支持。
- 不生成无法追溯的引号。不能保留原话来源时，改为不带引号的保守概括。
- 所有百分比、寿命、故障率、节省金额和性能数字必须有可追溯来源；估算必须明确假设和日期。
- 先审计目标页是否已有相关答案，再决定修改；已有覆盖时记录“无需修改”，不重复堆内容。
- `quickAnswer` 只补有明确用户问题和页面缺口的页面，不追求机械覆盖率。

## 修改与验证规则

- 修改前列出目标 slug 和文件；禁止没有页面清单的全模板批量替换。
- `modifiedDate` 只在该页面正文、结论、数据或结构发生实质变化时更新。
- 代码或页面修改后必须运行 `npm run build`；纯文档修改运行 `git diff --check`。
- 构建后至少抽查 3 个受影响页面的可见日期、Schema、来源和目标内容；模板级改动抽查 5 页。
- 页面数、sitemap URL 数、quickAnswer 数等用命令复算，不能沿用记忆里的旧数字。
- 失败后不得原样重复：先读错误和实际文件状态；第二次尝试必须改变方法。

## 外联与状态规则

- Claude 只准备研究、名单、文案和 CRM 更新，不自动发邮件、提交表单或联系品牌。
- 只有用户明确确认后，CRM 才能从 `Ready for human` 改为 `Sent-confirmed`。
- Guest Post 的“已发送”不等于“获得外链”；周报分别统计 Sent、Reply、Accepted、Placed、Referring domain。
- Brand Outreach 每批最多 3 个品牌；当前只执行 Aorkuler 收口和 Homerunpet email-first v2 小试点。

## 收工检查

1. 运行 `git diff --check`、必要的 build 和目标页抽查。
2. 再运行 `git status --short`；禁止使用 `git add -A` 顺带加入未知文件，尤其是当前的 `date-trace.txt`。
3. 更新 `progress.md` 的页面级记录；任务状态变化时更新 `task_plan.md`；形成稳定决策时才更新 `findings.md`。
4. 对外联分别记录 Drafted / Ready / Sent-confirmed / Replied / Placed，不合并描述。
5. 最终汇报必须区分：完成了什么、验证了什么、未完成什么、需要人工做什么、结果指标是否变化。
