from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# Mock data
TASKS = [
    {"id": 1, "title": "Complete Homework", "completed": False},
    {"id": 2, "title": "Buy Groceries", "completed": True}
]

@router.get("/")
def get_tasks():
    return TASKS

@router.get("/{task_id}")
def get_task(task_id: int):
    for task in TASKS:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
