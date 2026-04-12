import requests
import time
import sys
import threading
import uvicorn
from server.app import app

def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

def main():
    # Start server in background thread
    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()
    print("[Agent] Server thread started...")

    data = None

    # Wait for server to be ready
    for i in range(20):
        try:
            r = requests.post("http://localhost:8000/reset", timeout=5)
            r.raise_for_status()
            data = r.json()
            print(f"[Agent] Connected on attempt {i+1}")
            break
        except Exception as e:
            print(f"[Agent] Attempt {i+1} failed, retrying...")
            time.sleep(2)

    if data is None:
        print("[Agent] ERROR: Server never started")
        sys.exit(1)

    tasks = data["observation"]["tasks"]
    print(f"[Agent] Tasks: {tasks}")

    # Optimal strategy: highest priority first
    sorted_tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
    plan = [t["id"] for t in sorted_tasks]
    print(f"[Agent] Plan: {plan}")

    result = requests.post("http://localhost:8000/step", json={"plan": plan}, timeout=5)
    result.raise_for_status()
    output = result.json()

    print(f"[Agent] Reward: {output['reward']}")
    print(f"[Agent] Done: {output['done']}")

if __name__ == "__main__":
    main()
