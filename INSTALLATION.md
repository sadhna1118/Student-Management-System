# Installation Guide - Student Management System

## 🎯 Complete Installation Steps

Follow these steps to get your Student Management System up and running.

---

## Prerequisites

✅ **Python 3.10 or higher** (You have Python 3.14.2 ✓)
✅ **pip** (Python package manager)
✅ **Git** (for version control)
✅ **PostgreSQL** (optional, for production)

---

## Step-by-Step Installation

### 1️⃣ Create and Activate Virtual Environment

If you haven't created a virtual environment yet:

```powershell
# Create virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\activate

# Verify activation (you should see (venv) in your prompt)
```

### 2️⃣ Install Dependencies

```powershell
# Make sure you're in the project directory
cd "c:\Users\HP\OneDrive\Documents\Desktop\Student Management System"

# Install all required packages
pip install -r requirements.txt
```

**This will install:**
- Flask and extensions (SQLAlchemy, JWT, Migrate, CORS)
- Database drivers (PostgreSQL, SQLite)
- Report generation (ReportLab, OpenPyXL)
- Testing tools (Pytest)
- Development tools (Faker, Black, Flake8)

**Expected output:**
```
Collecting Flask==2.3.3
Downloading Flask-2.3.3...
Installing collected packages: ...
Successfully installed Flask-2.3.3 Flask-SQLAlchemy-3.0.5 ...
```

### 3️⃣ Create Environment Configuration

```powershell
# Copy the example environment file
copy .env.example .env
```

**For development, the default .env.example settings work fine:**
- Uses SQLite database (no PostgreSQL needed)
- Debug mode enabled
- Development secret keys

### 4️⃣ Initialize Database

```powershell
# Create database tables and default admin user
python scripts\init_db.py
```

**Expected output:**
```
✓ Database tables created
✓ Created role: admin
✓ Created role: teacher
✓ Created role: student
✓ Created default admin user (username: admin, password: admin123)
  ⚠ IMPORTANT: Change the default password immediately!

✓ Database initialization complete!
```

### 5️⃣ (Optional) Add Sample Data

```powershell
# Create 20 sample students for testing
python scripts\seed_data.py
```

**Expected output:**
```
Generating sample student data...
✓ Created student: John Smith (240001)
✓ Created student: Jane Doe (240002)
...
✓ Successfully created sample data!
```

### 6️⃣ Verify Installation

```powershell
# Run the setup checker
python scripts\check_setup.py
```

**Expected output:**
```
🔍 Checking Student Management System setup...

✓ Checking Python version...
  Python 3.14.2
✓ Checking required packages...
  ✓ flask
  ✓ flask_sqlalchemy
  ✓ flask_jwt_extended
  ...
✓ Checking configuration...
  ✓ .env file exists
✓ Checking database...
  ✓ Database configured with 3 roles

============================================================
✅ All checks passed! The application is ready to run.

To start the application, run:
  python run.py
============================================================
```

### 7️⃣ Run the Application

```powershell
# Start the development server
python run.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

### 8️⃣ Test the Application

Open a **new** PowerShell window (keep the app running in the first one):

```powershell
# Test health endpoint
curl http://localhost:5000/health
```

**Expected response:**
```json
{
  "status": "healthy",
  "message": "Student Management System is running"
}
```

**Test login:**
```powershell
curl -X POST http://localhost:5000/api/auth/login -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"admin123\"}"
```

---

## 🎉 Success!

Your Student Management System is now running at:
**http://localhost:5000**

### Default Credentials:
- **Username:** admin
- **Password:** admin123

⚠️ **IMPORTANT:** Change the default password immediately after first login!

---

## 📦 What Was Installed?

### Core Framework (5 packages)
- Flask 2.3.3 - Web framework
- Flask-SQLAlchemy 3.0.5 - Database ORM
- Flask-Migrate 4.0.5 - Database migrations
- Flask-JWT-Extended 4.5.2 - JWT authentication
- Flask-CORS 4.0.0 - Cross-origin support

### Database (3 packages)
- SQLAlchemy 2.0.20 - ORM framework
- psycopg2-binary 2.9.7 - PostgreSQL adapter
- python-dateutil 2.8.2 - Date utilities

### Security (2 packages)
- Werkzeug 2.3.7 - Security utilities
- PyJWT 2.8.0 - JWT tokens

### Reports (2 packages)
- ReportLab 4.0.4 - PDF generation
- OpenPyXL 3.1.2 - Excel export

### Testing (2 packages)
- Pytest 7.4.0 - Test framework
- pytest-cov 4.1.0 - Coverage reports

### Development (4 packages)
- Faker 19.3.0 - Sample data
- Black 23.7.0 - Code formatter
- Flake8 6.1.0 - Linter
- python-dotenv 1.0.0 - Environment variables

### Production (1 package)
- Gunicorn 21.2.0 - WSGI server

---

## 🔧 Troubleshooting

### Issue: "pip: command not found"
```powershell
# Use python -m pip instead
python -m pip install -r requirements.txt
```

### Issue: "Cannot activate virtual environment"
```powershell
# If using Command Prompt (cmd) instead of PowerShell
venv\Scripts\activate.bat

# If using Git Bash
source venv/Scripts/activate
```

### Issue: "Module not found" when running
```powershell
# Make sure virtual environment is activated
# You should see (venv) in your prompt
.\venv\Scripts\activate

# Reinstall if needed
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
```powershell
# Change port in .env file
# Or set environment variable
$env:PORT=8000
python run.py
```

### Issue: Database errors
```powershell
# Delete and recreate database (SQLite)
del student_management.db
python scripts\init_db.py
```

---

## 🐳 Alternative: Docker Installation

If you prefer using Docker:

```powershell
# Start all services (app + database)
docker-compose up -d

# Wait for initialization (about 30 seconds)
docker-compose logs -f app

# Access at http://localhost:5000
```

**Stop Docker services:**
```powershell
docker-compose down
```

---

## 📚 Next Steps

1. **Review Documentation:**
   - [README.md](README.md) - Project overview
   - [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - Complete API reference
   - [QUICK_START.md](QUICK_START.md) - Quick start guide

2. **Import Postman Collection:**
   - Open Postman
   - Import `postman_collection.json`
   - Start testing endpoints

3. **Change Default Password:**
   - Login as admin
   - Use `/api/auth/change-password` endpoint

4. **Start Development:**
   - Create students
   - Generate reports
   - Explore the API

---

## ✅ Installation Checklist

- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Environment file created (`.env`)
- [ ] Database initialized (`python scripts\init_db.py`)
- [ ] (Optional) Sample data seeded
- [ ] Setup verified (`python scripts\check_setup.py`)
- [ ] Application running (`python run.py`)
- [ ] Health check successful
- [ ] Login tested with default credentials
- [ ] Default password changed

---

## 💡 Development Tips

### Auto-reload on code changes:
```powershell
$env:FLASK_DEBUG="True"
python run.py
```

### Run tests:
```powershell
pytest
```

### View test coverage:
```powershell
pytest --cov=app tests/
```

### Format code:
```powershell
black app/
```

### Check code style:
```powershell
flake8 app/
```

---

## 🆘 Need Help?

1. **Check logs:** `logs/student_management.log`
2. **Review documentation:** See all .md files
3. **Run setup checker:** `python scripts\check_setup.py`
4. **Verify environment:** Check `.env` file
5. **Test endpoints:** Use Postman collection

---

**Installation Time:** ~5 minutes
**Difficulty:** Easy
**Status:** Ready to use!

🎉 **Enjoy your Student Management System!**