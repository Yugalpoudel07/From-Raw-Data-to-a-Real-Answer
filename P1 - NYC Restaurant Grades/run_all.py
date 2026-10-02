"""Reproduce the whole project in one command:   python run_all.py

1. downloads and checks the raw data            (src/download_data.py)
2. runs notebooks/01_data_quality_and_cleaning  (writes data/processed/)
3. runs notebooks/02_analysis_and_figures       (writes figures/ and results/)

The notebooks are executed in place, so their saved outputs are refreshed.
Takes about 2 minutes after the download.
"""
import subprocess
import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent
NOTEBOOKS = ["01_data_quality_and_cleaning.ipynb", "02_analysis_and_figures.ipynb"]


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "src" / "download_data.py")], check=True)
    for name in NOTEBOOKS:
        path = ROOT / "notebooks" / name
        t0 = time.time()
        print(f"Running {name} ...", flush=True)
        nb = nbformat.read(path, as_version=4)
        NotebookClient(nb, timeout=1200, kernel_name="python3",
                       resources={"metadata": {"path": str(path.parent)}}).execute()
        nbformat.write(nb, path)
        print(f"  done in {time.time() - t0:.0f}s")
    print("\nFinished. Figures are in figures/, key numbers in results/key_numbers.json.")


if __name__ == "__main__":
    main()
