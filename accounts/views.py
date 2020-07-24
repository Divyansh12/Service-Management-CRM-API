from rest_framework import generics,permissions,views,status,viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser,FormParser

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework.decorators import api_view, permission_classes
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_jwt.settings import api_settings

from accounts.permissions import *
from django.contrib.auth.models import update_last_login
from django_filters import rest_framework as djfilters

#Register API

from rest_framework import viewsets,permissions,filters,views
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import render

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

from rest_framework.permissions import IsAuthenticated

class CommonViewSet(viewsets.ModelViewSet):
	permission_classes  = (permissions.AllowAny,)
	filter_backends = (filters.OrderingFilter,djfilters.DjangoFilterBackend,)
	filterset_fields = '__all__'
	ordering_fields = '__all__'
	extra_permissions = None
	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		extra = []
		if self.extra_permissions is not None:
			extra = [permission() for permission in self.extra_permissions]
		return [permission() for permission in self.permission_classes]+extra

class RegisterAPI(generics.GenericAPIView):
    serializer_class= UserRegisterSerializer
    permission_classes= [IsManagement]
    authentication_classes = [JSONWebTokenAuthentication]
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [IsManagement]
    #     elif self.action == 'list':
    #         permission_classes = [IsManagement]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'destroy':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     return [permission() for permission in permission_classes]

    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # print(request.user)
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password cannot be created'
            )
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": jwt_token
        })





class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(UserSerializer(user,context=self.get_serializer_context()).data)
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": jwt_token
        })
       

#Get User Api

class UserAPI(generics.RetrieveAPIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UpdatePassword(generics.GenericAPIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"details": ["Wrong password."]}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"details":["Password Changed"]},status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserManagementViewSet(CommonViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = UserSerializer
    http_method_names = ['get', 'head', 'put', 'patch', 'delete']
    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [ AllowNone ]
        elif self.action == 'list':
            permission_classes = [IsManagement]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsManagement]
        elif self.action == 'destroy':
            permission_classes = [IsManagement]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.method=="GET":
            if((self.request.user and self.request.user.is_authenticated and (not(self.request.user.archived))) and (self.request.user.is_management == True or self.request.user.is_superuser == True)):
                
                return UserModel.objects.filter(archived=False)
            else:

                return UserModel.objects.filter(archived=False, username=self.request.user)
        elif self.request.method=="PUT" or self.request.method=="PATCH" :
            if((self.request.user and self.request.user.is_authenticated and (not(self.request.user.archived))) and (self.request.user.is_management == True or self.request.user.is_superuser == True)):
                
                return UserModel.objects.filter(archived=False)
            else:

                return UserModel.objects.filter(archived=False, username=self.request.user)
        else:
            return UserModel.objects.filter(archived=False)
    


class ClientManagementViewSet(CommonViewSet):
    permission_classes = [ IsManagement ]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = ClientSerializer
    http_method_names = ['get', 'head', 'put', 'patch', 'delete']
    queryset = Client.objects.filter(archived=False)

class ClientViewSet(CommonViewSet):
    
    permission_classes=[
        IsSale
    ]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = ClientSerializer
    def get_queryset(self):

        # return self.request.user.CLIENTS.filter(archived=False)
        return Client.objects.filter(archived=False)
    def perform_create(self,serializer):
        serializer.save(sales_contact=self.request.user)


