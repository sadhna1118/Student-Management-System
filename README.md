# Student Management System

🎓 Student Management System

A secure, role-based Student Management System built using Python (Flask) and SQLAlchemy, designed to manage students, users, and reports efficiently.
This project follows clean architecture, RESTful API principles, and industry-standard best practices.

🔗 Live Demo (Frontend):
https://sadhna1118.github.io/Student-Management-System/

📌 Key Features
🔐 Authentication & Authorization

JWT-based authentication

Role-based access control:

Admin

Teacher

Student

Secure login & token refresh mechanism

👩‍🎓 Student Management

Add, update, delete, and view student records

Auto-generated unique student IDs

Search and filter students easily

👥 User Management

Admin can manage users by roles

Controlled access to system features

📊 Reports & Dashboard

Generate PDF and Excel reports

Student statistics (e.g., gender distribution)

Centralized dashboard for quick insights

⚙️ System & Deployment

Clean modular architecture (models, services, routes)

Environment-based configuration using .env

Docker & Docker Compose support

Ready for cloud deployment (Render / Railway / AWS)

| Category | Technology             |
| -------- | ---------------------- |
| Backend  | Python, Flask          |
| Database | SQLite / PostgreSQL    |
| ORM      | SQLAlchemy             |
| Auth     | JWT                    |
| Frontend | HTML, CSS, JavaScript  |
| Reports  | PDF, Excel             |
| DevOps   | Docker, Docker Compose |
| Tools    | Git, GitHub            |




Student-Management-System/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── __init__.py
│
├── scripts/
├── tests/
├── run.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md


🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/sadhna1118/Student-Management-System.git
cd Student-Management-System

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables
cp .env.example .env


Update .env with your database and secret keys.

5️⃣ Run the Application
python run.py


App will run at:
📍 http://localhost:5000

🔑 Demo Credentials
Role	Username	Password
Admin	admin	admin123
Teacher	teacher1	teacher123

👩‍💻 Author

Sadhna
🎓 Master of Computer Science
💻 Python | Flask | SQL | Web Development
🔗 GitHub: https://github.com/sadhna1118

⭐ Support

If you like this project, please ⭐ star the repository — it helps a lot!
