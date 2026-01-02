# Student Management System - Frontend

## 🌐 Live Demo

Visit the live demo: **https://sadhna1118.github.io/Student-Management-System/**

## 🔑 Demo Credentials

```
Admin Account:
Username: admin
Password: admin123

Teacher Account:
Username: teacher1
Password: teacher123
```

## 📱 Features

### Dashboard
- View total students, active users, and gender distribution
- Quick statistics overview
- Recent students list

### Student Management
- List all students with search and filtering
- Add new students
- Edit student information
- Delete students
- Comprehensive student profiles

### User Management (Admin Only)
- View all users
- Manage user accounts
- Activate/deactivate users

### Reports
- Generate PDF reports
- Export to Excel
- View analytics dashboard

## 🚀 Deployment Modes

### Demo Mode (GitHub Pages)
- Runs entirely in the browser
- Uses sample data
- No backend required
- Perfect for demonstration

### Production Mode
- Connects to live backend API
- Real database integration
- Full feature set including reports

## 🔧 Configuration

Edit `js/config.js` to switch between modes:

```javascript
const config = {
    production: {
        apiBaseUrl: 'https://your-backend.com/api',
        isDemoMode: false
    }
};
```

## 🎨 Customization

### Change Theme Colors
Edit `css/style.css`:
```css
:root {
    --primary: #0d6efd;
    --success: #198754;
    --info: #0dcaf0;
    --warning: #ffc107;
    --danger: #dc3545;
}
```

### Add More Demo Data
Edit `js/demo-data.js` to include more sample students or users.

## 📦 Tech Stack

- **Bootstrap 5.3** - UI Framework
- **Bootstrap Icons** - Icon library
- **Vanilla JavaScript** - No framework dependencies
- **Responsive Design** - Mobile-friendly

## 🔗 Related Documentation

- [GitHub Pages Deployment Guide](../GITHUB_PAGES_DEPLOYMENT.md)
- [Backend Deployment Guide](../DEPLOYMENT_LIVE.md)
- [Main Project README](../README.md)

## 📄 License

MIT License - see [LICENSE](../LICENSE) file