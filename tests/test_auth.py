import pytest
from flask import Flask
from app import create_app, db
from app.models.user import User
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
def admin_user(app):
    """Create an admin user for testing"""
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
        return user


def test_register_user(client):
    """Test user registration"""
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'first_name': 'Test',
        'last_name': 'User'
    })
    
    assert response.status_code == 201
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'user' in data


def test_login_success(client, admin_user):
    """Test successful login"""
    response = client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'admin123'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'access_token' in data
    assert 'refresh_token' in data


def test_login_invalid_credentials(client):
    """Test login with invalid credentials"""
    response = client.post('/api/auth/login', json={
        'username': 'nonexistent',
        'password': 'wrongpassword'
    })
    
    assert response.status_code == 401
    data = response.get_json()
    assert data['status'] == 'error'


def test_get_current_user(client, admin_user):
    """Test getting current user info"""
    # Login first
    login_response = client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'admin123'
    })
    token = login_response.get_json()['access_token']
    
    # Get current user
    response = client.get('/api/auth/me', headers={
        'Authorization': f'Bearer {token}'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['user']['username'] == 'admin'


def test_change_password(client, admin_user):
    """Test password change"""
    # Login first
    login_response = client.post('/api/auth/login', json={
        'username': 'admin',
        'password': 'admin123'
    })
    token = login_response.get_json()['access_token']
    
    # Change password
    response = client.post('/api/auth/change-password', 
        headers={'Authorization': f'Bearer {token}'},
        json={
            'current_password': 'admin123',
            'new_password': 'newpassword123'
        }
    )
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'