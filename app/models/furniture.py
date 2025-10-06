from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum

from app.core.database import Base
from app.schemas.furniture import FurnitureCategory


class Furniture(Base):
    __tablename__ = "furnitures"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column()
    category: Mapped[FurnitureCategory] = mapped_column(
        Enum(FurnitureCategory), default=FurnitureCategory.SEATING
    )
