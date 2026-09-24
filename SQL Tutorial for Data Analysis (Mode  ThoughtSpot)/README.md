[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [📒 **Lesson Notes Index**](practice-mode-tutorial/README.md) &nbsp;•&nbsp; [**Start Reading: SELECT Basics** ⏭️](practice-mode-tutorial/select_basics_notes.md)

---

# 🗄️ SQL Tutorial for Data Analysis — Mode / ThoughtSpot

### *Getting Data Out of a Database, and Using It to Answer a Business Question*

[![Status: Completed](https://img.shields.io/badge/Status-100%25_Completed-brightgreen?style=flat-square)](#-lesson-directory--syllabus)
[![Lessons](https://img.shields.io/badge/Lessons-52%20of%2052-blue?style=flat-square)](#-lesson-directory--syllabus)
[![Notes](https://img.shields.io/badge/Note_files-15-blue?style=flat-square)](practice-mode-tutorial/README.md)
[![Platform](https://img.shields.io/badge/Platform-Mode%20%2F%20ThoughtSpot-orange?style=flat-square)](https://www.thoughtspot.com/sql-tutorial)
[![Focus](https://img.shields.io/badge/Focus-Analytical_SQL-purple?style=flat-square)](#)

> [!NOTE]
> **About this Tutorial:**
> Mode's **SQL Tutorial for Data Analysis** is a free, structured course that runs from `SELECT` to window functions, with a browser query editor and real practice datasets. Mode was acquired by ThoughtSpot, so the tutorial now lives on both domains; the [ThoughtSpot copy](https://www.thoughtspot.com/sql-tutorial) is the more recently maintained one.
>
> Beyond syntax, its **SQL Analytics Training** section works through three realistic product-analytics cases on Yammer data — an engagement drop, a search feature review, and an A/B test validation. Those cases are where SQL turns into analysis: forming hypotheses first, segmenting before concluding, and checking whether the data can support the claim.

---

## 🗺️ Lesson Directory & Syllabus

All 52 lessons across four phases are complete, written up in 15 note files inside [`practice-mode-tutorial/`](practice-mode-tutorial/README.md). Each file has syntax patterns, annotated queries against Mode's datasets, behavioural rules, and when-to-use guidance.

#### Phase 1 — Basic SQL (15 lessons)

| Notes | Topics Covered |
| :--- | :--- |
| [**SELECT, LIMIT, WHERE**](practice-mode-tutorial/select_basics_notes.md) | `SELECT`, column aliasing, `LIMIT`, introduction to `WHERE` |
| [**Filtering Operators**](practice-mode-tutorial/filtering_operators_notes.md) | Comparison operators, `BETWEEN`, `IN`, `LIKE`/`ILIKE`, `IS NULL`, arithmetic columns |
| [**Logical Operators & ORDER BY**](practice-mode-tutorial/logical_operators_notes.md) | `AND`, `OR`, `NOT`, operator precedence, `ORDER BY`, `GROUP BY`, comments |

#### Phase 2 — Intermediate SQL (20 lessons)

| Notes | Topics Covered |
| :--- | :--- |
| [**Aggregate Functions**](practice-mode-tutorial/aggregate_functions_notes.md) | `COUNT`, `SUM`, `MIN`, `MAX`, `AVG`, `HAVING`, `COUNT(DISTINCT)` |
| [**Joins**](practice-mode-tutorial/joins_notes.md) | `INNER`/`LEFT`/`RIGHT`/`FULL OUTER JOIN`, self join, `UNION`/`UNION ALL`, `WHERE` vs `ON`, multi-key joins, joins on comparison operators |
| [**DISTINCT and CASE**](practice-mode-tutorial/distinct_and_case_notes.md) | `DISTINCT`, `CASE` bucketing, conditional aggregation, `CASE` in `ORDER BY` |

#### Phase 3 — SQL Analytics Training (8 lessons)

| Notes | Case | Business Question |
| :--- | :-: | :--- |
| [**Investigating a Drop in User Engagement**](practice-mode-tutorial/case1_drop_in_engagement_notes.md) | 1 | What caused the weekly engagement drop? |
| [**Analyzing In-Product Search**](practice-mode-tutorial/case2_search_functionality_notes.md) | 2 | Is search worth improving, and what specifically should change? |
| [**Validating A/B Test Results**](practice-mode-tutorial/case3_ab_test_validation_notes.md) | 3 | Are these A/B test results valid before we ship? |
| [**Core Principles & Conclusion**](practice-mode-tutorial/core_principles_and_conclusion_notes.md) | All | The analytical discipline connecting the three cases |

#### Phase 4 — Advanced SQL (9 lessons)

| Notes | Topics Covered |
| :--- | :--- |
| [**Data Types & Dates**](practice-mode-tutorial/data_types_and_dates_notes.md) | Data types, `CAST`/`CONVERT`, the integer-division trap, `EXTRACT`, `DATE_TRUNC`, date arithmetic, `TO_CHAR` |
| [**String Functions & Data Wrangling**](practice-mode-tutorial/string_functions_and_wrangling_notes.md) | `LENGTH`, `TRIM`, `UPPER`/`LOWER`, `SUBSTRING`, `CONCAT`, `REPLACE`, `SPLIT_PART`, cleaning patterns |
| [**Subqueries**](practice-mode-tutorial/subqueries_notes.md) | Subqueries in `FROM`/`WHERE`/`SELECT`, `IN` vs `EXISTS`/`NOT EXISTS`, the `NULL` trap, CTEs, subqueries vs joins |
| [**Window Functions**](practice-mode-tutorial/window_functions_notes.md) | `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `NTILE`, window aggregates, running totals, frames |
| [**Pivoting & Performance**](practice-mode-tutorial/pivoting_and_performance_notes.md) | Pivoting with `CASE` + aggregates, performance-tuning checklist |

---

## 🧠 How the Phases Build

```text
   ┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
   │   BASIC              │   │   INTERMEDIATE       │   │   ADVANCED           │
   │   pick rows and      │──►│   summarise and      │──►│   reshape, rank,     │
   │   columns            │   │   combine tables     │   │   and compare rows   │
   │   SELECT / WHERE     │   │   GROUP BY / JOIN    │   │   windows / CTEs     │
   └──────────────────────┘   └──────────┬───────────┘   └──────────────────────┘
                                         │
                                         ▼
                            ┌──────────────────────────┐
                            │   ANALYTICS TRAINING      │
                            │   hypotheses first,       │
                            │   segment, then conclude  │
                            │   (3 Yammer cases)        │
                            └──────────────────────────┘
```

1. **Filter, then aggregate, then compare.** Most analytical queries are `WHERE` → `GROUP BY` → a comparison across groups or time.
2. **Joins change row counts.** Knowing what each join type does to the number of rows is the difference between a right answer and a silently inflated one.
3. **Window functions compare rows without collapsing them.** Rankings, running totals, and "previous event" logic (`LAG`) — the part that separates *can use SQL* from *good at SQL*.
4. **The query is not the analysis.** The Yammer cases show the real work: rule out tracking problems, form hypotheses before querying, and segment before concluding.

---

## 🛠️ Skills Demonstrated

`SELECT` · `WHERE` · `LIMIT` · `ORDER BY` · `GROUP BY` · `HAVING` · `AND/OR/NOT` · `BETWEEN` · `IN` · `LIKE/ILIKE` · `IS NULL` · `COUNT/SUM/MIN/MAX/AVG` · `DISTINCT` · `CASE` · `INNER/LEFT/RIGHT/FULL JOIN` · self join · `UNION/UNION ALL` · multi-key joins · subqueries · `EXISTS/NOT EXISTS` · CTEs · `ROW_NUMBER/RANK/DENSE_RANK` · `LAG/LEAD` · `NTILE` · window aggregates · running totals · `CAST` · date functions · string functions · pivoting · performance tuning · cohort analysis · session analysis · A/B test validation

---

## 📊 Datasets Used

| Dataset | Used In |
| :--- | :--- |
| `tutorial.us_housing_units` | SELECT basics, filtering operators, dates |
| `tutorial.billboard_top_100_year_end` | Logical operators, aggregates, `DISTINCT`/`CASE`, strings, subqueries, windows, pivoting |
| `tutorial.aapl_historical_stock_price` | Aggregates, `DISTINCT`/`CASE`, dates, subqueries, window functions, pivoting |
| `tutorial.crunchbase_companies`, `tutorial.crunchbase_investments` | Joins, subqueries, string wrangling |
| `tutorial.yammer_users`, `yammer_events`, `yammer_emails`, `yammer_experiments` | The three SQL Analytics Training cases |

---

## 🔗 How This Fits the Repository

* **SQL is how the raw data comes out of a database.** The pandas modules in this repo reshape it; SQL is usually where it starts.
* **Case 3 (A/B test validation)** is the practical side of the [StatQuest hypothesis testing set](../StatQuest%20-%20hypothesis%20testing%20set/README.md) — group balance, the primary metric, novelty effects and post-hoc rationalisation are the same ideas as power, p-hacking and multiple testing, seen from inside a company's data.
* **Next SQL steps** (tracked in the main README): answer 15 business questions on a real multi-table dataset, ending with window functions; keep a daily SQL practice habit; and do one analysis in both SQL and pandas.

---

## 📺 Source Material

* **Tutorial (current):** [thoughtspot.com/sql-tutorial](https://www.thoughtspot.com/sql-tutorial)
* **Tutorial (original):** [mode.com/sql-tutorial](https://mode.com/sql-tutorial)
* **Reference:** [PostgreSQL — Window Functions tutorial](https://www.postgresql.org/docs/current/tutorial-window.html)

---

[🏠 **Back to Main Repository**](../README.md) &nbsp;•&nbsp; [📒 **Lesson Notes Index**](practice-mode-tutorial/README.md) &nbsp;•&nbsp; [**Start with SELECT Basics** ⏭️](practice-mode-tutorial/select_basics_notes.md)
