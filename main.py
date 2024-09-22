from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Note(BaseModel):
    name: str
    description: Union[str, None]
    completed: bool = False
    date : str

app = FastAPI()

@app.get("/")
def read_root() -> Union[str, dict]:
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None) -> dict:
    return {"item_id": item_id, "q": q}

# create notes api crud
todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    return todos[todo_id]

@app.post("/addTodo")
def add_todo(todo: dict):
    todos.append(todo)
    return todos

@app.put("/updateTodo/{todo_id}")
def update_todo(todo_id: int, todo: dict):
    todos[todo_id] = todo
    return todos

@app.delete("/deleteTodo/{todo_id}")
def delete_todo(todo_id: int):
    todos.pop(todo_id)
    return todos
