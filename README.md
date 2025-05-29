
# 📊 FastAPI Sales Analytics Backend

This is a backend system built using **FastAPI** as part of a backend developer assignment for **XTechOn**. It simulates a lightweight analytics platform for small businesses, featuring user authentication, role-based access, CSV sales data ingestion, and analytics endpoints.

---

## 🔧 Features

- ✅ **User Registration & JWT Authentication**
- ✅ **Role-Based Access Control** (`admin`, `user`)
- ✅ **Admin CSV Upload for Sales**
- ✅ **Sales Analytics APIs**:
  - Total Sales, Transaction Count, Average Order Value
  - Top Customers by Revenue
  - Sales by Date Range
- ✅ **Utility Endpoint**: String Compression Logic (`POST /compress-string`)
- ✅ Built using **FastAPI**, **SQLite**, **Pandas**, and **JWT**

---

## 🚀 Getting Started

### 📁 Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-sales-analytics.git
cd fastapi-sales-analytics
```

### 📦 Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔑 Create `.env` File

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
DATABASE_URL=sales.db
```

### ▶️ Run the App

```bash
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/docs for Swagger UI

---

## 🔐 Authentication Flow

1. **Register User**: `POST /register`  
   Fields: `username`, `password`, `role` (`admin` or `user`)

2. **Login**: `POST /login`  
   Returns: JWT Token

3. **Authorize**: Use token in Swagger UI or set `Authorization: Bearer <token>` header

---

## 🧪 API Endpoints Overview

| Method | Endpoint | Description | Role |
|--------|----------|-------------|------|
| POST   | `/register` | Register new user | Public |
| POST   | `/login`    | Login and receive JWT | Public |
| GET    | `/profile`  | View your profile | Authenticated |
| POST   | `/upload-sales` | Upload CSV sales file | Admin only |
| GET    | `/analytics/summary` | Sales summary | Admin only |
| GET    | `/analytics/top-customers?limit=N` | Top N customers | Admin only |
| GET    | `/analytics/by-date?from=...&to=...` | Sales in date range | Admin only |
| POST   | `/compress-string` | Compress input string | Authenticated |

---

## 📄 Example CSV Format

```csv
customer_name,amount,date
Ram,250.75,2024-03-01
Shyam,100.50,2024-03-02
Pawan,320.00,2024-03-02
```

> Upload via `/upload-sales` (admin only)

---

## 📁 Folder Structure

```
app/
├── auth.py          # Login, register, JWT logic
├── database.py      # SQLite DB connection and init
├── models.py        # Pydantic models
├── sales.py         # Sales analytics & upload
├── utils.py         # Compression endpoint
├── main.py          # FastAPI app
├── config.py        # Environment variable loader
requirements.txt
README.md
.env (not committed)
```

---

## ✅ Sample Credentials for Testing

| Username | Password    | Role   |
|----------|-------------|--------|
| admin1   | adminpass   | admin  |
| user1    | userpass    | user   |

---

## 🔗 Postman Collection

You can test all APIs using this shared Postman collection:

👉 [Open Postman Collection](https://postman.co/workspace/My-Workspace~106f52d6-bd4c-447f-8938-9158c6ff44f8/collection/34829578-b0b84f40-d43b-48c1-99a6-4682a3e2ae55?action=share&creator=34829578)

> Make sure to set the `Authorization` header with your JWT token for protected routes.

---

## 📬 Submission

This project was created as part of the XTechOn Backend Developer Assignment due by **30-May-2025**.

---

## 🧠 Author

**Pawan Kumar**  
📧 kr.pawanverma.contact@gmail.com  
🔗 [GitHub Profile](https://github.com/Pawanverma9660)
