from flask import Blueprint
from flask_restful import Api

from .patient_router import Patient_router
from .staff_router import Staff_router
from .patient_email_login_router import Patient_email_login_router
from .patient_id_login_router import Patient_id_login_router
from .patient_login_router import Patient_login_router
from .staff_email_login_router import Staff_email_login_router
from .staff_id_login_router import Staff_id_login_router
from .staff_login_router import Staff_login_router

from .login import Login_router

# create blueprint for API v1
v1_blueprint = Blueprint('v1', __name__) 

Patient_router.init_app(v1_blueprint)
Staff_router.init_app(v1_blueprint)
Patient_email_login_router.init_app(v1_blueprint)
Patient_id_login_router.init_app(v1_blueprint)
# Patient_login_router.init_app(v1_blueprint)
Staff_email_login_router.init_app(v1_blueprint)
Staff_id_login_router.init_app(v1_blueprint)
Staff_login_router.init_app(v1_blueprint)

Login_router.init_app(v1_blueprint)

