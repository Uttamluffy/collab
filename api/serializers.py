from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Student, Teacher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'email', 'password', 'roll_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        student = Student.objects.create_user(**validated_data)
        return student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username', 'email', 'password', 'employee_id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        teacher = Teacher.objects.create_user(**validated_data)
        return teacher



#class StudentSerializer(serializers.ModelSerializers):
#    class Meta:
#        model = User
#        fields = ['id', 'username', 'email', 'password']
#        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        