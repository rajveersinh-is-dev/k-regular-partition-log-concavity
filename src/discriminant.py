"""
Exact calculation and structural decomposition of log-concavity discriminants.
"""

from typing import List, Dict


def compute_Delta(p_table: List[int]) -> List[int]:
    """
    Computes the classical partition Turan discriminant:
        Delta(n) = p(n)^2 - p(n-1) * p(n+1)
    for 1 <= n < len(p_table) - 1.
    """
    n_max = len(p_table) - 1
    delta = [0] * n_max
    for n in range(1, n_max):
        delta[n] = p_table[n] ** 2 - p_table[n - 1] * p_table[n + 1]
    return delta


def compute_Dk(pk_table: List[int]) -> List[int]:
    """
    Computes the k-regular partition log-concavity discriminant:
        D_k(n) = p_k(n)^2 - p_k(n-1) * p_k(n+1)
    for 1 <= n < len(pk_table) - 1.
    """
    n_max = len(pk_table) - 1
    dk = [0] * n_max
    for n in range(1, n_max):
        dk[n] = pk_table[n] ** 2 - pk_table[n - 1] * pk_table[n + 1]
    return dk


def boundary_penalty_Theta(p_table: List[int], k: int) -> int:
    """
    Computes the exact boundary penalty term at n = k:
        Theta(k) = 2 * p(k) - p(k-1) - 1.
    """
    if k < 1 or k >= len(p_table):
        raise ValueError(f"k={k} out of range for p_table length {len(p_table)}")
    return 2 * p_table[k] - p_table[k - 1] - 1


def cross_coupling_Gamma(p_table: List[int], k: int, m: int) -> int:
    """
    Computes the cross-coupling term Gamma(k, m) in the post-boundary region:
        Gamma(k, m) = p(k+m-1) * p(m+1) - 2 * p(k+m) * p(m) + p(k+m+1) * p(m-1).
    """
    if k + m + 1 >= len(p_table):
        raise ValueError(f"Index k+m+1={k+m+1} exceeds table size {len(p_table)}")
    term1 = p_table[k + m - 1] * p_table[m + 1]
    term2 = 2 * p_table[k + m] * p_table[m]
    term3 = p_table[k + m + 1] * p_table[m - 1]
    return term1 - term2 + term3


def verify_transition_decomposition(p_table: List[int], k: int, m: int) -> Dict[str, int]:
    """
    Verifies the exact identity for D_k(k+m):
        D_k(k+m) = Delta(k+m) + Delta(m) + Gamma(k, m).
    Returns a dictionary of all constituent terms and the computed sum.
    """
    A = p_table[k + m]
    B = p_table[k + m - 1]
    C = p_table[k + m + 1]
    a = p_table[m]
    b = p_table[m - 1]
    c = p_table[m + 1]

    delta_big = A ** 2 - B * C
    delta_small = a ** 2 - b * c
    gamma = cross_coupling_Gamma(p_table, k, m)
    predicted_Dk = delta_big + delta_small + gamma

    actual_Dk = (A - a) ** 2 - (B - b) * (C - c)

    return {
        "k": k,
        "m": m,
        "n": k + m,
        "Delta_big": delta_big,
        "Delta_small": delta_small,
        "Gamma": gamma,
        "predicted_Dk": predicted_Dk,
        "actual_Dk": actual_Dk,
        "match": predicted_Dk == actual_Dk,
    }
