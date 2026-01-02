from typing import TypeVar, Type, List, Dict, Any, Optional
from app.config.database import db

T = TypeVar('T', bound=db.Model)

class BaseRepository:
    def __init__(self, model: Type[T]):
        self.model = model
    
    def get_by_id(self, id: int) -> Optional[T]:
        return self.model.query.get(id)
    
    def get_all(self) -> List[T]:
        return self.model.query.all()
    
    def create(self, **kwargs) -> T:
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance
    
    def update(self, id: int, **kwargs) -> Optional[T]:
        instance = self.get_by_id(id)
        if instance:
            for key, value in kwargs.items():
                if hasattr(instance, key):
                    setattr(instance, key, value)
            db.session.commit()
        return instance
    
    def delete(self, id: int) -> bool:
        instance = self.get_by_id(id)
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return True
        return False
    
    def filter_by(self, **filters) -> List[T]:
        return self.model.query.filter_by(**filters).all()
    
    def first(self, **filters) -> Optional[T]:
        return self.model.query.filter_by(**filters).first()
    
    def exists(self, **filters) -> bool:
        return db.session.query(
            self.model.query.filter_by(**filters).exists()
        ).scalar()
