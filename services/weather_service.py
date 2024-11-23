from repositories import WeatherApiRepository, CoordinatesApiRepository
from flask import jsonify


class WeatherService:
    def __init__(self, weather_api_repository: WeatherApiRepository, coordinates_api_repository: CoordinatesApiRepository):
        self.weather_api_repository = weather_api_repository
        self.coordinates_api_repository = coordinates_api_repository
    
    def get_forecast(self, city_name):
        city = city_name

        if not city:
            return jsonify({"error": "Se requiere el parámetro 'city'"}), 400

            # Llama al servicio de Nominatim
        location_data = self.coordinates_api_repository.get_coordinates(city)
        if location_data is None:
            return jsonify({"error": "No se pudo obtener la ubicación"}), 500

        lat = location_data[0]["lat"]
        lon = location_data[0]["lon"]

        # Validación de parámetros
        if not lat or not lon:
            return jsonify({"error": "Se requieren los parámetros 'lat' y 'lon'"}), 400

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            return jsonify({"error": "Los parámetros 'lat' y 'lon' deben ser números válidos"}), 400

        # Llama al servicio
        forecast_data = self.weather_api_repository.get_forecast(lat, lon)
        if forecast_data is None:
            return jsonify({"error": "No se pudo obtener el pronóstico"}), 500

        return jsonify(forecast_data)
