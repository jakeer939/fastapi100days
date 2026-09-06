# FastAPI Backend Engineering

A hands-on repository for learning and practicing backend development with **FastAPI, SQLAlchemy, Pydantic, and SQLite**.

The repository contains progressively built APIs and backend exercises covering core FastAPI concepts, database integration, CRUD operations, validation, dependency injection, and authentication-related functionality.

## Current Coverage

- FastAPI application structure
- API routers with `APIRouter`
- Dependency injection with `Depends`
- SQLAlchemy ORM models and sessions
- Pydantic request and response schemas
- SQLite database integration
- CRUD API design
- HTTP status codes and exception handling
- Password hashing with bcrypt/passlib
- User and contact management APIs
- Book API development
- Debugging response validation and database issues

## Main Backend Components

### Todo / Contact APIs

Practice projects cover creating, reading, updating, and deleting records with SQLAlchemy-backed persistence.

### User API

Includes user model and user creation/retrieval flows with password hashing.

### Book API

A separate FastAPI + SQLAlchemy API used to practice database-backed resource management.

## Architecture

```text
HTTP Client
    │
    ▼
FastAPI Routes
    │
    ▼
Pydantic Schemas
    │
    ▼
SQLAlchemy ORM
    │
    ▼
SQLite Database
```

## Key Concepts

- Request vs response models
- ORM models vs Pydantic schemas
- Dependency injection
- Database session lifecycle
- `db.commit()` and `db.refresh()`
- `scalar()` vs `scalars()`
- Response validation
- Router organization
- Exception handling
- Password hashing
- CORS configuration

## Repository Structure

```text
fastapi100days/
├── Todosapp/
├── book_api/
├── contact_api/
├── README.MD
└── contact.db
```

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Passlib / bcrypt

## Status

**In progress.** This repository is used to build backend fundamentals through small, working API implementations. The codebase will evolve toward more structured production-style FastAPI applications.

## Author

**Jakeer**

GitHub: [@jakeer939](https://github.com/jakeer939)
