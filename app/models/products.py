from pydantic import BaseModel
from typing import Optional
import datetime

class Product(BaseModel):
    sneakers_id: str
    sneakers_name: str
    sneakers_brand : str
    sneakers_price: str
    sneakers_categories: str
    sneakers_detail: str
    image_url: str
    sneakers_sizes: list

class Order(BaseModel):
    order_id:str
    customer_id:str
    date_ordered: str
    complete: bool
    transaction_id: str

class OrderItem(BaseModel):
    sneakers_id:str
    order_id:str
    date_added: str
    quantity: str

class ShippingAddress(BaseModel):
    customer_id:str
    order_id:str
    name: str
    email: str
    postcode: str
    tel: str
    address: str
    date_added: str
