import requests_cache
import openmeteo_requests
from retry_requests import retry
import pandas as pd
import config as cfg

class WeatherApiRepository:
    def __init__(self):
        self.base_url = cfg.WEATHER_API_URL
        

    def get_forecast(self, lat, lon, yesterday):
        """
        Obtiene el pronóstico del clima para una ubicación específica.
        """
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)

        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m",
            "start_date": yesterday,
            "end_date": yesterday
        }
        
        response = openmeteo.weather_api(self.base_url, params=params)
        hourly = response[0].Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
	        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	        freq = pd.Timedelta(seconds = hourly.Interval()),
	        inclusive = "left"
        )}
        hourly_data["temperature_2m"] = hourly_temperature_2m

        hourly_dataframe = pd.DataFrame(data = hourly_data)
        return hourly_dataframe