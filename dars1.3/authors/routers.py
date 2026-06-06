from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def authors_home():
    return {"page": "Authors Home"}

@router.get('/list')
def authors_list():
    return {"authors": ["J.R.R. Tolkien", "George R.R. Martin"]}
