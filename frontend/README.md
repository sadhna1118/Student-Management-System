# Student Management System - Frontend

A modern, responsive web application for managing students, users, and generating reports.

## 🚀 Features

### ✅ Complete Implementation
- **Authentication** - Secure login with JWT tokens
- **Dashboard** - Statistics and recent students overview
- **Student Management** - Create, view, edit, delete students
- **User Management** - Admin-only user administration
- **Reports** - Generate PDF and Excel reports
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Role-Based Access** - Different features for Admin, Teacher, Student

## 🎨 Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Bootstrap 5
- **JavaScript (Vanilla)** - No frameworks, pure JS
- **Bootstrap 5.3** - UI components and responsive grid
- **Bootstrap Icons** - Beautiful icon set

## 📦 Project Structure

```
frontend/
├── index.html          # Main HTML file
├── css/
│   └── style.css      # Custom styles
├── js/
│   └── app.js         # Application logic
└── README.md          # This file
```

## 🏃 How to Run

### Prerequisites
1. Backend server must be running on `http://localhost:5000`
2. A modern web browser (Chrome, Firefox, Edge, Safari)

### Option 1: Open Directly (Simplest)
1. Navigate to the `frontend` folder
2. Double-click `index.html`
3. Your default browser will open the application

### Option 2: Using Python HTTP Server
```bash
cd frontend
python -m http.server 8080
```
Then open: http://localhost:8080

### Option 3: Using Node.js HTTP Server
```bash
cd frontend
npx http-server -p 8080
```
Then open: http://localhost:8080

### Option 4: Using Live Server (VS Code)
1. Install "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## 🔑 Default Login

- **Username:** admin
- **Password:** admin123

⚠️ **Change this password immediately after first login!**

## 📱 Features by Role

### Admin
- ✅ View Dashboard with statistics
- ✅ Full CRUD operations on students
- ✅ Manage all users (activate/deactivate)
- ✅ Generate reports (PDF, Excel)
- ✅ View analytics

### Teacher
- ✅ View Dashboard
- ✅ View all students
- ✅ Edit student information
- ✅ Generate reports

### Student
- ✅ View Dashboard
- ✅ View own profile
- ✅ Limited access

## 🎯 User Guide

### Dashboard
- View total students count
- See active users
- Gender distribution statistics
- Recent students list

### Students Page
- **Add Student**: Click "Add Student" button (Admin only)
- **Search**: Use search box to filter students
- **Filter**: Filter by gender
- **View**: Click eye icon to view details
- **Edit**: Click pencil icon to edit (Admin/Teacher)
- **Delete**: Click trash icon to delete (Admin only)

### Users Page (Admin Only)
- View all system users
- Activate/Deactivate user accounts
- See user roles and status

### Reports
- **PDF Report**: Download all students in PDF format
- **Excel Export**: Export data to Excel spreadsheet
- **Analytics**: View detailed statistics

## 🛠️ Configuration

To change the backend API URL, edit `frontend/js/app.js`:

```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

## 🎨 Customization

### Colors
Edit `frontend/css/style.css` to change theme colors:

```css
:root {
    --primary: #0d6efd;
    --success: #198754;
    --info: #0dcaf0;
    --warning: #ffc107;
    --danger: #dc3545;
}
```

### Branding
- Update the navbar brand in `index.html`
- Change the login page icon
- Modify card styles in `style.css`

## 📱 Responsive Design

The application is fully responsive and works on:
- 📱 Mobile devices (320px and up)
- 📱 Tablets (768px and up)
- 💻 Desktops (1024px and up)
- 🖥️ Large screens (1920px and up)

## 🔒 Security

- JWT token-based authentication
- Tokens stored in localStorage
- Automatic logout on token expiry
- Role-based access control
- CORS enabled for cross-origin requests

## 🐛 Troubleshooting

### "Connection error" on login
- Ensure backend server is running: `python run.py`
- Check if server is accessible at http://localhost:5000

### "Failed to load students"
- Verify you're logged in
- Check if your account has appropriate role permissions
- Ensure backend API is responding

### Modal not opening
- Clear browser cache
- Check browser console for errors
- Ensure Bootstrap JS is loaded

## 🚀 Deployment

### Deploy to Web Server
1. Upload all files to your web server
2. Update `API_BASE_URL` in `app.js` to your backend URL
3. Ensure CORS is configured on backend for your domain

### Deploy with Backend
1. Copy frontend folder to your backend project
2. Serve static files from Flask
3. Update backend to serve `index.html` on root route

## 📄 Browser Compatibility

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Opera (latest)

## 🎓 Future Enhancements

Possible additions:
- Advanced filtering and sorting
- Data export in more formats
- Print functionality
- Profile picture upload
- Real-time notifications
- Dark mode
- Multi-language support

## 📝 License

This project is part of the Student Management System.

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation
3. Check backend logs
4. Contact system administrator

---

**Built with ❤️ for educational institutions**