# SWIFT Connect Onboarding System

## Requirements Analysis

### User Roles
- **Business Users**: Submit and track onboarding requests
- **CRM Admin**: Review, approve/reject requests and manage workflow

### Requirements

#### Functional Requirements
- User authentication and authorization
- Business user portal for request submission
- Admin dashboard for request management
- Request status tracking
- Approval/rejection workflow

#### Non-Functional Requirements
- Fast response time
- User-friendly interface
- Role-based access control
- Secure data handling

## Setup & Running

1. Create and activate virtual environment:
```bash
python -m venv venv
```

2. Install dependencies:
```bash
pip install flask flask-sqlalchemy flask-login flask-wtf pymysql
```

3. Create MariaDB database and user:
```sql
CREATE DATABASE swift_connect;
CREATE USER 'swift_user'@'localhost' IDENTIFIED BY 'swift_password';
GRANT ALL PRIVILEGES ON swift_connect.* TO 'swift_user'@'localhost';
FLUSH PRIVILEGES;
```

4. Run the application:
```bash
python run.py
```


The server will start at http://localhost:5000

## Test Users

The application creates two test users automatically:

### Admin User
- Username: `admin`
- Password: `admin123`
- Can view and manage all requests

### Business User
- Username: `business`
- Password: `business123`
- Can submit and track requests

## Implementation Details

### Technology Stack
- Python/Flask
- MariaDB database
- Flask-SQLAlchemy
- Flask-Login
- Bootstrap CSS
