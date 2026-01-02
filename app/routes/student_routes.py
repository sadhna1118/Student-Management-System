from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.student_service import StudentService
from app.services.base_service import BaseService
from datetime import datetime

student_bp = Blueprint('students', __name__)
student_service = StudentService()


@student_bp.route('', methods=['GET'])
@jwt_required()
@BaseService.require_roles('admin', 'teacher')
def list_students():
    """List all students with optional filtering"""
    search_term = request.args.get('search', None)
    gender = request.args.get('gender', None)
    
    filters = {}
    if gender:
        filters['gender'] = gender
    
    response, status_code = student_service.list_students(
        search_term=search_term,
        **filters
    )
    return jsonify(response), status_code


@student_bp.route('/<int:student_id>', methods=['GET'])
@jwt_required()
def get_student(student_id):
    """Get student details by ID"""
    response, status_code = student_service.get_student_details(student_id)
    return jsonify(response), status_code


@student_bp.route('', methods=['POST'])
@jwt_required()
@BaseService.require_roles('admin')
def create_student():
    """Create a new student"""
    data = request.get_json()
    
    # Validate required fields
    required_user_fields = ['username', 'email', 'password', 'first_name', 'last_name']
    required_student_fields = ['date_of_birth']
    
    if not all(field in data for field in required_user_fields):
        return jsonify({
            'status': 'error',
            'message': 'Missing required user fields'
        }), 400
    
    if not all(field in data for field in required_student_fields):
        return jsonify({
            'status': 'error',
            'message': 'Missing required student fields'
        }), 400
    
    # Separate user and student data
    user_data = {
        'username': data['username'],
        'email': data['email'],
        'password': data['password'],
        'first_name': data['first_name'],
        'last_name': data['last_name']
    }
    
    # Parse date_of_birth
    try:
        date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({
            'status': 'error',
            'message': 'Invalid date format. Use YYYY-MM-DD'
        }), 400
    
    student_data = {
        'date_of_birth': date_of_birth,
        'gender': data.get('gender'),
        'address': data.get('address'),
        'phone': data.get('phone'),
        'admission_date': datetime.strptime(data['admission_date'], '%Y-%m-%d').date() if data.get('admission_date') else None
    }
    
    response, status_code = student_service.create_student(user_data, student_data)
    return jsonify(response), status_code


@student_bp.route('/<int:student_id>', methods=['PUT'])
@jwt_required()
@BaseService.require_roles('admin', 'teacher')
def update_student(student_id):
    """Update student information"""
    data = request.get_json()
    
    # Parse dates if provided
    if 'date_of_birth' in data:
        try:
            data['date_of_birth'] = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({
                'status': 'error',
                'message': 'Invalid date_of_birth format. Use YYYY-MM-DD'
            }), 400
    
    if 'admission_date' in data:
        try:
            data['admission_date'] = datetime.strptime(data['admission_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({
                'status': 'error',
                'message': 'Invalid admission_date format. Use YYYY-MM-DD'
            }), 400
    
    response, status_code = student_service.update_student(student_id, data)
    return jsonify(response), status_code


@student_bp.route('/<int:student_id>', methods=['DELETE'])
@jwt_required()
@BaseService.require_roles('admin')
def delete_student(student_id):
    """Delete a student"""
    success = student_service.delete(student_id)
    
    if success:
        return jsonify({
            'status': 'success',
            'message': 'Student deleted successfully'
        }), 200
    else:
        return jsonify({
            'status': 'error',
            'message': 'Student not found'
        }), 404