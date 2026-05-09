# 🚀 CodeSnippet Pro

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/React-18+-61DAFB.svg" alt="React">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

<p align="center">
  <b>智能程式碼片段管理工具</b> - 讓程式碼複用更簡單、更智能
</p>

<p align="center">
  <a href="README.md">简体中文</a> | 
  <a href="README_EN.md">English</a> | 
  <a href="#快速開始">快速開始</a> | 
  <a href="#功能特性">功能特性</a> | 
  <a href="#截圖">截圖</a>
</p>

---

## 📖 專案介紹

**CodeSnippet Pro** 是一款專為開發者設計的智能程式碼片段管理工具。它不僅僅是一個程式碼儲存庫，更是一個能夠理解程式碼語義、智能推薦、高效組織的智能助手。

### 🎯 解決的核心痛點

- **程式碼散落各處**：經常寫的程式碼片段散落在各個專案、筆記、Gist中，難以統一管理
- **搜尋困難**：傳統的關鍵詞搜尋無法找到語義相關的程式碼
- **重複造輪子**：相同功能的程式碼反覆編寫，浪費時間
- **團隊協作難**：團隊成員的優秀程式碼難以共享和複用

### ✨ 自研差異化亮點

1. **AI語義搜尋**：不只是關鍵詞匹配，能理解程式碼語義，找到真正相關的片段
2. **智能標籤提取**：自動分析程式碼內容，推薦合適的標籤
3. **本地優先**：資料儲存在本地，保護隱私，響應更快
4. **現代化UI**：簡潔美觀的介面，流暢的互動體驗
5. **多語言支援**：支援20+程式語言的語法高亮和檢測

---

## ✨ 核心特性

### 🔍 **智能搜尋**
- **全文搜尋**：支援標題、程式碼、描述、標籤的全文檢索
- **AI語義搜尋**：基於程式碼語義理解，找到相關片段
- **相似推薦**：自動推薦相似的程式碼片段
- **高級語法**：支援 `language:python tag:web` 等高級搜尋語法

### 🏷️ **標籤管理**
- **自動標籤**：AI自動分析程式碼，推薦合適的標籤
- **層級標籤**：支援多級標籤分類，靈活組織
- **標籤統計**：查看每個標籤下的程式碼數量

### 📁 **集合組織**
- **自定義集合**：按專案、技術棧、用途等維度組織程式碼
- **拖曳排序**：自由調整集合內程式碼的順序
- **批次操作**：支援批次匯入匯出

### 💾 **資料同步**
- **GitHub Gist**：與GitHub Gist雙向同步
- **本地備份**：支援匯出為JSON、Markdown格式
- **匯入匯出**：支援從其他工具匯入程式碼片段

### 📊 **統計分析**
- **使用統計**：查看程式碼片段的使用頻率
- **語言分布**：了解各程式語言的使用占比
- **熱門片段**：發現最常用的程式碼

### 🎨 **其他特性**
- **語法高亮**：支援20+程式語言的語法高亮
- **一鍵複製**：快速複製程式碼到剪貼簿
- **收藏功能**：標記常用程式碼，快速訪問
- **響應式設計**：支援桌面和移動設備

---

## 🚀 快速開始

### 環境要求

- **Python**: 3.11 或更高版本
- **Node.js**: 18 或更高版本
- **Git**: 用於版本控制

### 安裝步驟

#### 1. 複製倉庫

```bash
git clone https://github.com/gitstq/codesnippet-pro.git
cd codesnippet-pro
```

#### 2. 後端設定

```bash
cd backend

# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安裝依賴
pip install -r requirements.txt

# 啟動後端服務
python -m app.main
```

後端服務將在 `http://localhost:8000` 啟動

#### 3. 前端設定

```bash
cd frontend

# 安裝依賴
npm install

# 啟動開發伺服器
npm run dev
```

前端將在 `http://localhost:3000` 啟動

#### 4. 訪問應用

開啟瀏覽器訪問 `http://localhost:3000`，開始使用 CodeSnippet Pro！

---

## 📖 詳細使用指南

### 建立程式碼片段

1. 點擊左側"新建片段"按鈕
2. 填寫標題和程式碼內容
3. 選擇程式語言（或讓系統自動檢測）
4. 添加描述（可選）
5. 添加標籤（支援自動推薦）
6. 點擊儲存

### 搜尋程式碼

- **普通搜尋**：在頂部搜尋框輸入關鍵詞
- **AI語義搜尋**：在搜尋頁面開啟"AI語義"選項
- **高級搜尋**：使用語法如 `language:python tag:api`

### 管理標籤

- 在"標籤"頁面查看所有標籤
- 建立新片段時，系統會自動推薦標籤
- 點擊標籤可查看該標籤下的所有程式碼

### 建立集合

1. 進入"集合"頁面
2. 點擊"新建集合"
3. 輸入集合名稱和描述
4. 將相關程式碼添加到集合中

---

## 💡 設計思路與迭代規劃

### 技術選型原因

- **FastAPI**: 高效能、非同步支援、自動生成API文件
- **React + TypeScript**: 型別安全、元件化、生態豐富
- **SQLite**: 輕量級、零配置、適合本地應用
- **Tailwind CSS**: 原子化CSS、快速開發、易於定製

### 後續功能迭代計劃

#### v1.1.0 (計劃中)
- [ ] VS Code 外掛
- [ ] JetBrains 外掛
- [ ] 程式碼片段分享功能
- [ ] 團隊協作支援

#### v1.2.0 (計劃中)
- [ ] 程式碼執行功能（沙箱環境）
- [ ] 程式碼模板市場
- [ ] AI程式碼生成整合
- [ ] 多語言介面支援

#### v2.0.0 (規劃中)
- [ ] 雲端同步服務
- [ ] 移動端App
- [ ] 企業版功能
- [ ] API開放平台

### 社群貢獻方向

- 提交Bug報告和功能建議
- 貢獻程式碼片段模板
- 完善文件和教程
- 開發外掛和擴充套件

---

## 📦 打包與部署

### 開發模式

```bash
# 後端
cd backend
python -m app.main

# 前端
cd frontend
npm run dev
```

### 生產建構

```bash
# 前端建構
cd frontend
npm run build

# 建構產物在 frontend/dist 目錄
```

### Docker 部署

```dockerfile
# 建構映象
docker build -t codesnippet-pro .

# 執行容器
docker run -p 8000:8000 -v $(pwd)/data:/app/data codesnippet-pro
```

---

## 🤝 貢獻指南

我們歡迎各種形式的貢獻！請檢視 [CONTRIBUTING.md](CONTRIBUTING.md) 了解詳情。

### 貢獻方式

1. **提交 Issue**: 報告Bug或提出功能建議
2. **提交 PR**: 修復Bug或實現新功能
3. **完善文件**: 幫助改進文件和教程
4. **分享推廣**: 將專案分享給更多開發者

### 程式碼規範

- 遵循 PEP 8 (Python) 和 ESLint (TypeScript) 規範
- 編寫清晰的提交資訊
- 新增必要的測試用例
- 更新相關文件

---

## 📄 開源協議

本專案採用 [MIT License](LICENSE) 開源協議。

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

## 🙏 致謝

感謝以下開源專案和工具的支援：

- [FastAPI](https://fastapi.tiangolo.com/) - 現代、快速的Web框架
- [React](https://react.dev/) - 用於構建使用者介面的JavaScript庫
- [Tailwind CSS](https://tailwindcss.com/) - 實用優先的CSS框架
- [Prism.js](https://prismjs.com/) - 輕量級語法高亮庫

---

## 📞 聯絡我們

- **GitHub Issues**: [提交問題](https://github.com/gitstq/codesnippet-pro/issues)
- **Email**: codesnippet@example.com

---

<p align="center">
  Made with ❤️ by CodeSnippet Pro Team
</p>

<p align="center">
  ⭐ Star 我們，讓更多人發現這個工具！
</p>