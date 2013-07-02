"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from apigen.api.models import Api


class SimpleTest(TestCase):
    def test_basic_addition(self):
		api = Api(title="TEST")
		api.created = datetime.datetime.now()
		api.method = "/store/api/test"
		api.save()
		
