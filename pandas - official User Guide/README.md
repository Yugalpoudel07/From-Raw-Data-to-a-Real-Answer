[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [**Next module: matplotlib** ⏭️](../matplotlib%20-%20official%20tutorials/README.md)

---

# 🐼 pandas — official User Guide (Week 6)

### *The exact sections to read, in order, and what to do with each one*

[![Time](https://img.shields.io/badge/Time_budget-8_hrs-blue?style=flat-square)](#)
[![Version](https://img.shields.io/badge/pandas-3.0.x-150458?style=flat-square)](https://pandas.pydata.org/docs/user_guide/index.html)
[![Steps](https://img.shields.io/badge/Steps-7_parts-purple?style=flat-square)](#-the-study-path)
[![Status](https://img.shields.io/badge/Status-Completed_7%2F7_notebooks-brightgreen?style=flat-square)](#-notebooks)

> [!NOTE]
> **Roadmap assignment:** Indexing and selecting data · Merge/join/concatenate · Group By · Reshaping and pivot tables · Time series. **Skip everything else** and use it later as a lookup reference.
> **What you produce:** type every example into *your own messy dataset*, not a scratch cell.
>
> The User Guide is ~30 pages long and each page is huge. This file tells you **which headings inside each page** to read and which to skip. Every link below jumps straight to the heading.

> [!TIP]
> **Status: completed.** All 7 parts are worked through in Jupyter notebooks, one per page, with every example run and its output saved. 👉 **[Jump to the notebooks](#-notebooks)** · Graded practice: **[Kaggle Learn — Pandas](../Kaggle%20Learn%20-%20Pandas/README.md)** 🏆

> [!IMPORTANT]
> **pandas 3.0 changed one thing in the roadmap.** Week 6 says *"learn what causes `SettingWithCopyWarning`"*. In pandas 3.0 **Copy-on-Write is the only mode**, so that warning is gone. Chained assignment like `df[df.a > 0]["b"] = 1` now **never works** and gives a `ChainedAssignmentError` warning instead. Part 2 below covers this (15 minutes). Check your version with `pd.__version__`.

---

## 🗺️ The study path

| Part | Page | Time | Notebook | Status |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Indexing and selecting data | 1 h 15 | [`01`](Notebook/01_Indexing%20and%20selecting%20data.ipynb) | ✅ |
| 2 | Copy-on-Write *(replaces the SettingWithCopyWarning topic)* | 15 min | [`02`](Notebook/02_Copy%20on%20Write.ipynb) | ✅ |
| 3 | MultiIndex / advanced indexing | 45 min | [`03`](Notebook/03_MultiIndex%20%26%20advanced%20indexing.ipynb) | ✅ |
| 4 | Merge, join, concatenate | 1 h 15 | [`04`](Notebook/04_Merge%20join%20concatenate.ipynb) | ✅ |
| 5 | Group by: split-apply-combine | 2 h | [`05`](Notebook/05_Group%20by%20split-apply-combine.ipynb) | ✅ |
| 6 | Reshaping and pivot tables | 1 h | [`06`](Notebook/06_Reshaping%20and%20pivot%20tables.ipynb) | ✅ |
| 7 | Time series + windowing (rolling) | 1 h 30 | [`07`](Notebook/07_Time%20series%20%20rolling%20windows.ipynb) | ✅ |
| | **Total** | **8 h** | **7 notebooks** | ✅ **7 / 7** |

---

## 📓 Notebooks

One notebook per page, in study order. Headings follow the User Guide headings, so each notebook can be read next to the docs page it covers.

| # | Notebook | What's inside |
| :-: | :--- | :--- |
| 01 | [Indexing and selecting data](Notebook/01_Indexing%20and%20selecting%20data.ipynb) | `.loc` / `.iloc` / `[]`, label vs position slicing, callables, reindexing, boolean masks, `isin`, `where` / `mask`, `query()`; method chaining on [`baseball.csv`](Data/baseball.csv) |
| 02 | [Copy-on-Write](Notebook/02_Copy%20on%20Write.ipynb) | The old view/copy problem, why chained assignment no longer works, patterns to avoid |
| 03 | [MultiIndex & advanced indexing](Notebook/03_MultiIndex%20%26%20advanced%20indexing.ipynb) | Building a MultiIndex, `pd.IndexSlice`, `xs()`, `swaplevel`, sorting (and the `UnsortedIndexError` you get without it), `cut` / `qcut` |
| 04 | [Merge, join, concatenate](Notebook/04_Merge%20join%20concatenate.ipynb) | `concat`, all five merge types, ⭐ `validate=` and ⭐ `indicator=True`, `join`, `merge_asof`, `compare()`; every example has an *Explained* / *What happened* note, plus a merge-checking template and a cheat sheet |
| 05 | [Group by: split-apply-combine](Notebook/05_Group%20by%20split-apply-combine.ipynb) | Splitting (and `dropna`), iterating, aggregation, ⭐ named aggregation, ⭐ `transform`, `groupby().rolling()`, filtration, flexible `apply`, unobserved categoricals, `head` / `nth` per group |
| 06 | [Reshaping and pivot tables](Notebook/06_Reshaping%20and%20pivot%20tables.ipynb) | `pivot` vs `pivot_table`, `stack` / `unstack`, ⭐ `melt` / `wide_to_long`, `crosstab` with normalisation, `cut`, `get_dummies` / `from_dummies`, `explode` |
| 07 | [Time series + rolling windows](Notebook/07_Time%20series%20%20rolling%20windows.ipynb) | `to_datetime` (formats, `errors="coerce"`), `date_range`, partial string indexing, `.dt` components, `shift`, ⭐ `resample`, time zones; then the windowing page: rolling (centred and `"7D"`), expanding, EWM |

> [!NOTE]
> A few cells end in an error **on purpose**: they reproduce the "this raises" examples from the docs (out-of-bounds `.iloc`, reindexing on duplicate labels, an unsorted MultiIndex, a failed `validate=` check, an unparseable date with `errors="raise"`). The error output is left in so you can see what pandas says.

---

### Part 1 — Indexing and selecting data · 1 h 15
📄 https://pandas.pydata.org/docs/user_guide/indexing.html

- [x] 1. [Different choices for indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#different-choices-for-indexing): the three accessors — `.loc` (labels), `.iloc` (positions), `[]`. Learn which one to use when.
- [x] 2. [Basics](https://pandas.pydata.org/docs/user_guide/indexing.html#basics): `df[col]`, `df[[col1, col2]]`, swapping columns.
- [x] 3. [Selection by label](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label) + [Slicing with labels](https://pandas.pydata.org/docs/user_guide/indexing.html#slicing-with-labels): **`.loc` slices include the end label**, `.iloc` slices do not.
- [x] 4. [Selection by position](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-position): `.iloc[rows, cols]`, out-of-range behaviour.
- [x] 5. [Selection by callable](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-callable): `df.loc[lambda d: d.x > 0]`, used in method chains.
- [x] 6. [Combining positional and label-based indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#combining-positional-and-label-based-indexing) and [Reindexing](https://pandas.pydata.org/docs/user_guide/indexing.html#reindexing).
- [x] 7. [Boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing): masks with `&`, `|`, `~`, and **brackets around every condition**.
- [x] 8. [Indexing with isin](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-with-isin).
- [x] 9. [The where() Method and Masking](https://pandas.pydata.org/docs/user_guide/indexing.html#the-where-method-and-masking) + [Mask](https://pandas.pydata.org/docs/user_guide/indexing.html#mask).
- [x] 10. [The query() Method](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method): `df.query("age > 30 and city == @c")`.

**Skip:** Attribute access, Selecting random samples, Setting with enlargement, Setting with enlargement conditionally. Skim [Fast scalar value getting and setting](https://pandas.pydata.org/docs/user_guide/indexing.html#fast-scalar-value-getting-and-setting) (`.at` / `.iat`).

**On your dataset:** write the same filter three ways (a mask with `.loc`, `.query()`, and `.where()`) and check the row counts match.

---

### Part 2 — Copy-on-Write · 15 min
📄 https://pandas.pydata.org/docs/user_guide/copy_on_write.html

- [x] 1. [Previous behavior](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#previous-behavior): why the old view/copy confusion caused `SettingWithCopyWarning`.
- [x] 2. [Chained Assignment](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#chained-assignment): why `df[mask]["col"] = v` now does nothing.
- [x] 3. [Patterns to avoid](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#patterns-to-avoid).

**Rule to remember:** set values in one step with `df.loc[mask, "col"] = v`.

---

### Part 3 — MultiIndex / advanced indexing · 45 min
📄 https://pandas.pydata.org/docs/user_guide/advanced.html
*(Roadmap Week 6: "Index and MultiIndex — the thing everyone skips and then suffers for".)*

- [x] 1. [Creating a MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html#creating-a-multiindex-hierarchical-index-object): `from_tuples`, `from_product`, `set_index([a, b])`.
- [x] 2. [Basic indexing on axis with MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html#basic-indexing-on-axis-with-multiindex).
- [x] 3. [Using slicers](https://pandas.pydata.org/docs/user_guide/advanced.html#using-slicers): `pd.IndexSlice`.
- [x] 4. [Cross-section](https://pandas.pydata.org/docs/user_guide/advanced.html#cross-section): `df.xs(key, level=...)`.
- [x] 5. [Swapping levels](https://pandas.pydata.org/docs/user_guide/advanced.html#swapping-levels-with-swaplevel) and [Sorting a MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html#sorting-a-multiindex): an unsorted index gives a `PerformanceWarning`.
- [x] 6. [Binning data with cut and qcut](https://pandas.pydata.org/docs/user_guide/advanced.html#binning-data-with-cut-and-qcut).

**Skip:** Defined levels, Take methods, CategoricalIndex/RangeIndex/IntervalIndex details, the FAQ. Glance at [Endpoints are inclusive](https://pandas.pydata.org/docs/user_guide/advanced.html#endpoints-are-inclusive).

---

### Part 4 — Merge, join, concatenate · 1 h 15
📄 https://pandas.pydata.org/docs/user_guide/merging.html

- [x] 1. [concat()](https://pandas.pydata.org/docs/user_guide/merging.html#concat): [Joining logic of the resulting axis](https://pandas.pydata.org/docs/user_guide/merging.html#joining-logic-of-the-resulting-axis), [Ignoring indexes](https://pandas.pydata.org/docs/user_guide/merging.html#ignoring-indexes-on-the-concatenation-axis), [Resulting keys](https://pandas.pydata.org/docs/user_guide/merging.html#resulting-keys).
- [x] 2. [merge()](https://pandas.pydata.org/docs/user_guide/merging.html#merge) → [Merge types](https://pandas.pydata.org/docs/user_guide/merging.html#merge-types): `inner`, `left`, `right`, `outer`, `cross`.
- [x] 3. ⭐ [Merge key uniqueness](https://pandas.pydata.org/docs/user_guide/merging.html#merge-key-uniqueness): the `validate="one_to_one" / "one_to_many" / "many_to_one"` argument. **This is the roadmap's "validate every merge" rule.**
- [x] 4. ⭐ [Merge result indicator](https://pandas.pydata.org/docs/user_guide/merging.html#merge-result-indicator): `indicator=True` shows which rows matched.
- [x] 5. [Overlapping value columns](https://pandas.pydata.org/docs/user_guide/merging.html#overlapping-value-columns): `suffixes=`.
- [x] 6. [DataFrame.join()](https://pandas.pydata.org/docs/user_guide/merging.html#dataframe-join): read only the first part (joining on the index).
- [x] 7. [merge_asof()](https://pandas.pydata.org/docs/user_guide/merging.html#merge-asof): "nearest earlier timestamp" joins.
- [x] 8. [compare()](https://pandas.pydata.org/docs/user_guide/merging.html#compare): shows what changed between two versions of a frame (useful for checking your cleaning).

**Skip:** joins with two MultiIndexes, `combine_first`, `merge_ordered`.

**On your dataset:** for every merge, print `len()` before and after, pass `validate=` and `indicator=True`, then run `value_counts()` on `_merge`.

---

### Part 5 — Group by: split-apply-combine · 2 h *(the most important page)*
📄 https://pandas.pydata.org/docs/user_guide/groupby.html

- [x] 1. [Splitting an object into groups](https://pandas.pydata.org/docs/user_guide/groupby.html#splitting-an-object-into-groups), including [GroupBy dropna](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-dropna): **NaN keys are dropped by default**.
- [x] 2. [Iterating through groups](https://pandas.pydata.org/docs/user_guide/groupby.html#iterating-through-groups) and [Selecting a group](https://pandas.pydata.org/docs/user_guide/groupby.html#selecting-a-group) (`get_group`).
- [x] 3. [Aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#aggregation): [Built-in aggregation methods](https://pandas.pydata.org/docs/user_guide/groupby.html#built-in-aggregation-methods) and [The aggregate() method](https://pandas.pydata.org/docs/user_guide/groupby.html#the-aggregate-method).
- [x] 4. ⭐ [Named aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#named-aggregation): `agg(total=("sales", "sum"), n=("id", "count"))`, the clean way to name output columns.
- [x] 5. [Applying different functions to DataFrame columns](https://pandas.pydata.org/docs/user_guide/groupby.html#applying-different-functions-to-dataframe-columns).
- [x] 6. ⭐ [Transformation](https://pandas.pydata.org/docs/user_guide/groupby.html#transformation) + [The transform() method](https://pandas.pydata.org/docs/user_guide/groupby.html#the-transform-method): returns a result **the same length as the input**, e.g. share of group total, or filling NaN with the group mean.
- [x] 7. [Window and resample operations](https://pandas.pydata.org/docs/user_guide/groupby.html#window-and-resample-operations): `groupby().rolling()`.
- [x] 8. [Filtration](https://pandas.pydata.org/docs/user_guide/groupby.html#filtration): drop groups that are too small.
- [x] 9. [Flexible apply](https://pandas.pydata.org/docs/user_guide/groupby.html#flexible-apply): read *why* it is slow. It runs Python once per group. Try `agg`/`transform` first.
- [x] 10. [Handling of (un)observed Categorical values](https://pandas.pydata.org/docs/user_guide/groupby.html#handling-of-unobserved-categorical-values) and [Taking the first rows of each group](https://pandas.pydata.org/docs/user_guide/groupby.html#taking-the-first-rows-of-each-group).

**Skip:** Numba accelerated routines, grouping with ordered factors, enumerate groups, plotting.

**On your dataset:** this is **build task 3**. Write one group statistic with `.apply(lambda g: ...)`, rewrite it with `agg`/`transform`, time both with `%timeit`, and record the speedup.

---

### Part 6 — Reshaping and pivot tables · 1 h
📄 https://pandas.pydata.org/docs/user_guide/reshaping.html

- [x] 1. [pivot()](https://pandas.pydata.org/docs/user_guide/reshaping.html#pivot) vs [pivot_table()](https://pandas.pydata.org/docs/user_guide/reshaping.html#pivot-table): `pivot` fails on duplicate keys, `pivot_table` aggregates them. Plus [Adding margins](https://pandas.pydata.org/docs/user_guide/reshaping.html#adding-margins).
- [x] 2. [stack() and unstack()](https://pandas.pydata.org/docs/user_guide/reshaping.html#stack-and-unstack): [Multiple levels](https://pandas.pydata.org/docs/user_guide/reshaping.html#multiple-levels) and [Missing data](https://pandas.pydata.org/docs/user_guide/reshaping.html#missing-data).
- [x] 3. ⭐ [melt() and wide_to_long()](https://pandas.pydata.org/docs/user_guide/reshaping.html#melt-and-wide-to-long): wide → long. **seaborn needs long-form data**, so you will use this every week.
- [x] 4. [crosstab()](https://pandas.pydata.org/docs/user_guide/reshaping.html#crosstab) + [Normalization](https://pandas.pydata.org/docs/user_guide/reshaping.html#normalization): frequency tables and row/column percentages.
- [x] 5. [cut()](https://pandas.pydata.org/docs/user_guide/reshaping.html#cut), [get_dummies()](https://pandas.pydata.org/docs/user_guide/reshaping.html#get-dummies-and-from-dummies), [explode()](https://pandas.pydata.org/docs/user_guide/reshaping.html#explode): skim these three.

**Skip:** `factorize()`.

**On your dataset:** turn one table wide → long with `melt`, then back with `pivot_table`, and check you get the same numbers.

---

### Part 7 — Time series + rolling windows · 1 h 30
📄 https://pandas.pydata.org/docs/user_guide/timeseries.html

- [x] 1. [Overview](https://pandas.pydata.org/docs/user_guide/timeseries.html#overview) and [Timestamps vs. time spans](https://pandas.pydata.org/docs/user_guide/timeseries.html#timestamps-vs-time-spans): read these two together.
- [x] 2. ⭐ [Converting to timestamps](https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-timestamps): `pd.to_datetime`, [Providing a format argument](https://pandas.pydata.org/docs/user_guide/timeseries.html#providing-a-format-argument), [Invalid data](https://pandas.pydata.org/docs/user_guide/timeseries.html#invalid-data) (`errors="coerce"`, the fix for messy dates).
- [x] 3. [Generating ranges of timestamps](https://pandas.pydata.org/docs/user_guide/timeseries.html#generating-ranges-of-timestamps): `pd.date_range`, used to find missing dates.
- [x] 4. [Indexing](https://pandas.pydata.org/docs/user_guide/timeseries.html#indexing) → [Partial string indexing](https://pandas.pydata.org/docs/user_guide/timeseries.html#partial-string-indexing): `df.loc["2024-03"]`.
- [x] 5. [Time/date components](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-date-components): `.dt.year`, `.dt.dayofweek`, etc.
- [x] 6. [Shifting / lagging](https://pandas.pydata.org/docs/user_guide/timeseries.html#shifting-lagging): `shift()` for "change since last period".
- [x] 7. ⭐ [Resampling](https://pandas.pydata.org/docs/user_guide/timeseries.html#resampling): Basics, Upsampling, Aggregation (`df.resample("ME").sum()`).
- [x] 8. [Time zone handling](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-zone-handling): skim `tz_localize` vs `tz_convert`.

📄 **Plus the windowing page:** https://pandas.pydata.org/docs/user_guide/window.html *(the roadmap's "rolling windows" topic lives here)*
- [x] 9. [Rolling window](https://pandas.pydata.org/docs/user_guide/window.html#rolling-window) + [Centering windows](https://pandas.pydata.org/docs/user_guide/window.html#centering-windows): `rolling(7).mean()`, and `rolling("7D")` on a DatetimeIndex.
- [x] 10. [Expanding window](https://pandas.pydata.org/docs/user_guide/window.html#expanding-window) and [Exponentially weighted window](https://pandas.pydata.org/docs/user_guide/window.html#exponentially-weighted-window).

**Skip:** DateOffset details, custom business days/hours, epoch timestamps, Timestamp limitations, periods.

---

## 🌉 Bridge pages (Week 6 topics outside the 5 assigned pages; only if you have time)

| Week 6 topic | Read this | Sections |
| :--- | :--- | :--- |
| Missing data: *why* it's missing | [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) | [Values considered "missing"](https://pandas.pydata.org/docs/user_guide/missing_data.html#values-considered-missing), [Dropping](https://pandas.pydata.org/docs/user_guide/missing_data.html#dropping-missing-data), [Filling](https://pandas.pydata.org/docs/user_guide/missing_data.html#filling-missing-data), [Interpolation](https://pandas.pydata.org/docs/user_guide/missing_data.html#interpolation) |
| Data types and memory | [Scaling to large datasets](https://pandas.pydata.org/docs/user_guide/scale.html) | [Use efficient datatypes](https://pandas.pydata.org/docs/user_guide/scale.html#use-efficient-datatypes) (`category`, downcasting, `memory_usage(deep=True)`) |
| Categorical columns | [Categorical data](https://pandas.pydata.org/docs/user_guide/categorical.html) | Object creation, and the part on memory usage |

*([Kaggle Learn — Data Cleaning](../Kaggle%20Learn%20-%20Data%20Cleaning/README.md) 🏆 covers the missing-data topic too, on a real messy dataset.)*

---

## 🛠️ What this module produces (from the roadmap)

> The reading is done; these build tasks are still open and belong to the Month 2 cleaning work.

- [x] A messy public dataset cleaned completely, with **a reason written next to every decision** and row counts before and after: done in [Project P1](../P1%20-%20NYC%20Restaurant%20Grades/README.md#-cleaning-decisions-each-with-a-reason-and-row-counts) (NYC restaurant inspections)
- [x] `data_quality_report(df)`: missing values, unique counts, type problems, duplicates, outliers: [`P1/src/cleaning.py`](../P1%20-%20NYC%20Restaurant%20Grades/src/cleaning.py)
- [ ] A slow `apply` groupby rewritten vectorised, with the speedup recorded (Part 5)
