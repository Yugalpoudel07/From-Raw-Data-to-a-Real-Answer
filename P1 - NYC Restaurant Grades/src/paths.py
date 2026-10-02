"""One place for every file path, so notebooks and scripts agree."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # the project folder
RAW_CSV = ROOT / "data" / "raw" / "nyc_restaurants.csv"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"

for _p in (RAW_CSV.parent, PROCESSED, FIGURES, RESULTS):
    _p.mkdir(parents=True, exist_ok=True)
