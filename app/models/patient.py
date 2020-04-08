from mongoengine.fields import StringField, ListField, ReferenceField, DateField, BooleanField
from app import db
from .role import Role
from .contact_record import EmailRecord, PhoneRecord
from datetime import datetime
from app.utils import generate_initial_password
from app import bcrypt



class Patient(db.Document):
	
	patient_id = StringField(max_length=15, unique=True)

	# Bio
	title = StringField(max_length=10)
	first_name = StringField(required=True, max_length=50)
	middle_name = StringField(max_length=50)
	last_name = StringField(required=True, max_length=50)
	gender = StringField(max_length=10, choices={'male', 'female', 'other'})
	password_hash = StringField(required=True, max_length=100, default=generate_initial_password)

	# Contact Information
	email = ListField(ReferenceField(EmailRecord), required=True)
	phone_number = ListField(ReferenceField(PhoneRecord), required=True)
	home_address = StringField(max_length=150)
	office_address = StringField(max_length=150)

	#other
	marital_status = StringField(choices={'single', 'married', 'divorced', 'other'})
	state = StringField(max_length=50)
	country = StringField(max_length=50)
	date_joined = DateField()
	is_active = BooleanField(required=True, default=True)
	is_deleted = BooleanField(required=True, default=False)
	

	# Access
	#role = ListField(ReferenceField(Role), required=True)


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.date_joined = datetime.utcnow()

	def toggle_is_active(self):
		if self.is_active:
			self.is_active = False
		else:
			self.is_active=True

	def delete_account(self):
		self.is_active = False
		self.is_deleted = True

	def set_password(self, password):
		self.password_hash = bcrypt.generate_password_hash(password)

	def check_password(self, password):
		return bcrypt.check_password_hash(self.password_hash, password)

