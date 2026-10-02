# Data

| | |
| :-- | :-- |
| **Publisher** | NYC Department of Health and Mental Hygiene (DOHMH) |
| **Dataset** | [DOHMH New York City Restaurant Inspection Results](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j) (NYC Open Data) |
| **Copy used** | 300,000 rows sampled at random (seed 20181209) from the December 2018 extract, published by [TidyTuesday 2018-12-11](https://github.com/rfordatascience/tidytuesday/tree/master/data/2018/2018-12-11) because the full file exceeds GitHub's 100 MB limit |
| **File** | `raw/nyc_restaurants.csv`, 96.4 MB, SHA-256 `eccfb95d019476578c31d177fabca45623a28c3abb8bb4b4e3fa46cb77694c73` |
| **Get it** | `python src/download_data.py` (downloads and verifies the checksum) |
| **Licence** | NYC Open Data terms of use (public, free to reuse) |

`raw/` and `processed/` are not committed to git; both are re-created by `python run_all.py`.

## Raw columns (one row = one violation cited at one inspection)

| Column | Meaning |
| :-- | :-- |
| `camis` | restaurant ID (permit), constant per restaurant |
| `dba` | business name |
| `boro`, `zipcode` | location (`boro` can be the text `Missing`) |
| `cuisine_description` | cuisine, chosen by the restaurant |
| `inspection_date` | `MM/DD/YYYY`; `01/01/1900` = not yet inspected |
| `action` | what happened (violations cited, closed, re-opened...) |
| `violation_code`, `violation_description`, `critical_flag` | one violation per row |
| `score` | total violation points **for the whole inspection** (lower is better) |
| `grade` | A / B / C; Z or P = grade pending; N / Not Yet Graded |
| `inspection_type` | program / kind, e.g. `Cycle Inspection / Initial Inspection` |

## Processed tables (written by notebook 01)

| File | One row per | Key columns |
| :-- | :-- | :-- |
| `restaurants.csv` | restaurant | `camis`, `dba`, `boro`, `zipcode`, `cuisine` |
| `inspections.csv` | inspection | `inspection_id`, `camis`, `inspection_date`, `program`, `kind`, `score`, `grade`, `derived_grade` |
| `violations.csv` | violation at an inspection | `inspection_id`, `violation_code`, `critical_flag` |
| `nyc_inspections.duckdb` | the same three tables in a DuckDB database (for SQL) | |
| `cleaning_log.csv` | cleaning step | reason, rows before / after |
