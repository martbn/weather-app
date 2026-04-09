from pydantic import BaseModel


class CurrentWeather(BaseModel):
    temperature: float
    wind_speed: float


class TodayWeather(BaseModel):
    temperature_max: float
    temperature_min: float
    humidity_mean: float


class WeatherResponse(BaseModel):
    location: str
    current: CurrentWeather
    today: TodayWeather