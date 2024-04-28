from fastapi import APIRouter, HTTPException
from models.products import Product, Order, OrderItem
from models.users import Customer
from config import products_collection
from bson import ObjectId, json_util
import json

router = APIRouter()

@router.get("/")
async def testorder():
    return {"hello":"6666"}

