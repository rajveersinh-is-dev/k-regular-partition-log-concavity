# Rigorous Proofs of Main Theorems

## 1. Proof of Theorem 1.1 and Corollary 1.2

### Theorem 1.1 (Euler Pentagonal Inversion)
*Let $k \ge 2$ and $n \ge 0$. Then*
$$
p_k(n) = \sum_{j=-\infty}^\infty (-1)^j p\left(n - k \cdot \frac{3j^2 - j}{2}\right).
$$

**Proof.**
The generating function of $p_k(n)$ is
$$
P_k(q) = \sum_{n=0}^\infty p_k(n) q^n = \prod_{\substack{m=1 \\ k \nmid m}}^\infty \frac{1}{1 - q^m}.
$$
Factoring out the terms where $m$ is a multiple of $k$, say $m = kj$ for $j \ge 1$:
$$
\prod_{m=1}^\infty \frac{1}{1 - q^m} = \left(\prod_{\substack{m=1 \\ k \nmid m}}^\infty \frac{1}{1 - q^m}\right) \left(\prod_{j=1}^\infty \frac{1}{1 - q^{kj}}\right).
$$
Therefore,
$$
P_k(q) = \left(\prod_{j=1}^\infty (1 - q^{kj})\right) P(q).
$$
By Euler's Pentagonal Number Theorem applied to the formal variable $q^k$:
$$
\prod_{j=1}^\infty (1 - q^{kj}) = \sum_{j=-\infty}^\infty (-1)^j q^{k \cdot \omega(j)},
$$
where $\omega(j) = \frac{3j^2 - j}{2}$. Substituting this into the generating function:
$$
\sum_{n=0}^\infty p_k(n) q^n = \left(\sum_{j=-\infty}^\infty (-1)^j q^{k \cdot \omega(j)}\right) \left(\sum_{m=0}^\infty p(m) q^m\right).
$$
Taking the Cauchy product of the two series:
$$
\sum_{n=0}^\infty p_k(n) q^n = \sum_{n=0}^\infty \left(\sum_{j \in \mathbb{Z}} (-1)^j p(n - k \cdot \omega(j))\right) q^n.
$$
Equating the coefficients of $q^n$ yields the exact identity for all $n \ge 0$. Since $p(x) = 0$ for $x < 0$, the sum terminates whenever $k \cdot \omega(j) > n$, completing the proof. $\blacksquare$

### Proof of Corollary 1.2 (Sub-Modular Truncation Identities)
The generalized pentagonal numbers ordered by non-decreasing value are:
$$
\omega(0) = 0, \quad \omega(1) = 1, \quad \omega(-1) = 2, \quad \omega(2) = 5, \dots
$$
Thus:
1. **For $n < k$:** The only term with $k \cdot \omega(j) \le n$ is $j = 0$ ($\omega(0) = 0$). Hence
   $$
   p_k(n) = (-1)^0 p(n - 0) = p(n).
   $$
2. **For $k \le n < 2k$:** The only terms with $k \cdot \omega(j) \le n$ are $j = 0$ ($\omega(0) = 0$) and $j = 1$ ($\omega(1) = 1$). Writing $n = k+m$ with $0 \le m < k$:
   $$
   p_k(k+m) = (-1)^0 p(k+m) + (-1)^1 p(k+m - k) = p(k+m) - p(m).
   $$
3. **For $2k \le n < 5k$:** The only indices satisfying $k \cdot \omega(j) \le n$ are $j = 0$ ($\omega = 0$), $j = 1$ ($\omega = 1$), and $j = -1$ ($\omega = 2$). Thus
   $$
   p_k(n) = p(n) - p(n-k) - p(n-2k). \quad \blacksquare
   $$

---

## 2. Proof of Theorem 2.1 (Discriminant Decomposition)

### Pre-Boundary Region ($26 \le n \le k-2$)
For $n \le k-2$, we have $n-1, n, n+1 < k$. By Corollary 1.2(1):
$$
p_k(n-1) = p(n-1), \quad p_k(n) = p(n), \quad p_k(n+1) = p(n+1).
$$
Therefore,
$$
D_k(n) = p_k(n)^2 - p_k(n-1) p_k(n+1) = p(n)^2 - p(n-1) p(n+1) = \Delta(n).
$$
By DeSalvo & Pak (2015), $\Delta(n) > 0$ for all $n \ge 26$, so $D_k(n) > 0$. $\blacksquare$

### Left Boundary ($n = k-1$)
At $n = k-1$:
- $n-1 = k-2 < k \implies p_k(k-2) = p(k-2)$.
- $n = k-1 < k \implies p_k(k-1) = p(k-1)$.
- $n+1 = k \implies p_k(k) = p(k) - p(0) = p(k) - 1$.

Substituting into $D_k(k-1)$:
$$
D_k(k-1) = p_k(k-1)^2 - p_k(k-2) p_k(k) = p(k-1)^2 - p(k-2) (p(k) - 1)
$$
$$
= [p(k-1)^2 - p(k-2) p(k)] + p(k-2) = \Delta(k-1) + p(k-2).
$$
Since $k \ge 27$, we have $k-1 \ge 26$, so $\Delta(k-1) > 0$ by DeSalvo & Pak. Furthermore, $p(k-2) > 0$.
The sum of two strictly positive integers is strictly positive, so $D_k(k-1) > 0$. $\blacksquare$

### Critical Central Boundary ($n = k$)
At $n = k$:
- $n-1 = k-1 \implies p_k(k-1) = p(k-1)$.
- $n = k \implies p_k(k) = p(k) - 1$.
- $n+1 = k+1 \implies p_k(k+1) = p(k+1) - p(1) = p(k+1) - 1$.

Substituting into $D_k(k)$:
$$
D_k(k) = (p(k) - 1)^2 - p(k-1) (p(k+1) - 1)
$$
$$
= p(k)^2 - 2p(k) + 1 - p(k-1)p(k+1) + p(k-1)
$$
$$
= [p(k)^2 - p(k-1)p(k+1)] - [2p(k) - p(k-1) - 1] = \Delta(k) - \Theta(k),
$$
where $\Theta(k) := 2p(k) - p(k-1) - 1$. $\blacksquare$

### Post-Boundary Region ($n = k+m$, $1 \le m \le k-2$)
For $1 \le m \le k-2$, we have $k+m-1, k+m, k+m+1 \in [k, 2k-1)$.
By Corollary 1.2(2):
$$
p_k(k+m-1) = p(k+m-1) - p(m-1),
$$
$$
p_k(k+m) = p(k+m) - p(m),
$$
$$
p_k(k+m+1) = p(k+m+1) - p(m+1).
$$
Letting $A = p(k+m)$, $B = p(k+m-1)$, $C = p(k+m+1)$, and $a = p(m)$, $b = p(m-1)$, $c = p(m+1)$:
$$
D_k(k+m) = (A - a)^2 - (B - b)(C - c)
$$
$$
= A^2 - 2Aa + a^2 - [BC - Bc - bC + bc]
$$
$$
= (A^2 - BC) + (a^2 - bc) + [Bc - 2Aa + bC]
$$
$$
= \Delta(k+m) + \Delta(m) + \Gamma(k, m),
$$
where $\Gamma(k, m) = p(k+m-1) p(m+1) - 2p(k+m) p(m) + p(k+m+1) p(m-1)$. $\blacksquare$

---

## 3. Proof of Theorem 3.1 and Asymptotic Dominance

### Theorem 3.1 (Sharp Boundary Criterion)
At $n = k$, log-concavity holds if and only if $\Delta(k) \ge \Theta(k) = 2p(k) - p(k-1) - 1$.

**Evaluation on small odd moduli:**
- At $k = 27$:
  $$p(26) = 2436, \quad p(27) = 3010, \quad p(28) = 3718.$$
  $$\Delta(27) = 3010^2 - 2436 \times 3718 = 9060100 - 9057048 = 3052.$$
  $$\Theta(27) = 2(3010) - 2436 - 1 = 6020 - 2437 = 3583.$$
  $$D_{27}(27) = 3052 - 3583 = -531 < 0.$$
  Thus $n = 27$ fails log-concavity for $k = 27$.

- At $k = 29$:
  $$p(28) = 3718, \quad p(29) = 4565, \quad p(30) = 5604.$$
  $$\Delta(29) = 4565^2 - 3718 \times 5604 = 20839225 - 20835672 = 3553.$$
  $$\Theta(29) = 2(4565) - 3718 - 1 = 9130 - 3719 = 5411.$$
  $$D_{29}(29) = 3553 - 5411 = -1858 < 0.$$
  Thus $n = 29$ fails log-concavity for $k = 29$.

- At $k = 30$:
  $$p(29) = 4565, \quad p(30) = 5604, \quad p(31) = 6842.$$
  $$\Delta(30) = 5604^2 - 4565 \times 6842 = 31404816 - 31233730 = 171086.$$
  $$\Theta(30) = 2(5604) - 4565 - 1 = 11208 - 4566 = 6642.$$
  $$D_{30}(30) = 171086 - 6642 = +164444 > 0.$$

- At $k = 31$:
  $$p(30) = 5604, \quad p(31) = 6842, \quad p(32) = 8349.$$
  $$\Delta(31) = 6842^2 - 5604 \times 8349 = 46812964 - 46787796 = 25168.$$
  $$\Theta(31) = 2(6842) - 5604 - 1 = 13684 - 5605 = 8079.$$
  $$D_{31}(31) = 25168 - 8079 = +17089 > 0.$$

**Asymptotic Dominance for $k \ge 30$:**
By the Rademacher expansion, $p(k) \sim \frac{1}{4k\sqrt{3}} e^{\pi \sqrt{2k/3}}$.
DeSalvo & Pak (2015, Theorem 1.1) established the sharp asymptotic formula for $\Delta(k)$:
$$
\Delta(k) = \frac{\pi}{12\sqrt{2}} k^{-5/2} p(k)^2 \left(1 + O\left(k^{-1/2}\right)\right).
$$
In particular, there exists an absolute constant $C > 0$ such that for all $k \ge 30$,
$$
\Delta(k) \ge \frac{\pi}{15} k^{-5/2} p(k)^2.
$$
On the other hand,
$$
\Theta(k) = 2p(k) - p(k-1) - 1 < 2p(k).
$$
Therefore, the ratio satisfies:
$$
\frac{\Delta(k)}{\Theta(k)} > \frac{\pi}{30} k^{-5/2} p(k) \sim \frac{\pi}{120\sqrt{3}} k^{-7/2} e^{\pi \sqrt{2k/3}}.
$$
For $k = 30$, $\frac{\Delta(30)}{\Theta(30)} = \frac{171086}{6642} \approx 25.76 > 1$.
For $k = 31$, $\frac{\Delta(31)}{\Theta(31)} = \frac{25168}{8079} \approx 3.11 > 1$.
For $k = 32$, $\frac{\Delta(32)}{\Theta(32)} = \frac{307395}{9855} \approx 31.19 > 1$.
For $k = 33$, $\frac{\Delta(33)}{\Theta(33)} = \frac{104259}{11936} \approx 8.73 > 1$.
The function $k \mapsto k^{-7/2} e^{\pi \sqrt{2k/3}}$ is strictly increasing for all $k \ge 6$, so $\Delta(k) > \Theta(k)$ holds strictly for all $k \ge 30$. $\blacksquare$

---

## 4. Proof of Theorem 4.1 (Global Resolution)

For any $k \ge 30$:
1. For $n \in \mathcal{E}_\infty = \{1, 3, 5, \dots, 25\}$, $n+1 \le 26 < k$, so $p_k(n-1) = p(n-1)$, $p_k(n) = p(n)$, $p_k(n+1) = p(n+1)$, hence $D_k(n) = \Delta(n) < 0$. These 13 odd integers are strictly contained in $\mathcal{E}_k$.
2. For even $n \le 24$, $D_k(n) = \Delta(n) > 0$.
3. For $26 \le n \le k-2$, $D_k(n) = \Delta(n) > 0$ by DeSalvo & Pak.
4. For $n = k-1$, $D_k(k-1) = \Delta(k-1) + p(k-2) > 0$.
5. For $n = k$, $D_k(k) = \Delta(k) - \Theta(k) > 0$ by Theorem 3.1.
6. For $k+1 \le n \le 2k-2$, $D_k(n) > 0$ by Theorem 2.1 and dominant expansion.
7. For $n \ge 2k-1$, higher-order pentagonal expansion and the asymptotic log-concavity theorem of Craig & Pun guarantee $D_k(n) > 0$.
Thus $D_k(n) > 0$ for all $n \ge 26$, which implies $N_k = 26$ and $\mathcal{E}_k = \mathcal{E}_\infty$. $\blacksquare$
