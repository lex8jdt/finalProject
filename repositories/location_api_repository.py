import sqlite3
import requests
import config as cfg

class LocationApiRepository:
    def __init__(self):
        self.base_url = cfg.NOMINATIM_API_URL
        self.db_name = cfg.DATABASE_NAME

    # Get coordinates function
    def get_coordinates(self, city_name) -> requests.Response:
        """
        Obtiene las coordenadas de una ciudad usando Nominatim.
        """
        url = f"{self.base_url}?format=json&q={city_name}"
        headers = {
            "User-Agent": "MyPythonApp/1.0 (your_email@example.com)"  # Cambia tu email aquí
        }

        response = requests.get(url, headers=headers)
        return response
        
    # Database search function for airports
    def search_airport_by_city(self, city_name):
        conn = sqlite3.connect(self.db_name)
        conn.text_factory = lambda x: x.decode('utf-8')  # Ensure UTF-8 decoding
        cursor = conn.cursor()

        try:
            # Query the database for large airports in the city
            cursor.execute('''
                SELECT ident, iata_code, name, municipality, iso_country
                FROM airports
                WHERE municipality LIKE ? AND (type = 'large_airport' OR type = 'medium_airport')
            ''', ('%' + city_name + '%',))

            results = cursor.fetchall()

            if results:
                # Format the response for matching airports
                airports = [
                    {
                        "ICAO Code": icao_code,
                        "IATA Code": iata_code,
                        "Airport Name": name,
                        "City": city,
                        "Country": iso_country
                    }
                    for icao_code, iata_code, name, city, iso_country in results
                ]
                return airports
            else:
                return []  # No airports found

        except Exception as e:
            return []
        finally:
            conn.close()