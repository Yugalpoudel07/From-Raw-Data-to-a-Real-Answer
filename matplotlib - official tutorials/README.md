[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [⏮️ **pandas**](../pandas%20-%20official%20User%20Guide/README.md) &nbsp;•&nbsp; [**Next: seaborn** ⏭️](../seaborn%20-%20official%20tutorial/README.md)

---

# 📊 matplotlib — official tutorials (Week 7)

### *Stop using `plt.something()`. Learn the Figure → Axes → Artist tree once.*

[![Time](https://img.shields.io/badge/Time_budget-6_hrs-blue?style=flat-square)](#)
[![Version](https://img.shields.io/badge/matplotlib-3.11-11557c?style=flat-square)](https://matplotlib.org/stable/)
[![Steps](https://img.shields.io/badge/Steps-7_pages-purple?style=flat-square)](#-the-study-path)

> [!NOTE]
> **Roadmap assignment:** Quick Start Guide · the Artist tutorial (**read it twice**) · the Layout guide (constrained_layout / tight_layout). **Skip:** browsing the gallery for now.
> **What you produce:** eight chart types, all built with `fig, ax = plt.subplots()`.
>
> I added three short pages (Lifecycle of a Plot, Annotations, Choosing Colormaps) because Week 7 asks for annotation and colour-blind-safe colour, and the three core pages only touch on them. Together they still fit in 6 hours.

---

## 🗺️ The study path

| Step | Page | Time | Status |
| :-: | :--- | :-: | :-: |
| 1 | Quick start guide | 1 h 30 | ☐ |
| 2 | The Lifecycle of a Plot *(bridge)* | 45 min | ☐ |
| 3 | ⭐ Artist tutorial, read twice | 1 h 30 | ☐ |
| 4 | Constrained layout guide + Tight layout guide | 1 h | ☐ |
| 5 | Arranging multiple Axes (subplots, mosaic) | 30 min | ☐ |
| 6 | Annotations *(bridge)* | 30 min | ☐ |
| 7 | Choosing Colormaps *(bridge)* | 15 min | ☐ |
| | **Total** | **6 h** | |

---

### Step 1 — Quick start guide · 1 h 30
📄 https://matplotlib.org/stable/users/explain/quick_start.html

- [ ] 1. [A simple example](https://matplotlib.org/stable/users/explain/quick_start.html#a-simple-example): `fig, ax = plt.subplots()` then `ax.plot(...)`.
- [ ] 2. ⭐ [Parts of a Figure](https://matplotlib.org/stable/users/explain/quick_start.html#parts-of-a-figure): [Figure](https://matplotlib.org/stable/users/explain/quick_start.html#figure), [Axes](https://matplotlib.org/stable/users/explain/quick_start.html#axes), [Axis](https://matplotlib.org/stable/users/explain/quick_start.html#axis), [Artist](https://matplotlib.org/stable/users/explain/quick_start.html#artist). **Study the labelled "anatomy" image until you can draw it from memory.**
- [ ] 3. [Types of inputs to plotting functions](https://matplotlib.org/stable/users/explain/quick_start.html#types-of-inputs-to-plotting-functions): passing a DataFrame with `data=`.
- [ ] 4. ⭐ [Coding styles → The explicit and the implicit interfaces](https://matplotlib.org/stable/users/explain/quick_start.html#the-explicit-and-the-implicit-interfaces): OO (`ax.`) vs pyplot (`plt.`). This is **the 80% fix** from the roadmap. Then [Making a helper function](https://matplotlib.org/stable/users/explain/quick_start.html#making-a-helper-functions): a function that takes `ax` and returns artists. This is the seed of your `plotting_utils.py`.
- [ ] 5. [Styling Artists](https://matplotlib.org/stable/users/explain/quick_start.html#styling-artists): [Colors](https://matplotlib.org/stable/users/explain/quick_start.html#colors), [Linewidths, linestyles, markersizes](https://matplotlib.org/stable/users/explain/quick_start.html#linewidths-linestyles-and-markersizes).
- [ ] 6. [Labelling plots](https://matplotlib.org/stable/users/explain/quick_start.html#labelling-plots): [Axes labels and text](https://matplotlib.org/stable/users/explain/quick_start.html#axes-labels-and-text), [Annotations](https://matplotlib.org/stable/users/explain/quick_start.html#annotations), [Legends](https://matplotlib.org/stable/users/explain/quick_start.html#legends).
- [ ] 7. [Axis scales and ticks](https://matplotlib.org/stable/users/explain/quick_start.html#axis-scales-and-ticks): [Scales](https://matplotlib.org/stable/users/explain/quick_start.html#scales) (log), [Tick locators and formatters](https://matplotlib.org/stable/users/explain/quick_start.html#tick-locators-and-formatters), [Plotting dates and strings](https://matplotlib.org/stable/users/explain/quick_start.html#plotting-dates-and-strings), [Additional Axis objects](https://matplotlib.org/stable/users/explain/quick_start.html#additional-axis-objects) (`twinx`: learn it, then learn why to avoid it).
- [ ] 8. [Color mapped data](https://matplotlib.org/stable/users/explain/quick_start.html#color-mapped-data): [Colormaps](https://matplotlib.org/stable/users/explain/quick_start.html#colormaps), [Normalizations](https://matplotlib.org/stable/users/explain/quick_start.html#normalizations), [Colorbars](https://matplotlib.org/stable/users/explain/quick_start.html#colorbars).
- [ ] 9. [Working with multiple Figures and Axes](https://matplotlib.org/stable/users/explain/quick_start.html#working-with-multiple-figures-and-axes): `subplot_mosaic`.

**Skip:** Using mathematical expressions in text.

---

### Step 2 — The Lifecycle of a Plot · 45 min *(bridge)*
📄 https://matplotlib.org/stable/tutorials/lifecycle.html

One bar chart taken from raw data to a finished, saved figure using the OO API only. It is the Quick Start ideas used on a real chart. **Type along with your own data.**

- [ ] 1. [Getting started](https://matplotlib.org/stable/tutorials/lifecycle.html#getting-started): `ax.barh`.
- [ ] 2. [Controlling the style](https://matplotlib.org/stable/tutorials/lifecycle.html#controlling-the-style): `plt.style.use`.
- [ ] 3. [Customizing the plot](https://matplotlib.org/stable/tutorials/lifecycle.html#customizing-the-plot): `ax.set(...)`, `FuncFormatter` for tick labels.
- [ ] 4. [Combining multiple visualizations](https://matplotlib.org/stable/tutorials/lifecycle.html#combining-multiple-visualizations): add a mean line and text.
- [ ] 5. [Saving our plot](https://matplotlib.org/stable/tutorials/lifecycle.html#saving-our-plot): `fig.savefig(..., dpi=300, bbox_inches="tight")`.

---

### Step 3 — ⭐ Artist tutorial · 1 h 30 · **read twice**
📄 https://matplotlib.org/stable/tutorials/artists.html

- [ ] 1. **The intro (before the first heading):** the three layers (FigureCanvas → Renderer → Artist), and *primitives* (Line2D, Rectangle, Text) vs *containers* (Figure, Axes, Axis). **Read this part twice.**
- [ ] 2. [Customizing your objects](https://matplotlib.org/stable/tutorials/artists.html#customizing-your-objects): every artist has `get_*` / `set_*`. Learn `fig.patch`, `ax.patch`, and the property table (alpha, color, visible, zorder...).
- [ ] 3. [Object containers](https://matplotlib.org/stable/tutorials/artists.html#object-containers).
- [ ] 4. [Figure container](https://matplotlib.org/stable/tutorials/artists.html#figure-container): `fig.axes`, `fig.texts`, `fig.legends`.
- [ ] 5. ⭐ [Axes container](https://matplotlib.org/stable/tutorials/artists.html#axes-container): `ax.lines`, `ax.patches`, `ax.texts`, and the table mapping helper methods (`ax.plot` → Line2D, `ax.bar` → Rectangle...) to the artists they create.
- [ ] 6. [Axis containers](https://matplotlib.org/stable/tutorials/artists.html#axis-containers): `ax.xaxis`, tick locators/formatters, `get_ticklabels()`. Then do `ax.spines[["top", "right"]].set_visible(False)` yourself.

**Exercise:** make any chart, then use only `get_*`/`set_*` on the objects in `ax.lines`, `ax.patches` and `ax.xaxis` to recolour one bar, hide two spines and rotate the tick labels. When that works, the Artist tree makes sense.

---

### Step 4 — Layout guides · 1 h
📄 https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html *(45 min)*

- [ ] 1. [Simple example](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#simple-example): `plt.subplots(layout="constrained")`.
- [ ] 2. [Colorbars](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#colorbars), [Suptitle](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#suptitle), [Legends](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#legends) (legend outside the axes).
- [ ] 3. [Padding and spacing](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#padding-and-spacing): `fig.get_layout_engine().set(w_pad=..., hspace=...)`.
- [ ] 4. [Use with GridSpec](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#use-with-gridspec) and ["compressed" layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#grids-of-fixed-aspect-ratio-axes-compressed-layout).
- [ ] 5. Skim [Limitations](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#limitations).

**Skip:** rcParams, manually setting positions, Debugging, Notes on the algorithm.

📄 https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html *(15 min)*
- [ ] 6. [Simple example](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#simple-example) + [Caveats](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#caveats): know what `fig.tight_layout()` does and why constrained layout is the better default.

---

### Step 5 — Arranging multiple Axes · 30 min
📄 https://matplotlib.org/stable/users/explain/axes/arranging_axes.html
*(Needed for "subplots, shared axes" and the **small multiples** chart.)*

- [ ] 1. [Basic 2x2 grid](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#basic-2x2-grid): `plt.subplots(2, 2, sharex=True, sharey=True)`.
- [ ] 2. [Axes spanning rows or columns](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#axes-spanning-rows-or-columns-in-a-grid): `subplot_mosaic("AAB;CCB")`.
- [ ] 3. [Variable widths or heights](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#variable-widths-or-heights-in-a-grid): `width_ratios`.
- [ ] 4. [Nested Axes layouts](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#nested-axes-layouts): skim.

**Skip:** everything under "Low-level and advanced grid methods".

---

### Step 6 — Annotations · 30 min *(bridge: "a chart that makes an argument")*
📄 https://matplotlib.org/stable/users/explain/text/annotations.html

- [ ] 1. [Annotating data](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-data): `ax.annotate(text, xy=, xytext=)`.
- [ ] 2. [Annotating with arrows](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-with-arrows): `arrowprops`.
- [ ] 3. [Placing text annotations relative to data](https://matplotlib.org/stable/users/explain/text/annotations.html#placing-text-annotations-relative-to-data): `textcoords="offset points"`.
- [ ] 4. [Annotating with boxed text](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-with-boxed-text).
- [ ] 5. Skim [Coordinate systems for annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#coordinate-systems-for-annotations): know `xycoords="axes fraction"`.

**Skip:** custom box styles, ConnectionPatch, zoom effect.

---

### Step 7 — Choosing Colormaps · 15 min *(bridge: colour-blind-safe, "why rainbow is wrong")*
📄 https://matplotlib.org/stable/users/explain/colors/colormaps.html

- [ ] 1. [Classes of colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#classes-of-colormaps): [Sequential](https://matplotlib.org/stable/users/explain/colors/colormaps.html#sequential) (amounts), [Diverging](https://matplotlib.org/stable/users/explain/colors/colormaps.html#diverging) (± around a midpoint), [Qualitative](https://matplotlib.org/stable/users/explain/colors/colormaps.html#qualitative) (categories).
- [ ] 2. [Lightness of Matplotlib colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#lightness-of-matplotlib-colormaps): why `jet`/rainbow create fake boundaries.
- [ ] 3. [Color vision deficiencies](https://matplotlib.org/stable/users/explain/colors/colormaps.html#color-vision-deficiencies).

---

## 🎯 The eight charts (roadmap build task 1): what to use for each

Build each one from your **Week 6 cleaned data**, always starting with `fig, ax = plt.subplots(layout="constrained")`.

| # | Chart | Core calls | Page that teaches it |
| :-: | :--- | :--- | :--- |
| 1 | Histogram + density curve | `ax.hist(x, density=True)` + KDE line (`scipy.stats.gaussian_kde` or `sns.kdeplot(ax=ax)`) | Quick start · seaborn distributions |
| 2 | Box or violin plot | `ax.boxplot` / `ax.violinplot` | Quick start |
| 3 | Scatter + trend line | `ax.scatter` + `np.polyfit` → `ax.plot` | Quick start |
| 4 | Grouped bars | `ax.bar(x + offset, ...)` per group, `ax.set_xticks` | Lifecycle of a Plot |
| 5 | Time series + annotated events | `ax.plot(dates, y)` + `ax.annotate` / `ax.axvline` | Quick start (dates) · Annotations |
| 6 | Correlation heatmap | `ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1)` + `fig.colorbar` | Quick start (colormaps) · Choosing Colormaps |
| 7 | Small multiples | `plt.subplots(2, 3, sharex=True, sharey=True)`, loop over `axs.flat` | Arranging multiple Axes |
| 8 | Cumulative distribution | `ax.ecdf(x)` | Quick start |

**Also this week:**
- [ ] `plotting_utils.py`: `set_style()` (rcParams: font sizes, no top/right spines), a colour-blind-safe palette, and `save(fig, name)` → `fig.savefig(f"figures/{name}.png", dpi=300, bbox_inches="tight")`
- [ ] The **argument figure**: the title states the conclusion, one `ax.annotate` arrow points at the evidence, everything else grey. Use the [Storytelling with Data module](../Storytelling%20with%20Data%20%28Cole%20Nussbaumer%20Knaflic%29/README.md) for the design side.
- [ ] Bad chart → reproduce → fix → 150 words on what you changed and why

**Later, not now:** the [gallery](https://matplotlib.org/stable/gallery/index.html), Pyplot tutorial, Image tutorial, animations, transforms, paths.
