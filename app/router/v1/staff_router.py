from flask_restful import Api

from app.resources.staff_resources import Staffs

Staff_router = Api()

Staff_router.add_resource(Staffs, '/staff')
