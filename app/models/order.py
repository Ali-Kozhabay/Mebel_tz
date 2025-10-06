from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    list_goods: Mapped[list] = mapped_column(
        ARRAY(Integer),
        nullable=False,
    )
    over_all_price: Mapped[float] = mapped_column(default=0)
