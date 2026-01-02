// Student Management System - Frontend Application
const API_BASE_URL = `${window.location.protocol}//${window.location.host}/api`;

// Global state
let currentUser = null;
let accessToken = null;
let allStudents = [];
let studentModal = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is logged in
    const token = localStorage.getItem('accessToken');
    const user = localStorage.getItem('currentUser');
    
    if (token && user) {
        accessToken = token;
        currentUser = JSON.parse(user);
        showMainApp();
    } else {
        document.getElementById('loginPage').style.display = 'flex';
    }
    
    // Initialize Bootstrap modal
    const modalElement = document.getElementById('studentModal');
    if (modalElement) {
        studentModal = new bootstrap.Modal(modalElement);
    }
});

// Authentication
async function login(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const loginBtn = document.getElementById('loginBtn');
    const loginError = document.getElementById('loginError');
    
    loginBtn.disabled = true;
    loginBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Signing in...';
    loginError.style.display = 'none';
    
    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            accessToken = data.access_token;
            currentUser = data.user;
            
            localStorage.setItem('accessToken', accessToken);
            localStorage.setItem('currentUser', JSON.stringify(currentUser));
            
            showMainApp();
        } else {
            loginError.textContent = data.message || 'Invalid credentials';
            loginError.style.display = 'block';
        }
    } catch (error) {
        console.error('Login error:', error);
        loginError.textContent = 'Connection error. Please check if the backend server is running.';
        loginError.style.display = 'block';
    } finally {
        loginBtn.disabled = false;
        loginBtn.innerHTML = '<i class="bi bi-box-arrow-in-right"></i> Sign In';
    }
}

function logout() {
    if (confirm('Are you sure you want to logout?')) {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('currentUser');
        accessToken = null;
        currentUser = null;
        
        document.getElementById('mainNav').style.display = 'none';
        document.getElementById('dashboardPage').style.display = 'none';
        document.getElementById('studentsPage').style.display = 'none';
        document.getElementById('usersPage').style.display = 'none';
        document.getElementById('reportsPage').style.display = 'none';
        document.getElementById('loginPage').style.display = 'flex';
    }
}

function showMainApp() {
    document.getElementById('loginPage').style.display = 'none';
    document.getElementById('mainNav').style.display = 'block';
    document.getElementById('currentUserName').textContent = currentUser.username;
    
    // Show admin menu items if admin
    if (currentUser.role && currentUser.role.name === 'admin') {
        document.getElementById('usersNavItem').style.display = 'block';
        document.getElementById('addStudentBtn').style.display = 'block';
    }
    
    showDashboard();
}

// Page Navigation
function hideAllPages() {
    document.getElementById('dashboardPage').style.display = 'none';
    document.getElementById('studentsPage').style.display = 'none';
    document.getElementById('usersPage').style.display = 'none';
    document.getElementById('reportsPage').style.display = 'none';
}

function showDashboard() {
    hideAllPages();
    document.getElementById('dashboardPage').style.display = 'block';
    loadDashboardData();
}

function showStudents() {
    hideAllPages();
    document.getElementById('studentsPage').style.display = 'block';
    loadStudents();
}

function showUsers() {
    if (currentUser.role && currentUser.role.name === 'admin') {
        hideAllPages();
        document.getElementById('usersPage').style.display = 'block';
        loadUsers();
    }
}

function showReports() {
    hideAllPages();
    document.getElementById('reportsPage').style.display = 'block';
    document.getElementById('analyticsSection').style.display = 'none';
}

function showProfile() {
    alert('Profile page coming soon!');
}

// Dashboard Functions
async function loadDashboardData() {
    try {
        // Load students
        const studentsResponse = await fetch(`${API_BASE_URL}/students`, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        
        if (studentsResponse.ok) {
            const studentsData = await studentsResponse.json();
            const students = studentsData.students || [];
            
            document.getElementById('totalStudents').textContent = students.length;
            
            // Count by gender
            const male = students.filter(s => s.gender === 'Male').length;
            const female = students.filter(s => s.gender === 'Female').length;
            
            document.getElementById('maleStudents').textContent = male;
            document.getElementById('femaleStudents').textContent = female;
            
            // Recent students (last 5)
            const recent = students.slice(0, 5);
            displayRecentStudents(recent);
        }
        
        // Load users (admin only)
        if (currentUser.role && currentUser.role.name === 'admin') {
            const usersResponse = await fetch(`${API_BASE_URL}/admin/users`, {
                headers: {
                    'Authorization': `Bearer ${accessToken}`
                }
            });
            
            if (usersResponse.ok) {
                const usersData = await usersResponse.json();
                const users = usersData.users || [];
                const activeUsers = users.filter(u => u.is_active).length;
                document.getElementById('activeUsers').textContent = activeUsers;
            }
        } else {
            document.getElementById('activeUsers').textContent = '-';
        }
        
    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}

function displayRecentStudents(students) {
    const tbody = document.getElementById('recentStudentsTable');
    
    if (students.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="text-center">No students found</td></tr>';
        return;
    }
    
    tbody.innerHTML = students.map(student => `
        <tr>
            <td>${student.student_id || 'N/A'}</td>
            <td>${student.user ? student.user.first_name + ' ' + student.user.last_name : 'N/A'}</td>
            <td>${student.user ? student.user.email : 'N/A'}</td>
            <td>${student.gender || 'N/A'}</td>
            <td>${formatDate(student.admission_date)}</td>
        </tr>
    `).join('');
}

// Students Functions
async function loadStudents() {
    try {
        const response = await fetch(`${API_BASE_URL}/students`, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            allStudents = data.students || [];
            displayStudents(allStudents);
        } else {
            document.getElementById('studentsTable').innerHTML = 
                '<tr><td colspan="7" class="text-center text-danger">Failed to load students</td></tr>';
        }
    } catch (error) {
        console.error('Error loading students:', error);
        document.getElementById('studentsTable').innerHTML = 
            '<tr><td colspan="7" class="text-center text-danger">Error loading students</td></tr>';
    }
}

function displayStudents(students) {
    const tbody = document.getElementById('studentsTable');
    
    if (students.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" class="text-center">No students found</td></tr>';
        return;
    }
    
    tbody.innerHTML = students.map(student => {
        const isAdmin = currentUser.role && currentUser.role.name === 'admin';
        const canEdit = isAdmin || (currentUser.role && currentUser.role.name === 'teacher');
        
        return `
            <tr>
                <td>${student.student_id || 'N/A'}</td>
                <td>${student.user ? student.user.first_name + ' ' + student.user.last_name : 'N/A'}</td>
                <td>${student.user ? student.user.email : 'N/A'}</td>
                <td>${student.gender || 'N/A'}</td>
                <td>${student.phone || 'N/A'}</td>
                <td>${formatDate(student.date_of_birth)}</td>
                <td>
                    <button class="btn btn-sm btn-info btn-action" onclick="viewStudent(${student.id})" title="View">
                        <i class="bi bi-eye"></i>
                    </button>
                    ${canEdit ? `
                        <button class="btn btn-sm btn-warning btn-action" onclick="editStudent(${student.id})" title="Edit">
                            <i class="bi bi-pencil"></i>
                        </button>
                    ` : ''}
                    ${isAdmin ? `
                        <button class="btn btn-sm btn-danger btn-action" onclick="deleteStudent(${student.id})" title="Delete">
                            <i class="bi bi-trash"></i>
                        </button>
                    ` : ''}
                </td>
            </tr>
        `;
    }).join('');
}

function searchStudents() {
    const searchTerm = document.getElementById('searchStudent').value.toLowerCase();
    const genderFilter = document.getElementById('filterGender').value;
    
    let filtered = allStudents;
    
    // Apply search filter
    if (searchTerm) {
        filtered = filtered.filter(student => {
            const name = student.user ? (student.user.first_name + ' ' + student.user.last_name).toLowerCase() : '';
            const email = student.user ? student.user.email.toLowerCase() : '';
            const studentId = (student.student_id || '').toLowerCase();
            
            return name.includes(searchTerm) || email.includes(searchTerm) || studentId.includes(searchTerm);
        });
    }
    
    // Apply gender filter
    if (genderFilter) {
        filtered = filtered.filter(student => student.gender === genderFilter);
    }
    
    displayStudents(filtered);
}

function showAddStudentModal() {
    document.getElementById('studentModalTitle').textContent = 'Add Student';
    document.getElementById('studentForm').reset();
    document.getElementById('studentId').value = '';
    document.getElementById('passwordField').style.display = 'block';
    document.getElementById('studentPassword').required = true;
    studentModal.show();
}

function viewStudent(id) {
    const student = allStudents.find(s => s.id === id);
    if (student) {
        const details = `
            Student ID: ${student.student_id}
            Name: ${student.user ? student.user.first_name + ' ' + student.user.last_name : 'N/A'}
            Email: ${student.user ? student.user.email : 'N/A'}
            Gender: ${student.gender || 'N/A'}
            Date of Birth: ${formatDate(student.date_of_birth)}
            Phone: ${student.phone || 'N/A'}
            Address: ${student.address || 'N/A'}
            Admission Date: ${formatDate(student.admission_date)}
        `;
        alert(details);
    }
}

async function editStudent(id) {
    const student = allStudents.find(s => s.id === id);
    if (!student) return;
    
    document.getElementById('studentModalTitle').textContent = 'Edit Student';
    document.getElementById('studentId').value = student.id;
    document.getElementById('studentUsername').value = student.user ? student.user.username : '';
    document.getElementById('studentUsername').disabled = true;
    document.getElementById('studentEmail').value = student.user ? student.user.email : '';
    document.getElementById('studentFirstName').value = student.user ? student.user.first_name : '';
    document.getElementById('studentLastName').value = student.user ? student.user.last_name : '';
    document.getElementById('studentDOB').value = student.date_of_birth || '';
    document.getElementById('studentGender').value = student.gender || '';
    document.getElementById('studentPhone').value = student.phone || '';
    document.getElementById('studentAddress').value = student.address || '';
    document.getElementById('studentAdmissionDate').value = student.admission_date || '';
    
    document.getElementById('passwordField').style.display = 'none';
    document.getElementById('studentPassword').required = false;
    
    studentModal.show();
}

async function saveStudent(event) {
    event.preventDefault();
    
    const studentId = document.getElementById('studentId').value;
    const isEdit = !!studentId;
    
    const saveBtn = document.getElementById('saveStudentBtn');
    saveBtn.disabled = true;
    saveBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Saving...';
    
    try {
        const data = {
            username: document.getElementById('studentUsername').value,
            email: document.getElementById('studentEmail').value,
            first_name: document.getElementById('studentFirstName').value,
            last_name: document.getElementById('studentLastName').value,
            date_of_birth: document.getElementById('studentDOB').value,
            gender: document.getElementById('studentGender').value,
            phone: document.getElementById('studentPhone').value || null,
            address: document.getElementById('studentAddress').value || null,
            admission_date: document.getElementById('studentAdmissionDate').value || null
        };
        
        if (!isEdit) {
            data.password = document.getElementById('studentPassword').value;
        }
        
        const url = isEdit ? `${API_BASE_URL}/students/${studentId}` : `${API_BASE_URL}/students`;
        const method = isEdit ? 'PUT' : 'POST';
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            studentModal.hide();
            loadStudents();
            showNotification('success', isEdit ? 'Student updated successfully!' : 'Student created successfully!');
        } else {
            alert(result.message || 'Failed to save student');
        }
    } catch (error) {
        console.error('Error saving student:', error);
        alert('Error saving student');
    } finally {
        saveBtn.disabled = false;
        saveBtn.innerHTML = 'Save Student';
        document.getElementById('studentUsername').disabled = false;
    }
}

async function deleteStudent(id) {
    if (!confirm('Are you sure you want to delete this student?')) return;
    
    try {
        const response = await fetch(`${API_BASE_URL}/students/${id}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        
        if (response.ok) {
            loadStudents();
            showNotification('success', 'Student deleted successfully!');
        } else {
            const data = await response.json();
            alert(data.message || 'Failed to delete student');
        }
    } catch (error) {
        console.error('Error deleting student:', error);
        alert('Error deleting student');
    }
}

// Users Functions (Admin Only)
async function loadUsers() {
    try {
        const response = await fetch(`${API_BASE_URL}/admin/users`, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            displayUsers(data.users || []);
        } else {
            document.getElementById('usersTable').innerHTML = 
                '<tr><td colspan="6" class="text-center text-danger">Failed to load users</td></tr>';
        }
    } catch (error) {
        console.error('Error loading users:', error);
    }
}

function displayUsers(users) {
    const tbody = document.getElementById('usersTable');
    
    if (users.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="text-center">No users found</td></tr>';
        return;
    }
    
    tbody.innerHTML = users.map(user => `
        <tr>
            <td>${user.username}</td>
            <td>${user.first_name} ${user.last_name}</td>
            <td>${user.email}</td>
            <td><span class="badge bg-primary">${user.role ? user.role.name : 'N/A'}</span></td>
            <td>
                <span class="badge ${user.is_active ? 'status-active' : 'status-inactive'}">
                    ${user.is_active ? 'Active' : 'Inactive'}
                </span>
            </td>
            <td>
                ${user.is_active ? 
                    `<button class="btn btn-sm btn-warning btn-action" onclick="toggleUserStatus(${user.id}, false)">
                        <i class="bi bi-x-circle"></i> Deactivate
                    </button>` :
                    `<button class="btn btn-sm btn-success btn-action" onclick="toggleUserStatus(${user.id}, true)">
                        <i class="bi bi-check-circle"></i> Activate
                    </button>`
                }
            </td>
        </tr>
    `).join('');
}

async function toggleUserStatus(userId, activate) {
    const action = activate ? 'activate' : 'deactivate';
    
    try {
        const response = await fetch(`${API_BASE_URL}/admin/users/${userId}/${action}`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        
        if (response.ok) {
            loadUsers();
            showNotification('success', `User ${activate ? 'activated' : 'deactivated'} successfully!`);
        } else {
            const data = await response.json();
            alert(data.message || `Failed to ${action} user`);
        }
    } catch (error) {
        console.error(`Error ${action} user:`, error);
    }
}

// Reports Functions
async function generateReport(format) {
    try {
        const response = await fetch(`${API_BASE_URL}/reports/students?format=${format}`, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        
        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `students_report.${format === 'pdf' ? 'pdf' : 'xlsx'}`;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            showNotification('success', 'Report downloaded successfully!');
        } else {
            alert('Failed to generate report');
        }
    } catch (error) {
        console.error('Error generating report:', error);
        alert('Error generating report');
    }
}

async function showAnalytics() {
    document.getElementById('analyticsSection').style.display = 'block';
    
    try {
        const response = await fetch(`${API_BASE_URL}/reports/analytics`, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            const analytics = data.analytics || {};
            
            const html = `
                <div class="row">
                    <div class="col-md-4">
                        <h6>Total Students</h6>
                        <h3>${analytics.total_students || 0}</h3>
                    </div>
                    <div class="col-md-4">
                        <h6>Recent Admissions</h6>
                        <h3>${analytics.recent_admissions || 0}</h3>
                    </div>
                    <div class="col-md-4">
                        <h6>Gender Distribution</h6>
                        <ul class="list-unstyled">
                            ${Object.entries(analytics.gender_distribution || {}).map(([gender, count]) => 
                                `<li>${gender}: ${count}</li>`
                            ).join('')}
                        </ul>
                    </div>
                </div>
            `;
            
            document.getElementById('analyticsData').innerHTML = html;
        } else {
            document.getElementById('analyticsData').innerHTML = '<p class="text-danger">Failed to load analytics</p>';
        }
    } catch (error) {
        console.error('Error loading analytics:', error);
        document.getElementById('analyticsData').innerHTML = '<p class="text-danger">Error loading analytics</p>';
    }
}

// Helper Functions
function formatDate(dateString) {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

function showNotification(type, message) {
    // Simple notification - can be enhanced with a toast library
    alert(message);
}