from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    sneakers_id: str
    sneakers_name: str
    sneakers_brand : str
    sneakers_price: str
    sneakers_categories: str
    sneakers_detail: str
    image_url: str
    sneakers_sizes: list

