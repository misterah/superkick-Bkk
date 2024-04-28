from fastapi import APIRouter, HTTPException
from models.products import Product
from config import products_collection
from bson import ObjectId, json_util
import json

router = APIRouter()


@router.get("/all/")
def get_all_products():
    product = products_collection().find()
    #print(product,type(product))
    return {"sneakers": json.loads(json_util.dumps(product))}

@router.post("/products/")
def create_product(product_data: Product):
    product_id = products_collection().insert_one(product_data.dict()).inserted_id
    return {"sneakers": "Product created successfully", "product_id": str(product_id)}

@router.get("/products/{sneakers_id}")
def get_product(sneakers_id: str):
    product = products_collection().find_one({"sneakers_id": sneakers_id})
    if product:
        product["_id"] = str(product["_id"])  # Convert ObjectId to string
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@router.put("/products/{sneakers_id}")
def update_product(sneakers_id: str, product_data: dict):
    result = products_collection().update_one({"sneakers_id": sneakers_id}, {"$set": product_data})
    if result.modified_count == 1:
        return {"message": "Product updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")
    
@router.get("/brand/{brand}")
def get_product_by_brand(brand: str):
    product = products_collection().find({"sneakers_brand": brand})
    return {"sneakers": json.loads(json_util.dumps(product))}


@router.get("/categories/{categories}")
def get_product_by_categories(categories: str):
    product = products_collection().find({"sneakers_categories": categories})
    return {"sneakers": json.loads(json_util.dumps(product))}