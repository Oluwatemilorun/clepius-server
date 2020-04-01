from flask import Blueprint
from flask_restful import Api

from .user_router import user_router

# create blueprint for API v1
v1_blueprint = Blueprint('v1', __name__)

user_router.init_app(v1_blueprint)

