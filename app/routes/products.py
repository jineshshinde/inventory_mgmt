from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, database

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def get_products(db: Session = Depends(database.get_db)):
    return crud.get_products(db)

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(database.get_db)):
    return crud.get_product(db, product_id)

@router.post("/")
def create_product(name: str, description: str, price: float, db: Session = Depends(database.get_db)):
    return crud.create_product(db, name, description, price)