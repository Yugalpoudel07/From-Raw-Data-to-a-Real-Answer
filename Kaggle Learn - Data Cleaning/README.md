[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [⏮️ **Previous module: Kaggle Learn — Pandas**](../Kaggle%20Learn%20-%20Pandas/README.md)

---

# 🧹 Kaggle Learn — Data Cleaning (Week 6)

### *Five messy real datasets, five exercise notebooks, one certificate*

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)](#-certificate)
[![Lessons](https://img.shields.io/badge/Lessons-5%20of%205-blue?style=flat-square)](#-the-five-lessons)
[![Checks](https://img.shields.io/badge/Exercise_checks-18%20of%2018%20correct-success?style=flat-square)](#-the-five-lessons)
[![Certificate](https://img.shields.io/badge/Kaggle-Certificate_earned-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](#-certificate)
[![Course](https://img.shields.io/badge/Course-kaggle.com%2Flearn%2Fdata--cleaning-lightgrey?style=flat-square)](https://www.kaggle.com/learn/data-cleaning)

> [!NOTE]
> **Roadmap assignment:** the free [Kaggle Learn Data Cleaning course](https://www.kaggle.com/learn/data-cleaning): missing values, scaling and normalisation, dates, character encodings and inconsistent text entries.
> **Why it matters for this repo:** the repo's second rule is *"every cleaning decision has a reason"*. Each lesson here is one kind of decision, made on a **different real, messy dataset**, so the reasons are practised on data that actually fights back.

---

## 🏆 Certificate

<p align="center">
  <img src="kaggle-data-cleaning-certificate.png" alt="Kaggle Learn certificate of completion: Data Cleaning, awarded to Yugal Poudel on October 1, 2026" width="760">
</p>

<p align="center"><b>Certificate of Completion: Data Cleaning</b> · Kaggle Learn · awarded <b>1 October 2026</b></p>

---

## 📚 The five lessons

| # | Lesson | Exercise notebook | Dataset | Checks | Core moves practised |
| :-: | :--- | :--- | :--- | :-: | :--- |
| 1 | Handling Missing Values | [`01_handling-missing-values`](Notebooks/01_handling-missing-values.ipynb) | San Francisco Building Permits | ✅ 6 / 6 | `isnull().sum()`, % of cells missing, *why* a value is missing, `dropna()` on rows vs `dropna(axis=1)`, back-fill then `fillna(0)` |
| 2 | Scaling and Normalization | [`02_scaling-and-normalization`](Notebooks/02_scaling-and-normalization.ipynb) | Kickstarter Projects | ✅ 2 / 2 | Min-max **scaling** (changes the range) vs Box-Cox **normalisation** (changes the shape); positive values only for Box-Cox |
| 3 | Parsing Dates | [`03_parsing-dates`](Notebooks/03_parsing-dates.ipynb) | Significant Earthquakes 1965–2016 (+ Volcanic Eruptions) | ✅ 4 / 4 | Spotting `object` dates, finding malformed rows by string length, `pd.to_datetime(format=...)`, `.dt.day`, a histogram to sanity-check the parse |
| 4 | Character Encodings | [`04_character-encodings`](Notebooks/04_character-encodings.ipynb) | Fatal Police Shootings in the US | ✅ 3 / 3 | `bytes` vs `str`, `.decode()` / `.encode()`, `read_csv(encoding="windows-1252")`, guessing with `charset_normalizer`, saving as UTF-8 |
| 5 | Inconsistent Data Entry | [`05_inconsistent-data-entry`](Notebooks/05_inconsistent-data-entry.ipynb) | Pakistan Intellectual Capital | ✅ 3 / 3 | `unique()` to find near-duplicates, `.str.lower()` / `.str.strip()`, fuzzy matching with `fuzzywuzzy` and a replace-above-a-threshold function |
| | **Total** | **5 notebooks** | **5 datasets** | ✅ **18 / 18** | |

*Hint/solution cells are left commented out; every "Correct" in the notebooks was earned on the check.*

---

## 🔍 Cleaning decisions worth remembering

* **Ask *why* before you drop or fill.** A missing *Street Number Suffix* most likely **doesn't exist**; a missing *Zipcode* simply **wasn't recorded**. Same `NaN`, different decisions.
* **`dropna()` can delete everything.** On the building-permits data, dropping every row with a missing value leaves **zero rows**. Dropping columns instead keeps all the rows but loses whole variables, so either way the before/after counts must be printed.
* **Scaling ≠ normalisation.** Min-max scaling keeps the distribution's shape and squeezes it into 0–1; Box-Cox reshapes a heavily skewed variable (Kickstarter pledges) towards a bell curve.
* **Find bad dates by their shape.** In the earthquake data, 23,409 `Date` strings are 10 characters long and 3 are 24 (rows 3378, 7512, 20650: full timestamps). Fixing those three first lets one explicit `format="%m/%d/%Y"` parse every row; a histogram of day-of-month should then look flat.
* **An encoding detector is only a guess.** `charset_normalizer` read the first 10,000 bytes of the police-shootings file and said *ascii* with full confidence, but the file only loads as **`windows-1252`**. The bad bytes were further down.
* **Normalise text before matching it.** Lower-casing and stripping spaces merges entries like *"University of Central Florida"* and *" University of Central Florida"*; fuzzy matching (ratio ≥ 70) then merges spelling variants such as `usa` / `usofa`.

---

## 🔄 Code that needs updating for pandas 3.0

The course code still runs on Kaggle's older stack. In this repo's pandas 3.0 / NumPy 2 setup, three lines in these notebooks would warn or fail:

| In the notebook | Problem | Use instead |
| :--- | :--- | :--- |
| `sf_permits.fillna(method="bfill", axis=0).fillna(0)` | `fillna(method=...)` is deprecated (and removed in pandas 3.0) | `sf_permits.bfill().fillna(0)` |
| `np.product(sf_permits.shape)` | `np.product` was removed in NumPy 2.0 | `np.prod(sf_permits.shape)` or `sf_permits.size` |
| `sns.distplot(..., kde=False, bins=31)` | `distplot` is deprecated in seaborn | `sns.histplot(..., bins=31)` |

---

## 🔗 How it maps onto the rest of the repo

| Kaggle lesson | Related work in this repo | What it adds |
| :--- | :--- | :--- |
| 1 · Missing values | [Kaggle Pandas 05 — Data types and missing values](../Kaggle%20Learn%20-%20Pandas/Notebooks/05_data-types-and-missing-values.ipynb) · [pandas User Guide → *Working with missing data*](../pandas%20-%20official%20User%20Guide/README.md#-bridge-pages-week-6-topics-outside-the-5-assigned-pages-only-if-you-have-time) | The "why is it missing?" question that decides between drop, fill and flag |
| 3 · Parsing dates | [User Guide 07 — Time series + rolling windows](../pandas%20-%20official%20User%20Guide/Notebook/07_Time%20series%20%20rolling%20windows.ipynb) | `format=`, `errors="coerce"`, resampling once the dates are real dates |
| 2 · Scaling and normalization | [StatQuest — CLT and the t-test](../StatQuest%20-%20hypothesis%20testing%20set/06-central-limit-theorem-and-the-t-test.md) | When the shape of a distribution matters for a test, and when it doesn't |
| 5 · Inconsistent data entry | [SQL — String functions & wrangling](../SQL%20Tutorial%20for%20Data%20Analysis%20%28Mode%20%20ThoughtSpot%29/practice-mode-tutorial/string_functions_and_wrangling_notes.md) | The same `LOWER` / `TRIM` clean-up, done in pandas |
| All five | [The final analysis checklist](../README.md#%EF%B8%8F-what-this-repo-will-build) | "A genuinely messy public dataset, cleaned completely, with a reason next to every decision" |

---

## 📂 Folder contents

```text
Kaggle Learn - Data Cleaning/
├── README.md                                   # This page
├── kaggle-data-cleaning-certificate.png        # Certificate of completion (1 Oct 2026)
└── Notebooks/
    ├── 01_handling-missing-values.ipynb
    ├── 02_scaling-and-normalization.ipynb
    ├── 03_parsing-dates.ipynb
    ├── 04_character-encodings.ipynb
    └── 05_inconsistent-data-entry.ipynb
```

> [!TIP]
> The notebooks were run on Kaggle, where the datasets and the `learntools` answer checker are already attached. To rerun one, open the lesson from the [course page](https://www.kaggle.com/learn/data-cleaning); locally, the `q1.check()` cells and `../input/...` paths will not work.

---

[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [⏮️ **Previous module: Kaggle Learn — Pandas**](../Kaggle%20Learn%20-%20Pandas/README.md)
