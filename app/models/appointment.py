from mongoengine.fields import StringField, DateTimeField, IntField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, BooleanField

from app import db
from .appointment_type import AppointmentType
from .facility import Facility

class AppointmentSchedule(EmbeddedDocument):
	visit_date = DateTimeField(required=True)
	visit_duration = IntField(min_value=15, max_value=90) # in minutes
	
	# repeats
	will_repeat = BooleanField(default=False)
	repeat_span = IntField(min_value=1)
	repeat_interval = StringField(choices={'minute', 'hour', 'day', 'month', 'year'})

class Appointment(db.Document):
	staff = ReferenceField('Staff', required=True)
	patient = ReferenceField('Patient', required=True)

	appointment_type = ReferenceField(AppointmentType, required=True)
	appointment_reason = StringField(required=True, max_length=150)
	status = StringField(required=True, default='pending', choices={'pending', 'done', 'cancelled'})
	location = ReferenceField(Facility)
	
	schedule = EmbeddedDocumentField(AppointmentSchedule, required=True)

	is_deleted = BooleanField(default=False)