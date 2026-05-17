from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()
todo_list = [] 
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "msg": "todo Success"
    }

@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "todo": todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="ID")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "msg": "there is no task with the ID" 
    }