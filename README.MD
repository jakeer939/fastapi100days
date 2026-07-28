# Day 2 - FastAPI CRUD with SQLite

## Overview

Today I focused on learning how FastAPI interacts with SQLite using SQLAlchemy. The goal was to understand the complete CRUD workflow and the purpose of each component instead of just following syntax.

## Topics Covered

- FastAPI project structure
- SQLAlchemy ORM
- SQLite database connection
- Engine and SessionLocal
- Dependency Injection using `Depends`
- Database sessions
- SQLAlchemy Models
- Pydantic Request Models
- CRUD Operations
- HTTP Exception Handling
- SQLAlchemy `select()` queries

## Implemented Features

### Create
- Add a new todo
- Automatic ID generation using SQLite
- Request validation using Pydantic

### Read
- Get all todos
- Get a todo by ID

### Update
- Update todo details
- Commit changes to the database
- Refresh updated object

### Delete
- Delete a todo by ID
- Handle invalid IDs

## Key Concepts Learned

- Difference between SQLAlchemy Models and Pydantic Models
- Why `Session` is required
- Purpose of `Depends(get_db)`
- Why `yield` is used instead of `return`
- Difference between `db.get()` and `select()`
- When to use `db.refresh()`
- Automatic primary key generation
- ORM maps Python classes to database tables

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn