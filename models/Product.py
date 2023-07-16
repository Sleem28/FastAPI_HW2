from pydantic import BaseModel, Field 


class ProductIn(BaseModel):
    name: str = Field(..., max_length=20)
    description: str = Field(..., max_length=500)
    price: float = Field(...,) 

    class Config:
        from_attributes = True
    

class Product(ProductIn):
    id: int 

    class Config:
        from_attributes = True