[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [⏮️ **matplotlib**](../matplotlib%20-%20official%20tutorials/README.md) &nbsp;•&nbsp; [**Next: Storytelling with Data** ⏭️](../Storytelling%20with%20Data%20%28Cole%20Nussbaumer%20Knaflic%29/README.md)

---

# 🌊 seaborn — official tutorial (Week 7)

### *Statistical charts in a few lines, and knowing where seaborn stops and matplotlib takes over*

[![Time](https://img.shields.io/badge/Time_budget-4_hrs-blue?style=flat-square)](#)
[![Version](https://img.shields.io/badge/seaborn-0.13.2-4c72b0?style=flat-square)](https://seaborn.pydata.org/tutorial.html)
[![Pages](https://img.shields.io/badge/Pages-13-purple?style=flat-square)](#-the-study-path)
[![Status](https://img.shields.io/badge/Status-Completed_13%2F13_notebooks-brightgreen?style=flat-square)](#-notebooks)

> [!NOTE]
> **Roadmap assignment:** the full user guide and tutorial, skipping nothing. **What you produce:** the charts in your P1 project.
> Do the [matplotlib module](../matplotlib%20-%20official%20tutorials/README.md) first. Every seaborn plot is a matplotlib Figure/Axes underneath, so that is what lets you customise it.

> [!TIP]
> **Status: completed.** All 12 tutorial pages and the `heatmap` API page are worked through in 13 Jupyter notebooks, with every example run and its output saved. 👉 **[Jump to the notebooks](#-notebooks)** · Next: **[Storytelling with Data](../Storytelling%20with%20Data%20%28Cole%20Nussbaumer%20Knaflic%29/README.md)**

> [!TIP]
> **The one idea to take away:** *axes-level* functions (`scatterplot`, `histplot`, `boxplot`...) take `ax=` and draw into **your** `fig, ax`. *Figure-level* functions (`relplot`, `displot`, `catplot`, `lmplot`, `pairplot`) **create their own figure** and return a grid object `g`. You reach matplotlib through `g.axes` and `g.figure`. Page 2 teaches this.

---

## 🗺️ The study path

The order below is the one on the [tutorial index](https://seaborn.pydata.org/tutorial.html).

| # | Page | Time | Notebook | Status |
| :-: | :--- | :-: | :-: | :-: |
| 1 | An introduction to seaborn | 15 min | [`01`](Notebook/01_An%20introduction%20to%20seaborn.ipynb) | ✅ |
| 2 | ⭐ Overview of plotting functions | 30 min | [`02`](Notebook/02_Overview%20of%20plotting%20functions.ipynb) | ✅ |
| 3 | Data structures (long vs wide) | 20 min | [`03`](Notebook/03_Data%20structures.ipynb) | ✅ |
| 4 | The seaborn.objects interface + Properties | 20 min (skim) | [`04`](Notebook/04_The%20seaborn.objects%20interface.ipynb) | ✅ |
| 5 | Visualizing statistical relationships | 25 min | [`05`](Notebook/05_Visualizing%20statistical%20relationships.ipynb) | ✅ |
| 6 | ⭐ Visualizing distributions | 35 min | [`06`](Notebook/06_Visualizing%20distributions.ipynb) | ✅ |
| 7 | Visualizing categorical data | 25 min | [`07`](Notebook/07_Visualizing%20categorical%20data.ipynb) | ✅ |
| 8 | Statistical estimation and error bars | 20 min | [`08`](Notebook/08_Statistical%20estimation%20and%20error%20bars.ipynb) | ✅ |
| 9 | Estimating regression fits | 15 min | [`09`](Notebook/09_Estimating%20regression%20fits.ipynb) | ✅ |
| 10 | Building structured multi-plot grids | 20 min | [`10`](Notebook/10_Building%20structured%20multi-plot%20grids.ipynb) | ✅ |
| 11 | Controlling figure aesthetics | 15 min | [`11`](Notebook/11_Controlling%20figure%20aesthetics.ipynb) | ✅ |
| 12 | Choosing color palettes | 20 min | [`12`](Notebook/12_Choosing%20color%20palettes.ipynb) | ✅ |
| + | `heatmap` API page (not in the tutorial) | 10 min | [`13`](Notebook/13_heatmap%20API%20page.ipynb) | ✅ |
| | **Total** | **≈ 4 h 15** | **13 notebooks** | ✅ **13 / 13** |

---

## 📓 Notebooks

One notebook per page, in the order of the tutorial index. Headings follow the docs headings, so each notebook can be read next to its page. Every code cell is commented, and each notebook ends with **Key takeaways**.

| # | Notebook | What's inside |
| :-: | :--- | :--- |
| 01 | [An introduction to seaborn](Notebook/01_An%20introduction%20to%20seaborn.ipynb) | `relplot` / `lmplot` / `displot` / `catplot` / `jointplot` / `pairplot` tour, statistical estimation, `PairGrid`, polishing a figure through `g.figure`, `g.ax`, `g.legend` |
| 02 | [Overview of plotting functions](Notebook/02_Overview%20of%20plotting%20functions.ipynb) | The rel / dis / cat families, ⭐ axes-level (`ax=`) vs figure-level (owns its figure), `FacetGrid` sizing with `height` / `aspect`, `jointplot` / `pairplot`; ⭐ the README exercise (same histogram both ways, title changed in both) |
| 03 | [Data structures](Notebook/03_Data%20structures.ipynb) | Long vs wide vs messy data, what wide-form loses, `melt` on the anagrams data, dicts / Series / arrays as inputs; a wide → long → wide round-trip check |
| 04 | [The seaborn.objects interface](Notebook/04_The%20seaborn.objects%20interface.ipynb) | `so.Plot(...).add(Mark, Stat, Move)`, set vs mapped properties, `Agg` / `Hist` / `Est` / `PolyFit`, `Dodge` / `Jitter` / `Stack`, layers, `facet` / `pair`, `.on()` a matplotlib figure, scales, labels, themes; plus a Properties reference table |
| 05 | [Visualizing statistical relationships](Notebook/05_Visualizing%20statistical%20relationships.ipynb) | `hue` / `style` / `size` semantics, line plots with ⭐ bootstrapped 95% CI, `errorbar=None` / `"sd"`, `units=`, `hue_norm=LogNorm()`, `sort=False`, `orient="y"`, facets with `col_wrap` |
| 06 | [Visualizing distributions](Notebook/06_Visualizing%20distributions.ipynb) | Bin width / `bins` / `discrete=True`, `element="step"`, `multiple="stack" / "dodge"`, `stat=` + `common_norm=False`, KDE bandwidth and ⚠️ pitfalls, ECDF, bivariate hist / KDE, `jointplot`, `JointGrid`, `rugplot`, `pairplot`; roadmap charts 1 and 8 |
| 07 | [Visualizing categorical data](Notebook/07_Visualizing%20categorical%20data.ipynb) | Strip / swarm, `native_scale`, `order=`, box / boxen / violin (split, inner sticks), violin + swarm, bar (mean + CI) / count / point plots, faceted `catplot` finished with matplotlib |
| 08 | [Statistical estimation and error bars](Notebook/08_Statistical%20estimation%20and%20error%20bars.ipynb) | Spread (`sd`, `pi`) vs uncertainty (`se`, `ci`), parametric vs bootstrap, `n_boot` / `seed`, custom error functions, regression bands, "Are error bars enough?" (raw points + mean + CI) |
| 09 | [Estimating regression fits](Notebook/09_Estimating%20regression%20fits.ipynb) | `regplot` vs `lmplot`, `x_jitter` / `x_estimator`, Anscombe's quartet: `order=2`, `robust=True`, `logistic=True`, `lowess=True`, `residplot`, conditioning on `hue` / `col` / `row`; roadmap chart 3 |
| 10 | [Building structured multi-plot grids](Notebook/10_Building%20structured%20multi-plot%20grids.ipynb) | `FacetGrid` + `map` / ⭐ `map_dataframe`, `margin_titles`, `*_order`, `col_wrap`, `g.set` / `g.set_axis_labels`, `g.axes_dict`, custom functions (Q-Q plot, hexbin), `PairGrid` (upper / lower / diag), `pairplot` |
| 11 | [Controlling figure aesthetics](Notebook/11_Controlling%20figure%20aesthetics.ipynb) | Five styles, `despine(offset, trim)`, temporary styles with `with`, overriding with `rc=`, contexts `paper` → `poster`, `font_scale`; a `set_style()` for `plotting_utils.py` |
| 12 | [Choosing color palettes](Notebook/12_Choosing%20color%20palettes.ipynb) | Hue / saturation / luminance, hue for categories vs luminance for numbers, qualitative (`deep`, `colorblind`, `husl`, Brewer), sequential (`rocket`, `mako`, `flare`, `crest`, cubehelix, `light:` / `dark:`), diverging (`vlag`, `icefire`, `diverging_palette`) |
| 13 | [`heatmap` API page](Notebook/13_heatmap%20API%20page.ipynb) | Every example from the API page (`annot`, `fmt`, `linewidth`, `cmap`, `vmin` / `vmax`, Axes tweaks); roadmap chart 6: a masked correlation heatmap with `vlag` and `center=0` |

> [!NOTE]
> Cells marked **(my addition)** are not on the docs page. They connect the page to a roadmap task (charts 1, 3, 6 and 8, the `set_style()` helper, the exercise in Part 2). Everything else follows the docs code, with the docs' random seeds, so the outputs match the website.

**Running them:** built and run with **seaborn 0.13.2**, matplotlib 3.11.2 and pandas 3.0 (the first cell prints the versions). `sns.load_dataset(...)` downloads the example datasets the first time (needs internet), then caches them. Notebook 09 needs `pip install statsmodels` for the robust, logistic and lowess fits; notebook 10 uses scipy.

---

### 1 — An introduction to seaborn · 15 min
📄 https://seaborn.pydata.org/tutorial/introduction.html
- [x] Read all of it. Focus on [Statistical estimation](https://seaborn.pydata.org/tutorial/introduction.html#statistical-estimation), [Distributional representations](https://seaborn.pydata.org/tutorial/introduction.html#distributional-representations), and [Relationship to matplotlib](https://seaborn.pydata.org/tutorial/introduction.html#relationship-to-matplotlib).

### 2 — ⭐ Overview of seaborn plotting functions · 30 min
📄 https://seaborn.pydata.org/tutorial/function_overview.html
- [x] [Similar functions for similar tasks](https://seaborn.pydata.org/tutorial/function_overview.html#similar-functions-for-similar-tasks): the three families: **rel**ational, **dis**tributional, **cat**egorical.
- [x] [Axes-level functions make self-contained plots](https://seaborn.pydata.org/tutorial/function_overview.html#axes-level-functions-make-self-contained-plots): the `ax=` argument.
- [x] [Figure-level functions own their figure](https://seaborn.pydata.org/tutorial/function_overview.html#figure-level-functions-own-their-figure).
- [x] [Customizing plots from a figure-level function](https://seaborn.pydata.org/tutorial/function_overview.html#customizing-plots-from-a-figure-level-function): `g.set_axis_labels`, `g.set_titles`, `g.axes`.
- [x] [Specifying figure sizes](https://seaborn.pydata.org/tutorial/function_overview.html#specifying-figure-sizes): `height=` and `aspect=`, not `figsize`.
- [x] [Relative merits](https://seaborn.pydata.org/tutorial/function_overview.html#relative-merits-of-figure-level-functions) + [Combining multiple views](https://seaborn.pydata.org/tutorial/function_overview.html#combining-multiple-views-on-the-data) (`jointplot`, `pairplot`).

**Exercise:** draw the same histogram once with `sns.histplot(data=df, x=..., ax=ax)` inside your own `fig, ax`, and once with `sns.displot(...)`. Then change the title in both. That is the seaborn/matplotlib boundary. ✅ *Done at the end of [notebook 02](Notebook/02_Overview%20of%20plotting%20functions.ipynb).*

### 3 — Data structures accepted by seaborn · 20 min
📄 https://seaborn.pydata.org/tutorial/data_structure.html
- [x] [Long-form data](https://seaborn.pydata.org/tutorial/data_structure.html#long-form-data) vs [Wide-form data](https://seaborn.pydata.org/tutorial/data_structure.html#wide-form-data) vs [Messy data](https://seaborn.pydata.org/tutorial/data_structure.html#messy-data).
- [x] [Options for visualizing long-form data](https://seaborn.pydata.org/tutorial/data_structure.html#options-for-visualizing-long-form-data).
- 🔗 This is why pandas `melt()` matters ([pandas module, Part 6](../pandas%20-%20official%20User%20Guide/README.md)).

### 4 — The seaborn.objects interface · 20 min (skim)
📄 https://seaborn.pydata.org/tutorial/objects_interface.html · https://seaborn.pydata.org/tutorial/properties.html
- [x] Read [Specifying a plot and mapping data](https://seaborn.pydata.org/tutorial/objects_interface.html#specifying-a-plot-and-mapping-data), [Statistical transformation](https://seaborn.pydata.org/tutorial/objects_interface.html#statistical-transformation), [Adding multiple layers](https://seaborn.pydata.org/tutorial/objects_interface.html#adding-multiple-layers), [Integrating with matplotlib](https://seaborn.pydata.org/tutorial/objects_interface.html#integrating-with-matplotlib).
- Newer grammar-of-graphics style API (`so.Plot(...).add(so.Dot())`). Know that it exists; **the function interface (pages 5–12) is what you'll use this month.** Skim the Properties page only.

### 5 — Visualizing statistical relationships · 25 min
📄 https://seaborn.pydata.org/tutorial/relational.html
- [x] [Relating variables with scatter plots](https://seaborn.pydata.org/tutorial/relational.html#relating-variables-with-scatter-plots): `hue`, `style`, `size`.
- [x] [Emphasizing continuity with line plots](https://seaborn.pydata.org/tutorial/relational.html#emphasizing-continuity-with-line-plots) → [Aggregation and representing uncertainty](https://seaborn.pydata.org/tutorial/relational.html#aggregation-and-representing-uncertainty): **the shaded band is a bootstrapped 95% CI**. Connects to your Month 1 bootstrap work.
- [x] [Plotting subsets with semantic mappings](https://seaborn.pydata.org/tutorial/relational.html#plotting-subsets-of-data-with-semantic-mappings).
- [x] [Showing multiple relationships with facets](https://seaborn.pydata.org/tutorial/relational.html#showing-multiple-relationships-with-facets): `relplot(col=...)`.

### 6 — ⭐ Visualizing distributions of data · 35 min
📄 https://seaborn.pydata.org/tutorial/distributions.html
- [x] [Plotting univariate histograms](https://seaborn.pydata.org/tutorial/distributions.html#plotting-univariate-histograms): [Choosing the bin size](https://seaborn.pydata.org/tutorial/distributions.html#choosing-the-bin-size), [Conditioning on other variables](https://seaborn.pydata.org/tutorial/distributions.html#conditioning-on-other-variables), [Normalized histogram statistics](https://seaborn.pydata.org/tutorial/distributions.html#normalized-histogram-statistics) (`stat="density"`, `common_norm`).
- [x] [Kernel density estimation](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation): [Choosing the smoothing bandwidth](https://seaborn.pydata.org/tutorial/distributions.html#choosing-the-smoothing-bandwidth) and ⚠️ [KDE pitfalls](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation-pitfalls).
- [x] [Empirical cumulative distributions](https://seaborn.pydata.org/tutorial/distributions.html#empirical-cumulative-distributions): `ecdfplot` (chart #8).
- [x] [Visualizing bivariate distributions](https://seaborn.pydata.org/tutorial/distributions.html#visualizing-bivariate-distributions).
- [x] [Plotting joint and marginal distributions](https://seaborn.pydata.org/tutorial/distributions.html#plotting-joint-and-marginal-distributions) (`jointplot`) + [Plotting many distributions](https://seaborn.pydata.org/tutorial/distributions.html#plotting-many-distributions) (`pairplot`).

### 7 — Visualizing categorical data · 25 min
📄 https://seaborn.pydata.org/tutorial/categorical.html
- [x] [Categorical scatterplots](https://seaborn.pydata.org/tutorial/categorical.html#categorical-scatterplots): `stripplot`, `swarmplot`.
- [x] [Comparing distributions](https://seaborn.pydata.org/tutorial/categorical.html#comparing-distributions): [Boxplots](https://seaborn.pydata.org/tutorial/categorical.html#boxplots), [Violinplots](https://seaborn.pydata.org/tutorial/categorical.html#violinplots).
- [x] [Estimating central tendency](https://seaborn.pydata.org/tutorial/categorical.html#estimating-central-tendency): [Bar plots](https://seaborn.pydata.org/tutorial/categorical.html#bar-plots) (a bar = a *mean* + CI, not a count) and [Point plots](https://seaborn.pydata.org/tutorial/categorical.html#point-plots).
- [x] [Showing additional dimensions](https://seaborn.pydata.org/tutorial/categorical.html#showing-additional-dimensions): `catplot(col=...)`.

### 8 — Statistical estimation and error bars · 20 min
📄 https://seaborn.pydata.org/tutorial/error_bars.html
- [x] Measures of **spread** (`errorbar="sd"`, `"pi"`) vs measures of **estimate uncertainty** (`"se"`, `"ci"`). Know which question each one answers.
- [x] Custom error bars, and error bars on regression fits.
- [x] Read the closing section, "Are error bars enough?".

### 9 — Estimating regression fits · 15 min
📄 https://seaborn.pydata.org/tutorial/regression.html
- [x] [Functions for drawing linear regression models](https://seaborn.pydata.org/tutorial/regression.html#functions-for-drawing-linear-regression-models): `regplot` (axes-level) vs `lmplot` (figure-level). Use this for chart #3 (scatter + trend).
- [x] [Fitting different kinds of models](https://seaborn.pydata.org/tutorial/regression.html#fitting-different-kinds-of-models) and [Conditioning on other variables](https://seaborn.pydata.org/tutorial/regression.html#conditioning-on-other-variables).

### 10 — Building structured multi-plot grids · 20 min
📄 https://seaborn.pydata.org/tutorial/axis_grids.html
- [x] Conditional small multiples: `FacetGrid` + `g.map_dataframe` (chart #7).
- [x] Using custom functions: write a function that plots into the *current* axes.
- [x] Plotting pairwise data relationships: `PairGrid`, `map_upper` / `map_lower` / `map_diag`.

### 11 — Controlling figure aesthetics · 15 min
📄 https://seaborn.pydata.org/tutorial/aesthetics.html
- [x] [Seaborn figure styles](https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles) (`sns.set_theme(style="ticks")`), [Removing axes spines](https://seaborn.pydata.org/tutorial/aesthetics.html#removing-axes-spines) (`sns.despine()`), [Temporarily setting figure style](https://seaborn.pydata.org/tutorial/aesthetics.html#temporarily-setting-figure-style), [Overriding elements](https://seaborn.pydata.org/tutorial/aesthetics.html#overriding-elements-of-the-seaborn-styles), [Scaling plot elements](https://seaborn.pydata.org/tutorial/aesthetics.html#scaling-plot-elements) (`set_context("paper" | "talk")`).
- 🔗 Put the result into `plotting_utils.py`.

### 12 — Choosing color palettes · 20 min
📄 https://seaborn.pydata.org/tutorial/color_palettes.html
- [x] [General principles](https://seaborn.pydata.org/tutorial/color_palettes.html#general-principles-for-using-color-in-plots): [Vary hue to distinguish categories](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-hue-to-distinguish-categories), [Vary luminance to represent numbers](https://seaborn.pydata.org/tutorial/color_palettes.html#vary-luminance-to-represent-numbers).
- [x] [Qualitative](https://seaborn.pydata.org/tutorial/color_palettes.html#qualitative-color-palettes) → [Sequential](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-palettes) ([Perceptually uniform](https://seaborn.pydata.org/tutorial/color_palettes.html#perceptually-uniform-palettes)) → [Diverging](https://seaborn.pydata.org/tutorial/color_palettes.html#diverging-color-palettes) (use this for a correlation heatmap).
- Try `sns.color_palette("colorblind")`.

### + `heatmap`: not in the tutorial, but on the roadmap · 10 min
📄 https://seaborn.pydata.org/generated/seaborn.heatmap.html
- [x] Read the parameters `annot`, `fmt`, `cmap`, `center=0`, `vmin`/`vmax`, `mask`, then run the examples at the bottom. Use it for chart #6: `sns.heatmap(df.corr(numeric_only=True), cmap="vlag", center=0, annot=True, fmt=".2f", ax=ax)`.

---

## 🛠️ What this module produces

> The reading is done; these build tasks use your own cleaned Week 6 data and are still open. Worked examples on the tutorial datasets are in notebooks [06](Notebook/06_Visualizing%20distributions.ipynb), [09](Notebook/09_Estimating%20regression%20fits.ipynb), [11](Notebook/11_Controlling%20figure%20aesthetics.ipynb) and [13](Notebook/13_heatmap%20API%20page.ipynb).

- [ ] One of each: `relplot`, `displot`, `catplot`, `pairplot`, `heatmap`, all on your cleaned Week 6 data
- [ ] At least one seaborn chart finished with matplotlib calls (`ax.annotate`, `ax.set_title`, spines), so you've crossed the seaborn → matplotlib boundary on purpose
- [ ] The chosen charts saved via `plotting_utils.save()` for P1
