from fastapi import APIRouter, HTTPException, Depends
from app.models import UserCreate, UserLogin
from app.database import get_db
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import sqlite3

router = APIRouter()
SECRET_KEY = "secret"
ALGORITHM = "HS256"
bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/register")
def register(user: UserCreate):
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (user.username, bcrypt.hash(user.password), user.role),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"msg": "Registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    conn = get_db()
    cur = conn.execute("SELECT * FROM users WHERE username=?", (user.username,))
    db_user = cur.fetchone()
    if db_user and bcrypt.verify(user.password, db_user["password"]):
        token = create_access_token({"sub": db_user["username"], "role": db_user["role"]})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/profile")
def profile(current=Depends(get_current_user)):
    return {"username": current["sub"], "role": current["role"]}
