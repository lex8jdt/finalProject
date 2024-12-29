from repositories import FlightApiRepository

class FlightService:
    def __init__(self, flight_api_repository: FlightApiRepository):
        self.flight_api_repository = flight_api_repository

    def get_flights(self, airport_ICAO, from_date, to_date): 
        return self.flight_api_repository.get_flights(airport_ICAO, from_date, to_date)
