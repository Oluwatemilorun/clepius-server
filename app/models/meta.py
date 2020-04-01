from mongoengine.fields import StringField, FloatField

from app import db


class Meta(db.Document):
	# About
	hospital_name = StringField(unique=True, required=True, max_length=100)
	hospital_qoute = StringField(max_length=150)
	hospital_logo = StringField()
	hospital_cover = StringField()

	# Address
	hospital_address = StringField(max_length=200)
	hospital_city = StringField(max_length=100)
	hospital_country = StringField(default="nigeria", max_length=150)
	hospital_postcode = StringField(max_length=6)
	hospital_coord_lng = FloatField()
	hospital_coord_lat = FloatField()
	hospital_coord_elv = FloatField()

	# Contact details
	hospital_email = StringField(unique=True, required=True)
	hospital_phone_1 = StringField(unique=True, required=True)
	hospital_phone_2 = StringField(unique=True)

	# Super Admin
	hospital_admin_user = StringField(unique=True, required=True, max_length=30)
	hospital_admin_pass = StringField(required=True)


