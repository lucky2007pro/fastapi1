from fastapi import FastAPI
from routers.books import router as books_router
from routers.authors import router as authors_router

app = FastAPI(title="Book Library API")

app.include_router(books_router)
app.include_router(authors_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Book Library API"}
