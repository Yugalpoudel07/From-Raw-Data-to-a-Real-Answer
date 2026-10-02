"""Data-quality report and the cleaning steps for the NYC inspections file.

Every cleaning step is a small function that returns the new frame AND a
one-line reason, so the notebook can print a log with row counts before/after.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# --------------------------------------------------------------------------
# 1. data_quality_report(df)  — roadmap Week 6 build task
# --------------------------------------------------------------------------
def data_quality_report(df: pd.DataFrame, max_examples: int = 3) -> pd.DataFrame:
    """One row per column: type, missing values, unique values, outliers, type problems.

    Also prints the number of fully duplicated rows.
    """
    rows = []
    for col in df.columns:
        s = df[col]
        info = {
            "column": col,
            "dtype": str(s.dtype),
            "n_missing": int(s.isna().sum()),
            "pct_missing": round(100 * s.isna().mean(), 2),
            "n_unique": int(s.nunique(dropna=True)),
            "examples": " | ".join(str(v)[:30] for v in s.dropna().unique()[:max_examples]),
            "n_outliers_iqr": np.nan,
            "type_problem": "",
        }
        if pd.api.types.is_numeric_dtype(s):
            q1, q3 = s.quantile([0.25, 0.75])
            iqr = q3 - q1
            info["n_outliers_iqr"] = int(((s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)).sum())
            if (s < 0).any():
                info["type_problem"] = f"{int((s < 0).sum())} negative values"
        else:
            sample = s.dropna().astype(str).head(2000)
            as_num = pd.to_numeric(sample, errors="coerce").notna().mean()
            as_date = pd.to_datetime(sample, format="%m/%d/%Y", errors="coerce").notna().mean()
            if as_num > 0.95:
                info["type_problem"] = "numbers stored as text"
            elif as_date > 0.95:
                info["type_problem"] = "dates stored as text"
            elif sample.str.contains("Ã").any():
                info["type_problem"] = "mojibake (encoding) in text"
        rows.append(info)
    print(f"{len(df):,} rows x {df.shape[1]} columns | fully duplicated rows: {df.duplicated().sum():,}")
    return pd.DataFrame(rows).set_index("column")


# --------------------------------------------------------------------------
# 2. Cleaning steps (row-level file -> tidy tables)
# --------------------------------------------------------------------------
GRADE_CUTOFFS = [-np.inf, 13, 27, np.inf]          # DOHMH: 0-13 = A, 14-27 = B, 28+ = C
GRADE_LABELS = ["A", "B", "C"]


class CleaningLog:
    """Collects (step, reason, rows before, rows after) for the README table."""

    def __init__(self):
        self.steps = []

    def add(self, step: str, reason: str, before: int, after: int) -> None:
        self.steps.append({"step": step, "reason": reason,
                           "rows_before": before, "rows_after": after,
                           "rows_removed": before - after})

    def table(self) -> pd.DataFrame:
        return pd.DataFrame(self.steps)


def derive_grade(score: pd.Series) -> pd.Series:
    """Letter grade implied by a score, using the city's published cut-offs."""
    return pd.cut(score, GRADE_CUTOFFS, labels=GRADE_LABELS).astype("string")


def clean_rows(raw: pd.DataFrame, log: CleaningLog) -> pd.DataFrame:
    """Row-level cleaning (one row = one violation cited at one inspection)."""
    df = raw.copy()

    n = len(df)
    df = df.drop_duplicates()
    log.add("Drop exact duplicate rows",
            "Identical in every column, so they carry no extra information.", n, len(df))

    df["inspection_date"] = pd.to_datetime(df["inspection_date"], format="%m/%d/%Y")
    n = len(df)
    df = df[df["inspection_date"].dt.year > 1900]
    log.add("Drop 01/01/1900 'inspections'",
            "The data dictionary says 1/1/1900 means 'not yet inspected': these are new "
            "restaurants with no inspection, no score and no type.", n, len(df))

    n = len(df)
    df = df[df["inspection_date"] >= "2015-01-01"]
    log.add("Keep inspections from 2015 onward",
            "Only a few hundred stray rows before 2015 (the city keeps ~3 years per restaurant); "
            "a consistent 2015-2018 window avoids a thin, unrepresentative tail.", n, len(df))

    # Text fixes (no rows removed)
    df["cuisine_description"] = df["cuisine_description"].str.replace("CafÃ©", "Café", regex=False)
    zip_to_boro = (df[df["boro"] != "Missing"].groupby("zipcode")["boro"]
                   .agg(lambda s: s.mode().iat[0]))
    missing = df["boro"] == "Missing"
    df.loc[missing, "boro"] = df.loc[missing, "zipcode"].map(zip_to_boro)
    log.add("Fix text: 'CafÃ©' -> 'Café'; fill boro='Missing' from zip code",
            "Mojibake from a UTF-8 file read as Latin-1. 'Missing' boroughs all share zip 11249, "
            "which every other row places in Brooklyn.", len(df), len(df))

    df["score"] = df["score"].where(df["score"] >= 0)
    log.add("Set negative scores to missing",
            "A score counts violation points, so -1 is impossible; treated as 'not recorded'.",
            len(df), len(df))

    split = df["inspection_type"].str.split(" / ", n=1, expand=True)
    df["program"] = split[0]
    df["kind"] = split[1]
    df["zipcode"] = df["zipcode"].astype("Int64").astype("string")
    df["grade"] = df["grade"].where(df["grade"].isin(["A", "B", "C"]))  # Z, P, N = pending
    return df


def build_tables(rows: pd.DataFrame, log: CleaningLog):
    """Split the row-level file into three tidy tables.

    restaurants : one row per restaurant (camis)
    inspections : one row per inspection (camis + date + inspection_type)
    violations  : one row per violation cited at an inspection
    """
    restaurants = (rows.sort_values("inspection_date")
                   .groupby("camis", as_index=False)
                   .agg(dba=("dba", "last"), boro=("boro", "last"),
                        zipcode=("zipcode", "last"), cuisine=("cuisine_description", "last")))

    key = ["camis", "inspection_date", "inspection_type"]
    n_rows = len(rows)
    insp = (rows.groupby(key, as_index=False)
            .agg(program=("program", "first"), kind=("kind", "first"),
                 action=("action", "first"),
                 score=("score", "max"), n_scores=("score", "nunique"),
                 grade=("grade", lambda s: s.dropna().iat[0] if s.notna().any() else pd.NA),
                 n_violation_rows=("violation_code", "count")))
    log.add("Collapse to one row per inspection",
            "The raw file has one row per violation; score and grade belong to the inspection.",
            n_rows, len(insp))

    n = len(insp)
    insp = insp[insp["n_scores"] <= 1].drop(columns="n_scores")
    log.add("Drop inspections with two different scores",
            "A handful of inspections list conflicting scores; there is no way to tell which is "
            "final, and dropping them cannot move any result.", n, len(insp))

    graded = insp["program"].eq("Cycle Inspection") | insp["program"].str.startswith("Pre-permit")
    insp["derived_grade"] = derive_grade(insp["score"]).where(graded & insp["score"].notna())
    insp = insp.sort_values(["camis", "inspection_date"]).reset_index(drop=True)
    insp.insert(0, "inspection_id", np.arange(1, len(insp) + 1))

    violations = (rows.dropna(subset=["violation_code"])
                  .merge(insp[["inspection_id"] + key], on=key, how="inner", validate="many_to_one")
                  [["inspection_id", "violation_code", "violation_description", "critical_flag"]])
    return restaurants, insp, violations
