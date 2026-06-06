from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def books_home():
    return {"page": "Books Home"}

@router.get('/list')
def books_list():
    return {"books": ["The Hobbit", "The Lord of the Rings"]}
