from datetime import timedelta
from typing import Optional, Dict, Any, Tuple
from flask import current_app, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.security import check_password_hash

from app.models.user import User
from app.repositories.user_repo import UserRepository
from .base_service import BaseService

class AuthService(BaseService):
    def __init__(self):
        self.user_repo = UserRepository()
        super().__init__(self.user_repo)
    
    def login(self, username: str, password: str) -> Tuple[Optional[Dict[str, str]], int]:
        """Authenticate user and return JWT tokens"""
        user = self.user_repo.get_by_username(username)
        
        if not user or not check_password_hash(user.password_hash, password):
            return {
                'status': 'error',
                'message': 'Invalid username or password'
            }, 401
            
        if not user.is_active:
            return {
                'status': 'error',
                'message': 'Account is deactivated. Please contact administrator.'
            }, 403
        
        # Create tokens
        access_token = create_access_token(
            identity=user.id,
            additional_claims={
                'roles': [user.role.name] if user.role else []
            },
            expires_delta=timedelta(minutes=current_app.config.get('JWT_ACCESS_TOKEN_EXPIRES', 60))
        )
        
        refresh_token = create_refresh_token(identity=user.id)
        
        return {
            'status': 'success',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user.to_dict(include_role=True)
        }, 200
    
    def refresh_token(self) -> Tuple[Dict[str, str], int]:
        """Refresh access token using refresh token"""
        current_user_id = get_jwt_identity()
        user = self.user_repo.get_by_id(current_user_id)
        
        if not user:
            return {
                'status': 'error',
                'message': 'User not found'
            }, 404
            
        access_token = create_access_token(
            identity=user.id,
            additional_claims={
                'roles': [user.role.name] if user.role else []
            },
            expires_delta=timedelta(minutes=current_app.config.get('JWT_ACCESS_TOKEN_EXPIRES', 60))
        )
        
        return {
            'status': 'success',
            'access_token': access_token
        }, 200
    
    def change_password(self, user_id: int, current_password: str, new_password: str) -> Tuple[Dict[str, str], int]:
        """Change user password"""
        user = self.user_repo.get_by_id(user_id)
        
        if not user:
            return {
                'status': 'error',
                'message': 'User not found'
            }, 404
            
        if not check_password_hash(user.password_hash, current_password):
            return {
                'status': 'error',
                'message': 'Current password is incorrect'
            }, 400
            
        # Update password
        self.user_repo.update_user(user.id, password=new_password)
        
        return {
            'status': 'success',
            'message': 'Password updated successfully'
        }, 200
    
    def get_authenticated_user(self) -> Tuple[Optional[Dict[str, Any]], int]:
        """Get the currently authenticated user"""
        user = self.get_current_user()
        
        if not user:
            return {
                'status': 'error',
                'message': 'User not authenticated'
            }, 401
            
        return {
            'status': 'success',
            'user': user.to_dict(include_role=True)
        }, 200
    
    def register_user(self, user_data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        """Register a new user"""
        # Check if username or email already exists
        if self.user_repo.get_by_username(user_data.get('username')):
            return {
                'status': 'error',
                'message': 'Username already exists'
            }, 400
            
        if self.user_repo.get_by_email(user_data.get('email')):
            return {
                'status': 'error',
                'message': 'Email already registered'
            }, 400
        
        # Create user
        try:
            user = self.user_repo.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                role_id=user_data.get('role_id', 3),  # Default to student role
                first_name=user_data.get('first_name', ''),
                last_name=user_data.get('last_name', '')
            )
            
            return {
                'status': 'success',
                'message': 'User registered successfully',
                'user': user.to_dict(include_role=True)
            }, 201
            
        except Exception as e:
            current_app.logger.error(f"Error registering user: {str(e)}")
            return {
                'status': 'error',
                'message': 'Failed to register user'
            }, 500
