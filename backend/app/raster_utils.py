# backend/app/raster_utils.py

import rasterio

from rasterio.transform import rowcol

from app.config import DEM_PATH


# Open raster once during application lifetime
dataset = rasterio.open(DEM_PATH)


def get_pixel_value(latitude: float, longitude: float):

    """
    Get nearest DEM pixel value from geographic coordinates.
    """

    row, col = rowcol(
        dataset.transform,
        longitude,
        latitude
    )

    band1 = dataset.read(1)

    elevation = band1[row, col]

    return float(elevation)