from typing import List, Optional, Dict, Any
from datetime import datetime
from app.utils.database import get_db
from app.utils.embedding import get_embedding_generator
from app.utils.languages import detect_language


class SnippetService:
    """片段服务"""
    
    def __init__(self):
        self.db = get_db()
        self.embedding_gen = get_embedding_generator()
    
    def create_snippet(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """创建片段"""
        # 自动检测语言
        if not data.get("language"):
            data["language"] = detect_language(data["code"], data.get("filename", ""))
        
        # 生成嵌入向量
        text_for_embedding = f"{data.get('title', '')} {data.get('description', '')} {data['code'][:500]}"
        data["embedding"] = self.embedding_gen.generate_embedding(text_for_embedding)
        
        return self.db.create_snippet(data)
    
    def get_snippet(self, snippet_id: str) -> Optional[Dict[str, Any]]:
        """获取片段"""
        return self.db.get_snippet(snippet_id)
    
    def update_snippet(self, snippet_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """更新片段"""
        # 如果代码或标题更新，重新生成嵌入
        if "code" in data or "title" in data or "description" in data:
            existing = self.get_snippet(snippet_id)
            if existing:
                title = data.get("title", existing["title"])
                description = data.get("description", existing["description"])
                code = data.get("code", existing["code"])
                text_for_embedding = f"{title} {description} {code[:500]}"
                data["embedding"] = self.embedding_gen.generate_embedding(text_for_embedding)
        
        return self.db.update_snippet(snippet_id, data)
    
    def delete_snippet(self, snippet_id: str) -> bool:
        """删除片段"""
        return self.db.delete_snippet(snippet_id)
    
    def list_snippets(self, filters: Dict[str, Any] = None, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        """列出片段"""
        return self.db.list_snippets(filters, limit, offset)
    
    def toggle_favorite(self, snippet_id: str) -> Optional[Dict[str, Any]]:
        """切换收藏状态"""
        snippet = self.get_snippet(snippet_id)
        if snippet:
            return self.update_snippet(snippet_id, {"is_favorite": not snippet["is_favorite"]})
        return None
    
    def increment_usage(self, snippet_id: str) -> bool:
        """增加使用次数"""
        snippet = self.get_snippet(snippet_id)
        if snippet:
            snippet["usage_count"] = snippet.get("usage_count", 0) + 1
            self.db.update_snippet(snippet_id, {"usage_count": snippet["usage_count"]})
            return True
        return False
    
    def import_snippets(self, snippets: List[Dict[str, Any]]) -> Dict[str, Any]:
        """批量导入片段"""
        imported = []
        failed = []
        
        for item in snippets:
            try:
                snippet = self.create_snippet(item)
                imported.append(snippet)
            except Exception as e:
                failed.append({"item": item, "error": str(e)})
        
        return {
            "imported_count": len(imported),
            "failed_count": len(failed),
            "imported": imported,
            "failed": failed
        }
    
    def export_snippets(self, format_type: str = "json", filters: Dict[str, Any] = None) -> Dict[str, Any]:
        """导出片段"""
        snippets = self.list_snippets(filters, limit=10000)
        
        if format_type == "json":
            return {
                "format": "json",
                "count": len(snippets),
                "data": snippets
            }
        elif format_type == "markdown":
            markdown_content = self._export_to_markdown(snippets)
            return {
                "format": "markdown",
                "count": len(snippets),
                "content": markdown_content
            }
        else:
            raise ValueError(f"Unsupported format: {format_type}")
    
    def _export_to_markdown(self, snippets: List[Dict[str, Any]]) -> str:
        """导出为Markdown格式"""
        lines = ["# Code Snippets\n"]
        
        for snippet in snippets:
            lines.append(f"## {snippet['title']}\n")
            if snippet.get("description"):
                lines.append(f"{snippet['description']}\n")
            lines.append(f"**Language:** {snippet['language']}\n")
            if snippet.get("tags"):
                lines.append(f"**Tags:** {', '.join(snippet['tags'])}\n")
            lines.append(f"\n```{snippet['language']}")
            lines.append(snippet["code"])
            lines.append("```\n")
        
        return "\n".join(lines)
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        all_snippets = self.list_snippets(limit=10000)
        
        total = len(all_snippets)
        favorite_count = sum(1 for s in all_snippets if s.get("is_favorite"))
        
        # 语言分布
        language_counts = {}
        for snippet in all_snippets:
            lang = snippet.get("language", "other")
            language_counts[lang] = language_counts.get(lang, 0) + 1
        
        # 标签统计
        tag_counts = {}
        for snippet in all_snippets:
            for tag in snippet.get("tags", []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        # 热门片段
        trending = sorted(all_snippets, key=lambda x: x.get("usage_count", 0), reverse=True)[:10]
        
        # 最近添加
        recent = sorted(all_snippets, key=lambda x: x.get("created_at", ""), reverse=True)[:10]
        
        return {
            "total_snippets": total,
            "favorite_count": favorite_count,
            "language_distribution": language_counts,
            "tag_distribution": dict(sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:20]),
            "trending_snippets": trending,
            "recent_snippets": recent
        }