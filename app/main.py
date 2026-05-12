from fastapi import FastAPI, Depends
from app.routes import products
from . import database, models

# Create FastAPI application instance
app = FastAPI(title="Inventory Management System", version="1.0.0")

# Include the products router
app.include_router(products.router)

# Create all database tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Inventory Management System!"}