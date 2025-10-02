from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.order import Order
from app.models.furniture import Furniture
from app.schemas.order import OrderCreate
from app.service.email_service import send_email


class OrderCrud:
    @staticmethod
    async def get_order(email:str,db:AsyncSession):
        try:
            res = await db.execute(select(Order).where(Order.email==email))
            return res

        except Exception as e:
            raise e

    @staticmethod
    async def create_order(data:OrderCreate,db:AsyncSession):
        prices = await db.execute(select(Furniture).where(Furniture.id.in_(data.furniture_ids)))
        furniture_prices = prices.scalars().all()

        total_price = sum(item.price for item in furniture_prices)

        order=Order(
            email=data.email,
            list_goods=data.furniture_ids,
            over_all_price=total_price
        )
        try:
            db.add(order)
            await db.commit()
            await db.refresh(order)
        except Exception as e:
            raise e
        res = await db.execute(select(Order).where(Order.email == data.email))
        order_info = res.scalar()
        # Create a formatted message string
        message = f"""Order Confirmation

        Dear Customer,

        Thank you for your order!

        Order Details:
        --------------
        Email: {order_info.email}
        Items: {order_info.list_goods}
        Total Price: ${order_info.over_all_price}
        Order ID: {order_info.id}

        Thank you for your purchase!

        Best regards,
        Your Store"""

        await send_email(data.email, subject="Order Confirmation", body=message)


order_crud = OrderCrud()