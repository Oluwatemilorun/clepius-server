import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

MONGODB_SETTINGS = {
    'db': 'clepius',
    'host': os.environ.get('host'),
    'port': '27017',
    # 'username': os.environ.get('DB_USER'),
    # 'password': os.environ.get('DB_PASS')
}
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=2)
