from fastapi import FastAPI
from tasks.routers import router as tasks_router
from categories.routers import router as categories_router

app = FastAPI()

app.include_router(tasks_router, prefix="/tasks")
app.include_router(categories_router, prefix="/categories")

@app.get("/")
def home():
    return {"message": "Dars 1.2 Home"}
