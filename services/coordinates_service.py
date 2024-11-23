from repositories import CoordinatesApiRepository

class CoordinatesService:
    def __init__(self, coordinates_api_repository: CoordinatesApiRepository):
        self.coordinates_api_repository = coordinates_api_repository

    def get_coordinates(self, address):
        return self.coordinates_api_repository.get_coordinates(address)