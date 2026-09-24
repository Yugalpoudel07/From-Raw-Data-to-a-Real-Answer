[⏮️ **Previous: 06 — The CLT and the t-test**](06-central-limit-theorem-and-the-t-test.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 08 — t-tests and ANOVA as Linear Models** ⏭️](08-t-tests-and-anova-linear-models.md)

---

# 07: Which t-test to Use

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> There are really only three t-tests, and you pick one by asking **how your data are structured**: one group against a fixed number (**one-sample**), two separate groups of different subjects (**two-sample / independent**), or the same subjects measured twice (**paired**). Picking the wrong one isn't a technicality — using an unpaired test on paired data can turn a rock-solid effect into "not significant".

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Decision Tree

```text
                    What are you comparing?
                              |
         +--------------------+--------------------+
         |                                         |
   one group vs a                            two groups
   known number                                    |
         |                        +----------------+----------------+
   ONE-SAMPLE t-test              |                                 |
                        same subjects measured          different subjects
                        twice / naturally matched       in each group
                                  |                                 |
                           PAIRED t-test               TWO-SAMPLE t-test
                                                     (use Welch's by default)
```

---

### 2. The Three Tests

| Test | Question | Statistic | `scipy.stats` |
| :--- | :--- | :--- | :--- |
| **One-sample** | Is this group's mean different from $\mu_0$? | $\dfrac{\bar{x} - \mu_0}{s/\sqrt{n}}$ | `ttest_1samp(x, mu0)` |
| **Two-sample (Welch)** | Do two independent groups have different means? | $\dfrac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$ | `ttest_ind(a, b, equal_var=False)` |
| **Paired** | Did the same subjects change? | one-sample test on the differences $d_i$: $\dfrac{\bar{d}}{s_d/\sqrt{n}}$ | `ttest_rel(after, before)` |

> **Student's vs Welch's two-sample test.** Student's version assumes both groups have the same variance and pools them. Welch's doesn't. Welch loses almost nothing when variances *are* equal and protects you when they aren't, so **use Welch's by default**. (scipy's default is Student's — pass `equal_var=False`.)

---

### 3. Why Pairing Matters So Much

Eight patients, blood pressure before and after a drug:

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Before | 140 | 152 | 128 | 160 | 145 | 138 | 150 | 135 |
| After | 136 | 149 | 125 | 154 | 143 | 133 | 147 | 131 |
| Difference | −4 | −3 | −3 | −6 | −2 | −5 | −3 | −4 |

| Test used | t | p-value | Verdict |
| :--- | :-: | :-: | :--- |
| ❌ Two-sample (Welch), treating before/after as unrelated groups | −0.74 | 0.47 | "No effect" |
| ✅ Paired | −8.28 | 0.00007 | Clear drop of 3.75 mmHg |

```text
   Unpaired view: two clouds that overlap heavily
      before:  128 ........................... 160
      after:   125 ........................ 154

   Paired view: every single patient went DOWN by 2-6
      differences:  -6 -5 -4 -4 -3 -3 -3 -2      <- tight, all negative
```

Patients differ from each other by 30+ mmHg; the drug moves each one by about 4. The paired test subtracts out the between-patient variation and sees the drug effect clearly.

---

### 4. One-Tailed or Two-Tailed?

A separate choice from *which* test. Default to **two-tailed** (topic 02). Use one-tailed only if you fixed the direction before seeing the data and an effect the other way is genuinely irrelevant.

---

### 5. When None of Them Fit

| Problem | Alternative |
| :--- | :--- |
| Small samples, heavy skew or outliers | Permutation test (build task 1), Mann–Whitney U (independent), Wilcoxon signed-rank (paired) |
| More than two groups | ANOVA (topic 08) |
| Categorical outcome (counts in categories) | Chi-square test |
| Non-independent observations (users with many sessions) | Aggregate per user first, or use a mixed model |

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Paired test** | Comparing two models on the **same** folds or seeds | Model A vs B on the same 10 CV folds → `ttest_rel` on the per-fold scores |
| **Welch's test** | A/B tests with unequal group sizes and variances | Treatment gets 10% of traffic, control 90% |
| **One-sample** | Checking against a target or baseline | Is the model's mean error different from the old system's published 4.2? |
| **Wrong test, wrong answer** | Unpaired test on paired data hides real improvements | Per-fold CV scores treated as independent samples |

---

### 7. Check Your Understanding

**Q1: You evaluate model A and model B on the same 10 cross-validation folds. Which test?**
<details>
<summary><b>Reveal Answer</b></summary>

Paired t-test on the 10 per-fold differences — each fold is a matched pair. (Caveat: CV folds share training data, so they're not fully independent; treat the p-value as approximate.)
</details>

**Q2: Group A: 50 users on the old page. Group B: 50 *different* users on the new page. Which test, and which variant?**
<details>
<summary><b>Reveal Answer</b></summary>

Two-sample (independent) t-test, Welch's version (`equal_var=False`), since there's no reason to assume equal variances.
</details>

**Q3: Why is a paired test just a one-sample test in disguise?**
<details>
<summary><b>Reveal Answer</b></summary>

Compute each subject's difference $d_i = \text{after}_i - \text{before}_i$. The paired test asks whether the mean of those differences is 0 — which is exactly a one-sample t-test of $d$ against $\mu_0 = 0$.
</details>

---

### 📺 Source

* **Video:** [Which t-test to use](https://youtu.be/nnBJeb_I-q8)

---

[⏮️ **Previous: 06 — The CLT and the t-test**](06-central-limit-theorem-and-the-t-test.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 08 — t-tests and ANOVA as Linear Models** ⏭️](08-t-tests-and-anova-linear-models.md)
