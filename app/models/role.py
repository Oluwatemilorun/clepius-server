from mongoengine.fields import StringField, ListField, EmbeddedDocumentField

from app import db
from .permission import Permission

class Role(db.Document):
	name = StringField(unique=True, required=True)
	description = StringField(max_length=150)
	permissions = ListField(EmbeddedDocumentField(Permission))