# Deployment Guide

This guide covers different deployment options for the Student Management System.

## Table of Contents
- [Local Development](#local-development)
- [Docker Deployment](#docker-deployment)
- [Production Deployment](#production-deployment)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)

---

## Local Development

### Quick Start

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```powershell
   copy .env.example .env
   ```

3. **Initialize database:**
   ```powershell
   python scripts/init_db.py
   ```

4. **Run the application:**
   ```powershell
   python run.py
   ```

Access the API at: http://localhost:5000

### Development with Hot Reload

```powershell
$env:FLASK_ENV="development"
$env:FLASK_DEBUG="True"
python run.py
```

---

## Docker Deployment

### Prerequisites
- Docker Desktop installed
- Docker Compose installed

### Build and Run

1. **Start all services:**
   ```powershell
   docker-compose up -d
   ```

2. **View logs:**
   ```powershell
   docker-compose logs -f app
   ```

3. **Stop services:**
   ```powershell
   docker-compose down
   ```

### Database Migrations in Docker

```powershell
docker-compose exec app flask db upgrade
```

### Access the Application
- API: http://localhost:5000
- Database: localhost:5432

---

## Production Deployment

### Using Gunicorn

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn:**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
   ```

### Using systemd (Linux)

1. **Create service file** `/etc/systemd/system/student-mgmt.service`:
   ```ini
   [Unit]
   Description=Student Management System
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/path/to/app
   Environment="PATH=/path/to/venv/bin"
   ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. **Enable and start:**
   ```bash
   sudo systemctl enable student-mgmt
   sudo systemctl start student-mgmt
   ```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

---

## Environment Variables

### Required Variables

```env
SECRET_KEY=your-production-secret-key
JWT_SECRET_KEY=your-production-jwt-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/student_management
```

### Optional Variables

```env
FLASK_DEBUG=False
FLASK_ENV=production
PORT=5000
JWT_ACCESS_TOKEN_EXPIRES=3600
```

### Generating Secure Keys

```python
import secrets
print(secrets.token_hex(32))
```

---

## Database Setup

### PostgreSQL (Recommended for Production)

1. **Install PostgreSQL:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install postgresql postgresql-contrib

   # macOS
   brew install postgresql
   ```

2. **Create database:**
   ```sql
   CREATE DATABASE student_management;
   CREATE USER admin WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE student_management TO admin;
   ```

3. **Update .env:**
   ```env
   DATABASE_URL=postgresql://admin:your_password@localhost:5432/student_management
   ```

### SQLite (Development Only)

```env
DATABASE_URL=sqlite:///student_management.db
```

### Database Migrations

```bash
# Initialize migrations
flask db init

# Create migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade
```

---

## Cloud Deployment

### Heroku

1. **Install Heroku CLI**

2. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   ```

3. **Add PostgreSQL:**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set JWT_SECRET_KEY=your-jwt-secret-key
   ```

5. **Deploy:**
   ```bash
   git push heroku main
   ```

6. **Initialize database:**
   ```bash
   heroku run python scripts/init_db.py
   ```

### AWS EC2

1. **Launch EC2 instance** (Ubuntu 22.04)

2. **Install dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv postgresql nginx
   ```

3. **Clone and setup:**
   ```bash
   git clone <your-repo>
   cd student-management-system
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure systemd and nginx** (see sections above)

### Railway

1. **Install Railway CLI:**
   ```bash
   npm install -g railway
   ```

2. **Login and init:**
   ```bash
   railway login
   railway init
   ```

3. **Add PostgreSQL:**
   ```bash
   railway add postgresql
   ```

4. **Deploy:**
   ```bash
   railway up
   ```

---

## Performance Optimization

### Database Connection Pooling

Add to your settings:
```python
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size': 10,
    'pool_recycle': 3600,
    'pool_pre_ping': True
}
```

### Caching with Redis

```python
from flask_caching import Cache

cache = Cache(app, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
})
```

### Rate Limiting

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["200 per day", "50 per hour"]
)
```

---

## Monitoring

### Application Logs

```bash
tail -f logs/student_management.log
```

### Database Monitoring

```sql
-- Check active connections
SELECT count(*) FROM pg_stat_activity;

-- Check table sizes
SELECT relname, pg_size_pretty(pg_total_relation_size(relid))
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

---

## Backup and Recovery

### Database Backup

```bash
# Backup
pg_dump student_management > backup_$(date +%Y%m%d).sql

# Restore
psql student_management < backup_20240102.sql
```

### Automated Backups (Cron)

```bash
# Add to crontab
0 2 * * * pg_dump student_management > /backups/db_$(date +\%Y\%m\%d).sql
```

---

## Security Checklist

- [ ] Change default admin credentials
- [ ] Use strong SECRET_KEY and JWT_SECRET_KEY
- [ ] Enable HTTPS in production
- [ ] Use PostgreSQL (not SQLite) in production
- [ ] Set up firewall rules
- [ ] Enable rate limiting
- [ ] Regular security updates
- [ ] Monitor logs for suspicious activity
- [ ] Use environment variables for secrets
- [ ] Enable CORS only for trusted domains

---

## Troubleshooting

### Port Already in Use
```powershell
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Database Connection Issues
```bash
# Check PostgreSQL is running
systemctl status postgresql

# Test connection
psql -h localhost -U admin -d student_management
```

### Permission Errors
```bash
# Fix file permissions
chmod +x scripts/*.py
```

---

## Support

For deployment issues:
- Check logs: `logs/student_management.log`
- Review error messages
- Verify environment variables
- Test database connectivity

---

**Production Deployment Checklist:**

- [ ] All environment variables set
- [ ] Database migrations applied
- [ ] Default admin password changed
- [ ] HTTPS configured
- [ ] Logs directory created
- [ ] Backups configured
- [ ] Monitoring set up
- [ ] Rate limiting enabled
- [ ] Security headers configured