"""
Initialize the database with default data
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from datetime import date
from sqlalchemy import select


def init_db():
    """Initialize database with default roles and admin user"""
    app = create_app()
    
    with app.app_context():
        # Import models here to ensure they are registered before creating tables
        from app.models.role import Role
        from app.models.user import User
        from app.models.student import Student
        
        # Create all tables
        db.create_all()
        print("✓ Database tables created")
        
        # Create default roles
        roles_data = [
            {'name': 'admin', 'description': 'Administrator with full access'},
            {'name': 'teacher', 'description': 'Teacher with limited access'},
            {'name': 'student', 'description': 'Basic student access'}
        ]
        
        for role_data in roles_data:
            # Use new SQLAlchemy 2.0 style query
            stmt = select(Role).where(Role.name == role_data['name'])
            role = db.session.execute(stmt).scalar_one_or_none()
            
            if not role:
                role = Role(**role_data)
                db.session.add(role)
                print(f"✓ Created role: {role_data['name']}")
            else:
                print(f"- Role already exists: {role_data['name']}")
        
        db.session.commit()
        
        # Create default admin user
        stmt = select(Role).where(Role.name == 'admin')
        admin_role = db.session.execute(stmt).scalar_one_or_none()
        
        stmt = select(User).where(User.username == 'admin')
        admin = db.session.execute(stmt).scalar_one_or_none()
        
        if not admin:
            admin = User(
                username='admin',
                email='admin@example.com',
                first_name='System',
                last_name='Administrator',
                role_id=admin_role.id,
                is_active=True
            )
            admin.password = 'admin123'  # Change this in production!
            db.session.add(admin)
            db.session.commit()
            print("✓ Created default admin user (username: admin, password: admin123)")
            print("  ⚠ IMPORTANT: Change the default password immediately!")
        else:
            print("- Admin user already exists")
        
        print("\n✓ Database initialization complete!")


if __name__ == '__main__':
    init_db()