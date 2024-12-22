from flask import Blueprint, request
from services import weather_service

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route('/forecast', methods=['GET'])
def get_forecast():
    return weather_service.get_forecast(request.args.get('city'))