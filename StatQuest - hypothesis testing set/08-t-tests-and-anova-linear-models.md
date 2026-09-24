[⏮️ **Previous: 07 — Which t-test to Use**](07-which-t-test-to-use.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 09 — Statistical Power** ⏭️](09-statistical-power.md)

---

# 08: Linear Models Part 2 — t-tests and ANOVA

**StatQuest with Josh Starmer · Hypothesis Testing Set**

> [!TIP]
> **Core Intuition:**
> A t-test is secretly a **linear regression**. Fit a model with one overall mean (the null: "no groups") and a model with a separate mean per group (the alternative). If giving each group its own mean **shrinks the leftover error a lot** relative to the noise, the groups differ. That comparison is the **F-statistic**. With two groups it gives exactly the same answer as a t-test ($F = t^2$); with three or more groups the same recipe is **ANOVA**. One framework, many named tests.

> ✍️ **My one line (write after watching, no peeking):**

> [!WARNING]
> **Prerequisites:** this video builds on *Linear Models Part 0* (least squares) and *Part 1* (linear regression, $R^2$). If it feels confusing, skip it for now — topics 06–07 cover what you need for the t-tests this week, and linear regression is covered properly in Month 3. Come back to this note then.

---

### 1. Two Models for the Same Data

Group A = {3, 5, 4, 6} (mean 4.5), group B = {7, 8, 6, 9} (mean 7.5). Overall mean = 6.

```text
   Null model: ONE mean for everyone          Alternative: one mean PER group

   A: 3 4 5 6     B: 6 7 8 9                  A: 3 4 5 6        B: 6 7 8 9
   ------------ 6.0 ------------              --- 4.5 ---       --- 7.5 ---

   squared distances to 6.0                   squared distances to own group mean
   A: 9 + 4 + 1 + 0 = 14                      A: 2.25 + 0.25 + 0.25 + 2.25 = 5
   B: 0 + 1 + 4 + 9 = 14                      B: 2.25 + 0.25 + 0.25 + 2.25 = 5
   SS(mean) = 28                              SS(fit)  = 10
```

---

### 2. The F-Statistic

$$ \boxed{\; F = \frac{\big(SS(\text{mean}) - SS(\text{fit})\big) \,/\, (p_{\text{fit}} - p_{\text{mean}})}{SS(\text{fit}) \,/\, (n - p_{\text{fit}})} \;} $$

| Piece | Meaning | Example |
| :--- | :--- | :--- |
| $SS(\text{mean}) - SS(\text{fit})$ | Error removed by letting groups have their own means | 28 − 10 = 18 |
| $p_{\text{fit}} - p_{\text{mean}}$ | Extra parameters used to remove it | 2 − 1 = 1 |
| $SS(\text{fit}) / (n - p_{\text{fit}})$ | Leftover noise per remaining degree of freedom | 10 / (8 − 2) = 1.67 |

$$ F = \frac{18 / 1}{10 / 6} = 10.8 \qquad p = 0.017 $$

A Student's (pooled) two-sample t-test on the same data gives $t = -3.29$, and $(-3.29)^2 = 10.8$ with **the identical p-value**. Same test, different packaging.

---

### 3. The Design Matrix

Writing the alternative model as a regression makes the "linear model" part concrete:

```text
      y  =  B1 * [in group A]  +  B2 * [in group B]

      y      A   B
    [ 3 ]  [ 1   0 ]
    [ 5 ]  [ 1   0 ]            least squares gives
    [ 4 ]  [ 1   0 ]   ->       B1 = 4.5  (mean of A)
    [ 6 ]  [ 1   0 ]            B2 = 7.5  (mean of B)
    [ 7 ]  [ 0   1 ]
    [ 8 ]  [ 0   1 ]
    [ 6 ]  [ 0   1 ]
    [ 9 ]  [ 0   1 ]
```

The columns of 1s and 0s are just one-hot encoded group labels — the same thing `pd.get_dummies` produces.

---

### 4. ANOVA: More Than Two Groups

Add a third column for group C and the formula doesn't change: $p_{\text{fit}} = 3$, $p_{\text{mean}} = 1$. That's **one-way ANOVA**.

| | t-test | ANOVA |
| :--- | :--- | :--- |
| Groups | 2 | 2 or more |
| $H_0$ | $\mu_A = \mu_B$ | All group means equal |
| Rejecting $H_0$ tells you | A and B differ | **At least one** group differs — not which |

> **Why not run t-tests between every pair?** Three groups → 3 pairwise tests; ten groups → 45. The false positives pile up (topic 05, section 5). ANOVA asks one question first; follow-up pairwise comparisons then need a correction (Tukey, Bonferroni).

**Assumptions** (the "quiet requirements"): independent observations, roughly normal residuals, similar variance across groups. `scipy.stats.f_oneway` runs it; Welch's ANOVA exists if variances differ.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Tests are regressions** | Every coefficient p-value in `statsmodels` is a t-test | `smf.ols("y ~ group", df).fit().summary()` reproduces the t-test |
| **One-hot design matrix** | Categorical features in any linear model | `pd.get_dummies` / `OneHotEncoder` build exactly these columns |
| **F = error reduction / noise** | Same logic as comparing nested models | Does adding a feature reduce residual error more than chance would? |
| **ANOVA before pairwise** | Multi-arm experiments (A/B/C/D tests) | One omnibus test first, then corrected pairwise comparisons |

---

### 6. Check Your Understanding

**Q1: Two groups give $t = 2.5$. What F would the linear-model approach give?**
<details>
<summary><b>Reveal Answer</b></summary>

$F = t^2 = 6.25$, with the same p-value.
</details>

**Q2: An ANOVA across 4 ad creatives gives p = 0.003. Your manager asks which creative is best. What can you say?**
<details>
<summary><b>Reveal Answer</b></summary>

Only that the four creatives don't all have the same mean. To say which differ, run pairwise comparisons with a multiple-testing correction (e.g. Tukey's HSD) and report the estimated differences with confidence intervals.
</details>

**Q3: In the F formula, why divide $SS(\text{fit})$ by $n - p_{\text{fit}}$?**
<details>
<summary><b>Reveal Answer</b></summary>

It turns total leftover error into an estimate of noise **per degree of freedom**. Each parameter you fit uses up one degree of freedom, and a model with more parameters will always shrink the error a little by chance — dividing by the remaining degrees of freedom keeps the comparison fair.
</details>

---

### 📺 Source

* **Video:** [Linear Models Part 2: t-tests and ANOVA](https://youtu.be/NF5_btOaCig)

---

[⏮️ **Previous: 07 — Which t-test to Use**](07-which-t-test-to-use.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 09 — Statistical Power** ⏭️](09-statistical-power.md)
