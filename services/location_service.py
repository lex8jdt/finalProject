from flask import jsonify
from repositories import LocationApiRepository

class LocationService:
    def __init__(self, location_api_repository: LocationApiRepository):
        self.location_api_repository = location_api_repository

    def get_coordinates(self, address):
        data = self.location_api_repository.get_coordinates(address)
        try:
            data.raise_for_status()
            output = data.json()
        except Exception as e:
            print(f"Error en la solicitud: {e}")
            return jsonify({"error": "No se pudo obtener las coordenadas"}), 500
        
        return output
    
    def get_location_airports(self, city):
        data = self.location_api_repository.search_airport_by_city(city)
        
        if data == []:
            return jsonify({"error": "No se encontraron aeropuertos"}), 404
        
        response = self.location_api_repository.get_coordinates(city)
        
        try:
            response.raise_for_status()
            location_result = response.json()[0]
            latitude = location_result.get("lat")
            longitude = location_result.get("lon")
            # display_name = location_result.get("display_name")
        except Exception as e:
            print(f"Error en la solicitud: {e}")
            return jsonify({"error": "No se pudo obtener las coordenadas"}), 500
        
        data = jsonify({
            "city": city,
            "location": {
                "latitude": latitude,
                "longitude": longitude,
                # "display_name": display_name,
                # "bounding_box": location_result.get("boundingbox")
            },
            "airports": data
        })
        
        if data:
            return data, 200
        else:
            return jsonify({"error": "No se encontraron aeropuertos"}), 404
            
            