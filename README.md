# Student Management System

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/sadhna1118/Student-Management-System)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

A comprehensive student management system built with Python Flask, featuring user authentication, role-based access control, student record management, and report generation.

## 🚀 Quick Deploy

**Deploy to live server in 5 minutes:**

1. Click the **"Deploy to Render"** button above
2. Create free Render account
3. Your app will be live!

For detailed deployment instructions, see [DEPLOYMENT_LIVE.md](DEPLOYMENT_LIVE.md)

## Features

- 🔐 **Authentication & Authorization**
  - JWT-based authentication with refresh tokens
  - Role-based access control (Admin, Teacher, Student)
  - Secure password hashing with Werkzeug
  - Password strength validation

- 👨‍🎓 **Student Management**
  - Create, read, update, and delete student records
  - Auto-generated unique student IDs
  - Comprehensive student profiles
  - Search and filter functionality
  - User account activation/deactivation

- 👥 **User Management (Admin)**
  - Manage all user accounts
  - List users by role
  - Activate/deactivate accounts
  - View system statistics

- 📊 **Report Generation**
  - Generate student reports in PDF format
  - Export data to Excel spreadsheets
  - Individual student profile reports
  - Analytics dashboard with statistics
  - Gender distribution analysis

- 🏗️ **Architecture**
  - Repository pattern for data access
  - Service layer for business logic
  - RESTful API design
  - SQLAlchemy ORM with Flask-Migrate
  - CORS support for frontend integration
  - Comprehensive error handling
  - Structured logging

- 🐳 **DevOps**
  - Docker and Docker Compose support
  - Production-ready Gunicorn configuration
  - Health check endpoints
  - Automated deployment scripts

## Tech Stack

- **Framework:** Flask 2.3.3
- **Database:** PostgreSQL / SQLite
- **ORM:** SQLAlchemy 2.0.20
- **Authentication:** Flask-JWT-Extended 4.5.2
- **Report Generation:** ReportLab, OpenPyXL
- **Testing:** Pytest 7.4.0

## Project Structure

```
Student Management System/
├── app/
│   ├── __init__.py           # Application factory
│   ├── config/
│   │   ├── database.py       # Database configuration
│   │   └── settings.py       # App settings
│   ├── models/               # Database models
│   │   ├── user.py
│   │   ├── student.py
│   │   └── role.py
│   ├── repositories/         # Data access layer
│   │   ├── base_repo.py
│   │   ├── user_repo.py
│   │   └── student_repo.py
│   ├── services/             # Business logic layer
│   │   ├── base_service.py
│   │   ├── auth_service.py
│   │   ├── student_service.py
│   │   └── report_service.py
│   └── routes/               # API endpoints
│       ├── auth_routes.py
│       ├── student_routes.py
│       └── report_routes.py
├── scripts/
│   ├── init_db.py           # Database initialization
│   └── seed_data.py         # Sample data seeder
├── tests/                    # Test suite
├── requirements.txt          # Python dependencies
├── run.py                   # Application entry point
└── .env.example             # Environment variables template

```

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- PostgreSQL (optional, SQLite works for development)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Student Management System"
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example file
   copy .env.example .env

   # Edit .env and update the values
   # For development, you can use SQLite:
   # DATABASE_URL=sqlite:///student_management.db
   ```

5. **Initialize the database**
   ```bash
   python scripts/init_db.py
   ```

   This will:
   - Create all database tables
   - Set up default roles (admin, teacher, student)
   - Create a default admin user (username: `admin`, password: `admin123`)

6. **(Optional) Seed sample data**
   ```bash
   python scripts/seed_data.py
   ```

## Running the Application

### Check Setup

Before running, verify your setup:
```bash
python scripts/check_setup.py
```

### Development Mode

```bash
python run.py
```

The application will start on `http://localhost:5000`

### Using Docker

```bash
# Start all services (app + PostgreSQL)
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

### Production Mode

```bash
# Set environment variables
$env:FLASK_ENV="production"
$env:FLASK_DEBUG="False"

# Run with gunicorn (install first: pip install gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

## API Usage

### Default Admin Credentials
```
Username: admin
Password: admin123
```

⚠️ **IMPORTANT:** Change the default admin password immediately after first login!

### Quick Start Example

1. **Login to get access token:**
   ```bash
   curl -X POST http://localhost:5000/api/auth/login \
     -H "Content-Type: application/json" \
     -d "{\"username\": \"admin\", \"password\": \"admin123\"}"
   ```

2. **Create a student:**
   ```bash
   curl -X POST http://localhost:5000/api/students \
     -H "Authorization: Bearer <your_access_token>" \
     -H "Content-Type: application/json" \
     -d "{
       \"username\": \"john.doe\",
       \"email\": \"john@example.com\",
       \"password\": \"password123\",
       \"first_name\": \"John\",
       \"last_name\": \"Doe\",
       \"date_of_birth\": \"2000-01-15\",
       \"gender\": \"Male\"
     }"
   ```

3. **List all students:**
   ```bash
   curl -X GET http://localhost:5000/api/students \
     -H "Authorization: Bearer <your_access_token>"
   ```

For complete API documentation, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

### Using Postman

Import the [postman_collection.json](postman_collection.json) file into Postman for easy API testing.

### Health Check

```bash
curl http://localhost:5000/health
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_auth.py
```

## Database Migrations

The project uses Flask-Migrate for database migrations:

```bash
# Initialize migrations (first time only)
flask db init

# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Rollback last migration
flask db downgrade
```

## Role-Based Access Control

| Role | Permissions |
|------|-------------|
| **Admin** | Full access to all endpoints, manage users and students |
| **Teacher** | View and update students, generate reports |
| **Student** | View own profile, limited access |

## Report Generation

### Student List Report
```bash
# PDF format
curl -X GET "http://localhost:5000/api/reports/students?format=pdf" \
  -H "Authorization: Bearer <token>" \
  --output students.pdf

# Excel format
curl -X GET "http://localhost:5000/api/reports/students?format=excel" \
  -H "Authorization: Bearer <token>" \
  --output students.xlsx
```

### Student Profile Report
```bash
curl -X GET "http://localhost:5000/api/reports/student/1?format=pdf" \
  -H "Authorization: Bearer <token>" \
  --output student_profile.pdf
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | dev-key-please-change |
| `DATABASE_URL` | Database connection URL | sqlite:///student_management.db |
| `JWT_SECRET_KEY` | JWT signing key | jwt-secret-key-change |
| `JWT_ACCESS_TOKEN_EXPIRES` | Token expiry (seconds) | 3600 |
| `FLASK_DEBUG` | Debug mode | False |
| `PORT` | Server port | 5000 |

## Troubleshooting

### Database Issues

If you encounter database errors:
```bash
# Delete the database file (SQLite)
rm student_management.db

# Re-initialize
python scripts/init_db.py
```

### Module Import Errors

Ensure your virtual environment is activated:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Port Already in Use

Change the port in your `.env` file or run.py:
```bash
PORT=8000 python run.py
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Considerations

- ✅ Passwords are hashed using Werkzeug's secure password hashing
- ✅ JWT tokens expire after 1 hour by default
- ✅ Role-based access control on all protected endpoints
- ⚠️ Change default credentials immediately
- ⚠️ Use HTTPS in production
- ⚠️ Keep SECRET_KEY and JWT_SECRET_KEY secure
- ⚠️ Use PostgreSQL in production (not SQLite)

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
- Create an issue in the GitHub repository
- Contact the development team

## Future Enhancements

- [ ] Course and grade management
- [ ] Attendance tracking
- [ ] Email notifications
- [ ] File upload for student documents
- [ ] Advanced analytics dashboard
- [ ] Mobile app integration
- [ ] Real-time notifications

---

**Built with ❤️ using Flask**