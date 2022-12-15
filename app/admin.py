from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_filter    = ['topic_name']
    list_per_page  = 2 
    ordering       = ['topic_name']
    list_display   = ('topic_name','date')
    search_fields  = ['topic_name']







