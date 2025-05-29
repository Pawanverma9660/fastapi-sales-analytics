# Sales Analytics Backend - XTechOn Assignment

# FastAPI Sales Analytics Backend

This is a backend system built with FastAPI that supports:

- User registration/login (JWT + role-based access)
- Admin CSV sales data upload
- Analytics APIs: summary, top customers, date filters
- String compression utility

## 🔧 Setup

```bash
python -m venv venv
source venv\Scripts\activate  # or  venv/bin/activate   
pip install -r requirements.txt
uvicorn app.main:app --reload
