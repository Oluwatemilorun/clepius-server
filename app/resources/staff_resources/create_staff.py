from flask import request, jsonify
from flask_restful import Resource

from app.middlewares.validator import validate
from app.utils import response, generate_staff_id
from app.validators import create_staff_validator
from app.models.staff import Staff
from app.models.contact_record import EmailRecord, PhoneRecord
from app.models.role import Role

class Staffs(Resource):

	def get(self):
		data = Staff.objects(is_active=True).to_json()
		return response.success(
			data=data,
			message='All staffs fetched'
		)

	@validate(create_staff_validator)
	def post(self):
		data = request.get_json(force=True)
		if EmailRecord.objects(email=data['email']):
			return response.error(message="Email already used!")
		if not Role.objects(name=data['role']):
			return response.error(message="Invalid Role(s)", status=422)
		role = Role.objects(name=data['role'])
		email = EmailRecord(data['email']).save()
		phone_number = PhoneRecord(data['phone_number']).save()
		data['email'] = email.id
		data['phone_number'] = phone_number.id
		data['role'] = role.id

		try:
			staff = Staff(**data)
			staff.staff_id = generate_staff_id()
			staff.save()
		except:
			return response.error(message="Invalid crediential(s) given!", status=422)
		else:
			return response.success(
                   data=data,
                  message='New user created!',
                   status=201)