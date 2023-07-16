from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    first_name: str = Field(..., max_length=20)
    last_name: str = Field(..., max_length=20)
    email: EmailStr = Field(..., max_length=30) 
    password: str = Field(..., max_length=150)

    class Config:
        from_attributes = True

class User(UserIn):
    id: int 

    class Config:
        from_attributes = True
    