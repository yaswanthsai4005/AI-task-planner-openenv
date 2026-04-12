import requests
import time
import sys
import threading
import os
import uvicorn
from openai import OpenAI
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

    # Use their LLM proxy to decide task order
    client = OpenAI(
        api_key=os.environ.get("API_KEY", "dummy"),
        base_url=os.environ.get("API_BASE_URL", "https://api.openai.com/v1")
    )

    task_list = "\n".join([f"- {t['id']} (priority: {t['priority']})" for t in tasks])
    prompt = f"""You are a task planning agent. Given these tasks with priorities (higher = more important), return ONLY a comma-separated list of task IDs ordered from highest to lowest priority. Nothing else.

Tasks:
{task_list}

Return only the comma-separated task IDs:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )

    llm_output = response.choices[0].message.content.strip()
    print(f"[Agent] LLM output: {llm_output}", flush=True)

    # Parse LLM response, fallback to sorted by priority
    try:
        plan = [t.strip() for t in llm_output.split(",")]
        valid_ids = [t["id"] for t in tasks]
        plan = [p for p in plan if p in valid_ids]
        if len(plan) != len(tasks):
            raise ValueError("Invalid plan")
    except:
        sorted_tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
        plan = [t["id"] for t in sorted_tasks]

    print(f"[Agent] Plan: {plan}", flush=True)
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
