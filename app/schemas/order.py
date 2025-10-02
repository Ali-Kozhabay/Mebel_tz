from pydantic import BaseModel, EmailStr


class OrderCreate(BaseModel):

    email:str
    furniture_ids:list[int]
