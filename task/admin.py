from django.contrib import admin
from . models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'details', 'start_date', 'end_date', 'status','created_at')