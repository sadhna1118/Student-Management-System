# Student Management System - API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication

All protected endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <access_token>
```

---

## Authentication Endpoints

### Register User
**POST** `/auth/register`

Register a new user account.

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe",
  "role_id": 3
}
```

**Response (201):**
```json
{
  "status": "success",
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_active": true,
    "role": {
      "id": 3,
      "name": "student"
    }
  }
}
```

---

### Login
**POST** `/auth/login`

Authenticate user and receive JWT tokens.

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "status": "success",
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "role": {
      "name": "student"
    }
  }
}
```

---

### Refresh Token
**POST** `/auth/refresh`

Refresh the access token using a refresh token.

**Headers:**
```
Authorization: Bearer <refresh_token>
```

**Response (200):**
```json
{
  "status": "success",
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

### Get Current User
**GET** `/auth/me`

Get information about the currently authenticated user.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": {
      "name": "student"
    }
  }
}
```

---

### Change Password
**POST** `/auth/change-password`

Change the password for the authenticated user.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "current_password": "oldpassword123",
  "new_password": "newpassword123"
}
```

**Response (200):**
```json
{
  "status": "success",
  "message": "Password updated successfully"
}
```

---

## Student Endpoints

### List Students
**GET** `/students`

Get a list of all students. Requires admin or teacher role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `search` (optional): Search term for filtering students
- `gender` (optional): Filter by gender

**Response (200):**
```json
{
  "status": "success",
  "count": 10,
  "students": [
    {
      "id": 1,
      "student_id": "240001",
      "date_of_birth": "2000-01-15",
      "gender": "Male",
      "phone": "1234567890",
      "address": "123 Main St",
      "user": {
        "id": 2,
        "username": "johndoe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe"
      }
    }
  ]
}
```

---

### Get Student Details
**GET** `/students/<student_id>`

Get detailed information about a specific student.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "student": {
    "id": 1,
    "student_id": "240001",
    "date_of_birth": "2000-01-15",
    "gender": "Male",
    "phone": "1234567890",
    "address": "123 Main St",
    "admission_date": "2024-09-01",
    "user": {
      "id": 2,
      "username": "johndoe",
      "email": "john@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "role": {
        "name": "student"
      }
    }
  }
}
```

---

### Create Student
**POST** `/students`

Create a new student record. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "username": "janedoe",
  "email": "jane@example.com",
  "password": "password123",
  "first_name": "Jane",
  "last_name": "Doe",
  "date_of_birth": "2001-05-20",
  "gender": "Female",
  "address": "456 Oak Ave",
  "phone": "9876543210",
  "admission_date": "2024-09-01"
}
```

**Response (201):**
```json
{
  "status": "success",
  "message": "Student created successfully",
  "student": {
    "id": 2,
    "student_id": "240002",
    "date_of_birth": "2001-05-20",
    "gender": "Female",
    "user": {
      "username": "janedoe",
      "email": "jane@example.com"
    }
  }
}
```

---

### Update Student
**PUT** `/students/<student_id>`

Update student information. Requires admin or teacher role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "phone": "1112223333",
  "address": "789 New Street",
  "first_name": "Jane",
  "last_name": "Smith"
}
```

**Response (200):**
```json
{
  "status": "success",
  "message": "Student updated successfully",
  "student": {
    "id": 2,
    "student_id": "240002",
    "phone": "1112223333",
    "address": "789 New Street"
  }
}
```

---

### Delete Student
**DELETE** `/students/<student_id>`

Delete a student record. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "message": "Student deleted successfully"
}
```

---

## Report Endpoints

### Generate Student Report
**GET** `/reports/students`

Generate a report of all students. Requires admin or teacher role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `format` (required): Report format - `pdf` or `excel`
- `search` (optional): Filter students by search term
- `gender` (optional): Filter students by gender

**Response:**
Returns a downloadable file (PDF or Excel)

---

### Generate Student Profile
**GET** `/reports/student/<student_id>`

Generate a detailed profile report for a specific student.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `format` (optional): Report format - `pdf` (default)

**Response:**
Returns a downloadable PDF file

---

### Get Analytics
**GET** `/reports/analytics`

Get student analytics and statistics. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "analytics": {
    "total_students": 50,
    "gender_distribution": {
      "Male": 25,
      "Female": 23,
      "Other": 2
    },
    "recent_admissions": 5
  }
}
```

---

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "status": "error",
  "message": "Missing required fields"
}
```

### 401 Unauthorized
```json
{
  "status": "error",
  "message": "Invalid username or password"
}
```

### 403 Forbidden
```json
{
  "status": "error",
  "message": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "status": "error",
  "message": "Student not found"
}
```

### 500 Internal Server Error
```json
{
  "status": "error",
  "message": "Internal server error"
}
```

---

## Admin Endpoints

### List All Users
**GET** `/admin/users`

Get a list of all users in the system. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `role` (optional): Filter by role name (admin, teacher, student)
- `search` (optional): Search users by username, email, or name

**Response (200):**
```json
{
  "status": "success",
  "count": 25,
  "users": [
    {
      "id": 1,
      "username": "admin",
      "email": "admin@example.com",
      "first_name": "System",
      "last_name": "Administrator",
      "is_active": true,
      "role": {
        "id": 1,
        "name": "admin"
      }
    }
  ]
}
```

---

### Get User by ID
**GET** `/admin/users/<user_id>`

Get detailed information about a specific user. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "user": {
    "id": 2,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_active": true,
    "role": {
      "name": "student"
    }
  }
}
```

---

### Update User
**PUT** `/admin/users/<user_id>`

Update user information. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "first_name": "Updated",
  "last_name": "Name",
  "email": "newemail@example.com",
  "is_active": true
}
```

**Response (200):**
```json
{
  "status": "success",
  "message": "User updated successfully",
  "user": {
    "id": 2,
    "username": "johndoe",
    "email": "newemail@example.com",
    "first_name": "Updated",
    "last_name": "Name"
  }
}
```

---

### Deactivate User
**POST** `/admin/users/<user_id>/deactivate`

Deactivate a user account. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "message": "User deactivated successfully"
}
```

---

### Activate User
**POST** `/admin/users/<user_id>/activate`

Activate a user account. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "message": "User activated successfully"
}
```

---

### Delete User
**DELETE** `/admin/users/<user_id>`

Delete a user account permanently. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "message": "User deleted successfully"
}
```

---

### List All Roles
**GET** `/admin/roles`

Get a list of all available roles. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "roles": [
    {
      "id": 1,
      "name": "admin",
      "description": "Administrator with full access"
    },
    {
      "id": 2,
      "name": "teacher",
      "description": "Teacher with limited access"
    },
    {
      "id": 3,
      "name": "student",
      "description": "Basic student access"
    }
  ]
}
```

---

### Get System Statistics
**GET** `/admin/stats`

Get system-wide statistics including user counts and student data. Requires admin role.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "status": "success",
  "stats": {
    "total_users": 100,
    "active_users": 95,
    "inactive_users": 5,
    "total_students": 80,
    "users_by_role": {
      "admin": 2,
      "teacher": 18,
      "student": 80
    }
  }
}
```

---

## Role-Based Access Control

| Endpoint | Admin | Teacher | Student |
|----------|-------|---------|---------|
| POST /auth/register | ✓ | ✓ | ✓ |
| POST /auth/login | ✓ | ✓ | ✓ |
| GET /auth/me | ✓ | ✓ | ✓ |
| POST /auth/change-password | ✓ | ✓ | ✓ |
| GET /students | ✓ | ✓ | ✗ |
| GET /students/:id | ✓ | ✓ | Own only |
| POST /students | ✓ | ✗ | ✗ |
| PUT /students/:id | ✓ | ✓ | ✗ |
| DELETE /students/:id | ✓ | ✗ | ✗ |
| GET /admin/users | ✓ | ✗ | ✗ |
| GET /admin/users/:id | ✓ | ✗ | ✗ |
| PUT /admin/users/:id | ✓ | ✗ | ✗ |
| POST /admin/users/:id/activate | ✓ | ✗ | ✗ |
| POST /admin/users/:id/deactivate | ✓ | ✗ | ✗ |
| DELETE /admin/users/:id | ✓ | ✗ | ✗ |
| GET /admin/roles | ✓ | ✗ | ✗ |
| GET /admin/stats | ✓ | ✗ | ✗ |
| GET /reports/students | ✓ | ✓ | ✗ |
| GET /reports/student/:id | ✓ | ✓ | Own only |
| GET /reports/analytics | ✓ | ✗ | ✗ |

---

## Testing with cURL

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### List Students
```bash
curl -X GET http://localhost:5000/api/students \
  -H "Authorization: Bearer <your_token>"
```

### Create Student
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "student1",
    "email": "student1@example.com",
    "password": "password123",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "2000-01-15",
    "gender": "Male"
  }'
```