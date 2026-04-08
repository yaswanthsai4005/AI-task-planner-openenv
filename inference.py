from environment import TaskEnv

env = TaskEnv()
print("START")
result = env.reset()
tasks = result["observation"]["tasks"]
print("TASKS:", tasks)

plan = sorted(tasks, key=lambda x: -x["priority"])
plan_ids = [t["id"] for t in plan]
print("PLAN:", plan_ids)

result = env.step({"plan": plan_ids})
print("REWARD:", round(result["reward"], 2))
print("END")
