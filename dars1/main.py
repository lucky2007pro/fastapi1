from fastapi import FastAPI
from users.routers import router as users_router
from products.routers import router as products_router

app = FastAPI()

app.include_router(users_router, prefix="/users")
app.include_router(products_router, prefix="/products")

@app.get("/")
def home():
    return {"message": "Dars 1 Home"}