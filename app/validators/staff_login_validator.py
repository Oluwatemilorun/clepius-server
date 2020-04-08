from kanpai import Kanpai

staff_login_validator = Kanpai.Object({
    "staff_id" : Kanpai.String().trim(),
    "email" : Kanpai.Email(),
    "password" : Kanpai.String().required('Password is required'),
})