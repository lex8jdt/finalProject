import requests
import config as cfg

class FlightApiRepository:
    def __init__(self):
        self.base_url = cfg.OPENSKY_API_URL

    def get_flights(self, airport_ICAO, from_date, to_date) -> requests.Response:
        """
        Obtiene los vuelos usando OpenSky.
        """
        url = f"{self.base_url}?airport={airport_ICAO}&begin={from_date}&end={to_date}"

        response = requests.get(url)
        #response = url
        return response.json()