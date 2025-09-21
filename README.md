# 📚 LibraryDB CRUD Application (FastAPI + MySQL)

This project is a simple **CRUD application** built with **FastAPI** and **SQLAlchemy**, connected to a **MySQL database**.  
It demonstrates how to manage a **Library Management System**, including **Members** and **Books** entities.

---

## 🚀 Features
- **Members CRUD**
  - Add a new member
  - View all members
  - Update member details
  - Delete a member

- **Books CRUD**
  - Add a new book
  - View all books
  - Update book details
  - Delete a book

- Database: **MySQL**
- ORM: **SQLAlchemy**
- API Docs: **Swagger UI** at `/docs`

---

## 📂 Project Structure
wk-8-Jenny-light/

│── app/

│ ├── main.py # FastAPI entry point

│ ├── database.py # DB connection setup

│ ├── models.py # SQLAlchemy models

│ ├── schemas.py # Pydantic schemas

│ ├── crud.py # CRUD logic

│ ├── init.py

│── venv/ # Virtual environment (ignored in git)

│── requirements.txt # Dependencies

│── README.md # Project guide


---


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Jenny-light/LibraryDB-FastAPI.git
cd LibraryDB-FastAPI
```

### 2. Create & Activate Virtual Environment
# Windows (PowerShell)
```bash
python -m venv venv
.\venv\Scripts\activate
```

# macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup MySQL Database

Log into MySQL and create a database:
```bash
CREATE DATABASE LibraryDB;
```

Update app/database.py with your MySQL username & password:
```bash
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:yourpassword@localhost/LibraryDB"
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

## 📖 API Documentation

Once the server is running, open:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

## 🔗 Example Requests
Create a Member
```bash
{
  "first_name": "Jennifer",
  "last_name": "Omoregie",
  "email": "jenny@example.com",
  "phone": "08012345678",
  "address": "12 Library Street, Lagos",
  "membership_date": "2025-09-21"
}

Create a Book
{
  "title": "Data Analysis for Beginners",
  "isbn": "978-1234567890",
  "published_year": 2022,
  "copies_available": 5
}
```

## 🛠 Tech Stack

FastAPI

MySQL

SQLAlchemy

Pydantic

Uvicorn

## 👩‍💻 Author

Jennifer Omoregie

## 📜 License

This project is licensed under the MIT License.
