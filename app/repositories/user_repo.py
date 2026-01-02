from typing import Optional, Dict, Any, List
from app.models.user import User
from .base_repo import BaseRepository
from app import db

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
    
    def get_by_username(self, username: str) -> Optional[User]:
        return self.first(username=username)
    
    def get_by_email(self, email: str) -> Optional[User]:
        return self.first(email=email)
    
    def create_user(self, username: str, email: str, password: str, role_id: int, **kwargs) -> User:
        user = User(
            username=username,
            email=email,
            role_id=role_id,
            **kwargs
        )
        user.password = password  # This will hash the password
        db.session.add(user)
        db.session.commit()
        return user
    
    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        user = self.get_by_id(user_id)
        if not user:
            return None
            
        # Handle password update separately to ensure hashing
        if 'password' in kwargs:
            user.password = kwargs.pop('password')
            
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
                
        db.session.commit()
        return user
    
    def search_users(self, search_term: str, role_id: int = None) -> List[User]:
        query = User.query
        
        if search_term:
            search = f"%{search_term}%"
            query = query.filter(
                (User.username.ilike(search)) |
                (User.email.ilike(search)) |
                (User.first_name.ilike(search)) |
                (User.last_name.ilike(search))
            )
            
        if role_id is not None:
            query = query.filter_by(role_id=role_id)
            
        return query.all()
    
    def get_users_by_role(self, role_name: str) -> List[User]:
        from app.models.role import Role
        return db.session.query(User).join(Role).filter(Role.name == role_name).all()
    
    def get_students(self) -> List[User]:
        return self.get_users_by_role('student')
    
    def get_teachers(self) -> List[User]:
        return self.get_users_by_role('teacher')
    
    def get_admins(self) -> List[User]:
        return self.get_users_by_role('admin')
