from datetime import datetime
from app.config.database import db

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    admission_date = db.Column(db.Date, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    
    # Relationships
    user = db.relationship('User', back_populates='student')
    
    def __repr__(self):
        return f'<Student {self.student_id}>'
    
    def to_dict(self, include_user=False):
        student_dict = {
            'id': self.id,
            'student_id': self.student_id,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'gender': self.gender,
            'address': self.address,
            'phone': self.phone,
            'admission_date': self.admission_date.isoformat() if self.admission_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        
        if include_user and self.user:
            student_dict['user'] = self.user.to_dict(include_role=True)
        
        return student_dict
    
    @classmethod
    def generate_student_id(cls, admission_year=None):
        """Generate a unique student ID based on admission year and auto-incrementing number"""
        if not admission_year:
            admission_year = datetime.utcnow().year % 100  # Last two digits of current year
            
        # Find the highest student ID for the given year
        last_student = cls.query.filter(
            cls.student_id.like(f'{admission_year}%')
        ).order_by(cls.id.desc()).first()
        
        if last_student:
            last_number = int(last_student.student_id[-4:])
            new_number = last_number + 1
        else:
            new_number = 1
            
        return f"{admission_year}{new_number:04d}"
