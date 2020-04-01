from mongoengine.fields import StringField, GenericReferenceField

from app import db
# from 

class ContactRecord(db.Document):
	user = GenericReferenceField()
	label = StringField(required=True, max_length=15)

	meta = {'allow_inheritance': True}

class PhoneRecord(ContactRecord):
	phone = StringField(unique=True, required=True)

	# meta
	meta = {
        'indexes': [ 'phone' ]
	}

class EmailRecord(ContactRecord):
	email = StringField(unique=True, required=True)

	# meta
	meta = {
        'indexes': [ 'email' ]
	}