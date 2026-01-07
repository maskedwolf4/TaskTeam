# TaskTeam 📋

> A modern B2B SaaS application for managing and assigning tasks to team members and organizations

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE.md)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19.2.0-blue.svg)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-7.2.4-646CFF.svg)](https://vitejs.dev/)

## 🌟 Overview

TaskTeam is a comprehensive task management platform designed for modern teams and organizations. Built with scalability and user experience in mind, it provides powerful features for task assignment, tracking, and collaboration across teams.

## ✨ Features

- **User Authentication & Authorization**: Secure authentication powered by Clerk
- **Task Management**: Create, assign, update, and track tasks efficiently
- **Team Collaboration**: Organize tasks across teams and organizations
- **Modern UI**: Responsive React-based interface with smooth navigation
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
- **Framework**: React 19.2.0
- **Build Tool**: Vite 7.2.4
- **Routing**: React Router DOM 7.11.0
- **Authentication UI**: Clerk React 5.59.2
- **Language**: JavaScript (ES6+)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Backend Requirements
- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer

### Frontend Requirements
- Node.js 18+ and npm
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

#### Configure Backend Environment Variables

Edit the `backend/.env` file with your credentials:

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

#### Run the Backend

```bash
# Start the FastAPI server
python start.py

# Or use uvicorn directly
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create environment file
cp src/.env.example .env
```

#### Configure Frontend Environment Variables

Edit the `frontend/.env` file:

```env
VITE_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key_here
```

#### Run the Frontend

```bash
# Start development server
npm run dev
```

The application will be available at `http://localhost:5173`

### 4. API Documentation

Once the backend is running, access the interactive API documentation:
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
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── pages/            # Page components
│   │   ├── services/         # API services
│   │   ├── styles/           # CSS styles
│   │   ├── App.jsx           # Main App component
│   │   └── main.jsx          # Application entry
│   ├── public/               # Static assets
│   ├── index.html            # HTML template
│   ├── package.json          # Dependencies
│   └── vite.config.js        # Vite configuration
├── LICENSE.md
└── README.md
```

## 🔑 Key Dependencies

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Clerk Backend API**: User authentication and management
- **Svix**: Webhook infrastructure
- **PyJWT**: JSON Web Token implementation
- **HTTPX**: Next-generation HTTP client
- **Uvicorn**: Lightning-fast ASGI server

### Frontend
- **React**: UI library for building user interfaces
- **Vite**: Next-generation frontend build tool
- **React Router DOM**: Declarative routing for React
- **Clerk React**: Pre-built authentication components
- **ESLint**: Code quality and consistency

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
  - Task queue for background jobs (Celery/RQ integration)
  - Real-time presence tracking
  - Rate limiting and API throttling

### Phase 2: Database Enhancement
- **MongoDB Integration** 🎯
  - Migration strategy from SQLite to MongoDB
  - Flexible schema for complex task metadata
  - Better handling of nested documents and arrays
  - Improved query performance for large datasets
  - Support for geospatial queries (if location features added)
  - GridFS for file storage

### Phase 3: Collaboration Features
- **Comment System** 🎯
  - Threaded comments on tasks with nested replies
  - Mention team members with @username notifications
  - Rich text editor support (Markdown/WYSIWYG options)
  - File attachments in comments (images, documents, etc.)
  - Comment reactions and emoji support
  - Comment notifications and activity feed
  - Comment search and filtering
  - Edit history and version tracking
  - Real-time comment updates via WebSocket

### Phase 4: Advanced Features
- **Real-time Collaboration**
  - WebSocket integration for live updates
  - Collaborative task editing
  - Live cursor tracking and user presence
  - Real-time notifications
  
- **Analytics Dashboard**
  - Task completion metrics and trends
  - Team productivity insights
  - Time tracking and reporting
  - Burndown charts and sprint analytics
  - Custom reports and exports
  
- **Enhanced Notifications**
  - Email notifications with templates
  - Push notifications (web and mobile)
  - In-app notification center
  - Customizable notification preferences
  - Digest emails for activity summaries
  
- **File Management**
  - Cloud storage integration (S3, Google Drive, Dropbox)
  - File versioning and history
  - Image preview and thumbnails
  - Drag-and-drop file upload
  - File sharing and permissions

- **Advanced Task Features**
  - Subtasks and task dependencies
  - Custom fields and metadata
  - Task templates
  - Recurring tasks
  - Time estimates and tracking
  - Priority levels and labels

### Phase 5: UI/UX Enhancements
- **Design System**
  - Component library (Tailwind CSS or Material-UI)
  - Dark mode support
  - Responsive design improvements
  - Accessibility (WCAG compliance)
  
- **Advanced Search & Filters**
  - Full-text search with Elasticsearch
  - Advanced filtering options
  - Saved searches and views
  - Keyboard shortcuts

### Phase 6: Mobile & Desktop
- **Mobile Applications**
  - Native iOS app (React Native/Flutter)
  - Native Android app (React Native/Flutter)
  - Offline mode support
  - Push notifications
  
- **Desktop Application**
  - Electron-based desktop app
  - System tray integration
  - Native notifications

### Phase 7: Integration & API
- **Third-party Integrations**
  - Slack integration
  - Microsoft Teams integration
  - Google Calendar sync
  - Jira/Asana import
  - Zapier/Make.com webhooks
  
- **Public API**
  - Rate limiting
  - API key management
  - Comprehensive documentation
  - SDKs for popular languages

## 🔧 Development Scripts

### Backend
```bash
cd backend

# Run development server
python start.py

# Run with auto-reload
uvicorn app.main:app --reload

# Run tests (when implemented)
pytest
```

### Frontend
```bash
cd frontend

# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Use ESLint configuration for JavaScript/React code
- Write meaningful commit messages (conventional commits format)
- Add tests for new features
- Update documentation as needed
- Keep pull requests focused and atomic

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👥 Contributors

- [maskedwolf4](https://github.com/maskedwolf4) - MEET WADEKAR

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing backend framework
- [React](https://reactjs.org/) for the powerful UI library
- [Vite](https://vitejs.dev/) for the lightning-fast build tool
- [Clerk](https://clerk.com/) for authentication services
- All contributors and supporters of this project

---

**Note**: This project is under active development. Features and documentation are continuously being updated.

Made with ❤️ by the TaskTeam contributors
