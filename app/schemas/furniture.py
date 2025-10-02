import enum
from pydantic import BaseModel

class FurnitureCategory(str, enum.Enum):
    SEATING = "seating"
    TABLE = "table"
    BED = "bed"
    STORAGE = "storage"


class Furniture(BaseModel):
    # id: int
    name: str
    price: float
    category:FurnitureCategory = FurnitureCategory.SEATING