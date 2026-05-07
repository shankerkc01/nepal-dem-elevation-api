# backend/app/interpolation.py

from app.raster_utils import get_pixel_value


def interpolate_elevation(latitude: float, longitude: float):

    """
    Basic nearest-neighbor interpolation.
    """

    elevation = get_pixel_value(latitude, longitude)

    return elevation