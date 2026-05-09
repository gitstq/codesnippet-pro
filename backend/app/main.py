"""
CodeSnippet Pro - 智能代码片段管理工具
后端API服务
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.routers import (
    snippets_router,
    search_router,
    tags_router,
    collections_router,
    stats_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时执行
    print("🚀 CodeSnippet Pro API 服务启动中...")
    yield
    # 关闭时执行
    print("👋 CodeSnippet Pro API 服务已关闭")


# 创建FastAPI应用
app = FastAPI(
    title="CodeSnippet Pro API",
    description="智能代码片段管理工具API",
    version="1.0.0",
    lifespan=lifespan
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(snippets_router, prefix="/api")
app.include_router(search_router, prefix="/api")
app.include_router(tags_router, prefix="/api")
app.include_router(collections_router, prefix="/api")
app.include_router(stats_router, prefix="/api")


@app.get("/")
async def root():
    """根路径"""
    return {
        "name": "CodeSnippet Pro API",
        "version": "1.0.0",
        "description": "智能代码片段管理工具",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "service": "codesnippet-pro"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)