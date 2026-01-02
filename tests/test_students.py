import pytest
from datetime import date
from flask import Flask
from app import create_app, db
from app.models.user import User
from app.models.student import Student
from app.models.role import Role
from app.config.settings import TestingConfig


@pytest.fixture
def app():
    """Create and configure a test Flask application"""
    app = create_app()
    app.config.from_object(TestingConfig)
    
    with app.app_context():
        db.create_all()
        
        # Create test roles
        roles = [
            Role(name='admin', description='Administrator'),
            Role(name='teacher', description='Teacher'),
            Role(name='student', description='Student')
        ]
        for role in roles:
            db.session.add(role)
        db.session.commit()
        
        yield app
        
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Create a test client"""
    return app.test_client()


@pytest.fixture
def admin_token(client, app):
    """Get admin token for authenticated requests"""
    with app.app_context():
        admin_role = Role.query.filter_by(name='admin').first()
        user = User(
            username='admin',
            email='admin@test.com',
            first_name='Admin',
            last_name='User',
            role_id=admin_role.id
        )
        user.password = 'admin123'
        db.session.add(user)
        db.session.commit()
    
    response = client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'admin123'
    })
    return response.get_json()['access_token']


def test_create_student(client, admin_token):
    """Test creating a new student"""
    response = client.post('/api/students',
        headers={'Authorization': f'Bearer {admin_token}'},
        json={
            'username': 'student1',
            'email': 'student1@test.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '2000-01-15',
            'gender': 'Male',
            'address': '123 Test St',
            'phone': '1234567890'
        }
    )
    
    assert response.status_code == 201
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'student' in data


def test_list_students(client, admin_token):
    """Test listing all students"""
    response = client.get('/api/students',
        headers={'Authorization': f'Bearer {admin_token}'}
    )
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'students' in data


def test_get_student_details(client, admin_token, app):
    """Test getting student details"""
    # Create a student first
    with app.app_context():
        student_role = Role.query.filter_by(name='student').first()
        user = User(
            username='teststudent',
            email='teststudent@test.com',
            first_name='Test',
            last_name='Student',
            role_id=student_role.id
        )
        user.password = 'password123'
        db.session.add(user)
        db.session.flush()
        
        student = Student(
            user_id=user.id,
            student_id='2024001',
            date_of_birth=date(2000, 1, 1),
            gender='Male'
        )
        db.session.add(student)
        db.session.commit()
        student_id = student.id
    
    response = client.get(f'/api/students/{student_id}',
        headers={'Authorization': f'Bearer {admin_token}'}
    )
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'


def test_update_student(client, admin_token, app):
    """Test updating student information"""
    # Create a student first
    with app.app_context():
        student_role = Role.query.filter_by(name='student').first()
        user = User(
            username='updatestudent',
            email='updatestudent@test.com',
            first_name='Update',
            last_name='Test',
            role_id=student_role.id
        )
        user.password = 'password123'
        db.session.add(user)
        db.session.flush()
        
        student = Student(
            user_id=user.id,
            student_id='2024002',
            date_of_birth=date(2000, 1, 1),
            gender='Male'
        )
        db.session.add(student)
        db.session.commit()
        student_id = student.id
    
    response = client.put(f'/api/students/{student_id}',
        headers={'Authorization': f'Bearer {admin_token}'},
        json={
            'phone': '9876543210',
            'address': 'Updated Address'
        }
    )
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'