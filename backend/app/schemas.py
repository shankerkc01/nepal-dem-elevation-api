# backend/app/schemas.py

from pydantic import BaseModel


class ElevationResponse(BaseModel):

    latitude: float
    longitude: float
    elevation: float