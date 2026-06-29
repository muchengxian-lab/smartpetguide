# Amazon Affiliate Conversion Log

> Task A 后台基建 — 审核日期：2026-06-29

## 全局状态

| 检查项 | 状态 |
|------|:--:|
| 全部 products.json amazonUrl 含 `tag=smartpetgui0a-20` | ✅ |
| 全部页面模板 `rel="sponsored"` | ✅ |
| Review 模板有 affiliate disclosure | ✅ |
| Best 模板有 affiliate disclosure | 待确认 |
| Compare 模板有 affiliate disclosure | 待确认 |
| Guide 模板有联盟链接 | ❌ 零链接 |
| GA4 affiliate_click 事件 | 待确认 |
| GA4 outbound_click 事件 | ✅ 已配置 |

## 目标页面逐页审核

| # | Page | Type | Has tag | rel=sponsored | CTA count | Issue | Action |
|---|------|------|:--:|:--:|:--:|------|------|
| 1 | `/compare/lr5-vs-amazon-basics-cost/` | Compare | ✅ | ✅ | 2+ | LR5 用搜索 URL（非直接 ASIN） | 确认 ASIN，改直接链接 |
| 2 | `/reviews/litter-robot-5-review/` | Review | ✅ | ✅ | 2 | LR5 用搜索 URL | 同 #1 |
| 3 | `/reviews/amazon-basics-litter-box-review/` | Review | ✅ | ✅ | 2 | — | 已有 verdict + CTA ✅ |
| 4 | `/reviews/petlibro-granary-review/` | Review | ✅ | ✅ | 2 | — | 已有 verdict + CTA ✅ |
| 5 | `/compare/wopet-vs-petlibro/` | Compare | ✅ | ✅ | 2+ | — | 待加决策模块 |
| 6 | `/best/pet-cameras-no-subscription/` | Best | ✅ | ✅ | 1+/产品 | — | 待加决策模块 |
| 7 | `/guides/best-no-subscription-cameras/` | Guide | N/A | N/A | **0** | 指南页零联盟链接 | 加底部 CTA |
| 8 | `/reviews/aorkuler-gps-review/` | Review | ✅ | ✅ | 2 | — | 已有 verdict + CTA ✅ |
| 9 | `/best/gps-trackers-no-monthly-fee/` | Best | ✅ | ✅ | 1+/产品 | — | 待加决策模块 |
| 10 | `/guides/are-automatic-feeders-worth-it-for-one-cat/` | Guide | N/A | N/A | **0** | 指南页零联盟链接 | 加底部 CTA |

## 发现总结

### 已合规（无需改动）
- 全部 26 款产品 `amazonUrl` 含 `tag=smartpetgui0a-20`
- 全部 Review/Compare/Best 模板已用 `rel="nofollow sponsored noopener"`
- Review 模板底部有完整 affiliate disclosure

### 待修复
1. **LR5 产品用搜索 URL** (`/s?k=litter+robot+5`) 而非直接 ASIN 链接 — 降低点击到购买转化率
2. **2 篇指南页零联盟链接** — 目标页面 #7 和 #10 完全无变现路径
3. **Compare/Best 页面缺「Buy if / Skip if / Best alternative」决策模块** — 页面 #1, #5, #6, #9 待添加

### 设计决策
- 指南页的 CTA 应放在底部（跟 review 模板一致），不应在正文中插入
- 决策模块格式：`Buy if: ... / Skip if: ... / Best alternative: ...`
- Compare 页已有 verdict 段落，决策模块可放在每个产品卡片内

## D2-D3 执行计划

| 优先级 | 页面 | 动作 |
|:--:|------|------|
| 1 | `/reviews/petlibro-granary-review/` | 加决策模块（已有 verdict，加 Buy if/Skip if/Best alternative） |
| 2 | `/reviews/aorkuler-gps-review/` | 加决策模块 |
| 3 | `/reviews/amazon-basics-litter-box-review/` | 加决策模块 |
| 4 | `/compare/lr5-vs-amazon-basics-cost/` | 加决策模块 + 确认 LR5 ASIN |
| 5 | `/compare/wopet-vs-petlibro/` | 加决策模块 |
| 6 | `/best/pet-cameras-no-subscription/` | 加顶部决策摘要 |
| 7 | `/best/gps-trackers-no-monthly-fee/` | 加顶部决策摘要 |
| 8 | `/guides/best-no-subscription-cameras/` | 加底部 CTA |
| 9 | `/guides/are-automatic-feeders-worth-it-for-one-cat/` | 加底部 CTA |
| 10 | `/reviews/litter-robot-5-review/` | LR5 ASIN 修复（等确认） |
