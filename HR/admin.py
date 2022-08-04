from django.contrib import admin
from .models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'department', 'branch']
    search_fields = ['name']
    list_per_page = 6


admin.site.register(Employee, EmployeeAdmin)
