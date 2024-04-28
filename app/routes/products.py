from fastapi import APIRouter
from models.products import Product
from config import products_collection
from bson import ObjectId, json_util
import json

router = APIRouter()



@router.get("/")
async def create_course_endpoint():
    return {"hello":"555"}

@router.get("/all/")
def get_all_products():
    product = products_collection.find()
    #print(product,type(product))
    return {"sneaker": json.loads(json_util.dumps(product))}

@router.post("/products/")
def create_product(product_data: Product):
    product_id = products_collection.insert_one(product_data.dict()).inserted_id
    return {"sneaker": "Product created successfully", "product_id": str(product_id)}