from sqlalchemy import Column, Integer, String, Float
from .database import Base

# Product model representing the products table in the database
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)