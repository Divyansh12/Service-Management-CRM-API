from rest_framework import serializers,exceptions
from accounts.serializers import *
from contracts.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

#User Serializer

class ContractSerializer(serializers.ModelSerializer):
    sales_contact = UserSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    class Meta:
        model=ContractModel
        fields='__all__'
