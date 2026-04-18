# PromptWorld - AI 提示词分享平台

## 1. Project Overview

**项目名称**: PromptWorld
**项目类型**: 静态网站 (Single HTML + CSS + JS)
**核心功能**: 展示、浏览、复制文生图提示词，支持提示词录入和 AI 优化
**目标用户**: AI绘图爱好者、设计师、内容创作者
**部署方式**: GitHub Pages

---

## 2. Visual Specification

### 2.1 Layout Structure

| 页面 | 功能 |
|------|------|
| **首页** | 瀑布流展示提示词卡片，支持筛选、搜索 |
| **详情页** | 全屏展示卡片大图 + 完整提示词信息 |
| **管理后台** | 录入、编辑、删除提示词 |

### 2.2 Color Palette

| 用途 | 色值 |
|------|------|
| 背景 | `#F0F0F3` |
| 卡片背景 | `#FFFFFF` |
| 主色 | `#6366F1` |
| 辅助色 | `#EC4899` |
| 成功色 | `#22C55E` |
| 警告色 | `#F59E0B` |
| 星星色 | `#FBBF24` |
| 主文字 | `#1A1A1A` |
| 次文字 | `#666666` |
| 三级文字 | `#999999` |
| 边框 | `#E5E5E5` |

**Dark Mode**
- 背景: `#0F0F0F`
- 卡片: `#1A1A1A`
- 文字: `#FFFFFF`

### 2.3 Typography

- **主字体**: Inter (Google Fonts)
- **代码字体**: JetBrains Mono (Google Fonts)
- **中文字体**: Noto Sans SC fallback

### 2.4 Card Design (首页瀑布流卡片)

```
┌─────────────────────────────┐
│                             │
│         [图片动态高度]         │  ← 固定宽度，图片保持原始比例
│                             │
├─────────────────────────────┤
│ 标题（单行省略）        ❤️123 │  ← Row 1 + 点赞数
├─────────────────────────────┤
│ #标签1 #标签2 #标签3          │  ← Row 2
├─────────────────────────────┤
│ 行业 · 来源 · 点击率 · ★★★☆☆ │  ← Row 3
└─────────────────────────────┘
```

- 卡片宽度: 固定 280px
- 瀑布流布局，图片高度根据原始宽高比动态计算
- 间距: 16px
- 圆角: 12px
- 阴影: 0 1px 3px rgba(0,0,0,0.08)
- 悬停: 0 8px 30px rgba(0,0,0,0.12) + translateY(-2px)

### 2.5 Detail Page (详情页)

```
┌────────────────────────────────────────────────────────────┐
│  [← 返回]                               [☀/☽] [⚙ 管理]     │
├────────────────────────────────────────────────────────────┤
│                         │                                   │
│                         │  赛博朋克都市夜景                    │
│                         │  #夜景 #霓虹 #未来城市               │
│      [大图展示]          │  ─────────────────────           │
│      保持原始比例        │  行业: 建筑设计                     │
│                         │  来源: Midjourney                  │
│                         │  点击率: 8.2%  星级: ★★★★★  ❤️ 123 │
│                         │  ─────────────────────           │
│                         │  【原始提示词】                     │
│                         │  Cyberpunk cityscape at night,    │
│                         │  neon-lit skyscrapers...           │
│                         │  ─────────────────────           │
│                         │  【优化后提示词】 ⭐AI优化           │
│                         │  赛博朋克夜景, 霓虹灯高楼, 雨天街道, │
│                         │  科幻车辆, 全息广告, 电影光效        │
│                         │  ─────────────────────           │
│                         │  [📋 复制原始] [📋 复制优化]        │
└────────────────────────────────────────────────────────────┘
```

- 左侧 50%: 图片展示，保持原始宽高比，最大高度 80vh
- 右侧 50%: 提示词信息，垂直滚动
- 响应式: 移动端上下布局

### 2.6 Admin Panel (管理后台)

```
┌─────────────────────────────────────────────┐
│  管理后台                              [✕]   │
├─────────────────────────────────────────────┤
│  [列表]  [添加]                              │
├─────────────────────────────────────────────┤
│  ┌─────────────────────────────────────┐    │
│  │ 封面图片上传                          │    │
│  │ [拖拽或点击上传 / 粘贴图片 / 输入URL]   │    │
│  │ 支持 JPG, PNG, 或图片URL              │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  标题: [________________] ⭐必填            │
│                                             │
│  原始提示词: [________________________]    │
│             [________________________] ⭐必填│
│                                             │
│  图片类型: [____]  作者: [________]         │
│  行业: [________]                           │
│                                             │
│  [🤖 AI 自动优化]  [🤖 AI 自动生成标签]      │
│                                             │
│  优化后提示词: [________________________]   │
│               [________________________]    │
│                                             │
│  标签: [标签1, 标签2, 标签3] (AI生成)        │
│                                             │
│  点击率: [____]  星级: [★ ★ ★ ★ ★]        │
│                                             │
│  [保存]  [删除]                              │
└─────────────────────────────────────────────┘
```

---

## 3. Functionality Specification

### 3.1 Core Features

| 功能 | 描述 |
|------|------|
| **瀑布流展示** | 固定宽度卡片，图片高度根据原始比例动态调整 |
| **风格筛选** | 按 6 种风格分类筛选提示词 |
| **关键词搜索** | 搜索标题、标签、行业、来源 |
| **一键复制** | 复制原始提示词或优化后提示词 |
| **点赞功能** | 点击心形图标点赞/取消点赞，显示点赞数 |
| **详情页** | 点击卡片进入详情，展示完整信息 |
| **Dark Mode** | 浅色/深色主题切换 |
| **管理后台** | 添加/编辑/删除提示词 |
| **AI 优化** | 自动生成结构化精简的优化提示词 |
| **AI 生成标签** | 根据提示词内容自动生成相关标签 |

### 3.2 User Interactions

| 交互 | 行为 |
|------|------|
| 点击卡片 | 跳转到详情页 |
| 点击复制按钮 | 复制提示词，显示"已复制"反馈 |
| 筛选标签点击 | 过滤显示对应分类 |
| 搜索输入 | 实时搜索，300ms 防抖 |
| 悬停卡片 | 轻微上浮 + 阴影加深 |

### 3.3 Data Model

```javascript
{
  id: Number,           // 唯一ID
  title: String,        // 标题 ⭐必填
  category: String,     // 情绪氛围: fresh/active/humor/professional/cozy/relaxed/healing/luxurious/cool/romantic
  imageType: String,    // 图片类型: 人物写实/场景写实/动漫图/信息图/插画图/海报图/创意图
  image: String,        // 图片URL或Base64 (粘贴上传自动转Base64)
  imageWidth: Number,    // 图片原始宽度 (用于瀑布流高度计算)
  imageHeight: Number,  // 图片原始高度
  source: String,       // 作者/创作者名字
  industry: String,     // 广告主行业: 游戏/网服/教育/金融/旅游/家装等
  clickRate: String,    // 点击率: "8.5%"
  rating: Number,       // 星级: 1-5
  likes: Number,        // 点赞数
  likedByMe: Boolean,   // 我是否点赞过 (本地存储)
  tags: String[],       // 标签数组
  text: String,         // 原始提示词 ⭐必填
  textOptimized: String, // AI优化后的提示词
  createdAt: Number     // 创建时间戳
}
```

### 3.4 Storage

- **前端存储**: localStorage
- **Key**: `promptworld_prompts`
- **容量**: 约 2MB (适合少量数据)

---

## 4. Content Specification

### 4.1 Mood/Style (情绪氛围)

| Key | 中文名 | 英文名 |
|-----|--------|--------|
| fresh | 清新 | Fresh |
| active | 活泼 | Active |
| humor | 幽默 | Humor |
| professional | 专业 | Professional |
| cozy | 温馨 | Cozy |
| relaxed | 松弛 | Relaxed |
| healing | 治愈 | Healing |
| luxurious | 高端 | Luxurious |
| cool | 酷炫 | Cool |
| romantic | 浪漫 | Romantic |

### 4.2 Image Types (图片类型)

| 中文名 | 说明 |
|--------|------|
| 人物写实 | Photorealistic Portrait |
| 场景写实 | Photorealistic Scene/Landscape |
| 动漫图 | Anime/Cartoon |
| 信息图 | Infographic |
| 插画图 | Illustration |
| 海报图 | Poster |
| 创意图 | 概念/抽象/数字艺术等 Creative |

### 4.3 Industries (行业) - 广告主行业

游戏、网服、教育、金融、旅游、家装、电商、快消、美妆、医美、汽车、房产、娱乐、资讯、科技

---

## 5. Technical Specification

### 5.1 Technology Stack

| 技术 | 用途 |
|------|------|
| HTML5 | 页面结构 |
| CSS3 | 样式、瀑布流布局 |
| Vanilla JS | 交互逻辑 |
| Google Fonts | Inter + JetBrains Mono |
| Lucide Icons | 图标库 (CDN) |
| localStorage | 数据持久化 |

### 5.2 File Structure

```
PromptWorld/
├── index.html      # 单文件应用 (HTML + CSS + JS)
└── SPEC.md         # 产品规格文档
```

### 5.3 Waterfall Layout

```javascript
// CSS Grid 实现瀑布流
.prompt-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  grid-auto-rows: 10px;  // 最小单位
}

// JS 计算每张卡片占据的行数
cardRowSpan = Math.ceil((cardImageHeight + otherElementsHeight) / rowHeight);
```

---

## 6. Page Routes

| 页面 | URL 参数 | 说明 |
|------|----------|------|
| 首页 | `/` | 瀑布流展示 |
| 详情页 | `/?detail=id` | 显示指定提示词详情 |

---

## 7. TODO

- [ ] 实现瀑布流布局
- [ ] 实现详情页
- [ ] 实现图片上传 (URL/粘贴)
- [ ] 实现点赞功能
- [ ] 实现 AI 优化提示词功能
- [ ] 实现 AI 生成标签功能
- [ ] 更新管理后台表单
- [ ] 响应式适配
