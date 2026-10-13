"""
Core algorithms for partition numbers and k-regular partitions.
All values are computed dynamically from first principles without precomputed lookup tables.
"""

from typing import List


def generalized_pentagonal_number(j: int) -> int:
    """Computes the j-th generalized pentagonal number: omega(j) = (3*j^2 - j) // 2."""
    return (3 * j * j - j) // 2


def compute_partitions_euler(max_n: int) -> List[int]:
    """
    Computes the unrestricted partition function p(n) for 0 <= n <= max_n
    using Euler's pentagonal number recurrence:
        p(n) = sum_{j != 0} (-1)^(j-1) p(n - omega(j))
    No precomputed values or constants are used.
    """
    if max_n < 0:
        return []
    p = [0] * (max_n + 1)
    p[0] = 1

    for n in range(1, max_n + 1):
        total = 0
        j = 1
        while True:
            # Positive index pentagonal number
            w1 = (3 * j * j - j) // 2
            if w1 > n:
                break
            sign = 1 if (j % 2 != 0) else -1
            total += sign * p[n - w1]

            # Negative index pentagonal number
            w2 = (3 * j * j + j) // 2
            if w2 <= n:
                total += sign * p[n - w2]
            j += 1
        p[n] = total

    return p


def compute_sigma(max_n: int) -> List[int]:
    """Computes divisor sum sigma(n) = sum_{d | n} d for 0 <= n <= max_n from first principles."""
    sigma = [0] * (max_n + 1)
    for d in range(1, max_n + 1):
        for m in range(d, max_n + 1, d):
            sigma[m] += d
    return sigma


def compute_gk(max_n: int, k: int) -> List[int]:
    """
    Computes arithmetic function g_k(n) = sigma(n) - k * sigma(n / k)
    where sigma(x) = 0 if x is not an integer.
    """
    sigma = compute_sigma(max_n)
    gk = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        val = sigma[n]
        if n % k == 0:
            val -= k * sigma[n // k]
        gk[n] = val
    return gk


def compute_pk_recurrence(max_n: int, k: int) -> List[int]:
    """
    Computes the k-regular partition function p_k(n) for 0 <= n <= max_n
    using the arithmetic Euler-type recurrence:
        n * p_k(n) = sum_{j=1}^n g_k(j) * p_k(n-j)
    with p_k(0) = 1.
    """
    if max_n < 0:
        return []
    gk = compute_gk(max_n, k)
    pk = [0] * (max_n + 1)
    pk[0] = 1

    for n in range(1, max_n + 1):
        s = 0
        for j in range(1, n + 1):
            s += gk[j] * pk[n - j]
        pk[n] = s // n

    return pk


def compute_pk_pentagonal_inversion(max_n: int, k: int, p_table: List[int] = None) -> List[int]:
    """
    Computes p_k(n) for 0 <= n <= max_n using the exact Euler Pentagonal Inversion Theorem:
        p_k(n) = sum_{j in Z} (-1)^j * p(n - k * omega(j))
    where omega(j) = (3*j^2 - j) // 2.
    """
    if p_table is None or len(p_table) <= max_n:
        p_table = compute_partitions_euler(max_n)

    pk = [0] * (max_n + 1)
    for n in range(max_n + 1):
        total = p_table[n]
        j = 1
        while True:
            w1 = (3 * j * j - j) // 2
            kw1 = k * w1
            if kw1 > n:
                break
            sign = -1 if (j % 2 != 0) else 1
            total += sign * p_table[n - kw1]

            w2 = (3 * j * j + j) // 2
            kw2 = k * w2
            if kw2 <= n:
                total += sign * p_table[n - kw2]
            j += 1
        pk[n] = total

    return pk
