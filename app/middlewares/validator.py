from functools import wraps
from flask import request, url_for, abort
from app.utils import response, decorators
from app import jsonify

@decorators.parameterized
def validate(fn, validator):

	def validate_decorator(*xs, **kws):
		try:
			validation_result = validator.validate(request.get_json(force=True))
			if validation_result.get('success', False) is False:
				return response.error(
					data=validation_result.get('error'),
					message='invalid request body',
					status=422
				)
			else:
				return fn(*xs, **kws)

		except Exception as e:
			if e.__class__.__name__ == 'ValidationError':
				return response.error(
					data=e.errors,
					message='Invalid Request Body',
					status=422
				)
			else:
				return response.error(
					data=e,
					message='An error occured',
					status=500
				)
				

	return validate_decorator
