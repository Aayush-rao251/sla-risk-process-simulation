# what_if.py

from simulation import monte_carlo
from data import cases, AGENTS

print("What-If Analysis:\n")

for extra_agents in [0, 2, 3]:
    total_agents = AGENTS + extra_agents
    risk = monte_carlo(cases, total_agents)
    print(f"Agents: {total_agents} → SLA Risk: {risk * 100:.2f}%")
