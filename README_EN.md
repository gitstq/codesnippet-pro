# 🚀 CodeSnippet Pro

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/React-18+-61DAFB.svg" alt="React">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

<p align="center">
  <b>Intelligent Code Snippet Manager</b> - Making Code Reuse Simpler and Smarter
</p>

<p align="center">
  <a href="README.md">简体中文</a> | 
  <a href="README_TW.md">繁體中文</a> | 
  <a href="#quick-start">Quick Start</a> | 
  <a href="#features">Features</a> | 
  <a href="#screenshots">Screenshots</a>
</p>

---

## 📖 Introduction

**CodeSnippet Pro** is an intelligent code snippet management tool designed specifically for developers. It's not just a code repository, but an intelligent assistant that understands code semantics, provides smart recommendations, and organizes efficiently.

### 🎯 Core Pain Points Solved

- **Scattered Code**: Frequently used code snippets scattered across projects, notes, and Gists, difficult to manage centrally
- **Difficult Search**: Traditional keyword search cannot find semantically related code
- **Reinventing the Wheel**: Repeatedly writing code for the same functionality, wasting time
- **Team Collaboration**: Difficult to share and reuse excellent code among team members

### ✨ Differentiation Highlights

1. **AI Semantic Search**: Beyond keyword matching, understands code semantics to find truly relevant snippets
2. **Smart Tag Extraction**: Automatically analyzes code content and recommends appropriate tags
3. **Local-First**: Data stored locally, protecting privacy with faster response times
4. **Modern UI**: Clean and beautiful interface with smooth interaction experience
5. **Multi-Language Support**: Syntax highlighting and detection for 20+ programming languages

---

## ✨ Features

### 🔍 **Intelligent Search**
- **Full-Text Search**: Search across titles, code, descriptions, and tags
- **AI Semantic Search**: Based on code semantic understanding to find relevant snippets
- **Similar Recommendations**: Automatically recommend similar code snippets
- **Advanced Syntax**: Support advanced search syntax like `language:python tag:web`

### 🏷️ **Tag Management**
- **Auto Tags**: AI automatically analyzes code and recommends appropriate tags
- **Hierarchical Tags**: Support multi-level tag classification for flexible organization
- **Tag Statistics**: View code count for each tag

### 📁 **Collection Organization**
- **Custom Collections**: Organize code by project, tech stack, use case, etc.
- **Drag & Drop Sorting**: Freely adjust the order of code within collections
- **Batch Operations**: Support batch import and export

### 💾 **Data Sync**
- **GitHub Gist**: Two-way sync with GitHub Gist
- **Local Backup**: Support export to JSON, Markdown formats
- **Import/Export**: Support importing code snippets from other tools

### 📊 **Analytics**
- **Usage Statistics**: View usage frequency of code snippets
- **Language Distribution**: Understand usage percentage of each programming language
- **Trending Snippets**: Discover most frequently used code

### 🎨 **Other Features**
- **Syntax Highlighting**: Support syntax highlighting for 20+ programming languages
- **One-Click Copy**: Quickly copy code to clipboard
- **Favorites**: Mark frequently used code for quick access
- **Responsive Design**: Support desktop and mobile devices

---

## 🚀 Quick Start

### Requirements

- **Python**: 3.11 or higher
- **Node.js**: 18 or higher
- **Git**: For version control

### Installation

#### 1. Clone Repository

```bash
git clone https://github.com/gitstq/codesnippet-pro.git
cd codesnippet-pro
```

#### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend service
python -m app.main
```

Backend service will start at `http://localhost:8000`

#### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will start at `http://localhost:3000`

#### 4. Access Application

Open browser and visit `http://localhost:3000`, start using CodeSnippet Pro!

---

## 📖 Detailed Usage Guide

### Create Code Snippet

1. Click "New Snippet" button on the left
2. Fill in title and code content
3. Select programming language (or let system auto-detect)
4. Add description (optional)
5. Add tags (supports auto-recommendation)
6. Click save

### Search Code

- **Normal Search**: Enter keywords in top search box
- **AI Semantic Search**: Enable "AI Semantic" option on search page
- **Advanced Search**: Use syntax like `language:python tag:api`

### Manage Tags

- View all tags on "Tags" page
- System automatically recommends tags when creating new snippets
- Click tag to view all code under that tag

### Create Collection

1. Go to "Collections" page
2. Click "New Collection"
3. Enter collection name and description
4. Add related code to the collection

---

## 💡 Design Philosophy & Roadmap

### Technology Choices

- **FastAPI**: High performance, async support, automatic API documentation
- **React + TypeScript**: Type safety, component-based, rich ecosystem
- **SQLite**: Lightweight, zero configuration, suitable for local applications
- **Tailwind CSS**: Atomic CSS, rapid development, easy customization

### Future Roadmap

#### v1.1.0 (Planned)
- [ ] VS Code Extension
- [ ] JetBrains Plugin
- [ ] Code snippet sharing feature
- [ ] Team collaboration support

#### v1.2.0 (Planned)
- [ ] Code execution feature (sandbox environment)
- [ ] Code template marketplace
- [ ] AI code generation integration
- [ ] Multi-language UI support

#### v2.0.0 (Planning)
- [ ] Cloud sync service
- [ ] Mobile App
- [ ] Enterprise features
- [ ] API open platform

### Community Contribution

- Submit bug reports and feature suggestions
- Contribute code snippet templates
- Improve documentation and tutorials
- Develop plugins and extensions

---

## 📦 Packaging & Deployment

### Development Mode

```bash
# Backend
cd backend
python -m app.main

# Frontend
cd frontend
npm run dev
```

### Production Build

```bash
# Frontend build
cd frontend
npm run build

# Build output in frontend/dist directory
```

### Docker Deployment

```dockerfile
# Build image
docker build -t codesnippet-pro .

# Run container
docker run -p 8000:8000 -v $(pwd)/data:/app/data codesnippet-pro
```

---

## 🤝 Contributing

We welcome all forms of contributions! Please check [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Ways to Contribute

1. **Submit Issue**: Report bugs or suggest features
2. **Submit PR**: Fix bugs or implement new features
3. **Improve Documentation**: Help improve docs and tutorials
4. **Share & Promote**: Share the project with more developers

### Code Standards

- Follow PEP 8 (Python) and ESLint (TypeScript) standards
- Write clear commit messages
- Add necessary test cases
- Update relevant documentation

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

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

## 🙏 Acknowledgments

Thanks to the following open source projects and tools:

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [React](https://react.dev/) - JavaScript library for building user interfaces
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Prism.js](https://prismjs.com/) - Lightweight syntax highlighting library

---

## 📞 Contact Us

- **GitHub Issues**: [Submit Issue](https://github.com/gitstq/codesnippet-pro/issues)
- **Email**: codesnippet@example.com

---

<p align="center">
  Made with ❤️ by CodeSnippet Pro Team
</p>

<p align="center">
  ⭐ Star us to help more developers discover this tool!
</p>