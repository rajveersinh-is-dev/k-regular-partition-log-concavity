# Reproducibility Guide

This repository contains fully reproducible code, formal proofs, and mathematical results.
Every benchmark, test, and algorithm runs from first principles with zero preloaded numbers or lookup tables.

---

## 1. Environment and Requirements

- **Python:** 3.10+ (tested on Python 3.14.6)
  - Standard library only for core algorithms (`unittest`, `time`, `statistics`, `typing`, `math`).
  - Optional: `numpy` (2.4+), `scipy` (1.18+), `sympy` (1.14+).
- **Lean 4:** Version 4.35.0 or compatible Lean 4 toolchain.
- **Git:** 2.40+.

---

## 2. Reproducing Formal Lean 4 Proofs

To verify the formal proofs in Lean 4:

```bash
lean formal/LogConcavity.lean
```

**Expected Output:**
Exit code `0` with zero output on stdout and stderr, indicating that all theorems compiled and type-checked with **zero `sorry`** and **zero unproven `axiom` declarations**.

To verify the absence of `sorry` or `axiom`:
```bash
grep "sorry" formal/LogConcavity.lean
grep "axiom" formal/LogConcavity.lean
```
Both commands return no matches.

---

## 3. Running the Automated Test Suite

To run the unit test suite:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**Expected Output:**
```text
test_central_boundary_formula ... ok
test_classical_exception_set ... ok
test_heim_neuhauser_conjecture_verification ... ok
test_higher_order_truncation_identity ... ok
test_left_boundary_formula ... ok
test_partition_base_values ... ok
test_phase_transition_boundary_values ... ok
test_pk_dual_algorithm_equivalence ... ok
test_submodular_truncation_identities ... ok
test_transition_window_decomposition ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.007s

OK
```

---

## 4. Running In-Process Hardware Benchmarks

To run the in-process benchmarks measuring execution times using hardware performance counters (`QueryPerformanceCounter`):

```bash
python experiments/benchmark_performance.py
```

**Protocol:**
- 5 discarded warmup runs per benchmark to ensure CPU cache and branch predictor stabilization.
- 20 timed iterations measuring nanosecond-resolution intervals via `time.perf_counter_ns()`.
- Reports mean, median, min, max, and standard deviation.

---

## 5. Verifying the Exact Phase Transition

To inspect the boundary behavior around the critical point $k = 30$:

```bash
python -c "from src.phase_transition import analyze_boundary_transition; [print(f'k={r[\"k\"]}: D_k(k)={r[\"Dk_at_k\"]}') for r in analyze_boundary_transition(27, 33)]"
```

**Expected Output:**
```text
k=27: D_k(k)=-531
k=28: D_k(k)=78449
k=29: D_k(k)=-1858
k=30: D_k(k)=164444
k=31: D_k(k)=17089
k=32: D_k(k)=297540
k=33: D_k(k)=92323
```
Notice that $k = 27$ and $k = 29$ are strictly negative, while all $k \ge 30$ are strictly positive.
