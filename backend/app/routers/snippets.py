from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Body
from app.models.snippet import Snippet, SnippetCreate, SnippetUpdate, SnippetList
from app.services.snippet_service import SnippetService

router = APIRouter(prefix="/snippets", tags=["snippets"])
snippet_service = SnippetService()


@router.get("", response_model=List[Snippet])
async def list_snippets(
    language: Optional[str] = Query(None, description="按语言过滤"),
    tag: Optional[str] = Query(None, description="按标签过滤"),
    is_favorite: Optional[bool] = Query(None, description="按收藏状态过滤"),
    limit: int = Query(100, ge=1, le=1000, description="返回数量限制"),
    offset: int = Query(0, ge=0, description="偏移量")
):
    """获取片段列表"""
    filters = {}
    if language:
        filters["language"] = language
    if tag:
        filters["tag"] = tag
    if is_favorite is not None:
        filters["is_favorite"] = is_favorite
    
    snippets = snippet_service.list_snippets(filters, limit, offset)
    return snippets


@router.post("", response_model=Snippet)
async def create_snippet(snippet: SnippetCreate):
    """创建新片段"""
    try:
        created = snippet_service.create_snippet(snippet.model_dump())
        return created
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{snippet_id}", response_model=Snippet)
async def get_snippet(snippet_id: str):
    """获取单个片段"""
    snippet = snippet_service.get_snippet(snippet_id)
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet


@router.put("/{snippet_id}", response_model=Snippet)
async def update_snippet(snippet_id: str, snippet: SnippetUpdate):
    """更新片段"""
    update_data = {k: v for k, v in snippet.model_dump().items() if v is not None}
    updated = snippet_service.update_snippet(snippet_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return updated


@router.delete("/{snippet_id}")
async def delete_snippet(snippet_id: str):
    """删除片段"""
    deleted = snippet_service.delete_snippet(snippet_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return {"message": "Snippet deleted successfully"}


@router.post("/{snippet_id}/favorite")
async def toggle_favorite(snippet_id: str):
    """切换收藏状态"""
    snippet = snippet_service.toggle_favorite(snippet_id)
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet


@router.post("/{snippet_id}/usage")
async def increment_usage(snippet_id: str):
    """增加使用次数"""
    success = snippet_service.increment_usage(snippet_id)
    if not success:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return {"message": "Usage incremented"}


@router.post("/import")
async def import_snippets(snippets: List[dict] = Body(...)):
    """批量导入片段"""
    result = snippet_service.import_snippets(snippets)
    return result


@router.get("/export/{format_type}")
async def export_snippets(
    format_type: str = "json",
    language: Optional[str] = Query(None),
    tag: Optional[str] = Query(None)
):
    """导出片段"""
    filters = {}
    if language:
        filters["language"] = language
    if tag:
        filters["tag"] = tag
    
    result = snippet_service.export_snippets(format_type, filters)
    return result