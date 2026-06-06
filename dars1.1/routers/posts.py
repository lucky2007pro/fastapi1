from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

# Mock data
POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post content."},
    {"id": 2, "title": "Second Post", "content": "This is the second post content."}
]

@router.get("/")
def get_posts():
    return POSTS

@router.get("/{post_id}")
def get_post(post_id: int):
    for post in POSTS:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")
