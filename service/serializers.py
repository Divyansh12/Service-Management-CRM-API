from rest_framework import serializers,exceptions
from accounts.serializers import *
from contracts.serializers import *
from service.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

#Service Serializer

class ServiceSerializer(serializers.ModelSerializer):
    sales_contact = UserSerializer(read_only=True)
    support_contact = UserSerializer(read_only=True)
    contract= ContractSerializer(read_only=True,allow_null=True)
    class Meta:
        model=Service
        fields='__all__'
