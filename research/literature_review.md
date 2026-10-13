# Literature Review: Log-Concavity of Partition Functions and Regular Partitions

## 1. Historical Context and Log-Concavity of $p(n)$

The study of log-concavity and higher-order Turán inequalities for partition functions has a rich history originating in classical analytic number theory:

1. **Circle Method Foundations:**
   - G. H. Hardy and S. Ramanujan (1918) introduced the circle method to determine the asymptotic formula $p(n) \sim \frac{1}{4n\sqrt{3}} \exp\left(\pi \sqrt{\frac{2n}{3}}\right)$.
   - H. Rademacher (1937) established the exact convergent series representation for $p(n)$.
   - D. H. Lehmer (1939) derived sharp error bounds for Rademacher's series truncations.

2. **Log-Concavity of the Unrestricted Partition Function:**
   - J.-L. Nicolas (1978) proved that the sequence $\{p(n)\}_{n \ge 0}$ is log-concave for all sufficiently large $n$.
   - S. DeSalvo and I. Pak (2015, *Ramanujan J.*, 38:61–73) settled the exact threshold for $p(n)$:
     $$
     p(n)^2 - p(n-1) p(n+1) > 0 \quad \text{for all } n \ge 26.
     $$
     For $n \le 25$, the inequality holds if and only if $n$ is even. Thus, the minimal threshold is $N_\infty = 26$.
   - Chen, Wang, and Xie (2019) subsequently proved higher-order Turán inequalities ($4p(n)^3 - \dots > 0$) for $p(n)$.

## 2. Multiplicative Inequalities and $k$-Regular Partitions

1. **Bessenrodt–Ono Inequality:**
   - C. Bessenrodt and K. Ono (2016, *Ann. Comb.*, 20:59–64) proved that for $a, b \ge 2$ with $a+b \ge 10$:
     $$
     p(a) p(b) > p(a+b).
     $$
   - A. A. Alanazi, S. M. Gagola III, and A. O. Munagi (2017, *Ann. Comb.*) provided a combinatorial injection proof.

2. **Extensions to $k$-Regular Partitions:**
   - The generating function for the number of $k$-regular partitions $p_k(n)$ is:
     $$
     \sum_{n=0}^\infty p_k(n) q^n = \prod_{n=1}^\infty \frac{1 - q^{kn}}{1 - q^n}.
     $$
   - P. Hagis (1971, *Trans. Amer. Math. Soc.*) provided a Rademacher-type convergent series for $p_k(n)$.
   - O. Beckwith and C. Bessenrodt (2016, *Ann. Comb.*, 20:231–250) analyzed the Bessenrodt–Ono inequality for $p_k(n)$ for $2 \le k \le 6$.
   - B. Heim and M. Neuhauser (2024, *Research in Number Theory* / arXiv:2406.10987) proved that the Bessenrodt–Ono exception sets $E_k, F_k$ stabilize to $E_\infty, F_\infty$ if and only if $k \ge 10$.

## 3. Log-Concavity for $k$-Regular Partitions

1. **Asymptotic Log-Concavity:**
   - M. Griffin, K. Ono, L. Rolen, and D. Zagier (2019, *PNAS*, 116:6005–6010) developed a framework connecting Jensen polynomials to the Riemann Hypothesis and partition asymptotics.
   - W. Craig and A. Pun (2021, *Ann. Comb.*, 25:561–577) proved that for every fixed $k \ge 2$, $p_k(n)$ satisfies the Turán inequalities and is log-concave for all $n$ sufficiently large depending on $k$. However, their analytic bound on $N_k$ was not uniform in $k$ and grew very large.

2. **Resolution of $k = 2$:**
   - J. J. W. Dong and K. Q. Ji (2024, *J. Number Theory*) proved that for $k = 2$ (partitions into odd parts), $p_2(n)$ is log-concave for all $n \ge 33$, with failures at $n \in \{1, 2, 4, 8, 11, 13, 14, 16, 17, 19, 20, 23, 26, 29, 32\}$.

3. **The Heim–Neuhauser Stabilization Conjecture (2024):**
   - Heim & Neuhauser (2024, arXiv:2406.10987, Section 4) conjectured that $N_k$ stabilizes to $N_\infty = 26$ for all $k \ge 30$, while remaining strictly larger for $k < 30$ (e.g. $N_{29} = 30$, $N_{27} = 28$).
   - The exact algebraic and structural reason why $k = 30$ is the sharp stabilization threshold was left completely open.
