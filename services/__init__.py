from weather_service import WeatherService
from coordinates_service import CoordinatesService
import config as cfg

weather_service = WeatherService(api_key=cfg.WEATHER_API_KEY)
coordinates_service = CoordinatesService()