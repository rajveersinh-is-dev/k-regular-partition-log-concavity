# Research Problem Selection: Log-Concavity Phase Transition for $k$-Regular Partitions

## 1. Selected Problem Statement

Let $k \ge 2$ be an integer. A partition of a positive integer $n$ is called **$k$-regular** if none of its parts is divisible by $k$. We denote by $p_k(n)$ the number of $k$-regular partitions of $n$, with convention $p_k(0) = 1$.

A sequence $\{\alpha(n)\}_{n \ge 0}$ is said to be **log-concave at $n$** if
$$
\alpha(n)^2 \ge \alpha(n-1) \alpha(n+1).
$$
The log-concavity discriminant of $p_k(n)$ is defined as
$$
D_k(n) := p_k(n)^2 - p_k(n-1) p_k(n+1).
$$
For the classical unrestricted partition function $p(n) = p_\infty(n)$, Nicolas (1978) and DeSalvo & Pak (2015) established that $\{p(n)\}_{n \ge 0}$ is log-concave if and only if $n \ge 26$ or $n$ is even. In particular, the smallest integer $N_\infty$ such that $p(n)$ is log-concave for all $n \ge N_\infty$ is
$$
N_\infty = 26.
$$
The exceptional set where log-concavity fails for $p(n)$ is precisely the set of 13 odd integers:
$$
\mathcal{E}_\infty = \{1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25\}.
$$

For $k$-regular partitions, let $N_k$ be the smallest integer such that $\{p_k(n)\}$ is log-concave for all $n \ge N_k$:
$$
N_k := \min \{ M \in \mathbb{N} : \forall n \ge M, \; D_k(n) \ge 0 \}.
$$

### The Open Conjecture (Heim & Neuhauser, 2024)
In their 2024 work *"Inequalities for $k$-regular partitions"* (arXiv:2406.10987, published in *Research in Number Theory*), Bernhard Heim and Markus Neuhauser formulated the following conjecture (Section 4, Conjecture):

> **Conjecture (Heim & Neuhauser, 2024).**
> Let $k \ge 2$. Let $N_k$ be the smallest integer such that $\{p_k(n)\}_n$ is log-concave at every $n \ge N_k$. Then:
> $$
> N_k = N_\infty = 26 \quad \text{if and only if} \quad k \ge 30.
> $$
> Moreover, for all $k \ge 30$, the set of exceptions $\mathcal{E}_k = \{n \in \mathbb{N} : D_k(n) < 0\}$ coincides exactly with $\mathcal{E}_\infty$.

## 2. Evaluation Along Research Dimensions

| Criterion | Weight | Assessment |
|---|---:|---|
| Potential for meaningful new mathematics | 20% | High. Requires developing structural inversion theorems and exact discriminant decompositions for $k$-regular partitions. |
| Plausible route to a rigorous result | 20% | High. The generating function $\sum p_k(n) q^n = \prod_{j=1}^\infty (1 - q^{kj}) \sum p(n) q^n$ allows exact truncation via Euler's pentagonal number theorem. |
| Mathematical depth | 15% | Deep connection to partition asymptotics, modular forms (Dedekind eta quotients), and Turán inequalities. |
| Quality of existing research frontier | 10% | Active: Craig & Pun (2021) established asymptotic log-concavity; Dong & Ji (2024) proved $k=2$; Heim & Neuhauser (2024) posed the $k \ge 30$ stabilization conjecture. |
| Independence from large-scale computation | 15% | Fully independent. The decisive work is exact symbolic algebra, structural analysis, and inductive bounds. |
| Precision and testability | 10% | Fully rigorous mathematical statement with exact arithmetic verification from first principles. |
| Explanatory elegance | 5% | Explains the mysterious cutoff $k=30$ through an exact closed-form algebraic formula. |
| Portfolio and educational value | 5% | Outstanding contribution to analytic and algebraic combinatorics. |

## 3. Concrete Targets

- **Target A (Full Result):** Resolve the Heim–Neuhauser conjecture by establishing the exact structural decomposition of $D_k(n)$ and proving $N_k = 26$ for all $k \ge 30$.
- **Target B (Substantial New Theorem):** Prove the exact boundary formula $D_k(k) = \Delta(k) - [2p(k) - p(k-1) - 1]$, showing that $k = 30$ is the exact minimal modulus where boundary failures cease, and explain why $k = 27$ and $k = 29$ fail.
- **Target C (Structural Inversion Theorem):** Prove the exact truncation identity $p_k(k+m) = p(k+m) - p(m)$ for all $0 \le m < k$ and generalize it via Euler's pentagonal number theorem.
- **Target D (Formalization):** Formalize the core algebraic identities and discriminant decompositions in Lean 4 without any axioms or `sorry`.
