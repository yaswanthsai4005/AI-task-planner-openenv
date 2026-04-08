# 🚀 AI Task Planner OpenEnv

Agentic AI Task Planning Environment built with OpenEnv — evaluates decision-making by scoring task execution plans using dynamic priorities and reward logic.

---

## 🧠 Overview

This project simulates a real-world task planning environment where an AI agent must decide the optimal order of executing tasks.

Instead of checking task completion, the system evaluates how well the agent plans based on priority and efficiency.

---

## ⚙️ How It Works

1. **Reset**
   - Generates a set of tasks with dynamic priorities

2. **Agent Planning**
   - AI generates an execution order (plan)

3. **Evaluation**
   - System scores the plan based on:
     - Priority handling
     - Execution order

---

## 📋 Example Tasks

- email_triage
- code_review
- data_cleaning

Each task has:
- priority (1–5)

---

## 🧠 Example Output
📋 GENERATED TASKS:

email_triage (priority: 5)
code_review (priority: 3)
data_cleaning (priority: 2)

🧠 GENERATED PLAN:

email_triage
code_review
data_cleaning

📊 EVALUATION RESULT:
Reward Score: 0.87

💡 Insight: Higher priority tasks scheduled earlier → better reward

✅ DONE


---

## 🏆 Key Features

- Real-world task simulation (not a toy problem)
- Dynamic environment (randomized priorities each run)
- Meaningful reward function based on decision quality
- Agent-based planning evaluation
- Fully OpenEnv compliant

---

## 📦 Project Structure


ai_task_planner/
│── environment.py # Core environment logic
│── inference.py # Agent simulation script
│── openenv.yaml # OpenEnv configuration
│── pyproject.toml # Project config
│── uv.lock # Dependency lock
│── Dockerfile # Container setup
│── requirements.txt # Dependencies
│── server/
│ └── app.py # OpenEnv server entrypoint


---

## 🚀 How to Run

### ▶️ Run locally


python inference.py


---

### ✅ Validate OpenEnv


openenv validate


---

### 🌐 Serve Environment


uv run --project . server --port 8000


---

### 🐳 Run with Docker


openenv build
docker run -p 8000:8000 openenv-ai-task-planner


---

## 📊 Evaluation Logic

The reward system evaluates how well the agent plans tasks:

- Higher priority tasks scheduled earlier → higher score
- Poor ordering → lower reward
- Final score ranges from **0.0 to 1.0**

---

## 🎯 Use Cases

- AI decision intelligence systems
- Task scheduling optimization
- Autonomous agent benchmarking
- Workflow planning automation

---

## 🧠 Core Idea

> This project evaluates **how intelligently an AI agent plans tasks**, not just whether tasks are completed.

---

## 🔥 Future Improvements

- Add deadlines and time constraints
- Add task dependencies
- Multi-agent collaboration
- Real-world API integrations

---

## 📌 Tech Stack

- Python
- OpenEnv
- FastAPI (for serving)
- Docker

---

## 🏁 Conclusion

This project demonstrates how AI agents can be evaluated based on decision-making quality in realistic environments, making it a strong foundation for future autonomous systems.
