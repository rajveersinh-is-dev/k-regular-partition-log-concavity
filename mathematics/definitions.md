# Mathematical Definitions

## 1. Partitions and $k$-Regularity

### Definition 1.1 (Integer Partition)
A **partition** of a non-negative integer $n$ is a finite non-increasing sequence of positive integers $\lambda = (\lambda_1, \lambda_2, \dots, \lambda_\ell)$ such that
$$
\sum_{i=1}^\ell \lambda_i = n.
$$
The integers $\lambda_i$ are called the **parts** of $\lambda$, and $\ell = \ell(\lambda)$ is the **length** of the partition. By convention, there is exactly one partition of $0$, the empty partition $\emptyset$.
We denote by $p(n)$ the number of partitions of $n$, with $p(0) = 1$ and $p(n) = 0$ for $n < 0$.

### Definition 1.2 ($k$-Regular Partition)
Let $k \ge 2$ be an integer. A partition $\lambda = (\lambda_1, \dots, \lambda_\ell)$ of $n$ is called **$k$-regular** if no part $\lambda_i$ is divisible by $k$:
$$
\lambda_i \not\equiv 0 \pmod{k} \quad \text{for all } i \in \{1, \dots, \ell\}.
$$
We denote by $p_k(n)$ the number of $k$-regular partitions of $n$, with $p_k(0) = 1$ and $p_k(n) = 0$ for $n < 0$.
When $k = \infty$, we set $p_\infty(n) := p(n)$.

### Definition 1.3 (Generating Functions)
The generating functions of $p(n)$ and $p_k(n)$ are given by the formal power series:
$$
P(q) := \sum_{n=0}^\infty p(n) q^n = \prod_{m=1}^\infty \frac{1}{1 - q^m},
$$
$$
P_k(q) := \sum_{n=0}^\infty p_k(n) q^n = \prod_{\substack{m=1 \\ k \nmid m}}^\infty \frac{1}{1 - q^m} = \prod_{j=1}^\infty (1 - q^{kj}) \cdot P(q).
$$

### Definition 1.4 (Generalized Pentagonal Numbers)
For each integer $j \in \mathbb{Z}$, the **generalized pentagonal number** $\omega(j)$ is defined by
$$
\omega(j) := \frac{3j^2 - j}{2}.
$$
The sequence of values for $j = 0, 1, -1, 2, -2, 3, -3, \dots$ is
$$
\omega(0) = 0, \; \omega(1) = 1, \; \omega(-1) = 2, \; \omega(2) = 5, \; \omega(-2) = 7, \; \omega(3) = 12, \; \omega(-3) = 15, \dots
$$

## 2. Log-Concavity and Discriminants

### Definition 2.1 (Log-Concavity)
A sequence of non-negative real numbers $\{\alpha(n)\}_{n \ge 0}$ is said to be **log-concave at index $n \ge 1$** if
$$
\alpha(n)^2 \ge \alpha(n-1) \alpha(n+1).
$$
It is **strictly log-concave at $n$** if $\alpha(n)^2 > \alpha(n-1) \alpha(n+1)$.

### Definition 2.2 (Log-Concavity Discriminants)
For the unrestricted partition function $p(n)$, the **classical Turán discriminant** is
$$
\Delta(n) := p(n)^2 - p(n-1) p(n+1).
$$
For the $k$-regular partition function $p_k(n)$, the **$k$-regular discriminant** is
$$
D_k(n) := p_k(n)^2 - p_k(n-1) p_k(n+1).
$$

### Definition 2.3 (Log-Concavity Threshold)
For $k \in \{2, 3, 4, \dots\} \cup \{\infty\}$, the **log-concavity threshold** $N_k$ is the smallest non-negative integer such that $p_k(n)$ is log-concave for all $n \ge N_k$:
$$
N_k := \min \{ M \in \mathbb{N} : \forall n \ge M, \; D_k(n) \ge 0 \}.
$$

### Definition 2.4 (Exception Set)
The **exception set** $\mathcal{E}_k$ is the set of all positive integers where $p_k(n)$ fails log-concavity:
$$
\mathcal{E}_k := \{ n \in \mathbb{N} : D_k(n) < 0 \}.
$$
The classical exception set for $p(n)$ is
$$
\mathcal{E}_\infty = \{1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25\}.
$$
In particular, $|\mathcal{E}_\infty| = 13$ and $\max \mathcal{E}_\infty = 25$, so $N_\infty = 26$.
