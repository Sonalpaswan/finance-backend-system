# 💰 Finance Management Backend System (FastAPI)

## 📌 Project Overview

This project is a **Finance Management Backend System** built using **FastAPI**.
It allows users to manage financial transactions (income & expenses), analyze summaries, and access features based on their roles.

The system is designed to demonstrate **backend development skills**, including API design, database handling, validation, and role-based access control.

---

## 🚀 Features

### 🔹 1. Financial Records Management

* Create transactions (income/expense)
* View all transactions
* Update transactions
* Delete transactions
* Filter transactions by:

  * Type (income/expense)
  * Category
  * Date

---

### 🔹 2. Summary & Analytics

* Total Income calculation
* Total Expense calculation
* Current Balance
* Category-wise summary (if implemented)

---

### 🔹 3. Role-Based Access Control

| Role    | Permissions                                |
| ------- | ------------------------------------------ |
| Admin   | Full access (create, update, delete, view) |
| Analyst | View + filter + summary                    |
| Viewer  | Only view transactions                     |

---

### 🔹 4. Validation & Error Handling

* Input validation using **Pydantic**
* Proper error handling using **HTTPException**
* Prevent invalid data (e.g., negative amount)

---

### 🔹 5. API Interface

* RESTful API using **FastAPI**
* Interactive API testing using Swagger UI

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Validation:** Pydantic

---

## 📁 Project Structure

```
finance-system/
│
├── main.py          # API routes
├── models.py        # Database models
├── schemas.py       # Data validation schemas
├── crud.py          # Business logic
├── database.py      # Database connection
├── finance.db       # SQLite database
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone / Open Project

```bash
cd finance-system
```

### 2️⃣ Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server

```bash
uvicorn main:app --reload --port 8001
```

---

## 🌐 API Documentation

Open in browser:

```
http://127.0.0.1:8001/docs
```

👉 Swagger UI allows you to test all APIs easily.

---

## 🔌 API Endpoints

| Method | Endpoint             | Description                     |
| ------ | -------------------- | ------------------------------- |
| POST   | /transactions        | Create transaction (Admin only) |
| GET    | /transactions        | View all transactions           |
| PUT    | /transactions/{id}   | Update transaction (Admin only) |
| DELETE | /transactions/{id}   | Delete transaction (Admin only) |
| GET    | /transactions/filter | Filter transactions             |
| GET    | /summary             | Financial summary               |

---

## 🧪 Example Request (Create Transaction)

```json
{
  "amount": 5000,
  "type": "income",
  "category": "salary",
  "date": "2026-04-03",
  "notes": "first entry",
  "user": {
    "name": "sonal",
    "role": "admin"
  }
}
```

---

## 🎯 Key Highlights

* Clean and modular backend structure
* Role-based access implementation
* Real-world financial tracking logic
* Scalable and maintainable code

---

## 📌 Conclusion

This project demonstrates a strong understanding of:

* Backend API development
* Database design and operations
* Business logic implementation
* Role-based system design

It can be extended further with authentication, frontend integration, and advanced analytics.

---

## 👩‍💻 Author

**Sonal**
Aspiring Software Engineer 🚀
