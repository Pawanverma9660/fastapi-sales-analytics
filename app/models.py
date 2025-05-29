from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str  # "admin" or "user"

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class SalesUpload(BaseModel):
    customer_name: str
    amount: float
    date: str

class CompressRequest(BaseModel):
    text: str
