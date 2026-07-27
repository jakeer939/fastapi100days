# Day 7: Connecting FastAPI with SQLite using SQLAlchemy

## 📌 Description

On Day 7, I connected a FastAPI backend to a SQLite database using SQLAlchemy ORM. I configured the database engine, created database sessions, defined models, and established a persistent database connection for storing application data.

---

## 🚀 Topics Covered

* SQLAlchemy installation and setup
* SQLite database configuration
* Creating the SQLAlchemy engine
* Configuring `SessionLocal`
* Using `declarative_base()`
* Creating ORM models
* Defining tables using SQLAlchemy
* Creating database tables with `Base.metadata.create_all()`
* Managing database sessions using FastAPI dependencies

---

## 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## 📂 Project Structure

```text
project/
│
├── main.py
├── database.py
├── databasemodel.py
├── contact.db
├── requirements.txt
└── venv/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

---

## 📖 Learning Outcomes

* Understood how SQLAlchemy connects FastAPI to a SQLite database.
* Learned how to configure the database engine and session.
* Created ORM models using SQLAlchemy.
* Automatically generated database tables using metadata.
* Implemented a reusable database dependency with `get_db()`.

---

---

## 👨‍💻 Author

**Sk Jakeer**

