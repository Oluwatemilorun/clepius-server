
from flask_restful import Resource

from app.utils import response

class AllUsers(Resource):
	
	def get(self):
		return response.success(
			data=[],
			message='All users fetched'
		)

