from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def signU():
    return {"page": 'Product'}

@router.get('/list')
def product_app(pk: int):
    return {"products": ['olma', 'anor', 'gilos']}
