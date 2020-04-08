from kanpai import Kanpai

staff_id_login_validator = Kanpai.Object({
    "staff_id" : Kanpai.String().trim().required("Patient Id is required"),
    "password" : Kanpai.String().required("Password is required"), 
}) 