from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

config_schema = {
	"type": "object",
	"properties": {
		"hospital_name": {
			"type": "string"
		},
		"hospital_logo": {
			"type": "string"
		},
		"hospital_address": {
			"type": "string"
		}
	}
}