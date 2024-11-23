from flask import Flask, request, jsonify, render_template
from services.weatherService import WeatherService
from services.coordinatesService import CoordinatesService

app = Flask(__name__)

# Inicializa el servicio con tu clave de API
weather_service = WeatherService(api_key="df382b05ec56493b865063e984862441")
coordinates_service = CoordinatesService()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/forecast', methods=['GET'])
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

if __name__ == '__main__':
    app.run(debug=True)


