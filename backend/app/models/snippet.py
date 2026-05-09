from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class SnippetBase(BaseModel):
    """片段基础模型"""
    title: str = Field(..., min_length=1, max_length=200, description="片段标题")
    code: str = Field(..., min_length=1, description="代码内容")
    language: str = Field(..., description="编程语言")
    description: str = Field(default="", description="描述")
    tags: List[str] = Field(default_factory=list, description="标签列表")
    source: str = Field(default="manual", description="来源")
    is_favorite: bool = Field(default=False, description="是否收藏")
    is_public: bool = Field(default=False, description="是否公开")


class SnippetCreate(SnippetBase):
    """创建片段请求模型"""
    pass


class SnippetUpdate(BaseModel):
    """更新片段请求模型"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    code: Optional[str] = None
    language: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    is_favorite: Optional[bool] = None
    is_public: Optional[bool] = None


class SnippetInDB(SnippetBase):
    """数据库中的片段模型"""
    id: str = Field(..., description="唯一标识")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="创建时间")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="更新时间")
    usage_count: int = Field(default=0, description="使用次数")
    embedding: Optional[List[float]] = Field(default=None, description="向量嵌入")

    class Config:
        from_attributes = True


class Snippet(SnippetInDB):
    """片段响应模型"""
    pass


class SnippetList(BaseModel):
    """片段列表响应"""
    items: List[Snippet]
    total: int
    page: int
    page_size: int