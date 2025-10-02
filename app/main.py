import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.routes.furniture import  router as furniture_router
from app.api.routes.order import  router as order_router

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        logger.info("Creating all tables in the database")
        await conn.run_sync(Base.metadata.create_all)
        logger.info("All tables created successfully")
    yield

app = FastAPI(
    title="TZ",
    version="1.0.0",
    lifespan=lifespan,
)



app.include_router(furniture_router, prefix="/api/v1/furniture", tags=["furniture"])
app.include_router(order_router, prefix="/api/v1/order", tags=["order"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Intelligent LMS API", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
