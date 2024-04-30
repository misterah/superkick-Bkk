from pydantic import BaseModel
from typing import List
import datetime

class Product(BaseModel):
    sneakers_id: str
    sneakers_name: str
    sneakers_brand : str
    sneakers_price: int
    sneakers_categories: str
    sneakers_detail: str
    image_url: list
    sneakers_sizes: list

class ShippingAddress(BaseModel):
    username: str
    name: str
    email: str
    postcode: str
    tel: str
    address: str

class Transaction(BaseModel):
    order_id: str
    products: list
    total_price: int
    detail: ShippingAddress
    complete: bool




