import requests
import time
import sys

BASE_URL = "http://localhost:8000"

def main():
    data = None
    
    # Wait for server to be ready
    for i in range(15):
        try:
            r = requests.post(f"{BASE_URL}/reset", timeout=5)
            r.raise_for_status()
            data = r.json()
            print(f"[Agent] Connected on attempt {i+1}")
            break
        except Exception as e:
            print(f"[Agent] Attempt {i+1} failed: {e}")
            time.sleep(3)

    if data is None:
        print("[Agent] ERROR: Could not connect to server after 15 attempts")
        sys.exit(1)

    tasks = data["observation"]["tasks"]
    print(f"[Agent] Tasks: {tasks}")

    # Sort by priority descending (optimal strategy)
    sorted_tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
    plan = [t["id"] for t in sorted_tasks]
    print(f"[Agent] Plan: {plan}")

    # Execute plan
    result = requests.post(f"{BASE_URL}/step", json={"plan": plan}, timeout=5)
    result.raise_for_status()
    output = result.json()

    print(f"[Agent] Reward: {output['reward']}")
    print(f"[Agent] Done: {output['done']}")

if __name__ == "__main__":
    main()
