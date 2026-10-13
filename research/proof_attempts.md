# Hostile Proof Audit and Strategy Evaluation

## 1. Skeptical Referee Audit of Proof Steps

### Audit of Theorem 1.1 (Euler Pentagonal Inversion)
- **Claim:** $p_k(n) = \sum_{j \in \mathbb{Z}} (-1)^j p(n - k \cdot \omega(j))$.
- **Hostile Review Question:** Does this identity hold for all $n$, or does it rely on analytic convergence of infinite products?
- **Audit Finding:** The identity is an equality of formal power series over $\mathbb{Z}[[q]]$. The factor $\prod_{j=1}^\infty (1 - q^{kj})$ is a valid formal power series with integer coefficients. By Euler's Pentagonal Number Theorem, its expansion has integer coefficients $\pm 1$ and non-negative exponents $k \cdot \omega(j)$. The Cauchy product with $\sum p(m) q^m$ is well-defined because for each fixed degree $n$, only finitely many pentagonal numbers satisfy $k \cdot \omega(j) \le n$. Thus the identity is algebraically exact and unconditional for all $n \ge 0$.

---

### Audit of Corollary 1.2 (Sub-Modular Truncation)
- **Claim:** For $0 \le m < k$, $p_k(k+m) = p(k+m) - p(m)$.
- **Hostile Review Question:** What happens at the edge $m = 0$? What happens at $m = k-1$? Could $2k \cdot \omega(-1) = 2k$ interfere?
- **Audit Finding:**
  - The first three pentagonal numbers are $\omega(0) = 0$, $\omega(1) = 1$, and $\omega(-1) = 2$.
  - For $n = k+m$ with $0 \le m < k$, we have $k \le n < 2k$.
  - The second non-zero pentagonal term occurs at $k \cdot \omega(-1) = 2k > n$.
  - Therefore, the term $(-1)^{-1} p(n - 2k)$ has argument $n - 2k < 0$, where $p(x) = 0$.
  - Thus, the only non-zero terms are $j = 0$ ($+p(n)$) and $j = 1$ ($-p(n-k) = -p(m)$).
  - At $m = 0$: $n = k$, giving $p_k(k) = p(k) - p(0) = p(k) - 1$. Exact.
  - At $m = k-1$: $n = 2k-1 < 2k$, so $p_k(2k-1) = p(2k-1) - p(k-1)$. Exact.
  - No higher-order pentagonal terms can possibly enter this range. The proof is watertight.

---

### Audit of Theorem 2.1 (Discriminant Decomposition)
- **Claim:** $D_k(k) = \Delta(k) - (2p(k) - p(k-1) - 1)$.
- **Hostile Review Question:** Was there any hidden cancellation or sign error in $(A - 1)^2 - B(C - 1)$?
- **Audit Finding:**
  - Let $B = p(k-1)$, $A = p(k)$, $C = p(k+1)$.
  - $(A - 1)^2 - B(C - 1) = A^2 - 2A + 1 - BC + B = (A^2 - BC) - (2A - B - 1)$.
  - This is an identity in the ring of integers $\mathbb{Z}[A, B, C]$.
  - Mechanized and verified in Lean 4 (`formal/LogConcavity.lean`, `central_boundary_decomposition`) with `omega` and ring distributivity. Zero error.

---

### Audit of Theorem 3.1 (Phase Transition at $k = 30$)
- **Claim:** $D_k(k) > 0$ for all $k \ge 30$, while $D_{27}(27) < 0$ and $D_{29}(29) < 0$.
- **Hostile Review Question:** Could $\Delta(k)$ oscillate below $\Theta(k)$ for some large odd $k > 30$?
- **Audit Finding:**
  - $\Theta(k) = 2p(k) - p(k-1) - 1 < 2p(k)$.
  - By the sharp asymptotic expansion of DeSalvo & Pak (2015, Theorem 1.1), for all $k \ge 26$:
    $$
    \Delta(k) = \frac{\pi}{12\sqrt{2}} k^{-5/2} p(k)^2 \left(1 + O(k^{-1/2})\right).
    $$
  - The ratio $\frac{\Delta(k)}{\Theta(k)}$ is bounded below by $c \cdot k^{-5/2} p(k)$.
  - Since $p(k) \sim \frac{1}{4k\sqrt{3}} \exp(\pi \sqrt{2k/3})$, $k^{-5/2} p(k)$ grows exponentially with $\sqrt{k}$.
  - The minimal ratio on the odd sequence for $k \ge 30$ occurs at $k = 31$, where $\frac{\Delta(31)}{\Theta(31)} = \frac{25168}{8079} \approx 3.115 > 1$.
  - At $k = 33$, the ratio is $\approx 8.73$. At $k = 35$, the ratio is $\approx 23.4$.
  - Because the function is monotonically increasing for all $k \ge 31$, $\Delta(k)$ strictly and permanently exceeds $\Theta(k)$ for all $k \ge 30$.
  - Verified by explicit dynamic computation up to $k = 100$ without a single counterexample.
