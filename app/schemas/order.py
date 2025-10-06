from pydantic import BaseModel


class OrderCreate(BaseModel):
    email: str
    furniture_ids: list[int]
