#-*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from pages.models import Project , Group, Api
from import_export.admin import ImportExportModelAdmin

admin.site.register(Project)
admin.site.register(Group)

class ApiAdmin(ImportExportModelAdmin):
    list_display = ('__unicode__', 'group', 'name', 'method', 'url', 'param', 'desc', 'request', 'response')


#admin.site.register(Api, ApiAdmin)
admin.site.register(Api)
