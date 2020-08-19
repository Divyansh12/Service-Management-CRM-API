from django.urls import path,include
from service.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'service',ServiceViewSet,'Services')
router.register(r'manage/service',ServiceManagementViewSet,'ManageServices')
router.register(r'support/service',SupportServiceViewSet,'SupportService')


urlpatterns = [
]

urlpatterns += router.urls
