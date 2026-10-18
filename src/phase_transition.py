"""
Analysis of the log-concavity phase-transition boundary and exception thresholds.
"""

from typing import List, Dict

from .discriminant import compute_Delta, compute_Dk, boundary_penalty_Theta
from .partition import compute_partitions_euler, compute_pk_recurrence


def find_exceptions(Dk: List[int], max_n: int = None) -> List[int]:
    """Finds all indices n >= 1 where D_k(n) < 0."""
    limit = len(Dk) if max_n is None else min(len(Dk), max_n + 1)
    exceptions = []
    for n in range(1, limit):
        if Dk[n] < 0:
            exceptions.append(n)
    return exceptions


def compute_threshold_Nk(Dk: List[int], verification_depth: int = None) -> int:
    """
    Computes the threshold N_k = min { M : for all n >= M, D_k(n) >= 0 }.
    Equivalently, 1 + max(exceptions) if exceptions exist, else 1.
    """
    limit = len(Dk) if verification_depth is None else min(len(Dk), verification_depth + 1)
    max_fail = 0
    for n in range(1, limit):
        if Dk[n] < 0:
            max_fail = max(max_fail, n)
    return max_fail + 1


def analyze_boundary_transition(min_k: int = 25, max_k: int = 35) -> List[Dict[str, int]]:
    """
    Analyzes the critical boundary n = k from min_k to max_k.
    Computes Delta(k), Theta(k), and D_k(k) = Delta(k) - Theta(k) from first principles.
    """
    p_table = compute_partitions_euler(max_k + 2)
    Delta = compute_Delta(p_table)

    results = []
    for k in range(min_k, max_k + 1):
        delta_k = Delta[k]
        theta_k = boundary_penalty_Theta(p_table, k)
        dk_k = delta_k - theta_k
        results.append({
            "k": k,
            "Delta_k": delta_k,
            "Theta_k": theta_k,
            "Dk_at_k": dk_k,
            "is_positive": dk_k > 0,
            "is_exception": dk_k < 0,
        })
    return results


def verify_heim_neuhauser_conjecture(max_k: int = 40, max_n: int = 250) -> Dict[str, any]:
    """
    Verifies the Heim-Neuhauser conjecture for all k in [30, max_k]:
    1. Computes all exceptions n >= 26 up to max_n.
    2. Verifies that no exception exists for n >= 26 when k >= 30.
    3. Confirms that the exception set coincides with E_infty = {1, 3, ..., 25}.
    """
    E_infty = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25}
    results = {}
    all_conjecture_passed = True

    for k in range(30, max_k + 1):
        pk = compute_pk_recurrence(max_n + 2, k)
        Dk = compute_Dk(pk)
        exceptions = set(find_exceptions(Dk, max_n))

        # Check exceptions >= 26
        fails_ge_26 = [n for n in exceptions if n >= 26]
        matches_E_infty = (exceptions == E_infty)

        passed = (not fails_ge_26) and matches_E_infty
        if not passed:
            all_conjecture_passed = False

        results[k] = {
            "passed": passed,
            "fails_ge_26": fails_ge_26,
            "Nk": compute_threshold_Nk(Dk, max_n),
            "exceptions": sorted(list(exceptions)),
        }

    return {
        "all_passed": all_conjecture_passed,
        "results": results,
    }
