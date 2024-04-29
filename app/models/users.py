from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    username: str
    email : str
    hashed_password : str

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str