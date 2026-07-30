# PhoneBook Contact API

## Overview

Built the foundation of a simple Contact Management REST API using **FastAPI**, **SQLAlchemy**, and **SQLite**. The project currently supports creating contacts and retrieving all saved contacts.

## Tech Stack

* FastAPI
* SQLAlchemy ORM
* SQLite
* Pydantic

## Features Implemented

### Create a New Contact

* Accepts contact details through a POST request.
* Validates request data using Pydantic.
* Stores the contact in the SQLite database.

### Get All Contacts

* Retrieves all contacts stored in the database.
* Returns the data as a JSON response.

## API Endpoints

| Method | Endpoint    | Description           |
| ------ | ----------- | --------------------- |
| `GET`  | `/contacts` | Retrieve all contacts |
| `POST` | `/contacts` | Create a new contact  |

## Concepts Practiced

* Setting up a FastAPI project
* Connecting FastAPI with SQLite using SQLAlchemy
* Creating ORM models
* Using Pydantic request models
* Managing database sessions with dependency injection
* Implementing basic CRUD operations (Create & Read)

