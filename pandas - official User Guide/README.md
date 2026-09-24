[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [**Next module: matplotlib** ⏭️](../matplotlib%20-%20official%20tutorials/README.md)

---

# 🐼 pandas — official User Guide (Week 6)

### *The exact sections to read, in order, and what to do with each one*

[![Time](https://img.shields.io/badge/Time_budget-8_hrs-blue?style=flat-square)](#)
[![Version](https://img.shields.io/badge/pandas-3.0.x-150458?style=flat-square)](https://pandas.pydata.org/docs/user_guide/index.html)
[![Steps](https://img.shields.io/badge/Steps-7_parts-purple?style=flat-square)](#-the-study-path)

> [!NOTE]
> **Roadmap assignment:** Indexing and selecting data · Merge/join/concatenate · Group By · Reshaping and pivot tables · Time series. **Skip everything else** and use it later as a lookup reference.
> **What you produce:** type every example into *your own messy dataset*, not a scratch cell.
>
> The User Guide is ~30 pages long and each page is huge. This file tells you **which headings inside each page** to read and which to skip. Every link below jumps straight to the heading.

> [!IMPORTANT]
> **pandas 3.0 changed one thing in the roadmap.** Week 6 says *"learn what causes `SettingWithCopyWarning`"*. In pandas 3.0 **Copy-on-Write is the only mode**, so that warning is gone. Chained assignment like `df[df.a > 0]["b"] = 1` now **never works** and gives a `ChainedAssignmentError` warning instead. Part 2 below covers this (15 minutes). Check your version with `pd.__version__`.

---

## 🗺️ The study path

| Part | Page | Time | Status |
| :-: | :--- | :-: | :-: |
| 1 | Indexing and selecting data | 1 h 15 | ☐ |
| 2 | Copy-on-Write *(replaces the SettingWithCopyWarning topic)* | 15 min | ☐ |
| 3 | MultiIndex / advanced indexing | 45 min | ☐ |
| 4 | Merge, join, concatenate | 1 h 15 | ☐ |
| 5 | Group by: split-apply-combine | 2 h | ☐ |
| 6 | Reshaping and pivot tables | 1 h | ☐ |
| 7 | Time series + windowing (rolling) | 1 h 30 | ☐ |
| | **Total** | **8 h** | |

---

### Part 1 — Indexing and selecting data · 1 h 15
📄 https://pandas.pydata.org/docs/user_guide/indexing.html

- [ ] 1. [Different choices for indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#different-choices-for-indexing): the three accessors — `.loc` (labels), `.iloc` (positions), `[]`. Learn which one to use when.
- [ ] 2. [Basics](https://pandas.pydata.org/docs/user_guide/indexing.html#basics): `df[col]`, `df[[col1, col2]]`, swapping columns.
- [ ] 3. [Selection by label](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label) + [Slicing with labels](https://pandas.pydata.org/docs/user_guide/indexing.html#slicing-with-labels): **`.loc` slices include the end label**, `.iloc` slices do not.
- [ ] 4. [Selection by position](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-position): `.iloc[rows, cols]`, out-of-range behaviour.
- [ ] 5. [Selection by callable](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-callable): `df.loc[lambda d: d.x > 0]`, used in method chains.
- [ ] 6. [Combining positional and label-based indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#combining-positional-and-label-based-indexing) and [Reindexing](https://pandas.pydata.org/docs/user_guide/indexing.html#reindexing).
- [ ] 7. [Boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing): masks with `&`, `|`, `~`, and **brackets around every condition**.
- [ ] 8. [Indexing with isin](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-with-isin).
- [ ] 9. [The where() Method and Masking](https://pandas.pydata.org/docs/user_guide/indexing.html#the-where-method-and-masking) + [Mask](https://pandas.pydata.org/docs/user_guide/indexing.html#mask).
- [ ] 10. [The query() Method](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method): `df.query("age > 30 and city == @c")`.

**Skip:** Attribute access, Selecting random samples, Setting with enlargement, Setting with enlargement conditionally. Skim [Fast scalar value getting and setting](https://pandas.pydata.org/docs/user_guide/indexing.html#fast-scalar-value-getting-and-setting) (`.at` / `.iat`).

**On your dataset:** write the same filter three ways (a mask with `.loc`, `.query()`, and `.where()`) and check the row counts match.

---

### Part 2 — Copy-on-Write · 15 min
📄 https://pandas.pydata.org/docs/user_guide/copy_on_write.html

- [ ] 1. [Previous behavior](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#previous-behavior): why the old view/copy confusion caused `SettingWithCopyWarning`.
- [ ] 2. [Chained Assignment](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#chained-assignment): why `df[mask]["col"] = v` now does nothing.
- [ ] 3. [Patterns to avoid](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#patterns-to-avoid).

**Rule to remember:** set values in one step with `df.loc[mask, "col"] = v`.

---

### Part 3 — MultiIndex / advanced indexing · 45 min
📄 https://pandas.pydata.org/docs/user_guide/advanced.html
*(Roadmap Week 6: "Index and MultiIndex — the thing everyone skips and then suffers for".)*

- [ ] 1. [Creating a MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html#creating-a-multiindex-hierarchical-index-object): `from_tuples`, `from_product`, `set_index([a, b])`.
- [ ] 2. [Basic indexing on axis with MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html#basic-indexing-on-axis-with-multiindex).
- [ ] 3. [Using slicers](https://pandas.pydata.org/docs/user_guide/advanced.html#using-slicers): `pd.IndexSlice`.
- [ ] 4. [Cross-section](https://pandas.pydata.org/docs/user_guide/advanced.html#cross-section): `df.xs(key, level=...)`.
- [ ] 5. [Swapping levels](https://pandas.pydata.org/docs/user_guide/advanced.html#swapping-levels-with-swaplevel) and [Sorting a MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html#sorting-a-multiindex): an unsorted index gives a `PerformanceWarning`.
- [ ] 6. [Binning data with cut and qcut](https://pandas.pydata.org/docs/user_guide/advanced.html#binning-data-with-cut-and-qcut).

**Skip:** Defined levels, Take methods, CategoricalIndex/RangeIndex/IntervalIndex details, the FAQ. Glance at [Endpoints are inclusive](https://pandas.pydata.org/docs/user_guide/advanced.html#endpoints-are-inclusive).

---

### Part 4 — Merge, join, concatenate · 1 h 15
📄 https://pandas.pydata.org/docs/user_guide/merging.html

- [ ] 1. [concat()](https://pandas.pydata.org/docs/user_guide/merging.html#concat): [Joining logic of the resulting axis](https://pandas.pydata.org/docs/user_guide/merging.html#joining-logic-of-the-resulting-axis), [Ignoring indexes](https://pandas.pydata.org/docs/user_guide/merging.html#ignoring-indexes-on-the-concatenation-axis), [Resulting keys](https://pandas.pydata.org/docs/user_guide/merging.html#resulting-keys).
- [ ] 2. [merge()](https://pandas.pydata.org/docs/user_guide/merging.html#merge) → [Merge types](https://pandas.pydata.org/docs/user_guide/merging.html#merge-types): `inner`, `left`, `right`, `outer`, `cross`.
- [ ] 3. ⭐ [Merge key uniqueness](https://pandas.pydata.org/docs/user_guide/merging.html#merge-key-uniqueness): the `validate="one_to_one" / "one_to_many" / "many_to_one"` argument. **This is the roadmap's "validate every merge" rule.**
- [ ] 4. ⭐ [Merge result indicator](https://pandas.pydata.org/docs/user_guide/merging.html#merge-result-indicator): `indicator=True` shows which rows matched.
- [ ] 5. [Overlapping value columns](https://pandas.pydata.org/docs/user_guide/merging.html#overlapping-value-columns): `suffixes=`.
- [ ] 6. [DataFrame.join()](https://pandas.pydata.org/docs/user_guide/merging.html#dataframe-join): read only the first part (joining on the index).
- [ ] 7. [merge_asof()](https://pandas.pydata.org/docs/user_guide/merging.html#merge-asof): "nearest earlier timestamp" joins.
- [ ] 8. [compare()](https://pandas.pydata.org/docs/user_guide/merging.html#compare): shows what changed between two versions of a frame (useful for checking your cleaning).

**Skip:** joins with two MultiIndexes, `combine_first`, `merge_ordered`.

**On your dataset:** for every merge, print `len()` before and after, pass `validate=` and `indicator=True`, then run `value_counts()` on `_merge`.

---

### Part 5 — Group by: split-apply-combine · 2 h *(the most important page)*
📄 https://pandas.pydata.org/docs/user_guide/groupby.html

- [ ] 1. [Splitting an object into groups](https://pandas.pydata.org/docs/user_guide/groupby.html#splitting-an-object-into-groups), including [GroupBy dropna](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-dropna): **NaN keys are dropped by default**.
- [ ] 2. [Iterating through groups](https://pandas.pydata.org/docs/user_guide/groupby.html#iterating-through-groups) and [Selecting a group](https://pandas.pydata.org/docs/user_guide/groupby.html#selecting-a-group) (`get_group`).
- [ ] 3. [Aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#aggregation): [Built-in aggregation methods](https://pandas.pydata.org/docs/user_guide/groupby.html#built-in-aggregation-methods) and [The aggregate() method](https://pandas.pydata.org/docs/user_guide/groupby.html#the-aggregate-method).
- [ ] 4. ⭐ [Named aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#named-aggregation): `agg(total=("sales", "sum"), n=("id", "count"))`, the clean way to name output columns.
- [ ] 5. [Applying different functions to DataFrame columns](https://pandas.pydata.org/docs/user_guide/groupby.html#applying-different-functions-to-dataframe-columns).
- [ ] 6. ⭐ [Transformation](https://pandas.pydata.org/docs/user_guide/groupby.html#transformation) + [The transform() method](https://pandas.pydata.org/docs/user_guide/groupby.html#the-transform-method): returns a result **the same length as the input**, e.g. share of group total, or filling NaN with the group mean.
- [ ] 7. [Window and resample operations](https://pandas.pydata.org/docs/user_guide/groupby.html#window-and-resample-operations): `groupby().rolling()`.
- [ ] 8. [Filtration](https://pandas.pydata.org/docs/user_guide/groupby.html#filtration): drop groups that are too small.
- [ ] 9. [Flexible apply](https://pandas.pydata.org/docs/user_guide/groupby.html#flexible-apply): read *why* it is slow. It runs Python once per group. Try `agg`/`transform` first.
- [ ] 10. [Handling of (un)observed Categorical values](https://pandas.pydata.org/docs/user_guide/groupby.html#handling-of-unobserved-categorical-values) and [Taking the first rows of each group](https://pandas.pydata.org/docs/user_guide/groupby.html#taking-the-first-rows-of-each-group).

**Skip:** Numba accelerated routines, grouping with ordered factors, enumerate groups, plotting.

**On your dataset:** this is **build task 3**. Write one group statistic with `.apply(lambda g: ...)`, rewrite it with `agg`/`transform`, time both with `%timeit`, and record the speedup.

---

### Part 6 — Reshaping and pivot tables · 1 h
📄 https://pandas.pydata.org/docs/user_guide/reshaping.html

- [ ] 1. [pivot()](https://pandas.pydata.org/docs/user_guide/reshaping.html#pivot) vs [pivot_table()](https://pandas.pydata.org/docs/user_guide/reshaping.html#pivot-table): `pivot` fails on duplicate keys, `pivot_table` aggregates them. Plus [Adding margins](https://pandas.pydata.org/docs/user_guide/reshaping.html#adding-margins).
- [ ] 2. [stack() and unstack()](https://pandas.pydata.org/docs/user_guide/reshaping.html#stack-and-unstack): [Multiple levels](https://pandas.pydata.org/docs/user_guide/reshaping.html#multiple-levels) and [Missing data](https://pandas.pydata.org/docs/user_guide/reshaping.html#missing-data).
- [ ] 3. ⭐ [melt() and wide_to_long()](https://pandas.pydata.org/docs/user_guide/reshaping.html#melt-and-wide-to-long): wide → long. **seaborn needs long-form data**, so you will use this every week.
- [ ] 4. [crosstab()](https://pandas.pydata.org/docs/user_guide/reshaping.html#crosstab) + [Normalization](https://pandas.pydata.org/docs/user_guide/reshaping.html#normalization): frequency tables and row/column percentages.
- [ ] 5. [cut()](https://pandas.pydata.org/docs/user_guide/reshaping.html#cut), [get_dummies()](https://pandas.pydata.org/docs/user_guide/reshaping.html#get-dummies-and-from-dummies), [explode()](https://pandas.pydata.org/docs/user_guide/reshaping.html#explode): skim these three.

**Skip:** `factorize()`.

**On your dataset:** turn one table wide → long with `melt`, then back with `pivot_table`, and check you get the same numbers.

---

### Part 7 — Time series + rolling windows · 1 h 30
📄 https://pandas.pydata.org/docs/user_guide/timeseries.html

- [ ] 1. [Overview](https://pandas.pydata.org/docs/user_guide/timeseries.html#overview) and [Timestamps vs. time spans](https://pandas.pydata.org/docs/user_guide/timeseries.html#timestamps-vs-time-spans): read these two together.
- [ ] 2. ⭐ [Converting to timestamps](https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-timestamps): `pd.to_datetime`, [Providing a format argument](https://pandas.pydata.org/docs/user_guide/timeseries.html#providing-a-format-argument), [Invalid data](https://pandas.pydata.org/docs/user_guide/timeseries.html#invalid-data) (`errors="coerce"`, the fix for messy dates).
- [ ] 3. [Generating ranges of timestamps](https://pandas.pydata.org/docs/user_guide/timeseries.html#generating-ranges-of-timestamps): `pd.date_range`, used to find missing dates.
- [ ] 4. [Indexing](https://pandas.pydata.org/docs/user_guide/timeseries.html#indexing) → [Partial string indexing](https://pandas.pydata.org/docs/user_guide/timeseries.html#partial-string-indexing): `df.loc["2024-03"]`.
- [ ] 5. [Time/date components](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-date-components): `.dt.year`, `.dt.dayofweek`, etc.
- [ ] 6. [Shifting / lagging](https://pandas.pydata.org/docs/user_guide/timeseries.html#shifting-lagging): `shift()` for "change since last period".
- [ ] 7. ⭐ [Resampling](https://pandas.pydata.org/docs/user_guide/timeseries.html#resampling): Basics, Upsampling, Aggregation (`df.resample("ME").sum()`).
- [ ] 8. [Time zone handling](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-zone-handling): skim `tz_localize` vs `tz_convert`.

📄 **Plus the windowing page:** https://pandas.pydata.org/docs/user_guide/window.html *(the roadmap's "rolling windows" topic lives here)*
- [ ] 9. [Rolling window](https://pandas.pydata.org/docs/user_guide/window.html#rolling-window) + [Centering windows](https://pandas.pydata.org/docs/user_guide/window.html#centering-windows): `rolling(7).mean()`, and `rolling("7D")` on a DatetimeIndex.
- [ ] 10. [Expanding window](https://pandas.pydata.org/docs/user_guide/window.html#expanding-window) and [Exponentially weighted window](https://pandas.pydata.org/docs/user_guide/window.html#exponentially-weighted-window).

**Skip:** DateOffset details, custom business days/hours, epoch timestamps, Timestamp limitations, periods.

---

## 🌉 Bridge pages (Week 6 topics outside the 5 assigned pages; only if you have time)

| Week 6 topic | Read this | Sections |
| :--- | :--- | :--- |
| Missing data: *why* it's missing | [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) | [Values considered "missing"](https://pandas.pydata.org/docs/user_guide/missing_data.html#values-considered-missing), [Dropping](https://pandas.pydata.org/docs/user_guide/missing_data.html#dropping-missing-data), [Filling](https://pandas.pydata.org/docs/user_guide/missing_data.html#filling-missing-data), [Interpolation](https://pandas.pydata.org/docs/user_guide/missing_data.html#interpolation) |
| Data types and memory | [Scaling to large datasets](https://pandas.pydata.org/docs/user_guide/scale.html) | [Use efficient datatypes](https://pandas.pydata.org/docs/user_guide/scale.html#use-efficient-datatypes) (`category`, downcasting, `memory_usage(deep=True)`) |
| Categorical columns | [Categorical data](https://pandas.pydata.org/docs/user_guide/categorical.html) | Object creation, and the part on memory usage |

*(Kaggle Learn — Data Cleaning covers the missing-data topic too.)*

---

## 🛠️ What this module produces (from the roadmap)

- [ ] A messy public dataset cleaned completely, with **a reason written next to every decision** and row counts before and after
- [ ] `data_quality_report(df)`: missing values, unique counts, type problems, duplicates, outliers
- [ ] A slow `apply` groupby rewritten vectorised, with the speedup recorded (Part 5)
