from kanpai import Kanpai

create_patient_validator = Kanpai.Object({
	"first_name" : Kanpai.String().trim().required("First Name is required"),
    "last_name" : Kanpai.String().trim().required("Last Name is required"),
    "email" : Kanpai.Email().required('A valid email is required'),
    "phone_number" : Kanpai.String().required('Phone Number is required')
})