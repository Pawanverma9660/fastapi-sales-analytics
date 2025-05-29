from fastapi import APIRouter, File, UploadFile, Depends, HTTPException, Query
from app.auth import get_current_user
from app.database import get_db
import pandas as pd
from io import StringIO

router = APIRouter()

@router.post("/upload-sales")
def upload_sales(file: UploadFile = File(...), current=Depends(get_current_user)):
    if current["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin allowed")
    content = file.file.read().decode()
    df = pd.read_csv(StringIO(content))

    conn = get_db()
    for _, row in df.iterrows():
        conn.execute(
            "INSERT INTO sales (customer_name, amount, date) VALUES (?, ?, ?)",
            (row["customer_name"], row["amount"], row["date"])
        )
    conn.commit()
    return {"msg": "Sales uploaded"}

@router.get("/analytics/summary")
def summary(current=Depends(get_current_user)):
    if current["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin allowed")
    conn = get_db()
    cur = conn.execute("SELECT COUNT(*), SUM(amount), AVG(amount) FROM sales")
    count, total, avg = cur.fetchone()
    return {
        "total_sales": total or 0,
        "total_transactions": count,
        "average_order_value": avg or 0
    }

@router.get("/analytics/top-customers")
def top_customers(limit: int = 3, current=Depends(get_current_user)):
    if current["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin allowed")
    conn = get_db()
    cur = conn.execute(
        "SELECT customer_name, SUM(amount) as total FROM sales GROUP BY customer_name ORDER BY total DESC LIMIT ?",
        (limit,)
    )
    return cur.fetchall()

@router.get("/analytics/by-date")
def by_date(from_date: str, to_date: str, current=Depends(get_current_user)):
    if current["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin allowed")
    conn = get_db()
    cur = conn.execute(
        "SELECT * FROM sales WHERE date BETWEEN ? AND ?",
        (from_date, to_date)
    )
    return cur.fetchall()
