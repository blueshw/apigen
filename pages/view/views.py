from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils.html import *

from pages.models import Project, Group, Api
import string
 
class IndexView(generic.ListView):
	template_name = 'pages/index.html'
	context_object_name = 'latest_project_list'

	def get_queryset(self):
		return Project.objects.order_by('-create_dt')[:5]


class ApiListView(generic.View):

	def get(self, request, group_id):
		apilist = Api.objects.filter(group_id = group_id)
		group = Group.objects.filter(id = group_id)
		context = {'apilist': apilist, 
					'group': group[0]}
		return render(request, 'pages/api_list.html', context)

class ApiDocumentView(generic.View):

	def get(self, request, api_id):
		print "API ID: %s" % (api_id)
		apiDoc = Api.objects.filter(id = api_id)
		print apiDoc[0].name
	#	response = apiDoc[0].response.replace('\r\n', '<br />')
	#	response = format_html(u"%s" % (response) )
		print apiDoc[0].html_response
		context = {'apidoc': apiDoc[0],
					}
		return render(request, 'pages/api_document.html', context)


