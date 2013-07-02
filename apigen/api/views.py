# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from apigen.api.models import Api 
from django.template import Context, loader
import datetime


def index(request):
	print ("index run")

	ctx = Context({
			"hello":"This is gen!!"
			})
	ctx.update(csrf(request))

	#return HttpResponse(tpl.render(ctx))
	return render_to_response("input_api.html", ctx)

def inputApi(request):
	print "input API"
	print request.POST['apiExample']

	resource_url = []
	resource_url.append("alpha : http://alpha-story.kakao.com/papi/propagations/register")
	resource_url.append("beta : http://beta-story.kakao.com:7070/papi/propagations/register")

	params = {}
	params["sKey"] = "This is sKey"
	params["uid"] = "This is user id"

	title = request.POST['apiExample']
	api = Api(title = title)
	api.created = datetime.datetime.now()
	api.method = "/store/api/test"
	api.resource_url = resource_url
	api.params = params
	api.save()

	ctx = Context({
			"hello": request.POST["apiExample"]
			})
	ctx.update(csrf(request))

	return render_to_response("helloTemplate.html", ctx)


