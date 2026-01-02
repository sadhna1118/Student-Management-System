# 🚀 GitHub Pages Deployment Guide

This guide will help you deploy the **Student Management System** frontend to GitHub Pages.

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Deploy Frontend to GitHub Pages](#deploy-frontend-to-github-pages)
4. [Connect to Backend](#connect-to-backend)
5. [Demo Mode](#demo-mode)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

✅ GitHub account  
✅ Your repository: https://github.com/sadhna1118/Student-Management-System  
✅ Basic understanding of GitHub Pages

---

## Initial Setup

### Step 1: Enable GitHub Pages

1. Go to your repository: https://github.com/sadhna1118/Student-Management-System
2. Click **Settings** tab
3. In the left sidebar, click **Pages**
4. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
   - (This will use the workflow we've created)

### Step 2: Push Your Changes

The GitHub Actions workflow (`.github/workflows/deploy-pages.yml`) has been created and will automatically:
- Deploy the `frontend` folder to GitHub Pages
- Run on every push to the `main` branch
- Can be manually triggered from the Actions tab

```bash
# If you have local changes, push them
git add .
git commit -m "Setup GitHub Pages deployment"
git push origin main
```

---

## Deploy Frontend to GitHub Pages

### Automatic Deployment

Once you push to the `main` branch:

1. Go to the **Actions** tab in your GitHub repository
2. You'll see the "Deploy to GitHub Pages" workflow running
3. Wait 2-3 minutes for deployment to complete
4. Your site will be live at: **https://sadhna1118.github.io/Student-Management-System/**

### Manual Deployment

You can also trigger deployment manually:

1. Go to **Actions** tab
2. Click "Deploy to GitHub Pages" workflow
3. Click **Run workflow** button
4. Select `main` branch
5. Click **Run workflow**

---

## Connect to Backend

The frontend is configured to work in **two modes**:

### Mode 1: Demo Mode (Default for GitHub Pages)

When deployed to GitHub Pages without a backend, the app automatically runs in **demo mode**:
- ✅ Fully functional UI
- ✅ Sample data included
- ✅ All features work (except file downloads)
- ⚠️ Data doesn't persist (resets on refresh)

**Demo Credentials:**
```
Username: admin
Password: admin123

OR

Username: teacher1
Password: teacher123
```

### Mode 2: Connect to Live Backend

To use with a real backend:

1. **Deploy Backend First**  
   Follow [DEPLOYMENT_LIVE.md](./DEPLOYMENT_LIVE.md) to deploy the backend to Render, Railway, or Heroku

2. **Update Frontend Configuration**  
   Edit `frontend/js/config.js`:

   ```javascript
   const config = {
       production: {
           apiBaseUrl: 'https://your-backend-url.onrender.com/api', // ← Change this
           isDemoMode: false // ← Set to false
       },
       // ... rest of config
   };
   ```

3. **Push Changes**
   ```bash
   git add frontend/js/config.js
   git commit -m "Connect frontend to live backend"
   git push origin main
   ```

4. **Wait for Redeployment**  
   GitHub Actions will automatically redeploy your site

---

## Demo Mode

### What is Demo Mode?

Demo mode allows the frontend to run **without a backend server** using:
- Pre-loaded sample data
- Simulated API calls
- In-browser data storage

### Demo Mode Features

✅ **Working Features:**
- User login (admin/teacher)
- View dashboard with statistics
- List all students
- Add new students
- Edit existing students
- Delete students
- Search and filter students
- View user management
- View analytics

⚠️ **Limited Features:**
- PDF/Excel report generation (requires backend)
- Data persists only during session
- No email functionality
- No real database storage

### Sample Data Included

- **Admin User:** admin / admin123
- **Teacher User:** teacher1 / teacher123
- **5 Sample Students** with complete profiles

---

## Customization

### Update API URL

Edit `frontend/js/config.js`:

```javascript
const config = {
    production: {
        apiBaseUrl: 'https://your-actual-backend.com/api',
        isDemoMode: false
    },
    // ...
};
```

### Add More Demo Data

Edit `frontend/js/demo-data.js` to add more sample students, users, or modify existing data.

### Customize Theme

Edit `frontend/css/style.css` to change colors, fonts, and styling:

```css
:root {
    --primary: #0d6efd;    /* Change primary color */
    --success: #198754;    /* Change success color */
    /* ... add more customization */
}
```

---

## Troubleshooting

### ❌ GitHub Pages not updating?

**Solution:**
1. Go to **Actions** tab
2. Check if deployment succeeded
3. Clear browser cache (Ctrl+Shift+R)
4. Wait 2-3 minutes for CDN to update

### ❌ 404 Error on GitHub Pages?

**Solution:**
1. Verify GitHub Pages is enabled in Settings → Pages
2. Check Source is set to "GitHub Actions"
3. Ensure workflow file exists: `.github/workflows/deploy-pages.yml`

### ❌ App shows white screen?

**Solution:**
1. Open browser console (F12)
2. Check for JavaScript errors
3. Verify all script files are loading:
   - `js/config.js`
   - `js/demo-data.js`
   - `js/app.js`

### ❌ Login not working?

**Solution:**
In demo mode, use these credentials:
```
Username: admin
Password: admin123
```

If connected to backend:
- Verify backend is running
- Check API URL in `config.js` is correct
- Check browser console for CORS errors

### ❌ CORS Error when connecting to backend?

**Solution:**
Your backend needs to allow requests from GitHub Pages.

Add to your Flask app:
```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['https://sadhna1118.github.io'])
```

---

## File Structure

```
frontend/
├── index.html           # Main HTML file
├── css/
│   └── style.css       # Custom styles
└── js/
    ├── config.js       # Environment configuration
    ├── demo-data.js    # Sample data for demo mode
    └── app.js          # Main application logic
```

---

## URLs

| Environment | URL |
|------------|-----|
| **GitHub Pages (Demo)** | https://sadhna1118.github.io/Student-Management-System/ |
| **Backend (Render)** | https://student-management-system.onrender.com/api |
| **Local Development** | http://localhost:5000 |

---

## Next Steps

1. ✅ Deploy frontend to GitHub Pages (Demo mode)
2. 🔄 Deploy backend to Render/Railway (See [DEPLOYMENT_LIVE.md](./DEPLOYMENT_LIVE.md))
3. 🔗 Connect frontend to backend (Update `config.js`)
4. 🎨 Customize theme and branding
5. 📱 Share your live URL!

---

## Support

If you encounter any issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review GitHub Actions logs
3. Check browser console for errors
4. Create an issue on GitHub

---

## 🎉 Your Site is Live!

Once deployed, visit:
**https://sadhna1118.github.io/Student-Management-System/**

Share this URL to showcase your Student Management System!

---

**Built with ❤️ | Deployed on GitHub Pages**