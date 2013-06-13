from django.db import models

# Create your models here.

class Api(models.Model):
	Name = models.CharField(max_length=20, null=False)
	Content = models.TextField(max_length=2000, null=False)
	Created = models.DateTimeField(auto_now_add=True, auto_now=True)

	class Admin:
		pass

class Param(models.Model):
	Api = models.ForeignKey(Api)
	Name = models.CharField(max_length=20, null=False)
	Value = models.CharField(max_length=200, null=False)
	Content = models.TextField(max_length=2000, null=False)
	Created = models.DateTimeField(auto_now_add=True, auto_now=True)

	class Admin:
		pass
