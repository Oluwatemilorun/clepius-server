from flask_restful import Api

from app.resources.patient_resources import Patients

Patient_router = Api()

Patient_router.add_resource(Patients, '/patient')

# api.add_resource(AllUsers, '/users')
# api.add_resource(SingleUser, '/users/<user_reg>')
# api.add_resource(ResetUserPassword, '/users/<user_reg>/reset-password')
# api.add_resource(AddUserAssignment, '/users/<user_reg>/add-ass