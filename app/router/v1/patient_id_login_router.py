from flask_restful import Api

from app.resources.patient_resources import Patient_id_login

Patient_id_login_router = Api()

Patient_id_login_router.add_resource(Patient_id_login, '/login')