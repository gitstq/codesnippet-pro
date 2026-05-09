from .snippets import router as snippets_router
from .search import router as search_router
from .tags import router as tags_router
from .collections import router as collections_router
from .stats import router as stats_router

__all__ = [
    "snippets_router",
    "search_router",
    "tags_router",
    "collections_router",
    "stats_router",
]