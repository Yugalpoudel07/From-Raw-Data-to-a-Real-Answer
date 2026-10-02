"""Project-wide chart style (roadmap Week 7, build task 4).

    from src.plotting_utils import set_style, PALETTE, save
    set_style()
    fig, ax = plt.subplots(layout="constrained")
    ...
    save(fig, "fig1_score_bunching")
"""
import matplotlib.pyplot as plt
import seaborn as sns

from src.paths import FIGURES

# Okabe-Ito colour-blind-safe palette, plus a neutral grey for context
PALETTE = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "sky": "#56B4E9",
    "yellow": "#F0E442",
    "grey": "#9A9A9A",
    "dark": "#333333",
}
# The two groups compared in the analysis always get the same colours
GROUP_COLORS = {"A at initial": PALETTE["blue"], "A after re-inspection": PALETTE["red"]}


def set_style(context: str = "notebook") -> None:
    """Clean ticks style, no top/right spines, colour-blind palette, readable fonts."""
    sns.set_theme(
        style="ticks",
        context=context,
        palette=list(PALETTE.values())[:7],
        rc={
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titlesize": 13,
            "axes.titleweight": "bold",
            "axes.titlelocation": "left",
            "axes.labelsize": 11,
            "figure.dpi": 100,
            "savefig.dpi": 300,
        },
    )


def save(fig: plt.Figure, name: str) -> str:
    """Save a figure as figures/<name>.png at 300 dpi and return the path."""
    path = FIGURES / f"{name}.png"
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    return str(path)
