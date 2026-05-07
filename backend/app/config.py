# backend/app/config.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEM_PATH = BASE_DIR / "data" / "nepal_dem.tif"