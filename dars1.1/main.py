from fastapi import FastAPI
from posts.routers import router as posts_router
from comments.routers import router as comments_router

app = FastAPI()

app.include_router(posts_router, prefix="/posts")
app.include_router(comments_router, prefix="/comments")

@app.get("/")
def home():
    return {"message": "Dars 1.1 Home"}
