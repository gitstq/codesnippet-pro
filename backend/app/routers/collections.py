from typing import List
from fastapi import APIRouter, HTTPException
from app.models.collection import Collection, CollectionCreate, CollectionUpdate, CollectionList
from app.services.collection_service import CollectionService

router = APIRouter(prefix="/collections", tags=["collections"])
collection_service = CollectionService()


@router.get("", response_model=List[Collection])
async def get_collections():
    """获取所有集合"""
    return collection_service.get_all_collections()


@router.post("", response_model=Collection)
async def create_collection(collection: CollectionCreate):
    """创建集合"""
    return collection_service.create_collection(collection.model_dump())


@router.get("/{collection_id}", response_model=Collection)
async def get_collection(collection_id: str):
    """获取单个集合"""
    collection = collection_service.get_collection(collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection


@router.put("/{collection_id}", response_model=Collection)
async def update_collection(collection_id: str, collection: CollectionUpdate):
    """更新集合"""
    update_data = {k: v for k, v in collection.model_dump().items() if v is not None}
    updated = collection_service.update_collection(collection_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Collection not found")
    return updated


@router.delete("/{collection_id}")
async def delete_collection(collection_id: str):
    """删除集合"""
    deleted = collection_service.delete_collection(collection_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Collection not found")
    return {"message": "Collection deleted successfully"}


@router.post("/{collection_id}/snippets/{snippet_id}")
async def add_snippet_to_collection(collection_id: str, snippet_id: str):
    """添加片段到集合"""
    success = collection_service.add_snippet_to_collection(collection_id, snippet_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to add snippet to collection")
    return {"message": "Snippet added to collection"}


@router.delete("/{collection_id}/snippets/{snippet_id}")
async def remove_snippet_from_collection(collection_id: str, snippet_id: str):
    """从集合中移除片段"""
    success = collection_service.remove_snippet_from_collection(collection_id, snippet_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to remove snippet from collection")
    return {"message": "Snippet removed from collection"}