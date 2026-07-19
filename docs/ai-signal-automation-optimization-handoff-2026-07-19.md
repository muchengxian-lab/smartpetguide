# AI Signal / 知识库自动化优化交接清单

> 交接日期：2026-07-19
> 用途：复制给知识库主控对话，由该对话在 `E:\knowledge-base` 与对应自动化脚本仓库中完成修复。
> 边界：本交接只描述问题、证据与验收标准；不得修改 `C:\Users\Administrator\smartpetguide` 的站点源码或自动改变 Signal / Experiment 状态。

## 一、给知识库主控对话的提示词

```text
请按 E:\knowledge-base\07 Maps\AI Agent Entry.md 的协议，修复 2026-W29 AI Signal、SmartPetGuide Knowledge Sync、L2 VOC、Knowledge Health 和 HTML Dashboard 的事实同步与数据质量问题。

执行边界：
1. 先读取 AI Agent Entry.md，再读取 W29 Weekly Review、VOC Input Audit、VOC Review、SmartPetGuide Project Snapshot、Knowledge Sync Audit、health.json、lifecycle.json 和当前 Dashboard。
2. SmartPetGuide 当前事实只读自 C:\Users\Administrator\smartpetguide 的 task_plan.md、progress.md、findings.md、Git 状态和已确认数据；不要修改 SmartPetGuide 源码。
3. 不得因为修复报表而自动修改 Signal State、实验结论或人工确认状态。
4. 保留历史记录，但当前汇总字段必须读取最新事实块，不能扫描到历史旧数字后误判。

必须修复的问题：
A. SmartPetGuide 事实同步
- 正确字段：7/13 的 discovered-not-indexed 已经是 0；本周变化是 crawled-not-indexed 8 -> 4，不能写成 discovered-not-indexed 8 -> 4 -> 0。
- GA4 的 US 用户不是首次出现：7/13 已有 6，7/17 为 7。
- Semrush 12 referring domains / 28 backlinks / 20 keywords / AS 2 已由用户在 7/17 人工确认。可以保留“新增 referring-domain URL 未识别”，但不能把总数写成待核验。
- quickAnswer 当前有效值是 13/38；健康检查命中历史段落中的 8/38 属于假冲突。解析器必须读取当前汇总字段或带日期的 authoritative block。

B. W29 VOC 时间窗口与跨产物一致性
- W29 标注 7/13-7/19，但 Input Audit 把 7/12 18:03-18:04 的 PAA 18 条和 Amazon 16 条计入，周报合计 175；7/19 Dashboard 显示 141，只包含 7/19 的 PAA 17 + Amazon 1 + YouTube 123。
- 明确定义自然周 inclusive date、rolling 7x24h 或 current batch 三种口径中的一种。周报、Input Audit、Dashboard 必须使用相同口径；如果有意展示不同口径，标题必须明确标注并分别显示。
- 增加跨产物断言：source file count、per-source row count、total rows 在 Input Audit / VOC Review / Dashboard 间一致，否则流程应 Warning 而不是静默发布。

C. VOC 来源质量与分类 QA
- W29 的 YouTube 为 123/175，约 70%，来源明显失衡；报告必须显示各主题的 per-source counts，而不只显示总记录数/来源数。
- 增加按 video/product/query 的去重统计，避免单个视频评论量支配 High confidence。
- 修正至少以下误分类："how to pull/remove the grain bucket/container for cleaning" 应归 setup/cleaning；"what is one portion" 应归 portion accuracy，不应归 WiFi/app/offline reliability。
- 每周随机抽查至少 10-20 条分类，并输出 precision issue / corrected label / affected theme count。

D. 从信号到页面任务的防重复闸门
- feeder WiFi/app/offline reliability 在 Week 9 已做 phrasing map 和页面 fact-layer 回填。再次产生页面任务前，先读取当前页面/Git，生成“信号 -> 已覆盖页面 -> 真实缺口 -> 是否需要改动”的 coverage-gap matrix。
- 已覆盖的信号只能进入 Watch / Reinforce evidence，不得机械生成重复改页任务。

E. 生命周期与实验队列
- 当前 104 signals / 93 active / 69 overdue；28 experiments / 0 active / 23 backlog / 15 overdue。
- 先做 overdue triage 与证据回填，不批量自动改变状态。
- 只提出一个 Active experiment 候选，建议使用 GA4 AI/referral attribution baseline；由用户确认后才能激活。4 个未索引页面检查属于日常维护，不必包装为实验。

F. Dashboard 与健康检查时间语义
- Knowledge Health 22:33 记录 Dashboard Pending Refresh，Dashboard 22:43 已成功刷新。这是调度先后，不是运行失败。
- Dashboard 应同时显示 health_generated_at 与 dashboard_generated_at；刷新后不能继续让用户误以为 Dashboard 尚未执行。
- PROJECT-OVERVIEW.md 已陈旧 31 天，明确标记为 stale background，不得作为当前 KPI 来源。

验收标准：
1. 重跑后，GSC discovered/crawled 两个桶位、US 用户和 Semrush 确认状态全部正确。
2. quickAnswer 不再因历史 8/38 触发当前冲突；当前值为 13/38。
3. W29 Input Audit、VOC Review、Dashboard 的窗口与总数一致，或明确标注为不同口径。
4. VOC 输出含 per-source theme counts、dedup counts 和 taxonomy QA 结果。
5. 页面动作先经过 coverage-gap matrix，不重复 Week 9 已完成工作。
6. 自动化不修改 SmartPetGuide 源码，不自动晋升/关闭 Signal 或 Experiment。
7. 输出修复文件清单、重跑命令、关键计数、仍需人工确认项。
```

## 二、已核验证据

| 项目 | 当前证据 |
|------|------|
| GSC 当前桶位 | indexed 33 / unindexed 15 / discovered-not-indexed 0 / crawled-not-indexed 4 |
| Semrush | 12 RD / 28 backlinks / 20 keywords / AS 2，用户 7/17 人工确认 |
| W29 VOC 周报 | PAA 35 / Amazon 17 / YouTube 123 / total 175 |
| 7/19 当前批次 | PAA 17 / Amazon 1 / YouTube 123 / total 141 |
| 被额外计入的 7/12 文件 | PAA 18（18:03）/ Amazon 16（18:04） |
| 生命周期 | 104 signals / 93 active / 69 overdue |
| 实验 | 28 total / 0 active / 23 backlog / 15 overdue |
| Dashboard | 2026-07-19 22:43 已刷新；Health 22:33 早于 Dashboard |

## 三、优先级

1. **P0：事实字段锁定与跨产物一致性**——避免错误周报继续进入计划。
2. **P0：VOC 时间窗口统一**——先解决 175 与 141 的口径冲突。
3. **P1：分类 QA、来源占比与去重**——降低错误 High confidence。
4. **P1：coverage-gap 防重复闸门**——避免自动化重复修改已覆盖页面。
5. **P1：生命周期/实验清理**——先回填证据，再由用户确认唯一 Active experiment。
6. **P2：Dashboard 时间语义与陈旧文件提示**。
