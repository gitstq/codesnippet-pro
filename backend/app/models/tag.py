from typing import Optional, List
from pydantic import BaseModel, Field


class TagBase(BaseModel):
    """标签基础模型"""
    name: str = Field(..., min_length=1, max_length=50, description="标签名称")
    color: str = Field(default="#3B82F6", description="标签颜色")
    parent_id: Optional[str] = Field(default=None, description="父标签ID")


class TagCreate(TagBase):
    """创建标签请求模型"""
    pass


class TagUpdate(BaseModel):
    """更新标签请求模型"""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    color: Optional[str] = None
    parent_id: Optional[str] = None


class TagInDB(TagBase):
    """数据库中的标签模型"""
    id: str = Field(..., description="唯一标识")
    snippet_count: int = Field(default=0, description="关联片段数量")

    class Config:
        from_attributes = True


class Tag(TagInDB):
    """标签响应模型"""
    children: Optional[List["Tag"]] = Field(default=None, description="子标签")


class TagTree(BaseModel):
    """标签树结构"""
    tags: List[Tag]