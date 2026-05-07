from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def get_products():
    return {"message": "List of products"}

@router.get("/{product_id}")
def get_product(product_id: int):
    return {"message": f"Details of product {product_id}"}

@router.post("/")
def create_product():
    return {"message": "Product created"}