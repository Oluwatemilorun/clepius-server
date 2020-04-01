from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

staff_schema = {
	"type": "object",
	"properties": {
		"title": {
			"type": "string",
			"enum": ["mr", "mrs", "miss", "master", "mistress", "sir", "dr"]
		},
		"firstname": {
			"type": "string"
		},
		"middlename": {
			"type": "string"
		},
		"lastname": {
			"type": "string"
		},
		"position": {
			"type": "string",
			"enum": ["administrator", "physician", "clinician", "accountant", "receptionist"]
		},
		"speciality": {
			"type": "string"
		}
	}
}