from flask_restful import Api

from app.resources.user_resources import AllUsers

user_router = Api()

user_router.add_resource(AllUsers, '/user')

# api.add_resource(AllUsers, '/users')
# api.add_resource(SingleUser, '/users/<user_reg>')
# api.add_resource(ResetUserPassword, '/users/<user_reg>/reset-password')
# api.add_resource(AddUserAssignment, '/users/<user_reg>/add-ass