from fastapi import FastAPI
from books.routers import router as books_router
from authors.routers import router as authors_router

app = FastAPI()

app.include_router(books_router, prefix="/books")
app.include_router(authors_router, prefix="/authors")

@app.get("/")
def home():
    return {"message": "Dars 1.3 Home"}
