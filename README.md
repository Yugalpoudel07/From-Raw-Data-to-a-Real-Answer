# 🔎 From Raw Data to a Real Answer

Taking messy real-world data to a defensible conclusion. Hypothesis testing (permutation tests, p-hacking simulation, power analysis), data cleaning in pandas, publication-quality matplotlib/seaborn charts, and SQL with window functions — ending in a complete, honest analysis of real public data.

[![Modules with notes](https://img.shields.io/badge/Modules_with_notes-2%20of%2010-brightgreen?style=flat-square)](#-learning-roadmap--curriculum-status)
[![StatQuest](https://img.shields.io/badge/StatQuest_Hypothesis_Testing-16%20of%2016%20notes-blue?style=flat-square)](StatQuest%20-%20hypothesis%20testing%20set/README.md)
[![SQL Tutorial](https://img.shields.io/badge/Mode%20SQL%20Tutorial-52%20of%2052%20lessons-blue?style=flat-square)](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Focus](https://img.shields.io/badge/Focus-Clean%20%C2%B7%20Query%20%C2%B7%20Test%20%C2%B7%20Chart-purple?style=flat-square)](#)

---

## 🎯 Vision & Philosophy

The [Mathematics-for-Data-Science](https://github.com/Yugalpoudel07/Mathematics-for-Data-Science) repo rebuilt the maths. This repo is the **daily craft of a data scientist**: take a messy file, get it out of a database, clean it, reshape it, chart it, and draw a conclusion you can defend.

1. **Statistical Honesty First:** Every number comes with a range. Confidence intervals instead of bare point estimates, corrections when many things are tested, and a limitations section saying what the analysis *cannot* prove.
2. **Every Cleaning Decision Has a Reason:** Dropping a row, filling a gap or merging two tables is an analytical choice, so it's written down next to the code — with the row count before and after.
3. **Charts That Argue:** A figure's title states the finding, an annotation points at the evidence, and nothing is decorative.

---

## 🔄 The Pipeline

```text
   RAW DATA                                                          A REAL ANSWER
   (messy file,                                                      (a conclusion you
    database)                                                         can defend)
       │                                                                   ▲
       ▼                                                                   │
  ┌──────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
  │  QUERY   │ ───► │ CLEAN &      │ ───► │  TEST        │ ───► │  SHOW        │
  │          │      │ RESHAPE      │      │              │      │              │
  │  SQL     │      │  pandas      │      │  hypothesis  │      │  matplotlib  │
  │  joins,  │      │  merges,     │      │  tests,      │      │  seaborn,    │
  │  windows │      │  groupby,    │      │  power,      │      │  chart       │
  │          │      │  missing data│      │  FDR         │      │  choice      │
  └──────────┘      └──────────────┘      └──────────────┘      └──────────────┘
   Mode SQL          pandas User Guide     StatQuest set         matplotlib
   Daily SQL         Kaggle Pandas         Khan Academy          seaborn
                     Kaggle Data Cleaning                        Storytelling with Data
```

---

## 🗺️ Learning Roadmap & Curriculum Status

| Stage | Track / Module | Primary Source | Core Focus | Status | Progress |
| :-: | :--- | :--- | :--- | :-: | :-: |
| Test | **[StatQuest — Hypothesis Testing Set](StatQuest%20-%20hypothesis%20testing%20set/README.md)** | Josh Starmer | Null hypotheses, p-values, t-tests, ANOVA, power, p-hacking, FDR | ✅ **Notes written** | **16 / 16** |
| Test | **Khan Academy — Significance Tests** | Khan Academy | Practice problems on significance tests and confidence intervals | ⏳ Upcoming | 0 / 40+ problems |
| Clean | **pandas — official User Guide** | pandas docs | Indexing, merge/join, group by, reshaping, time series | ⏳ Upcoming | Planned |
| Clean | **Kaggle Learn — Pandas** | Kaggle | Six hands-on lessons with exercises | ⏳ Upcoming | 0 / 6 |
| Clean | **Kaggle Learn — Data Cleaning** | Kaggle | Missing values, scaling, dates, encodings, inconsistent entries | ⏳ Upcoming | 0 / 5 |
| Show | **matplotlib — official tutorials** | matplotlib docs | Quick Start, the Artist tutorial, layout (`fig, ax = plt.subplots()`) | ⏳ Upcoming | Planned |
| Show | **seaborn — official tutorial** | seaborn docs | `relplot`, `displot`, `catplot`, `pairplot`, `heatmap` | ⏳ Upcoming | Planned |
| Show | **Storytelling with Data** | Cole Nussbaumer Knaflic | Chart choice, decluttering, focusing attention | ⏳ Upcoming | Planned |
| Query | **[SQL Tutorial for Data Analysis (Mode / ThoughtSpot)](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/README.md)** | Mode / ThoughtSpot | `SELECT` to window functions, plus three product-analytics cases | ✅ **Completed** | **52 / 52 lessons** |
| Query | **A daily SQL practice platform** | DataLemur / StrataScratch / LeetCode | 30 minutes of timed SQL problems every study day | ⏳ Upcoming | Habit |

---

## 🌟 Spotlight: StatQuest — Hypothesis Testing Set (Notes Written)

> [!TIP]
> **Complete Notes Available:** All 16 videos have a note with a **Core Intuition** callout, worked numbers, an ASCII diagram, a **Connection to Machine Learning & Data Science** table, and self-check questions with hidden answers.  
> 👉 **[Explore the Hypothesis Testing Module Directory](StatQuest%20-%20hypothesis%20testing%20set/README.md)**

### 📚 Topic Breakdown

#### Part I: Foundations

* [**Topic 01: Hypothesis Testing and the Null Hypothesis**](StatQuest%20-%20hypothesis%20testing%20set/01-hypothesis-testing-and-the-null-hypothesis.md) — Start from "no difference"; reject or fail to reject, never prove.
* [**Topic 02: The Alternative Hypothesis**](StatQuest%20-%20hypothesis%20testing%20set/02-alternative-hypothesis.md) — What counts as extreme; two-sided by default, chosen before the data.

#### Part II: p-values

* [**Topic 03: p-values — What They Are**](StatQuest%20-%20hypothesis%20testing%20set/03-p-values-what-they-are.md) — $P(\text{data} \mid H_0)$, and the four things a p-value is not.
* [**Topic 04: How to Calculate p-values**](StatQuest%20-%20hypothesis%20testing%20set/04-how-to-calculate-p-values.md) — Observed + equally rare + rarer; tail areas; permutation tests.
* [**Topic 05: Thresholds for Significance**](StatQuest%20-%20hypothesis%20testing%20set/05-thresholds-for-significance.md) — α as an accepted false-positive rate, chosen by cost.

#### Part III: t-tests

* [**Topic 06: The CLT and the t-test**](StatQuest%20-%20hypothesis%20testing%20set/06-central-limit-theorem-and-the-t-test.md) — Why t-tests work on non-normal data; why "t" and not "z".
* [**Topic 07: Which t-test to Use**](StatQuest%20-%20hypothesis%20testing%20set/07-which-t-test-to-use.md) — One-sample, Welch two-sample, or paired — and why pairing matters.
* [**Topic 08: t-tests and ANOVA as Linear Models**](StatQuest%20-%20hypothesis%20testing%20set/08-t-tests-and-anova-linear-models.md) — $F = t^2$; ANOVA for 3+ groups *(revisit after Month 3)*.

#### Part IV: Statistical Power

* [**Topic 09: Statistical Power**](StatQuest%20-%20hypothesis%20testing%20set/09-statistical-power.md) — The chance of catching a real effect, and its four levers.
* [**Topic 10: Power Analysis**](StatQuest%20-%20hypothesis%20testing%20set/10-power-analysis.md) — Sample size from α, power and effect size; $n \propto 1/d^2$.

#### Part V: Multiple Testing, p-hacking & FDR

* [**Topic 11: p-hacking**](StatQuest%20-%20hypothesis%20testing%20set/11-p-hacking.md) — 20 tests on noise → 64% chance of a false "discovery"; Bonferroni.
* [**Topic 12: False Discovery Rate**](StatQuest%20-%20hypothesis%20testing%20set/12-false-discovery-rate.md) — The fraction of your discoveries that are false.
* [**Topic 13: FDR and Benjamini–Hochberg**](StatQuest%20-%20hypothesis%20testing%20set/13-fdr-benjamini-hochberg.md) — The step-up procedure, worked by hand.
* [**Topic 14: p-hacking and Power Calculations**](StatQuest%20-%20hypothesis%20testing%20set/14-p-hacking-and-power-calculations.md) — Topping up data, peeking, and the winner's curse.

#### Optional Refreshers

* [**Topic 15: Type I Errors**](StatQuest%20-%20hypothesis%20testing%20set/15-type-1-errors.md) · [**Topic 16: Type II Errors**](StatQuest%20-%20hypothesis%20testing%20set/16-type-2-errors.md) — False positives and false negatives, mapped onto the confusion matrix.

---

## 🌟 Spotlight: SQL Tutorial for Data Analysis — Mode / ThoughtSpot (Completed)

> [!TIP]
> **Complete Notes Available:** All 52 lessons across four phases are written up in 15 note files, from `SELECT` basics to window functions, plus three real product-analytics cases on Yammer data.  
> 👉 **[Explore the SQL Module Overview](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/README.md)** · **[Lesson Notes Index](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/README.md)**

### 📚 Phase Breakdown

#### Phase 1: Basic SQL (15 lessons)

* [**SELECT, LIMIT, WHERE**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/select_basics_notes.md) · [**Filtering Operators**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/filtering_operators_notes.md) · [**Logical Operators & ORDER BY**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/logical_operators_notes.md)

#### Phase 2: Intermediate SQL (20 lessons)

* [**Aggregate Functions**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/aggregate_functions_notes.md) · [**Joins**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/joins_notes.md) · [**DISTINCT and CASE**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/distinct_and_case_notes.md)

#### Phase 3: SQL Analytics Training (8 lessons)

* [**Case 1 — Investigating a Drop in User Engagement**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/case1_drop_in_engagement_notes.md) — What caused the weekly engagement drop?
* [**Case 2 — Analyzing In-Product Search**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/case2_search_functionality_notes.md) — Is search worth improving, and what should change?
* [**Case 3 — Validating A/B Test Results**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/case3_ab_test_validation_notes.md) — Are the results valid before we ship?
* [**Core Principles & Conclusion**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/core_principles_and_conclusion_notes.md) — The analytical discipline connecting all three cases.

#### Phase 4: Advanced SQL (9 lessons)

* [**Data Types & Dates**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/data_types_and_dates_notes.md) · [**String Functions & Wrangling**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/string_functions_and_wrangling_notes.md) · [**Subqueries**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/subqueries_notes.md) · [**Window Functions**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/window_functions_notes.md) · [**Pivoting & Performance**](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/pivoting_and_performance_notes.md)

---

## 💡 How Each Stage Powers Data Science

| Stage | Concept | Data Science Role | Concrete Application |
| :-: | :--- | :--- | :--- |
| Query | **Joins & aggregation** | Getting the right rows out of a database | Row counts checked before and after every join |
| Query | **Window functions** | Rankings, running totals, "previous event" logic | Sessionising events with `LAG`, top-N per group, cohort retention |
| Clean | **Merges, groupby, reshaping** | Making the question answerable | `pivot_table`, `melt`, validated merges |
| Clean | **Missing data** | *Why* it's missing decides how to handle it | Documented drop/fill decisions |
| Test | **p-values & t-tests** | Is a difference real or noise? | A/B test readouts, model comparisons |
| Test | **Power analysis** | Enough data to see what matters | Sample size before an experiment |
| Test | **Multiple testing / FDR** | Keeping many comparisons honest | BH correction across dashboard metrics |
| Show | **Chart choice** | Distribution, comparison, relationship, composition, trend | The right chart, justified against two alternatives |
| Show | **Annotation** | A figure that argues a point | Title states the finding; arrow points at the evidence |

---

## 🛠️ What This Repo Will Build

**Hypothesis testing**

- [ ] A permutation test from scratch, checked against a t-test
- [ ] A p-hacking simulation: 20 tests on pure noise, a correction applied, and a 200-word write-up
- [ ] A power analysis, verified by simulation

**Cleaning & reshaping**

- [ ] A genuinely messy public dataset, cleaned completely, with a reason next to every decision
- [ ] A reusable `data_quality_report(df)` function: missing values, unique counts, type problems, duplicates, outliers
- [ ] A slow groupby analysis rewritten vectorised, with the speedup recorded

**Charts**

- [ ] Eight chart types at publication quality, built with `fig, ax = plt.subplots()`
- [ ] One figure that argues a single finding
- [ ] A bad chart from the wild, reproduced and fixed, with a 150-word explanation
- [ ] `plotting_utils.py` — default style, colours, and a 300-dpi save function

**SQL**

- [x] Mode SQL Tutorial — all 52 lessons
- [ ] 15 business questions answered in SQL on a real multi-table dataset, ending with window functions
- [ ] One analysis done in both SQL and pandas, with a note on which was clearer

**The final analysis — a complete answer from real, messy public data**

- [ ] A question stated at the top, before any analysis
- [ ] Cleaning decisions documented with reasons
- [ ] Confidence intervals, not bare point estimates
- [ ] 5–8 publication-quality figures
- [ ] A conclusion that answers the question
- [ ] A limitations section: what the analysis cannot prove
- [ ] A README a stranger can follow to run it

---

## 🔗 How This Repo Connects to the Mathematics Repo

```text
   MATHEMATICS-FOR-DATA-SCIENCE                    FROM RAW DATA TO A REAL ANSWER
   (Month 1: the maths)                            (Month 2: the craft)

   CLT, standard error            ───────────►     t-tests (topic 06)
   Confidence intervals           ───────────►     "a CI that excludes 0 = significant"
   Bootstrap (resampling)         ───────────►     permutation tests (shuffling)
   Bayes' theorem, base rates     ───────────►     why p ≠ P(H0), FDR (topics 03, 12)
   Binomial distribution          ───────────►     coin-flip p-values (topic 04)
```

The Month 1 [StatQuest module](https://github.com/Yugalpoudel07/Mathematics-for-Data-Science/tree/main/StatQuest%20with%20Josh%20Starmer) is about *estimating honestly*; this repo's StatQuest set is about *deciding honestly*.

---

## 📂 Repository Organization

```text
From-Raw-Data-to-a-Real-Answer/
├── StatQuest - hypothesis testing set/              # [Notes written: 16/16 videos]
│   ├── README.md                                    # Topic index, build tasks & ML concepts
│   ├── 01-hypothesis-testing-and-the-null-hypothesis.md
│   ├── ...                                          # Topics 02 - 15
│   └── 16-type-2-errors.md
├── Khan Academy - Significance Tests/               # [Upcoming]
├── pandas - official User Guide/                    # [Upcoming]
├── Kaggle Learn - Pandas/                           # [Upcoming]
├── Kaggle Learn - Data Cleaning/                    # [Upcoming]
├── matplotlib - official tutorials/                 # [Upcoming]
├── seaborn - official tutorial/                     # [Upcoming]
├── Storytelling with Data (Cole Nussbaumer Knaflic)/# [Upcoming]
├── SQL Tutorial for Data Analysis (Mode  ThoughtSpot)/  # [Completed: 52/52 lessons]
│   ├── README.md                                    # Module overview & syllabus
│   └── practice-mode-tutorial/                      # 15 lesson-note files + index
├── A daily SQL practice platform/                   # [Upcoming]
├── LICENSE                                          # MIT License
└── README.md                                        # Main repository index (You are here)
```

---

## 🚀 Navigation & Study Guide

* Every StatQuest note has **top and bottom navigation** so you can read straight through.
* Start each StatQuest note at the **`[!TIP]` Core Intuition** callout, and fill in the **"My one line"** box yourself after watching the video.
* StatQuest Part V (p-hacking, FDR) maps directly onto the p-hacking simulation — watch it right before writing that code.
* The SQL notes' **Case 3 (A/B test validation)** is the practical twin of the StatQuest power and p-hacking topics — read them side by side.

---

*Authored as part of the Data Science Journey. Continuously updated as new modules are completed.*
