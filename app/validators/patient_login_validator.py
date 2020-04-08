from kanpai import Kanpai

patient_login_validator = Kanpai.Object({
    "patient_id" : Kanpai.String().trim(),
    "email" : Kanpai.Email(),
    "password" : Kanpai.String().required('Password is required'),
})