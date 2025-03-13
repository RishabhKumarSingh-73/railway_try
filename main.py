import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Railway!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set
    uvicorn.run(app, host="0.0.0.0", port=port)