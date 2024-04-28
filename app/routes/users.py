from fastapi import APIRouter, HTTPException
from models.users import Customer
from config import users_collection
from bson import ObjectId, json_util
import json

router = APIRouter()


@router.get("/all/")
def get_all_users():
    users = users_collection().find()
    #print(product,type(product))
    return {"users": json.loads(json_util.dumps(users))}

@router.post("/users/")
def create_users(user_data: Customer):
    user_id = users_collection().insert_one(user_data.dict()).inserted_id
    return {"users": "User created successfully", "user_id": str(user_id)}

# @router.get("/products/{sneakers_id}")
# def get_product(sneakers_id: str):
#     product = products_collection().find_one({"sneakers_id": sneakers_id})
#     if product:
#         product["_id"] = str(product["_id"])  # Convert ObjectId to string
#         return product
#     else:
#         raise HTTPException(status_code=404, detail="Product not found")