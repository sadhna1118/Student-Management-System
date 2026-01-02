"""
Custom decorators for the application
"""
from functools import wraps
from flask import request, jsonify
from app.utils.validators import validate_email, validate_password


def validate_registration(f):
    """Validate user registration data"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = request.get_json()
        
        # Check required fields
        required_fields = ['username', 'email', 'password']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'status': 'error',
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Validate email
        if not validate_email(data['email']):
            return jsonify({
                'status': 'error',
                'message': 'Invalid email format'
            }), 400
        
        # Validate password
        is_valid, message = validate_password(data['password'])
        if not is_valid:
            return jsonify({
                'status': 'error',
                'message': message
            }), 400
        
        return f(*args, **kwargs)
    return decorated_function


def validate_student_creation(f):
    """Validate student creation data"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = request.get_json()
        
        # Check required fields
        required_fields = ['username', 'email', 'password', 'first_name', 'last_name', 'date_of_birth']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'status': 'error',
                    'message': f'Missing required field: {field}'
                }), 400
        
        return f(*args, **kwargs)
    return decorated_function