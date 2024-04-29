from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    name: str
    email: str
    postcode: str
    tel: str
    address: str

class ProductsOrder(BaseModel):
    sneakers_id: str
    size: str
    quantity: int

class OrderData(BaseModel):
    username: str
    shipping_info: Address
    products_order: List[ProductsOrder]
