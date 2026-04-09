from fastapi import FastAPI
import uvicorn
from environment import TaskEnv

app = FastAPI()
env = TaskEnv()

@app.get("/")
def read_root():
    return {"status": "AI Task Planner is running!"}

@app.post("/reset")
def reset_env():
    result = env.reset()
    return result

@app.post("/step")
def take_step(plan: dict):
    result = env.step(plan)
    return result

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
