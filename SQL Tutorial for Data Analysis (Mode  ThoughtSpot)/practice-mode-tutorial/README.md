[🏠 **Repository Home**](../../README.md) &nbsp;•&nbsp; [🗄️ **SQL Module Overview**](../README.md) &nbsp;•&nbsp; [**Start Reading: SELECT Basics** ⏭️](select_basics_notes.md)

---

# 📒 Mode SQL Tutorial — Lesson Notes

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)](#-progress)
[![Lessons](https://img.shields.io/badge/Lessons-52%20of%2052-blue?style=flat-square)](#-progress)
[![Files](https://img.shields.io/badge/Note_files-15-blue?style=flat-square)](#-files--basic-sql-15-lessons)

**Platform:** Mode Analytics (now part of ThoughtSpot) · [thoughtspot.com/sql-tutorial](https://www.thoughtspot.com/sql-tutorial) · [mode.com/sql-tutorial](https://mode.com/sql-tutorial)

---

## What This Folder Contains

Structured notes from the Mode SQL Tutorial — all 4 phases, 52 lessons, 15 note files. Each file contains syntax patterns, annotated queries against Mode's practice datasets, behavioural rules, and when-to-use guidance. Together they cover SQL from basic filtering, through real-world business case analysis, to window functions and performance tuning.

---

## 📄 Files — Basic SQL (15 lessons)

| File | Topics Covered |
| :--- | :--- |
| [`select_basics_notes.md`](select_basics_notes.md) | `SELECT`, column aliasing, `LIMIT`, `WHERE` introduction |
| [`filtering_operators_notes.md`](filtering_operators_notes.md) | Comparison operators, `BETWEEN`, `IN`, `LIKE`/`ILIKE`, `IS NULL`, arithmetic columns |
| [`logical_operators_notes.md`](logical_operators_notes.md) | `AND`, `OR`, `NOT`, operator precedence, `ORDER BY`, `GROUP BY`, SQL comments |

---

## 📄 Files — Intermediate SQL (20 lessons)

| File | Topics Covered |
| :--- | :--- |
| [`aggregate_functions_notes.md`](aggregate_functions_notes.md) | `COUNT`, `SUM`, `MIN`, `MAX`, `AVG`, `HAVING`, `COUNT(DISTINCT)` |
| [`joins_notes.md`](joins_notes.md) | `INNER`/`LEFT`/`RIGHT`/`FULL OUTER JOIN`, self join, `UNION`/`UNION ALL`, `WHERE` vs `ON`, multi-key joins, joins with comparison operators |
| [`distinct_and_case_notes.md`](distinct_and_case_notes.md) | `DISTINCT`, `COUNT(DISTINCT)`, `CASE` bucketing, conditional aggregation, `CASE` in `ORDER BY` |

---

## 📄 Files — SQL Analytics Training (8 lessons)

| File | Case | Business Question Answered |
| :--- | :-: | :--- |
| [`case1_drop_in_engagement_notes.md`](case1_drop_in_engagement_notes.md) | 1 | What caused the weekly engagement drop? |
| [`case2_search_functionality_notes.md`](case2_search_functionality_notes.md) | 2 | Is search worth improving, and what specifically should change? |
| [`case3_ab_test_validation_notes.md`](case3_ab_test_validation_notes.md) | 3 | Are these A/B test results valid before we ship? |
| [`core_principles_and_conclusion_notes.md`](core_principles_and_conclusion_notes.md) | All | The analytical framework connecting all three cases |

---

## 📄 Files — Advanced SQL (9 lessons)

| File | Topics Covered |
| :--- | :--- |
| [`data_types_and_dates_notes.md`](data_types_and_dates_notes.md) | Data types, `CAST`/`CONVERT`, integer-division trap, `EXTRACT`, `DATE_TRUNC`, date arithmetic, `TO_CHAR` |
| [`string_functions_and_wrangling_notes.md`](string_functions_and_wrangling_notes.md) | `LENGTH`, `TRIM`, `UPPER`/`LOWER`, `SUBSTRING`, `CONCAT`, `REPLACE`, `SPLIT_PART`, data cleaning patterns |
| [`subqueries_notes.md`](subqueries_notes.md) | Subqueries in `FROM`/`WHERE`/`SELECT`, `IN` vs `EXISTS`/`NOT EXISTS`, `NULL` trap, CTEs, subqueries vs joins |
| [`window_functions_notes.md`](window_functions_notes.md) | `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `NTILE`, window aggregates, running totals, moving averages |
| [`pivoting_and_performance_notes.md`](pivoting_and_performance_notes.md) | Pivoting via `CASE`, performance-tuning checklist |

---

## 📊 Datasets Used Across All Phases

* `tutorial.us_housing_units` — US regional housing construction data
* `tutorial.billboard_top_100_year_end` — Billboard year-end top 100 charts
* `tutorial.aapl_historical_stock_price` — Apple historical stock prices
* `tutorial.crunchbase_companies` / `tutorial.crunchbase_investments` — startup company and investment records
* `tutorial.yammer_users` / `tutorial.yammer_events` / `tutorial.yammer_emails` / `tutorial.yammer_experiments` — Yammer product analytics data (SQL Analytics Training)

---

## ✅ Progress

- [x] Basic SQL — 15 lessons
- [x] Intermediate SQL — 20 lessons
- [x] SQL Analytics Training — 8 lessons
- [x] Advanced SQL — 9 lessons

**Mode SQL Tutorial: 100% complete — 52 lessons across 15 note files.**

---

[🏠 **Repository Home**](../../README.md) &nbsp;•&nbsp; [🗄️ **SQL Module Overview**](../README.md) &nbsp;•&nbsp; [**Start Reading: SELECT Basics** ⏭️](select_basics_notes.md)
