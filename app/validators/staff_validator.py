from kanpai.Kanpai import Object, String, Email, Array

create_staff_validator = Object({
	"first_name" : String().trim().required('First Name is required'),
	"last_name" : String().trim().required('Last Name is required'),
	"email" : Email().required('A valid email is required'),
	"phone_number" : String().required('Phone Number is required'),
	"role" : Array().required('A valid role is required'),
})