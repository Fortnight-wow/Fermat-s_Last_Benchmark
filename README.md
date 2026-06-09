# Fermat's Last Benchmark

> A research-oriented benchmark for evaluating mathematical reasoning systems on difficult and historically significant problems.

---

## What is this?

Fermat's Last Benchmark (FLB) is an open-source project designed to evaluate how effectively AI systems and reasoning engines solve advanced mathematical problems.

Unlike standard benchmarks focused on school-level questions, FLB emphasizes:

- Deep mathematical reasoning
- Proof-oriented thinking
- Research-inspired challenges
- Automated verification
- Reproducible evaluation

---

## Quick Start

```bash
git clone https://github.com/Fortnight-wow/Fermat-s_Last_Benchmark.git
cd Fermat-s_Last_Benchmark
pip install -r requirements.txt
pytest
```

For complete instructions see:

➡️ **[HOW_TO_USE.md](HOW_TO_USE.md)**

---

## Current Domains

| Domain | Status |
|----------|----------|
| Number Theory | Active |
| Algebra | Active |
| Graph Theory | Active |
| Combinatorics | Planned |
| Optimization | Planned |
| Computational Complexity | Active |

---

## Features

- Mathematical datasets
- SymPy-based verification tools
- Automated testing with PyTest
- GitHub Actions CI
- Benchmark execution scripts
- Leaderboard infrastructure
- Research challenge collections

---

## Repository Structure

```text
Fermat-s_Last_Benchmark/
│
├── benchmark/
├── datasets/
├── verification/
├── scripts/
├── tests/
├── leaderboard/
├── research_sets/
├── HOW_TO_USE.md
├── CONTRIBUTING.md
├── requirements.txt
└── README.md
```

---

## Benchmark Workflow

```text
Problem Selection
        ↓
Model Generates Solution
        ↓
Automatic Verification
        ↓
Score Calculation
        ↓
Leaderboard Entry
```

---

## Current Components

### Verification

- verify_number_theory.py
- verify_algebra.py
- verify_graph_theory.py

### Testing

- test_verify_number_theory.py
- test_verify_algebra.py

### Research Collections

- Millennium Problems
- Recently Solved Problems

---

## Roadmap

### Phase 1

- Core benchmark infrastructure
- Verification utilities
- CI/CD pipeline

### Phase 2

- Larger datasets
- Difficulty calibration
- Model comparison reports

### Phase 3

- Lean integration
- Coq integration
- Public benchmark leaderboard

---

## Contributing

Interested in contributing new problems, verification systems, or benchmark ideas?

See **[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

## License

MIT License
