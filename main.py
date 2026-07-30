from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Task(BaseModel):
    title: str

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Walk the dog", "done": True},
    {"id": 3, "title": "Finish assignment", "done": False}
]

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/hello")
def say_hello():
    return {"msg": "hi"}

@app.get("/health")
def health_func():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")



@app.post("/tasks", status_code=201)
def create_task(new_task: Task):
    next_id = len(tasks) + 1
    task = {"id": next_id, "title": new_task.title, "done": False}
    tasks.append(task)
    return task

    