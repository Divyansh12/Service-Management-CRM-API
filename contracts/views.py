from rest_framework import generics,permissions,views,status,viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from accounts.models import *

from accounts.permissions import *

#Register API

from rest_framework import viewsets,permissions,filters,views
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as djfilters
  

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

class ContractManagementViewSet(CommonViewSet):
    permission_classes = [ IsManagement ]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = ContractSerializer
    http_method_names = ['get', 'head', 'put', 'patch', 'delete']
    queryset = Contract.objects.filter(archived=False)

    def perform_update(self,serializer):
        try:
            if(self.request.data['client']):
                client = Client.objects.get(id=self.request.data['client'],archived=False)
                serializer.save(client=client)
        except:
            print("Exception Occurred")
        finally:
            serializer.save()

class ContractViewSet(viewsets.ModelViewSet):
    
    permission_classes=[
        IsSale
    ]
    serializer_class = ContractSerializer
    def get_queryset(self):
        return Contract.objects.filter(archived=False)
    def perform_create(self,serializer):
        print(self.request.data)
        client= Client.objects.get(id=self.request.data['client'],archived=False)
        serializer.save(client=client,sales_contact=self.request.user)
    def perform_update(self,serializer):
        print(self.request.data)
        try:
            if(self.request.data['client']):
                client = Client.objects.get(id=self.request.data['client'],archived=False)
                serializer.save(client=client)
        except:
            print("Error")
        finally:
            serializer.save()
