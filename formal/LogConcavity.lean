/-
  Formal Verification in Lean 4
  Repository: k-regular-partition-log-concavity
  Theorem: Exact Algebraic Decomposition of Log-Concavity Discriminants
  Author: Rajveer
  Rules: Zero `sorry`, Zero unproven `axiom` declarations.
-/

namespace KRegularPartitions

/--
  Theorem 1: Exact Left-Boundary Algebraic Decomposition (at n = k - 1).
  When p_k(k-2) = B, p_k(k-1) = A, and p_k(k) = C - 1,
  the discriminant D_k(k-1) satisfies:
    A^2 - B * (C - 1) = (A^2 - B * C) + B.
-/
theorem left_boundary_decomposition (A B C : Int) :
    A * A - B * (C - 1) = (A * A - B * C) + B := by
  have h : B * (C - 1) = B * C - B := by
    rw [Int.mul_sub, Int.mul_one]
  rw [h]
  omega

/--
  Theorem 2: Exact Central-Boundary Algebraic Decomposition (at n = k).
  When p_k(k-1) = B, p_k(k) = A - 1, and p_k(k+1) = C - 1,
  the discriminant D_k(k) satisfies:
    (A - 1)^2 - B * (C - 1) = (A^2 - B * C) - (2 * A - B - 1).
-/
theorem central_boundary_decomposition (A B C : Int) :
    (A - 1) * (A - 1) - B * (C - 1) = (A * A - B * C) - (2 * A - B - 1) := by
  have h1 : (A - 1) * (A - 1) = A * A - 2 * A + 1 := by
    calc
      (A - 1) * (A - 1) = A * (A - 1) - 1 * (A - 1) := by rw [Int.sub_mul]
      _ = (A * A - A * 1) - (A - 1) := by rw [Int.mul_sub, Int.one_mul]
      _ = A * A - 2 * A + 1 := by omega
  have h2 : B * (C - 1) = B * C - B := by
    rw [Int.mul_sub, Int.mul_one]
  rw [h1, h2]
  omega

/--
  Theorem 3: Exact General Transition Window Decomposition (for n = k + m).
  For any integers A, B, C (representing p(k+m), p(k+m-1), p(k+m+1))
  and a, b, c (representing p(m), p(m-1), p(m+1)),
  the shifted discriminant satisfies:
    (A - a)^2 - (B - b) * (C - c) = (A^2 - B * C) + (a^2 - b * c) + (B * c - 2 * A * a + b * C).
-/
theorem transition_window_decomposition (A B C a b c : Int) :
    (A - a) * (A - a) - (B - b) * (C - c) =
      (A * A - B * C) + (a * a - b * c) + (B * c - 2 * A * a + b * C) := by
  have hcomm : a * A = A * a := by rw [Int.mul_comm]
  have hassoc : 2 * A * a = 2 * (A * a) := by rw [Int.mul_assoc]
  have h1 : (A - a) * (A - a) = A * A - 2 * A * a + a * a := by
    calc
      (A - a) * (A - a) = A * (A - a) - a * (A - a) := by rw [Int.sub_mul]
      _ = (A * A - A * a) - (a * A - a * a) := by rw [Int.mul_sub, Int.mul_sub]
      _ = (A * A - A * a) - (A * a - a * a) := by rw [hcomm]
      _ = A * A - 2 * (A * a) + a * a := by omega
      _ = A * A - 2 * A * a + a * a := by rw [hassoc]
  have h2 : (B - b) * (C - c) = B * C - B * c - b * C + b * c := by
    calc
      (B - b) * (C - c) = B * (C - c) - b * (C - c) := by rw [Int.sub_mul]
      _ = (B * C - B * c) - (b * C - b * c) := by rw [Int.mul_sub, Int.mul_sub]
      _ = B * C - B * c - b * C + b * c := by omega
  rw [h1, h2]
  omega

/--
  Theorem 4: Exact Computation for k = 27 (Proving failure at n = 27).
  With p(26) = 2436, p(27) = 3010, p(28) = 3718:
  The boundary penalty strictly exceeds the classical discriminant.
-/
theorem boundary_failure_k27 :
    let B : Int := 2436
    let A : Int := 3010
    let C : Int := 3718
    let Δ : Int := A * A - B * C
    let Θ : Int := 2 * A - B - 1
    (A - 1) * (A - 1) - B * (C - 1) = -531 ∧
    Δ = 3052 ∧
    Θ = 3583 ∧
    Δ - Θ = -531 ∧
    (A - 1) * (A - 1) - B * (C - 1) < 0 := by
  intro B A C Δ Θ
  dsimp [B, A, C, Δ, Θ]
  decide

/--
  Theorem 5: Exact Computation for k = 29 (Proving failure at n = 29).
  With p(28) = 3718, p(29) = 4565, p(30) = 5604:
  The boundary penalty strictly exceeds the classical discriminant.
-/
theorem boundary_failure_k29 :
    let B : Int := 3718
    let A : Int := 4565
    let C : Int := 5604
    let Δ : Int := A * A - B * C
    let Θ : Int := 2 * A - B - 1
    (A - 1) * (A - 1) - B * (C - 1) = -1858 ∧
    Δ = 3553 ∧
    Θ = 5411 ∧
    Δ - Θ = -1858 ∧
    (A - 1) * (A - 1) - B * (C - 1) < 0 := by
  intro B A C Δ Θ
  dsimp [B, A, C, Δ, Θ]
  decide

/--
  Theorem 6: Exact Computation for k = 30 (Proving success at n = 30).
  With p(29) = 4565, p(30) = 5604, p(31) = 6842:
  The discriminant is strictly positive, establishing stability onset at k = 30.
-/
theorem boundary_success_k30 :
    let B : Int := 4565
    let A : Int := 5604
    let C : Int := 6842
    let Δ : Int := A * A - B * C
    let Θ : Int := 2 * A - B - 1
    (A - 1) * (A - 1) - B * (C - 1) = 164444 ∧
    Δ = 171086 ∧
    Θ = 6642 ∧
    Δ - Θ = 164444 ∧
    (A - 1) * (A - 1) - B * (C - 1) > 0 := by
  intro B A C Δ Θ
  dsimp [B, A, C, Δ, Θ]
  decide

/--
  Theorem 7: Exact Computation for k = 31 (Proving success at n = 31).
  With p(30) = 5604, p(31) = 6842, p(32) = 8349:
  Strict positivity continues.
-/
theorem boundary_success_k31 :
    let B : Int := 5604
    let A : Int := 6842
    let C : Int := 8349
    let Δ : Int := A * A - B * C
    let Θ : Int := 2 * A - B - 1
    (A - 1) * (A - 1) - B * (C - 1) = 17089 ∧
    Δ = 25168 ∧
    Θ = 8079 ∧
    Δ - Θ = 17089 ∧
    (A - 1) * (A - 1) - B * (C - 1) > 0 := by
  intro B A C Δ Θ
  dsimp [B, A, C, Δ, Θ]
  decide

end KRegularPartitions
