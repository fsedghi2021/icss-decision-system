# Integrative Cognitive Selection System (ICSS)

This repository contains the simulation code, data, and figures associated with the paper:

> **"The Integrative Cognitive Selection System (ICSS): A Multi-Objective Model of Decision-Making Under Internal Conflict"**  
> Farbod Sedghi (2026)

---

## 🧠 Overview

The **Integrative Cognitive Selection System (ICSS)** is a computational framework that models decision-making as a **multi-objective optimization process under internal conflict**.

Unlike traditional models that assume a unified utility function, ICSS represents behavior as the outcome of **competition among multiple cognitive subsystems**, each producing its own valuation of available actions.

The core decision rule is:

```
S(i,t) = Σ w_k(t) · V_k(i,t) − λ(t) · C(i,t)
```

Where:

- `V_k(i,t)` = value assigned by cognitive layer *k*  
- `w_k(t)` = dynamic dominance weight  
- `C(i,t)` = cross-layer conflict  
- `λ(t)` = conflict sensitivity parameter  

---

## 🎯 Key Features Demonstrated

This repository provides a simple simulation illustrating:

- ✅ Dynamic dominance across cognitive layers  
- ✅ Context-dependent decision reversal  
- ✅ Internal conflict as a measurable cost  
- ✅ **Lifestyle Coherence (LC)** as a system-level metric  
- ✅ Non-stationary behavior under stable valuations  
- ✅ Confidence bands representing uncertainty (illustrative)

---

## 📊 Simulation Output

The simulation produces:

- **Panel A:** Evolution of dominance weights over time  
- **Panel B:** Lifestyle Coherence (LC) trajectory  
- **Confidence bands:** Represent hypothetical variability  

📌 These outputs correspond directly to **Figure 3 in the paper**.

---

## 📂 Repository Structure

```
icss-decision-system/
├── README.md
├── simulation.py
├── icss_data.csv
├── figures/
│   ├── icss_two_panel_confidence.png
│   ├── icss_two_panel_confidence.pdf
└── requirements.txt
```

---

## ⚙️ Installation

Install dependencies using:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Simulation

Run the following command:

```
python simulation.py
```

This will:

- Generate simulation data (`icss_data.csv`)
- Produce figures in the `figures/` directory
- Display plots

---

## 📁 Output Files

| File | Description |
|------|------------|
| `icss_data.csv` | Simulation dataset (weights + LC) |
| `icss_two_panel_confidence.png` | Main figure (paper-ready) |
| `icss_two_panel_confidence.pdf` | Vector version for publication |

---

## ⚠️ Notes on Data and Simulation

- This simulation is **illustrative**, not empirically calibrated  
- Confidence bands are **hypothetical**, not statistical estimates  
- The goal is to demonstrate the **behavioral dynamics of the ICSS framework**

---

## 📖 Reproducibility

All results presented in the simulation section of the paper can be reproduced using:

```
python simulation.py
```

No external datasets are required.

---

## 📌 Citation

If you use this repository or build upon this work, please cite:

```
Sedghi, F. (2026).
The Integrative Cognitive Selection System (ICSS): A Multi-Objective Model of Decision-Making Under Internal Conflict.
```

---

## 🔗 Paper Link

(TODO)

---

## 🚀 Future Work

This repository provides a minimal implementation. Potential extensions include:

- Stochastic simulation (randomized weight dynamics)  
- Parameter estimation from behavioral data  
- Multi-agent interaction models  
- Integration with reinforcement learning frameworks  

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this code with proper attribution.

---

## 🤝 Contact

**Farbod Sedghi**

---

## ⭐ Acknowledgment

This repository is part of ongoing work on computational models of decision-making, aiming to bridge **behavioral science, cognitive systems, and engineering frameworks**.
