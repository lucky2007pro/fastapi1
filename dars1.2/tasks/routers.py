from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def tasks_home():
    return {"page": "Tasks Home"}

@router.get('/list')
def tasks_list():
    return {"tasks": ["Read book", "Write code", "Drink water"]}
