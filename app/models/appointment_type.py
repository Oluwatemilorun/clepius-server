from mongoengine.fields import StringField

from app import db

class AppointmentType(db.Document):
	name = StringField(required=True, max_length=50)
	description = StringField(max_length=200)