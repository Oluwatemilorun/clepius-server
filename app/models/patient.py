from mongoengine.fields import StringField, ListField, ReferenceField

from app import db
from .role import Role
from .contact_record import EmailRecord, PhoneRecord

class Patient(db.Document):
	# Bio
	title = StringField(max_length=10)
	first_name = StringField(required=True, max_length=50)
	middle_name = StringField(max_length=50)
	last_name = StringField(required=True, max_length=50)

	# Contact Information
	email = ListField(ReferenceField(EmailRecord), required=True)
	phone = ListField(ReferenceField(EmailRecord), required=True)
	home_address = StringField(max_length=150)
	office_address = StringField(max_length=150)

	# Access
	role = ListField(ReferenceField(Role) required=True)
