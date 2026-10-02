"""Download the raw data (96 MB) and check it is the exact file the analysis used.

Run from the project folder:   python src/download_data.py
"""
import hashlib
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.paths import RAW_CSV  # noqa: E402

URL = ("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/"
       "data/2018/2018-12-11/nyc_restaurants.csv")
SHA256 = "eccfb95d019476578c31d177fabca45623a28c3abb8bb4b4e3fa46cb77694c73"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if RAW_CSV.exists() and sha256(RAW_CSV) == SHA256:
        print(f"Already downloaded and verified: {RAW_CSV}")
        return
    print(f"Downloading {URL}\n  -> {RAW_CSV}  (about 96 MB)")
    urllib.request.urlretrieve(URL, RAW_CSV)
    got = sha256(RAW_CSV)
    if got != SHA256:
        raise SystemExit(f"Checksum mismatch: expected {SHA256}, got {got}. "
                         "The source file has changed; results may differ.")
    print("Download complete, checksum OK.")


if __name__ == "__main__":
    main()
