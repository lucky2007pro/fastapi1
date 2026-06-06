from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

# Mock data
COMMENTS = [
    {"id": 1, "post_id": 1, "text": "Great post!"},
    {"id": 2, "post_id": 1, "text": "Very informative, thanks."},
    {"id": 3, "post_id": 2, "text": "Awesome content!"}
]

@router.get("/")
def get_comments():
    return COMMENTS

@router.get("/{comment_id}")
def get_comment(comment_id: int):
    for comment in COMMENTS:
        if comment["id"] == comment_id:
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")
