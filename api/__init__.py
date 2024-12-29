# api/__init__.py
from flask import Blueprint

# Importa los blueprints
from .home_api import home_bp
from .search_api import search_bp

# Crea el blueprint
api_bp = Blueprint('api', __name__)

# Registra los blueprints
api_bp.register_blueprint(home_bp)
api_bp.register_blueprint(search_bp, url_prefix='/search')