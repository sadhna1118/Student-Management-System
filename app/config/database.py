from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def init_db(app):
    with app.app_context():
        # Import all models here to ensure they are registered with SQLAlchemy
        from app.models.user import User
        from app.models.student import Student
        from app.models.role import Role
        
        # Create all database tables
        db.create_all()
        
        # Create default roles if they don't exist
        create_default_roles()

def create_default_roles():
    from app.models.role import Role
    
    default_roles = [
        {'name': 'admin', 'description': 'Administrator with full access'},
        {'name': 'teacher', 'description': 'Teacher with limited access'},
        {'name': 'student', 'description': 'Basic student access'}
    ]
    
    for role_data in default_roles:
        role = Role.query.filter_by(name=role_data['name']).first()
        if not role:
            role = Role(**role_data)
            db.session.add(role)
    
    db.session.commit()
