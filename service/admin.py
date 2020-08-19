
# Register your models here.


from django.contrib import admin
from django.apps import apps


# from django.apps import apps
# from .models import CustomUser,EventType,Event,Total,Participated,Team,Teammate,TeamParticipated

app = apps.get_app_config('service')

for model_name, model in app.models.items():
    model_admin = type(model_name + "Admin", (admin.ModelAdmin, ), {'list_display': tuple([field.name for field in model._meta.fields])})
    admin.site.register(model, model_admin)

# from .models import *

# admin.site.register(CustomUser)
# admin.site.register(EventType)
# admin.site.register(Event)
# admin.site.register(Total)
# admin.site.register(Participated)
# admin.site.register(Team)
# admin.site.register(Teammate)
# admin.site.register(TeamParticipated)


# class PersonAdmin(admin.ModelAdmin):
#     search_fields = ['user','mobNo','email']

# for model_name, model in app.models.items():
#     model_admin = type(model_name + "Admin", (PersonAdmin, ), {'list_display': tuple([field.name for field in model._meta.fields])})
#     admin.site.register(model, model_admin)
#     list_filter = '__all__'