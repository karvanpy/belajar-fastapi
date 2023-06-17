import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/jobs")
def get_jobs():
    with open("jobs.json") as f:
        jobs = json.load(f)
    return jobs

if __name__ == "__main__":
    uvicorn.run(app, port=8000)