[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [⏮️ **matplotlib**](../matplotlib%20-%20official%20tutorials/README.md) &nbsp;•&nbsp; [**Next: Storytelling with Data** ⏭️](../Storytelling%20with%20Data%20%28Cole%20Nussbaumer%20Knaflic%29/README.md)

---

# 🌊 seaborn — official tutorial (Week 7)

### *Statistical charts in a few lines, and knowing where seaborn stops and matplotlib takes over*

[![Time](https://img.shields.io/badge/Time_budget-4_hrs-blue?style=flat-square)](#)
[![Version](https://img.shields.io/badge/seaborn-0.13.2-4c72b0?style=flat-square)](https://seaborn.pydata.org/tutorial.html)
[![Pages](https://img.shields.io/badge/Pages-13-purple?style=flat-square)](#-the-study-path)

> [!NOTE]
> **Roadmap assignment:** the full user guide and tutorial, skipping nothing. **What you produce:** the charts in your P1 project.
> Do the [matplotlib module](../matplotlib%20-%20official%20tutorials/README.md) first. Every seaborn plot is a matplotlib Figure/Axes underneath, so that is what lets you customise it.

> [!TIP]
> **The one idea to take away:** *axes-level* functions (`scatterplot`, `histplot`, `boxplot`...) take `ax=` and draw into **your** `fig, ax`. *Figure-level* functions (`relplot`, `displot`, `catplot`, `lmplot`, `pairplot`) **create their own figure** and return a grid object `g`. You reach matplotlib through `g.axes` and `g.figure`. Page 2 teaches this.

---

## 🗺️ The study path

The order below is the one on the [tutorial index](https://seaborn.pydata.org/tutorial.html).

| # | Page | Time | Status |
| :-: | :--- | :-: | :-: |
| 1 | An introduction to seaborn | 15 min | ☐ |
| 2 | ⭐ Overview of plotting functions | 30 min | ☐ |
| 3 | Data structures (long vs wide) | 20 min | ☐ |
| 4 | The seaborn.objects interface + Properties | 20 min (skim) | ☐ |
| 5 | Visualizing statistical relationships | 25 min | ☐ |
| 6 | ⭐ Visualizing distributions | 35 min | ☐ |
| 7 | Visualizing categorical data | 25 min | ☐ |
| 8 | Statistical estimation and error bars | 20 min | ☐ |
| 9 | Estimating regression fits | 15 min | ☐ |
| 10 | Building structured multi-plot grids | 20 min | ☐ |
| 11 | Controlling figure aesthetics | 15 min | ☐ |
| 12 | Choosing color palettes | 20 min | ☐ |
| + | `heatmap` API page (not in the tutorial) | 10 min | ☐ |
| | **Total** | **≈ 4 h 15** | |

---

### 1 — An introduction to seaborn · 15 min
📄 https://seaborn.pydata.org/tutorial/introduction.html
- [ ] Read all of it. Focus on [Statistical estimation](https://seaborn.pydata.org/tutorial/introduction.html#statistical-estimation), [Distributional representations](https://seaborn.pydata.org/tutorial/introduction.html#distributional-representations), and [Relationship to matplotlib](https://seaborn.pydata.org/tutorial/introduction.html#relationship-to-matplotlib).

### 2 — ⭐ Overview of seaborn plotting functions · 30 min
📄 https://seaborn.pydata.org/tutorial/function_overview.html
- [ ] [Similar functions for similar tasks](https://seaborn.pydata.org/tutorial/function_overview.html#similar-functions-for-similar-tasks): the three families: **rel**ational, **dis**tributional, **cat**egorical.
- [ ] [Axes-level functions make self-contained plots](https://seaborn.pydata.org/tutorial/function_overview.html#axes-level-functions-make-self-contained-plots): the `ax=` argument.
- [ ] [Figure-level functions own their figure](https://seaborn.pydata.org/tutorial/function_overview.html#figure-level-functions-own-their-figure).
- [ ] [Customizing plots from a figure-level function](https://seaborn.pydata.org/tutorial/function_overview.html#customizing-plots-from-a-figure-level-function): `g.set_axis_labels`, `g.set_titles`, `g.axes`.
- [ ] [Specifying figure sizes](https://seaborn.pydata.org/tutorial/function_overview.html#specifying-figure-sizes): `height=` and `aspect=`, not `figsize`.
- [ ] [Relative merits](https://seaborn.pydata.org/tutorial/function_overview.html#relative-merits-of-figure-level-functions) + [Combining multiple views](https://seaborn.pydata.org/tutorial/function_overview.html#combining-multiple-views-on-the-data) (`jointplot`, `pairplot`).

**Exercise:** draw the same histogram once with `sns.histplot(data=df, x=..., ax=ax)` inside your own `fig, ax`, and once with `sns.displot(...)`. Then change the title in both. That is the seaborn/matplotlib boundary.

### 3 — Data structures accepted by seaborn · 20 min
📄 https://seaborn.pydata.org/tutorial/data_structure.html
- [ ] [Long-form data](https://seaborn.pydata.org/tutorial/data_structure.html#long-form-data) vs [Wide-form data](https://seaborn.pydata.org/tutorial/data_structure.html#wide-form-data) vs [Messy data](https://seaborn.pydata.org/tutorial/data_structure.html#messy-data).
- [ ] [Options for visualizing long-form data](https://seaborn.pydata.org/tutorial/data_structure.html#options-for-visualizing-long-form-data).
- 🔗 This is why pandas `melt()` matters ([pandas module, Part 6](../pandas%20-%20official%20User%20Guide/README.md)).

### 4 — The seaborn.objects interface · 20 min (skim)
📄 https://seaborn.pydata.org/tutorial/objects_interface.html · https://seaborn.pydata.org/tutorial/properties.html
- [ ] Read [Specifying a plot and mapping data](https://seaborn.pydata.org/tutorial/objects_interface.html#specifying-a-plot-and-mapping-data), [Statistical transformation](https://seaborn.pydata.org/tutorial/objects_interface.html#statistical-transformation), [Adding multiple layers](https://seaborn.pydata.org/tutorial/objects_interface.html#adding-multiple-layers), [Integrating with matplotlib](https://seaborn.pydata.org/tutorial/objects_interface.html#integrating-with-matplotlib).
- Newer grammar-of-graphics style API (`so.Plot(...).add(so.Dot())`). Know that it exists; **the function interface (pages 5–12) is what you'll use this month.** Skim the Properties page only.

### 5 — Visualizing statistical relationships · 25 min
📄 https://seaborn.pydata.org/tutorial/relational.html
- [ ] [Relating variables with scatter plots](https://seaborn.pydata.org/tutorial/relational.html#relating-variables-with-scatter-plots): `hue`, `style`, `size`.
- [ ] [Emphasizing continuity with line plots](https://seaborn.pydata.org/tutorial/relational.html#emphasizing-continuity-with-line-plots) → [Aggregation and representing uncertainty](https://seaborn.pydata.org/tutorial/relational.html#aggregation-and-representing-uncertainty): **the shaded band is a bootstrapped 95% CI**. Connects to your Month 1 bootstrap work.
- [ ] [Plotting subsets with semantic mappings](https://seaborn.pydata.org/tutorial/relational.html#plotting-subsets-of-data-with-semantic-mappings).
- [ ] [Showing multiple relationships with facets](https://seaborn.pydata.org/tutorial/relational.html#showing-multiple-relationships-with-facets): `relplot(col=...)`.

### 6 — ⭐ Visualizing distributions of data · 35 min
📄 https://seaborn.pydata.org/tutorial/distributions.html
- [ ] [Plotting univariate histograms](https://seaborn.pydata.org/tutorial/distributions.html#plotting-univariate-histograms): [Choosing the bin size](https://seaborn.pydata.org/tutorial/distributions.html#choosing-the-bin-size), [Conditioning on other variables](https://seaborn.pydata.org/tutorial/distributions.html#conditioning-on-other-variables), [Normalized histogram statistics](https://seaborn.pydata.org/tutorial/distributions.html#normalized-histogram-statistics) (`stat="density"`, `common_norm`).
- [ ] [Kernel density estimation](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation): [Choosing the smoothing bandwidth](https://seaborn.pydata.org/tutorial/distributions.html#choosing-the-smoothing-bandwidth) and ⚠️ [KDE pitfalls](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation-pitfalls).
- [ ] [Empirical cumulative distributions](https://seaborn.pydata.org/tutorial/distributions.html#empirical-cumulative-distributions): `ecdfplot` (chart #8).
- [ ] [Visualizing bivariate distributions](https://seaborn.pydata.org/tutorial/distributions.html#visualizing-bivariate-distributions).
- [ ] [Plotting joint and marginal distributions](https://seaborn.pydata.org/tutorial/distributions.html#plotting-joint-and-marginal-distributions) (`jointplot`) + [Plotting many distributions](https://seaborn.pydata.org/tutorial/distributions.html#plotting-many-distributions) (`pairplot`).

### 7 — Visualizing categorical data · 25 min
📄 https://seaborn.pydata.org/tutorial/categorical.html
- [ ] [Categorical scatterplots](https://seaborn.pydata.org/tutorial/categorical.html#categorical-scatterplots): `stripplot`, `swarmplot`.
- [ ] [Comparing distributions](https://seaborn.pydata.org/tutorial/categorical.html#comparing-distributions): [Boxplots](https://seaborn.pydata.org/tutorial/categorical.html#boxplots), [Violinplots](https://seaborn.pydata.org/tutorial/categorical.html#violinplots).
- [ ] [Estimating central tendency](https://seaborn.pydata.org/tutorial/categorical.html#estimating-central-tendency): [Bar plots](https://seaborn.pydata.org/tutorial/categorical.html#bar-plots) (a bar = a *mean* + CI, not a count) and [Point plots](https://seaborn.pydata.org/tutorial/categorical.html#point-plots).
- [ ] [Showing additional dimensions](https://seaborn.pydata.org/tutorial/categorical.html#showing-additional-dimensions): `catplot(col=...)`.

### 8 — Statistical estimation and error bars · 20 min
📄 https://seaborn.pydata.org/tutorial/error_bars.html
- [ ] Measures of **spread** (`errorbar="sd"`, `"pi"`) vs measures of **estimate uncertainty** (`"se"`, `"ci"`). Know which question each one answers.
- [ ] Custom error bars, and error bars on regression fits.
- [ ] Read the closing section, "Are error bars enough?".

### 9 — Estimating regression fits · 15 min
📄 https://seaborn.pydata.org/tutorial/regression.html
- [ ] [Functions for drawing linear regression models](https://seaborn.pydata.org/tutorial/regression.html#functions-for-drawing-linear-regression-models): `regplot` (axes-level) vs `lmplot` (figure-level). Use this for chart #3 (scatter + trend).
- [ ] [Fitting different kinds of models](https://seaborn.pydata.org/tutorial/regression.html#fitting-different-kinds-of-models) and [Conditioning on other variables](https://seaborn.pydata.org/tutorial/regression.html#conditioning-on-other-variables).

### 10 — Building structured multi-plot grids · 20 min
📄 https://seaborn.pydata.org/tutorial/axis_grids.html
- [ ] Conditional small multiples: `FacetGrid` + `g.map_dataframe` (chart #7).
- [ ] Using custom functions: write a function that plots into the *current* axes.
- [ ] Plotting pairwise data relationships: `PairGrid`, `map_upper` / `map_lower` / `map_diag`.

### 11 — Controlling figure aesthetics · 15 min
📄 https://seaborn.pydata.org/tutorial/aesthetics.html
- [ ] [Seaborn figure styles](https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles) (`sns.set_theme(style="ticks")`), [Removing axes spines](https://seaborn.pydata.org/tutorial/aesthetics.html#removing-axes-spines) (`sns.despine()`), [Temporarily setting figure style](https://seaborn.pydata.org/tutorial/aesthetics.html#temporarily-setting-figure-style), [Overriding elements](https://seaborn.pydata.org/tutorial/aesthetics.html#overriding-elements-of-the-seaborn-styles), [Scaling plot elements](https://seaborn.pydata.org/tutorial/aesthetics.html#scaling-plot-elements) (`set_context("paper" | "talk")`).
- 🔗 Put the result into `plotting_utils.py`.

### 12 — Choosing color palettes · 20 min
📄 https://seaborn.pydata.org/tutorial/color_palettes.html
- [ ] [General principles](https://seaborn.pydata.org/tutorial/color_palettes.html#general-principles-for-using-color-in-plots): [Vary hue to distinguish categories](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-hue-to-distinguish-categories), [Vary luminance to represent numbers](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-luminance-to-represent-numbers).
- [ ] [Qualitative](https://seaborn.pydata.org/tutorial/color_palettes.html#qualitative-color-palettes) → [Sequential](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-palettes) ([Perceptually uniform](https://seaborn.pydata.org/tutorial/color_palettes.html#perceptually-uniform-palettes)) → [Diverging](https://seaborn.pydata.org/tutorial/color_palettes.html#diverging-color-palettes) (use this for a correlation heatmap).
- Try `sns.color_palette("colorblind")`.

### + `heatmap`: not in the tutorial, but on the roadmap · 10 min
📄 https://seaborn.pydata.org/generated/seaborn.heatmap.html
- [ ] Read the parameters `annot`, `fmt`, `cmap`, `center=0`, `vmin`/`vmax`, `mask`, then run the examples at the bottom. Use it for chart #6: `sns.heatmap(df.corr(numeric_only=True), cmap="vlag", center=0, annot=True, fmt=".2f", ax=ax)`.

---

## 🛠️ What this module produces

- [ ] One of each: `relplot`, `displot`, `catplot`, `pairplot`, `heatmap`, all on your cleaned Week 6 data
- [ ] At least one seaborn chart finished with matplotlib calls (`ax.annotate`, `ax.set_title`, spines), so you've crossed the seaborn → matplotlib boundary on purpose
- [ ] The chosen charts saved via `plotting_utils.save()` for P1
