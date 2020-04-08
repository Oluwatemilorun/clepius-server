from mongoengine.fields import StringField, DateTimeField

from app import db

class Speciality(db.Document):
	name = StringField(required=True, max_length=50)
	description = StringField(max_length=150)

	#date_created = DateTimeField(default=)

	# meta
	meta = {
        'indexes': [ 'name' ],
		'ordering': ['-name']
	}