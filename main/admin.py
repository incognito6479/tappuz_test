from django.contrib import admin
from main.models import CustomUser, Department


@admin.register(Department)
class DepartmentAdminModel(admin.ModelAdmin):
    list_display = ['created_at', 'department_name', 'department_status', 'employee_number']
    search_fields = ['department_name']


@admin.register(CustomUser)
class CustomUserAdminModel(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'middle_name', 'phone_number']
    search_fields = ['username']
