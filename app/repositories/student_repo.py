from typing import Optional, List, Dict, Any
from datetime import date
from app.models.student import Student
from app.models.user import User
from .base_repo import BaseRepository
from app import db

class StudentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Student)
    
    def create_student(self, user_id: int, date_of_birth: date, **kwargs) -> Student:
        """Create a new student with auto-generated student ID"""
        # Generate student ID based on admission year
        admission_year = date.today().year
        student_id = Student.generate_student_id(admission_year)
        
        student = Student(
            user_id=user_id,
            student_id=student_id,
            date_of_birth=date_of_birth,
            **kwargs
        )
        
        db.session.add(student)
        db.session.commit()
        return student
    
    def get_by_user_id(self, user_id: int) -> Optional[Student]:
        return self.first(user_id=user_id)
    
    def get_by_student_id(self, student_id: str) -> Optional[Student]:
        return self.first(student_id=student_id)
    
    def search_students(self, search_term: str = None, **filters) -> List[Student]:
        query = Student.query.join(User)
        
        if search_term:
            search = f"%{search_term}%"
            query = query.filter(
                (Student.student_id.ilike(search)) |
                (User.first_name.ilike(search)) |
                (User.last_name.ilike(search)) |
                (User.email.ilike(search)) |
                (User.phone.ilike(search) if hasattr(User, 'phone') else False)
            )
        
        # Apply additional filters
        for key, value in filters.items():
            if hasattr(Student, key):
                query = query.filter(getattr(Student, key) == value)
            elif hasattr(User, key):
                query = query.filter(getattr(User, key) == value)
        
        return query.order_by(User.last_name, User.first_name).all()
    
    def update_student(self, student_id: int, **kwargs) -> Optional[Student]:
        student = self.get_by_id(student_id)
        if not student:
            return None
            
        # Handle user data if provided
        user_data = {}
        user_fields = ['first_name', 'last_name', 'email', 'phone', 'is_active']
        
        for field in user_fields:
            if field in kwargs:
                user_data[field] = kwargs.pop(field)
        
        # Update student fields
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        
        # Update user fields if any
        if user_data and hasattr(student, 'user'):
            for key, value in user_data.items():
                if hasattr(student.user, key):
                    setattr(student.user, key, value)
        
        db.session.commit()
        return student
    
    def get_students_by_class(self, class_id: int) -> List[Student]:
        # This is a placeholder - you'll need to implement the StudentClass model
        # and relationship to use this method
        # Example: return Student.query.join(StudentClass).filter(StudentClass.class_id == class_id).all()
        raise NotImplementedError("This method requires implementation of class enrollment")
    
    def get_students_with_details(self) -> List[Dict[str, Any]]:
        """Get all students with their user details"""
        students = db.session.query(Student, User).join(User).all()
        
        result = []
        for student, user in students:
            student_data = student.to_dict()
            student_data['user'] = user.to_dict(include_role=True)
            result.append(student_data)
            
        return result
    
    def get_student_with_details(self, student_id: int) -> Optional[Dict[str, Any]]:
        """Get a single student with full details"""
        result = db.session.query(Student, User).join(User).filter(Student.id == student_id).first()
        
        if not result:
            return None
            
        student, user = result
        student_data = student.to_dict()
        student_data['user'] = user.to_dict(include_role=True)
        
        # Add additional details like enrollments, grades, etc. here
        # Example: student_data['enrollments'] = [e.to_dict() for e in student.enrollments]
        
        return student_data
