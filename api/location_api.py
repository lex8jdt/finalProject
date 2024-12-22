from flask import Blueprint, jsonify, request
from services import location_service
import requests


location_bp = Blueprint('location', __name__)

# Unified endpoint
@location_bp.route('/airports', methods=['GET'])
def get_location_airports():
    query = request.args.get('city')
    response = location_service.get_location_airports(query)

    # Return the response, ensuring special characters display correctly
    return response
