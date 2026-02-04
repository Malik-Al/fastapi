from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.item_service import ItemService
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

def get_service(db: Session = Depends(get_db)):
    return ItemService(db)

@router.post("/", response_model=ItemResponse)
def create_item(data: ItemCreate, service: ItemService = Depends(get_service)):
    return service.create_item(data)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, service: ItemService = Depends(get_service)):
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/", response_model=list[ItemResponse])
def get_items(service: ItemService = Depends(get_service)):
    return service.get_items()

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, data: ItemUpdate, service: ItemService = Depends(get_service)):
    item = service.update_item(item_id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int, service: ItemService = Depends(get_service)):
    success = service.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}