from flask import Flask, Blueprint, request, jsonify, current_app, g
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

from app.utils import JSONEncoder

# create flask app
app = Flask(__name__)

# use Werkzeug’s built-in password hashing utilities
bcrypt = Bcrypt(app)

# connect mongo
db = MongoEngine(app)

# apply extend endcoder
app.json_encoder = JSONEncoder

# create flask blueprint
api_bp = Blueprint('api', __name__)

# allow CORS for all domains on all routes
CORS(api_bp, supports_credentials=True, origins=['http://localhost:3000'])

# use flask_restful resource routing
api = Api(api_bp)

# register routes
from app.router.v1 import v1_blueprint

app.register_blueprint(v1_blueprint, url_prefix='/api/v1')
