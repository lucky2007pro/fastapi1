from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def posts_home():
    return {"page": "Posts Home"}

@router.get('/list')
def posts_list():
    return {"posts": ["New Tech in 2026", "FastAPI vs Django"]}
