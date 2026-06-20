# Skills 使用规范 — SmartPetGuide

## 已配置 Skills

| Skill | 用途 | 安装 |
|------|------|------|
| `planning-with-files-zh` | 项目计划/进度/调研文件管理 | ✅ |
| `frontend-design` | 前端设计（Forest+Honey 编辑风） | ✅ 内置 |
| `agent-browser` | 浏览器自动化（Amazon 调研/页面验证） | ✅ |
| `seo-content-optimizer` | SEO 内容优化（关键词/可读性/竞品） | ✅ |
| `article-content` | 长文写作（评测/指南/列表） | ✅ 新装 |
| `copywriting` | 短文案（标题/CTA/转化文案） | ✅ 新装 |
| `affiliate-marketing` | 联盟营销策略（佣金/转化） | ✅ 新装 |
| `verify` | 代码变更验证（改完即验） | ✅ 内置 |
| `run` | 启动开发服务器 | ✅ 内置 |
| `simplify` | 代码审查/重构/质量检查 | ✅ 内置 |
| `baoyu-imagine` | AI 图片生成（Pin 图/社交图/OG 图） | ✅ 新装 |
| `image-optimization` | 图片压缩/WebP/SEO 优化 | ✅ 新装 |
| `baoyu-infographic` | 信息图生成（Pinterest 引流） | ✅ 新装 |
| `baoyu-translate` | 多语言翻译（精翻/快翻/校对） | ✅ 新装 |
| `superpowers` | 完整 SDLC 工作流（规划→执行→审查→TDD→调试） | ✅ 新装 |
| `claude-mem` | 跨会话持久记忆（SQLite+向量检索） | ✅ 新装 |
| `cold-start-strategy` | 冷启动策略框架（产品→渠道→节奏） | ✅ |
| `pinterest-posts` | Pinterest Pin 创建/优化（Board SEO+Alt text） | ✅ |
| `traffic-analysis` | 流量来源分析/归因/渠道对比 | ✅ |
| `geo-skills` | GEO 全站审计（22技能：可引用度/品牌/技术/Schema） | ✅ 新装 |
| `aaron-seo-geo` | 20个SEO+GEO技能（关键词→内容→Schema→审计→监控） | ✅ 新装 |
| `qwoted-seo-backlinks` | Qwoted PR 外链：搜记者提问→建统计页→写 pitch→提交 | ✅ 6/20 |

---

## 按阶段使用

### 阶段 4-5：内容冲刺
```
写文章前  → seo-content-optimizer（关键词分析）
写文章    → article-content（长文评测/指南/列表）
写标题    → copywriting（标题/CTA/转化文案）
调研产品  → agent-browser（Amazon 搜索/BSR）
写完验证  → verify（构建 + 页面抽查）
变现策略  → affiliate-marketing（佣金/转化优化）
规划管理  → planning-with-files-zh（更新 task_plan.md）
代码改动  → superpowers:brainstorm → superpowers:write-plan → superpowers:execute-plan（结构化开发）
记忆持久  → claude-mem（后台自动运行，跨会话记住上下文）
```

### 阶段 6-7：数据分析 + 优化
```
GSC 分析  → 手动 + findings.md 记录
SEO 优化  → seo-content-optimizer（内容评分/竞品对比）
代码重构  → simplify（代码质量检查）
```

### 阶段 7：GEO + Schema
```
Schema   → 手动编写（Review/Article/FAQ）
前端调整 → frontend-design（Key Takeaways 样式/布局）
验证     → verify + run
```

### 阶段 8：社交引流
```
Pinterest → baoyu-imagine（Pin 图生成）+ baoyu-infographic（信息图）
Reddit   → agent-browser（浏览社区/发布）
Medium   → 手动交叉发布
```

### 阶段 9：多语言
```
翻译     → baoyu-translate（精翻模式，保持术语一致性）
前端调整 → frontend-design（语言切换 UI）
```

### 阶段 10：规模化
```
商业策略 → validate-idea（模式验证）
内容生产 → seo-content-optimizer + agent-browser
图片优化 → image-optimization（WebP/压缩/LCP）
```

---

## 调用优先级

1. **开始任何工作前** → `planning-with-files-zh`（读取当前计划）
2. **任何代码改动** → `superpowers:brainstorm` → `superpowers:write-plan` → `superpowers:execute-plan`
3. **写内容/做 SEO 前** → `seo-content-optimizer`
4. **浏览器操作（Amazon/验证页面）** → `agent-browser`
5. **设计/UI 调整** → `frontend-design`
6. **改完代码** → `verify`（构建 + 验证）
7. **质量检查** → `simplify`
8. **启动项目** → `run`

> `claude-mem` 在后台自动运行（SessionStart/Stop 钩子），无需手动调用，跨会话自动注入历史上下文。

## 注意事项
- 不要在所有阶段同时调用所有 skill，按需调用
- `planning-with-files-zh` 是基础，每次会话第一步就调用
- Amazon 调研始终用 `agent-browser`，不用 WebFetch（被拦截）
- SEO 优化在新内容写作前调用 `seo-content-optimizer`
- 设计改动始终用 `frontend-design`（保持 Forest+Honey 风格一致）
