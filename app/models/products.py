from pydantic import BaseModel
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
    products: object
    total_price: str
    

class ShippingAddress(BaseModel):
    name: str
    email: str
    postcode: str
    tel: str
    address: str
    date_added: str
