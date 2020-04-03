from flask_restful import Api

from app.resources.staff_resources import Staff

staff_router = Api()

staff_router.add_resource(Staff, '/staff')
