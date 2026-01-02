from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.base_service import BaseService
from app.repositories.user_repo import UserRepository
from app.models.role import Role
from app import db

admin_bp = Blueprint('admin', __name__)
user_repo = UserRepository()


@admin_bp.route('/users', methods=['GET'])
@jwt_required()
@BaseService.require_roles('admin')
def list_users():
    """List all users with optional filtering"""
    role_name = request.args.get('role', None)
    search = request.args.get('search', None)
    
    if role_name:
        users = user_repo.get_users_by_role(role_name)
    elif search:
        users = user_repo.search_users(search)
    else:
        users = user_repo.get_all()
    
    return jsonify({
        'status': 'success',
        'count': len(users),
        'users': [user.to_dict(include_role=True) for user in users]
    }), 200


@admin_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
@BaseService.require_roles('admin')
def get_user(user_id):
    """Get user details by ID"""
    user = user_repo.get_by_id(user_id)
    
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found'
        }), 404
    
    return jsonify({
        'status': 'success',
        'user': user.to_dict(include_role=True)
    }), 200


@admin_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
@BaseService.require_roles('admin')
def update_user(user_id):
    """Update user information"""
    data = request.get_json()
    
    user = user_repo.update_user(user_id, **data)
    
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found'
        }), 404
    
    return jsonify({
        'status': 'success',
        'message': 'User updated successfully',
        'user': user.to_dict(include_role=True)
    }), 200


@admin_bp.route('/users/<int:user_id>/deactivate', methods=['POST'])
@jwt_required()
@BaseService.require_roles('admin')
def deactivate_user(user_id):
    """Deactivate a user account"""
    user = user_repo.update_user(user_id, is_active=False)
    
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found'
        }), 404
    
    return jsonify({
        'status': 'success',
        'message': 'User deactivated successfully'
    }), 200


@admin_bp.route('/users/<int:user_id>/activate', methods=['POST'])
@jwt_required()
@BaseService.require_roles('admin')
def activate_user(user_id):
    """Activate a user account"""
    user = user_repo.update_user(user_id, is_active=True)
    
    if not user:
        return jsonify({
            'status': 'error',
            'message': 'User not found'
        }), 404
    
    return jsonify({
        'status': 'success',
        'message': 'User activated successfully'
    }), 200


@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
@BaseService.require_roles('admin')
def delete_user(user_id):
    """Delete a user account"""
    success = user_repo.delete(user_id)
    
    if success:
        return jsonify({
            'status': 'success',
            'message': 'User deleted successfully'
        }), 200
    else:
        return jsonify({
            'status': 'error',
            'message': 'User not found'
        }), 404


@admin_bp.route('/roles', methods=['GET'])
@jwt_required()
@BaseService.require_roles('admin')
def list_roles():
    """List all available roles"""
    roles = Role.query.all()
    
    return jsonify({
        'status': 'success',
        'roles': [role.to_dict() for role in roles]
    }), 200


@admin_bp.route('/stats', methods=['GET'])
@jwt_required()
@BaseService.require_roles('admin')
def get_system_stats():
    """Get system statistics"""
    from app.models.user import User
    from app.models.student import Student
    
    total_users = User.query.count()
    active_users = User.query.filter_by(is_active=True).count()
    total_students = Student.query.count()
    
    # Count users by role
    role_counts = db.session.query(
        Role.name,
        db.func.count(User.id)
    ).join(User).group_by(Role.name).all()
    
    return jsonify({
        'status': 'success',
        'stats': {
            'total_users': total_users,
            'active_users': active_users,
            'inactive_users': total_users - active_users,
            'total_students': total_students,
            'users_by_role': {role: count for role, count in role_counts}
        }
    }), 200