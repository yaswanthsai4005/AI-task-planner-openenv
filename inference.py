from environment import TaskEnv

def main():
    env = TaskEnv()

    print("\n🚀 AI TASK PLANNER STARTED\n")

    result = env.reset()

    tasks = result["observation"]["tasks"]

    print("📋 GENERATED TASKS:")
    for t in tasks:
        print(f"- {t['id']} (priority: {t['priority']})")

    # simple agent logic (sort by priority)
    plan = sorted(tasks, key=lambda x: -x["priority"])
    plan_ids = [t["id"] for t in plan]

    print("\n🧠 GENERATED PLAN:")
    for i, t in enumerate(plan_ids):
        print(f"{i+1}. {t}")

    result = env.step({"plan": plan_ids})

    print("\n📊 EVALUATION RESULT:")
    print(f"Reward Score: {result['reward']:.2f}")

    print("\n💡 Insight: Higher priority tasks scheduled earlier → better reward")

    print("\n✅ DONE\n")

if __name__ == "__main__":
    main()