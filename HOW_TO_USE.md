# How to Use Fermat's Last Benchmark

## 1. Clone the Repository

```bash
git clone https://github.com/Fortnight-wow/Fermat-s_Last_Benchmark.git
cd Fermat-s_Last_Benchmark
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Verification Utilities

### Number Theory

```bash
python verification/sympy/verify_number_theory.py
```

### Algebra

```bash
python verification/sympy/verify_algebra.py
```

### Graph Theory

```bash
python verification/sympy/verify_graph_theory.py
```

## 4. Run Tests

```bash
pytest
```

## 5. Execute Benchmark Runner

```bash
python scripts/run_benchmark.py
```

## 6. Add New Problems

1. Follow benchmark/problem_schema.md
2. Create a dataset entry
3. Add a verification method if applicable
4. Add tests

## 7. Benchmark Workflow

Problem -> Model Solution -> Verification -> Score -> Leaderboard

## Repository Sections

- datasets/ : benchmark datasets
- verification/ : automated verification tools
- tests/ : unit tests
- scripts/ : benchmark execution scripts
- leaderboard/ : benchmark results
- research_sets/ : research-oriented collections
