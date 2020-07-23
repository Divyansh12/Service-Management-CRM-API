from django.contrib.auth.models import Group
from rest_framework import permissions


# def _is_in_group(user, group_name):
#     """
#     Takes a user and a group name, and returns `True` if the user is in that group.
#     """
#     try:
#         return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
#     except Group.DoesNotExist:
#         return None

# def _has_group_permission(user, required_groups):
#     return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsSupport(permissions.BasePermission):
    # group_name for super admin
    def has_permission(self, request, view):
        print(request.user)
        return bool((request.user and request.user.is_authenticated and (not(request.user.archived))) and (request.user.is_management == True or request.user.is_support == True or request.user.is_superuser) )

class IsSale(permissions.BasePermission):
    # group_name for super admin
    
    def has_permission(self, request, view):
        print(request.user)
        return bool((request.user and request.user.is_authenticated and (not(request.user.archived))) and (request.user.is_management == True or request.user.is_sale == True or request.user.is_superuser) )

class IsManagement(permissions.BasePermission):
    # group_name for super admin
    def has_permission(self, request, view):
        print(request.user)
        return bool((request.user and request.user.is_authenticated and (not(request.user.archived))) and (request.user.is_management == True or request.user.is_superuser == True) )

    
class AllowNone(permissions.BasePermission):
    message = {'details': 'No one allowed to use this method'}
    def has_permission(self, request, view):
        return False
