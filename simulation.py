# simulation.py

# simulation.py
import random
from data import cases, AGENTS, AVG_HANDLING_TIME, SLA_HOURS


def simulate_once(cases):
    total_work = 0
    for case in cases:
        noise = random.uniform(0.9, 1.1)
        total_work += case["complexity"] * noise
    return total_work


def monte_carlo(cases, agents, runs=10000):
    capacity_per_agent = (SLA_HOURS * 60) / AVG_HANDLING_TIME
    total_capacity = agents * capacity_per_agent

    breaches = 0
    for _ in range(runs):
        work = simulate_once(cases)
        if work > total_capacity:
            breaches += 1

    return breaches / runs


if __name__ == "__main__":
    risk = monte_carlo(cases, AGENTS)
    print(f"SLA Breach Risk: {risk * 100:.2f}%")
