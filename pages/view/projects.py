from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils.html import *

from pages.models import Project, Group, Api
import string
 
class GroupListView(generic.ListView):
#	template_name = 'pages/group_list.html'
#	context_object_name = 'group_list'
#
#	def get_queryset(self):
#		group_list = Group.objects.filter(project_id = project_id)
#		return group_list 

	def get(self, request, project_id):
		group_list = Group.objects.filter(project_id = project_id)
		project  = Project.objects.filter(id = project_id)
		context = {'group_list': group_list,
					'project': project[0]}
		return render(request, 'pages/group_list.html', context)



