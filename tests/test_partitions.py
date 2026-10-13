"""
Comprehensive unit test suite for k-regular partition log-concavity algorithms.
All tests compute values from first principles without preloaded tables.
"""

import unittest
from src.partition import (
    compute_partitions_euler,
    compute_sigma,
    compute_gk,
    compute_pk_recurrence,
    compute_pk_pentagonal_inversion,
)
from src.discriminant import (
    compute_Delta,
    compute_Dk,
    boundary_penalty_Theta,
    cross_coupling_Gamma,
    verify_transition_decomposition,
)
from src.phase_transition import (
    find_exceptions,
    compute_threshold_Nk,
    analyze_boundary_transition,
    verify_heim_neuhauser_conjecture,
)


class TestPartitionsAndLogConcavity(unittest.TestCase):

    def setUp(self):
        self.p_table = compute_partitions_euler(120)

    def test_partition_base_values(self):
        """Verifies that Euler recurrence computes known combinatorial values from first principles."""
        p = self.p_table
        self.assertEqual(p[0], 1)
        self.assertEqual(p[1], 1)
        self.assertEqual(p[2], 2)
        self.assertEqual(p[3], 3)
        self.assertEqual(p[4], 5)
        self.assertEqual(p[5], 7)
        self.assertEqual(p[6], 11)
        self.assertEqual(p[7], 15)
        self.assertEqual(p[8], 22)
        self.assertEqual(p[9], 30)
        self.assertEqual(p[10], 42)

    def test_pk_dual_algorithm_equivalence(self):
        """Verifies that the divisor-recurrence algorithm and pentagonal-inversion algorithm agree."""
        for k in [2, 3, 5, 10, 20]:
            pk_rec = compute_pk_recurrence(50, k)
            pk_inv = compute_pk_pentagonal_inversion(50, k, self.p_table)
            self.assertEqual(pk_rec, pk_inv, f"Algorithms disagree for k={k}")

    def test_submodular_truncation_identities(self):
        """Verifies Corollary 1.2: p_k(n) = p(n) for n < k, and p_k(k+m) = p(k+m) - p(m) for m < k."""
        for k in [15, 25, 30]:
            pk = compute_pk_recurrence(2 * k, k)
            # Range 0 <= n < k
            for n in range(k):
                self.assertEqual(pk[n], self.p_table[n])
            # Range 0 <= m < k
            for m in range(k):
                expected = self.p_table[k + m] - self.p_table[m]
                self.assertEqual(pk[k + m], expected, f"Mismatch at k={k}, m={m}")

    def test_higher_order_truncation_identity(self):
        """Verifies Corollary 1.2(3): p_k(2k+m) = p(2k+m) - p(k+m) - p(m) for m < k."""
        k = 15
        pk = compute_pk_recurrence(3 * k, k)
        for m in range(k):
            expected = self.p_table[2 * k + m] - self.p_table[k + m] - self.p_table[m]
            self.assertEqual(pk[2 * k + m], expected, f"Mismatch at m={m}")

    def test_left_boundary_formula(self):
        """Verifies D_k(k-1) = Delta(k-1) + p(k-2) for k >= 27."""
        Delta = compute_Delta(self.p_table)
        for k in [27, 28, 29, 30, 31]:
            pk = compute_pk_recurrence(k + 2, k)
            Dk = compute_Dk(pk)
            expected = Delta[k - 1] + self.p_table[k - 2]
            self.assertEqual(Dk[k - 1], expected, f"Mismatch at left boundary for k={k}")
            self.assertGreater(Dk[k - 1], 0, f"D_k(k-1) must be strictly positive for k={k}")

    def test_central_boundary_formula(self):
        """Verifies D_k(k) = Delta(k) - (2*p(k) - p(k-1) - 1)."""
        Delta = compute_Delta(self.p_table)
        for k in [25, 27, 28, 29, 30, 31, 32]:
            pk = compute_pk_recurrence(k + 2, k)
            Dk = compute_Dk(pk)
            theta = boundary_penalty_Theta(self.p_table, k)
            expected = Delta[k] - theta
            self.assertEqual(Dk[k], expected, f"Mismatch at central boundary for k={k}")

    def test_phase_transition_boundary_values(self):
        """
        Verifies the exact phase transition values at the central boundary n = k:
        k=27 and k=29 are negative (exceptions), while k=30 and k=31 are positive.
        """
        results = {r["k"]: r for r in analyze_boundary_transition(27, 32)}
        # k = 27 fails
        self.assertEqual(results[27]["Dk_at_k"], -531)
        self.assertTrue(results[27]["is_exception"])

        # k = 29 fails
        self.assertEqual(results[29]["Dk_at_k"], -1858)
        self.assertTrue(results[29]["is_exception"])

        # k = 30 succeeds
        self.assertEqual(results[30]["Dk_at_k"], 164444)
        self.assertTrue(results[30]["is_positive"])

        # k = 31 succeeds
        self.assertEqual(results[31]["Dk_at_k"], 17089)
        self.assertTrue(results[31]["is_positive"])

    def test_transition_window_decomposition(self):
        """Verifies D_k(k+m) = Delta(k+m) + Delta(m) + Gamma(k, m) for 1 <= m <= k-2."""
        k = 30
        for m in range(1, k - 1):
            decomp = verify_transition_decomposition(self.p_table, k, m)
            self.assertTrue(decomp["match"], f"Decomposition failed at m={m}")
            self.assertGreater(decomp["actual_Dk"], 0, f"D_k(k+m) not positive at m={m}")

    def test_classical_exception_set(self):
        """Verifies that Delta(n) fails exactly for the 13 odd integers <= 25."""
        Delta = compute_Delta(self.p_table)
        exceptions = [n for n in range(1, 100) if Delta[n] < 0]
        expected_exceptions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
        self.assertEqual(exceptions, expected_exceptions)

    def test_heim_neuhauser_conjecture_verification(self):
        """Verifies the Heim-Neuhauser conjecture N_k = 26 for k in [30, 36] up to n = 100."""
        verification = verify_heim_neuhauser_conjecture(max_k=36, max_n=100)
        self.assertTrue(verification["all_passed"])
        for k in range(30, 37):
            res = verification["results"][k]
            self.assertEqual(res["Nk"], 26)
            self.assertEqual(len(res["fails_ge_26"]), 0)


if __name__ == "__main__":
    unittest.main()
