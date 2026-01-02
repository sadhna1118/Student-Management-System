from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()


@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['username', 'email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({
            'status': 'error',
            'message': 'Missing required fields'
        }), 400
    
    response, status_code = auth_service.register_user(data)
    return jsonify(response), status_code


@auth_bp.route('/login', methods=['POST'])
def login():
    """Login user and return JWT tokens"""
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({
            'status': 'error',
            'message': 'Username and password are required'
        }), 400
    
    response, status_code = auth_service.login(
        username=data['username'],
        password=data['password']
    )
    return jsonify(response), status_code


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Refresh access token"""
    response, status_code = auth_service.refresh_token()
    return jsonify(response), status_code


@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current authenticated user"""
    response, status_code = auth_service.get_authenticated_user()
    return jsonify(response), status_code


@auth_bp.route('/change-password', methods=['POST'])
@jwt_required()
def change_password():
    """Change user password"""
    data = request.get_json()
    current_user_id = get_jwt_identity()
    
    if not data or not data.get('current_password') or not data.get('new_password'):
        return jsonify({
            'status': 'error',
            'message': 'Current password and new password are required'
        }), 400
    
    response, status_code = auth_service.change_password(
        user_id=current_user_id,
        current_password=data['current_password'],
        new_password=data['new_password']
    )
    return jsonify(response), status_code


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """Logout user (client should discard the token)"""
    return jsonify({
        'status': 'success',
        'message': 'Successfully logged out'
    }), 200