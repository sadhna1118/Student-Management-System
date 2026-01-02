from typing import List, Dict, Any, Optional, Tuple
from datetime import date
from flask import current_app
from app.models.student import Student
from app.repositories.student_repo import StudentRepository
from app.repositories.user_repo import UserRepository
from .base_service import BaseService

class StudentService(BaseService):
    def __init__(self):
        self.student_repo = StudentRepository()
        self.user_repo = UserRepository()
        super().__init__(self.student_repo)
    
    def create_student(self, user_data: Dict[str, Any], student_data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        """Create a new student with user account"""
        # First create the user
        user_response, status_code = self._create_user_account(user_data, role_name='student')
        
        if status_code != 201:  # If user creation failed
            return user_response, status_code
            
        user = user_response['user']
        
        # Then create the student profile
        try:
            student = self.student_repo.create_student(
                user_id=user['id'],
                **student_data
            )
            
            # Get the complete student data with user details
            result = self.student_repo.get_student_with_details(student.id)
            
            return {
                'status': 'success',
                'message': 'Student created successfully',
                'student': result
            }, 201
            
        except Exception as e:
            # Rollback user creation if student creation fails
            self.user_repo.delete(user['id'])
            current_app.logger.error(f"Error creating student: {str(e)}")
            return {
                'status': 'error',
                'message': 'Failed to create student profile'
            }, 500
    
    def update_student(self, student_id: int, student_data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        """Update student information"""
        student = self.student_repo.get_by_id(student_id)
        
        if not student:
            return {
                'status': 'error',
                'message': 'Student not found'
            }, 404
            
        # Separate user and student data
        user_data = {}
        student_updates = {}
        
        for key, value in student_data.items():
            if hasattr(Student, key):
                student_updates[key] = value
            else:
                user_data[key] = value
        
        # Update student data
        if student_updates:
            self.student_repo.update(student_id, **student_updates)
        
        # Update user data if any
        if user_data and student.user:
            self.user_repo.update_user(student.user.id, **user_data)
        
        # Get updated student data
        updated_student = self.student_repo.get_student_with_details(student_id)
        
        return {
            'status': 'success',
            'message': 'Student updated successfully',
            'student': updated_student
        }, 200
    
    def get_student_details(self, student_id: int) -> Tuple[Dict[str, Any], int]:
        """Get detailed information about a student"""
        student = self.student_repo.get_student_with_details(student_id)
        
        if not student:
            return {
                'status': 'error',
                'message': 'Student not found'
            }, 404
            
        return {
            'status': 'success',
            'student': student
        }, 200
    
    def list_students(self, search_term: str = None, **filters) -> Tuple[Dict[str, Any], int]:
        """List all students with optional filtering"""
        try:
            students = self.student_repo.get_students_with_details()
            
            # Apply search filter if provided
            if search_term:
                search = search_term.lower()
                students = [
                    s for s in students 
                    if (search in s['student_id'].lower() or
                        search in s['user'].get('first_name', '').lower() or
                        search in s['user'].get('last_name', '').lower() or
                        search in s['user'].get('email', '').lower())
                ]
            
            # Apply additional filters
            for key, value in filters.items():
                if value is not None:
                    students = [s for s in students if str(s.get(key, '')).lower() == str(value).lower()]
            
            return {
                'status': 'success',
                'count': len(students),
                'students': students
            }, 200
            
        except Exception as e:
            current_app.logger.error(f"Error listing students: {str(e)}")
            return {
                'status': 'error',
                'message': 'Failed to retrieve students'
            }, 500
    
    def _create_user_account(self, user_data: Dict[str, Any], role_name: str) -> Tuple[Dict[str, Any], int]:
        """Helper method to create a user account with the specified role"""
        from app.models.role import Role
        
        # Get the role ID
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            return {
                'status': 'error',
                'message': f'Role {role_name} not found'
            }, 500
            
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
        
        try:
            # Create the user
            user = self.user_repo.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                role_id=role.id,
                first_name=user_data.get('first_name', ''),
                last_name=user_data.get('last_name', '')
            )
            
            return {
                'status': 'success',
                'message': 'User account created successfully',
                'user': user.to_dict(include_role=True)
            }, 201
            
        except Exception as e:
            current_app.logger.error(f"Error creating user account: {str(e)}")
            return {
                'status': 'error',
                'message': 'Failed to create user account'
            }, 500
