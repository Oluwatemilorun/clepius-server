from datetime import datetime
from mongoengine.fields import StringField, DateTimeField

from app import db

class StaffPosition(db.Document):
	name = StringField(required=True, max_length=30)
	description = StringField(max_length=150)