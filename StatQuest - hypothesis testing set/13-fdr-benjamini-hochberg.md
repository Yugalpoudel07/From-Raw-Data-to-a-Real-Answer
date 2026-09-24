[⏮️ **Previous: 12 — False Discovery Rate**](12-false-discovery-rate.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 14 — p-hacking and Power Calculations** ⏭️](14-p-hacking-and-power-calculations.md)

---

# 13: FDR and the Benjamini–Hochberg Method

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> Benjamini–Hochberg (BH) is a simple recipe that controls the false discovery rate: **sort your p-values, and compare each one to a threshold that grows with its rank.** The smallest p-value must beat a very strict bar; the second-smallest a slightly looser one; and so on. Find the largest p-value that still clears its bar and call it — and everything smaller — significant. It keeps far more real discoveries than Bonferroni while still promising that only about $q$ (e.g. 5%) of your discoveries are false.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Procedure

For $m$ tests and a target FDR $q$ (often 0.05):

```text
   1. Sort the p-values from smallest to largest:  p(1) <= p(2) <= ... <= p(m)
   2. Give each a rank i = 1, 2, ..., m
   3. Compute each rank's threshold:              (i / m) * q
   4. Find the LARGEST i where                     p(i) <= (i / m) * q
   5. Reject H0 for tests 1 ... i                  (all p-values up to that one)
```

$$ \boxed{\; k = \max\Big\{\, i : p_{(i)} \le \tfrac{i}{m}\, q \,\Big\} \quad\Rightarrow\quad \text{reject } H_{(1)}, \dots, H_{(k)} \;} $$

---

### 2. Worked Example

Ten tests, $q = 0.05$:

| Rank $i$ | p-value | Threshold $\frac{i}{10}(0.05)$ | $p \le$ threshold? | BH-adjusted p |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 0.001 | 0.005 | ✅ | 0.010 |
| 2 | 0.011 | 0.010 | ❌ | 0.044 |
| 3 | 0.014 | 0.015 | ✅ | 0.044 |
| 4 | 0.019 | 0.020 | ✅ | 0.044 |
| **5** | **0.022** | **0.025** | ✅ ← largest | 0.044 |
| 6 | 0.210 | 0.030 | ❌ | 0.350 |
| 7 | 0.380 | 0.035 | ❌ | 0.543 |
| 8 | 0.470 | 0.040 | ❌ | 0.588 |
| 9 | 0.620 | 0.045 | ❌ | 0.689 |
| 10 | 0.890 | 0.050 | ❌ | 0.890 |

The largest rank that passes is 5, so **tests 1–5 are discoveries — including rank 2, which failed its own threshold.** BH is a "step-up" procedure: once a larger p-value passes, everything below it comes along.

| Method | Discoveries |
| :--- | :-: |
| No correction (p < 0.05) | 5 |
| **Benjamini–Hochberg** (FDR 5%) | **5** |
| Bonferroni (p < 0.005) | 1 |

---

### 3. Adjusted p-values

Instead of comparing to thresholds, you can adjust every p-value and compare to $q$ directly:

$$ p^{\text{BH}}_{(i)} = \min_{j \ge i} \left( \frac{m}{j}\, p_{(j)} \right), \quad \text{capped at } 1 $$

Call significant anything with $p^{\text{BH}} \le 0.05$. Same answer as the threshold method, and it's what software returns:

```python
from statsmodels.stats.multitest import multipletests

reject, p_bh, _, _ = multipletests(pvals, alpha=0.05, method="fdr_bh")
```

---

### 4. Why It Works (Intuition)

```text
   p-value
   0.05 |                                            /  <- (i/m) q : the BH line
        |                                        /
        |                                    /
        |                                /
        |                            /
        |       o   o   o   o    /
        |   o               /      o      o      o      o   <- sorted p-values
        |o             /
      0 +------------------------------------------------ rank i
          discoveries = everything left of the last point under the line
```

If every test were null, sorted p-values would climb roughly in a straight line from 0 to 1 (they're uniform — topic 12). Real effects produce a cluster of p-values much smaller than that line predicts. The BH line sits $q$ of the way up the "all-null" line, so the points that fall under it are the ones too small to be explained by nulls alone.

**Assumptions:** the tests are independent or positively correlated (the usual case). For arbitrary dependence there's a more conservative variant (Benjamini–Yekutieli, `method="fdr_by"`).

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **BH on many metrics** | Controlling false alarms across a dashboard | After an A/B test, apply BH across all 40 secondary metrics |
| **Feature screening** | Keeping a list of candidate features honest | Univariate tests on 5,000 features → BH → shortlist for modelling |
| **Anomaly / alerting** | Many simultaneous monitors | BH across per-region drift tests so alerts aren't mostly noise |
| **Build task 2** | The "apply a correction" step | Run BH and Bonferroni on your 20 noise p-values and compare |

---

### 6. Check Your Understanding

**Q1: m = 5, q = 0.05, sorted p-values: 0.004, 0.030, 0.035, 0.041, 0.300. Which are discoveries?**
<details>
<summary><b>Reveal Answer</b></summary>

Thresholds: 0.01, 0.02, 0.03, 0.04, 0.05.
0.004 ≤ 0.01 ✅ · 0.030 ≤ 0.02 ❌ · 0.035 ≤ 0.03 ❌ · 0.041 ≤ 0.04 ❌ · 0.300 ≤ 0.05 ❌.
Largest passing rank is 1 → **only the first test** is a discovery.
</details>

**Q2: Why can BH reject a test whose p-value was above its own threshold?**
<details>
<summary><b>Reveal Answer</b></summary>

Because the rule is "find the largest rank that passes, then reject everything up to it". If rank 5 passes, the evidence as a whole supports five discoveries; rank 2's p-value is smaller than rank 5's, so it would be inconsistent to keep 5 and drop 2.
</details>

**Q3: When would you still prefer Bonferroni over BH?**
<details>
<summary><b>Reveal Answer</b></summary>

When even a single false positive is costly and there are few tests — for example, a handful of pre-specified primary outcomes in a clinical trial. Bonferroni controls the chance of *any* false positive; BH only controls their proportion.
</details>

---

### 📺 Source

* **Video:** [FDR and the Benjamini–Hochberg Method](https://youtu.be/K8LQSvtjcEo)

---

[⏮️ **Previous: 12 — False Discovery Rate**](12-false-discovery-rate.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 14 — p-hacking and Power Calculations** ⏭️](14-p-hacking-and-power-calculations.md)
