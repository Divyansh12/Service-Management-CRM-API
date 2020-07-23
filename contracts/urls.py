from django.urls import path,include
from contracts.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'contract',ContractViewSet,'Contracts')
router.register(r'manage/contract',ContractManagementViewSet,'ManageContract')


urlpatterns = [
]

urlpatterns += router.urls
