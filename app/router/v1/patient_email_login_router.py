from flask_restful import Api

from app.resources.patient_resources import Patient_email_login

Patient_email_login_router = Api()

Patient_email_login_router.add_resource(Patient_email_login, '/login')