# 🚀 Quick Deploy Commands

## Deploy to GitHub (5 Minutes)

```powershell
# Step 1: Initialize Git
git init

# Step 2: Add all files
git add .

# Step 3: Commit
git commit -m "Initial commit: Student Management System"

# Step 4: Add GitHub remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/Student-Management-System.git

# Step 5: Push to GitHub
git branch -M main
git push -u origin main
```

## Deploy to Render (Free Hosting)

1. Go to https://render.com and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in:
   - **Name:** student-management-system
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -w 4 -b 0.0.0.0:$PORT "app:create_app()"`
5. Add Environment Variables:
   - `SECRET_KEY` = (generate a random string)
   - `JWT_SECRET_KEY` = (generate a random string)
   - `DATABASE_URL` = (Render will provide PostgreSQL)
   - `FLASK_ENV` = production
6. Click "Create Web Service"
7. Wait for deployment (2-5 minutes)
8. Your app will be live at: `https://student-management-system-xxxx.onrender.com`

## Deploy to Railway (Free Hosting)

```powershell
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up

# Add PostgreSQL
railway add
# Select: PostgreSQL

# Set environment variables
railway variables set SECRET_KEY=your-secret-key-here
railway variables set JWT_SECRET_KEY=your-jwt-secret-here
railway variables set FLASK_ENV=production

# Your app is live!
railway open
```

## After Deployment

1. **Initialize Database:**
   - Most platforms: Run `python scripts/init_db.py` in their console
   
2. **Change Admin Password:**
   - Login with `admin` / `admin123`
   - Change password immediately!

3. **Test Your API:**
   ```bash
   curl https://your-app-url.com/health
   ```

## That's It! 🎉

Your app is now live and accessible to the world!