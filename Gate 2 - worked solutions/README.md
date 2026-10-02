[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [⏮️ **P1 — NYC Restaurant Grades**](../P1%20-%20NYC%20Restaurant%20Grades/README.md)

---

# 🚦 Gate 2 — Worked Solutions

### *SQL, pandas, chart choice and the artifact test, all worked through on P1's data*

[![SQL](https://img.shields.io/badge/SQL-3%20queries%20%2B%20bonus-blue?style=flat-square)](01_SQL%20-%20three%20queries%20with%20window%20functions.ipynb)
[![pandas](https://img.shields.io/badge/pandas-groupby%E2%86%92merge%E2%86%92reshape-150458?style=flat-square)](02_pandas%20-%20groupby%20merge%20reshape.ipynb)
[![Charts](https://img.shields.io/badge/Charts-3%20questions-purple?style=flat-square)](03_Charts%20-%20choosing%20the%20right%20chart.ipynb)
[![Artifact](https://img.shields.io/badge/Artifact%20test-clean%20run%20passed%20%C2%B7%20person%20test%20open-orange?style=flat-square)](04_Artifact%20test.md)

> [!IMPORTANT]
> **What this folder is, and isn't.** The roadmap's Gate 2 is a **closed-book, 90-minute test you sit yourself**. These are **worked solutions** to Gate-2-style questions, written as study material. Reading them doesn't pass the gate; sitting a fresh version timed, without notes, does. The best way to use them: read a question, close the notebook, answer it with a timer running, then compare.

## The gate (from the roadmap, Week 8)

| Part | Time | Task | Worked solution |
| :-: | :-: | :-- | :-- |
| 1 | 45 min | **SQL, no reference:** three queries, at least one using a window function with a partition | [`01_SQL`](01_SQL%20-%20three%20queries%20with%20window%20functions.ipynb) |
| 2 | 20 min | **pandas:** given a described dataset, write the groupby → merge → reshape chain that answers a question | [`02_pandas`](02_pandas%20-%20groupby%20merge%20reshape.ipynb) |
| 3 | 10 min | **Charts:** given a question, name the right chart and justify it against two alternatives | [`03_Charts`](03_Charts%20-%20choosing%20the%20right%20chart.ipynb) |
| 4 | — | **Artifact test:** someone with no context runs P1 and tells you the finding | [`04_Artifact test`](04_Artifact%20test.md) |

## What's inside

### 1 · SQL (DuckDB, on P1's three tables)
- **Q1** joins + `GROUP BY` + `HAVING`: the 10 cuisines with the worst surprise-inspection scores, plus a row-count check that the join kept every inspection.
- **Q2** `LAG() OVER (PARTITION BY camis ORDER BY date)`: how long the city waits before the next surprise inspection after an A, B or C-range score (about 381 vs 235 vs 217 days), and proof of what goes wrong without `PARTITION BY`.
- **Q3** `RANK() OVER (PARTITION BY boro ...)` in a CTE, filtered in the outer query: the top 3 cuisines by failure rate in each borough. Also `ROW_NUMBER` vs `RANK` vs `DENSE_RANK`.
- **Bonus:** P1's headline result rebuilt in SQL with `LEAD` and a named `WINDOW`. It **matches the pandas result exactly** (33.13% vs 51.63%), with a short note on which was clearer. That's the roadmap's "do one analysis in both SQL and pandas" task.
- Plus the logical execution order (`FROM` → `WHERE` → `GROUP BY` → `HAVING` → window → `SELECT` → `ORDER BY`) and why it means you can't use an alias in `WHERE`.

### 2 · pandas
"What % of surprise inspections cited at least one critical violation, by borough and year?" as one method chain: **groupby** (violations → one row per inspection) → **merge** ×2 with `validate=` → **groupby** → **unstack**. Then the `indicator=True` check, how much an inner join would have **inflated** the answer, and the same result with `pivot_table`.

### 3 · Charts
Three questions, each drawn as **the right chart next to the two alternatives it beats**:
- distributions across boroughs → box plots (not mean bars, not overlapping histograms);
- a trend over 4 years → a line with a 95% band (not 48 bars, not pies per year). The line also reveals a seasonal cycle the others hide;
- a numeric predictor and a yes/no outcome → binned rates with CIs (not a raw 0/1 scatter, not one correlation coefficient).

Ends with a 60-second answer template and a question-type → chart table.

### 4 · Artifact test
- ✅ **Clean-machine check, done:** P1 was copied without its data into a brand-new virtual environment, and the README's two commands (`pip install -r requirements.txt`, `python run_all.py`) reproduced every number identically in 71 seconds.
- ⏳ **Person test, still yours to do:** a checklist to send a tester, a grading table, and a log to fill in.

## ▶️ Running these notebooks

They read P1's processed data, so build P1 first:

```bash
cd "../P1 - NYC Restaurant Grades"
pip install -r requirements.txt
python run_all.py
```

Then open the notebooks here in Jupyter. All three were run on 2 October 2026 with pandas 3.0.2, duckdb 1.5.6, matplotlib 3.11.2 and seaborn 0.13.2, and their outputs are saved.

## Gate 2 status

| Part | Status |
| :-- | :-- |
| 1 SQL | 📘 worked solutions ready; ☐ sit a timed, closed-book attempt |
| 2 pandas | 📘 worked solution ready; ☐ sit a timed attempt |
| 3 Charts | 📘 worked solutions ready; ☐ answer 3 new questions out loud, 10 min |
| 4 Artifact test | ✅ clean-machine run passed; ☐ person with no context runs P1 and states the finding |
