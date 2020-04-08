from flask_restful import Api

from app.resources.patient_resources import Patient_login

Patient_login_router = Api()

Patient_login_router.add_resource(Patient_login, '/login')