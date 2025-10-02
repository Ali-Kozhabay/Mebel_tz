from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.furniture import Furniture

class FurnitureCrud():

    @staticmethod
    async def get_all_furniture(db : AsyncSession):
        try:
            res = await db.execute(select(Furniture))
            return res.scalars().all()
        except Exception as e:
            raise e

    @staticmethod
    async def get_furniture_by_id(db:AsyncSession,furniture_id:int):
        try:
            res = await db.execute(select(Furniture).where(Furniture.id == furniture_id))
            return res.scalars().first()
        except Exception as e:
            raise e

    @staticmethod
    async def add_furniture(db:AsyncSession,data:Furniture):
        try:
            furniture = Furniture(
                name = data.name,
                price = data.price,
                category=data.category
            )
            db.add(furniture)
            await db.commit()
            await db.refresh(furniture)

        except Exception as e:
            raise e

furniture_crud = FurnitureCrud()