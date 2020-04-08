from flask_restful import Resource
from app.utils import error, success
from app.models.staff import Staff
from app.middlewares.validator import validate
from app.validators import staff_email_login_validator

class Staff_email_login(Resource):

    @validate(staff_email_login_validator)
    def post(self):
        data = request.get_json()
        staff  = Staff.objects(email=data['email'])
        if (staff.check_password(data['password'])) or (staff.password_hash == data['password']):
            return success("You've been logged in")
        return error(message="Invalid login credientials!", status=442)
