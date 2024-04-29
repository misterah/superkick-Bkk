
from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from bson import ObjectId, json_util
import json

from models.users import Customer, RegisterRequest, LoginRequest
from config import users_collection, SECRET_KEY

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#create JWT token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

@router.post("/register/")
def register_user(register_request: RegisterRequest):
    hashed_password = pwd_context.hash(register_request.password)
    new_user = Customer(username=register_request.username, email=register_request.email, hashed_password=hashed_password)
    users_collection().insert_one(new_user.dict())
    return {"message": "User registered successfully"}

@router.post("/login/")
def login_user(login_request: LoginRequest):
    # user = users_collection().find_one({"username": login_request.username})
    user = users_collection().find_one({
    "$or": [
        {"username": login_request.username},
        {"email": login_request.username}
    ]
})
    if user and pwd_context.verify(login_request.password, user["hashed_password"]):
        # Create JWT token with user's username and expiration time
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

#users ทั้งหมด
@router.get("/all/")
def get_all_users():
    users = users_collection().find()
    #print(product,type(product))
    return {"users": json.loads(json_util.dumps(users))}
#สร้าง user
@router.post("/users/")
def create_user(user_data: Customer):
    user_id = users_collection().insert_one(user_data.dict()).inserted_id
    return {"users": "User created successfully", "user_id": str(user_id)}
#เรียก user
@router.get("/users/{users_id}")
def get_user(users_id: str):
    user = users_collection().find_one({"_id": ObjectId(users_id)})
    if user:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
#edit user
@router.put("/users/{users_id}")
def update_user(users_id: str, users_data: dict):
    result = users_collection().update_one({"_id": ObjectId(users_id)}, {"$set": users_data})
    if result.modified_count == 1:
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
#delete user
@router.delete("/users/{users_id}")
def delete_user(users_id: str):
    result = users_collection().delete_one({"_id": ObjectId(users_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    

