from typing import Type, TypeVar, Generic, Optional, Dict, Any, List
from functools import wraps
from flask import jsonify, request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt
from app.models.user import User
from app.repositories.user_repo import UserRepository

T = TypeVar('T')

class BaseService:
    def __init__(self, repository):
        self.repository = repository
    
    def get_all(self) -> List[Dict[str, Any]]:
        """Get all items"""
        items = self.repository.get_all()
        return [item.to_dict() for item in items]
    
    def get_by_id(self, item_id: int) -> Optional[Dict[str, Any]]:
        """Get item by ID"""
        item = self.repository.get_by_id(item_id)
        return item.to_dict() if item else None
    
    def create(self, **kwargs) -> Dict[str, Any]:
        """Create a new item"""
        item = self.repository.create(**kwargs)
        return item.to_dict() if item else None
    
    def update(self, item_id: int, **kwargs) -> Optional[Dict[str, Any]]:
        """Update an existing item"""
        item = self.repository.update(item_id, **kwargs)
        return item.to_dict() if item else None
    
    def delete(self, item_id: int) -> bool:
        """Delete an item"""
        return self.repository.delete(item_id)
    
    @staticmethod
    def require_roles(*roles):
        """Decorator to require specific roles for a route"""
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                verify_jwt_in_request()
                current_user_id = get_jwt_identity()
                current_user_roles = get_jwt().get('roles', [])
                
                # Check if user has any of the required roles
                if not any(role in current_user_roles for role in roles):
                    return jsonify({
                        'status': 'error',
                        'message': 'Insufficient permissions'
                    }), 403
                
                return f(*args, **kwargs)
            return decorated_function
        return decorator
    
    @staticmethod
    def get_current_user() -> Optional[User]:
        """Get the current authenticated user"""
        try:
            verify_jwt_in_request(optional=True)
            user_id = get_jwt_identity()
            if user_id:
                return UserRepository().get_by_id(user_id)
            return None
        except:
            return None
