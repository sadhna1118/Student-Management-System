// Demo data for offline/demo mode
const DEMO_DATA = {
    users: [
        {
            id: 1,
            username: 'admin',
            email: 'admin@example.com',
            first_name: 'Admin',
            last_name: 'User',
            role: { id: 1, name: 'admin' },
            is_active: true
        },
        {
            id: 2,
            username: 'teacher1',
            email: 'teacher@example.com',
            first_name: 'Jane',
            last_name: 'Smith',
            role: { id: 2, name: 'teacher' },
            is_active: true
        }
    ],
    students: [
        {
            id: 1,
            student_id: 'STU001',
            user: {
                id: 3,
                username: 'john.doe',
                email: 'john.doe@example.com',
                first_name: 'John',
                last_name: 'Doe'
            },
            date_of_birth: '2000-01-15',
            gender: 'Male',
            phone: '+1234567890',
            address: '123 Main St, City',
            admission_date: '2023-09-01'
        },
        {
            id: 2,
            student_id: 'STU002',
            user: {
                id: 4,
                username: 'jane.smith',
                email: 'jane.smith@example.com',
                first_name: 'Jane',
                last_name: 'Smith'
            },
            date_of_birth: '2001-03-20',
            gender: 'Female',
            phone: '+1234567891',
            address: '456 Oak Ave, Town',
            admission_date: '2023-09-01'
        },
        {
            id: 3,
            student_id: 'STU003',
            user: {
                id: 5,
                username: 'mike.johnson',
                email: 'mike.johnson@example.com',
                first_name: 'Mike',
                last_name: 'Johnson'
            },
            date_of_birth: '1999-07-10',
            gender: 'Male',
            phone: '+1234567892',
            address: '789 Pine Rd, Village',
            admission_date: '2023-08-15'
        },
        {
            id: 4,
            student_id: 'STU004',
            user: {
                id: 6,
                username: 'sarah.wilson',
                email: 'sarah.wilson@example.com',
                first_name: 'Sarah',
                last_name: 'Wilson'
            },
            date_of_birth: '2000-11-25',
            gender: 'Female',
            phone: '+1234567893',
            address: '321 Elm St, City',
            admission_date: '2023-09-01'
        },
        {
            id: 5,
            student_id: 'STU005',
            user: {
                id: 7,
                username: 'david.brown',
                email: 'david.brown@example.com',
                first_name: 'David',
                last_name: 'Brown'
            },
            date_of_birth: '2001-05-08',
            gender: 'Male',
            phone: '+1234567894',
            address: '654 Maple Dr, Town',
            admission_date: '2023-08-20'
        }
    ]
};

// Demo API handler
class DemoAPI {
    constructor() {
        this.accessToken = 'demo-token-12345';
        this.currentUser = null;
    }

    async login(username, password) {
        // Simulate API delay
        await this.delay(500);
        
        // Check credentials
        if (username === 'admin' && password === 'admin123') {
            this.currentUser = DEMO_DATA.users[0];
            return {
                success: true,
                access_token: this.accessToken,
                user: this.currentUser
            };
        } else if (username === 'teacher1' && password === 'teacher123') {
            this.currentUser = DEMO_DATA.users[1];
            return {
                success: true,
                access_token: this.accessToken,
                user: this.currentUser
            };
        }
        
        throw new Error('Invalid credentials');
    }

    async getStudents() {
        await this.delay(300);
        return {
            success: true,
            students: DEMO_DATA.students,
            total: DEMO_DATA.students.length
        };
    }

    async getStudent(id) {
        await this.delay(200);
        const student = DEMO_DATA.students.find(s => s.id === id);
        if (!student) throw new Error('Student not found');
        return { success: true, student };
    }

    async createStudent(data) {
        await this.delay(400);
        const newId = DEMO_DATA.students.length + 1;
        const newStudent = {
            id: newId,
            student_id: `STU${String(newId).padStart(3, '0')}`,
            user: {
                id: newId + 10,
                username: data.username,
                email: data.email,
                first_name: data.first_name,
                last_name: data.last_name
            },
            date_of_birth: data.date_of_birth,
            gender: data.gender,
            phone: data.phone || null,
            address: data.address || null,
            admission_date: data.admission_date || new Date().toISOString().split('T')[0]
        };
        DEMO_DATA.students.push(newStudent);
        return { success: true, student: newStudent };
    }

    async updateStudent(id, data) {
        await this.delay(400);
        const index = DEMO_DATA.students.findIndex(s => s.id === id);
        if (index === -1) throw new Error('Student not found');
        
        DEMO_DATA.students[index] = {
            ...DEMO_DATA.students[index],
            user: {
                ...DEMO_DATA.students[index].user,
                email: data.email,
                first_name: data.first_name,
                last_name: data.last_name
            },
            date_of_birth: data.date_of_birth,
            gender: data.gender,
            phone: data.phone,
            address: data.address,
            admission_date: data.admission_date
        };
        
        return { success: true, student: DEMO_DATA.students[index] };
    }

    async deleteStudent(id) {
        await this.delay(300);
        const index = DEMO_DATA.students.findIndex(s => s.id === id);
        if (index === -1) throw new Error('Student not found');
        
        DEMO_DATA.students.splice(index, 1);
        return { success: true };
    }

    async getUsers() {
        await this.delay(300);
        return {
            success: true,
            users: DEMO_DATA.users,
            total: DEMO_DATA.users.length
        };
    }

    async getAnalytics() {
        await this.delay(300);
        const maleCount = DEMO_DATA.students.filter(s => s.gender === 'Male').length;
        const femaleCount = DEMO_DATA.students.filter(s => s.gender === 'Female').length;
        
        return {
            success: true,
            analytics: {
                total_students: DEMO_DATA.students.length,
                recent_admissions: 2,
                gender_distribution: {
                    Male: maleCount,
                    Female: femaleCount
                }
            }
        };
    }

    async generateReport(format) {
        await this.delay(500);
        // In demo mode, we can't actually generate files
        throw new Error('Report generation is not available in demo mode. Please connect to a live backend.');
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Export demo API
window.DEMO_API = new DemoAPI();