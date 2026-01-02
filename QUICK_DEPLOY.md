# Quick Deployment Guide

## Option 1: GitHub Pages (2 Minutes)

1. Go to: https://github.com/sadhna1118/Student-Management-System
2. Click **Settings** → **Pages**
3. Under Source, select: **GitHub Actions**
4. Wait 2 minutes
5. Visit: https://sadhna1118.github.io/Student-Management-System/

## Option 2: Render (5 Minutes)

### One-Click Deploy:
Click: https://render.com/deploy?repo=https://github.com/sadhna1118/Student-Management-System

### Manual Steps:
1. Sign up at https://render.com with GitHub
2. Click **New +** → **PostgreSQL** → Name: `student-management-db` → **Free** → Create
3. Copy the Internal Database URL
4. Click **New +** → **Web Service** → Connect **Student-Management-System**
5. Configure:
   - Name: `student-management-system`
   - Build: `pip install -r requirements.txt && python scripts/init_db.py`
   - Start: `gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"`
   - Add env var: `DATABASE_URL` = [paste database URL]
   - Instance: **Free**
6. Click **Create Web Service**
7. Wait 5 minutes

## Default Login
Username: `admin`
Password: `admin123`

Change password immediately after first login!