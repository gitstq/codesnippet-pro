from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class CollectionBase(BaseModel):
    """集合基础模型"""
    name: str = Field(..., min_length=1, max_length=100, description="集合名称")
    description: str = Field(default="", description="描述")


class CollectionCreate(CollectionBase):
    """创建集合请求模型"""
    snippet_ids: List[str] = Field(default_factory=list, description="片段ID列表")


class CollectionUpdate(BaseModel):
    """更新集合请求模型"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    snippet_ids: Optional[List[str]] = None


class CollectionInDB(CollectionBase):
    """数据库中的集合模型"""
    id: str = Field(..., description="唯一标识")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="创建时间")
    snippet_count: int = Field(default=0, description="片段数量")

    class Config:
        from_attributes = True


class Collection(CollectionInDB):
    """集合响应模型"""
    snippet_ids: List[str] = Field(default_factory=list, description="片段ID列表")


class CollectionList(BaseModel):
    """集合列表响应"""
    items: List[Collection]
    total: int