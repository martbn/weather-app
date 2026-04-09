from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from app.models.weather import WeatherResponse

from app.services.weather_service import fetch_weather

app = FastAPI()

allowed_origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/weather", response_model=WeatherResponse)
def get_weather(city: str = Query(default="Oslo")) -> WeatherResponse:
    return fetch_weather(city)