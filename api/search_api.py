from flask import Blueprint, request
from services import search_service

search_bp = Blueprint('search', __name__)

@search_bp.route('/', methods=['GET'])

def get_search():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    response = search_service.get_search(origin, destination)
    return response 