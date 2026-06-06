from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

# Mock data
CATEGORIES = [
    {"id": 1, "name": "Work"},
    {"id": 2, "name": "Personal"}
]

@router.get("/")
def get_categories():
    return CATEGORIES

@router.get("/{category_id}")
def get_category(category_id: int):
    for category in CATEGORIES:
        if category["id"] == category_id:
            return category
    raise HTTPException(status_code=404, detail="Category not found")
