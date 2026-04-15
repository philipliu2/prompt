# PromptWorld - 文生图提示词分享站

## 1. Project Overview

**项目名称**: PromptWorld
**项目类型**: 静态网站 (Single HTML + CSS + JS)
**核心功能**: 展示、浏览和复制文生图提示词
**目标用户**: AI绘图爱好者、设计师、内容创作者

### 2.1 Layout Structure
- **Hero Section**: 全屏渐变背景 + 标题 + 简介
- **Filter Bar**: 风格/场景筛选标签栏
- **Prompt Grid**: 响应式卡片网格布局
- **Admin Panel**: 管理员入口按钮（右上角）+ 模态框编辑界面
- **Footer**: 版权信息 + GitHub链接

### 2.2 Color Palette
- **Primary**: #6366f1 (Indigo)
- **Secondary**: #ec4899 (Pink)
- **Background**: #0f0f23 (Deep Navy)
- **Card BG**: #1a1a2e (Dark Purple)
- **Text Primary**: #ffffff
- **Text Secondary**: #a0a0b0
- **Accent Gradient**: linear-gradient(135deg, #6366f1, #ec4899)

### 2.3 Typography
- **Headings**: "Noto Sans SC", sans-serif (Bold)
- **Body**: "Noto Sans SC", sans-serif (Regular)
- **Code/Prompt**: "JetBrains Mono", monospace

### 2.4 Card Design
- 顶部封面图片 (保持原始宽高比)
- 半透明背景 + 毛玻璃效果 (backdrop-filter: blur)
- 悬停时边框发光效果
- 圆角: 16px
- 内边距: 24px
- **Meta 信息**: 行业 | 来源 | 点击率 | 星级(1-5星)

### 2.5 Grid Layout
- 桌面端: 4列等宽
- 断点: 1200px (3列) / 900px (2列) / 600px (1列)

## 3. Interaction Specification

### 3.1 Core Features
1. **提示词卡片展示**: 封面图 + 标题 + 提示词内容 + 风格标签 + Meta信息(行业/来源/点击率/星级)
2. **一键复制**: 点击复制按钮，将提示词复制到剪贴板
3. **风格筛选**: 按风格（写实、动漫、插画、抽象等）筛选
4. **搜索功能**: 关键词搜索提示词（支持标题、内容、标签、行业、来源）
5. **复制成功反馈**: Toast提示"已复制到剪贴板"
6. **Admin 管理后台**: 点击设置图标打开模态框，可添加/编辑/删除提示词，数据存储在 localStorage

### 3.2 User Interactions
- 卡片悬停: scale(1.02) + 边框发光
- 复制按钮点击: 按钮变为"已复制"状态(2秒后恢复)
- 筛选标签点击: 激活状态 + 过滤显示

## 4. Content Specification

### 4.1 Prompt Categories (风格分类)
1. 写实摄影 (Photorealistic)
2. 动漫风格 (Anime)
3. 数字艺术 (Digital Art)
4. 插画风格 (Illustration)
5. 概念艺术 (Concept Art)
6. 抽象艺术 (Abstract)

### 4.2 Sample Prompts (20个预设提示词)
包含中英文提示词，覆盖不同风格和场景

## 5. Technical Specification

### 5.1 Technology Stack
- **前端**: 纯 HTML + CSS + Vanilla JavaScript
- **字体**: Google Fonts (Noto Sans SC, JetBrains Mono)
- **图标**: Lucide Icons (CDN)
- **部署**: GitHub Pages

### 5.2 File Structure
```
PromptWorld/
├── index.html      (单文件包含所有代码)
└── SPEC.md
```

## 6. Deployment

- 推送到 GitHub 仓库
- 启用 GitHub Pages (main branch)
- 访问地址: https://[username].github.io/PromptWorld/
