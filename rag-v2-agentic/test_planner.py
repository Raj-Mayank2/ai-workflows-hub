from agent.planner import plan

questions = [
    "What are the limitations and how can they be mitigated?",
    "Compare supervised and unsupervised learning",
    "What is the main topic of this document?"
]

for q in questions:
    print("\nQUESTION:", q)
    print("PLAN:", plan(q))
