import requests
import time
import sys
import threading
import uvicorn
from server.app import app

def start_server():
    uvicorn.run(app, host="0.0.0.0", port=7860, log_level="info")

def main():
    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()
    print("[Agent] Server thread started...", flush=True)

    data = None

    for i in range(20):
        try:
            r = requests.post("http://localhost:7860/reset", timeout=5)
            r.raise_for_status()
            data = r.json()
            print(f"[Agent] Connected on attempt {i+1}", flush=True)
            break
        except Exception as e:
            print(f"[Agent] Attempt {i+1} failed, retrying...", flush=True)
            time.sleep(2)

    if data is None:
        print("[Agent] ERROR: Server never started", flush=True)
        sys.exit(1)

    tasks = data["observation"]["tasks"]
    print(f"[Agent] Tasks: {tasks}", flush=True)

    sorted_tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
    plan = [t["id"] for t in sorted_tasks]

    # Required structured output
    print(f"[START] task=ai_task_planner", flush=True)

    result = requests.post("http://localhost:7860/step", json={"plan": plan}, timeout=5)
    result.raise_for_status()
    output = result.json()

    reward = output["reward"]

    print(f"[STEP] step=1 reward={reward}", flush=True)
    print(f"[END] task=ai_task_planner score={reward} steps=1", flush=True)

    print(f"[Agent] Reward: {reward}", flush=True)
    print(f"[Agent] Done: {output['done']}", flush=True)

if __name__ == "__main__":
    main()
