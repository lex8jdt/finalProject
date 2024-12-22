from repositories import WeatherApiRepository, LocationApiRepository
from flask import jsonify


class WeatherService:
    def __init__(self, weather_api_repository: WeatherApiRepository, location_api_repository: LocationApiRepository):
        self.weather_api_repository = weather_api_repository
        self.location_api_repository = location_api_repository
    
    def get_forecast(self, city_name):
        city = city_name

        if not city:
            return jsonify({"error": "Se requiere el parámetro 'city'"}), 400

            # Llama al servicio de Nominatim
        location_data = self.location_api_repository.get_coordinates(city)
        try:
            location_data.raise_for_status()
            location_data = location_data.json()
        except Exception as e:
            print(f"Error en la solicitud: {e}")
            return jsonify({"error": "No se pudo obtener la ubicación"}), 500

        lat = location_data[0]["lat"]
        lon = location_data[0]["lon"]

        print(f"Ubicación encontrada: {lat}, {lon}")

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
        try:
            forecast_data.raise_for_status()
            forecast_data = forecast_data.json()
        except Exception as e:
            return jsonify({"error": "No se pudo obtener el pronóstico"}), 500

        return forecast_data, 200
