from flask_restful import Api

from app.resources.login_resources import Patient_login

Login_router = Api()

Login_router.add_resource(Patient_login , '/login/email/patient')