from pydantic import BaseModel, Field
from datetime import date
from .User import User
from .Product import Product
from typing import List


class OrderIn(BaseModel):
    user_id: int = Field(default=None, foreign_key="users.id")
    product_id: int = Field(default=None, foreign_key="products.id")
    create_date: date = Field(..., format="%Y-%M-%d") 
    status: bool = Field(default=True)

    class Config:
        from_attributes = True

class Order(OrderIn):
    id: int 

    class Config:
        from_attributes = True