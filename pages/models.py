from django.db import models
from django.contrib.auth.models import User
import string

class Project(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	create_dt = models.DateTimeField('date created')

	def __unicode__ (self):
		return self.title

class Group(models.Model):
	project = models.ForeignKey(Project)
	title = models.CharField(max_length=200)
	create_dt = models.DateTimeField('date created')

	def __unicode__ (self):
		return self.title

class Api(models.Model):
	group = models.ForeignKey(Group)
	name = models.CharField(max_length=100)
	method = models.CharField(max_length=10)
	url = models.CharField(max_length=200)
	param = models.CharField(max_length=256)
	desc = models.TextField('description')
	request= models.TextField('request')
	response = models.TextField('response')
	create_dt = models.DateTimeField('date created')
	
	def __unicode__ (self):
		return self.name
	
	def html_desc(self):
		return self.desc.replace('\r\n', '<br />')

	def html_response(self):
		return self.response.replace('\r\n', '<br />')

