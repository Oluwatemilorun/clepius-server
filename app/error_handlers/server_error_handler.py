from app.utils import response
from flask import jsonify

def server_error_handler(error):
    return response.error(message="Internal server error")
