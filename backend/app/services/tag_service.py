from typing import List, Dict, Any, Optional
from app.utils.database import get_db


class TagService:
    """标签服务"""
    
    def __init__(self):
        self.db = get_db()
    
    def get_all_tags(self) -> List[Dict[str, Any]]:
        """获取所有标签"""
        return self.db.get_all_tags()
    
    def get_tag_tree(self) -> List[Dict[str, Any]]:
        """获取标签树"""
        return self.db.get_tag_tree()
    
    def create_tag(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """创建标签"""
        # 这里简化处理，实际应该调用db的create_tag方法
        # 但db中目前是get_or_create，需要扩展
        import uuid
        tag_id = str(uuid.uuid4())
        
        # 颜色如果没有提供，随机选择
        if not data.get("color"):
            colors = ["#3B82F6", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6", "#EC4899", "#06B6D4"]
            import random
            data["color"] = random.choice(colors)
        
        # 实际应该保存到数据库
        return {
            "id": tag_id,
            "name": data["name"],
            "color": data["color"],
            "parent_id": data.get("parent_id"),
            "snippet_count": 0
        }
    
    def update_tag(self, tag_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """更新标签"""
        # 实现更新逻辑
        pass
    
    def delete_tag(self, tag_id: str) -> bool:
        """删除标签"""
        # 实现删除逻辑
        pass
    
    def suggest_tags(self, code: str, description: str = "") -> List[str]:
        """基于代码内容建议标签"""
        suggestions = []
        
        # 基于代码特征提取标签
        code_lower = code.lower()
        desc_lower = description.lower()
        combined = code_lower + " " + desc_lower
        
        # 技术栈标签
        tech_patterns = {
            "react": ["react", "jsx", "usestate", "useeffect"],
            "vue": ["vue", "v-if", "v-for", "computed"],
            "angular": ["angular", "@component", "@injectable"],
            "node": ["node", "nodejs", "require(", "module.exports"],
            "django": ["django", "models", "views"],
            "flask": ["flask", "@app.route"],
            "fastapi": ["fastapi", "@app.get"],
            "spring": ["spring", "@controller", "@service"],
            "docker": ["docker", "dockerfile", "from", "cmd"],
            "kubernetes": ["kubernetes", "k8s", "pod", "deployment"],
            "aws": ["aws", "boto3", "amazon"],
            "database": ["database", "sql", "query", "select", "insert"],
            "api": ["api", "rest", "endpoint", "request", "response"],
            "auth": ["auth", "authentication", "jwt", "token", "login"],
            "test": ["test", "unittest", "pytest", "jest", "mocha"],
            "algorithm": ["algorithm", "sort", "search", "tree", "graph"],
            "utils": ["utils", "utility", "helper", "common"],
        }
        
        for tag, patterns in tech_patterns.items():
            for pattern in patterns:
                if pattern in combined:
                    suggestions.append(tag)
                    break
        
        # 基于语言建议
        languages = {
            "python": "python",
            "javascript": "javascript",
            "typescript": "typescript",
            "java": "java",
            "go": "go",
            "rust": "rust",
            "cpp": "cpp",
            "c": "c",
        }
        
        for lang, keyword in languages.items():
            if keyword in combined:
                suggestions.append(lang)
        
        # 去重并返回
        return list(set(suggestions))[:10]
    
    def auto_tag_snippet(self, snippet_id: str) -> List[str]:
        """自动为片段打标签"""
        snippet = self.db.get_snippet(snippet_id)
        if not snippet:
            return []
        
        suggested_tags = self.suggest_tags(
            snippet.get("code", ""),
            snippet.get("description", "")
        )
        
        # 更新片段标签
        if suggested_tags:
            current_tags = snippet.get("tags", [])
            new_tags = list(set(current_tags + suggested_tags))
            self.db.update_snippet(snippet_id, {"tags": new_tags})
        
        return suggested_tags