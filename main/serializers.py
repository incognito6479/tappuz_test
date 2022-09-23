from rest_framework import serializers
from main.models import CustomUser, Department


class CustomUserCreationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'phone_number', 'department', 'username', 'password']
        extra_kwargs = {'department': {'required': True}}


class DepartmentModelSerializer(serializers.ModelSerializer):
    employee_obj = CustomUserCreationModelSerializer(many=True, read_only=True, source='department')

    class Meta:
        model = Department
        fields = ["id", "created_at", "department_name", "department_status", "employee_number", "employee_obj"]

