# Integrative Cognitive Selection System (ICSS)

This repository contains the simulation code, data, and figures associated with the paper:

**"The Integrative Cognitive Selection System (ICSS): A Multi-Objective Model of Decision-Making Under Internal Conflict"**

## Overview

ICSS models decision-making as a multi-objective optimization process under internal conflict:

S(i,t) = Σ w_k(t) V_k(i,t) - λ C(i,t)

This repository provides a simple simulation illustrating:

- Dynamic dominance weights
- Decision reversal under changing conditions
- Lifestyle Coherence (LC) dynamics
- Confidence intervals (illustrative)

---

## Files

- `simulation.py`: Reproduces the main simulation and figures  
- `icss_data.csv`: Generated data (weights and LC values)  
- `figures/`: Contains output figures used in the paper  

---

## Reproducing Results

1. Install dependencies:

``
