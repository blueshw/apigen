from django.conf.urls import patterns, include, url

from pages import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apigen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^project/(?P<project_id>\d+)/$', views.GroupListView.as_view()),
	url(r'^apilist/(?P<group_id>\d+)/$', views.ApiListView.as_view()),
	url(r'^apidoc/(?P<api_id>\d+)/$', views.ApiDocumentView.as_view()),
    url(r'^', views.IndexView.as_view() , name = 'index'),
)
