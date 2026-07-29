from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/hello")
def say_hello():
    return {"msg": "hi"}

@app.get("/health")
def health_func():
    return {"status": "ok"}