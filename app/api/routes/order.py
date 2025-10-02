from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from app.crud.order import order_crud
from app.core.database import get_db
from app.schemas.order import OrderCreate


router = APIRouter()

@router.post('/create_order')
async def create_order(data:OrderCreate,db:AsyncSession=Depends(get_db)):
    try:
        order = await order_crud.create_order(data=data,db=db)
        return {"message":"success"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))


@router.get('/orders')
async def get_order(email:str,db:AsyncSession=Depends(get_db)):
    try:
        order = await order_crud.get_order(email=email,db=db)
        if order is None:
            raise HTTPException(status_code=404,detail="order not found")
        return order.scalars().all()
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))

