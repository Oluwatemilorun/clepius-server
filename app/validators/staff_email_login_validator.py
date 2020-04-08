from kanpai import Kanpai

staff_email_login_validator = Kanpai.Object({
    "email" : Kanpai.String().required("Email is required"),
    "password" : Kanpai.String().required("Password is required"), 
}) 