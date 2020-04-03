from Kanpai import Object, String

create_staff_validator = Object({
	"firstname": String().trim().required('Firstname is required')
})