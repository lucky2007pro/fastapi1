from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Mock data
USERS = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

@router.get("/")
def get_users():
    return USERS

@router.get("/{user_id}")
def get_user(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
