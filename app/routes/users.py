from fastapi import APIRouter, HTTPException
from models.users import Customer
from config import users_collection
from bson import ObjectId, json_util
import json

router = APIRouter()

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
