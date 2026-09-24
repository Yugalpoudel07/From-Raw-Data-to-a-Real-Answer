[⏮️ **Previous: 03 — p-values: What They Are**](03-p-values-what-they-are.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 05 — Thresholds for Significance** ⏭️](05-thresholds-for-significance.md)

---

# 04: How to Calculate p-values

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> A p-value is built from **three pieces added together**: (1) the probability of exactly what you observed, (2) the probability of anything **equally rare**, and (3) the probability of anything **rarer**. Parts 2 and 3 are why a p-value is never just "the probability of my data" — a single outcome can be very unlikely without being surprising (every specific sequence of 100 coin flips is unlikely). For continuous data the same idea becomes **area in the tails** of a distribution.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Three-Part Recipe

$$ p = \underbrace{P(\text{observed})}_{\text{1}} + \underbrace{P(\text{equally rare outcomes})}_{\text{2}} + \underbrace{P(\text{rarer outcomes})}_{\text{3}} $$

All three are computed **assuming the null hypothesis is true**.

---

### 2. Discrete Example: Is This Coin Fair?

**$H_0$:** the coin is fair, $P(H) = 0.5$.

**Flip it twice, get two heads.**

```text
   Outcome   HH     HT     TH     TT
   Prob.    0.25   0.25   0.25   0.25

   1. observed (2 heads)          0.25
   2. equally rare (2 tails)      0.25
   3. rarer                       none
                                 -----
                          p  =   0.50
```

Two heads in two flips is completely unremarkable for a fair coin.

**Flip it five times, get 4 heads and 1 tail.** Count heads; each count has a binomial probability ($n=5, p=0.5$):

| Heads | 0 | 1 | 2 | 3 | 4 | 5 |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| Probability | 1/32 | 5/32 | 10/32 | 10/32 | **5/32** | 1/32 |

1. Observed (4 heads): 5/32
2. Equally rare (1 head = 4 tails): 5/32
3. Rarer (0 heads, 5 heads): 1/32 + 1/32

$$ p = \frac{5 + 5 + 1 + 1}{32} = \frac{12}{32} = 0.375 $$

Still no reason to doubt the coin.

> **Why add "equally rare" and "rarer"?** Without them, collecting more data would make *every* specific result look astonishing — the chance of any exact count of heads in 1,000 flips is tiny. The p-value measures how **extreme** the result is, not how specific.

---

### 3. Continuous Example: Tail Areas

For continuous data you can't list outcomes, so "equally rare or rarer" becomes **everything at least as far from the centre** — the area in the tails.

Suppose adult heights under $H_0$ follow $N(\mu = 170, \sigma = 10)$ cm, and you observe someone 190 cm tall.

$$ z = \frac{190 - 170}{10} = 2.0 $$

```text
                        ___
                      /     \
                    /         \
                 __/           \__
    ####______/                   \______####
   -----|-----------------|-----------------|-----
       150               170               190
       z=-2                                z=+2

   left tail  = 0.0228        right tail = 0.0228
   two-sided p = 0.0455
```

| | p-value |
| :--- | :--- |
| Two-sided ("taller **or shorter** than expected") | **0.0455** |
| One-sided ("taller than expected" only) | 0.0228 |

The two-sided value is the default for the reasons in topic 02.

---

### 4. When There's No Formula: Simulate the Null

The same recipe works by brute force. A **permutation test** builds the null distribution by shuffling:

```text
   1. Compute the observed difference in means between groups A and B.
   2. Pool all values. Shuffle the group labels at random.
   3. Recompute the difference. Repeat 10,000 times.
   4. p = (number of shuffled differences at least as extreme as observed + 1)
          / (10,000 + 1)
```

If the labels don't matter (the null), shuffling them shouldn't change anything — so the shuffled differences *are* the null distribution. No normality assumption needed. This is the first build task of the week: implement it and check it against `scipy.stats.ttest_ind`.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Tail area** | What `scipy.stats` functions return | `2 * norm.sf(abs(z))` for a two-sided z-test |
| **Binomial p-value** | Testing a rate against a baseline | `scipy.stats.binomtest(k, n, p=0.5)` |
| **Permutation test** | p-values for any metric, no formula needed | Is model B's F1 better than A's on the same test set? Shuffle which model each prediction came from |
| **"Equally rare or rarer"** | Why a single unlikely event isn't evidence | A "rare" anomaly among millions of rows is expected by chance |

---

### 6. Check Your Understanding

**Q1: A fair-coin null. You flip 5 times and get 5 heads. What is the two-sided p-value?**
<details>
<summary><b>Reveal Answer</b></summary>

Observed: 1/32. Equally rare: 5 tails, 1/32. Rarer: none. $p = 2/32 = 0.0625$. Even five heads in a row is not below 0.05 — five flips is a very small experiment.
</details>

**Q2: Under $H_0$ a test statistic is standard normal. You observe z = −2.5. Two-sided p-value?**
<details>
<summary><b>Reveal Answer</b></summary>

Each tail beyond |z| = 2.5 has area ≈ 0.0062, so two-sided $p \approx 0.0124$.
</details>

**Q3: In a permutation test with 10,000 shuffles, 37 shuffled differences are at least as extreme as the observed one. What's the p-value?**
<details>
<summary><b>Reveal Answer</b></summary>

$p = (37 + 1) / (10{,}000 + 1) \approx 0.0038$. The +1 counts the observed arrangement itself and prevents reporting an impossible p = 0.
</details>

---

### 📺 Source

* **Video:** [How to Calculate p-values](https://youtu.be/JQc3yx0-Q9E)

---

[⏮️ **Previous: 03 — p-values: What They Are**](03-p-values-what-they-are.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 05 — Thresholds for Significance** ⏭️](05-thresholds-for-significance.md)
