from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):
    def myPhoto(self,object):
        return format_html('<img  src = "{}" width="40">'.format(object.photo.url))
    list_display=('name','myPhoto','city','category','camera_type')
    list_display_links=('myPhoto',)
    list_filter=('camera_type','category')
    search_fields=('city','name')

admin.site.register(Youtuber,YoutuberAdmin)