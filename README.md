# Proactive SLA Risk Prediction using Process Simulation

## Problem
Operational teams detect SLA breaches only after they occur, leading to reactive firefighting and operational stress.

## Solution
This project uses probabilistic process simulation to predict the risk of SLA breaches before they happen, using current workload and workforce conditions.

## Key Features
- Monte Carlo based process simulation
- SLA breach risk prediction
- What-if scenario analysis for staffing decisions

## How It Works
1. Takes a snapshot of current work-in-progress
2. Simulates variability in case complexity and processing speed
3. Runs thousands of future simulations
4. Calculates probability of SLA breach

## How to Run
```bash
python simulation.py
python what_if.py