from django.contrib import admin
from django.apps import apps
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField , AdminPasswordChangeForm
# Register your models here.
app = apps.get_app_config('accounts')
from .models import UserModel
from django.utils.translation import gettext, gettext_lazy as _
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = UserModel
#         fields = UserCreationForm.Meta.fields + ('is_management','is_sale','is_support',)

# class CustomUserChangeForm(UserChangeForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField(label=("Password"),
#         help_text=("Raw passwords are not stored, so there is no way to see "
#                     "this user's password, but you can change the password "
#                     "using <a href=\"../password/\">this form</a>."))

#     class Meta:
#         model = UserModel
#         fields = '__all__'
#         field_classes = {'username': UsernameField}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         password = self.fields.get('password')
#         if password:
#             password.help_text = password.help_text.format('../password/')
#         user_permissions = self.fields.get('user_permissions')
#         if user_permissions:
#             user_permissions.queryset = user_permissions.queryset.select_related('content_type')

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial.get('password')

# class CustomPasswordChangeForm(AdminPasswordChangeForm):


#     def save(self, commit=True):
#         """Save the new password."""
#         password = self.cleaned_data["password1"]
#         self.user.set_password(password)
#         self.user.save()
#         print(self.user)
#         if commit:
#             self.user.save()
#         return self.user

class CustomUserAdmin(UserAdmin):
    # change_password_form = CustomPasswordChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (_('Roles'), {
            'fields': ('is_management','is_sale','is_support','archived',),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Roles'), {
            'fields': ('is_management','is_sale','is_support',),
        }),
    )

for model_name, model in app.models.items():
    if(model_name=="usermodel"):
        admin.site.register(UserModel, CustomUserAdmin)
    else:
        
        model_admin = type(model_name + "Admin", (admin.ModelAdmin, ), {'list_display': tuple([field.name for field in model._meta.fields])})
        admin.site.register(model, model_admin)
