# GitHub Deployment Guide

Complete guide to deploy the Student Management System to GitHub and various hosting platforms.

## 📦 Deploy to GitHub

### Initial Setup

1. **Create GitHub Repository**
   - Go to https://github.com/new
   - Repository name: `Student-Management-System`
   - Description: "A comprehensive student management system built with Flask"
   - Choose Public or Private
   - Click "Create repository"

2. **Push Code to GitHub**

```powershell
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Student Management System v1.0"

# Add remote repository (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/Student-Management-System.git

# Push to GitHub
git branch -M main
git push -u origin main
```

3. **Verify Upload**
   - Visit your repository on GitHub
   - All files should be visible

### Add Repository Badges

Add these badges to your README.md:

```markdown
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Flask Version](https://img.shields.io/badge/flask-2.3.3-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Build Status](https://github.com/YOUR-USERNAME/Student-Management-System/workflows/CI%2FCD%20Pipeline/badge.svg)
```

---

## 🚀 Deploy to Hosting Platforms

### Option 1: Deploy to Render (Recommended)

1. **Create Account** at https://render.com

2. **Create New Web Service**
   - Connect your GitHub repository
   - Name: `student-management-system`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"`

3. **Add Environment Variables**
   ```
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-here
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   FLASK_ENV=production
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy

### Option 2: Deploy to Railway

1. **Install Railway CLI**
   ```powershell
   npm install -g @railway/cli
   ```

2. **Login and Deploy**
   ```powershell
   railway login
   railway init
   railway up
   ```

3. **Add PostgreSQL Database**
   ```powershell
   railway add
   # Select PostgreSQL
   ```

4. **Set Environment Variables**
   ```powershell
   railway variables set SECRET_KEY=your-secret-key
   railway variables set JWT_SECRET_KEY=your-jwt-secret
   ```

### Option 3: Deploy to Heroku

1. **Install Heroku CLI**
   Download from https://devcenter.heroku.com/articles/heroku-cli

2. **Login and Create App**
   ```powershell
   heroku login
   heroku create student-management-system
   ```

3. **Add PostgreSQL**
   ```powershell
   heroku addons:create heroku-postgresql:mini
   ```

4. **Set Environment Variables**
   ```powershell
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set JWT_SECRET_KEY=your-jwt-secret
   heroku config:set FLASK_ENV=production
   ```

5. **Create Procfile** (already exists in project)

6. **Deploy**
   ```powershell
   git push heroku main
   ```

7. **Initialize Database**
   ```powershell
   heroku run python scripts/init_db.py
   ```

### Option 4: Deploy to PythonAnywhere

1. **Create Account** at https://www.pythonanywhere.com

2. **Upload Code**
   - Use Git to clone your repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
   ```

3. **Create Virtual Environment**
   ```bash
   cd Student-Management-System
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to Web tab
   - Add new web app
   - Select Flask
   - Point to your app

5. **Set Environment Variables**
   - Add in WSGI configuration file

### Option 5: Deploy with Docker

1. **Build Docker Image**
   ```powershell
   docker build -t student-management-system .
   ```

2. **Run Container**
   ```powershell
   docker run -p 5000:5000 -e SECRET_KEY=your-key student-management-system
   ```

3. **Deploy to Docker Hub**
   ```powershell
   docker tag student-management-system YOUR-USERNAME/student-management-system
   docker push YOUR-USERNAME/student-management-system
   ```

---

## 🔧 Post-Deployment Steps

### 1. Initialize Database

For most platforms, run:
```bash
python scripts/init_db.py
```

### 2. Change Default Credentials

**IMPORTANT:** Change the default admin password immediately!

```bash
curl -X POST https://your-app.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### 3. Configure CORS

Update CORS settings in `app/__init__.py` to allow your frontend domain:

```python
CORS(app, resources={r"/api/*": {"origins": "https://your-frontend.com"}})
```

### 4. Set Up SSL/HTTPS

Most platforms (Render, Railway, Heroku) provide free SSL certificates automatically.

### 5. Monitor Application

- Set up error tracking (Sentry, Rollbar)
- Monitor logs
- Set up uptime monitoring

---

## 📊 GitHub Pages (Frontend Only)

To deploy the frontend as a static site on GitHub Pages:

1. **Create gh-pages branch**
   ```powershell
   git checkout -b gh-pages
   ```

2. **Push frontend files**
   ```powershell
   git add frontend/*
   git commit -m "Deploy frontend to GitHub Pages"
   git push origin gh-pages
   ```

3. **Enable GitHub Pages**
   - Go to repository Settings
   - Pages section
   - Select gh-pages branch
   - Set folder to /frontend

4. **Update API URL**
   - Update `frontend/js/app.js`
   - Point to your deployed backend API

---

## 🔐 Security Checklist

Before deploying to production:

- [ ] Change SECRET_KEY and JWT_SECRET_KEY
- [ ] Change default admin password
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS
- [ ] Set FLASK_ENV=production
- [ ] Set FLASK_DEBUG=False
- [ ] Configure proper CORS settings
- [ ] Set up database backups
- [ ] Review .gitignore (ensure no sensitive data)
- [ ] Set up environment variables properly
- [ ] Enable rate limiting
- [ ] Set up monitoring and logging

---

## 🔄 Continuous Deployment

The project includes GitHub Actions workflows for CI/CD:

- **`.github/workflows/ci.yml`** - Runs tests on every push
- **`.github/workflows/deploy.yml`** - Deploys on version tags

### Create a Release

```powershell
# Tag a new version
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

This will trigger the deployment workflow automatically.

---

## 📞 Support

If you encounter issues during deployment:

1. Check the deployment logs
2. Verify environment variables are set correctly
3. Ensure database is initialized
4. Check the platform's documentation
5. Create an issue on GitHub

---

## 🎉 You're All Set!

Your Student Management System is now deployed and accessible online!

**Next Steps:**
- Share the URL with your team
- Set up monitoring
- Configure backups
- Add custom domain (optional)
- Enable notifications