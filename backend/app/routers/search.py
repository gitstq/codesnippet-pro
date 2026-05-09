from typing import Optional, List
from fastapi import APIRouter, Query
from app.models.search import SearchResponse, SemanticSearchRequest, SearchResult
from app.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["search"])
search_service = SearchService()


@router.get("", response_model=SearchResponse)
async def search(
    q: str = Query(..., description="搜索关键词"),
    language: Optional[str] = Query(None, description="语言过滤"),
    tag: Optional[str] = Query(None, description="标签过滤"),
    is_favorite: Optional[bool] = Query(None, description="收藏过滤"),
    limit: int = Query(20, ge=1, le=100)
):
    """全文搜索"""
    filters = {}
    if language:
        filters["language"] = language
    if tag:
        filters["tag"] = tag
    if is_favorite is not None:
        filters["is_favorite"] = is_favorite
    
    return search_service.search(q, filters, limit)


@router.post("/semantic", response_model=SearchResponse)
async def semantic_search(request: SemanticSearchRequest):
    """语义搜索"""
    return search_service.semantic_search(request.query, request.limit)


@router.get("/similar/{snippet_id}")
async def get_similar_snippets(
    snippet_id: str,
    limit: int = Query(5, ge=1, le=20)
):
    """获取相似片段"""
    results = search_service.get_similar_snippets(snippet_id, limit)
    return {
        "results": results,
        "total": len(results),
        "snippet_id": snippet_id
    }