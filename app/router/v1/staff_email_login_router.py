from flask_restful import Api

from app.resources.staff_resources import Staff_email_login

Staff_email_login_router = Api()

Staff_email_login_router.add_resource(Staff_email_login, '/login')