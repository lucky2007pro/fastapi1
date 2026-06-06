from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def categories_home():
    return {"page": "Categories Home"}

@router.get('/list')
def categories_list():
    return {"categories": ["Work", "Personal", "Health"]}
