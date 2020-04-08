from app.utils import response
from flask import jsonify

def not_found_handler(error):
    return response.error(message="request item not found!", status=404)