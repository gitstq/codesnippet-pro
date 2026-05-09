# 🚀 CodeSnippet Pro

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/React-18+-61DAFB.svg" alt="React">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

<p align="center">
  <b>智能代码片段管理工具</b> - 让代码复用更简单、更智能
</p>

<p align="center">
  <a href="README_EN.md">English</a> | 
  <a href="README_TW.md">繁體中文</a> | 
  <a href="#快速开始">快速开始</a> | 
  <a href="#功能特性">功能特性</a> | 
  <a href="#截图">截图</a>
</p>

---

## 📖 项目介绍

**CodeSnippet Pro** 是一款专为开发者设计的智能代码片段管理工具。它不仅仅是一个代码存储库，更是一个能够理解代码语义、智能推荐、高效组织的智能助手。

### 🎯 解决的核心痛点

- **代码散落各处**：经常写的代码片段散落在各个项目、笔记、Gist中，难以统一管理
- **搜索困难**：传统的关键词搜索无法找到语义相关的代码
- **重复造轮子**：相同功能的代码反复编写，浪费时间
- **团队协作难**：团队成员的优秀代码难以共享和复用

### ✨ 自研差异化亮点

1. **AI语义搜索**：不只是关键词匹配，能理解代码语义，找到真正相关的片段
2. **智能标签提取**：自动分析代码内容，推荐合适的标签
3. **本地优先**：数据存储在本地，保护隐私，响应更快
4. **现代化UI**：简洁美观的界面，流畅的交互体验
5. **多语言支持**：支持20+编程语言的语法高亮和检测

---

## ✨ 核心特性

### 🔍 **智能搜索**
- **全文搜索**：支持标题、代码、描述、标签的全文检索
- **AI语义搜索**：基于代码语义理解，找到相关片段
- **相似推荐**：自动推荐相似的代码片段
- **高级语法**：支持 `language:python tag:web` 等高级搜索语法

### 🏷️ **标签管理**
- **自动标签**：AI自动分析代码，推荐合适的标签
- **层级标签**：支持多级标签分类，灵活组织
- **标签统计**：查看每个标签下的代码数量

### 📁 **集合组织**
- **自定义集合**：按项目、技术栈、用途等维度组织代码
- **拖拽排序**：自由调整集合内代码的顺序
- **批量操作**：支持批量导入导出

### 💾 **数据同步**
- **GitHub Gist**：与GitHub Gist双向同步
- **本地备份**：支持导出为JSON、Markdown格式
- **导入导出**：支持从其他工具导入代码片段

### 📊 **统计分析**
- **使用统计**：查看代码片段的使用频率
- **语言分布**：了解各编程语言的使用占比
- **热门片段**：发现最常用的代码

### 🎨 **其他特性**
- **语法高亮**：支持20+编程语言的语法高亮
- **一键复制**：快速复制代码到剪贴板
- **收藏功能**：标记常用代码，快速访问
- **响应式设计**：支持桌面和移动设备

---

## 🚀 快速开始

### 环境要求

- **Python**: 3.11 或更高版本
- **Node.js**: 18 或更高版本
- **Git**: 用于版本控制

### 安装步骤

#### 1. 克隆仓库

```bash
git clone https://github.com/gitstq/codesnippet-pro.git
cd codesnippet-pro
```

#### 2. 后端设置

```bash
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动后端服务
python -m app.main
```

后端服务将在 `http://localhost:8000` 启动

#### 3. 前端设置

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端将在 `http://localhost:3000` 启动

#### 4. 访问应用

打开浏览器访问 `http://localhost:3000`，开始使用 CodeSnippet Pro！

---

## 📖 详细使用指南

### 创建代码片段

1. 点击左侧"新建片段"按钮
2. 填写标题和代码内容
3. 选择编程语言（或让系统自动检测）
4. 添加描述（可选）
5. 添加标签（支持自动推荐）
6. 点击保存

### 搜索代码

- **普通搜索**：在顶部搜索框输入关键词
- **AI语义搜索**：在搜索页面开启"AI语义"选项
- **高级搜索**：使用语法如 `language:python tag:api`

### 管理标签

- 在"标签"页面查看所有标签
- 创建新片段时，系统会自动推荐标签
- 点击标签可查看该标签下的所有代码

### 创建集合

1. 进入"集合"页面
2. 点击"新建集合"
3. 输入集合名称和描述
4. 将相关代码添加到集合中

---

## 💡 设计思路与迭代规划

### 技术选型原因

- **FastAPI**: 高性能、异步支持、自动生成API文档
- **React + TypeScript**: 类型安全、组件化、生态丰富
- **SQLite**: 轻量级、零配置、适合本地应用
- **Tailwind CSS**: 原子化CSS、快速开发、易于定制

### 后续功能迭代计划

#### v1.1.0 (计划中)
- [ ] VS Code 插件
- [ ] JetBrains 插件
- [ ] 代码片段分享功能
- [ ] 团队协作支持

#### v1.2.0 (计划中)
- [ ] 代码执行功能（沙箱环境）
- [ ] 代码模板市场
- [ ] AI代码生成集成
- [ ] 多语言界面支持

#### v2.0.0 (规划中)
- [ ] 云端同步服务
- [ ] 移动端App
- [ ] 企业版功能
- [ ] API开放平台

### 社区贡献方向

- 提交Bug报告和功能建议
- 贡献代码片段模板
- 完善文档和教程
- 开发插件和扩展

---

## 📦 打包与部署

### 开发模式

```bash
# 后端
cd backend
python -m app.main

# 前端
cd frontend
npm run dev
```

### 生产构建

```bash
# 前端构建
cd frontend
npm run build

# 构建产物在 frontend/dist 目录
```

### Docker 部署

```dockerfile
# 构建镜像
docker build -t codesnippet-pro .

# 运行容器
docker run -p 8000:8000 -v $(pwd)/data:/app/data codesnippet-pro
```

---

## 🤝 贡献指南

我们欢迎各种形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### 贡献方式

1. **提交 Issue**: 报告Bug或提出功能建议
2. **提交 PR**: 修复Bug或实现新功能
3. **完善文档**: 帮助改进文档和教程
4. **分享推广**: 将项目分享给更多开发者

### 代码规范

- 遵循 PEP 8 (Python) 和 ESLint (TypeScript) 规范
- 编写清晰的提交信息
- 添加必要的测试用例
- 更新相关文档

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

```
MIT License

Copyright (c) 2026 CodeSnippet Pro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 致谢

感谢以下开源项目和工具的支持：

- [FastAPI](https://fastapi.tiangolo.com/) - 现代、快速的Web框架
- [React](https://react.dev/) - 用于构建用户界面的JavaScript库
- [Tailwind CSS](https://tailwindcss.com/) - 实用优先的CSS框架
- [Prism.js](https://prismjs.com/) - 轻量级语法高亮库

---

## 📞 联系我们

- **GitHub Issues**: [提交问题](https://github.com/gitstq/codesnippet-pro/issues)
- **Email**: codesnippet@example.com

---

<p align="center">
  Made with ❤️ by CodeSnippet Pro Team
</p>

<p align="center">
  ⭐ Star 我们，让更多人发现这个工具！
</p>