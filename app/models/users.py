from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    username: str
    email : str