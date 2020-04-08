from mongoengine.fields import StringField, ListField, ReferenceField, DateField, BooleanField

from app import db
from .staff_position import StaffPosition
from .contact_record import EmailRecord, PhoneRecord
from .role import Role
from .speciality import Speciality
from .appointment import Appointment
from .report import Report
from app.utils import generate_initial_password
from app import bcrypt


class Staff(db.Document):
	# Bio
	staff_id = StringField(max_length=15, unique=True)
	title = StringField(max_length=10, choices={'mr', 'mrs', 'miss', 'master', 'dr', 'sir', 'madam'})
	first_name = StringField(required=True, max_length=50)
	middle_name = StringField(max_length=50)
	last_name = StringField(required=True, max_length=50)
	dob = DateField()

	# Work
	position = ReferenceField(StaffPosition)
	specialities = ListField(ReferenceField(Speciality))

	# Contact Information
	email = ListField(ReferenceField(EmailRecord), required=True)
	phone_number = ListField(ReferenceField(PhoneRecord), required=True)
	address = StringField(max_length=150)
	password_hash = StringField(required=True, max_length=100, default=generate_initial_password)
	date_joined = DateField()

	# Operations
	appointments = ListField(ReferenceField(Appointment))
	reports = ListField(ReferenceField(Report))

	# Security
	role = ListField(ReferenceField(Role), required=True)
	is_active = BooleanField(required=True, default=True)
	is_deleted = BooleanField(required=True, default=False)
	
	# Misc


	# meta
	meta = {
        'indexes': [ 'last_name' ],
		'ordering': ['-date_added']
	}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.date_joined = datetime.utcnow()

	def toggle_is_active(self):
		if self.is_active:
			self.is_active = False
		else:
			self.is_active = True
	
	def delete_account(self):
		self.is_active = False
		self.is_deleted = True

	def set_password(self, password):
		self.password_hash = bcrypt.generate_password_hash(password)

	def check_password(self, password):
		return bcrypt.check_password_hash(self.password_hash, password)
