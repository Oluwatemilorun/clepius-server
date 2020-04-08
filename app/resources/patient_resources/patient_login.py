from flask_restful import Resource
from app.models.patient import Patient
from app.utils import error, success
from app.middlewares.validator import validate
from app.validators import patient_login_validator
from app.models.contact_record import PhoneRecord, EmailRecord

class Patient_login(Resource):

    @validate(patient_login_validator)
    def post(self):
        data = request.get_json()
        user = EmailRecord.filter(email=data['email']).first()
        print(user)
        patient = Patient.objects(patient_id=data['patient_id']) or Patient.objects(email=data['email'])
        if (patient.check_password(data['password'])) or (patient.password_hash == data['password']):
            return success("You've been logged in")
        return error(message="Invalid login credientials!", status=442)
    

    # @validate(patient_login_validator)
    # def post(self):
    #     data = request.get_json()
    #     pr = PhoneRecord.objects(phone=data['phone_number']).user_type
