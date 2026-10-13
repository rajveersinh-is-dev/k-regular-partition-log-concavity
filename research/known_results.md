# Known Results and Theoretical Foundations

## 1. Classical Theorems

### Theorem 1.1 (Euler's Pentagonal Number Theorem)
For $|q| < 1$,
$$
\prod_{n=1}^\infty (1 - q^n) = \sum_{j=-\infty}^\infty (-1)^j q^{\omega(j)} = 1 - q - q^2 + q^5 + q^7 - q^{12} - q^{15} + \cdots
$$
where $\omega(j) = \frac{3j^2 - j}{2}$ are the generalized pentagonal numbers for $j \in \mathbb{Z}$.

### Theorem 1.2 (Log-Concavity of $p(n)$; DeSalvo & Pak, 2015)
Let $p(n)$ denote the unrestricted partition function. Then
$$
\Delta(n) := p(n)^2 - p(n-1) p(n+1) > 0 \quad \text{for all } n \ge 26.
$$
For $1 \le n \le 25$, $\Delta(n) > 0$ if and only if $n$ is even. In particular:
- $\Delta(25) = -2936 < 0$.
- $\Delta(26) = 40516 > 0$.
- $\Delta(27) = 3052 > 0$.
- $\Delta(28) = 82874 > 0$.
- $\Delta(29) = 3553 > 0$.
- $\Delta(30) = 171086 > 0$.

### Theorem 1.3 (Higher-Order Turán Inequalities; Craig & Pun, 2021)
For any fixed $k \ge 2$, the $k$-regular partition function $p_k(n)$ satisfies the Turán inequalities and is strictly log-concave for all $n \ge M_k$ for some integer $M_k$.

### Theorem 1.4 (Threshold for $k=2$; Dong & Ji, 2024)
For $k = 2$ (partitions into odd parts), $N_2 = 33$. The exact failure set is
$$
\mathcal{E}_2 = \{1, 2, 4, 8, 11, 13, 14, 16, 17, 19, 20, 23, 26, 29, 32\}.
$$

### Theorem 1.5 (Bessenrodt–Ono Threshold for $p_k(n)$; Heim & Neuhauser, 2024)
The exception and equality sets $E_k$ and $F_k$ for the Bessenrodt–Ono inequality $p_k(a) p_k(b) > p_k(a+b)$ stabilize to $E_\infty$ and $F_\infty$ if and only if $k \ge 10$.

## 2. The Open Problem: Log-Concavity Threshold for $k \ge 3$

Prior to this work:
- For $3 \le k \le 29$, $N_k$ was known only through empirical calculation up to $n = 1000$ (Heim & Neuhauser 2024, Table 3).
- For $k \ge 30$, it was conjectured that $N_k = 26$ unconditionally, but no proof was known.
- The structural origin of the threshold $k = 30$ and the precise behavior at the critical boundary $n = k$ were completely unexplained.
