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
async def memory_assessment_endpoint():
    questions_str = await memory_assessment()
    unboxed_string = remove_boxed_formatting(questions_str)
    data = json.loads(unboxed_string)
    return data

#roadmap


#mindmap


#vedio

def remove_boxed_formatting(response: str) -> str:
    if response.startswith(r"\boxed{") and response.endswith("}"):
        return response[len(r"\boxed{"):-1]  
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set
    uvicorn.run(app, host="0.0.0.0", port=port)