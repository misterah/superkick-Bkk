from pydantic import BaseModel,validator
from typing import Optional
from config import users_collection

class Customer(BaseModel):
    username: str
    email : str
    hashed_password : str

    @validator('username')
    def check_username_unique(cls, v):
        # Check if username already exists in the collection
        if users_collection.find_one({'username': v}):
            raise ValueError('Username already exists')
        return v

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str