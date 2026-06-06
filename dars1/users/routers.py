from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def users_list():
    return {"users": ["Ali", "Vali"]}

@router.get('/info')
def user_info():
    return {"status": "Active users check"}
