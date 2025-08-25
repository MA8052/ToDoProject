from django.contrib import admin
from .models import ToDoTable

# Register your models here.
class ToDoTableAdmin(admin.ModelAdmin):
    list_display=(id.__name__,'Task_column')

admin.site.register(ToDoTable,ToDoTableAdmin)