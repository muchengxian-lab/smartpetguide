# 发现与决策

## Pretty Happy Pets 最终交稿状态（2026-07-16）

**事实**：首个已接受的 Guest Post 已在承诺的 7/17 截止日前完成交付。2026-07-16 使用原邮件线程回复，附 PDF，并提供 Google Docs 链接；最终稿约 2,099 词，含 FAQ、可核查来源与 Author bio。

**口径**：当前状态是 `Draft submitted / awaiting editorial and veterinary review`，不是 `Published` 或 `Backlink won`。只有收到采用确认且文章实际发布、作者链接上线后，才计为 guest post placement / referring domain 结果。

**下一步**：等待编辑修改意见、兽医审核或发布时间。未收到反馈前不重复发送稿件；后续跟进只围绕是否需要修改及预计发布节奏，不要求 reciprocal/dofollow 链接。

## TCO 跨页口径不一致（2026-07-16）

**发现**：`pet-tech-statistics` 相机类别 3-Year Cost 范围 $43–$370，但 `smart-pet-devices-subscription-cost` 指南中订阅型相机 3 年成本为 $395（Furbo 360）和 $465（Petcube Bites 2），均超出 stats 表上限。

**原因**：stats 表保留了较早的相机 TCO 上限，而新增方法学脚注明确包含适用的订阅费；因此不能继续把 `$370` 解释为不同口径。

**处置**：2026-07-16 收工验收时立即修正。stats 相机范围更新为 `$43–$465`，与订阅指南中的最高值 Petcube Bites 2 `$464.64` 按整美元展示一致；页面可见更新时间和引用日期同时统一为 2026-07-16。

## Editorial Outreach Round 4 目标复核（2026-07-16）

**核验结果**：BarkyTech、Purely Wholesome、The Upper Pawside、PetsAnalysis 均有可公开核查的投稿规则与联系方式。原 #2 iTechPet 只能访问到机器人验证页，公开搜索无法支持“接受投稿 / admin 邮箱 / 严格编辑政策”等记录，因此不能计入 5 个合格目标。

**替换决定**：以 **GlobalPETS / PETS International** 替换 iTechPet。该媒体当前仍更新，公开覆盖 smart pet devices 与消费者趋势，May 2026 杂志 masthead 列出编辑邮箱 `content@pets.nl`；pitch 改为面向行业读者的订阅疲劳与 3 年成本数据分析。

**状态口径**：Round 4 五个目标均为 `Researched — not sent`，不是 `Drafted` 或 `Sent`。只有形成完整邮件草稿后才可标 Drafted，人工实际发送后才标 Sent。

## 第三方审计整改计划（2026-06-02）

审计来源：`Codex/2026-06-02/smartpetguide-ai-report-generator` 项目审查报告第4节
审计范围：仅公开页面（Product Hunt + smartpetguide.net），未做代码/站点内部审计

### P0-1：Product Hunt 页面措辞与站内矛盾 🔴

**问题**：PH 页面写 "70+ hands-on reviews" / "tested every product with real pets"，但站内已在 Day 11 EEAT 审计中全部改为 "research-backed" / "analyzed by reviewing verified owner data"。两个地方的承诺不一致，如果 Google 或用户交叉验证会发现矛盾。

**整改**：
- [ ] 立即更新 Product Hunt 页面描述，与站内一致：改为 "research-backed reviews" / "analyzed from verified Amazon owner data"
- [ ] 检查 Indie Hackers / Crunchbase / Hotfrog 等其他外链平台的描述是否也有 "hands-on" / "tested" 措辞

**时间**：30 分钟

---

### P0-2：信任证据墙缺失 🔴

**问题**：审计指出每篇评测没有实测照片、视频、测试日期、评分维度。用户会将其视为普通 affiliate 站而非可信评测源。

**我们做不到的**（诚实面对）：
- 没有真实产品，无法拍摄实测照片/视频
- 审计要求的"test with real pets"在当前阶段不可行

**我们能做的**：
- [ ] **新建 "How We Research" 公开页**（替代当前的 About 页 methodology 段落）
  - 明确说明：我们通过分析 Amazon 已验证购买者评论（verified purchase reviews）、BSR 排名趋势、制造商规格对比来做评测
  - 说明为什么用这个方式：聚合 500+ 条真实用户反馈 > 单人单次测试
  - 透明写出：我们不买产品做物理测试，但我们读每条 verified review
- [ ] **评测页底部数据来源强化**：当前有 "Data sourced from Amazon.com"，扩展为具体数据点（review count / BSR / avg rating / 数据采集日期）
- [ ] **建一个"不推荐"页面**：列出我们评估后不推荐的产品及原因（比推荐列表更能建立信任）
- [ ] **选 3-5 篇核心评测**（LR4/Petlibro/Pioneer Pet），增加"What 500+ Owners Actually Say"板块，引用 Amazon verified review 中的真实用户原话

**时间**：How We Research 页 2h + 不推荐页 1h + 核心评测增强 3h = 6h

---

### P1-1：Affiliate 披露不够显眼 🟡

**问题**：有独立的 affiliate-disclosure 页面，但不是每篇文章顶部/购买按钮旁都标注。

**整改**：
- [ ] **CTA 按钮下方统一加注**：已有（"As an Amazon Associate, we earn from qualifying purchases"），确认全部 84 页覆盖
- [ ] **评测页顶部加一行小字**："💡 How we review: We analyze verified owner reviews and product specs — [learn more](/about)"，同时起到披露+信任+内链三作用
- [ ] **对比页/ Best 列表同理**

**时间**：1h（模板改 4 个文件，全站自动同步）

---

### P1-2：邮件订阅缺失 🟡

**问题**：没有任何方式把一次性 SEO 流量转化为可复访用户。

**整改**：
- [ ] **Footer 加 ConvertKit/Buttondown 订阅表单**（免费 tier 足够，< 1000 subscribers 不花钱）
  - 文案："Get the latest smart pet device picks — no spam, just the good stuff"
  - 放在 footer CTA 区域，全站自动出现
- [ ] **创建欢迎邮件序列**（2-3 封）：Welcome → Best Starter Devices → When to Upgrade
- [ ] **在 3 篇高流量潜力文章底部加内容升级**（checklist/PDF → 换邮箱）

**时间**：注册+嵌入 1h + 邮件序列 2h = 3h

---

### P1-3：医疗/健康建议免责 🟡

**问题**：GPS 健康追踪、猫砂盆监测等页面可能触及宠物健康建议边界。

**整改**：
- [ ] **BaseLayout footer 加 veterinary disclaimer**："This site provides product research, not veterinary advice. Consult your vet for health concerns."
- [ ] **健康相关页面**（GPS/猫砂盆/饮水机）评测正文中遇到健康声明时加 "...according to owner reports, not veterinary diagnosis"

**时间**：30 分钟

---

### P2-1：品类聚焦建议 ⚪

**问题**：审计建议锁定 1 个品类打穿，但我们已经是 5 品类 84 页。

**实际情况**：已经铺开了，回不去。但可以选择**哪个品类做深做证据化**。

**策略**：
- 选**不锈钢饮水机**作为"信任墙示范品类"（Trends 23，KD 33，已有 6 产品+3 对比+3 指南）
- 先把这 12 个页面的信任证据补齐，形成可复制的样板
- 其他 4 个品类维持现状，不追加新内容

**时间**：融入 P0-2 的 3-5 篇核心评测增强中

---

## 整改优先级总结

| 优先级 | 事项 | 预计耗时 | 阻塞什么 |
|:--:|------|:--:|------|
| 🔴 P0 | PH 页面措辞修正 + 外链平台排查 | 30min | 合规+信任一致性 |
| 🔴 P0 | How We Research 页 + 不推荐页 + 核心评测增强 | 6h | 站内信任基础 |
| 🟡 P1 | Affiliate 披露强化 | 1h | 合规 |
| 🟡 P1 | 邮件订阅 | 3h | 用户留存 |
| 🟡 P1 | 兽医免责 | 30min | 合规 |
| ⚪ P2 | 饮水机品类做深 | 融入 P0-2 | 长期竞争优势 |

**总计：约 11 小时，建议分 3 天执行。**

### 执行顺序

| 天 | 任务 | 耗时 |
|:--:|------|:--:|
| 6/3 | PH 措辞修正 + Affiliate 披露强化 + 兽医免责 | 2h |
| 6/4 | How We Research 页 + 不推荐页 | 3h |
| 6/5 | 3-5 篇核心评测信任增强 + 邮件订阅 | 6h |

---

## 市场数据
- Pet Tech 全球市场 $7.5B → $18B（CAGR 19%）
- Google Trends 2026：智能宠物设备搜索量 5 年持续上涨
- 猫砂盆品类佣金最高：$50-100/单
- 自动喂食器搜索量最大

---

## 关键词调研（2026-05-21）

### 方法
- Amazon 搜索建议 API — 挖掘买家真实搜索词
- Google SERP 首页分析 — 判断竞争强度
- Amazon Best Sellers Rank — 验证产品真实销量
- Google Trends API — 对比搜索趋势（相对热度 0-100）
- Google SERP 广告密度 — 验证商业价值（广告多=购买意图强）

### Amazon 高频搜索修饰词
| 修饰词 | 出现频率 | 含义 |
|--------|---------|------|
| no subscription / no monthly fee | ★★★★★ | GPS+摄像头最大痛点 |
| with camera | ★★★★ | 喂食器刚需 |
| stainless steel | ★★★★ | 饮水机材质焦虑 |
| for multiple cats / large cats | ★★★ | 猫砂盆细分 |
| wireless / cordless | ★★★ | 饮水机便利性 |
| no filter | ★★ | 饮水机成本痛点 |
| open top | ★★ | 猫砂盆新趋势 |

### Google SERP 竞争分析
| 关键词 | 首页竞争 | 机会判断 |
|--------|---------|---------|
| best automatic cat feeder | cats.com, Wired, NYTimes | ❌ 巨头垄断 |
| best self cleaning litter box | cats.com, CNN, Forbes, SprucePets | ❌ 巨头垄断 |
| best gps dog tracker no monthly fee | Reddit, 小品牌站, Facebook | ~~低竞争~~ **无搜索量** ❌ |
| best pet camera no subscription | 小品牌站, Reddit, Wired | ~~有空间~~ **无搜索量** ❌ |
| stainless steel cat water fountain | Amazon, Reddit, Petlibro | ✅ 电商向，编辑内容少 |
| best automatic litter box for large cats | cats.com, Reddit, Wired | ⚠️ 细分有机会 |

### Google Trends 搜索量验证（2026-05-21）
**关键发现：Amazon 搜索 ≠ Google 搜索**

| 关键词 | Trends 热度 | SERP 广告 | 结论 |
|------|------|------|------|
| **stainless steel cat water fountain** | **23** | 0 | 🔥🔥 高需求+低竞争 |
| **best pet camera** | **14** | 0 | 🔥 高需求+可切入 |
| best automatic cat feeder | 6 | **4 广告** | ⚠️ 有人花钱买流量 |
| best self cleaning litter box | 5 | 0 | ✅ 稳定需求 |
| best dog gps tracker | 2 | 0 | ⚠️ 需求弱 |
| automatic cat feeder for 2 cats | 1 | 0 | ❌ 近零 |
| **gps dog tracker no monthly fee** | **0** | — | ❌ Google 上没人搜 |
| **pet camera no subscription** | **0** | — | ❌ Google 上没人搜 |

**核心教训**："no subscription/monthly fee" 是 Amazon 站内搜索词，不是 Google 搜索词。两个平台的用户行为完全不同。Amazon 上的买家在比价，Google 上的用户还在调研。

---

## 产品健康度（Amazon BSR 实测 2026-05-21）

| 产品 | BSR | 评分 | 判断 |
|------|-----|------|------|
| Petlibro Granary | #1,173 | 4.2⭐ | 🔥🔥🔥 爆款 |
| Litter-Robot 4 | #4,116 | 4.6⭐ | 🔥🔥 大单品 |
| PETKIT Eversweet | #10,986 | 4.2⭐ | 🔥 表现好 |
| WOPET Feeder | #25,252 | 4.3⭐ | ✅ 尚可 |
| Catit PIXI | #77,196 | 3.9⭐ | ⚠️ 偏弱 |
| Leo's Loo Too | #172,242 | 3.9⭐ | ❌ 卖不动 |
| Petcube Bites 2 | #204,272 | 4.0⭐ | ❌ 卖不动 |
| Whistle Switch | #270,865 | 3.0⭐ | ❌❌ 差评+滞销 |

### 产品调整决策（已完成 2026-05-21）
- [x] **删** Whistle Switch（BSR 270K + 3.0星，推它浪费流量）
- [x] **删** PETKIT P2（2016 年已下架，Amazon 搜不到）
- [x] **删** DOGNESS Fountain（所有 Amazon 站点无此产品）
- [x] 21 → 18 款产品，5 个品类
- **降级** Leo's Loo Too、Petcube Bites 2（对比文保留，不单写评测）
- **集中火力** Petlibro Granary + Litter-Robot 4

---

## 内容优先级（基于调研 + Trends 验证）

### P0 — 高需求 + 低竞争（立即追加）
1. **Stainless Steel Cat Water Fountain**（Trends 热度 23，🔥 远超所有品类词）
   - 已有 1 篇 Best 列表 → 追加单品评测 ×2 + 对比 + 使用指南
2. **Pet Camera**（Trends 热度 14，品类最高）
   - 已有 6 款产品 → 追加评测 ×2 + 对比
3. 强化 Petlibro Granary（BSR #1,173 爆款，feeder 有 4 广告 = 高转化）

### P1 — 好需求 + 可差异化
4. Best Self-Cleaning Litter Boxes for Large Cats（Trends 细分词）
5. Litter-Robot 4 vs 更多竞品对比（对比词转化率高）

### P2 — 验证后降级或延后
6. ~~GPS Dog Trackers Without Monthly Fee~~ → 已做，不追加
7. ~~Pet Cameras Without Subscription~~ → 已做，不追加
8. ~~Automatic Cat Feeder for 2 Cats~~ → Trends 仅 1，不追加
9. Hidden Litter Box Furniture · 品种专题扩展

---

## 竞品分析
- 大站（cats.com, Wired, CNN, Forbes）占据品类大词
- 新站策略：打细分长尾 + 对比词 + "无订阅费"等痛点词
- Reddit 频繁出现在长尾词 SERP = 内容未被专业站满足的信号
- Amazon 搜索建议是真实买家意图的最佳来源

## 遇到的问题
| 问题 | 解决方案 |
|------|---------|
| Astro 静态输出 index.html 结构，Vercel 默认路由不匹配 | 用 cleanUrls: true 替代自定义 routes |
| 全部 Amazon 占位 ASIN 为无效编号 | 浏览器逐个访问商品页提取真实 ASIN |
| 产品图占位 SVG，文章无配图 | Playwright 从 Amazon 提取高清原图（_AC_SL1500_） |
| 多个页面各自硬编码产品数据（假 ASIN + 空图片） | 重构为 products.json 单一数据源 |
| Amazon Associates 图片 widget URL 不可用 | 改用 m.media-amazon.com 直链 |
| DOGNESS/Whistle Switch/PETKIT P2 不在 Amazon 销售或已下架 | 删除出产品库，只保留有真实 ASIN 的产品 |
| Google 搜索建议 API 被 Playwright 当作下载拦截 | Amazon 搜索建议 API 可用作主要数据源 |
| JSON 编辑后尾逗号导致构建失败 | 删除数组末尾元素后检查逗号 |

## 视觉/浏览器发现
<!-- 关键：每执行2次查看/浏览器操作后必须更新此部分 -->
- smartpetguide.net 线上可访问，**112 页**正常
- 对比文 15 篇、Best 列表 10 篇、评测 26 篇、指南 37 篇、品种 7 篇、信息页 17 篇
- 7/1 新增机器人吸尘器测试品类（Robot #6）

## 技术栈
| 决策 | 理由 |
|------|------|
| Astro 5 纯静态 | <2s 加载，Vercel 免费，SEO 友好 |
| Tailwind CSS v3 | 轻量快速 |
| products.json 单一数据源 | 改一处全站同步 |
| Amazon m.media-amazon.com 图片 | AA 合规，高清 |
| Playwright + Amazon API | 关键词调研零成本 |
| google-trends-api | 趋势对比 |

## 设计系统
| 元素 | 选择 |
|------|------|
| 色调 | Forest #1A3C34 + Honey #D4914B |
| 标题 | Fraunces |
| 正文 | Atkinson Hyperlegible |

## GSC 数据（2026-05-21 → 2026-05-22 晚间）
- 站点地图：✅ 成功提交，17 URL 已发现，上次读取 5/21
- 效果数据：🔴 开始出现但全为 0（总点击 0，总曝光 0，仅 5/20 有微弱柱状信号，上次更新 4h 前）
- 索引编制：⏳ 处理中
- site: 搜索实测：~5 结果，但唯一页面仍是 3 个（首页 + Petlibro 评测 + 猫砂盆指南）
- 结论：新域名第 4 天，Google 爬取预算极低（2-5 页/天），预计 D7-10 出现第一批展示，D14-21 大部分页面被索引
- **当前策略：等数据 + 做推广，暂停大规模内容冲刺**

## 社交引流发现（2026-05-21）

### Reddit（7 条评论：4 条旧 + 3 条今日新增）
- 4 条旧存活：r/CatAdvice 猫砂盆×2 + 水碗×1，r/dogs GPS×1
- 3 条今日新增（2026-05-22，全部对齐 Trends 调研）：
  - r/CatAdvice "Automatic Cat Feeders" — RFID vs 标准喂食器科普（喂食器 Trends 6）
  - r/cats "small cat water fountains--help" — 不锈钢饮水机推荐（不锈钢 Trends 23 🔥）
  - r/CatAdvice "自动喂食器/猫砂盆推荐" — 英文版全品类推荐
- 2 条被 spam 移除（旧）
- Old Reddit 比新版更适合自动化回复

### Pinterest
- 5 张 Pin 已发布（5/21）
- **2 张新 Pin 已发布（5/22）**：
  - Stainless Steel Cat Water Fountains — Why Steel Beats Plastic → /best/stainless-steel-cat-fountains/
  - Best Pet Cameras With NO Subscription 2026 → /best/pet-cameras-no-subscription/
- 累计 **7 张 Pin**，覆盖 5 品类
- 1 张草稿待确认（Petlibro 喂食器对比图）

## AI 搜索调研（2026-05-21 · Perplexity 实测）

### 3 次查询结果
| 查询 | AI 推荐的品牌 | 我们有的产品 | 被引用源 |
|------|------|------|------|
| 最好自动喂食器 | PETKIT YumShare | ❌ Petlibro BSR #1,173 未出现 | cats.com, Wired, YouTube |
| 最好不锈钢饮水机 | Rellaty/Petlibro钢 | ❌ Pioneer Pet 18,500评未出现 | Forbes, Petlibro.com, cats.com |
| LR4 vs Leo's Loo Too | 观点与我们一致 | ✅ | CNN, Forbes, litterboxlab |

### 核心发现
- **AI 只认大站**：100% 的引用来自 Forbes/Wired/CNN/cats.com（DA70+），smartpetguide.net 零次出现
- **产品覆盖 ≠ 能被引用**：我们写过的产品 AI 看不到，因为没有被权威站引用
- **对比文最有价值**：LR4 vs Leo's Loo Too 的内容方向与 AI 回答一致，说明我们的内容策略是对的
- **数据独占**：我们的 BSR 数据、3年成本分析、价格对比表 AI 拿不到

### AI 搜索优化路径（2026-05-23 深度调研更新）

#### 四大 AI 引擎核心差异
| 引擎 | 引用数 | 偏好 | 对小站友好度 |
|------|--------|------|-------------|
| **ChatGPT** | 最少（~7条） | 百科全书式权威源，吸收深度最高 | ⭐⭐ |
| **Perplexity** | 最多（~16条） | 专业精准源，Reddit/社区内容 | ⭐⭐⭐⭐ |
| **Google AIO** | 中等（~6条） | 92%来自Top10域名，但18%是UGC | ⭐⭐⭐ |
| **Gemini** | 中等 | 政府/机构源（.gov .org占36%） | ⭐ |

#### 真实案例
- **Growth Pro**：0→82 AI 引用（ChatGPT 37 + AIO 18 + Gemini 13 + Perplexity 10），11 个月，133% 自然流量增长
- **The Rank Masters**：ChatGPT 引荐流量 8,337% 增长，每用户 50+ PV，5min+ 停留
- **SEO Vendor**：50 个 ChatGPT 直签用户，42% 转化率，几乎零 Google 自然流量

#### 被 AI 引用的关键因子（按权重）
| 因子 | 效果 | 我们现状 |
|------|------|---------|
| 代码块/结构化数据 | +77% 吸收率 | ✅ Schema 已覆盖 |
| 数字/统计数据 | +62% | ✅ BSR/评分/价格数据 |
| 对比内容 | +55% | ✅ 11 篇对比文 |
| 定义标签 | +57% | ⚠️ 可加强 |
| 前 150 词含答案 | 极强正相关 | ⚠️ 可优化 |
| Q&A 格式 | **-6%**（负相关） | ⚠️ FAQ 不应是主要结构 |
| 问题式 H2 标题 | +2.8× 引用率 | ⚠️ 部分页面未用 |

#### 五个关键发现
1. **AI 引用 ≠ Google 排名**：ChatGPT/Gemini/Copilot 中仅 10% 来源在 Google Top10，小站有独立获胜空间
2. **ChatGPT 引用最少但吸收最深**：被 ChatGPT 引用的内容会深度融入回答
3. **Perplexity 最可能引用小站**：偏好专业化、精准回答特定问题的源，不唯 DA 论
4. **Q&A 格式反而减分**：证据密度（数据+定义+对比+代码）比表面格式重要得多
5. **仅 6% 的营销人在做 GEO**：先发优势窗口还在

### 针对 smartpetguide.net 的行动清单

#### 立即可做（0 成本）
| 动作 | 效果 |
|------|------|
| robots.txt 允许 GPTBot/PerplexityBot/Google-Extended | 确保能被 AI 爬取 |
| 所有页面首段 40-60 字直接给结论 | 前 150 词答对问题 |
| H2 标题改为问题式（"Which feeder is best for 2 cats?"） | +2.8× 引用率 |
| 每页加入 3+ 个具体数字（价格/评分/BSR/成本） | +62% 吸收率 |
| 对比页加入结构化对比表 | 已做 ✅ |
| 长段落拆成 2-3 句短段 | Grade 8 已做 ✅ |

#### 本周可做
| 动作 | 时间 |
|------|------|
| Medium 追加 2 篇（不锈钢饮水机+摄像头） | 20min/篇 |
| Quora 回答 3 个宠物智能设备问题 | 15min/条 |
| Reddit 养号继续（D15 开始放链接） | 10min/天 |

#### 1-3 个月
- Perplexity 每月手动查询覆盖关键词，追踪引用增长
- 被 Reddit/Quora 讨论引用 → 进入 AI 引用池
- 争取被其他宠物博客/记者引用（HARO）

#### 关键指标追踪
- 每月手动在 ChatGPT/Perplexity/Google 搜索目标关键词，记录是否被引用
- GA4 建立 AI 引荐渠道（chatgpt.com / perplexity.ai / gemini.google.com）
- 品牌搜索量和直接流量作为早期指标
- **当前策略：传统 SEO 优先 + AI 优化打好基础（Schema/结构化数据）**

### Medium 首发（2026-05-23）
- Petlibro Granary 评测通过 Import 工具发布到 Medium
- canonical 正确指向 smartpetguide.net（已验证）
- 后续可追加 2-3 篇

### GSC 首次真实数据（2026-05-23）
- 1 点击 / 4 曝光 / CTR 25% / 平均排名 1
- 首次确认 Google 在展示 smartpetguide.net
- 查询词和页面明细待出（比汇总晚 1-3 天）

---

## GEO + Schema 验证（2026-05-21）
- Rich Results Test 验证通过：
  - 评测页：6/6 valid（Product+Merchant+Article+Breadcrumb+FAQ+Review）
  - Best 列表：3/3 valid（Article+Breadcrumb+FAQ）
  - About 页：1/1 valid（Article）
- Review Schema 需含 itemReviewed → Product(name+description+brand+offers) 才通过
- FAQ + Breadcrumb Schema 早就有了，无需改动
- Key Takeaways 组件放在评测/Best/对比页 h1 之后效果最佳
- About 页 EEAT 信号：团队描述+测试方法+透明盈利+AboutPage Schema

---

## 引流渠道调研（2026-05-22 · 完整报告见 traffic-research.md）

### 核心结论：三线并进

| 线 | 渠道 | 优先级 | 风险 | 目标 PV |
|----|------|--------|------|---------|
| 1 | Pinterest 提频 | P0 | 极低 | 2-3 月后 2K-10K/月 |
| 2 | Facebook Groups | P0 | 低 | 1 月后 500-3K/月 |
| 3 | Reddit 新号养号 | P1 | 高 | 养号 2 周后 1K-5K/月 |

### 关键数据
- Pinterest：96% 搜索不带品牌名，Pin 生命周期 6-12 月，ROAS 高于 FB/IG 30%
- Facebook Groups：案例 30 天零广告费获取 12 个客户
- Reddit：转化率 2-3x vs 社交媒体，但必须 90/10 法则
- TikTok：affiliate 互动率 5.2%（vs IG 2.0%），faceless 模式月入可达 $30-40K
- Medium：主要价值 canonical 借用 DA95 域名权威为主站"拉票"
- Quora：74% 流量来自 Google，回答可持续引流 3-5 年

### 已确认的教训
- Reddit 自动化发帖 100% 被检测 · 旧号 10 条全部移除
- 新号 Day 1 放链接 = 必死
- Pinterest 7 Pin 全部存活，是目前最安全渠道

## Day 6（5/24）数据初探

### GSC 数据评估
- 1 点击 / 4 曝光 / 4 页面出数据
- **评估为自身测试流量**：site:smartpetguide.net 搜索 + 页面 URL 检查产生的曝光
- 索引报告仍在"处理中"
- 数据延迟 ≥2 天，5/22+ 数据未到

### Pinterest 早期信号
| 发现 | 数据 |
|------|------|
| Best 列表 Pin 浏览量 | ~11/Pin（3 天） |
| 对比文 Pin 浏览量 | ~4/Pin |
| Best vs 对比 | **~3:1** |
| 保存/点击 | 全部为 0 |
| 月浏览量 | 5 |

- Best 列表类型在 Pinterest 算法中曝光优于对比文
- 零互动对 3 天新 Pin 属正常

### Awin 联盟入驻
- ShareASale 已被 Awin 收购合并
- 自助注册路径：ui.awin.com/publisher-signup/
- 4 步流程：Account Setup → Promotional Type → Promotional Space → Verification
- 需 reCAPTCHA 手动验证
- 注册后 1 个工作日邮件联系

### 时间线校正
- Day 1=5/19 正确，M7 达标=Day 4（5/22，非 Day 5）
- 阶段 4 完成于 Day 3（5/21），非 Day 4-7

## 客户研究（VOC + Reddit）— 2026-05-24

### 综合结论
- Amazon VOC + Reddit + Google Trends 三角验证，方向高度一致
- **不锈钢饮水机** 是最大内容机会（Trends 23 + Reddit 材质共识 + Amazon 好评）
- **可靠性 > 一切**：WiFi 断连在 Amazon 和 Reddit 上都是一票否决项
- **订阅费愤怒** 是跨品类转化杠杆，"3 年真实总成本"对比是差异化利器
- **"Worth It"** 是 Reddit 最高频帖子类型，$/月 拆解是转化关键
- WOPET 在 Reddit 口碑翻车，评测需诚实标注可靠性风险
- 缺 4 款社区热推产品：Eufy D605 / Wyze Cam v4 / SureFeed Microchip / Owlet

### 文件产出
- `customer-research/amazon-voc-raw.md` — Amazon 3 产品 38 条评论 VOC 原话
- `customer-research/reddit-raw.md` — Reddit 6 子版块 57 次搜索社区挖掘
- `customer-research/synthesis-report.md` — 综合分析 + 10 选题 + CTA 升级清单

### 10 个经验证选题（见 synthesis-report.md）
### 买家原话语录库（VOC Gold，见 synthesis-report.md）

---

## 良辰美案例对照分析（2026-05-25，Day 7）

### 来源
抖音博主「光羽的平行世界」采访 AI 建站者良辰美（1997年奶爸，300+网站，年入$200K+）的深度分析。

### 良辰美的真实路径

| 维度 | 良辰美 | SmartPetGuide | 差异分析 |
|------|--------|---------------|---------|
| 策略 | 300个站赌1个爆（量） | 1个站做深做透（质） | 本质不同，不可照搬 |
| 成功率 | ~2.7%（前36个全失败，第37个爆） | 未知（才70篇） | **他的核心不是"怎么成功"，而是"承受失败"** |
| 流量获取 | SEO为主（含评论外链灰帽） | 社交+SEO白帽 | 他快但高风险，你慢但可持续 |
| 变现 | AdSense广告+工具付费 | Amazon联盟 | 他的RPM更高但你的转化意图更强 |
| 速度 | 5-10分钟/站 | 1-3小时/篇 | 你投入更大，单篇长期回报也更大 |
| 技术 | 声称完全不懂代码 | AI辅助+人工判断 | 你比他更诚实 |
| 风险 | 已被封禁（关联账号光羽笔记AI） | 白帽低风险 | 你的路径可持续 |

### 可迁移的 5 个核心经验

1. **不要在第 5 个站就停下来**
   - 良辰美前 36 个站全部默默无闻。如果他在第 5 个就放弃，就没有后来的 $200K。
   - → SmartPetGuide 才 70 篇，远没到该停止内容生产的阶段。
   - → **恢复内容生产，每周 5-8 篇。**

2. **新域名 SEO 数据回馈周期是 2-4 个月，不是 1-2 周**
   - 良辰美第 37 个站从上线到日流量 10 万用了数月。
   - GSC 当前 1点击/4曝光 是正常新站状态，不能据此判断内容方向。
   - → **"等数据 1-2 周"是错误的决策，立即修正为"边等边建"。**

3. **成功的窗口期 = 追热点 + 第一个做**
   - 良辰美第 37 个站爆在「心动小镇」游戏刚上线的搜索需求爆发期。
   - SmartPetGuide 的等效策略：追踪 Amazon 宠物智能设备 New Releases。
   - → **建立「新品速报」栏目，48 小时内出稿。**

4. **内容分级 > 每篇精雕**
   - 良辰美的优势不是质量而是速度。但你不需要做到他的极端。
   - 用分级策略：20% A级精雕（高竞争词）+ 50% B级标准（中等竞争）+ 30% C级快速（长尾覆盖）。
   - → **节省的时间用于产出更多 B/C 级内容，扩大长尾词覆盖。**

5. **社交流量是放大器，不是发动机**
   - 良辰美 100% 依赖 SEO。社交渠道（Pinterest/FB/Reddit）有价值，但在早期不应占据核心精力。
   - → **社交压缩到 15min/天，Pinterest 保持每周发布节奏。**

### 绝不能学的 3 个坑

| 坑 | 风险 | 后果 |
|------|------|------|
| AI 评论外链引流 | 🔴 黑帽SEO | Google SpamBrain 检测 → 域名降权/除名 |
| 完全 AI 自动化生成内容 | 🔴 规模化滥用 | 2026年3月 Spam Update 专门打击，仅30%恢复 |
| "不懂代码"的营销人设 | 🟡 误导 | 实际需要一定的技术判断力（尤其是支付/安全） |

### 策略调整记录（2026-05-25）

| 原策略 | 新策略 | 触发原因 |
|--------|--------|---------|
| 暂停新内容，等数据 1-2 周 | 恢复生产，每周 5-8 篇 | 良辰美教训：新域数据要月级才有意义 |
| 全部内容 A 级打磨 | 20/50/30 分级 | 效率优化，长尾词不值得全流程 |
| FB+Reddit 每日重点养号 | 压缩到 15min/天 | 社交流量不稳定，SEO 是复利引擎 |
| Medium 继续追加 | 暂停追加 | 3 篇 canonical 足够，边际收益递减 |
| Quora/TikTok 待启动 | 无限期推迟 | 当前阶段聚焦内容+SEO |
| 无新品追踪机制 | 建立 Amazon New Releases 监控 | 学习良辰美"追热点窗口期"策略 |

### 关键数据推算（供后续验证）

```
良辰美游戏攻略站：
300万UV → $30K/月广告收入
RPM ≈ $6.67（合理范围，需主要英语国家流量）

SmartPetGuide 对应的目标：
要达到月入$2000（12月目标高线）：
- Amazon 佣金率 3%，客单价 $60，转化率 2%
- 需要：$2000 ÷ 3% ÷ $60 ÷ 2% = 55,556 UV/月 ≈ 1,852 UV/天
- 按良辰美的 RPM $6.67，如果加 AdSense：55,556 × $6.67/1000 ≈ $370/月
- 结论：联盟 vs 广告双线变现是最优解（Mediavine Journey 加入计划）
```

## GSC 数据交叉验证（2026-05-25 Day 7）

### 方法
对照 24h 逐时数据 + 3 个月汇总数据 + 当天操作日志，区分测试噪音和真实搜索流量。

### 发现

| 数据项 | 原始值 | 交叉验证后 | 判断依据 |
|--------|:--:|:--:|------|
| 3 个月总曝光 | 7 | 约 5-6（真实） | 首页部分为 site: 残留，其余无测试证据 |
| 3 个月总点击 | 1 | 1 | 猫砂盆购买指南，未主动搜过或点过 |
| 24h 曝光 | 5 | 约 4-5 | 晚 8-9 点集群，经查操作日志该时段无测试活动 |
| 24h 点击 | 0 | 0 | — |

### 交叉验证方法
1. 24h 逐时数据找到曝光集群时段
2. 对照当天操作日志，确认该时段是否有测试行为
3. 查查询词表 — 如为 site: 搜索应在查询词中出现 `site:` 前缀
4. 5/24 晚 8-9 点无操作日志、查询词表为空 → 不能确认是测试噪音

### 核心教训
- **GSC 数据包含自身测试噪音**：但并非所有曝光都是测试，需逐时段交叉验证
- **不要在无操作日志的情况下假设数据是测试产生的**
- **新站第一周数据量太小**：即使全部是真实的也不足以做方向判断
- **交叉验证必须有操作日志支撑**：不能凭"那天做了某件事"就推断

---
*每次调研后更新此文件*

## GSC Snapshot 6 与高展示零点击页判断（2026-07-15）

### 当前实测数据

- GSC 索引报告更新于 2026-07-10：**33 已索引 / 15 未索引**，较 Snapshot 5 的 22 已索引增加 11。
- 未索引分类：网页会自动重定向 5、重定向错误 3、备用网页（有适当规范标记）1、已抓取未索引 4、重复网页（Google 选择的规范页不同）2。
- Sitemap 于 2026-07-11 读取成功，发现 **113 URL**。
- 最近 3 个月效果：**4 点击 / 287 展示 / CTR 1.4% / 平均排名 35.4**。
- 高展示零点击页：Petlibro Granary 69、GPS no monthly fee 53、Catit PIXI 49。

### 重定向结论

- 5 个“网页会自动重定向”中，两个是不带尾斜杠 URL → 带尾斜杠 canonical；两个是 HTTP/WWW → HTTPS 规范域；这些是预期重定向，不应改成 200。
- `/reviews/nofee-gps-tracker-review/` 当前已直接返回 200，GSC 仍显示 2026-05-24 的旧抓取结果，属于报告滞后。
- 3 个“重定向错误”示例（smart-home-pet-devices、best-no-subscription-cameras、amazon-basics-litter-box-review）当前均直接返回 200；验证已开始，继续等待 Google 重抓，无需新增代码重定向。
- “网页会自动重定向”的验证失败不等于 canonical 故障；这些 URL 本来就应该跳转，反复验证会继续失败。

### SEO 决策

- 三个目标页源码标题原为 70+ 字符；BaseLayout 还会追加 `| SmartPetGuide`。优化必须按最终 HTML 长度验收，而不是只看源码 title。
- Petlibro 已有 Quick Answer、Buy/Skip/Alternative，正文结构足够；最小改动是精简搜索标题和描述，并从相关指南补正文内链。
- GPS 页实际包含两个免订阅方案和一个需要订阅的 Tractive。优化重点是显式说明 Tractive 仅为 cellular benchmark，并增加月费/技术/适用场景/限制比较表。
- Catit 页缺少首屏购买判断；新增 Quick Answer 与 Buy/Skip/Alternative，但不新增无法追溯的 owner quote 或医疗结论。
- 站点平均排名仍为 35.4，title/meta 只是 CTR 基础；后续应以 14-28 天窗口观察目标页展示、点击和平均排名，不在短期内反复改标题。

### 生产交付结论

- SEO 提交 `c42b9a1` 已推送到 `origin/master`，本地 `HEAD` 与远程跟踪分支一致。
- Vercel 生产部署 `dpl_FjC2DxWF4siygZSn5LuhidoQZR4R` 状态为 `READY`，生产别名包含 `smartpetguide.net` 与 `www.smartpetguide.net`。
- 生产 HTTP 核验：主页、`robots.txt`、`sitemap-index.xml` 及三个目标页均返回 200，未发生意外跳转。
- 生产 HTML 核验：Petlibro/GPS/Catit 的 title 长度为 58/56/59，description 为 150/151/158；canonical 均为带尾斜杠自指，`dateModified` 均为 `2026-07-15`，目标决策内容已上线。
- 本轮没有新增 URL，因此不需要仅为本次 title/meta 调整重提 sitemap；继续按既定 14-28 天窗口观察 GSC。

## W28 自动化信号与 Week 10 方向（2026-07-12）

### 证据汇总

- W28 L2 VOC 共 165 条：Google PAA 36、Amazon 25、YouTube 104。
- 唯一达到 High 跨来源标准的主题是 **automatic feeder WiFi / app / offline reliability**，共 41 条、覆盖 3 类来源。
- 四集群 phrasing map 和 LR4 compatibility 已由 Weekly Review 依据 Git/页面证据判定为 Proven；不再作为下一周实验重复执行。
- AI Signal Daily/Weekly 反复提醒：单次 AI visibility 排名波动不能代表趋势。现阶段更可靠的检查对象是 `identity / source / date / quickAnswer / follow-up answerability`。
- Week 9 的结果层仍未突破：索引 22、引用域名 11、Pinterest 出站 0、品牌回复 1/6、affiliate/outbound 0。

### 决策

1. Week 10 不再做新的技术 GEO Sprint；GEO 转为现有高价值页的事实层与复述稳定性审计。
2. 默认不新增页面。~~先完成剩余 4 个已抓取未索引 URL 的确认与处置~~ → **7/13 已闭环**：8/8 URL 已确认并分类，后续完成其中 2 个待加固页面。
3. 外链从“发出邮件数”升级为“编辑型目标 + 可链接资产 + 回复/落链结果”，目录/Profile 不作为主要成果。
4. Brand Outreach 不按原 D20 一次扩 10 个 CRM；先用 Homerunpet 做 1 个 email-first v2 小试点，Aorkuler只做一次收口。
5. Pinterest 在出站点击破 0 前不恢复铺量。
6. `quickAnswer` 真实进度以 Git 为准：13/38；覆盖率不作为机械 KPI，只补目标页缺口。

### 持续观察

- YouTube 7/12 刷新失败，W28 使用 7/7 样本；下周重试一次，并把采样扩到猫砂盆 TCO、饮水机健康、零订阅摄像头/GPS。
- GEO 综合分数最近明确值仍是 74；下次复检看综合 AI Citability/Brand Authority，不重复证明 Technical GEO 基础项。
- Guest Post Round 3 已发 5/5，但尚无回复/落链，7/14 后才能判断触达质量。

## Month 2 四周战略决策（2026-07-13）

- 战略周期固定为 2026-07-13 至 2026-08-09，采用“月度框架固定、每周日滚动拆解、每日最多 3 个 P0”。
- 北极星从页面数量转为外部验证：索引、编辑型外链、品牌认真回复和真实点击。
- 四周资源比例固定为：外链/PR 35-40%，GSC/现有页 25-30%，战略 GEO/VOC 20-25%，数据与维护 10-15%。
- 新内容默认 0，只有 GSC 连续增长、跨来源 VOC、外联资产需求或合格新品触发时才创建；单周最多 2 篇，周期最多 6 篇。
- GEO 保留但转为“引用理由”建设；Technical GEO 周度只做 5 分钟存活检查，综合审计月度一次。
- 详细目标、四周主题和 Continue/Adjust/Stop 规则见 `docs/month-2-strategy-2026-07-13-to-2026-08-09.md`。

---

## Week 10 周一基线复核（2026-07-13）

### GSC 数据实测

- 索引 22（持平），曝光 282（+14），点击 4（持平），CTR 1.4%，平均排名 35。
- `automatic-feeder-wifi-keeps-disconnecting` 已不在"已抓取-未索引"列表中 → **已入索引**（Week 9 内链加固首果）。
- 重定向错误 3 + 自动重定向 4 + 规范标记 1 + 重复规范 1 无变化。

### 已抓取-未索引 8 URL 处置（3+2+2+1=8）

| 分类 | URL | 处置 | 理由 |
|------|------|:--:|------|
| 等待 | `stop-automatic-feeder-from-jamming/` | — | Week 9 已加固（quickAnswer+FAQ+内链+VOC quotes） |
| 等待 | `introduce-cat-to-automatic-litter-box/` | — | Week 9 已加固（quickAnswer+FAQ+内链） |
| 等待 | `cat-wont-drink-from-water-fountain/` | — | Week 9 已加固（quickAnswer+FAQ+内链） |
| 加固 | `cat-breaking-into-automatic-feeder/` | PAA C级，缺内链输入 | 从已索引 buying guide 补 Related Resources |
| 等待 | `for-brands/` | 商业页面 | 不期望被搜索用户发现 |
| 加固 | `self-cleaning-litter-box-buying-guide/` | 核心购买指南 | 已有 VOC TCO+quickAnswer，补内链 |
| 等301 | `wopet-automatic-feeder-review` | 无尾斜杠旧 URL | 已验证 301→带斜杠正常，等 Google 重抓 |
| 等301 | `automatic-feeder-buying-guide` | 无尾斜杠旧 URL | 同上 |

> `automatic-feeder-wifi-keeps-disconnecting/` 已退出该桶（7/13 列表中不存在）→ 已入索引。

### Pinterest

- 月浏览 1,105→1,423（+29%），粉丝 1，出站点击仍为 0。
- 增长健康但未形成分发闭环。继续只观察不铺量。

### 引用域名

- Semrush 检测到引用域名 12（+1 vs 7/10 的 11）、外链 28、Authority Score 2（首现）。
- 新增域名、来源页面、目标 URL 和相关性**待核验**——12 只是工具计数变化，不能直接断言为"自然外链积累"或编辑型外链落地。
- 待核验字段见 `weekly-metrics-log.md` Snapshot 5。

### GA4

- 7/13 浏览器实测：29 活跃用户/7天、30 page_view、0 affiliate/outbound。21/29 来自 Singapore，Organic Search 为 0 session。Singapore 占比过高，疑似测试或非目标流量，不直接断言为自测。

## 竞品格局调研 + Semrush KD 实测（2026-05-27，Day 9）

### 一、竞品生存状态

调研了 6 个"中小宠物评测站"的生存状态：

| 站点 | 索引量 | 外链 | 域名年龄 | 状态 |
|------|:--:|:--:|:--:|------|
| **pawsomeadvice.com** | 806 | 723 (357域) | 5.3年 | 🟡 停更（2023-2024），唯一可比竞品 |
| excitedcats.com | 残留124 | — | 6.3年 | ❌ 被 Catster 收购 |
| allaboutcats.com | 残留9 | — | 24年 | ❌ 被 cats.com 吞并 |
| litterboxlab.com | 40 | — | 2个月 | ❌ 已死 |
| thepetsdaily.com | 0 | — | — | ❌ 从未建成 |
| catster.com | 7,310 | — | 多年 | 🔴 已是头部大站，非竞品 |

**核心发现：中层竞品全灭。宠物评测赛道的独立中小站要么死了、要么被收购了。目前智能宠物设备这个细分里，没有一个活跃的独立评测站。**

### 二、SERP 格局

三个高价值商业关键词的 Google 首页完全被 DA70+ 大站 + Reddit 垄断。小站在首页出现率为 0%。这不是内容质量问题，是域名权重不够——Google 根本不会把新域名排到 Forbes/cats.com 中间。

### 三、Semrush KD 实测

| 关键词 | KD | 月搜索量(US) | 意图 | 对应我们内容 |
|------|:--:|:--:|------|------|
| best self cleaning litter box | **55%** | 8.1K | Commercial | Best 列表 |
| best automatic cat feeder | **41%** | 3.6K | Commercial | Best 列表 |
| stainless steel cat water fountain | **33%** | **9.9K** | Commercial | Best 列表 🟡 |
| litter robot 4 review | **29%** | 720 | Informational | 单品评测 |
| best pet camera no subscription | **15%** | 140 | Commercial | Best 列表 ✅ |
| how to clean cat water fountain | **12%** | 140 | Informational | **还没做！** ✅ |

**KD 55% 意味着需要 26 个引用域名才能参与竞争。我们目前只有 1 个。**

### 四、pawsomeadvice 外链拆解

**结论：不是靠主动外链建设，是 5 年 806 页内容的自然积累。**

- 查到的引用域名类型：联盟平台(impact.com)、社交(Pinterest/FB/IG)、宠物品牌(armarkat)、网站统计(easycounter)、学术(jstor)
- Domain Strength 仅 16（5 年！）——证明从未做过 deliberate outreach
- **只做内容不做外链 = 5 年后 Domain Strength 16 = 停更**

### 五、三层数据交叉验证

| 维度 | AuGrav 案例 | pawsomeadvice | SmartPetGuide | 教训 |
|------|:--:|:--:|:--:|------|
| KD 策略 | 全部 <20 | 未评估 | 做了 9 篇 KD 33-55 | ❌ 大词太早 |
| 外链策略 | 未披露 | 0 主动，自然积累 | 0 主动 | ❌ 必须启动 |
| 技术 SEO | 未提及 | 未提及 | 投入 29% 时间 | ❌ 过度打磨 |
| 社交信号 | ✅ 提升排名 | ❌ 完全缺失 | ✅ Pinterest 起步 | ✅ 差异化优势 |
| 内容聚焦 | 垂直（珠宝定制） | 太散（狗+猫+野生动物） | 极致聚焦（智能设备） | ✅ 长期优势 |

### 六、经验提炼

1. **外链从 1% → 20%**：子木公式验证（SEO=80%内容+20%外链+0%技术），我们技术投入 29%，外链 1%，严重失衡
2. **KD<20 优先**：Best 列表全部 KD 33-55，在 Day 9 做是提前了 6 个月。优先做 KD 5-20 的长尾信息型内容
3. **中层真空 = 机会窗口**：没有同级竞品，坚持 12 个月做到 200+ 页就是唯一活人
4. **时间线再次确认**：良辰美（最快）8 个月爆发，pawsomeadvice（最慢）5 年还在停更，我们预估 Month 5-6 心理门槛合理
5. **"No Subscription" 角度验证有效**：Pinterest GPS Pin 831 浏览 + Semrush KD 15% + Amazon VOC 排名第一痛点，三线交叉验证

---

## EEAT 真实性审计（2026-05-29，Day 11）

### 审计发现
- 全站 60+ 处 "tested/hands-on/testing" 措辞与研究方法论不符
- 缺失作者署名、数据来源标注等 EEAT 信号
- 邮箱域名 .com vs .net 不一致

### 修正
- 全站措辞统一：tested → research-backed/analyzed ✅
- 作者署名 + 数据来源已补全 ✅
- 邮箱已修正，About 页已重写 ✅

### 新 EEAT SOP
每篇新文章 Day 1 就带：作者署名 + 更新日期 + 数据来源 + 联盟披露

---

## GSC 索引问题：尾部斜杠重定向（2026-06-01，Day 13）

### 发现
- GSC 报告 4 个重定向错误 + 3 个自动重定向页面
- 根本原因：Astro 默认生成带斜杠 URL (`/page/`)，Vercel 配置 `trailingSlash: false` → 浏览器请求 `/page/` 时 Vercel 301 重定向到 `/page`
- Googlebot 看到 301 即标记为"重定向错误"

### 修复
- `astro.config.mjs` 添加 `trailingSlash: "never"` — 全站 URL 统一无斜杠
- Sitemap 同步更新为无斜杠 URL
- 同时发现站点在 Vercel 而非 Netlify（之前凭假设记错）

### 教训
- 新站 Day 10-14 必做：GSC 索引报告检查 + 尾部斜杠统一
- 部署相关操作前先验证平台（读 `server` 响应头，不是凭记忆）

---

## Vercel GitHub 自动部署（2026-06-01，Day 13）

### 发现
- Vercel 项目未连接 GitHub，之前依赖 CLI 手动部署（最后一次：`8d131b9` Day 8）
- 今天 Day 13 的 8 个 commit 推送到 GitHub 后未自动部署，~1 小时后才发现
- 5/29-5/31 期间无代码提交，不存在积压

### 修复
- Vercel Settings → Git → 连接 `muchengxian-lab/smartpetguide`
- 现在每次 `git push` 自动触发 Vercel 构建部署（已验证 3 次自动部署成功）

### 教训
- 项目初始化后第一件事：确认 CI/CD 自动部署已接通
- 变更部署配置后立刻验证线上是否生效（响应头、新增内容）

---

## 内链不对称诊断（2026-06-22，Week 6）

### 发现
全站内链结构严重不对称：

| 方向 | 状态 | 缺口 |
|------|:--:|:--:|
| 评测 → Best/指南/对比 | ✅ Explore More 区块 | 0 |
| Best → 评测 | ❌ 产品名为纯文本 | ~45 条 |
| 对比 → 评测 | ❌ 产品名为纯文本 | ~30 条 |
| 品种 → 评测 | ❌ 产品名为纯文本 | ~25 条 |
| 指南 → 评测 | ❌ Related Resources 只链 Best/指南 | ~30 条 |

总缺失约 100 条跨类型内链。评测页是核心转化页面，却是入站链接最少的类型。

### 修复
- `products.json` 新增 `reviewSlug` 字段（26 款产品）
- Best/对比/品种三模板产品名改为条件链接
- 抽象对比页无 reviewSlug 自动跳过

---

## 尾斜杠 308 重定向链（2026-06-22，Week 6）

### 发现
站内导航全部用 `/page/`，但 Astro+Vercel 配置输出 `/page`。每次内链触发 308。101 页 × 8 内链 ≈ 每次全站爬取浪费 800 次请求。属于静默泄漏——不报错不 404，但爬取效率腰斩。

### 修复
- `astro.config.mjs`：trailingSlash `"never"` → `"always"`
- `vercel.json`：trailingSlash `false` → `true`
- Sitemap 自动同步为带斜杠 URL

### 教训
- Astro 和 Vercel 的 trailingSlash 必须与站内链接格式三方一致
- 新站应在索引量少时（14 页）修复，过渡代价最小

---

## www 子域名不解析（2026-06-22，Week 6）

### 发现
`www.smartpetguide.net` 无 DNS 响应。任何带 www 的外链全部丢失。

### 修复
`vercel.json` 添加 host-based 301 重定向（需 www 子域 DNS 指向 Vercel 才能完全生效）。

---

## 满月第三方审计（2026-06-22，Week 6 → Week 7 策略转向）

审计来源：[MONTH-1-THIRD-PARTY-AUDIT.md](MONTH-1-THIRD-PARTY-AUDIT.md)，第三方视角，结合本地项目数据 + 构建验证 + 线上入口响应 + 公开市场信息（APPA/NYPost/WSJ/The Verge/Pew/arXiv） + 既有用户研究。

### 审计核心发现

**SmartPetGuide 第一个月不是"流量增长月"，而是"资产与索引种子月"。** 内容/技术/GEO 超前，索引/外链/社交出站/点击/转化仍在冷启动早期。

评分：内容资产 A- | 技术 SEO A | GEO B+ | EEAT B | 搜索表现 C | 社交流量 C- | 外链权威 C | 商业转化 D | 数据治理 C+ | 合规 C

### P0 风险（6/23 已修复）

1. **隐私页 vs GA4 不一致**：`privacy.astro` 写不用追踪但 `BaseLayout.astro` 加载 GA4 → ✅ 改为真实披露
2. **外部素材旧口径**：`backlinks/action-plan.md` 和 `pins/pin-plan.md` 残留 hands-on/testing → ✅ 全改 research-backed

### 策略转向：生产驱动 → 分发与验证驱动

- 内容生产维持 5-7 篇/周，但仅围绕 4 个集群（不锈钢饮水机/零订阅摄像头GPS/喂食器可靠性/猫砂盆TCO）
- 外链 Outreach 升级为每周固定 2-3h（不可挤占）
- Pinterest KPI 从 Pin 浏览切换为出站点击率

---
## GSC Sitemap 与抓取行为实测（2026-06-28，Week 7 总结）

### 发现

通过 GSC 抓取统计报告 + sitemap 读取记录交叉验证，得出以下关于 Google 对小站行为的实测结论：

### 核心事实

| 发现 | 证据 |
|------|------|
| Google 首次提交后读一次，之后不主动回读 | sitemap 6/5 读取后，22 天无主动回读，直到 6/27 手动重提 |
| 手动重提 sitemap 是能触发 Google 重读的 | 6/27 重提后立即读取 |
| 批量内容更新能触发抓取峰值 | 6/27 21 文件改动 → 单日抓取 ~55 次（平时 3.8） |
| URL Inspection 比 sitemap 更优先 | 手动提交的 URL 直接入优先抓取队列 |
| 抓取预算 ~3.8/天不是硬上限 | 6/27 峰值证明 Google 可以放大抓取，前提是探测到"重要变化" |

### 由此制定的三条操作规则

1. **每天 GSC URL Inspection 5 个优先 URL** — 把有限抓取定向到最有价值的页面
2. **每周一重提 sitemap** — 保底，确保 Google 至少每周读一次
3. **新内容上线当天重提 sitemap** — URL 数量变化时触发峰值抓取（类似 6/27 效应）

### 其他 Sitemap 经验

| 规则 | 说明 |
|------|------|
| `lastmod` 必须真实 | 造假会让 Google 全程忽略此字段（已修 ✅） |
| `priority` / `changefreq` 被 Google 忽略 | 可以删掉省代码 |
| robots.txt 加 sitemap 声明 | 被动发现兜底 `Sitemap: https://smartpetguide.net/sitemap-index.xml` |
| sitemap 不能含 301/404 | 降低 Google 对 sitemap 的信任 |
- GSC KPI 从曝光/点击切换为索引率
- 取消：死目录提交、无反馈大词 Best、无出站验证 Pin 铺量
- 暂停：机器人吸尘器仅保留 3 篇测试、Medium 不再追加

### 4 个内容集群（VOC + 市场双验证）

| 集群 | 核心角度 | 验证 |
|------|------|------|
| A: Stainless Steel Cat Fountain Hub | 卫生/痤疮/清洁/材质安全 | Trends 23 + Reddit + Amazon |
| B: No Subscription Camera/GPS TCO Hub | 3年成本，零订阅替代 | VOC #1 + Semrush KD 15 |
| C: Automatic Feeder Reliability Hub | 断网出粮/卡粮/App稳定性 | VOC #1 购买门槛 |
| D: Litter Box Worth-It/3-Year Cost Hub | $699→月成本拆解 | Reddit 最高频 + 转化杠杆 |

### 整改记录（6/23）

- [x] privacy.astro GA4 披露修正
- [x] backlinks/action-plan.md 4 处 hands-on → research-backed
- [x] pins/pin-plan.md 2 处 hands-on/testing → research-backed/analyzing
- [x] task_plan.md 日常/周期任务全面重构（新增口径自检 + GA4 看板 + 外链固定 + 出站实验 + 取消清单）
- [x] task_plan.md 新增阶段 14 满月审计策略调整
- [x] 构建验证：103 页，0 错误

## 变现 Sprint 启动 + 两日密集执行（2026-06-29 ~ 07-01）

### 三轨道合并决策
- 原始 A/B/C 三轨道评估后合并为两轨道：Task A（后台基建）+ Brand Outreach（B+C 合并）
- 合并理由：B 和 C 打的是同一批 12 个品牌，分开外联会自我竞争；A 在 GSC 仅 3 次点击时 30 天内不可能有可量化收入信号
- 执行顺序调整为 A 先（3 天一次性完成）→ Brand Outreach（唯一主动外联轨道）

### Task A 变现基建完成
- 联盟链接审核：全部 26 款产品含 `tag=smartpetgui0a-20`，全部模板 `rel="sponsored"`
- Review 模板新增 Quick Decision 模块（buyIf/skipIf/bestAlternative）：3 篇高优先级评测已添加
- Guide 模板新增推荐产品 CTA：2 篇指南从零变现路径到各 3 产品卡片
- GA4 周检确认：affiliate_click/outbound_click 跟踪代码正确，内部流量过滤器已启用，30 活跃用户/7 天

### Brand Outreach 推进
- `/for-brands/` 页面：免费可见性快照 → $199/$499/$1,200 审计阶梯 + 编辑边界
- 审计模板（12 节）、外联 CRM（12 品牌）、Aorkuler 样本审计
- 旧索链接模板标记为 Historical，新序列：D0（3 买家问题）→ D3（免费快照）→ D7（闭环）
- Wave 1 外联：Aorkuler（service@）、KittySpout（表单）、YEAPAW（表单）、Elspet（help@elspet.com 已建 cares）、xpai（无官网跳过）

### 内容+SEO 进展
- 两日内容：PAA #3-#5（饮水机/喂食器WiFi/喂食器防盗）+ Robot #6（机器人吸尘器），106→112 页
- 内链补全：评测模板 5 品类各加 2 指南链接 + Best 模板跨品类互链
- 页面加固：No-Fee GPS/Aorkuler 加用户原话，Catit PIXI verdict 强化，首页加 social proof
- GSC：索引仍 14 冻结（5 周），点击 3→4，评价摘要 2→4。Sitemap 已重提交（106→109 已读取）
- 实验 Pin：7/12→8/12（Pin #7 WiFi断连角度、Pin #8 猫砂+机器人吸尘器角度）

### 本周交叉排班验证
- 两套任务体系（Week 8 内容+变现 Sprint）首次交叉执行，22/22 任务全部完成
- 优先级规则（GSC > Pin > 人工阻塞 Sprint > 内容 > Claude Sprint）经实战验证有效
- 在 task_plan.md 顶部固化了两套体系的协调排班表

## 机器人吸尘器品类测试 + GEO 模板收官（2026-07-03）

### 机器人吸尘器测试
- 新增 3 篇：猫砂清理 / Golden Retriever 掉毛 / 机器人 vs 手持对比
- 测试结论：机器人吸尘器是宠物设备站的天然延伸品类（搜索量中、竞争低、内容可复用现有研究框架）
- 图片问题：无产品数据库，Pin 图复用 Litter-Robot 4 图片，长期需自建产品图库

### GEO 模板修复
- Compare/Best 模板底部加数据来源+日期脚注（解决 Codex 6/27 增量审计 P1-6/7）
- Guide 模板新增 `quickAnswer` 可选字段（40-60字一句结论，AI 可提取的结构化摘要）
- GEO Score 70→74（7/1 复检），目标 8/1 达到 80

### 外联进展（截至 7/3）
- Wave 1：Aorkuler **已回复+快照已发** ✅；KittySpout/YEAPAW/Elspet D3 跟进已发
- Wave 2：WOPET/Petlibro D0 已发（7/3），D3 跟进日 7/6
- 外联 Round 3：5 个 guest post 目标已备，待人类发送
- 关键里程碑：**Aorkuler 回复验证了「给价值再开口」的策略**，首个正向品牌信号

### 114 页内容结构
- 评测 26 篇 / 对比 15 篇 / Best 10 篇 / 指南 37 篇 / 品种 7 篇 / 信息页 17 篇 / 品牌页 1 篇 / 机器人吸尘器 3 篇(测试品类)

### 周五（7/3）收尾
- Pin #10：Robot vs Stick 对比角度（10/12 实验 Pin）
- Wave 1 D3 跟进：KittySpout/YEAPAW/Elspet 已发
- llms.txt 更新到 7/3（指南 31→37）+ llms-full.txt 日期更新
- 周复盘：全周 49/50 任务完成，内容 106→114 页，GEO 70→74

### GSC 索引突破分析（7/3）

#### 关键数据
- **索引 14→22（+8）**，6/27 批量抓取触发了 ~14 个旧页面入索引
- 全部是 5-6 月写的旧页，本周新内容（PAA #1-#5、Robot #6-#8）尚未入索引
- **"已发现-尚未编入索引"桶已清零**：Google 已处理所有 sitemap 中的 URL
- **新瓶颈**："已抓取-尚未编入索引" 8 页——Google 已经爬了但决定暂不索引

#### 索引加速的三触发机制（已验证，下周固化到 task_plan.md）

| # | 动作 | 频率 | 机制 |
|:--:|------|------|------|
| 1 | **周五批量改动**：选 3-5 个已索引页面做信号改动（FAQ/对比表/用户原话）→ 一次性 push → 5 分钟内 GSC 重提 sitemap | 每周五 | Google 探测"重要变化"后临时放大抓取预算（6/27 验证：日均 3.8→55 次） |
| 2 | **新内容上线后从已索引页加内链**：首页（6/9 抓取）+ 已索引评测（5/24）+ 已索引指南（6/27）→ 链到新页面 | 每次新内容 | Google 顺着内链从信任页面发现新 URL |
| 3 | **URL Inspection 精准投放**：每天 2 个本周新内容 + 2 个"已抓取-未索引"轮换 + 1 个高价值旧页 | 每天 5 个 | 直接入优先抓取队列，跳过 sitemap 发现→抓取→索引的等待链 |

#### 下周起每周五固定操作（固化到 task_plan.md）

```
周五 4pm:
1. 选 3-5 个已索引页面做信号改动
2. git push
3. GSC 重提 sitemap
4. GA4 周度量 Snapshot
```

#### 5 个未索引原因及修复

| 原因 | 数量 | 修复方案 | 状态 |
|------|:--:|------|:--:|
| 已抓取-尚未编入索引 | 8 | 首页加 8 条内链（7/3 已完成）+ 确认 citation cue | ✅ 已修，等 Google 重抓 |
| 重定向错误 | 3 | 旧尾斜杠 URL，等 Google 重验证 | 🔄 GSC 验证失败 7/1，需重新验证 |
| 网页会自动重定向 | 2 | 同上 | 🔄 |
| 重复-规范网页不同 | 1 | 待查具体 URL 后修复 | ⏳ |
| 已发现-尚未编入索引 | 0 | 已清零 ✅ | ✅ |

---
*每次调研后更新此文件*
