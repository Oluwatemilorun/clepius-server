from flask_restful import Api

from app.resources.staff_resources import Staff_login

Staff_login_router = Api()

Staff_login_router.add_resource(Staff_login, '/login')