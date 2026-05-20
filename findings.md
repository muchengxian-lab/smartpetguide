# 发现与决策

## 需求
- 英文为主的宠物智能设备评测/推荐内容站
- 联盟营销（Amazon Associates）+ 广告变现
- 碎片化时间操作，每天 1-3 小时

## 研究发现

### 市场数据
- Pet Tech 全球市场 $7.5B → $18B（CAGR 19%）
- Google Trends 2026：智能宠物设备搜索量 5 年持续上涨
- 猫砂盆品类佣金最高：$50-100/单（Litter-Robot 等 $500+ 产品）
- 自动喂食器搜索量最大：月搜 8,000+（"best automatic cat feeder"）

### 竞品分析
- 大站占据品类大词（KD 35-38），新站需从长尾品种词（KD 5-8）切入
- 对比词（"A vs B"）流量精准、竞争低，转化率最高
- 品种推荐词零竞争："best feeder for French Bulldog"（月搜 200，KD 5）

### 关键词数据（关键发现）
| 层级 | 例子 | 月搜量 | KD | 策略 |
|------|------|--------|-----|------|
| 品类大词 | "best automatic cat feeder" | 8,000 | 35 | 第4月做 |
| 对比词 | "Furbo vs Petcube" | 1,500 | 18 | 第2月做 |
| 长尾品种词 | "best feeder for french bulldog" | 200 | 5 | 第1周就做 |

## 技术决策
| 决策 | 理由 |
|------|------|
| Astro 5 纯静态生成 | 加载速度 <2s，Vercel 免费层，SEO 友好 |
| Tailwind CSS v3 | 轻量，快速开发，无需额外 CSS 框架 |
| 产品数据集中 `products.json` | 15款产品参数统一管理，组件化引用 |
| SVG 占位图 → SiteStripe 替换 | 避免版权风险，AA 通过后立即替换 |
| 子目录多语言（/es/, /de/） | 比子域名更利于主域权重积累 |
| 不做主动外链前3个月 | 新站先积累内容质量，避免 Google 惩罚 |

## 当前状态（2026-05-20）

### 基础设施
- 域名：smartpetguide.net（阿里云, A 记录 → 76.76.21.21）
- 部署：Vercel 静态，HTTPS 自动签发
- GA4：G-DKYRD8PSCT ✅
- GSC：域名已验证，sitemap 待 DNS 刷新后提交
- Amazon Associates：smartpetgui0a-20（2026-05-20 提交，审核中 ~3h，预计 24-48h 出结果）
- Pinterest：企业账号，网站已验证
- Reddit：u/Additional_Diver3250

### 已发布内容（19 页）
1. 首页 `index.astro` — 最新推荐 + 分类入口
2. 猫砂盆 Best 列表 — "Best Self-Cleaning Litter Boxes 2026"
3. 喂食器 Best 列表 — "Best Automatic Cat Feeders 2026"
4. Litter-Robot 4 评测
5. Petlibro Granary 评测
6. WOPET Automatic 评测
7. DOGNESS Mini 评测
8. Leo's Loo Too 评测
9. PetSafe ScoopFree 评测
10. Litter-Robot 4 vs Leo's Loo Too 对比
11. Automatic vs Manual Litter Box 对比
12. 喂食器购买指南
13. 猫砂盆购买指南
14. French Bulldog 品种推荐
15-19. About / Privacy / Affiliate Disclosure / 404 / RSS

### 产品数据库
15款产品，5个品类：猫砂盆(5)、喂食器(4)、饮水机(3)、摄像头(2)、GPS(1)

## 视觉/浏览器发现
<!-- 关键：每执行2次查看/浏览器操作后必须更新此部分 -->
- smartpetguide.net 线上可访问，首页加载正常
- SVG 占位图在部署后正常显示
- Vercel 部署秒级生效
- **2026-05-20 重设计**：Forest + Honey 编辑杂志风，Fraunces + Atkinson Hyperlegible 字体
  - 配色：cream #FDF9F3 / forest #1A3C34 / honey #D4914B / sage #E9EFE8
  - 首页、评测页、Best列表、对比页、指南页、品种页全部刷新
  - favicon.svg 已修复

## 设计系统（2026-05-20 重设计）
| 元素 | 选择 | 理由 |
|------|------|------|
| 色调 | Forest + Honey（深绿+琥珀） | 温暖、专业、宠物友好，非AI感 |
| 标题字体 | Fraunces（Google Fonts） | 有特色的编辑体，温暖不冷漠 |
| 正文字体 | Atkinson Hyperlegible | 高可读性、独特、非通用字体 |
| 卡片 | 圆角2xl + 浅色边框 + hover阴影 | 柔和有层次，不僵硬 |
| 按钮 | 琥珀色圆角 + hover变深 + active微缩放 | 有反馈感，引导点击 |
| 页脚 | 深绿底白字 | 对比分明，收尾稳重 |
| 背景纹理 | SVG噪声叠加 opacity 3% | 微妙的纸张质感 |

## 资源
- [原始完整计划](C:\Users\Administrator\.claude\plans\lucky-floating-flame.md)
- [项目记忆](C:\Users\Administrator\.claude\projects\C--Users-Administrator\memory\smartpetguide_project.md)

---
*每执行2次查看/浏览器/搜索操作后更新此文件*
*防止视觉信息丢失*
