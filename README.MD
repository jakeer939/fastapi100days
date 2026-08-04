# Day 3 - FastAPI Authentication & Authorization

## Overview

Today's work focused on securing the Todo API using JWT-based authentication and implementing role-based authorization. The project now supports protected routes, user-specific data access, password updates, and administrator-only operations.

---

## Features Implemented

### JWT Authentication
- Configured `OAuth2PasswordBearer`.
- Protected API endpoints using bearer tokens.
- Implemented `get_current_user()` dependency to extract and validate user information from JWT.

### User Authorization
- Restricted all Todo operations to authenticated users.
- Users can only access their own todos.
- Ownership validation added for:
  - Get Todo
  - Update Todo
  - Delete Todo

### Todo API Improvements
- Added router prefix and tags.

```
/todos
```

Available endpoints:

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/todos/` | Get authenticated user's todos |
| GET | `/todos/{id}` | Get a specific todo |
| POST | `/todos/` | Create a todo |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

---

## Admin Module

Created a dedicated Admin Router.

```
/admin
```

### Admin Features

- View all todos.
- Delete any todo regardless of owner.
- Role-based authorization using JWT claims.

Only users with:

```
role = "admin"
```

can access these endpoints.

---

## User Module

Created a dedicated User Router.

```
/user
```

### User Features

- View authenticated user's profile.
- Change account password.
- Verify current password before updating.
- Store new password securely using bcrypt hashing.

---

## Security Improvements

- JWT-protected endpoints.
- Role-based access control.
- Ownership validation.
- Password hashing with bcrypt.
- Password verification before updates.
- Protected admin routes.
- Protected user profile routes.

---

## Concepts Learned

- OAuth2PasswordBearer
- JWT Authentication
- Protected Routes
- Dependency Injection
- Role-Based Authorization (RBAC)
- User Ownership Validation
- Password Verification
- Password Update Flow
- SQLAlchemy Authorization Queries
- FastAPI Router Organization

---

## Project Structure

```
Todosapp/
│
├── auth.py
├── admin.py
├── users.py
├── todos.py
├── database.py
├── databasemodel.py
└── main.py
```

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)
- OAuth2PasswordBearer
- Uvicorn

---

## Key Takeaways

- Built a complete JWT authentication workflow.
- Secured CRUD endpoints using authentication and authorization.
- Implemented admin-only functionality.
- Added user profile management with secure password updates.
- Organized the backend into separate routers for authentication, todos, users, and admin operations.

---