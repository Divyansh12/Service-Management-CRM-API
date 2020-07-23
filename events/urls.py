from django.urls import path,include
from events.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'event',EventViewSet,'Events')
router.register(r'manage/event',EventManagementViewSet,'ManageEvents')


urlpatterns = [
]

urlpatterns += router.urls
