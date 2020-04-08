from kanpai import Kanpai

patient_id_login_validator = Kanpai.Object({
    "patient_id" : Kanpai.String().trim().required("Patient Id is required"),
    "password" : Kanpai.String().required("Password is required"), 
}) 