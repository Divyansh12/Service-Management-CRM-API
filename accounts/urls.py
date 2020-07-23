from django.urls import path,include
from accounts.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'client',ClientViewSet,'Client')
router.register(r'manage/client',ClientManagementViewSet,'ManageClient')
router.register(r'manage/user',UserManagementViewSet,'ManageUser')


urlpatterns = [
    path('auth/register',RegisterAPI.as_view()),
    path('auth/login',LoginAPI.as_view()),
    path('auth/user',UserAPI.as_view()),
    path('auth/user/changepassword',UpdatePassword.as_view())
]

urlpatterns += router.urls
