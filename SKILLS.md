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
| `review` | PR 审查 | ✅ 内置 |
| `micro-saas-launcher` | 商业策略/规模化 | ✅ 内置 |
| `news-monitor` | 行业动态监测 | ✅ 内置 |

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
Pinterest → 手动设计 Pin 图
Reddit   → agent-browser（浏览社区/发布）
Medium   → 手动交叉发布
```

### 阶段 9：多语言
```
翻译     → 手动（Claude 翻译初稿 + 人工校对）
前端调整 → frontend-design（语言切换 UI）
```

### 阶段 10：规模化
```
商业策略 → micro-saas-launcher
行业趋势 → news-monitor
内容生产 → seo-content-optimizer + agent-browser
```

---

## 调用优先级

1. **开始任何工作前** → `planning-with-files-zh`（读取当前计划）
2. **写内容/做 SEO 前** → `seo-content-optimizer`
3. **浏览器操作（Amazon/验证页面）** → `agent-browser`
4. **设计/UI 调整** → `frontend-design`
5. **改完代码** → `verify`（构建 + 验证）
6. **质量检查** → `simplify`
7. **启动项目** → `run`

## 注意事项
- 不要在所有阶段同时调用所有 skill，按需调用
- `planning-with-files-zh` 是基础，每次会话第一步就调用
- Amazon 调研始终用 `agent-browser`，不用 WebFetch（被拦截）
- SEO 优化在新内容写作前调用 `seo-content-optimizer`
- 设计改动始终用 `frontend-design`（保持 Forest+Honey 风格一致）
