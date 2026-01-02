# Quick Start Guide - Student Management System

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (1 minute)
```powershell
# Activate virtual environment (if not already)
.\venv\Scripts\activate

# Install all required packages
pip install -r requirements.txt
```

### Step 2: Configure Environment (30 seconds)
```powershell
# Create your environment file
copy .env.example .env

# (Optional) Edit .env to customize settings
# For development, the defaults work fine
```

### Step 3: Initialize Database (30 seconds)
```powershell
# This creates tables, roles, and default admin user
python scripts\init_db.py
```

**Output:**
```
✓ Database tables created
✓ Created role: admin
✓ Created role: teacher
✓ Created role: student
✓ Created default admin user (username: admin, password: admin123)
  ⚠ IMPORTANT: Change the default password immediately!
✓ Database initialization complete!
```

### Step 4: (Optional) Add Sample Data (30 seconds)
```powershell
# This creates 20 sample students for testing
python scripts\seed_data.py
```

### Step 5: Run the Application (immediate)
```powershell
python run.py
```

**You should see:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

## ✅ Verify Installation

Open a new terminal and run:
```powershell
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "message": "Student Management System is running"
}
```

---

## 🔐 First Login

### Using cURL:
```powershell
curl -X POST http://localhost:5000/api/auth/login -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"admin123\"}"
```

### Using Postman:
1. Import `postman_collection.json`
2. Select "Login" request
3. Click Send
4. The access token will be automatically saved

### Response:
```json
{
  "status": "success",
  "access_token": "eyJ0eXAiOiJKV1QiLC...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLC...",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "role": {
      "name": "admin"
    }
  }
}
```

---

## 🎯 Try Your First API Call

### Create a Student:
```powershell
curl -X POST http://localhost:5000/api/students `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" `
  -H "Content-Type: application/json" `
  -d '{
    \"username\": \"john.doe\",
    \"email\": \"john@example.com\",
    \"password\": \"password123\",
    \"first_name\": \"John\",
    \"last_name\": \"Doe\",
    \"date_of_birth\": \"2000-01-15\",
    \"gender\": \"Male\"
  }'
```

### List All Students:
```powershell
curl -X GET http://localhost:5000/api/students `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Generate PDF Report:
```powershell
curl -X GET "http://localhost:5000/api/reports/students?format=pdf" `
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" `
  --output students.pdf
```

---

## 📱 Using Postman

1. **Import Collection:**
   - Open Postman
   - Click Import
   - Select `postman_collection.json`

2. **Login:**
   - Go to Authentication > Login
   - Click Send
   - Access token is saved automatically

3. **Test Endpoints:**
   - All requests now use the saved token
   - Try "List Students", "Create Student", etc.

---

## 🔧 Common Commands

### Development
```powershell
# Run application
python run.py

# Run with auto-reload
$env:FLASK_DEBUG="True"
python run.py

# Run tests
pytest

# Run tests with coverage
pytest --cov=app tests/
```

### Database
```powershell
# Initialize database
python scripts\init_db.py

# Add sample data
python scripts\seed_data.py

# Check setup
python scripts\check_setup.py

# Reset database (SQLite)
del student_management.db
python scripts\init_db.py
```

### Docker
```powershell
# Start with Docker
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop
docker-compose down
```

---

## 📚 Next Steps

1. **Change Default Password**
   ```
   POST /api/auth/change-password
   ```

2. **Create Users**
   - Create teachers and students
   - Assign appropriate roles

3. **Explore Reports**
   - Generate PDF reports
   - Export to Excel
   - View analytics

4. **Customize**
   - Update environment variables
   - Configure database
   - Set up CORS for your frontend

---

## 🆘 Troubleshooting

### Port Already in Use
```powershell
# Change port in .env or:
$env:PORT=8000
python run.py
```

### Module Not Found
```powershell
# Ensure virtual environment is activated
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Database Error
```powershell
# Reset database
del student_management.db
python scripts\init_db.py
```

### Import Error
```powershell
# Ensure you're in the project root directory
cd "c:\Users\HP\OneDrive\Documents\Desktop\Student Management System"
```

---

## 📖 Documentation

- **README.md** - Complete project overview
- **API_DOCUMENTATION.md** - All API endpoints with examples
- **DEPLOYMENT.md** - Production deployment guide
- **PROJECT_SUMMARY.md** - Comprehensive project summary

---

## ✨ You're Ready!

Your Student Management System is now running and ready to use.

Access it at: **http://localhost:5000**

Default credentials: `admin` / `admin123`

Happy coding! 🎉