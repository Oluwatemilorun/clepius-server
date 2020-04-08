from mongoengine.fields import StringField, ReferenceField, DateTimeField
from .patient import Patient
from .appointment import Appointment
from .appointment_type import AppointmentType

from app import db

class Report(db.Document):
    title = StringField(max_length=50, required=True)
    description = StringField(max_length=250)
    patient = ReferenceField(Patient)
    date = DateTimeField()
    appointment = ReferenceField(Appointment)
    appointment_type = ReferenceField(AppointmentType)