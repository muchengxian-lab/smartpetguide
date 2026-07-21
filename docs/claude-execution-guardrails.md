# Claude Execution Guardrails

> 生效日期：2026-07-19。用途：减少 Claude 在任务执行、事实引用、日期、状态同步和批量修改上的重复错误。每次开始 SmartPetGuide 任务前读取。

## Week 11 方向

- 主目标：让现有页面获得索引、引用、回复和分发，不追求任务数量或页面数量。
- 时间权重：外链/编辑型分发 35-40%；GSC 与现有页加固 25-30%；战略 GEO/VOC 20-25%；Pinterest 只维护。
- 新页面默认 0；只有 GSC 查询或跨来源 VOC 明确触发时才新增，单周最多 2 页。
- GEO 只做现有页的 `identity + source + date + quickAnswer + answerability`，不再启动新的技术 GEO 冲刺。
- 索引已达到 33；4 个已抓取未索引页面只按实质变化维护，主力转向 query/page、排名、CTR 和渠道归因。
- Round 4 按 2 + 3 分批；Batch A 两封已于 7/21 `Sent-confirmed` 并进入观察，剩余三封保持 hold。Brand Outreach 不扩量，Aorkuler 已关闭，只观察 Homerunpet。

## Week 9 暴露的问题

| 问题 | 实际表现 | 下周防错规则 |
|------|------|------|
| 日期与阶段漂移 | 旧指令仍写 Week 9；历史上曾把星期写错 | 每次先运行 `Get-Date -Format "yyyy-MM-dd dddd"`；所有排期写绝对日期，不从 Day/Week 公式推算星期 |
| 当前指令互相冲突 | 根目录与 `.claude/CLAUDE.md` 曾停留在 Week 10 或更早方向 | `task_plan.md` 顶部活跃区、本文件和 Week 11 提示词优先；历史计划只作背景 |
| 状态/数字漂移 | `quickAnswer` 实际 13/38，汇总仍写 8/38；CRM 顶部停在 D3 | 汇总数字必须用 Git、源码、构建或当前 CRM 明细复算；同一任务结束时同步当前事实文件 |
| 批量日期失真 | 模板改动曾把约 100 页 `modifiedDate` 一次刷新到 7/10 | 只有页面内容发生实质变化才更新该页日期；禁止按模板类型统一刷新日期；日期从 `content-dates.json` 逐页维护 |
| VOC 证据过度表达 | 曾写入无可核验来源的 owner quotes 和 70-90%、30-50% 等精确数字 | 原话必须有 URL、采集日期和 source ledger；否则只做保守转述；数字必须能追溯到明确来源或标为 editorial scenario |
| 编辑结果误判 | `are-self-cleaning-litter-boxes-worth-it` 被标记 Edit 失败，实际内容已落地 | 工具报错后先查目标文件、`git diff` 和构建结果，再判定成功/失败；不凭工具消息直接写状态 |
| 计数手工猜测 | llms 页面分类数、索引页数和页面总数发生过漂移 | 页面数从 build/dist/sitemap 计算；内容字段从源码检索；私有指标只用当次后台快照，不补猜测值 |
| 外部动作口径混写 | “邮件文案已备”“人工已发”“收到回复”曾出现在不同文件的不同状态 | 固定使用 `Drafted`、`Ready for human`、`Sent-confirmed`、`Replied`、`Placed`；没有用户确认不得写 Sent |
| 已发正文与仓库证据混写 | 人工发送后，仓库复用稿可能继续修订；UTM 备注也可能未真正附在链接上 | `Sent-confirmed` 只证明动作发生；另记 exact-body/UTM 是否 verified。发送后修订必须标为 reuse copy，不得反向改写成当时已发送内容 |
| 一次任务过密 | 同时处理过多小项后出现遗漏和重复修复 | 每天最多 3 个 P0；完成 2-3 个任务后做一次 diff/build/status 检查 |
| 项目文件漏更新 | 页面、外联、数据或战略状态只更新了一个文件 | 收工前逐项执行“文件同步矩阵”，每个变化必须说明已更新文件或明确 `N/A` 理由 |

## 开工检查

1. 运行 `Get-Date -Format "yyyy-MM-dd dddd"`。
2. 运行 `git status --short`，记录已有改动和未跟踪文件；不要覆盖或顺手提交不属于当前任务的文件。
3. 读取 `task_plan.md` 顶部活跃区、`progress.md` 最近日志、`findings.md` 最近决策；涉及商业外联时再读 CRM 和 30 天排期。
4. 写清今天最多 3 个 P0、目标 URL/文件和验收标准，再开始修改。
5. 若旧文档与当前计划冲突，按以下顺序裁决：实时后台/用户确认 > Git/源码/build > `task_plan.md` 活跃区 > `progress.md` 页面级记录 > 周报与历史文档。
6. 开工确认中列出“预计修改文件”；实际新增文件超出清单时说明原因，避免顺手扩大范围。

## 内容与证据规则

- 不把单条 Reddit、YouTube、Amazon 评论写成事实；High claim 至少需要跨来源重复或官方规格支持。
- 不生成无法追溯的引号。不能保留原话来源时，改为不带引号的保守概括。
- 所有百分比、寿命、故障率、节省金额和性能数字必须有可追溯来源；估算必须明确假设和日期。
- 对外价格/TCO 必须优先核对官方产品页和计划页，区分完整套装、替换件、标价、促销价与月费等值；涉及预付方案时不得把月费等值写成实际结账金额。
- 先审计目标页是否已有相关答案，再决定修改；已有覆盖时记录“无需修改”，不重复堆内容。
- `quickAnswer` 只补有明确用户问题和页面缺口的页面，不追求机械覆盖率。

## 修改与验证规则

- 修改前列出目标 slug 和文件；禁止没有页面清单的全模板批量替换。
- `modifiedDate` 只在该页面正文、结论、数据或结构发生实质变化时更新。
- 代码或页面修改后必须运行 `npm.cmd run build`；纯文档修改运行 `git diff --check`。
- 构建后至少抽查 3 个受影响页面的可见日期、Schema、来源和目标内容；模板级改动抽查 5 页。
- 页面数、sitemap URL 数、quickAnswer 数等用命令复算，不能沿用记忆里的旧数字。
- 失败后不得原样重复：先读错误和实际文件状态；第二次尝试必须改变方法。

## 外联与状态规则

- Claude 只准备研究、名单、文案和 CRM 更新，不自动发邮件、提交表单或联系品牌。
- 只有用户明确确认实际发送后，状态才能从 `Ready for human` 或 `Scheduled` 改为 `Sent-confirmed`；定时发送尚未发生时只能写 `Scheduled`。
- Guest Post 的“已发送”不等于“获得外链”；周报分别统计 Sent、Reply、Accepted、Placed、Referring domain。
- Pretty Happy Pets 确认回信已由用户于 **2026-07-20 13:00 Asia/Shanghai** 实际发送，当前为 `Sent-confirmed`；不得重复发送。
- Brand Outreach 每批最多 3 个品牌；Aorkuler 已关闭，不再联系；Homerunpet 只等待回复。Round 4 是独立的编辑型外联；GlobalPETS + The Upper Pawside 已发送，只观察回复，剩余三封保持 hold。

## 文件同步矩阵

| 发生的变化 | 必须核对/更新 | 不应误更新 |
|------|------|------|
| 每次执行会话 | `progress.md`；任务状态变化时 `task_plan.md` | 不为了凑记录修改 `findings.md` |
| 稳定结论、策略或边界变化 | `findings.md` + `task_plan.md`；命中月度触发条件时再改战略书 | 普通执行结果不改月度战略 |
| GSC / GA4 / Pinterest / Semrush 新快照 | `docs/monetization/weekly-metrics-log.md` + `progress.md`；周复盘时同步 `weekly-report.md` | 不把旧快照覆盖成新事实，不补猜缺失值 |
| Guest Post / 编辑型外联状态 | 对应 `backlinks/round*.md` + `progress.md` + `task_plan.md`；周快照时同步 metrics/report | 不写入 Brand CRM，不把 Accepted/Review 写成 Placed |
| Brand Outreach 状态 | `docs/monetization/brand-outreach-crm.md` + `progress.md`；阶段变化时同步 30 天排期 | 不把同一品牌的多次邮件重复计为新回复 |
| 页面正文、结论、数据或结构实质变化 | 目标源码 + 该页 `src/data/content-dates.json` + `progress.md` + `task_plan.md` | 不批量刷新其他页面日期 |
| 只有文档/提示词变化 | 对应文档 + `progress.md`；如改变执行规则则同步 Claude 入口文件 | 不改页面日期或站点数据 |
| AI Signal / 知识库自动化问题 | 只读交接清单并消费修正后的输出 | 不在 SmartPetGuide 仓库修自动化，不改 Signal/Experiment 状态 |

收工前必须逐条输出：`变化 -> 已同步文件 -> N/A 理由（如有）`。任何一项说不清楚都不算完成。

## 收工检查

1. 运行 `git diff --check`、必要的 build 和目标页抽查。
2. 再运行 `git status --short`；禁止使用 `git add -A` 顺带加入未知文件或历史误生成产物。
3. 更新 `progress.md` 的页面级记录；任务状态变化时更新 `task_plan.md`；形成稳定决策时才更新 `findings.md`。
4. 按“文件同步矩阵”复核相关文件，并在 `progress.md` 记录修改文件、验证命令和未完成边界。
5. 对外联分别记录 Drafted / Ready for human / Scheduled / Sent-confirmed / Replied / Accepted / Placed，不合并描述。
6. 若任务包含交付而非只读审查：只暂存本次明确文件，提交并推送；核对 `origin/master...HEAD` 为 `0 0`。站点源码有变化时再核验 Vercel READY 和受影响线上页面。
7. 最终汇报必须区分：完成了什么、更新了哪些文件、验证了什么、未完成什么、需要人工做什么、Git/部署状态和结果指标是否变化。
