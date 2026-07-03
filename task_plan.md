# SmartPetGuide 任务计划

**最后更新：2026-07-03 周四 | 114 页 / 86 Pin 在线 | 策略阶段：分发与验证驱动 | 实验 Pin 9/12 | 索引 14 冻结 5 周 | Wave 2 外联 2/5 已发**

> 核心策略：从"产出页面"切换到"获得分发"。继续 5-7 篇/周，但 40-50% 时间转向外链、GSC 反馈、Pinterest 出站实验、GA4 数据治理和高价值页面复用。

## 📋 两套任务体系协调

> 当前同时运行两套计划。每天开工时先读此表确认当天任务，收工时更新两边的状态。

| 体系 | 文件 | 角色 | 节奏 |
|------|------|------|------|
| **Week 8 内容+分发** | `task_plan.md`（本文件） | 日常生产引擎 | 每天 ~2-3h，周二至周五 |
| **30 天变现 Sprint** | `docs/monetization/30-day-schedule.md` | 商业验证轨道 | D1-D30，与 Week 排班协调 |

### 本周交叉排班（6/30-7/4）

| 天 | 日期 | Week 8 任务 | 变现 Sprint | 预计工时 |
|:--:|------|------|------|:--:|
| 周一 | 6/30 | PAA #1#2 + Petlibro 加固 + GSC 周检 + Pin #6 | Task A D1-D3 + GA4 周检 + Brand Outreach D4-D7 | ~3h（全部完成✅） |
| 周二 | 7/1 | PAA #3#4 + 内链补全 + Pin #7 + GSC + Sitemap | D8 QA + D9 外联准备 + Wave 1 发送 | ~2.5h（全部完成✅） |
| 周三 | 7/2 | PAA #5 + Robot #6 + GEO 复检 + 4 页加固 + Pin #8 | D10-D12 D3跟进+度量日志 | ~3h（全部完成✅） |
| 周四 | 7/3 | Robot #7#8 + GEO 模板修复 + 外链第 3 轮 + Pin #9 | D13 Wave 2（WOPET+Petlibro 已发，3 品牌待查联系方式） | 8/9 ✅ |
| 周五 | 7/4 | GEO 收尾 + NR + Pin #10 + 周复盘 | Wave 1 D3 跟进已发 + Aorkuler 快照已发 | 6/6 ✅ |

### 优先级规则
1. **GSC URL Inspection（5 个/天）** — 雷打不动，每天 5 分钟
2. **实验 Pin（1 个/天）** — 雷打不动，每天 10 分钟
3. **变现 Sprint 人工阻塞项优先** — 人类时间不可控，能推进的先推进
4. **内容生产** — 弹性，被 Sprint 挤占时从 C 级开始砍
5. **变现 Sprint Claude 可执行项** — 在内容生产间隙推进

---

## Monetization Validation Sprint（Claude Code 执行入口）

> 新增日期：2026-06-29。目标：把 SmartPetGuide 的 3 条更快变现路径整理成 Claude Code 可以逐条执行的项目文件。执行前先读根目录 `CLAUDE.md` 与 `docs/monetization/README.md`。
> **2026-06-29 更新**：原始三轨道合并为两轨道（Task A 后台基建 + Brand Outreach B+C 合并），Task A 已于当日 D1-D3 合并执行完成。

| Track | 目标 | 执行文件 | 状态 |
|------|------|------|:--:|
| Schedule | 30 天排期（合并版）：A→Brand Outreach 两轨道 | `docs/monetization/30-day-schedule.md` | D0-D12 已执行 |
| A | Amazon affiliate conversion：5 页决策模块 + 2 指南 CTA + 全站审核 | `docs/monetization/task-a-amazon-affiliate-conversion.md` | ✅ 完成 |
| Brand Outreach | B+C 合并：`/for-brands/` → 免费快照 → 付费审计 | `docs/monetization/task-b-brand-partnerships.md` + `task-c-pet-tech-visibility-audit.md` | 🔄 Wave 1 外联中，D3 跟进 7/4 |

### 内容选题引擎（6/26 起）

| 引擎 | 优先级 | 频次 | 产出类型 |
|------|:--:|------|------|
| **Google PAA** | 🔴 P0 | 每周 1 次，搜 3-4 个核心词 | C 级长尾（KD<10） |
| **Reddit 问题** | 🟡 P1 | 每周 1 次，扫描 r/CatAdvice+r/cats | C 级长尾 + 选题验证 |
| **Amazon NR** | ⚪ P2 | 每周 1 次（周六），仅监不追 | B 级新品评测（极少触发） |

> PAA 做法：在 Google 搜 `how to [品类词] [问题词]`，看 People Also Ask 和搜索结果中的问题式标题。每个高赞 Reddit 帖子的问题 = 一篇 C 级。NR 自动触发条件：BSR<10K + 评论<100 → 48h 出稿。

### Week 8 PAA 候选（6/26 已挖掘，待下周执行）

| # | 标题 | KD | 级别 | 工时 |
|---|------|:--:|:--:|:--:|
| 1 | How to Stop Your Automatic Feeder From Jamming (7 Fixes) | <5 | C | 30min |
| 2 | How to Introduce Cat to Automatic Litter Box (Without Scaring Them) | <5 | C | 45min |
| 3 | Cat Won't Drink From Water Fountain? 8 Reasons & Fixes | <5 | C | 30min |
| 4 | Why Does My Automatic Feeder Keep Disconnecting from WiFi? | <5 | C | 30min |
| 5 | How to Keep Your Cat From Breaking Into the Automatic Feeder | <5 | C | 30min |

### 今日任务状态（6/23 周二）

| 任务 | 状态 |
|------|:--:|
| C #1+#2 内容 | ✅ 6/22 已完成 |
| P1-1 GA4 基础看板 | ✅ 全部完成（outbound_click + debug过滤 + IP规则209.137.178.236 + 内部流量过滤器已启用） |
| GEO-P0-3 Wikidata 验证 | ✅ 4 属性全存在（P31/P571/P407/P856）+ description |
| GSC 索引请求 ×2 | ✅ 两篇已提交优先抓取队列 |
| 口径一致性周检 | ✅ 1 处修复（alltop-email.txt），src/pins 干净 |
| Pinterest 出站实验 Pin #1 | ✅ 已发布（Pet Cameras-no subscription） |
| robots.txt 修复 | ✅ Vercel 域名 308 死循环修复 + AdsBot 封禁 |
| GSC 抓取统计 + 链接报告审查 | ✅ 346 请求/90天 / 外部链接仅1条（数据延迟） |
| Reddit D33 首条链接 | ✅ r/CatAdvice 2猫除臭帖，回复存活 10min+ |

### 今日任务状态（6/24 周三）

| 任务 | 状态 |
|------|:--:|
| B #3 PETKIT vs Catit PIXI | ✅ 已有内容 + citation cue + verdict 优化 |
| 外链 Outreach | ✅ 3封guest post已发（PetPress/PetsAnalysis/AnimalPetsBlog） |
| GSC Top 6 页优化 | ✅ Petlibro 标题/描述 CTR 修复（55曝光→0点击） |
| Pinterest 实验 Pin #2 | ✅ pin74_exp2.jpg 已生成（3-Year TCO Cost角度） |
| Reddit | 🔴 首条链接24h后被移除，策略降级为纯价值回复不挂链接 |
| GSC Top 6 页优化（续） | ✅ No-Fee GPS/Aorkuler/WOPET Camera 标题问句改断言 |
| press@ 邮件配置 | ✅ Gmail SMTP 别名已生效 |

### 今日任务状态（6/25 周四）

| 任务 | 状态 |
|------|:--:|
| B #4 Best Stainless Steel Fountains | ✅ 已有内容 + citation cue + keyword 优化 |
| B #5 Large Cats Litter Box | ✅ 已有内容 + citation cue + breed keyword |
| Pinterest Pin #3 | ✅ pin75_exp3.jpg 已发布（避坑/健康角度 → Pet Water Fountains） |
| P1-5 Named author profile | ✅ Wikidata Q140290653 挂接全站 Schema + 名称统一为"Research Team" |
| Reddit | 🔴 暂停链接，只做纯价值 |

### 今日任务状态（6/26 周五）

| 任务 | 状态 |
|------|:--:|
| B #6 Traveling with Pets | ✅ 新写 6 节 + 4 FAQ，104→105 页 |
| A #7 Multi-Cat Litter Box | ✅ 新写（LR5/LR4/CATLINK/Elspet），105 页 |
| GEO P1-1 C级 citation cue | ✅ C #1+#2 描述已加 |
| GEO P1-3 指南 citation cue | ✅ 33 篇指南统一脚注 `Data sourced from Amazon.com, June 2026` |
| Pinterest Pin #4 | ✅ pin76_exp4.jpg 已生成（多猫/可靠性） |
| 外链 Outreach 第 2 轮 | 🔄 PetsAnalysis+AnimalPetsBlog 等回复 / USA TODAY lead |

### 今日任务状态（6/27 周六）

| 任务 | 状态 |
|------|:--:|
| Week 7 补提交推送 | ✅ 21 文件/1230 行，sitemap 102→104 |
| 每日收尾提交步骤 | ✅ 已加入 Week 8 排班表 |
| GSC 索引追踪 | ✅ 索引 14 / 12 重定向错误实为已修复 / sitemap 重提交 |
| GSC 12 URL Inspection | ✅ 逐个验证，全部已索引 |
| Pinterest 出站分析 | ✅ 1,990 浏览 / 0 出站点击 / 1 保存 / 6 受众 |
| GEO Schema 抽样 | ✅ 3/3 页通过（Petlibro/Multi-Cat/xpai），dateModified 全停在 6/3 |
| GEO Wikidata 验证 | ✅ Q140290653 存活，P31/P571/P407/P856 完整 |
| PAA 选题确认 | ✅ 5 个候选网络调研完成，内容丰富可写 |
| Amazon NR 扫描 | ⚪ 503 阻断，跳过 |
| 外链 Outreach 跟进 | 🔴 PetPress=$250 付费站 / PetsAnalysis+AnimalPetsBlog 3 天无回复 |
| 实验 Pin #5 | ✅ pin77_exp5 已发布（价格/价值角度，Automatic Cat Feeders） |

### 今日任务状态（6/28 周日）

| 任务 | 状态 |
|------|:--:|
| GSC 购物报告发现 | ✅ 产品摘要 1 有效 / 商家信息 1 有效 ⚠️缺退货政策+运费 / 评价摘要 2 有效 |
| 评价摘要深度分析 | ✅ 2 页被识别（首页+LR5），其余 24 篇缺 reviewRating + publisher 信息不全 |
| Review Schema 增强 | ✅ 加 reviewRating + url + 统一 author/publisher sameAs，26 篇评测页一次生效 |
| 构建验证 | ✅ 105 页 0 错误 |
| 线上验证 | ✅ Petlibro Granary 页 Review Schema 完整 |
| 提交推送 | ✅ `06c78ae` |
| GSC 抓取行为分析 | ✅ 3 个月 321 次 / 6/27 峰值 ~55 次（21 文件改动触发） / 平时 3.8/天 |
| Sitemap 经验调研 | ✅ Google 小站不会主动回读 / `lastmod` 必须真实 / `priority`+`changefreq` 被忽略 |
| 抓取策略三条 | ✅ ①每天 URL Inspection 5 个 ②每周一重提 sitemap ③新内容上线当天重提 |
| 经验复盘文件 | ✅ `lessons-learned.md` 创建，10 大类 62 条经验覆盖 Day 1-41 |

### 今日任务状态（6/30 周一 — Week 8 Day 1）

| 任务 | 状态 |
|------|:--:|
| PAA #1: Feeder Jamming 7 Fixes | ✅ 新写 7 节 + 4 FAQ，C 级 30min |
| PAA #2: Cat Litter Box Introduction | ✅ 新写 8 节 + 4 FAQ，C 级 45min |
| Petlibro Granary 加固 | ✅ 用户原话引语 8 条 + Petlibro/WOPET/PETKIT 对比 FAQ |
| GSC 周检 | ✅ 索引 14（冻结 4 周）/ HTTPS 0→10 / 路径 10→11 / 评价摘要仍 2 |
| Sitemap 重提交 | ✅ 周一例行，sitemap-0.xml 含 106 URL |
| GEO 存活检查 | ✅ llms.txt 200 / robots.txt 200 / Wikidata Q140290653 存活 |
| 口径一致性周检 | ✅ 6 条命中全部合理上下文 |
| GSC URL Inspection | ✅ 7 个优先 URL（2 新篇 + 5 优先页） |
| 实验 Pin #6 | ✅ pin78_exp6 已发布（使用场景/空间角度） |
| GA4 周检 | ✅ 6/29 完成（见 progress.md） |
| **Task A 变现基建** | ✅ 联盟审核 + 3 review 决策模块 + 2 guide CTA |
| **Brand Outreach D4-D7** | ✅ /for-brands/ 页面 + 审计模板 + CRM + 样本审计 |

### 今日任务状态（7/1 周三 — 接续周二）

| 任务 | 状态 |
|------|:--:|
| PAA #5：Cat Breaking Into Feeder | ✅ C 级 30min，112 页 |
| Robot #6：Best Robot Vacuum for Cat Litter | ✅ B 级 1h，品类测试 |
| GEO 月度复检 + llms-full.txt 更新 | ✅ 112 页 + 新内容覆盖 |
| GSC 索引追踪 | ✅ 仍 14 冻结，Sitemap 106→109 |
| No-Fee GPS + 用户原话 | ✅ whatOwnersSay 已加 |
| Aorkuler GPS + 用户原话 + 决策模块 | ✅ whatOwnersSay + buyIf/skipIf/bestAlt |
| Catit PIXI verdict 强化 | ✅ 结论更具体 |
| 首页 social proof 数字条 | ✅ 112页/26产品/85K+评论/6品类 |
| 实验 Pin #8 | ✅ pin80_exp8 已生成+发布 |
| GSC URL Inspection ×5 | ✅ 人工已提交 |
| Sprint D11 D3 跟进草稿 | ✅ 4 品牌，7/4 发送 |
| Sprint D12 度量日志 | ✅ weekly-metrics-log.md 创建 |
| Sitemap 重提交 | ✅ 7/1 两次重提 |

### ⚠️ 本周关注

| 事项 | 严重度 | 说明 |
|------|:--:|------|
| 索引冻结 | 🔴 | 14 已 5 周不动。Sitemap 已重提+内链已补，等 Google 响应 |
| 改动队列堆积 | 🟡 | Review Schema/PAA #1-#5/Robot #6/4 页加固都在等 Google 重抓 |
| Pin #8 已发 | 🟢 | 实验进度 8/12 |
| 外联 Wave 1 | 🟢 | 4/5 品牌已发，D3 跟进 7/4 |

| 任务 | 时间 | 说明 |
|------|:--:|------|
| **口径自检** | 2min | 新写/修改的任何对外文字，检查 hands-on/tested/we tested 残留 |
| **Pinterest 出站实验 Pin** | 10min | 每天 1 个带 UTM 的实验 Pin（价格/TCO/零订阅/可靠性/避坑型标题）。12 个做完前不发普通 Pin |
| **内容生产** | 90min | 仅围绕 4 个集群（不锈钢饮水机/零订阅摄像头GPS/喂食器可靠性/猫砂盆TCO）。A 级每周≤2 篇 / B 级 1-1.5h / C 级 30min |
| **FB + Reddit** | 10min | FB：浏览/点赞/纯帮助回复。Reddit：纯价值回复不挂链接，养到500+karma再尝试自然链接 |
| **GSC URL Inspection** | 5min | 每天手动提交 5 个优先 URL，直接入优先抓取队列。优先列表见下方 |

> **优先 URL 池**（周一刷新）：Petlibro Granary 评测 > Multi-Cat Best > Traveling Guides > No-Fee GPS 评测 > Aorkuler 评测 > WOPET Camera 评测 > Catit PIXI 对比 > Stainless Steel Best > Large Cats Best > LR5 评测

---

## 📅 每周（~5.5h）

| 任务 | 时间 | 频次 | 说明 |
|------|:--:|:--:|------|
| **Sitemap 重提交** | 2min | 每周 1 次（周一） | 手动重提 sitemap-index.xml。小站 Google 不会主动回读，必须手动催。新内容上线当天也重提一次 |

| 任务 | 时间 | 频次 | 说明 |
|------|:--:|:--:|------|
| **外链 Outreach** | 2-3h | 每周 1 次（固定，不可挤占） | Qwoted 2-3 pitch + 资源页 outreach + 品牌补充资料。目标：每周 +2-5 可验证外链 |
| **GSC 索引追踪** | 15min | 每周 2 次（周三+周六） | 核心 KPI：索引页数（目标 14→30→60）+ 索引率。索引<20 时暂停大规模扩页 |
| **GSC 曝光 Top 6 页优化** | 20min | 每周 1 次（周三） | Petlibro Granary / Catit PIXI / 首页 / Aorkuler GPS / No-Fee GPS / WOPET Camera — 补 verdict + 数据脚注 + 内链 |
| **Pinterest 出站分析** | 10min | 每周 1 次（周六） | KPI 从 Pin 浏览切换为 **outbound click rate + save rate + 每个 Board 的链接点击** |
| **GA4 数据净化** | 10min | 每周 1 次（周一） | 检查 source/medium 报告，确认自测流量已过滤。看 affiliate_click + outbound_click 事件是否正常上报 |
| **Google PAA 选题挖掘** | 30min | 每周 1 次（周六） | 搜 3-4 个核心词看 PAA + Reddit 问题帖，产出 3-5 个 C 级候选 |
| **Amazon NR 扫描** | 10min | 每周 1 次（周六） | 仅监不追，触发条件极罕见（BSR<10K + 评论<100） |
| **GEO 存活检查** | 5min | 每周 1 次（周一） | 验证 llms.txt + llms-full.txt 200；robots.txt AI bot 白名单完整；Wikidata Q140290653 存活 |
| **GSC 设置报告巡检** | 10min | 每周 1 次（周一） | robots.txt 报告（0 错误）+ 抓取统计信息（301/404 占比<10% + 平均响应<200ms + AdsBot 零请求） |
| **口径一致性周检** | 5min | 每周 1 次（周一） | Grep 全站 `hands-on|tested|testing` 确认零残留；抽查 pin-plan.md / backlinks/ 素材无旧口径 |

---

## 🟢 每月（~3h）

| 任务 | 时间 | 说明 |
|------|:--:|------|
| **GSC 深度分析** | 30min | 每月 1 号。导出查询词报告，对比上月，找出曝光增长最快的页面和新增查询词 |
| **Pinterest 月度分析** | 15min | 按月趋势：出站点击率变化、保存率、Board 排名 |
| **Semrush KD 复查** | 30min | 每月 1 次。免费版 10 次查询。重点关注哪些词的 KD 在下降 |
| **选题池更新** | 30min | 汇总 Amazon NR + Reddit 高频问题 + Semrush 低 KD 词，只围绕 4 个集群扩展 |
| **外链进度回顾** | 15min | 本月新增外链数、引用域名数。目标：每月 +10-20 外链 |
| **GEO 月度复检** | 30min | 每月 1 号。跑 geo-audit 重新打分（目标 +3-5/月）；更新 llms-full.txt；Schema 抽查 5 页 |
| **信任一致性审计** | 15min | 每月 1 号。隐私页 vs GA4 实际追踪是否一致；外链平台描述 vs 站内 How We Research 是否一致 |

---

## 🔵 新文章发布后（~7min）

| 任务 | 说明 |
|------|------|
| **GSC 请求索引** | URL Inspection → Request Indexing |
| **Sitemap 重提交** | 新内容上线当天重提 sitemap-index.xml（URL 数量变化触发 Google 峰值抓取） |
| **内部链接检查** | 新文章是否被分类索引页 + 已有 Top 页面引用 |
| **CTA + 数据脚注** | 确认有 verdict/conclusion + 数据来源标注 + affiliate 披露 |
| **Pinterest 排期** | 仅当文章属于 4 个集群时才做 Pin，否则跳过 |

---

## 🚫 已取消/暂停

| 事项 | 状态 | 理由 |
|------|:--:|------|
| 死目录提交（Manta/Hotfrog/AllTop 等） | ❌ 取消 | 免费目录大多已死，ROI 近零 |
| 无反馈大词 Best 列表新建 | ❌ 取消 | 已有 9 篇够用，等 DA>10 或索引>50 |
| 无出站验证 Pin 批量铺量 | 🟡 暂停 | 先 12 个实验 Pin 验证通路 |
| 机器人吸尘器品类扩张 | 🟡 仅保留 3 篇测试 | 3 个月看 GSC 数据再决定 |
| Medium 追加文章 | ❌ 取消 | 3 篇 canonical 足够，ROI 递减 |
| hands-on/tested 口径 | ❌ 已全站清零 | 每周 Grep 自检 |

---

## 🔴 本周任务（6/23-6/27）

### 紧急行动

| # | 任务 | 类型 | 耗时 | 状态 |
|:--:|------|:--:|:--:|:--:|
| P0-1 | 隐私页 GA4 披露修正 | 合规 | ✅ | 6/23 完成 |
| P0-2 | 外部素材口径统一（backlinks/ + pins/） | 合规 | ✅ | 6/23 完成 |
| P1-1 | **GA4 基础看板**：source/medium + landing_page + affiliate_click + outbound_click + self-traffic exclusion | 数据治理 | 30min | ✅ 全部完成 |
| P1-2 | **GSC 曝光 Top 6 页轻优化**：补 verdict + 数据脚注 + 内链 | 索引加速 | 45min | ✅ 4/6完成（Petlibro+No-Fee/Aorkuler/WOPET） |
| P1-3 | **Pinterest 12 个出站实验 Pin**：价格/TCO/零订阅/可靠性/避坑型标题，全部带 UTM | 社交验证 | 分 3 天 | 🔄 4/12 完成 |
| P1-4 | **外链 Outreach 2 轮**：Qwoted 2-3 pitch + 资源页 outreach | 外链权威 | 2×2.5h | 🔄 第1轮：PetPress🔴付费站 / 第2轮：等2家回复+USA TODAY lead |
| P1-5 | **创建 named author profile**：EEAT 增强，Schema sameAs 挂接 | EEAT | 30min | ✅ Wikidata Q140290653 挂接全站 Schema |

### GEO 任务

| # | 任务 | 耗时 | 状态 |
|:--:|------|:--:|:--:|
| GEO-P0-1 | llms.txt 内容更新（计数修正 + URL 加尾斜杠） | — | ✅ 6/22 完成 |
| GEO-P0-2 | llms-full.txt 增强（品类覆盖详情 + 最新日期 + 方法论） | — | ✅ 6/22 完成 |
| GEO-P0-3 | **Wikidata Q140290653 属性补全**（official website / inception 2026-05-19 / description / language） | 15min | ✅ 4属性全部已存在 |
| GEO-P1-1 | 7 篇新文章全部加 citation cue（Data sourced from Amazon.com, June 2026） | 持续 | ✅ C #1+#2 描述已加 / Best 系列自带 |
| GEO-P1-2 | 新文章全部加 verdict 段落（C 级 2-3 句，B/A 级完整 verdict） | 持续 | ✅ Best 列表自带 verdict + 评测页自带 |
| GEO-P1-3 | 指南页 citation cue 分批补，本周目标 ~10 篇 | 持续 | ✅ 33 篇指南底部统一加引用脚注 |
| GEO-P1-4 | Schema 抽样验证（周日，Rich Results Test 2-3 页） | 10min | ⏳ |
| GEO-P1-5 | Wikidata Q140290653 存活验证（7/1 前确认未被删除/合并） | 5min | ⏳ |

### Week 7 选题（7 篇，~6h）

> 选题优先级：GSC 直驱 > Pinterest 已验证角度 > 站点内容缺口 > 新场景探索

| # | 标题 | 类型 | KD | 工时 | 选题理由 | 状态 |
|---|------|:--:|:--:|:--:|------|:--:|
| 1 | **5 Best No-Subscription Pet Cameras (2026)** | C | 12-18 | 30min | No Subscription 已验证 + 摄像头集群内链 | ✅ 6/22 |
| 2 | **Smart Home for Pets: Alexa & Google Home Compatible Devices** | C | 8-12 | 45min | 站点 0 覆盖，真正内容缺口，GEO 友好 | ✅ 6/22 |
| 3 | **PETKIT Eversweet vs Catit PIXI — Which Smart Fountain Wins?** | B | 20-25 | 1h | GSC 直驱："catit pixi" 在 Top 查询词 | ✅ 6/24 |
| 4 | **Best Stainless Steel Cat Water Fountains (2026)** | B | 18-22 | 1h | Pinterest 已验证：不锈钢 139 浏览 | ✅ 6/25 |
| 5 | **Best Automatic Litter Box for Large Cats — Maine Coon Guide** | B | 22-28 | 1.5h | Pinterest 已验证：大猫 75 浏览 + 独立评测内容稀缺 | ✅ 6/25 |
| 6 | **Traveling with Pets? Smart Tech You Actually Need** | B | 12-18 | 1h | 场景缺口，清单格式 GEO 友好 | ✅ 6/26 |
| 7 | **Best Automatic Litter Box for Multiple Cats — LR4 vs CS106 vs CATLINK** | A | 30-40 | 2h | 多猫场景大缺口，支柱内容，积累权威 | ✅ 6/26 |

### 每日排班

| 日 | 内容 | 分发/验证 | 总工时 |
|:--:|------|------|:--:|
| 周二 6/23 | C #1+#2 ✅ | GA4 看板 + Wikidata 验证 + GSC 索引请求 + 口径周检 | ~1.5h |
| 周三 6/24 | B #3 PETKIT vs Catit PIXI | 🔴 **外链 Outreach 2-3h** + Pinterest 出站实验 Pin ×2 | ~3.5h |
| 周四 6/25 | B #4 Best Stainless Steel Fountains | 🔴 GSC 索引追踪 + 曝光 Top 6 页轻优化 + 口径一致性 Grep | ~2h |
| 周五 6/26 | B #5 Large Cats Litter Box + B #6 Traveling with Pets | 🔴 Pinterest 出站实验 Pin ×2 + named author profile 创建 | ~2.5h |
| 周六 6/27 | A #7 Multi-Cat Litter Box | 🔴 外链 Outreach 第 2 轮 + Amazon NR 扫描 + Pinterest 出站分析 + 下周选题 | ~3.5h |

---

## 📊 数据看板

| 指标 | 当前 (7/1) | 30 天目标 | 审计评分 |
|------|:--:|:--:|:--:|
| 页面数 | 112 | 115-120 | A- |
| GSC 索引 | 14 | 30+ | C |
| GSC 点击 | 4 | 20 | C |
| Pinterest 出站点击 | 0 | >5 | C- |
| 引用域名 | 11 | 18+ | C |
| GA4 affiliate_click | 0 | 有数据 | C+ |
| GEO Score | 70 | 75+ | B+ |
| Wikidata | Q140290653 | 补全属性 | B |
| 口径一致性 | ✅ | 零残留 | — |

### 每日时间预算

```
周二至周六：~2-3h/天
    2min  口径自检（hands-on/tested 零容忍）
   10min  Pinterest 出站实验 Pin ×1（12 个做完前不发普通 Pin）
   10min  FB + Reddit 养号
   60-120min 内容生产（仅围绕 4 个集群，含 verdict + 数据脚注）
    5min  新文章后 GSC 索引请求
   
周三额外：GSC 索引追踪 + 曝光 Top 页轻优化 (+30min)
周六额外：Amazon NR 扫描 + Pinterest 出站分析 + 外链 Outreach (+3h)
```

---

## ⏭️ Week 8（6/30-7/4）

### 1. 内容与选题（Content, 5.5h）

> 引擎：Google PAA 主力 + Reddit 辅助 + NR 仅监不追

| # | 标题 | KD | 级别 | 工时 | 选题来源 |
|---|------|:--:|:--:|:--:|------|
| 1 | How to Stop Your Automatic Feeder From Jamming (7 Fixes) | <5 | C | 30min | PAA |
| 2 | How to Introduce Cat to Automatic Litter Box | <5 | C | 45min | PAA |
| 3 | Cat Won't Drink From Water Fountain? 8 Reasons & Fixes | <5 | C | 30min | PAA |
| 4 | Why Does My Automatic Feeder Keep Disconnecting from WiFi? | <5 | C | 30min | Reddit |
| 5 | How to Keep Your Cat From Breaking Into the Automatic Feeder | <5 | C | 30min | Reddit | ✅ 7/1 |
| 6 | Best Robot Vacuum for Cat Litter Tracking (2026) | 15-25 | B | 1h | 品类测试 | ✅ 7/1 |
| 7 | Best Robot Vacuum for Golden Retriever Shedding | 10-15 | B | 1h | 品类测试 |
| 8 | Robot Vacuum vs Stick Vacuum for Pet Hair | 15-20 | B | 1h | 品类测试 |

> 机器人吸尘器测试标准：3 个月后任意 1 篇 > 50 曝光 → 继续；全部 < 50 → 搁置等 DA>10。

---

### 2. 页面优化（On-Page, 3h）

> 已索引 14 页中，GSC 曝光最高的 5 个做深度加固。目标：提高现有页面的 EEAT 信号和用户行为指标，促使 Google 增加抓取预算。

| # | 页面 | 曝光 | 加固动作 | 工时 |
|:--:|------|:--:|------|:--:|
| 1 | Petlibro Granary 评测 | 55 | 加"真实用户原话"正反引用 + 对比表 | 45min | ✅ 6/30 |
| 2 | Catit PIXI 对比 | 39 | verdict 强化 + 内链→饮水机评测 | 30min | ✅ 7/1 |
| 3 | 首页 | 37 | 加最新研究区块 + social proof 数字 | 30min | ✅ 7/1 |
| 4 | No-Fee GPS 评测 | 29 | 加"真实用户原话" + Tractive/Aorkuler 对比表 | 45min | ✅ 7/1 |
| 5 | Aorkuler GPS 评测 | 29 | 加使用场景章节 + 内链→对比文 | 30min | ✅ 7/1 |

---

### 3. 内链体系（Internal Linking, 1h）

> 上一次全站内链重构是 6/22（~100 条跨类型链接）。本周目标：从 14 个已索引页面出发，给新页面补入站链接。

| # | 动作 | 工时 |
|:--:|------|:--:|
| 1 | 14 索引页各加 Related Resources → 本周 8 新篇 + A #7 | 30min |
| 2 | 评测模板 "Explore More" → 补 3 个高价值指南链接 | 15min |
| 3 | 饮水机↔猫砂盆↔喂食器↔摄像头 Best 列表互相链接 | 15min |

---

### 4. 外链建设（Off-Page, 2h）

| # | 动作 | 工时 |
|:--:|------|:--:|
| 1 | PetsAnalysis + AnimalPetsBlog 跟进（1 周未回复→搜新目标） | 30min |
| 2 | 第 3 轮 outreach：搜 5 个新目标，排除公开标价站 | 1h |
| 3 | 起草 + 发送 pitch 邮件 | 30min |

---

### 5. 技术 SEO（Technical, 30min）

| # | 动作 | 工时 |
|:--:|------|:--:|
| 1 | 本周 8 新篇 + 5 个强化页重新提交 GSC 优先抓取 | 15min |
| 2 | robots.txt / sitemap / canonical 抽样验证 | 10min |
| 3 | Schema 抽样验证（GEO P1-4，Rich Results Test 2-3 页） | 10min |

---

### 6. 社交与分发（Social & Distribution, 1.5h）

| 任务 | 频次 | 说明 |
|------|:--:|------|
| Pinterest 实验 Pin #5-8 | 每天 1 个 | 4/12→8/12，角度：可靠性/价格/避坑/使用场景 |
| Reddit 纯价值回复 | 每天 5min | 不挂链接，养 karma |

---

### 7. GEO 优化（1h + 增量修复 2-3h）

| # | 动作 | 工时 | 说明 |
|:--:|------|:--:|------|
| 1 | **7/1 月度 GEO 复检**（geo-audit 重打分） | 20min | 目标从 70→75+ |
| 2 | llms-full.txt 更新 | 15min | 105→113 页 + 新增机器人吸尘器品类 |
| 3 | Wikidata Q140290653 存活验证（P1-5） | 5min | 确认未被删除/合并 |
| 4 | 新文章 citation cue（P1-1） | 持续 | 8 篇新文章描述加 `Data sourced from Amazon.com, June 2026` |
| 5 | Schema 抽样验证（P1-4） | 10min | Rich Results Test 抽查 2-3 页 |

### 7.1 Codex GEO 增量审计修复（6/27 新增，Claude 执行）

> 来源：Codex 2026-06-27 AI 可见性 / GEO 增量审计。目标不是重做基础 GEO，而是补齐 compare / best / guide / stats 的可引用性、结构化语义和作者实体。

| # | 优先级 | 任务 | 范围 | 验收标准 |
|:--:|:--:|------|------|------|
| GEO-P1-6 | P1 | Compare 模板加来源/日期脚注 | `src/pages/compare/[slug].astro` | `dist/compare/litter-robot-5-vs-litter-robot-4/index.html` 可见 `Data sourced` 或同等来源日期说明 |
| GEO-P1-7 | P1 | Best 模板加来源/价格日期说明 | `src/pages/best/[slug].astro` | `dist/best/automatic-cat-feeders/index.html` 可见来源、价格波动、更新时间说明 |
| GEO-P1-8 | P1 | Guide 顶部加 `Quick answer` / `Bottom line` | `src/pages/guides/[slug].astro` | `dist/guides/how-to-clean-cat-water-fountain/index.html` H1 后有 2-3 句可摘取结论 |
| GEO-P2-6 | P2 | 步骤型 Guide 增加 `HowTo` Schema | 清洁、维护、安装类 guides | 清洁饮水机样本页 JSON-LD 出现 `HowTo` |
| GEO-P2-7 | P2 | Stats 页增加 `Dataset` JSON-LD | `src/pages/pet-tech-statistics.astro` | 页面 JSON-LD 包含 `Dataset`，保留现有 `Article` |
| GEO-P2-8 | P2 | 建真正的 named author profile | `/about` 或 `/authors/...` | 至少 1 个个人作者页，并能被 Article author 引用 |
| GEO-DOC-1 | P2 | 同步 6/27 Codex 增量审计摘要 | `GEO-AUDIT-REPORT.md` | 项目内 canonical GEO 报告记录 86/100 新基线与新增修复项 |

---

### 8. 数据与监控（Analytics, 1h）

| 任务 | 频次 | 说明 |
|------|:--:|------|
| GSC/Pinterest/GA4 周检 | 周一 | 索引变化 + 出站点击 + GA4 事件 |
| 口径一致性自检 | 每天 2min | Grep `hands-on\|tested` |
| NR 扫描 | 周六 | 仅监不追 |
| Pinterest 出站分析 | 周五 | 4 实验 Pin 对比出站点击率 |

---

### 每日排班

| 日 | 上午（内容） | 下午（分发） |
|:--:|------|------|
| **周一** | PAA #1+#2 | 主力页 Petlibro + GSC 提交 + 周检 |
| **周二** | PAA #3+#4 | 内链补全 + Pin #5 |
| **周三** | PAA #5 + Robot #6 | GEO 月度复检 + llms-full.txt 更新 + GEO-P1-6/7 模板来源脚注 + 主力页 Catit/首页/No-Fee/Aorkuler + Pin #6 |
| **周四** | Robot #7+#8 | GEO-P1-8 Guide 顶部 Quick answer + 外链第 3 轮 + Pin #7 |
| **周五** | — | GEO-P2-6/7/8 结构化与作者页收尾 + GEO-DOC-1 审计报告同步 + 外链跟进 + NR + Pin #8 + 周复盘 + 下周 PAA |
| **每日** | GSC URL Inspection（5 个优先 URL） | 实验 Pin + Reddit 5min + `git add -A && commit && push` |

> ⚠️ **每日收尾提交**：每天工作结束前必须 commit + push。内容写完不推送 = Google 看不到 = 白写。
> 🔍 **每日 URL Inspection**：每天手动提交 5 个优先 URL，把有限抓取定向到最有价值的页面。周一顺便重提 sitemap。

---

### Week 8 成功标准

| 指标 | 当前 | 目标 | 判定 |
|------|:--:|:--:|------|
| GSC 索引 | 14 | **20+** | 🔴 主力 KPI |
| Pinterest 出站点击 | 0 | 1+ | 必须破 0 |
| 引用域名 | 11 | 15+ | 外链发力 |
| GEO Score | 70 | 75+ | 品牌权威 |
| 实验 Pin | 4/12 | 8/12 | 持续验证 |
| GA4 affiliate_click | ? | 有数据 | 看板已建

---

## 📈 触发条件（什么时候调整节奏）

| 触发条件 | 调整方向 |
|------|------|
| **Pinterest 出站点击 > 5/周** | 出站实验 Pin 12→常态化，恢复每日 1-2 Pin 发布 |
| **索引 > 30 页** | GSC 曝光 Top 页优化升级为每周 2 次 |
| **月自然点击 > 100** | GSC 检查升级为每周 3 次，开始做查询词驱动更新 |
| **GA4 过滤后月活 > 100** | 开始做 source/medium + landing page 归因分析 |
| **Authority Score > 5** | 可以开始做 KD 20-30 的对比文 |
| **月佣金 > $50** | 复盘哪些文章在产生收入，多写同类内容 |
| **月流量 > 1,000 PV** | 注册 GA4 增强型电商追踪 |
| **GEO Score > 80** | GEO 月度复检降为季度 |
| **任一集群月曝光 > 500** | 围绕该集群做 hub page + 对比页 + FAQ 页 + Pinterest 系列 |
| **索引 < 30 持续 4 周** | 暂停大规模扩页，70% 时间转内链+外链+重写 |
| **Pinterest 出站=0 持续 4 周** | 重新设计 Pin 策略（标题/CTA/图片/Board 结构） |

---

## 📋 项目基础信息

### 技术栈
- **域名**：https://smartpetguide.net
- **框架**：Astro 5 + Tailwind CSS v3，纯静态
- **部署**：Vercel（`vercel.com/muchengxian-labs-projects/smartpetguide`），GitHub push 自动部署
- **数据源**：`src/data/products.json`（26 款产品，6 品类）
- **设计系统**：Forest + Honey 编辑杂志风（Fraunces + Atkinson Hyperlegible）

### 选品原则
1. 关键词先行：Amazon 搜索建议 + Google Trends 双平台验证
2. BSR 验证：只推 Amazon BSR < 50,000 的产品
3. 评分过滤：只推 ≥ 3.8 星的产品
4. 竞争评估：优先做 Google 首页有小站/Reddit 结果的关键词
5. Trends 验证：Google Trends 热度 > 3 才投入，0 = 不投入
6. 平台区分：Amazon 搜索词 ≠ Google 搜索词，选品需双平台验证

### 4 个内容集群（VOC 验证 + 市场确认）

| 集群 | 核心角度 | 验证来源 |
|------|------|------|
| **A: Stainless Steel Cat Fountain Hub** | 卫生/猫下巴痤疮/清洁难度/材质安全 | Trends 23 + Reddit 共识 + Amazon 好评 |
| **B: No Subscription Camera/GPS TCO Hub** | 3 年真实成本对比，零订阅替代方案 | VOC #1 痛点（订阅费愤怒）+ Semrush KD 15 |
| **C: Automatic Feeder Reliability Hub** | 断网是否仍出粮/卡粮/App 稳定性 | VOC #1 购买门槛（可靠性 > 一切） |
| **D: Litter Box Worth-It/3-Year Cost Hub** | $699→每月成本拆解，多猫家庭 TCO | Reddit 最高频帖子类型 + 转化杠杆 |

### 内容结构（103 页）

| 类型 | 数量 | 说明 |
|------|:--:|------|
| 评测（Reviews） | 26 | 猫砂盆×7 / 喂食器×4 / 饮水机×6 / 摄像头×6 / GPS×3 |
| 对比（Compare） | 15 | 猫砂盆×5 / 喂食器×2 / 饮水机×2 / 摄像头×3 / GPS×1 / 跨品类×2 |
| Best 列表 | 9 | 全品类覆盖 + 细分专题 |
| 指南（Guides） | 33 | 购买/场景/保养/长尾/份量/滤芯/入门/湿粮/公寓/成本/新手/智能家居等 |
| 品种（Breed） | 7 | 法斗/金毛/拉布拉多/德牧/多猫/老猫/小狗 |
| 信息页 | 13 | 首页/about/privacy/affiliate/how-we-research/不推荐/pet-tech-statistics/分类索引×5/404 |

### 里程碑

| 里程碑 | 内容数 | 状态 |
|--------|--------|:--:|
| M1: 基础上线 | 19 | ✅ Day 1 |
| M2: 变现激活 | 19 | ✅ Day 3 |
| M3: 30篇+架构完善 | 33 | ✅ Day 3 |
| M4: 关键词驱动38篇 | 38 | ✅ Day 3 |
| M5: 对比+品种43篇 | 43 | ✅ Day 4 |
| M6: GEO+Schema优化 | 43 | ✅ Day 4 |
| M7: 70篇+社交三线 | 70 | ✅ Day 4 |
| M8: 规模化 | 150+ | ⏳ Month 2-3 |
| M9: 广告变现 | 200+ | ⏳ Month 4-6 |

### 90 天目标（到 2026-09-15）

| 指标 | 当前 | 目标 |
|------|:--:|:--:|
| 页面数 | 112 | 150-180 |
| GSC 索引 | 14 | 60-100 |
| 引用域名 | 11 | 25-40 |
| Pin | 79 | 150-220 |
| 月自然点击 | 3 | 100-500 |
| **GEO Score** | **70** | **85+** |

### 新文章 EEAT SOP

| 元素 | 位置 | 格式 |
|------|------|------|
| 作者署名 | 文章底部 | Written by the SmartPetGuide research team |
| 更新日期 | 文章顶部 | Updated: Month DD, 2026 |
| 数据来源 | 评测页 CTA 区域 | Data sourced from Amazon.com as of [Month] 2026 |
| 联盟披露 | CTA 按钮下方 | As an Amazon Associate, we earn from qualifying purchases |

### 每篇新文章 GEO checklist
- [ ] 数据来源标注：`Data sourced from Amazon.com, [Month] 2026`
- [ ] 评测/指南有独立 verdict/conclusion 句
- [ ] Citation cue 已加

---

## 📚 历史阶段（只读归档）

### 阶段 1：基础设施搭建 ✅ Day 1 (5/19)
- 域名 smartpetguide.net + Vercel 部署 + GA4/GSC
- Astro 5 + Tailwind CSS v3 搭建
- 产品数据库 products.json（15 款产品）
- 首批 19 页内容发布 + Amazon Associates 提交

### 阶段 2：内容冲刺 + 变现激活 ✅ Day 3 (5/21)
- 喂食器 Best + 评测 + 指南 + 猫砂盆补齐
- WOPET vs Petlibro 对比 + AA 审核通过 + GSC Sitemap 提交
- Forest + Honey 编辑杂志风全站重设计

### 阶段 3：饮水机 + 摄像头品类拓展 ✅ Day 3 (5/21)
- 饮水机/摄像头 Best + 评测 + 对比 + 指南
- 404 修复 + 24 假 ASIN 替换 + 产品配图 18/18 Amazon 高清
- 架构重构：products.json 为唯一数据源

### 阶段 4：关键词驱动内容冲刺 ✅ Day 3-4 (5/21-22)
- P0：GPS 无月费 + 摄像头无订阅 + Petlibro 评测增强
- P1：大猫猫砂盆 + 不锈钢饮水机 + 2猫喂食器
- 产品清理：18→24 款，累计 38→43 页

### 阶段 5：对比文 + 品种拓展 ✅ Day 4 (5/22)
- LR4 vs PetSafe ScoopFree / Furbo vs eufy 对比
- Golden Retriever / Multiple Cats 品种专题
- GPS 购买指南 + Pinterest 首批 5 张 Pin

### 阶段 6：数据分析 + 策略重整 ✅ Day 7-9 (5/25-27)
- 良辰美案例分析 → 策略调整：恢复生产 + 内容分级 A20/B50/C30
- 生财有术案例对照 → KD<20 优先 + 外链从 1%→20%
- Amazon New Releases 扫描 + Amazon Basics 新品抢发

### 阶段 7：GEO + Schema + AI 搜索优化 ✅ Day 4-6 (5/22-23)
- Article/Review/FAQPage/BreadcrumbList Schema 全覆盖
- robots.txt AI 爬虫白名单 6 bot + 66 H2 问题式标题 + 22 dfn 标签
- Medium 3 篇 canonical + Rich Results 验证 6/6 通过

### 阶段 8：社交引流三线并进 ✅ Day 5 (5/22)
- Pinterest 5 Board + 41 Pin 计划 + 第1-2轮发布
- Facebook 8 群组入群 + Reddit 新号养号
- 策略确定：Pinterest 提频 + FB Groups + Reddit 养号

### 阶段 9-10：CTA 补齐 + Skills 优化 + 外链获取 ✅ Day 6 (5/24)
- 评测/对比/Best 三模板底部 CTA + Awin 注册
- 14→21 Skills + GitHub/PH/IH/CatSite 外链上线
- 技术优化：canonical 修复 + 内链审计 + 图片性能

### 阶段 11：生财有术经验驱动策略调整 ✅ Day 9 (5/27)
- 资源重新分配：内容 75% / 外链 20% / 技术 5%
- 外链建设 4 周计划 + KD<20 选题策略
- Semrush 实测：KD 55→12 分布，最佳 ROI 词确认

### 阶段 12：EEAT 审计 + 81 页策略拐点 ✅ Day 11 (5/29)
- 全站 60+ 处 tested→research-backed 措辞统一
- 作者署名 + 数据来源标注 + 邮箱修正
- 新文章 EEAT SOP：署名/日期/来源/披露 Day 1 就带

### 阶段 13：第三方审计整改 ✅ Day 14-16 (6/2-6/5)
- P0：8 坏链修复 + 信任声明 + 移动导航
- P1：Schema 日期 + FAQ HTML + OG 图片 + Review Schema
- How We Research 页 + 不推荐产品页 + 3 篇评测增强

### 阶段 14：满月审计 + 策略转向（6/22-6/23）
- 核心诊断：第一个月是"资产与索引种子月"，内容/技术/GEO 超前，索引/外链/社交出站仍在冷启动早期
- 策略转向：生产驱动 → 分发与验证驱动
- 内容方向从全品类铺开 → 4 个集群深耕
- P0 修复：隐私页 GA4 披露 + 外部素材口径统一 ✅
- 任务体系全面重构（日常/每周/每月 + 触发条件 + 数据看板）

---

*后续任务管理统一在本文件维护，不再分散到 dashboard.md。每次会话开工读此文件顶部活跃任务区，收工更新任务状态。*
*progress.md 继续作为会话日志单独维护。findings.md 继续作为研究/决策记录单独维护。*
