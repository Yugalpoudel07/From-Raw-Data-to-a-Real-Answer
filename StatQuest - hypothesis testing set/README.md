[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [**Start Reading: Topic 01 — Hypothesis Testing & the Null Hypothesis** ⏭️](01-hypothesis-testing-and-the-null-hypothesis.md)

---

# 🧪 StatQuest with Josh Starmer — Hypothesis Testing Set

### *Deciding When a Result Is Real — and Seeing How Results Fool People*

[![Notes](https://img.shields.io/badge/Notes-16%20of%2016%20written-brightgreen?style=flat-square)](#-topic-directory--syllabus)
[![Channel](https://img.shields.io/badge/StatQuest-Josh_Starmer-red?style=flat-square&logo=youtube)](https://www.youtube.com/@statquest)
[![Videos](https://img.shields.io/badge/Videos-14%20core%20%2B%202%20shorts-blue?style=flat-square)](#-topic-directory--syllabus)
[![Focus](https://img.shields.io/badge/Focus-p--values%20%C2%B7%20t--tests%20%C2%B7%20power%20%C2%B7%20FDR-purple?style=flat-square)](#)

> [!NOTE]
> **About this Set:**
> Month 1's [StatQuest module](https://github.com/Yugalpoudel07/Mathematics-for-Data-Science/tree/main/StatQuest%20with%20Josh%20Starmer) was about *estimating* things honestly — standard errors, confidence intervals, the bootstrap. This set is about *deciding*: is the difference between two groups real, or could it be noise? It covers null hypotheses, p-values, t-tests, statistical power, and — most importantly — **the multiple-testing problem**: run 20 tests on random noise and one will look "significant". That one idea explains why so many published findings and dashboard "wins" don't hold up.
>
> The videos were picked from the [StatQuest video index](https://statquest.org/video-index/) to match the roadmap's assignment: *p-values, t-tests, statistical power, multiple-testing corrections, FDR* (time budget ≈ 3 hours).

---

## 🗺️ Topic Directory & Syllabus

Every note has a **Core Intuition** callout, a **"My one line"** box to fill in after watching, worked formulas and numbers, an ASCII diagram, a **Connection to Machine Learning & Data Science** table, and **Check Your Understanding** questions with hidden answers. The order below is the recommended watching order.

#### Part I — Foundations *(watch first; everything builds on these)*

| # | Topic | Core Statistical Idea | ML / Data Science Application |
| :-: | :--- | :--- | :--- |
| **01** | [**Hypothesis Testing and the Null Hypothesis**](01-hypothesis-testing-and-the-null-hypothesis.md) | Start from "no difference" and ask if the data are too surprising for it; you reject or fail to reject, never prove. | Every A/B test and model comparison starts from a null. |
| **02** | [**The Alternative Hypothesis**](02-alternative-hypothesis.md) | $H_1$ is "the null is wrong"; it fixes what counts as extreme — two-sided by default. | Choosing one- vs two-sided tests before the experiment. |

#### Part II — p-values

| # | Topic | Core Statistical Idea | ML / Data Science Application |
| :-: | :--- | :--- | :--- |
| **03** | [**p-values: What They Are and How to Interpret Them**](03-p-values-what-they-are.md) | $P(\text{data this extreme} \mid H_0)$ — not the probability the null is true, not effect size. | Reading A/B test results correctly; the most asked stats interview question. |
| **04** | [**How to Calculate p-values**](04-how-to-calculate-p-values.md) | Observed + equally rare + rarer; tail areas for continuous data; permutation tests by simulation. | p-values for any metric via shuffling (build task 1). |
| **05** | [**Thresholds for Significance**](05-thresholds-for-significance.md) | α is the false-positive rate you accept on true nulls; pick it by cost, before the data. | Same logic as choosing a classification threshold. |

#### Part III — t-tests

| # | Topic | Core Statistical Idea | ML / Data Science Application |
| :-: | :--- | :--- | :--- |
| **06** | [**The CLT and the t-test**](06-central-limit-theorem-and-the-t-test.md) | Means are ~normal even when data aren't; $t$ has heavier tails because $s$ is estimated. | t-tests on skewed business metrics; small-sample model comparisons. |
| **07** | [**Which t-test to Use**](07-which-t-test-to-use.md) | One-sample, two-sample (Welch by default), or paired — chosen by data structure. | Paired tests on per-fold CV scores; Welch for unequal A/B arms. |
| **08** | [**Linear Models Part 2: t-tests and ANOVA**](08-t-tests-and-anova-linear-models.md) *(needs Linear Models 0–1)* | A t-test is a regression; $F = t^2$; ANOVA extends it to 3+ groups. | Coefficient p-values in `statsmodels`; multi-arm experiments. |

#### Part IV — Statistical Power

| # | Topic | Core Statistical Idea | ML / Data Science Application |
| :-: | :--- | :--- | :--- |
| **09** | [**Statistical Power**](09-statistical-power.md) | $P(\text{catch a real effect}) = 1 - \beta$; driven by effect size, noise, $n$ and α. | Power is recall; why A/B tests need so much traffic. |
| **10** | [**Power Analysis**](10-power-analysis.md) | Choose α, power and the smallest effect worth detecting → $n$; $n \propto 1/d^2$. | Minimum detectable effect and sample size before launch (build task 3). |

#### Part V — Multiple Testing, p-hacking and FDR *(most important for the simulation write-up)*

| # | Topic | Core Statistical Idea | ML / Data Science Application |
| :-: | :--- | :--- | :--- |
| **11** | [**p-hacking: What It Is and How to Avoid It**](11-p-hacking.md) | Extra chances to hit p < 0.05 manufacture false findings; $1 - 0.95^{20} = 0.64$; Bonferroni. | Many metrics, hyperparameter search, test-set reuse (build task 2). |
| **12** | [**False Discovery Rate (FDR)**](12-false-discovery-rate.md) | The fraction of your discoveries that are false; null p-values are uniform. | FDR = 1 − precision; screening many metrics or features. |
| **13** | [**FDR and the Benjamini–Hochberg Method**](13-fdr-benjamini-hochberg.md) | Sort p-values; compare $p_{(i)}$ to $\frac{i}{m}q$; reject up to the largest pass. | `multipletests(method="fdr_bh")` across dashboards and feature screens. |
| **14** | [**p-hacking and Power Calculations**](14-p-hacking-and-power-calculations.md) | Topping up data inflates false positives (~20% with 10 looks); underpowered wins are exaggerated. | The peeking problem in A/B tests; the winner's curse after launch. |

#### Optional — Quick Refreshers *(YouTube Shorts, under a minute each)*

| # | Topic | Core Statistical Idea | ML / Data Science Application |
| :-: | :--- | :--- | :--- |
| **15** | [**Type I Errors (False Positives)**](15-type-1-errors.md) | Rejecting a true null; probability α. | False positives / FPR in classifiers. |
| **16** | [**Type II Errors (False Negatives)**](16-type-2-errors.md) | Missing a real effect; probability β = 1 − power. | False negatives / 1 − recall. |

---

## 🧠 Key Conceptual Pillars

```text
               ┌─────────────────────────────────────────────────┐
               │            THE LOGIC OF A TEST                   │
               │  H0, H1, "reject" vs "fail to reject"            │
               └────────────────────────┬────────────────────────┘
                                        ▼
               ┌─────────────────────────────────────────────────┐
               │            MEASURING SURPRISE                    │
               │  p-values, tail areas, thresholds (alpha)        │
               └────────────────────────┬────────────────────────┘
                                        ▼
               ┌─────────────────────────────────────────────────┐
               │            THE WORKHORSE TESTS                   │
               │  CLT -> t-tests (one/two-sample, paired), ANOVA  │
               └────────────────────────┬────────────────────────┘
                                        ▼
               ┌─────────────────────────────────────────────────┐
               │            DESIGNING TO SEE THE TRUTH            │
               │  power, effect size, sample size                 │
               └────────────────────────┬────────────────────────┘
                                        ▼
               ┌─────────────────────────────────────────────────┐
               │            HOW RESULTS FOOL PEOPLE               │
               │  p-hacking, peeking, multiple testing, FDR       │
               └─────────────────────────────────────────────────┘
```

1. **A p-value Is About the Data, Not the Hypothesis.** It's $P(\text{data} \mid H_0)$. It never tells you the probability your idea is right, and it never tells you how big the effect is.
2. **"Not Significant" Is Not "No Effect".** A test can only fail to reject. Whether that means anything depends on its power.
3. **Every Extra Look Is an Extra Chance to Be Fooled.** Twenty tests, one peek too many, one more outlier rule — each adds false-positive risk unless you correct for it.
4. **Design Before Data.** Hypothesis, metric, α and sample size are chosen before collecting anything. That's what makes the final p-value mean what it says.

---

## 💡 How Hypothesis Testing Powers Data Science & ML

| Statistical Concept | Machine Learning / Data Science Role | Concrete Application |
| :--- | :--- | :--- |
| **Null & alternative hypotheses** | The frame of every experiment | A/B tests, model-vs-model comparisons |
| **p-values** | Quantifying surprise under "no effect" | Experiment readouts, regression coefficient tables |
| **t-tests & ANOVA** | Comparing means across groups | Conversion/revenue per arm, per-fold CV score comparisons |
| **Type I / Type II errors** | The confusion matrix of decisions | α ↔ FPR, power ↔ recall, FDR ↔ 1 − precision |
| **Power analysis** | Sizing experiments before launch | Minimum detectable effect, traffic planning |
| **Multiple-testing corrections** | Keeping many simultaneous tests honest | Bonferroni / BH across metrics, segments, features |
| **Peeking & winner's curse** | Why wins shrink after launch | Fixed-horizon tests, sequential methods (Month 4) |

---

## 🛠️ Build Tasks This Set Prepares You For

| # | Build task (roadmap) | Notes to read first |
| :-: | :--- | :--- |
| 1 | **Permutation test from scratch** — shuffle labels thousands of times; check against a t-test | [04](04-how-to-calculate-p-values.md), [06](06-central-limit-theorem-and-the-t-test.md), [07](07-which-t-test-to-use.md) |
| 2 | **Simulate p-hacking on yourself** — 20 tests on noise, find the "significant" one, apply a correction, write 200 words | [11](11-p-hacking.md), [12](12-false-discovery-rate.md), [13](13-fdr-benjamini-hochberg.md), [14](14-p-hacking-and-power-calculations.md) |
| 3 | **Power analysis** — sample size for a given effect, verified by simulation | [09](09-statistical-power.md), [10](10-power-analysis.md) |

> [!IMPORTANT]
> **Gaps in the video set, covered in the notes instead:**
> * **Bonferroni correction** has no standalone video on the index — it's explained in [topic 11](11-p-hacking.md) and compared with BH in [topic 13](13-fdr-benjamini-hochberg.md). Your own simulation (build task 2) is the real teacher here.
> * **Chi-square tests** appear in the roadmap's "what you learn" list but aren't in this set; [topic 07](07-which-t-test-to-use.md) notes where they fit.

---

## 🔗 Relationship to the Other Modules

* **Mathematics-for-Data-Science → StatQuest topics 11, 15–18** (CLT, standard error, confidence intervals, bootstrap) are the foundation: a t-statistic is an estimate divided by its standard error, and a confidence interval that excludes 0 is a significant test.
* **Khan Academy — Significance Tests** (this repo) is the practice volume: 40+ problems on exactly these ideas.
* **The final analysis project** in this repo must use this material honestly — confidence intervals instead of bare point estimates, and a limitations section on what the tests can't prove.

---

## 📌 Study Tips

* Watch Parts I–II first — p-values are the idea everything else leans on.
* If topic 08 (Linear Models Part 2) feels confusing, skip it for now and return after linear regression in Month 3.
* Watch Part V **right before** writing the p-hacking simulation.
* Fill in each **"My one line"** box before reading the rest of the note.
* The four p-value misconceptions in [topic 03](03-p-values-what-they-are.md) are worth being able to recite from memory.

---

## 📺 Source Material

* **Channel:** [StatQuest with Josh Starmer — YouTube](https://www.youtube.com/@statquest)
* **Video index:** [statquest.org/video-index](https://statquest.org/video-index/)
* **Author:** Josh Starmer

---

[🏠 **Back to Main Repository**](../README.md) &nbsp;•&nbsp; [**Start with Topic 01: Hypothesis Testing & the Null Hypothesis** ⏭️](01-hypothesis-testing-and-the-null-hypothesis.md)
