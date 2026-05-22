# 发现与决策

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
- smartpetguide.net 线上可访问，**50 页**正常
- 新增 3 篇对比文：Pioneer Pet vs YEAPAW / xpai vs eufy / PETKIT vs Catit PIXI
- 对比文从 6 → 9 篇，覆盖全部 5 个品类
- 产品图片替换为 Amazon 高清原图后，文章视觉效果大幅提升
- 对比页双卡 + 图片布局在桌面端并排、移动端堆叠
- Amazon 商品页结构稳定，#landingImage + data-old-hires 可可靠提取图片

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

## GSC 数据（2026-05-21 → 2026-05-22）
- 站点地图：✅ 成功提交，17 URL 已发现，上次读取 5/21
- 效果数据：⏳ 处理中（5/22 检查仍无数据）
- 索引编制：⏳ 处理中
- site: 搜索实测：3 页已索引（首页 + Petlibro 评测 + 猫砂盆指南），Petlibro 评测 5/21 14:00 被收录
- Google 提示有更多相似结果被省略，实际索引量估计 3-10 页
- 结论：新域名 3 天，索引刚起步，完全正常。预计 Week 2-3 达 50-80% 索引率

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

### AI 搜索优化路径
| 阶段 | 时间 | 行动 |
|------|------|------|
| 短期 | 0-3月 | Schema+结构化摘要已做 ✅，聚焦传统Google SEO |
| 中期 | 3-6月 | Reddit外链积累→被其他站引用→进入AI引用池 |
| 长期 | 6-12月 | 品类权威建立→AI+Google双渠道 |

### 与 Google Trends 验证的联动
- Google 搜索（文字链接）仍是主力流量来源
- AI 搜索是新渠道但需要权威信号积累
- **当前策略：传统 SEO 优先 + AI 优化打好基础（Schema/结构化数据）**

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

---
*每次调研后更新此文件*
