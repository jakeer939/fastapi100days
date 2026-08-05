FastAPI Revision
Overview

Today's session focused on revising FastAPI fundamentals by building a PhoneBook REST API using FastAPI, SQLAlchemy, SQLite, and Pydantic. The emphasis was on understanding CRUD operations, dependency injection, response models, and common debugging scenarios.

Topics Revised
FastAPI project structure
APIRouter configuration
Dependency Injection with Depends
SQLAlchemy ORM models
Pydantic request and response models
SQLite database integration
CRUD operations
HTTP status codes and exception handling
Password hashing using passlib
Work Completed
Project Setup
Configured main.py as the application entry point.
Registered API routers.
Connected the SQLite database.
Created database tables using SQLAlchemy metadata.
PhoneBook API
Implemented GET endpoint to retrieve all contacts.
Implemented POST endpoint to create a new contact.
Implemented PUT endpoint to update an existing contact.
Added dependency injection for database sessions.
Used SQLAlchemy ORM for database operations.
Added response validation using Pydantic models.
Implemented proper error handling for missing contacts.
User API
Created the Users database model.
Implemented user creation endpoint.
Added password hashing using bcrypt.
Configured user retrieval endpoint.
Debugging & Fixes
Fixed router prefix configuration.
Corrected response_model definitions.
Fixed missing return statement causing ResponseValidationError.
Resolved SQLite schema mismatch (owner_id column).
Corrected SQLAlchemy query to use ORM models instead of Pydantic models.
Fixed incorrect db.commit() usage.
Fixed update logic by modifying ORM object attributes instead of calling the object.
Corrected tuple assignment caused by a trailing comma.
Improved understanding of .scalar(), .scalars(), .all(), and db.refresh().
Key Concepts Revised
Difference between SQLAlchemy models and Pydantic schemas.
Why Base.metadata.create_all() does not update existing tables.
Difference between db.scalar() and db.scalars().
Purpose of db.commit() and db.refresh().
Request model vs Response model.
Dependency Injection with Depends.
Password hashing workflow using passlib.
Tech Stack
Python
FastAPI
SQLAlchemy
SQLite
Pydantic
Passlib (bcrypt)