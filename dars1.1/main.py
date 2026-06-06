from fastapi import FastAPI
from routers.posts import router as posts_router
from routers.comments import router as comments_router

app = FastAPI(title="Blog API")

app.include_router(posts_router)
app.include_router(comments_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Blog API"}
