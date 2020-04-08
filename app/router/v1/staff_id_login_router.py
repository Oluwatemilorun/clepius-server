from flask_restful import Api

from app.resources.staff_resources import Staff_id_login

Staff_id_login_router = Api()

Staff_id_login_router.add_resource(Staff_id_login, '/login')