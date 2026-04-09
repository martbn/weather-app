import requests
from fastapi import HTTPException

OPEN_METEO_WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
OPEN_METEO_GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"


def get_coordinates(city: str) -> tuple[float, float]:
    try:
        response = requests.get(
            OPEN_METEO_GEOCODING_URL,
            params={"name": city, "count": 1},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch location data",
        ) from error

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"City '{city}' not found",
        )

    result = data["results"][0]
    return result["latitude"], result["longitude"]


def fetch_weather(city: str) -> dict:
    latitude, longitude = get_coordinates(city)

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,relative_humidity_2m_mean",
        "timezone": "auto",
    }

    try:
        response = requests.get(
            OPEN_METEO_WEATHER_URL,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch weather data",
        ) from error

    weather_data = response.json()

    return {
    "location": city,
    "current": {
        "temperature": weather_data["current"]["temperature_2m"],
        "wind_speed": weather_data["current"]["wind_speed_10m"],
    },
    "today": {
        "temperature_max": weather_data["daily"]["temperature_2m_max"][0],
        "temperature_min": weather_data["daily"]["temperature_2m_min"][0],
        "humidity_mean": weather_data["daily"]["relative_humidity_2m_mean"][0],
    },
}