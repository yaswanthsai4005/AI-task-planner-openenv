import random
from openenv_core import Environment

class TaskEnv(Environment):

    def reset(self):
        # dynamic tasks (IMPORTANT for agentic behavior)
        self.tasks = [
            {"id": "email_triage", "priority": random.randint(1,5)},
            {"id": "code_review", "priority": random.randint(1,5)},
            {"id": "data_cleaning", "priority": random.randint(1,5)}
]

        return {
            "observation": {"tasks": self.tasks},
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    def step(self, action):
        plan = action.get("plan", [])

        score = 0
        total = len(self.tasks)

        for i, t in enumerate(plan):
            for task in self.tasks:
                if task["id"] == t:
                    score += (task["priority"] * (total - i))

        reward = min(score / (total * 5 * total), 1.0)

        return {
            "observation": {"tasks": self.tasks},
            "reward": reward,
            "done": True,
            "info": {"message": "Evaluation complete"}
        }

    def state(self):
        return {"tasks": self.tasks}

