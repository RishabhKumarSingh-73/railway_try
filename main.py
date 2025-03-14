import json
import os
from fastapi import FastAPI
import uvicorn

from llm_calls.memory_recall_assessment import memory_assessment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Railway!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

#assessment
@app.get("/memory")
async def get_memory_recall_assessment_questions():
    questions_str = await memory_assessment()
    data = json.loads(questions_str)
    return data

#roadmap


#mindmap


#vedio



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set
    uvicorn.run(app, host="0.0.0.0", port=port)