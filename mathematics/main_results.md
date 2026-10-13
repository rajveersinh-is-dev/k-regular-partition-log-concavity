# Main Mathematical Results

## 1. Exact Inversion and Truncation Representation

### Theorem 1.1 (Euler Pentagonal Inversion for $k$-Regular Partitions)
Let $k \ge 2$ and $n \ge 0$. Then $p_k(n)$ satisfies the exact finite alternating sum:
$$
p_k(n) = \sum_{j=-\infty}^\infty (-1)^j p\left(n - k \cdot \frac{3j^2 - j}{2}\right),
$$
where the sum has only finitely many non-zero terms (restricted to $|j| \le \frac{1 + \sqrt{1 + 24n/k}}{6}$).

### Corollary 1.2 (Sub-Modular Truncation Identitites)
For any $k \ge 2$:
1. **Range $0 \le n < k$:**
   $$
   p_k(n) = p(n).
   $$
2. **Range $k \le n < 2k$ (letting $n = k+m$ with $0 \le m < k$):**
   $$
   p_k(k+m) = p(k+m) - p(m).
   $$
3. **Range $2k \le n < 5k$ (letting $n = 2k+m$ with $0 \le m < 3k$):**
   $$
   p_k(n) = p(n) - p(n-k) - p(n-2k).
   $$

---

## 2. Structural Decomposition of the Discriminant

### Theorem 2.1 (Discriminant Decomposition in the Primary Transition Window)
Let $k \ge 27$, and let $D_k(n) = p_k(n)^2 - p_k(n-1) p_k(n+1)$.

1. **Pre-Boundary Region ($26 \le n \le k-2$):**
   $$
   D_k(n) = \Delta(n) > 0.
   $$
2. **Left Boundary ($n = k-1$):**
   $$
   D_k(k-1) = \Delta(k-1) + p(k-2).
   $$
   Since $k-1 \ge 26$ and $p(k-2) > 0$, $D_k(k-1) > 0$ strictly for all $k \ge 27$.
3. **Critical Central Boundary ($n = k$):**
   $$
   D_k(k) = \Delta(k) - \Theta(k),
   $$
   where $\Theta(k) := 2p(k) - p(k-1) - 1$.
4. **Post-Boundary Region ($n = k+m$ with $1 \le m \le k-2$):**
   $$
   D_k(k+m) = \Delta(k+m) + \Delta(m) + \Gamma(k, m),
   $$
   where the cross-coupling term is
   $$
   \Gamma(k, m) := p(k+m-1) p(m+1) - 2 p(k+m) p(m) + p(k+m+1) p(m-1).
   $$

---

## 3. The Phase-Transition Boundary Criterion

### Theorem 3.1 (Sharp Boundary Criterion at $n = k$)
The critical boundary $n = k$ is log-concave if and only if
$$
\Delta(k) \ge 2p(k) - p(k-1) - 1.
$$
Moreover:
1. For $k = 27$:
   $$
   \Delta(27) = 3052 < 3583 = \Theta(27) \implies D_{27}(27) = -531 < 0.
   $$
   Thus $n = 27$ is an exception, and $N_{27} \ge 28 > 26$.
2. For $k = 29$:
   $$
   \Delta(29) = 3553 < 5411 = \Theta(29) \implies D_{29}(29) = -1858 < 0.
   $$
   Thus $n = 29$ is an exception, and $N_{29} \ge 30 > 26$.
3. For $k = 30$:
   $$
   \Delta(30) = 171086 > 6642 = \Theta(30) \implies D_{30}(30) = +164444 > 0.
   $$
4. For all $k \ge 30$:
   $$
   \Delta(k) > \Theta(k) \implies D_k(k) > 0.
   $$
Therefore, $k = 30$ is the **exact, minimal integer** at which the critical boundary failure disappears.

---

## 4. Main Resolution Theorem

### Theorem 4.1 (Resolution of the Heim–Neuhauser Conjecture)
Let $k \ge 30$. Then:
1. $D_k(n) > 0$ for all $n \ge 26$.
2. The log-concavity threshold satisfies $N_k = 26$.
3. The exception set $\mathcal{E}_k$ stabilizes to
   $$
   \mathcal{E}_k = \mathcal{E}_\infty = \{1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25\}.
   $$
4. The stabilization condition $N_k = 26$ holds if and only if $k \ge 30$ (within the family of moduli with no odd boundary exceptions).
