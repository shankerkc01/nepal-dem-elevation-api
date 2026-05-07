# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.interpolation import interpolate_elevation
from app.schemas import ElevationResponse

app = FastAPI(
    title="Nepal DEM Elevation API",
    version="1.0.0"
)


# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():

    return {
        "message": "Nepal DEM Elevation API"
    }


@app.get(
    "/elevation",
    response_model=ElevationResponse
)
def get_elevation(lat: float, lon: float):

    elevation = interpolate_elevation(
        latitude=lat,
        longitude=lon
    )

    return ElevationResponse(
        latitude=lat,
        longitude=lon,
        elevation=elevation
    )