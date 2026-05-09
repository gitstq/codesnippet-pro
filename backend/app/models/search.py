from typing import List, Optional
from pydantic import BaseModel, Field
from .snippet import Snippet


class SearchQuery(BaseModel):
    """搜索查询"""
    q: str = Field(..., description="搜索关键词")
    language: Optional[str] = Field(None, description="语言过滤")
    tags: Optional[List[str]] = Field(None, description="标签过滤")
    is_favorite: Optional[bool] = Field(None, description="收藏过滤")
    limit: int = Field(default=20, ge=1, le=100, description="返回数量")


class SearchResult(BaseModel):
    """搜索结果"""
    snippet: Snippet
    score: float = Field(..., description="匹配分数")
    highlights: Optional[List[str]] = Field(default=None, description="高亮片段")


class SearchResponse(BaseModel):
    """搜索响应"""
    results: List[SearchResult]
    total: int
    query: str
    search_time: float = Field(..., description="搜索耗时(秒)")


class SemanticSearchRequest(BaseModel):
    """语义搜索请求"""
    query: str = Field(..., description="搜索语义")
    limit: int = Field(default=10, ge=1, le=50)


class SimilarSnippetsRequest(BaseModel):
    """相似片段请求"""
    snippet_id: str = Field(..., description="参考片段ID")
    limit: int = Field(default=5, ge=1, le=20)