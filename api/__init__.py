# api/__init__.py
from flask import Blueprint

# Importa los blueprints
from .home_api import home_bp
from .weather_api import weather_bp
from .location_api import location_bp

# Crea el blueprint
api_bp = Blueprint('api', __name__)

# Registra los blueprints
api_bp.register_blueprint(home_bp)
api_bp.register_blueprint(weather_bp, url_prefix='/weather')
api_bp.register_blueprint(location_bp, url_prefix='/location')