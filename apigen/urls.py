from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apigen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^member/', include('accounts.urls')),
    url(r'^page/', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
