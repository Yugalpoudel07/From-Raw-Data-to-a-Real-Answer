"""Analysis helpers: rebuild inspection cycles and compute cluster-bootstrap CIs.

The unit that repeats in this data is the RESTAURANT (the same place is
inspected again and again), so every confidence interval resamples whole
restaurants, not single inspections.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

A_MAX = 13          # a score of 0-13 earns an A
REINSPECT_DAYS = 120  # a re-inspection more than ~4 months later is not the same cycle


def cycle_inspections(insp: pd.DataFrame) -> pd.DataFrame:
    """Scored 'Cycle Inspection' initial and re-inspections, sorted by restaurant and date."""
    cyc = insp[(insp["program"] == "Cycle Inspection")
               & insp["kind"].isin(["Initial Inspection", "Re-inspection"])
               & insp["score"].notna()]
    return cyc.sort_values(["camis", "inspection_date"]).reset_index(drop=True)


def build_grade_events(cyc: pd.DataFrame, boro: pd.Series) -> pd.DataFrame:
    """One row per A grade, labelled by how it was earned, with the NEXT initial inspection.

    route = "A at initial"            initial inspection scored 0-13 (A straight away)
    route = "A after re-inspection"   initial scored 14+, the re-inspection (<=120 days later)
                                      scored 0-13, so the A was earned at the re-inspection
    next_score = score at the restaurant's next unannounced initial inspection
    """
    c = cyc.copy()
    g = c.groupby("camis", sort=False)
    # the inspection that follows each row, within the same restaurant
    c["next_kind"] = g["kind"].shift(-1)
    c["next_date"] = g["inspection_date"].shift(-1)
    c["next_row_score"] = g["score"].shift(-1)

    # for every row: the first INITIAL inspection strictly after it
    is_init = c["kind"].eq("Initial Inspection")
    c["_init_score"] = c["score"].where(is_init)
    c["_init_date"] = c["inspection_date"].where(is_init)
    after = c.groupby("camis", sort=False)[["_init_score", "_init_date"]].shift(-1)
    after = after.groupby(c["camis"], sort=False).bfill()
    c["next_init_score"] = after["_init_score"]
    c["next_init_date"] = after["_init_date"]

    init = c[is_init]
    a_first = init[init["score"] <= A_MAX].assign(
        route="A at initial", grade_date=lambda d: d["inspection_date"],
        next_score=lambda d: d["next_init_score"], next_date=lambda d: d["next_init_date"])

    failed = init[(init["score"] > A_MAX)
                  & init["next_kind"].eq("Re-inspection")
                  & ((init["next_date"] - init["inspection_date"]).dt.days <= REINSPECT_DAYS)
                  & (init["next_row_score"] <= A_MAX)]
    # the next initial after the RE-INSPECTION row = value stored on the re-inspection row
    reinsp_rows = c.loc[failed.index + 1]
    a_second = failed.assign(
        route="A after re-inspection",
        grade_date=reinsp_rows["inspection_date"].to_numpy(),
        next_score=reinsp_rows["next_init_score"].to_numpy(),
        next_date=reinsp_rows["next_init_date"].to_numpy())

    ev = pd.concat([a_first, a_second], ignore_index=True)
    ev = ev.rename(columns={"score": "initial_score"})
    ev["boro"] = ev["camis"].map(boro)
    ev["gap_days"] = (ev["next_date"] - ev["grade_date"]).dt.days
    ev["next_fail"] = (ev["next_score"] > A_MAX).astype(float).where(ev["next_score"].notna())
    cols = ["camis", "boro", "route", "inspection_date", "initial_score", "grade_date",
            "next_date", "next_score", "next_fail", "gap_days"]
    return ev[cols].sort_values(["camis", "inspection_date"]).reset_index(drop=True)


# --------------------------------------------------------------------------
# Cluster bootstrap (resample restaurants)
# --------------------------------------------------------------------------
def _cluster_sums(df: pd.DataFrame, value: str, by: str | None, cluster: str):
    """Per-cluster sums and counts, one column per level of `by`."""
    d = df.dropna(subset=[value])
    keys = [cluster] + ([by] if by else [])
    agg = d.groupby(keys, observed=True)[value].agg(["sum", "count"])
    if by:
        S = agg["sum"].unstack(by, fill_value=0)
        N = agg["count"].unstack(by, fill_value=0)
    else:
        S, N = agg[["sum"]], agg[["count"]]
        S.columns = N.columns = ["all"]
    return S, N


def cluster_bootstrap_means(df, value, by=None, cluster="camis", B=2000, seed=2026, chunk=250):
    """Mean of `value` per level of `by`, with 95% percentile CIs from a cluster bootstrap.

    Returns (summary DataFrame, draws DataFrame with B rows) so differences can be
    computed from the same resamples.
    """
    S, N = _cluster_sums(df, value, by, cluster)
    s, n = S.to_numpy(float), N.to_numpy(float)
    R = len(S)
    rng = np.random.default_rng(seed)
    draws = []
    for start in range(0, B, chunk):
        b = min(chunk, B - start)
        w = rng.multinomial(R, np.full(R, 1 / R), size=b)   # how often each restaurant is drawn
        draws.append((w @ s) / (w @ n))
    draws = pd.DataFrame(np.vstack(draws), columns=S.columns)
    est = pd.Series(s.sum(0) / n.sum(0), index=S.columns)
    summary = pd.DataFrame({
        "estimate": est,
        "ci_low": draws.quantile(0.025),
        "ci_high": draws.quantile(0.975),
        "n_obs": n.sum(0).astype(int),
        "n_restaurants": (n > 0).sum(0),
    })
    return summary, draws


def diff_ci(draws: pd.DataFrame, a: str, b: str, estimate: float) -> dict:
    """Difference a - b with a 95% CI from paired bootstrap draws."""
    d = draws[a] - draws[b]
    return {"estimate": estimate, "ci_low": d.quantile(0.025), "ci_high": d.quantile(0.975)}


def fmt_ci(est, lo, hi, pct=False, digits=1):
    """'12.3 (95% CI 11.8 to 12.9)' — or percentages if pct=True."""
    if pct:
        return f"{100*est:.{digits}f}% (95% CI {100*lo:.{digits}f}% to {100*hi:.{digits}f}%)"
    return f"{est:.{digits}f} (95% CI {lo:.{digits}f} to {hi:.{digits}f})"
