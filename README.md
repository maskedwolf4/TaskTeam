# TaskTeam 📋

> A modern B2B SaaS application for managing and assigning tasks to team members and organizations

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE.md)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0+-green.svg)](https://fastapi.tiangolo.com/)

## 🌟 Overview

TaskTeam is a comprehensive task management platform designed for modern teams and organizations. Built with scalability and user experience in mind, it provides powerful features for task assignment, tracking, and collaboration across teams.

## ✨ Features

- **User Authentication & Authorization**: Secure authentication powered by Clerk
- **Task Management**: Create, assign, update, and track tasks efficiently
- **Team Collaboration**: Organize tasks across teams and organizations
- **RESTful API**: Well-documented API built with FastAPI
- **Real-time Updates**: Webhook integration for instant notifications
- **Scalable Architecture**: Designed for growth from small teams to enterprises

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.128.0+
- **Database**: SQLite (SQLAlchemy ORM)
- **Authentication**: Clerk Backend API
- **Webhooks**: Svix for secure webhook handling
- **Runtime**: Python 3.12+

### Frontend
- Coming soon - React/Next.js implementation planned

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- A Clerk account for authentication

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/maskedwolf4/TaskTeam.git
cd TaskTeam
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies using uv
uv sync

# Create environment file
cp .env.example .env
```

### 3. Configure Environment Variables

Edit the `.env` file with your credentials:

```env
# Clerk Configuration
CLERK_SECRET_KEY=your_clerk_secret_key_here
CLERK_WEBHOOK_SECRET=your_webhook_secret_here

# Database Configuration
DATABASE_URL=sqlite:///./taskboard.db

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

### 4. Run the Application

```bash
# Start the FastAPI server
python start.py

# Or use uvicorn directly
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### 5. API Documentation

Once running, access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📁 Project Structure

```
TaskTeam/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application entry
│   │   ├── models/           # SQLAlchemy models
│   │   ├── routes/           # API endpoints
│   │   ├── services/         # Business logic
│   │   └── utils/            # Helper functions
│   ├── .env.example          # Environment template
│   ├── pyproject.toml        # Project dependencies
│   ├── start.py              # Application starter
│   └── taskboard.db          # SQLite database
├── frontend/                 # Frontend application (planned)
├── LICENSE.md
└── README.md
```

## 🔑 Key Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Clerk Backend API**: User authentication and management
- **Svix**: Webhook infrastructure
- **PyJWT**: JSON Web Token implementation
- **HTTPX**: Next-generation HTTP client
- **Uvicorn**: Lightning-fast ASGI server

## 📚 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/webhook` - Clerk webhook handler

### Tasks
- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/{id}` - Get task details
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

### Organizations
- `GET /api/organizations` - List organizations
- `POST /api/organizations` - Create organization
- `GET /api/organizations/{id}/tasks` - Get organization tasks

## 🚧 Future Development Roadmap

### Phase 1: Performance & Scalability
- **Redis Integration** 🎯
  - Implement Redis for caching frequently accessed data
  - Session management and user state caching
  - Task queue for background jobs
  - Real-time presence tracking

### Phase 2: Database Enhancement
- **MongoDB Integration** 🎯
  - Migration strategy from SQLite to MongoDB
  - Flexible schema for complex task metadata
  - Better handling of nested documents
  - Improved query performance for large datasets
  - Support for geospatial queries (if location features added)

### Phase 3: Collaboration Features
- **Comment System** 🎯
  - Threaded comments on tasks
  - Mention team members with @username
  - Rich text editor support (Markdown/WYSIWYG)
  - File attachments in comments
  - Comment notifications and activity feed
  - Comment search and filtering

### Phase 4: Advanced Features
- **Real-time Collaboration**
  - WebSocket integration for live updates
  - Collaborative task editing
  - Live cursor tracking
  
- **Analytics Dashboard**
  - Task completion metrics
  - Team productivity insights
  - Time tracking and reporting
  
- **Notifications System**
  - Email notifications
  - Push notifications
  - In-app notification center
  - Customizable notification preferences
  
- **File Management**
  - Cloud storage integration (S3, Google Drive)
  - File versioning
  - Image preview and thumbnails

### Phase 5: Mobile & Desktop
- Mobile applications (iOS/Android)
- Desktop application (Electron)
- Offline mode support

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👥 Contributors

- [maskedwolf4](https://github.com/maskedwolf4) - MEET WADEKAR
- [meet-wadekar-gh](https://github.com/meet-wadekar-gh)

## 📞 Support

For support, questions, or feedback:
- Open an issue on GitHub
- Contact: [Your contact information]

## 🙏 Acknowledgments

- FastAPI for the amazing framework
- Clerk for authentication services
- All contributors and supporters of this project

---

**Note**: This project is under active development. Features and documentation are continuously being updated.

Made with ❤️ by the TaskTeam contributors
