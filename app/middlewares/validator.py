from functools import wraps
from flask import request, url_for, abort
from app.utils import response, decorators

@decorators.parameterized(fn)
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
			return response.error(
				data=e,
				message='An error occured',
				status=500
			)

	return validate_decorator
