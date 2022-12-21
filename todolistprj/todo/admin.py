from django.contrib import admin
from . models import Task
# Register your models here.

class Taskadmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'complete', 'created', 'updated')
    list_filter = ('user', 'title', 'description', 'complete', 'created', 'updated')

admin.site.register(Task,Taskadmin)

