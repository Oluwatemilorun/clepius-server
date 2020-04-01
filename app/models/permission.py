from mongoengine.fields import StringField

from app import db

class Permission(db.Document):
	name = StringField(unique=True, required=True)
	description = StringField(max_length=150)
	