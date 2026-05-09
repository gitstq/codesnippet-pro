# CodeSnippet Pro 技术规格文档

## 项目概述

**项目名称**: CodeSnippet Pro  
**版本**: v1.0.0  
**定位**: 智能代码片段管理工具  
**技术栈**: Python + FastAPI + React + TypeScript + SQLite

## 系统架构

### 整体架构
```
┌─────────────────────────────────────────────────────────────┐
│                    CodeSnippet Pro                          │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Web UI     │  │   CLI Tool   │  │  API Server  │      │
│  │  (React)     │  │   (Python)   │  │  (FastAPI)   │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         └─────────────────┴─────────────────┘               │
│                           │                                 │
│                    ┌──────┴──────┐                         │
│                    │  Core Layer │                         │
│                    │  (Python)   │                         │
│                    └──────┬──────┘                         │
│                           │                                 │
│         ┌─────────────────┼─────────────────┐              │
│         ▼                 ▼                 ▼              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   SQLite     │  │  AI Engine   │  │   Sync       │      │
│  │  (Local DB)  │  │  (Embedding) │  │  (GitHub)    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## 核心模块设计

### 1. 数据模型

```python
# 代码片段模型
class Snippet(BaseModel):
    id: str  # UUID
    title: str
    code: str
    language: str  # python, javascript, etc.
    description: str
    tags: List[str]
    source: str  # manual, github, clipboard
    created_at: datetime
    updated_at: datetime
    usage_count: int
    is_favorite: bool
    is_public: bool
    embedding: Optional[List[float]]  # 向量嵌入

# 标签模型
class Tag(BaseModel):
    id: str
    name: str
    color: str
    parent_id: Optional[str]  # 支持层级标签
    snippet_count: int

# 集合模型
class Collection(BaseModel):
    id: str
    name: str
    description: str
    snippet_ids: List[str]
    created_at: datetime
```

### 2. 核心功能模块

#### 2.1 片段管理模块 (snippet_manager.py)
- **功能**: CRUD操作、批量导入导出
- **接口**:
  - `create_snippet(data)` - 创建片段
  - `get_snippet(id)` - 获取片段
  - `update_snippet(id, data)` - 更新片段
  - `delete_snippet(id)` - 删除片段
  - `list_snippets(filters)` - 列表查询
  - `import_snippets(file)` - 批量导入
  - `export_snippets(format)` - 批量导出

#### 2.2 智能搜索模块 (search_engine.py)
- **功能**: 语义搜索、全文搜索、过滤器
- **接口**:
  - `semantic_search(query, limit=10)` - 语义搜索
  - `fulltext_search(query, limit=10)` - 全文搜索
  - `search_by_language(language)` - 按语言搜索
  - `search_by_tags(tags)` - 按标签搜索
  - `get_similar_snippets(snippet_id)` - 相似推荐

#### 2.3 AI处理模块 (ai_engine.py)
- **功能**: 代码分析、标签提取、嵌入生成
- **接口**:
  - `analyze_code(code)` - 代码分析
  - `extract_tags(code, description)` - 自动提取标签
  - `generate_embedding(text)` - 生成向量嵌入
  - `explain_code(code)` - 代码解释
  - `suggest_usage(code)` - 用法建议

#### 2.4 同步模块 (sync_manager.py)
- **功能**: GitHub Gist同步、本地备份
- **接口**:
  - `sync_to_gist()` - 同步到Gist
  - `sync_from_gist()` - 从Gist同步
  - `export_to_file(path)` - 导出到文件
  - `import_from_file(path)` - 从文件导入

#### 2.5 标签管理模块 (tag_manager.py)
- **功能**: 标签CRUD、层级管理、颜色管理
- **接口**:
  - `create_tag(name, color, parent_id)` - 创建标签
  - `update_tag(id, data)` - 更新标签
  - `delete_tag(id)` - 删除标签
  - `get_tag_tree()` - 获取标签树
  - `auto_tag_snippet(snippet_id)` - 自动标签

## API设计

### RESTful API端点

```
# 片段管理
GET    /api/snippets              # 获取片段列表
POST   /api/snippets              # 创建片段
GET    /api/snippets/{id}         # 获取单个片段
PUT    /api/snippets/{id}         # 更新片段
DELETE /api/snippets/{id}         # 删除片段
POST   /api/snippets/{id}/favorite # 收藏/取消收藏

# 搜索
GET    /api/search?q={query}      # 搜索片段
POST   /api/search/semantic       # 语义搜索
GET    /api/search/similar/{id}   # 相似片段

# 标签
GET    /api/tags                  # 获取标签列表
POST   /api/tags                  # 创建标签
PUT    /api/tags/{id}             # 更新标签
DELETE /api/tags/{id}             # 删除标签
GET    /api/tags/tree             # 获取标签树

# 集合
GET    /api/collections           # 获取集合列表
POST   /api/collections           # 创建集合
GET    /api/collections/{id}      # 获取集合详情
PUT    /api/collections/{id}      # 更新集合
DELETE /api/collections/{id}      # 删除集合

# 同步
POST   /api/sync/gist/export      # 导出到Gist
POST   /api/sync/gist/import      # 从Gist导入
POST   /api/sync/file/export      # 导出到文件
POST   /api/sync/file/import      # 从文件导入

# AI功能
POST   /api/ai/analyze            # 分析代码
POST   /api/ai/explain            # 解释代码
POST   /api/ai/suggest-tags       # 建议标签
POST   /api/ai/generate-embedding # 生成嵌入

# 统计
GET    /api/stats/overview        # 概览统计
GET    /api/stats/languages       # 语言分布
GET    /api/stats/tags            # 标签统计
GET    /api/stats/trending        # 热门片段
```

## 数据库设计

### SQLite Schema

```sql
-- 片段表
CREATE TABLE snippets (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    code TEXT NOT NULL,
    language TEXT NOT NULL,
    description TEXT,
    source TEXT DEFAULT 'manual',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usage_count INTEGER DEFAULT 0,
    is_favorite INTEGER DEFAULT 0,
    is_public INTEGER DEFAULT 0,
    embedding BLOB
);

-- 标签表
CREATE TABLE tags (
    id TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    color TEXT DEFAULT '#3B82F6',
    parent_id TEXT,
    snippet_count INTEGER DEFAULT 0,
    FOREIGN KEY (parent_id) REFERENCES tags(id)
);

-- 片段-标签关联表
CREATE TABLE snippet_tags (
    snippet_id TEXT,
    tag_id TEXT,
    PRIMARY KEY (snippet_id, tag_id),
    FOREIGN KEY (snippet_id) REFERENCES snippets(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

-- 集合表
CREATE TABLE collections (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 集合-片段关联表
CREATE TABLE collection_snippets (
    collection_id TEXT,
    snippet_id TEXT,
    order_index INTEGER,
    PRIMARY KEY (collection_id, snippet_id),
    FOREIGN KEY (collection_id) REFERENCES collections(id) ON DELETE CASCADE,
    FOREIGN KEY (snippet_id) REFERENCES snippets(id) ON DELETE CASCADE
);

-- 索引
CREATE INDEX idx_snippets_language ON snippets(language);
CREATE INDEX idx_snippets_favorite ON snippets(is_favorite);
CREATE INDEX idx_snippets_created ON snippets(created_at);
CREATE INDEX idx_snippet_tags_tag ON snippet_tags(tag_id);
```

## 前端设计

### 页面结构

```
/
├── /                    # 首页 - 片段列表
├── /snippet/:id         # 片段详情
├── /snippet/new         # 新建片段
├── /snippet/:id/edit    # 编辑片段
├── /search              # 搜索结果
├── /tags                # 标签管理
├── /collections         # 集合管理
├── /settings            # 设置
└── /stats               # 统计
```

### 组件结构

```
src/
├── components/
│   ├── common/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Modal.tsx
│   │   └── Card.tsx
│   ├── snippet/
│   │   ├── SnippetCard.tsx
│   │   ├── SnippetEditor.tsx
│   │   ├── SnippetViewer.tsx
│   │   └── CodeBlock.tsx
│   ├── search/
│   │   ├── SearchBar.tsx
│   │   ├── SearchFilters.tsx
│   │   └── SearchResults.tsx
│   ├── tags/
│   │   ├── TagList.tsx
│   │   ├── TagTree.tsx
│   │   └── TagInput.tsx
│   └── layout/
│       ├── Sidebar.tsx
│       ├── Header.tsx
│       └── Layout.tsx
├── pages/
│   ├── Home.tsx
│   ├── SnippetDetail.tsx
│   ├── SnippetEdit.tsx
│   ├── Search.tsx
│   ├── Tags.tsx
│   ├── Collections.tsx
│   ├── Settings.tsx
│   └── Stats.tsx
├── hooks/
│   ├── useSnippets.ts
│   ├── useSearch.ts
│   ├── useTags.ts
│   └── useAI.ts
├── services/
│   ├── api.ts
│   ├── snippetService.ts
│   ├── searchService.ts
│   └── aiService.ts
└── utils/
    ├── storage.ts
    ├── formatters.ts
    └── languages.ts
```

## 技术实现细节

### 1. 语义搜索实现

```python
# 使用 sentence-transformers 生成嵌入
from sentence_transformers import SentenceTransformer
import numpy as np

class SemanticSearch:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def generate_embedding(self, text: str) -> List[float]:
        """生成文本嵌入向量"""
        embedding = self.model.encode(text)
        return embedding.tolist()
    
    def search(self, query: str, snippets: List[Snippet], top_k: int = 10):
        """语义搜索"""
        query_embedding = self.generate_embedding(query)
        
        results = []
        for snippet in snippets:
            if snippet.embedding:
                similarity = cosine_similarity(query_embedding, snippet.embedding)
                results.append((snippet, similarity))
        
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

def cosine_similarity(a: List[float], b: List[float]) -> float:
    """计算余弦相似度"""
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

### 2. 代码高亮

```typescript
// 使用 Prism.js 进行代码高亮
import Prism from 'prismjs';
import 'prismjs/components/prism-python';
import 'prismjs/components/prism-javascript';
// ... 其他语言

const CodeBlock: React.FC<{ code: string; language: string }> = ({ code, language }) => {
  useEffect(() => {
    Prism.highlightAll();
  }, [code]);

  return (
    <pre className={`language-${language}`}>
      <code>{code}</code>
    </pre>
  );
};
```

### 3. 本地存储

```typescript
// IndexedDB 封装
class SnippetStorage {
  private db: IDBDatabase | null = null;
  
  async init() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open('CodeSnippetPro', 1);
      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve(this.db);
      };
      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;
        db.createObjectStore('snippets', { keyPath: 'id' });
        db.createObjectStore('tags', { keyPath: 'id' });
      };
    });
  }
  
  async saveSnippet(snippet: Snippet): Promise<void> {
    // 实现保存逻辑
  }
  
  async getSnippet(id: string): Promise<Snippet | null> {
    // 实现获取逻辑
  }
}
```

## 开发计划

### 第一阶段：核心功能 (Day 1)
- [x] 项目初始化
- [x] 数据库设计
- [x] API开发
- [x] 基础Web UI

### 第二阶段：增强功能 (Day 2)
- [ ] 语义搜索
- [ ] AI功能集成
- [ ] GitHub同步
- [ ] 标签系统

### 第三阶段：优化完善 (Day 3)
- [ ] 性能优化
- [ ] 测试完善
- [ ] 文档编写
- [ ] 发布准备

## 测试策略

### 单元测试
```python
# 示例测试
def test_create_snippet():
    manager = SnippetManager()
    snippet = manager.create_snippet({
        'title': 'Test',
        'code': 'print("hello")',
        'language': 'python'
    })
    assert snippet.title == 'Test'
    assert snippet.language == 'python'
```

### 集成测试
- API端点测试
- 数据库操作测试
- 搜索功能测试

### E2E测试
- 用户流程测试
- 界面交互测试

## 部署方案

### 本地部署
```bash
# 安装依赖
pip install -r requirements.txt
npm install

# 启动后端
python -m app.main

# 启动前端
npm run dev
```

### Docker部署
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "app.main"]
```

## 安全考虑

1. **代码执行安全** - 不执行用户代码，仅存储和展示
2. **数据隐私** - 本地优先，用户数据不上传
3. **API安全** - 输入验证、SQL注入防护
4. **GitHub集成** - OAuth安全流程

## 性能指标

- 搜索响应时间: < 500ms
- 页面加载时间: < 2s
- 支持片段数量: 10,000+
- 并发用户: 100+
