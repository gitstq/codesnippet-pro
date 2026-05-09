# 贡献指南

感谢您对 CodeSnippet Pro 的兴趣！我们欢迎各种形式的贡献。

## 如何贡献

### 报告问题

如果您发现了bug或有功能建议，请通过 GitHub Issues 提交：

1. 检查是否已有相关问题
2. 使用问题模板创建新issue
3. 提供详细的描述和复现步骤

### 提交代码

1. Fork 本仓库
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/codesnippet-pro.git
cd codesnippet-pro

# 后端设置
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 前端设置
cd ../frontend
npm install
npm run dev
```

### 代码规范

- Python: 遵循 PEP 8
- TypeScript: 使用 ESLint 配置
- 提交信息遵循 Conventional Commits

## 行为准则

- 尊重所有参与者
- 接受建设性批评
- 关注对社区最有利的事情

## 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。