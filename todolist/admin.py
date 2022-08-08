from django.contrib import admin
from todolist.models import *

class TodoAdmin(admin.ModelAdmin):
    search_fields = ['todo', 'is_complete']

# Register your models here.
admin.site.register(Todo, TodoAdmin)