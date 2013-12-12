from mongoengine import * 
from apigen.settings import DBNAME
# Create your models here.

connect(DBNAME)

class Api(Document):
	title = StringField(max_length=20, required=False)
	method = StringField(max_length=200, required=True)
	content = StringField(max_length=2000, required=False)
	created = DateTimeField(required=True)
	resource_url = ListField()
	params = DictField(required=False)


