from rest_framework import serializers
from .models import *

class RegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone_number']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
