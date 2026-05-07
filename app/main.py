from fastapi import FastAPI, Depends
from app.routes import products
from . import database, models

app = FastAPI(title="Inventory Management System", version="1.0.0")

app.include_router(products.router)

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Inventory Management System!"}