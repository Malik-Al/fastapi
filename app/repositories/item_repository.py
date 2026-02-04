from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data:ItemCreate) -> Item:
        item = Item(name=data.name, description=data.description)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
    
    def get_by_id(self, item_id: int) -> Item | None:
        return self.db.query(Item).filter(item.id == item_id).first()
    
    def get_all(self) -> list[Item]:
        return self.db.query(Item).all()
    
    def update(self, item_id: int, data: ItemUpdate)  -> Item | None:
        item = self.get_by_id(item_id)

        if not item:
            return None
        if data.name is not None:
            item.name = data.name
        if data.description is not None:
            item.description = data.description

        self.db.commit()
        self.db.refresh(item)
        return self    
    
    def dalete(self, item_id: int) -> bool:
        item = self.get_by_id(item_id)
        if not item:
            return False
        
        self.db.delete(item)
        self.db.commit()
        return True