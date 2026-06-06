from fastapi import FastAPI
from routers.users import router as users_router
from routers.products import router as products_router

app = FastAPI(title="E-Commerce API")

app.include_router(users_router)
app.include_router(products_router)

@app.get("/")
def root():
    return {"message": "Welcome to the E-Commerce API"}