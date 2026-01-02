"""
Seed the database with sample data for testing
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.user import User
from app.models.role import Role
from app.models.student import Student
from faker import Faker
from datetime import date, timedelta
import random


def seed_data():
    """Seed database with sample students"""
    app = create_app()
    fake = Faker()
    
    with app.app_context():
        student_role = Role.query.filter_by(name='student').first()
        
        if not student_role:
            print("Error: Student role not found. Please run init_db.py first.")
            return
        
        print("Generating sample student data...")
        
        # Create 20 sample students
        for i in range(20):
            # Create user
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}{i}"
            email = f"{username}@example.com"
            
            # Check if user already exists
            if User.query.filter_by(username=username).first():
                continue
            
            user = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role_id=student_role.id,
                is_active=True
            )
            user.password = 'password123'
            db.session.add(user)
            db.session.flush()
            
            # Create student profile
            admission_year = random.randint(2020, 2024)
            birth_year = admission_year - random.randint(16, 20)
            
            student = Student(
                user_id=user.id,
                student_id=Student.generate_student_id(admission_year % 100),
                date_of_birth=date(birth_year, random.randint(1, 12), random.randint(1, 28)),
                gender=random.choice(['Male', 'Female', 'Other']),
                address=fake.address().replace('\n', ', '),
                phone=fake.phone_number()[:20],
                admission_date=date(admission_year, random.randint(1, 12), 1)
            )
            db.session.add(student)
            
            print(f"✓ Created student: {first_name} {last_name} ({student.student_id})")
        
        db.session.commit()
        print(f"\n✓ Successfully created sample data!")


if __name__ == '__main__':
    seed_data()