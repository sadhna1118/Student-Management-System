"""
Check if the application is properly set up
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def check_setup():
    """Check application setup"""
    print("🔍 Checking Student Management System setup...\n")
    
    issues = []
    warnings = []
    
    # Check Python version
    print("✓ Checking Python version...")
    if sys.version_info < (3, 10):
        issues.append("Python 3.10 or higher is required")
    else:
        print(f"  Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check required packages
    print("\n✓ Checking required packages...")
    required_packages = [
        'flask',
        'flask_sqlalchemy',
        'flask_jwt_extended',
        'flask_migrate',
        'flask_cors',
        'werkzeug',
        'sqlalchemy',
        'reportlab',
        'openpyxl',
        'pytest'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✓ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"  ✗ {package} - NOT INSTALLED")
    
    if missing_packages:
        issues.append(f"Missing packages: {', '.join(missing_packages)}")
    
    # Check .env file
    print("\n✓ Checking configuration...")
    if not os.path.exists('.env'):
        warnings.append(".env file not found - using default configuration")
        print("  ⚠ .env file not found")
    else:
        print("  ✓ .env file exists")
    
    # Check database
    print("\n✓ Checking database...")
    try:
        from app import create_app, db
        app = create_app()
        with app.app_context():
            db.create_all()
            from app.models.role import Role
            role_count = Role.query.count()
            if role_count == 0:
                warnings.append("Database has no roles - run scripts/init_db.py")
                print("  ⚠ No roles found in database")
            else:
                print(f"  ✓ Database configured with {role_count} roles")
    except Exception as e:
        issues.append(f"Database error: {str(e)}")
        print(f"  ✗ Database error: {str(e)}")
    
    # Check directory structure
    print("\n✓ Checking directory structure...")
    required_dirs = [
        'app',
        'app/models',
        'app/services',
        'app/repositories',
        'app/routes',
        'app/config',
        'scripts',
        'tests'
    ]
    
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"  ✓ {dir_path}")
        else:
            issues.append(f"Missing directory: {dir_path}")
            print(f"  ✗ {dir_path}")
    
    # Summary
    print("\n" + "="*60)
    if not issues and not warnings:
        print("✅ All checks passed! The application is ready to run.")
        print("\nTo start the application, run:")
        print("  python run.py")
    else:
        if issues:
            print("❌ Setup Issues Found:")
            for issue in issues:
                print(f"  - {issue}")
        
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"  - {warning}")
        
        if issues:
            print("\nPlease fix the issues above before running the application.")
            return False
    
    print("="*60)
    return True


if __name__ == '__main__':
    success = check_setup()
    sys.exit(0 if success else 1)