from flask import request
from flask_restful import Resource

from app.middlewares import validator
from app.utils import response
from app.validators import create_staff_validator

class Staff(Resource):

	def get(self):
		return response.success(
			data=[],
			message='All staffs fetched'
		)

	@validator(create_staff_validator)
	def post(self):
		print(request.get_json(force=True))
