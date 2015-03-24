#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	create_dt = models.DateTimeField('date created')

class Group(models.Model):
	project = models.ForeignKey(Project)
	title = models.CharField(max_length=200)
	create_dt = models.DateTimeField('date created')

class Api(models.Model):
	group = models.ForeignKey(Group)
	name = models.CharField("이름", max_length=100)
	method = models.CharField("메서드", max_length=10)
	url = models.CharField("유알엘",max_length=200)
	param = models.CharField(max_length=256)
	desc = models.TextField("상세설명",'description')
	request= models.TextField('request')
	response = models.TextField('response')
	create_dt = models.DateTimeField('date created')
	
	def html_desc(self):
		return self.desc.replace('\r\n', '<br />')

	def html_response(self):
		return self.response.replace('\r\n', '<br />')

