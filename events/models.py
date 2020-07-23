from django.db import models
from accounts.models import CommonModel, UserModel, Client
from contracts.models import Contract
# Create your models here.

class Events(CommonModel):
    sales_contact = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True , related_name='Client_Events')
    support_contact = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True, related_name='Support_Events')
    contract= models.ForeignKey(Contract, on_delete=models.CASCADE, blank=True, null=True, related_name= 'Contract_Events')
    status= models.BooleanField(default=False, blank=True, null=True)
    amount= models.FloatField(default=0.0, blank=True, null=True)
    event_date= models.DateTimeField(blank=True, null=True)
    attendees= models.IntegerField()
    notes= models.CharField(max_length=10000)
