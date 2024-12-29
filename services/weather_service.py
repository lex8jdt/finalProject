from repositories import WeatherApiRepository
from flask import jsonify


class WeatherService:
    def __init__(self, weather_api_repository: WeatherApiRepository):
        self.weather_api_repository = weather_api_repository
    
    def get_forecast(self, latitude, longitude, yesterday):
        # Llama al servicio
        forecast_data = self.weather_api_repository.get_forecast(latitude, longitude, yesterday)
        try:
            forecast_data.raise_for_status()
            forecast_data = forecast_data.json()
        except Exception as e:
            return jsonify({"error": "No se pudo obtener el pronóstico"}), 500

        return forecast_data, 200
        
        
