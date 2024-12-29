from .weather_service import WeatherService
from .location_service import LocationService
from .flight_service import FlightService
from .search_service import SearchService

from repositories import weather_api_repository, location_api_repository, flight_api_repository


weather_service = WeatherService(weather_api_repository)
location_service = LocationService(location_api_repository)
flight_service = FlightService(flight_api_repository)
search_service = SearchService(location_api_repository, flight_api_repository, weather_api_repository)