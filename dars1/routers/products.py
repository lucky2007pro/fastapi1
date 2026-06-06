from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# Mock data
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99}
]

@router.get("/")
def get_products():
    return PRODUCTS

@router.get("/{product_id}")
def get_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
