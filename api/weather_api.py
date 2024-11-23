from flask import Blueprint, request, jsonify
import services.coordinates_service as coordinates_service
import services.weather_service as weather_service

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route('/forecast', methods=['GET'])
def get_forecast():

    city = request.args.get('ciudad')

    if not city:
        return jsonify({"error": "Se requiere el parámetro 'city'"}), 400

        # Llama al servicio de Nominatim
    location_data = coordinates_service.get_coordinates(city)
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
    forecast_data = weather_service.get_forecast(lat, lon)
    if forecast_data is None:
        return jsonify({"error": "No se pudo obtener el pronóstico"}), 500

    return jsonify(forecast_data)