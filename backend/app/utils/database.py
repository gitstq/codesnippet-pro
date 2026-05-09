import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import List, Optional, Dict, Any
import json
import uuid


class Database:
    """SQLite数据库管理类"""
    
    def __init__(self, db_path: str = "codesnippet.db"):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """初始化数据库"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # 创建片段表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS snippets (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    code TEXT NOT NULL,
                    language TEXT NOT NULL,
                    description TEXT DEFAULT '',
                    source TEXT DEFAULT 'manual',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    usage_count INTEGER DEFAULT 0,
                    is_favorite INTEGER DEFAULT 0,
                    is_public INTEGER DEFAULT 0,
                    embedding TEXT
                )
            """)
            
            # 创建标签表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tags (
                    id TEXT PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    color TEXT DEFAULT '#3B82F6',
                    parent_id TEXT,
                    snippet_count INTEGER DEFAULT 0
                )
            """)
            
            # 创建片段-标签关联表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS snippet_tags (
                    snippet_id TEXT,
                    tag_id TEXT,
                    PRIMARY KEY (snippet_id, tag_id),
                    FOREIGN KEY (snippet_id) REFERENCES snippets(id) ON DELETE CASCADE,
                    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
                )
            """)
            
            # 创建集合表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS collections (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT DEFAULT '',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # 创建集合-片段关联表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS collection_snippets (
                    collection_id TEXT,
                    snippet_id TEXT,
                    order_index INTEGER DEFAULT 0,
                    PRIMARY KEY (collection_id, snippet_id),
                    FOREIGN KEY (collection_id) REFERENCES collections(id) ON DELETE CASCADE,
                    FOREIGN KEY (snippet_id) REFERENCES snippets(id) ON DELETE CASCADE
                )
            """)
            
            # 创建索引
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_snippets_language ON snippets(language)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_snippets_favorite ON snippets(is_favorite)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_snippets_created ON snippets(created_at)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_snippet_tags_tag ON snippet_tags(tag_id)")
            
            conn.commit()
    
    @contextmanager
    def _get_connection(self):
        """获取数据库连接"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
    
    # 片段操作
    def create_snippet(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """创建片段"""
        snippet_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        
        embedding_json = None
        if data.get("embedding"):
            embedding_json = json.dumps(data["embedding"])
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO snippets (id, title, code, language, description, source,
                                    created_at, updated_at, is_favorite, is_public, embedding)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                snippet_id, data["title"], data["code"], data["language"],
                data.get("description", ""), data.get("source", "manual"),
                now, now, int(data.get("is_favorite", False)),
                int(data.get("is_public", False)), embedding_json
            ))
            
            # 处理标签
            tags = data.get("tags", [])
            for tag_name in tags:
                tag = self._get_or_create_tag(conn, tag_name)
                cursor.execute("""
                    INSERT OR IGNORE INTO snippet_tags (snippet_id, tag_id)
                    VALUES (?, ?)
                """, (snippet_id, tag["id"]))
                cursor.execute("""
                    UPDATE tags SET snippet_count = snippet_count + 1 WHERE id = ?
                """, (tag["id"],))
            
            conn.commit()
        
        return self.get_snippet(snippet_id)
    
    def get_snippet(self, snippet_id: str) -> Optional[Dict[str, Any]]:
        """获取片段"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM snippets WHERE id = ?", (snippet_id,))
            row = cursor.fetchone()
            
            if not row:
                return None
            
            snippet = dict(row)
            snippet["is_favorite"] = bool(snippet["is_favorite"])
            snippet["is_public"] = bool(snippet["is_public"])
            
            if snippet["embedding"]:
                snippet["embedding"] = json.loads(snippet["embedding"])
            
            # 获取标签
            cursor.execute("""
                SELECT t.name FROM tags t
                JOIN snippet_tags st ON t.id = st.tag_id
                WHERE st.snippet_id = ?
            """, (snippet_id,))
            snippet["tags"] = [row[0] for row in cursor.fetchall()]
            
            return snippet
    
    def update_snippet(self, snippet_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """更新片段"""
        now = datetime.utcnow().isoformat()
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # 检查片段是否存在
            cursor.execute("SELECT id FROM snippets WHERE id = ?", (snippet_id,))
            if not cursor.fetchone():
                return None
            
            # 构建更新字段
            updates = []
            params = []
            
            if "title" in data:
                updates.append("title = ?")
                params.append(data["title"])
            if "code" in data:
                updates.append("code = ?")
                params.append(data["code"])
            if "language" in data:
                updates.append("language = ?")
                params.append(data["language"])
            if "description" in data:
                updates.append("description = ?")
                params.append(data["description"])
            if "is_favorite" in data:
                updates.append("is_favorite = ?")
                params.append(int(data["is_favorite"]))
            if "is_public" in data:
                updates.append("is_public = ?")
                params.append(int(data["is_public"]))
            if "embedding" in data:
                updates.append("embedding = ?")
                params.append(json.dumps(data["embedding"]) if data["embedding"] else None)
            
            if updates:
                updates.append("updated_at = ?")
                params.append(now)
                params.append(snippet_id)
                
                cursor.execute(f"""
                    UPDATE snippets SET {', '.join(updates)} WHERE id = ?
                """, params)
            
            # 更新标签
            if "tags" in data:
                # 删除旧标签关联
                cursor.execute("""
                    SELECT tag_id FROM snippet_tags WHERE snippet_id = ?
                """, (snippet_id,))
                old_tags = [row[0] for row in cursor.fetchall()]
                
                for tag_id in old_tags:
                    cursor.execute("""
                        UPDATE tags SET snippet_count = snippet_count - 1 WHERE id = ?
                    """, (tag_id,))
                
                cursor.execute("DELETE FROM snippet_tags WHERE snippet_id = ?", (snippet_id,))
                
                # 添加新标签
                for tag_name in data["tags"]:
                    tag = self._get_or_create_tag(conn, tag_name)
                    cursor.execute("""
                        INSERT OR IGNORE INTO snippet_tags (snippet_id, tag_id)
                        VALUES (?, ?)
                    """, (snippet_id, tag["id"]))
                    cursor.execute("""
                        UPDATE tags SET snippet_count = snippet_count + 1 WHERE id = ?
                    """, (tag["id"],))
            
            conn.commit()
        
        return self.get_snippet(snippet_id)
    
    def delete_snippet(self, snippet_id: str) -> bool:
        """删除片段"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # 更新标签计数
            cursor.execute("""
                SELECT tag_id FROM snippet_tags WHERE snippet_id = ?
            """, (snippet_id,))
            tags = [row[0] for row in cursor.fetchall()]
            
            for tag_id in tags:
                cursor.execute("""
                    UPDATE tags SET snippet_count = snippet_count - 1 WHERE id = ?
                """, (tag_id,))
            
            cursor.execute("DELETE FROM snippets WHERE id = ?", (snippet_id,))
            conn.commit()
            
            return cursor.rowcount > 0
    
    def list_snippets(self, filters: Dict[str, Any] = None, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        """列出片段"""
        filters = filters or {}
        conditions = []
        params = []
        
        if "language" in filters:
            conditions.append("language = ?")
            params.append(filters["language"])
        if "is_favorite" in filters:
            conditions.append("is_favorite = ?")
            params.append(int(filters["is_favorite"]))
        if "tag" in filters:
            conditions.append("""
                EXISTS (SELECT 1 FROM snippet_tags st 
                       JOIN tags t ON st.tag_id = t.id 
                       WHERE st.snippet_id = snippets.id AND t.name = ?)
            """)
            params.append(filters["tag"])
        
        where_clause = "WHERE " + " AND ".join(conditions) if conditions else ""
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                SELECT * FROM snippets {where_clause}
                ORDER BY updated_at DESC
                LIMIT ? OFFSET ?
            """, params + [limit, offset])
            
            snippets = []
            for row in cursor.fetchall():
                snippet = dict(row)
                snippet["is_favorite"] = bool(snippet["is_favorite"])
                snippet["is_public"] = bool(snippet["is_public"])
                if snippet["embedding"]:
                    snippet["embedding"] = json.loads(snippet["embedding"])
                
                # 获取标签
                cursor.execute("""
                    SELECT t.name FROM tags t
                    JOIN snippet_tags st ON t.id = st.tag_id
                    WHERE st.snippet_id = ?
                """, (snippet["id"],))
                snippet["tags"] = [r[0] for r in cursor.fetchall()]
                
                snippets.append(snippet)
            
            return snippets
    
    def _get_or_create_tag(self, conn, name: str) -> Dict[str, Any]:
        """获取或创建标签"""
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM tags WHERE name = ?", (name,))
        row = cursor.fetchone()
        
        if row:
            return dict(row)
        
        tag_id = str(uuid.uuid4())
        colors = ["#3B82F6", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6", "#EC4899", "#06B6D4"]
        import random
        color = random.choice(colors)
        
        cursor.execute("""
            INSERT INTO tags (id, name, color, snippet_count)
            VALUES (?, ?, ?, 0)
        """, (tag_id, name, color))
        
        return {"id": tag_id, "name": name, "color": color, "snippet_count": 0}
    
    # 标签操作
    def get_all_tags(self) -> List[Dict[str, Any]]:
        """获取所有标签"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tags ORDER BY name")
            return [dict(row) for row in cursor.fetchall()]
    
    def get_tag_tree(self) -> List[Dict[str, Any]]:
        """获取标签树"""
        tags = self.get_all_tags()
        tag_map = {tag["id"]: {**tag, "children": []} for tag in tags}
        
        root_tags = []
        for tag in tags:
            if tag["parent_id"] and tag["parent_id"] in tag_map:
                tag_map[tag["parent_id"]]["children"].append(tag_map[tag["id"]])
            else:
                root_tags.append(tag_map[tag["id"]])
        
        return root_tags
    
    # 集合操作
    def create_collection(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """创建集合"""
        collection_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO collections (id, name, description, created_at)
                VALUES (?, ?, ?, ?)
            """, (collection_id, data["name"], data.get("description", ""), now))
            
            for idx, snippet_id in enumerate(data.get("snippet_ids", [])):
                cursor.execute("""
                    INSERT INTO collection_snippets (collection_id, snippet_id, order_index)
                    VALUES (?, ?, ?)
                """, (collection_id, snippet_id, idx))
            
            conn.commit()
        
        return self.get_collection(collection_id)
    
    def get_collection(self, collection_id: str) -> Optional[Dict[str, Any]]:
        """获取集合"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM collections WHERE id = ?", (collection_id,))
            row = cursor.fetchone()
            
            if not row:
                return None
            
            collection = dict(row)
            
            cursor.execute("""
                SELECT snippet_id FROM collection_snippets
                WHERE collection_id = ? ORDER BY order_index
            """, (collection_id,))
            collection["snippet_ids"] = [row[0] for row in cursor.fetchall()]
            collection["snippet_count"] = len(collection["snippet_ids"])
            
            return collection
    
    def get_all_collections(self) -> List[Dict[str, Any]]:
        """获取所有集合"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM collections ORDER BY created_at DESC")
            
            collections = []
            for row in cursor.fetchall():
                collection = dict(row)
                cursor.execute("""
                    SELECT COUNT(*) FROM collection_snippets WHERE collection_id = ?
                """, (collection["id"],))
                collection["snippet_count"] = cursor.fetchone()[0]
                collections.append(collection)
            
            return collections


# 全局数据库实例
_db_instance = None

def get_db() -> Database:
    """获取数据库实例"""
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
    return _db_instance