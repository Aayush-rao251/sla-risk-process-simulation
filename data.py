# data.py

cases = [
    {"id": i, "complexity": 1.0 + (i % 3) * 0.2}
    for i in range(120)
]

AGENTS = 5
AVG_HANDLING_TIME = 30  # minutes per case
SLA_HOURS = 6
