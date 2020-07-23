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
from rest_framework import status
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

class EventManagementViewSet(CommonViewSet):
    permission_classes = [ IsManagement ]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = EventSerializer
    http_method_names = ['get', 'head', 'put', 'patch', 'delete']
    queryset = Events.objects.filter(archived=False)

    def perform_update(self,serializer):
        print(self.request.data)
        try: 
            support= UserModel.objects.get(id=self.request.data['support_contact'],is_support=True,archived=False)

            try:
                contract= Contract.objects.get(id=self.request.data['contract'],archived=False)
            
                serializer.save(support_contact=support, contract=contract)
            except:
                print("Contract not provided") 
            # if(support == None):
            #     return Response({"details":"User is not Support Staff"})
                serializer.save(support_contact=support)
        except:
            print("Support Contact Not provided")
            try:
                contract= Contract.objects.get(id=self.request.data['contract'],archived=False)
            
                serializer.save(contract=contract)
            except:
                print("Contract not provided")
            
        finally:
            serializer.save()

class EventViewSet(CommonViewSet):
    
    permission_classes=[
        IsSale
    ]
    serializer_class = EventSerializer
    def get_queryset(self):
        return Events.objects.filter(archived=False)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res, res_status=self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if(res_status==status.HTTP_400_BAD_REQUEST):
            return Response(res, status=res_status, headers=headers)
        else:
            return Response(serializer.data, status=res_status, headers=headers)       
        
    def perform_create(self,serializer):
        print(self.request.data)
        
        try:
            self.request.data['contract']
        except:
            return {"details":"'contract' field is required"}, status.HTTP_400_BAD_REQUEST
        
        try:
            contract = Contract.objects.get(id=self.request.data['contract'],archived=False)
        except:
            return {"details":"Contract is archived"}, status.HTTP_400_BAD_REQUEST


        try: 
            support= UserModel.objects.get(id=self.request.data['support_contact'],is_support=True,archived=False)
            serializer.save(sales_contact=self.request.user,contract=contract,support_contact=support)
        except:
            return {"details":"support_contact field is required"}, status.HTTP_400_BAD_REQUEST           
        finally:
            return serializer.save(sales_contact=self.request.user,contract=contract), status.HTTP_201_CREATED

    def perform_update(self,serializer):
        print(self.request.data)
        try: 
            support= UserModel.objects.get(id=self.request.data['support_contact'],is_support=True,archived=False)

            try:
                contract= Contract.objects.get(id=self.request.data['contract'],archived=False)
            
                serializer.save(support_contact=support, contract=contract)
            except:
                print("Contract not provided") 
            # if(support == None):
            #     return Response({"details":"User is not Support Staff"})
                serializer.save(support_contact=support)
        except:
            print("Support Contact Not provided")
            try:
                contract= Contract.objects.get(id=self.request.data['contract'],archived=False)
            
                serializer.save(contract=contract)
            except:
                print("Contract not provided")
            
        finally:
            serializer.save()



class SupportEventViewSet(CommonViewSet):
    
    permission_classes=[
        IsSupport
    ]
    serializer_class = EventSerializer
    http_method_names = ['get', 'head', 'put', 'patch', 'delete']

    def get_queryset(self):
        return  self.request.user.Support_Events.filter(archived=False)   
    def perform_update(self,serializer):
        print(self.request.data)
        try: 
            support= UserModel.objects.get(id=self.request.data['support_contact'],is_support=True,archived=False)

            try:
                contract= Contract.objects.get(id=self.request.data['contract'],archived=False)
            
                serializer.save(support_contact=support, contract=contract)
            except:
                print("Contract not provided") 
            # if(support == None):
            #     return Response({"details":"User is not Support Staff"})
                serializer.save(support_contact=support)
        except:
            print("Support Contact Not provided")
            try:
                contract= Contract.objects.get(id=self.request.data['contract'],archived=False)
            
                serializer.save(contract=contract)
            except:
                print("Contract not provided")
            
        finally:
            serializer.save()
