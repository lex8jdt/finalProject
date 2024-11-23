import requests

class CoordinatesService:
    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"

    def get_coordinates(self, city_name):
        """
        Obtiene las coordenadas de una ciudad usando Nominatim.
        """
        url = f"{self.base_url}?format=json&q={city_name}"
        headers = {
            "User-Agent": "MyPythonApp/1.0 (your_email@example.com)"  # Cambia tu email aquí
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lanza un error si la respuesta HTTP no es 200
            return response.json()
        except requests.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None
