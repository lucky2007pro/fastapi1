from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def comments_home():
    return {"page": "Comments Home"}

@router.get('/list')
def comments_list():
    return {"comments": ["Nice post!", "I learned a lot, thanks"]}
