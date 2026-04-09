import requests
from fastapi import HTTPException

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
OSLO_LATITUDE = 59.9139
OSLO_LONGITUDE = 10.7522


def fetch_oslo_weather() -> dict:
    params = {
        "latitude": OSLO_LATITUDE,
        "longitude": OSLO_LONGITUDE,
        "current": "temperature_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
    }

    try:
        response = requests.get(OPEN_METEO_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch weather data from external API",
        ) from error

    weather_data = response.json()

    return {
        "location": "Oslo",
        "current": {
            "temperature": weather_data["current"]["temperature_2m"],
            "wind_speed": weather_data["current"]["wind_speed_10m"],
        },
        "today": {
            "temperature_max": weather_data["daily"]["temperature_2m_max"][0],
            "temperature_min": weather_data["daily"]["temperature_2m_min"][0],
        },
    }