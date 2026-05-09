from typing import List, Dict, Any, Optional
import re
from app.utils.database import get_db
from app.utils.embedding import get_embedding_generator


class SearchService:
    """搜索服务"""
    
    def __init__(self):
        self.db = get_db()
        self.embedding_gen = get_embedding_generator()
    
    def search(self, query: str, filters: Dict[str, Any] = None, limit: int = 20) -> Dict[str, Any]:
        """全文搜索"""
        import time
        start_time = time.time()
        
        filters = filters or {}
        all_snippets = self.db.list_snippets(filters, limit=1000)
        
        query_lower = query.lower()
        results = []
        
        for snippet in all_snippets:
            score = 0
            highlights = []
            
            # 标题匹配 (权重最高)
            if query_lower in snippet.get("title", "").lower():
                score += 10
                highlights.append("title")
            
            # 代码匹配
            code_lower = snippet.get("code", "").lower()
            if query_lower in code_lower:
                score += 5
                highlights.append("code")
            
            # 描述匹配
            if query_lower in snippet.get("description", "").lower():
                score += 3
                highlights.append("description")
            
            # 标签匹配
            for tag in snippet.get("tags", []):
                if query_lower in tag.lower():
                    score += 4
                    highlights.append(f"tag:{tag}")
            
            # 语言匹配
            if query_lower in snippet.get("language", "").lower():
                score += 2
                highlights.append("language")
            
            if score > 0:
                results.append({
                    "snippet": snippet,
                    "score": score,
                    "highlights": list(set(highlights))
                })
        
        # 按分数排序
        results.sort(key=lambda x: x["score"], reverse=True)
        
        search_time = time.time() - start_time
        
        return {
            "results": results[:limit],
            "total": len(results),
            "query": query,
            "search_time": round(search_time, 3)
        }
    
    def semantic_search(self, query: str, limit: int = 10) -> Dict[str, Any]:
        """语义搜索"""
        import time
        start_time = time.time()
        
        # 生成查询向量
        query_embedding = self.embedding_gen.generate_embedding(query)
        
        # 获取所有片段
        all_snippets = self.db.list_snippets(limit=1000)
        
        results = []
        for snippet in all_snippets:
            if snippet.get("embedding"):
                similarity = self.embedding_gen.cosine_similarity(
                    query_embedding, snippet["embedding"]
                )
                if similarity > 0.3:  # 相似度阈值
                    results.append({
                        "snippet": snippet,
                        "score": similarity,
                        "highlights": ["semantic"]
                    })
        
        # 按相似度排序
        results.sort(key=lambda x: x["score"], reverse=True)
        
        search_time = time.time() - start_time
        
        return {
            "results": results[:limit],
            "total": len(results),
            "query": query,
            "search_time": round(search_time, 3)
        }
    
    def get_similar_snippets(self, snippet_id: str, limit: int = 5) -> List[Dict[str, Any]]:
        """获取相似片段"""
        target = self.db.get_snippet(snippet_id)
        if not target or not target.get("embedding"):
            return []
        
        all_snippets = self.db.list_snippets(limit=1000)
        
        results = []
        for snippet in all_snippets:
            if snippet["id"] != snippet_id and snippet.get("embedding"):
                similarity = self.embedding_gen.cosine_similarity(
                    target["embedding"], snippet["embedding"]
                )
                if similarity > 0.5:
                    results.append({
                        "snippet": snippet,
                        "score": similarity
                    })
        
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:limit]
    
    def advanced_search(self, query: str, **kwargs) -> Dict[str, Any]:
        """高级搜索"""
        # 解析查询语法
        # language:python tag:web sort:recent
        
        filters = {}
        search_terms = []
        
        # 解析特殊语法
        patterns = [
            (r'language:(\w+)', 'language'),
            (r'lang:(\w+)', 'language'),
            (r'tag:(\w+)', 'tag'),
            (r'is:favorite', 'is_favorite'),
        ]
        
        remaining_query = query
        for pattern, key in patterns:
            matches = re.findall(pattern, query, re.IGNORECASE)
            for match in matches:
                if key == 'is_favorite':
                    filters[key] = True
                else:
                    filters[key] = match
                remaining_query = re.sub(pattern, '', remaining_query, flags=re.IGNORECASE)
        
        # 清理剩余查询
        remaining_query = ' '.join(remaining_query.split())
        
        if remaining_query:
            return self.search(remaining_query, filters, kwargs.get('limit', 20))
        else:
            # 只有过滤器，返回过滤结果
            snippets = self.db.list_snippets(filters, limit=kwargs.get('limit', 100))
            return {
                "results": [{"snippet": s, "score": 1, "highlights": []} for s in snippets],
                "total": len(snippets),
                "query": query,
                "search_time": 0
            }