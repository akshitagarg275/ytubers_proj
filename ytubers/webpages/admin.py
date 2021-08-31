from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def myPhoto(self,object):
        return format_html('<img  src = "{}" width="40">'.format(object.photo.url))
    def nameUp(self,object):
        return format_html('<b>{}</b>'.format(object.first_name.upper()))
    list_display=('id','myPhoto','nameUp','role','created_date')
    list_display_links=('role',)
    search_fields=('role',)
    list_filter=('role','created_date')

admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)