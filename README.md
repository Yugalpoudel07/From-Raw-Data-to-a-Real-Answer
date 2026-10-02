# 🔎 From Raw Data to a Real Answer

Taking messy real-world data to a defensible conclusion. Hypothesis testing (permutation tests, p-hacking simulation, power analysis), data cleaning in pandas, publication-quality matplotlib/seaborn charts, and SQL with window functions — ending in a complete, honest analysis of real public data.

[![Modules with notes](https://img.shields.io/badge/Modules_with_notes-7%20of%2010-brightgreen?style=flat-square)](#-learning-roadmap--curriculum-status)
[![StatQuest](https://img.shields.io/badge/StatQuest_Hypothesis_Testing-16%20of%2016%20notes-blue?style=flat-square)](StatQuest%20-%20hypothesis%20testing%20set/README.md)
[![SQL Tutorial](https://img.shields.io/badge/Mode%20SQL%20Tutorial-52%20of%2052%20lessons-blue?style=flat-square)](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/README.md)
[![pandas User Guide](https://img.shields.io/badge/pandas%20User%20Guide-7%20of%207%20notebooks-blue?style=flat-square)](pandas%20-%20official%20User%20Guide/README.md)
[![matplotlib tutorials](https://img.shields.io/badge/matplotlib%20tutorials-7%20of%207%20notebooks-blue?style=flat-square)](matplotlib%20-%20official%20tutorials/README.md)
[![seaborn tutorial](https://img.shields.io/badge/seaborn%20tutorial-13%20of%2013%20notebooks-blue?style=flat-square)](seaborn%20-%20official%20tutorial/README.md)
[![Kaggle Pandas](https://img.shields.io/badge/Kaggle%20Learn%20Pandas-Certified%20%C2%B7%206%20of%206-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](Kaggle%20Learn%20-%20Pandas/README.md)
[![Kaggle Data Cleaning](https://img.shields.io/badge/Kaggle%20Learn%20Data%20Cleaning-Certified%20%C2%B7%205%20of%205-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](Kaggle%20Learn%20-%20Data%20Cleaning/README.md)
[![Project P1](https://img.shields.io/badge/Project%20P1-NYC%20Restaurant%20Grades%20%C2%B7%20reproducible-brightgreen?style=flat-square)](P1%20-%20NYC%20Restaurant%20Grades/README.md)
[![Gate 2](https://img.shields.io/badge/Gate%202-worked%20solutions%20ready-orange?style=flat-square)](Gate%202%20-%20worked%20solutions/README.md)
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
| Clean | **[pandas — official User Guide](pandas%20-%20official%20User%20Guide/README.md)** | pandas docs | Indexing, Copy-on-Write, MultiIndex, merge/join, group by, reshaping, time series | ✅ **Completed** | **7 / 7 notebooks** |
| Clean | **[Kaggle Learn — Pandas](Kaggle%20Learn%20-%20Pandas/README.md)** | Kaggle | Six hands-on lessons with exercises | ✅ **Certified** 🏆 | **6 / 6 lessons** |
| Clean | **[Kaggle Learn — Data Cleaning](Kaggle%20Learn%20-%20Data%20Cleaning/README.md)** | Kaggle | Missing values, scaling, dates, encodings, inconsistent entries | ✅ **Certified** 🏆 | **5 / 5 lessons** |
| Show | **[matplotlib — official tutorials](matplotlib%20-%20official%20tutorials/README.md)** | matplotlib docs | Quick Start, the Artist tutorial, layout, arranging Axes, annotations, colormaps | ✅ **Completed** | **7 / 7 notebooks** |
| Show | **[seaborn — official tutorial](seaborn%20-%20official%20tutorial/README.md)** | seaborn docs | Axes- vs figure-level, `relplot`, `displot`, `catplot`, error bars, regression, grids, palettes, `heatmap` | ✅ **Completed** | **13 / 13 notebooks** |
| Show | **[Storytelling with Data](Storytelling%20with%20Data%20%28Cole%20Nussbaumer%20Knaflic%29/README.md)** | Cole Nussbaumer Knaflic | Chart choice, decluttering, focusing attention | ⏳ Upcoming | Planned |
| Query | **[SQL Tutorial for Data Analysis (Mode / ThoughtSpot)](SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/README.md)** | Mode / ThoughtSpot | `SELECT` to window functions, plus three product-analytics cases | ✅ **Completed** | **52 / 52 lessons** |
| Query | **A daily SQL practice platform** | DataLemur / StrataScratch / LeetCode | 30 minutes of timed SQL problems every study day | ⏳ Upcoming | Habit |
| **Ship** | **[Project P1 — Does an "A" Mean the Same Thing Twice?](P1%20-%20NYC%20Restaurant%20Grades/README.md)** | NYC Open Data (DOHMH) | Real messy data → documented cleaning → CIs → 7 figures → limitations | ✅ **Built & reproducible** | **2 notebooks · 7 figures** |
| **Gate** | **[Gate 2 — worked solutions](Gate%202%20-%20worked%20solutions/README.md)** | P1's tables in DuckDB | SQL window functions, a pandas groupby–merge–reshape chain, chart choice, artifact test | 📘 **Solutions ready** · gate still to sit | **3 notebooks + checklist** |

---

## 🍽️ Spotlight: Project P1 — Does an "A" Mean the Same Thing Twice?

> [!TIP]
> **The Month 2 project.** 300,000 rows of real NYC restaurant inspection data, cleaned with a reason next to every decision, analysed with restaurant-level bootstrap confidence intervals, and reproducible with one command (`python run_all.py`, checked from scratch in a fresh environment).  
> 👉 **[Read the P1 README](P1%20-%20NYC%20Restaurant%20Grades/README.md)** · **[Gate 2 worked solutions](Gate%202%20-%20worked%20solutions/README.md)**

**Question:** does an A in a New York restaurant's window mean the same thing whether it was earned at the first, unannounced inspection or only after a re-inspection?

**Answer: no.** About **3 in 10** A grades follow a failed surprise inspection. Those restaurants fail their **next** surprise inspection **51.6%** of the time vs **33.1%** for first-time A's: **+18.5 points (95% CI 17.5 to 19.5)**, in every borough.

<p align="center">
  <a href="P1%20-%20NYC%20Restaurant%20Grades/README.md"><img src="P1%20-%20NYC%20Restaurant%20Grades/figures/fig1_next_inspection_fail_rate.png" alt="Fail rate at the next surprise inspection: 33% for first-time A grades vs 52% for A grades earned on re-inspection" width="640"></a>
</p>

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

## 🌟 Spotlight: pandas — official User Guide (Completed)

> [!TIP]
> **Complete Notebooks Available:** The seven User Guide pages assigned for Week 6 are worked through in seven Jupyter notebooks, every example run with its output saved. The headings match the docs, so each notebook can be read next to the page it covers.  
> 👉 **[Explore the pandas Module Guide](pandas%20-%20official%20User%20Guide/README.md)**

### 📚 Notebook Breakdown

#### Selecting

* [**01 — Indexing and Selecting Data**](pandas%20-%20official%20User%20Guide/Notebook/01_Indexing%20and%20selecting%20data.ipynb) — `.loc` vs `.iloc`, boolean masks, `isin`, `where`/`mask`, `query()`.
* [**02 — Copy-on-Write**](pandas%20-%20official%20User%20Guide/Notebook/02_Copy%20on%20Write.ipynb) — Why `SettingWithCopyWarning` is gone in pandas 3.0 and chained assignment no longer works.
* [**03 — MultiIndex & Advanced Indexing**](pandas%20-%20official%20User%20Guide/Notebook/03_MultiIndex%20%26%20advanced%20indexing.ipynb) — `IndexSlice`, `xs()`, sorting levels, `cut`/`qcut`.

#### Combining

* [**04 — Merge, Join, Concatenate**](pandas%20-%20official%20User%20Guide/Notebook/04_Merge%20join%20concatenate.ipynb) — Every merge type, explained; `validate=` and `indicator=True` for checking merges; `merge_asof`, `compare()`.

#### Summarising & Reshaping

* [**05 — Group By: Split-Apply-Combine**](pandas%20-%20official%20User%20Guide/Notebook/05_Group%20by%20split-apply-combine.ipynb) — Named aggregation, `transform`, filtration, and why `apply` is the slow path.
* [**06 — Reshaping and Pivot Tables**](pandas%20-%20official%20User%20Guide/Notebook/06_Reshaping%20and%20pivot%20tables.ipynb) — `pivot_table`, `stack`/`unstack`, `melt` (long-form data for seaborn), `crosstab`.

#### Time

* [**07 — Time Series + Rolling Windows**](pandas%20-%20official%20User%20Guide/Notebook/07_Time%20series%20%20rolling%20windows.ipynb) — Parsing messy dates, `resample`, `shift`, time zones, rolling / expanding / EWM windows.

---

## 🏆 Spotlight: Kaggle Learn — Pandas (Certified)

> [!TIP]
> **Course completed with certificate (1 October 2026).** All six lessons done, every exercise check passed (**35 / 35**), mostly on the 130k-row Wine Reviews dataset.  
> 👉 **[Explore the Kaggle Pandas Module](Kaggle%20Learn%20-%20Pandas/README.md)**

<p align="center">
  <a href="Kaggle%20Learn%20-%20Pandas/README.md"><img src="Kaggle%20Learn%20-%20Pandas/kaggle-pandas-certificate.png" alt="Kaggle Learn Pandas certificate of completion, Yugal Poudel, 1 October 2026" width="520"></a>
</p>

| # | Lesson | Notebook | Checks |
| :-: | :--- | :--- | :-: |
| 1 | Creating, Reading and Writing | [01](Kaggle%20Learn%20-%20Pandas/Notebooks/01_creating-reading-and-writing.ipynb) | 5 / 5 |
| 2 | Indexing, Selecting & Assigning | [02](Kaggle%20Learn%20-%20Pandas/Notebooks/02_indexing-selecting-and-assigning.ipynb) | 9 / 9 |
| 3 | Summary Functions and Maps | [03](Kaggle%20Learn%20-%20Pandas/Notebooks/03_summary-functions-and-maps.ipynb) | 7 / 7 |
| 4 | Grouping and Sorting | [04](Kaggle%20Learn%20-%20Pandas/Notebooks/04_grouping-and-sorting.ipynb) | 6 / 6 |
| 5 | Data Types and Missing Values | [05](Kaggle%20Learn%20-%20Pandas/Notebooks/05_data-types-and-missing-values.ipynb) | 4 / 4 |
| 6 | Renaming and Combining | [06](Kaggle%20Learn%20-%20Pandas/Notebooks/06_renaming-and-combining.ipynb) | 4 / 4 |

---

## 🏆 Spotlight: Kaggle Learn — Data Cleaning (Certified)

> [!TIP]
> **Course completed with certificate (1 October 2026).** All five lessons done, every exercise check passed (**18 / 18**), each on a different real, messy dataset. The module README lists the cleaning decisions worth remembering and the three course lines that need updating for pandas 3.0.  
> 👉 **[Explore the Kaggle Data Cleaning Module](Kaggle%20Learn%20-%20Data%20Cleaning/README.md)**

<p align="center">
  <a href="Kaggle%20Learn%20-%20Data%20Cleaning/README.md"><img src="Kaggle%20Learn%20-%20Data%20Cleaning/kaggle-data-cleaning-certificate.png" alt="Kaggle Learn Data Cleaning certificate of completion, Yugal Poudel, 1 October 2026" width="520"></a>
</p>

| # | Lesson | Dataset | Notebook | Checks |
| :-: | :--- | :--- | :--- | :-: |
| 1 | Handling Missing Values | SF Building Permits | [01](Kaggle%20Learn%20-%20Data%20Cleaning/Notebooks/01_handling-missing-values.ipynb) | 6 / 6 |
| 2 | Scaling and Normalization | Kickstarter Projects | [02](Kaggle%20Learn%20-%20Data%20Cleaning/Notebooks/02_scaling-and-normalization.ipynb) | 2 / 2 |
| 3 | Parsing Dates | Significant Earthquakes | [03](Kaggle%20Learn%20-%20Data%20Cleaning/Notebooks/03_parsing-dates.ipynb) | 4 / 4 |
| 4 | Character Encodings | US Police Shootings | [04](Kaggle%20Learn%20-%20Data%20Cleaning/Notebooks/04_character-encodings.ipynb) | 3 / 3 |
| 5 | Inconsistent Data Entry | Pakistan Intellectual Capital | [05](Kaggle%20Learn%20-%20Data%20Cleaning/Notebooks/05_inconsistent-data-entry.ipynb) | 3 / 3 |

---

## 🌟 Spotlight: matplotlib — official tutorials (Completed)

> [!TIP]
> **Complete Notebooks Available:** The three core pages (Quick Start, the Artist tutorial, the layout guides) plus four bridge pages are worked through in seven notebooks, every example run with its output saved and every cell commented. All of it uses `fig, ax = plt.subplots()`.
> 👉 **[Explore the matplotlib Module Guide](matplotlib%20-%20official%20tutorials/README.md)**

* [**01 — Quick Start Guide**](matplotlib%20-%20official%20tutorials/Notebook/01_Quick%20start%20guide.ipynb) — Figure → Axes → Axis → Artist, OO vs pyplot, the `ax` helper-function pattern.
* [**02 — The Lifecycle of a Plot**](matplotlib%20-%20official%20tutorials/Notebook/02_The%20Lifecycle%20of%20a%20Plot.ipynb) — One chart from raw data to a saved PNG.
* [**03 — Artist Tutorial**](matplotlib%20-%20official%20tutorials/Notebook/03_Artist%20tutorial.ipynb) — Primitives vs containers, `get_*`/`set_*`, and the setters-only exercise.
* [**04 — Constrained & Tight Layout**](matplotlib%20-%20official%20tutorials/Notebook/04_Constrained%20and%20tight%20layout.ipynb) · [**05 — Arranging Multiple Axes**](matplotlib%20-%20official%20tutorials/Notebook/05_Arranging%20multiple%20Axes.ipynb) — Colorbars, legends outside, mosaics, small multiples.
* [**06 — Annotations**](matplotlib%20-%20official%20tutorials/Notebook/06_Annotations.ipynb) · [**07 — Choosing Colormaps**](matplotlib%20-%20official%20tutorials/Notebook/07_Choosing%20colormaps.ipynb) — The arrow that makes the argument, and why `jet` is wrong.

---

## 🌟 Spotlight: seaborn — official tutorial (Completed)

> [!TIP]
> **Complete Notebooks Available:** All 12 pages of the user guide and tutorial, plus the `heatmap` API page, in 13 notebooks with outputs saved. The docs' random seeds are kept, so the bootstrapped bands match the website.
> 👉 **[Explore the seaborn Module Guide](seaborn%20-%20official%20tutorial/README.md)**

| Part | Notebooks |
| :--- | :--- |
| How seaborn works | [01 Introduction](seaborn%20-%20official%20tutorial/Notebook/01_An%20introduction%20to%20seaborn.ipynb) · [02 ⭐ Axes- vs figure-level](seaborn%20-%20official%20tutorial/Notebook/02_Overview%20of%20plotting%20functions.ipynb) · [03 Long vs wide data](seaborn%20-%20official%20tutorial/Notebook/03_Data%20structures.ipynb) · [04 seaborn.objects](seaborn%20-%20official%20tutorial/Notebook/04_The%20seaborn.objects%20interface.ipynb) |
| Plotting functions | [05 Relationships](seaborn%20-%20official%20tutorial/Notebook/05_Visualizing%20statistical%20relationships.ipynb) · [06 ⭐ Distributions](seaborn%20-%20official%20tutorial/Notebook/06_Visualizing%20distributions.ipynb) · [07 Categorical](seaborn%20-%20official%20tutorial/Notebook/07_Visualizing%20categorical%20data.ipynb) |
| Statistics | [08 Error bars](seaborn%20-%20official%20tutorial/Notebook/08_Statistical%20estimation%20and%20error%20bars.ipynb) · [09 Regression fits](seaborn%20-%20official%20tutorial/Notebook/09_Estimating%20regression%20fits.ipynb) |
| Figures & style | [10 Multi-plot grids](seaborn%20-%20official%20tutorial/Notebook/10_Building%20structured%20multi-plot%20grids.ipynb) · [11 Aesthetics](seaborn%20-%20official%20tutorial/Notebook/11_Controlling%20figure%20aesthetics.ipynb) · [12 Colour palettes](seaborn%20-%20official%20tutorial/Notebook/12_Choosing%20color%20palettes.ipynb) · [13 `heatmap`](seaborn%20-%20official%20tutorial/Notebook/13_heatmap%20API%20page.ipynb) |

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

- [x] A genuinely messy public dataset, cleaned completely, with a reason next to every decision
- [x] A reusable `data_quality_report(df)` function: missing values, unique counts, type problems, duplicates, outliers
- [ ] A slow groupby analysis rewritten vectorised, with the speedup recorded

**Charts**

- [ ] Eight chart types at publication quality, built with `fig, ax = plt.subplots()`
- [x] One figure that argues a single finding
- [ ] A bad chart from the wild, reproduced and fixed, with a 150-word explanation
- [x] `plotting_utils.py` — default style, colours, and a 300-dpi save function

**SQL**

- [x] Mode SQL Tutorial — all 52 lessons
- [ ] 15 business questions answered in SQL on a real multi-table dataset, ending with window functions
- [x] One analysis done in both SQL and pandas, with a note on which was clearer

**The final analysis — a complete answer from real, messy public data** → [Project P1](P1%20-%20NYC%20Restaurant%20Grades/README.md)

- [x] A question stated at the top, before any analysis
- [x] Cleaning decisions documented with reasons
- [x] Confidence intervals, not bare point estimates
- [x] 5–8 publication-quality figures
- [x] A conclusion that answers the question
- [x] A limitations section: what the analysis cannot prove
- [x] A README a stranger can follow to run it

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
├── pandas - official User Guide/                    # [Completed: 7/7 notebooks]
│   ├── README.md                                    # Study guide: sections to read, skips, exercises
│   ├── Notebook/                                    # 01_Indexing ... 07_Time series (one per docs page)
│   └── Data/baseball.csv                            # Sample data used in the indexing notebook
├── Kaggle Learn - Pandas/                           # [Certified: 6/6 lessons]
│   ├── README.md                                    # Lessons, scores, certificate
│   ├── kaggle-pandas-certificate.png                # Certificate of completion
│   └── Notebooks/                                   # 01_creating-reading-and-writing ... 06_renaming-and-combining
├── Kaggle Learn - Data Cleaning/                    # [Certified: 5/5 lessons]
│   ├── README.md                                    # Lessons, datasets, scores, certificate
│   ├── kaggle-data-cleaning-certificate.png         # Certificate of completion
│   └── Notebooks/                                   # 01_handling-missing-values ... 05_inconsistent-data-entry
├── matplotlib - official tutorials/                 # [Completed: 7/7 notebooks]
│   ├── README.md                                    # Study guide: sections to read, skips, exercises
│   ├── Notebook/                                    # 01_Quick start guide ... 07_Choosing colormaps
│   └── Figures/                                     # PNGs saved by notebooks 02 and 04
├── seaborn - official tutorial/                     # [Completed: 13/13 notebooks]
│   ├── README.md                                    # Study guide: the 12 tutorial pages + heatmap
│   └── Notebook/                                    # 01_An introduction ... 13_heatmap API page
├── Storytelling with Data (Cole Nussbaumer Knaflic)/# [Study guide written]
├── SQL Tutorial for Data Analysis (Mode  ThoughtSpot)/  # [Completed: 52/52 lessons]
│   ├── README.md                                    # Module overview & syllabus
│   └── practice-mode-tutorial/                      # 15 lesson-note files + index
├── A daily SQL practice platform/                   # [Upcoming]
├── P1 - NYC Restaurant Grades/                      # [Project P1: built & reproducible]
│   ├── README.md                                    # Question, answer, how to run, cleaning, results, limitations
│   ├── run_all.py                                   # One command: download → clean → analyse
│   ├── notebooks/                                   # 01_data_quality_and_cleaning, 02_analysis_and_figures
│   ├── src/                                         # cleaning.py, analysis.py, plotting_utils.py, download_data.py
│   ├── figures/                                     # 7 figures, 300 dpi
│   └── results/                                     # key_numbers.json, robustness_checks.csv
├── Gate 2 - worked solutions/                       # [SQL, pandas, charts, artifact test]
├── docs/                                            # Month 2 Project Guide (Word report)
├── LICENSE                                          # MIT License
└── README.md                                        # Main repository index (You are here)
```

---

## 🚀 Navigation & Study Guide

* Every StatQuest note has **top and bottom navigation** so you can read straight through.
* Start each StatQuest note at the **`[!TIP]` Core Intuition** callout, and fill in the **"My one line"** box yourself after watching the video.
* StatQuest Part V (p-hacking, FDR) maps directly onto the p-hacking simulation — watch it right before writing that code.
* Each pandas notebook follows the headings of its User Guide page, so keep the docs page open beside it. Notebook 04's **validate= / indicator=True** template is the one to copy into every cleaning notebook.
* Do the Kaggle Pandas exercises *after* the matching User Guide notebook; the module README has a lesson-by-lesson map between the two.
* Before the final analysis, reread the **"Cleaning decisions worth remembering"** list in the Kaggle Data Cleaning README: it is the checklist for documenting every drop, fill and fix.
* Read matplotlib notebook 03 (Artist tutorial) before the seaborn notebooks: seaborn notebook 02 shows where seaborn hands you a matplotlib `Axes` (`ax=`) or a grid (`g.ax`, `g.axes`).
* The chart build tasks have worked examples to copy: argument figure → matplotlib 06, small multiples → matplotlib 05, histogram + density and ECDF → seaborn 06, scatter + trend → seaborn 09, correlation heatmap → seaborn 13.
* The SQL notes' **Case 3 (A/B test validation)** is the practical twin of the StatQuest power and p-hacking topics — read them side by side.

---

*Authored as part of the Data Science Journey. Continuously updated as new modules are completed.*
