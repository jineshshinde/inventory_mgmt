from sqlalchemy.orm import Session
from . import models

def create_product(db: Session, name: str, description: str, price: float):
    db_product = models.Product(name=name, description=description, price=price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session):
    return db.query(models.Product).all()