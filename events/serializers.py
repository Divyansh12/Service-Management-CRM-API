from rest_framework import serializers,exceptions
from accounts.serializers import *
from contracts.serializers import *
from events.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

#User Serializer

class EventSerializer(serializers.ModelSerializer):
    sales_contact = UserSerializer(read_only=True)
    support_contact = UserSerializer(read_only=True)
    contract= ContractSerializer(allow_null=True)
    class Meta:
        model=Events
        fields='__all__'
