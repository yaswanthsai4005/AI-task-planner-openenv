import requests
import time

BASE_URL = "http://localhost:8000"

def main():
    # Wait for server to be ready
    for i in range(10):
        try:
            r = requests.post(f"{BASE_URL}/reset")
            r.raise_for_status()
            data = r.json()
            break
        except:
            time.sleep(2)

    tasks = data["observation"]["tasks"]
    print(f"[Agent] Tasks: {tasks}")

    # Sort by priority descending (optimal strategy)
    sorted_tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
    plan = [t["id"] for t in sorted_tasks]
    print(f"[Agent] Plan: {plan}")

    # Execute plan
    result = requests.post(f"{BASE_URL}/step", json={"plan": plan})
    result.raise_for_status()
    output = result.json()

    print(f"[Agent] Reward: {output['reward']}")
    print(f"[Agent] Done: {output['done']}")

if __name__ == "__main__":
    main()
