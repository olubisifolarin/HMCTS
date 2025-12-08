# Task Management System

A full-stack web application for creating and managing tasks, built with Django REST Framework and React.

## Features

- Create new tasks with title, description, status, and due date
- Task validation and error handling
- RESTful API with comprehensive documentation
- Responsive React frontend
- Unit tests for both backend and frontend

## Technology Stack

### Backend
- **Framework**: Django and Django REST Framework
- **Database**: SQLite
- **API Documentation**: drf-yasg (Swagger)
- **Server**: Gunicorn
- **Testing**: Django's built-in test framework
- **Deployment**: Render

### Frontend
- **Framework**: React with Vite
- **Language**: JavaScript
- **HTTP Client**: Fetch API


## Installation and Setup

### Prerequisites
- Python 3.10+
- Node.js 20+

### Backend Setup

1. **Clone the repository**
```bash
   git clone https://github.com/olubisifolarin/HMCTS.git
   cd HMCTS
   cd task_manager
```

2. **Create virtual environment**
```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

5. **Run migrations**
```bash
   python manage.py migrate
```

6. **Collect static files** 
```bash
   python manage.py collectstatic --no-input
```

7. **Start the development server**
```bash
   python manage.py runserver
```
   
   Backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
```bash
   cd task-frontend
```

2. **Install dependencies**
```bash
   npm install
```

3. **Start development server**
```bash
   npm run dev
```
   
   Frontend will be available at `http://localhost:5173`

## API Documentation

### Base URL
```
https://hmcts-9pa0.onrender.com/

```

### Interactive API Documentation
Access Swagger UI at: `https://hmcts-9pa0.onrender.com/swagger/`


## License

This project is built by me.
