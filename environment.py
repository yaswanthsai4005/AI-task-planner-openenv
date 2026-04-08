
class TaskEnv:
    def reset(self):
        return {"observation": {"tasks": [{"id": "a", "priority": 1}]}}
    def step(self, action):
        return {"reward": 1.0}
