from mongoengine.fields import StringField, ListField, ListField, ReferenceField, DateField, DateTimeField, BooleanField

from app import db
from .staff_position import StaffPosition
from .contact_record import EmailRecord, PhoneRecord
from .role import Role
from .speciality import Speciality
from .appointment import Appointment

class Staff(db.Document):
	# Bio
	title = StringField(choices={'mr', 'mrs', 'miss', 'master', 'dr', 'sir', 'madam'})
	first_name = StringField(required=True, max_length=50)
	middle_name = StringField(max_length=50)
	last_name = StringField(required=True, max_length=50)
	dob = DateField()

	# Work
	position = ReferenceField(StaffPosition)
	specialities = ListField(ReferenceField(Speciality))

	# Contact Information
	email = ListField(ReferenceField(EmailRecord), required=True)
	phone = ListField(ReferenceField(EmailRecord), required=True)
	address = StringField(max_length=150)

	# Operations
	appointments = ListField(ReferenceField(Appointment))
	reports

	# Security
	role = ListField(ReferenceField(Role) required=True)
	pw_hash = StringField(required=True)
	is_active = BooleanField(required=True, default=True)
	is_deleted = BooleanField(required=True, default=False)
	
	# Misc


	# meta
	meta = {
        'indexes': [ 'last_name' ]
		'ordering': ['-date_added']
	}