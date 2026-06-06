from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

# Mock data
BOOKS = [
    {"id": 1, "title": "The Great Gatsby", "author_id": 1},
    {"id": 2, "title": "1984", "author_id": 2}
]

@router.get("/")
def get_books():
    return BOOKS

@router.get("/{book_id}")
def get_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
