from rest_framework import serializers,exceptions
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username','email','first_name','last_name','is_support','is_management','is_sale')
#Register Serializer

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username','email','password','first_name','last_name','is_support','is_management','is_sale')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user = UserModel.objects.create_user(username=validated_data['username'],email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],password=validated_data['password'],is_support=validated_data['is_support'],is_management=validated_data['is_management'],is_sale=validated_data['is_sale'])
        return user

#Login Users
class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user :
            if user.is_active:
                if not(user.archived):
                    return user
                raise exceptions.AuthenticationFailed('User is Archived')
            raise exceptions.AuthenticationFailed('Account is not activated')
        raise serializers.ValidationError("Credentials Not Found")



class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

# class ChangePassowrdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ('id','email','password')


class ClientSerializer(serializers.ModelSerializer):
    sales_contact = UserSerializer(read_only=True)
    class Meta:
        model=Client
        fields='__all__'
