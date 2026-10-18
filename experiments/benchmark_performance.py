"""
High-resolution in-process benchmarking for partition algorithms.
Measures execution times using QueryPerformanceCounter (time.perf_counter_ns)
over multiple iterations preceded by at least 5 discarded warmup runs.
Zero precomputed lookup tables; strictly executing unadulterated workloads.
"""

import os
import statistics
import sys
import time

from src.discriminant import compute_Dk
from src.partition import compute_partitions_euler, compute_pk_recurrence, compute_pk_pentagonal_inversion
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



def benchmark_function(name: str, fn, iterations: int = 15, warmup_runs: int = 5):
    """Executes fn() with warmup and high-resolution timing."""
    print(f"--- Benchmarking: {name} ---")
    print(f"Executing {warmup_runs} discarded warmup runs...")
    for _ in range(warmup_runs):
        _ = fn()

    timings_ms = []
    print(f"Executing {iterations} timed iterations...")
    for i in range(iterations):
        t0 = time.perf_counter_ns()
        res = fn()
        t1 = time.perf_counter_ns()
        elapsed_ms = (t1 - t0) / 1_000_000.0
        timings_ms.append(elapsed_ms)

    mean_t = statistics.mean(timings_ms)
    median_t = statistics.median(timings_ms)
    min_t = min(timings_ms)
    max_t = max(timings_ms)
    stdev_t = statistics.stdev(timings_ms) if len(timings_ms) > 1 else 0.0

    print(f"Iterations: {iterations}")
    print(f"Mean:   {mean_t:.4f} ms")
    print(f"Median: {median_t:.4f} ms")
    print(f"Min:    {min_t:.4f} ms")
    print(f"Max:    {max_t:.4f} ms")
    print(f"Stdev:  {stdev_t:.4f} ms\n")

    return {
        "name": name,
        "iterations": iterations,
        "mean_ms": mean_t,
        "median_ms": median_t,
        "min_ms": min_t,
        "max_ms": max_t,
        "stdev_ms": stdev_t,
    }


def run_benchmarks():
    """Worker function for benchmarks.
    
    """
    print("=== HIGH-RESOLUTION IN-PROCESS BENCHMARKS ===\n")

    # 1. Classical partition function p(n) up to n = 500
    benchmark_function(
        "Euler Pentagonal Partition p(n) [n=500]",
        lambda: compute_partitions_euler(500),
        iterations=20,
        warmup_runs=5,
    )

    # 2. k-regular partitions via divisor recurrence p_30(n) up to n = 300
    benchmark_function(
        "k-Regular Divisor Recurrence p_30(n) [n=300]",
        lambda: compute_pk_recurrence(300, 30),
        iterations=20,
        warmup_runs=5,
    )

    # 3. k-regular partitions via pentagonal inversion p_30(n) up to n = 300
    p_pre = compute_partitions_euler(300)
    benchmark_function(
        "k-Regular Pentagonal Inversion p_30(n) [n=300]",
        lambda: compute_pk_pentagonal_inversion(300, 30, p_pre),
        iterations=20,
        warmup_runs=5,
    )

    # 4. Discriminant calculation D_30(n) up to n = 300
    pk_30 = compute_pk_recurrence(302, 30)
    benchmark_function(
        "Log-Concavity Discriminant D_30(n) [n=300]",
        lambda: compute_Dk(pk_30),
        iterations=20,
        warmup_runs=5,
    )


if __name__ == "__main__":
    run_benchmarks()
