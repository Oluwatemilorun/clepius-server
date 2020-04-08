from flask_restful import Resource
from flask import request, abort, jsonify
from app.models.patient import Patient
from app.utils import response, generate_patient_id
from app.middlewares.validator import validate
from app.validators import create_patient_validator
from app.models.contact_record import EmailRecord, PhoneRecord
import json


class Patients(Resource):
    def get(self):
        data = Patient.objects(is_active=True).to_json()
        return response.success(
            data=data,
			message='All patients fetched'
        )

    @validate(create_patient_validator)
    def post(self):
        data = request.get_json(force=True)
        if EmailRecord.objects(email=data['email']):
            return response.error(message="Email already used!")
        if PhoneRecord.objects(phone=data['phone_number']):
            return response.error(message="Phone Number used!")
        email = EmailRecord(data['email'], label='Personal').save()
        phone_number = PhoneRecord(data['phone_number'], label="Mobile").save()
        data['email'] = email.id
        data['phone_number'] = phone_number.id
        try:
            patient = Patient(**data)
            patient.patient_id = generate_patient_id()
            patient.save()
        except:
            return response.error(message="Invalid crediential(s) given!", status=422)
        else:
            email.user_type = patient.id
            phone_number.user_type = patient.id
            email.save()
            phone_number.save()

        return response.success(
                   data={data},
                  message='New user created!',
                   status=201
            )
        