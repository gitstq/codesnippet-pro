from typing import List
from fastapi import APIRouter, HTTPException
from app.models.tag import Tag, TagCreate, TagUpdate, TagTree
from app.services.tag_service import TagService

router = APIRouter(prefix="/tags", tags=["tags"])
tag_service = TagService()


@router.get("", response_model=List[Tag])
async def get_tags():
    """获取所有标签"""
    return tag_service.get_all_tags()


@router.get("/tree", response_model=List[Tag])
async def get_tag_tree():
    """获取标签树"""
    return tag_service.get_tag_tree()


@router.post("", response_model=Tag)
async def create_tag(tag: TagCreate):
    """创建标签"""
    return tag_service.create_tag(tag.model_dump())


@router.post("/suggest")
async def suggest_tags(code: str, description: str = ""):
    """建议标签"""
    suggestions = tag_service.suggest_tags(code, description)
    return {"suggestions": suggestions}


@router.post("/{snippet_id}/auto-tag")
async def auto_tag_snippet(snippet_id: str):
    """自动为片段打标签"""
    tags = tag_service.auto_tag_snippet(snippet_id)
    return {"tags": tags}