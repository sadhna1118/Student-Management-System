# This file makes the models directory a Python package
# Import all models here to make them available when importing from app.models

# Import models here to ensure they are registered with SQLAlchemy
from .role import Role
from .user import User
from .student import Student

# Export models
def init_app(app):
    # This function can be used to perform any model-related initialization
    pass
