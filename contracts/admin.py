from django.contrib import admin
from django.apps import apps

# Register your models here.
app = apps.get_app_config('contracts')

for model_name, model in app.models.items():
    model_admin = type(model_name + "Admin", (admin.ModelAdmin, ), {'list_display': tuple([field.name for field in model._meta.fields])})
    admin.site.register(model, model_admin)
