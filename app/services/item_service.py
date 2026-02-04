from sqlalchemy.orm import Session
from app.repositories.item_repository import ItemRepository
from app.schemas.item import ItemCreate, ItemUpdate

class ItemService:

    def __init__(self, db: Session):
        self.repo  = ItemRepository(db)

    def create_item(self, data: ItemCreate):
        return self.repo.create(data)    
    
    def get_item(self, item_id: int):
        return self.repo.get_by_id(item_id)
    
    def get_items(self):
        return self.repo.get_all()
    
    def update_item(self, item_id: int, data: ItemUpdate):
        return self.repo.update(item_id, data)\
        
    def delete_item(self, item_id: int):
        return self.repo.delete(item_id)