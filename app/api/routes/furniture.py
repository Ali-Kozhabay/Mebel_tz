import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.furniture import furniture_crud
from app.core.database import get_db
from app.schemas.furniture import Furniture

router = APIRouter()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@router.get("/furnitures")
async def get_furnitures(db:AsyncSession=Depends(get_db)):
    try:
        logger.info("Fetching all furnitures")
        furniture= await furniture_crud.get_all_furniture(db=db)
        return furniture
    except Exception as e:
        raise HTTPException(status_code=404, detail="Not Found")


@router.get("/furniture/{furniture_id}")
async def get_furniture_by_id(furniture_id:int,db: AsyncSession = Depends(get_db)):
    logger.info("Fetching furniture by id")
    furniture = await furniture_crud.get_furniture_by_id(db = db,furniture_id = furniture_id)
    if furniture is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return {"furniture": furniture}

@router.post("/add_furniture")
async def add_furniture(data:Furniture=Depends(),db: AsyncSession = Depends(get_db)):
    try:
        logger.info("Adding furniture")
        await furniture_crud.add_furniture(db=db,data=data)
        return {"message": 'Furniture Added'}
    except Exception as e:
        raise e
