from fastapi import APIRouter
from app.services.snippet_service import SnippetService

router = APIRouter(prefix="/stats", tags=["stats"])
snippet_service = SnippetService()


@router.get("/overview")
async def get_overview():
    """获取概览统计"""
    return snippet_service.get_stats()


@router.get("/languages")
async def get_language_stats():
    """获取语言分布统计"""
    stats = snippet_service.get_stats()
    return {
        "languages": stats.get("language_distribution", {}),
        "total": stats.get("total_snippets", 0)
    }


@router.get("/tags")
async def get_tag_stats():
    """获取标签统计"""
    stats = snippet_service.get_stats()
    return {
        "tags": stats.get("tag_distribution", {}),
        "total": sum(stats.get("tag_distribution", {}).values())
    }


@router.get("/trending")
async def get_trending_snippets():
    """获取热门片段"""
    stats = snippet_service.get_stats()
    return {
        "snippets": stats.get("trending_snippets", [])
    }


@router.get("/recent")
async def get_recent_snippets():
    """获取最近添加的片段"""
    stats = snippet_service.get_stats()
    return {
        "snippets": stats.get("recent_snippets", [])
    }