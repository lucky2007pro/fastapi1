from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

# Mock data
AUTHORS = [
    {"id": 1, "name": "F. Scott Fitzgerald"},
    {"id": 2, "name": "George Orwell"}
]

@router.get("/")
def get_authors():
    return AUTHORS

@router.get("/{author_id}")
def get_author(author_id: int):
    for author in AUTHORS:
        if author["id"] == author_id:
            return author
    raise HTTPException(status_code=404, detail="Author not found")
