from fastapi import FastAPI
from app.routes import products

app = FastAPI(title="Inventory Management System", version="1.0.0")

app.include_router(products.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Inventory Management System!"}