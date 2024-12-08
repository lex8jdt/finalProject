import requests
import config as cfg

class WeatherApiRepository:
    def __init__(self):
        self.api_key = cfg.WEATHER_API_KEY
        self.base_url = cfg.WEATHER_API_URL
        

    def get_forecast(self, lat, lon, days=7, lang="es"):
        """
        Obtiene el pronóstico del clima para una ubicación específica.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "days": days,
            "key": self.api_key,
            "lang": lang
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None