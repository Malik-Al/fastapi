from fastapi import FastAPI
from app.database import Base, engine
from app.routers.item_router import router as item_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD Example")

app.include_router(item_router)