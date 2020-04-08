from flask_restful import Resource
from app.models.patient import Patient
from app.utils import error, success
from app.middlewares.validator import validate
from app.validators import patient_email_login_validator

class Patient_email_login(Resource):

    @validate(patient_email_login_validator)
    def post(self):
        data = request.get_json()
        patient = Patient.objects(email=data['email'])
        if (patient.check_password(data['password'])) or (patient.password_hash == data['password']):
            return success("You've been logged in")
        return error(message="Invalid login credientials!", status=442)
