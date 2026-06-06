from fastapi import FastAPI
from routers.tasks import router as tasks_router
from routers.categories import router as categories_router

app = FastAPI(title="Task Manager API")

app.include_router(tasks_router)
app.include_router(categories_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API"}
