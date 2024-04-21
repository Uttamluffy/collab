from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

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


#class StudentSerializer(serializers.ModelSerializers):
#    class Meta:
#        model = User
#        fields = ['id', 'username', 'email', 'password']
#        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        