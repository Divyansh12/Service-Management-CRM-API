from django.db import models
from accounts.models import CommonModel, UserModel, ClientModel
from contracts.models import ContractModel
# Create your models here.

class Service(CommonModel):
    service_name= models.CharField(max_length=50)
    service_type= models.CharField(max_length=50)
    description= models.CharField(max_length=50000)
    sales_contact = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True , related_name='Client_Service')
    support_contact = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True, related_name='Support_Services')
    contract= models.ForeignKey(ContractModel, on_delete=models.CASCADE, blank=True, null=True, related_name= 'Contract_Services')
    is_done= models.BooleanField(default=False, blank=True, null=True)
    amount= models.FloatField(default=0.0, blank=True, null=True)
    event_date= models.DateTimeField(blank=True, null=True)
    attendees= models.IntegerField()
    additional_requirements= models.CharField(max_length=10000)
