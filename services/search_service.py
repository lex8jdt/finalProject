from repositories import LocationApiRepository, FlightApiRepository, WeatherApiRepository
from flask import jsonify, render_template
import json
import datetime

class SearchService:

    def __init__(self, location_api_repository: LocationApiRepository, flight_api_repository: FlightApiRepository, weather_api_repository: WeatherApiRepository):
        self.location_api_repository = location_api_repository
        self.flight_api_repository = flight_api_repository
        self.weather_api_repository = weather_api_repository

    def get_search(self, origin, destination):
        now = datetime.datetime.now()    
        yesterday = datetime.datetime(now.year, now.month, now.day) - datetime.timedelta(days=1)    

        #Obtenemos las coordenadas de origen
        origin_coordinates = self.location_api_repository.get_coordinates(origin)
        try:
            origin_coordinates.raise_for_status()
            origin_location_result = origin_coordinates.json()[0]
            origin_latitude = origin_location_result.get("lat")
            origin_longitude = origin_location_result.get("lon")
        except Exception as e:
            print(f"Error en la solicitud: {e}")
            return jsonify({"error": "No se pudo obtener las coordenadas"}), 500
        
        #Obtenemos la temperatura de origen
        origin_weather = self.weather_api_repository.get_forecast(origin_latitude, origin_longitude, yesterday.date())

        #Obtenemos las coordenadas de destino
        destination_coordinates = self.location_api_repository.get_coordinates(destination)
        try:
            destination_coordinates.raise_for_status()
            destination_location_result = destination_coordinates.json()[0]
            destination_latitude = destination_location_result.get("lat")
            destination_longitude = destination_location_result.get("lon")
        except Exception as e:
            print(f"Error en la solicitud: {e}")
            return jsonify({"error": "No se pudo obtener las coordenadas"}), 500
        
        #Obtenemos la temperatura de destino
        destination_weather = self.weather_api_repository.get_forecast(destination_latitude, destination_longitude, yesterday.date())

        #Obtenemos los aeropuertos de origen y destino
        origin_airports = self.location_api_repository.search_airport_by_city(origin)
        destination_airports = self.location_api_repository.search_airport_by_city(destination)

        #Obtenemos los UnixTime de ayer
        start_of_day = datetime.datetime(now.year, now.month, now.day, 0, 0, 0) - datetime.timedelta(days=1)
        start_of_day_timestamp = int(start_of_day.timestamp())

        end_of_day = datetime.datetime(now.year, now.month, now.day, 23, 59, 59) - datetime.timedelta(days=1)
        end_of_day_timestamp = int(end_of_day.timestamp())

        #Obtenemos los vuelos
        completeFlights = []
        for i in origin_airports:
            flights = self.flight_api_repository.get_flights(i['ICAO Code'], start_of_day_timestamp, end_of_day_timestamp)
            for j in flights:
                for k in destination_airports:
                    if j['estArrivalAirport'] == k['ICAO Code']:
                        j['firstSeen'] = datetime.datetime.fromtimestamp(j['firstSeen'])
                        j['lastSeen'] = datetime.datetime.fromtimestamp(j['lastSeen'])
                        completeFlights.append(j)

        #formateamos la temperatura de origen
        origin_weather_json_str = origin_weather.to_json()
        origin_weather_json = json.loads(origin_weather_json_str)

        origin_weather_result = []
        for key in origin_weather_json['date']:
            origin_weather_result.append({
                "date": datetime.datetime.fromtimestamp(origin_weather_json['date'][key] / 1000, tz=datetime.timezone.utc),
                "temperature_2m": origin_weather_json['temperature_2m'][key]
            })

        #formateamos la temperatura de destino
        destination_weather_json_str = destination_weather.to_json()
        destination_weather_json = json.loads(destination_weather_json_str)

        destination_weather_result = []
        for key in destination_weather_json['date']:
            destination_weather_result.append({
                "date": datetime.datetime.fromtimestamp(destination_weather_json['date'][key] / 1000, tz=datetime.timezone.utc),
                "temperature_2m": destination_weather_json['temperature_2m'][key]
            })

        #formateamos los vuelos
        flights_info = []
        for flight in completeFlights:
            flights_info.append({
                "departure_time": flight['firstSeen'],
                "arrival_time": flight['lastSeen'],
                "origin": origin,  # Asumiendo que 'origin' es una variable válida en tu código
                "destination": destination  # Asumiendo que 'destination' es una variable válida en tu código
            })

        #Retornamos la información
        data = jsonify({
            "origin_weather": origin_weather_result,
            "destination_weather": destination_weather_result,
            "flights": flights_info
        })

        data = data.get_json()
        return render_template('index.html', data=data)