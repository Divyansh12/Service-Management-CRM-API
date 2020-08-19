from django.db import models
from accounts.models import CommonModel, UserModel, ClientModel
# Create your models here.

class ContractModel(CommonModel):
    sales_contact = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True , related_name='Client_Contracts')
    client= models.ForeignKey(ClientModel, on_delete=models.CASCADE, blank=True, null=True, related_name='Contracts')
    is_done= models.BooleanField(default=False, blank=True, null=True)
    amount= models.FloatField(default=0.0, blank=True, null=True)
    payment_date= models.DateTimeField(blank=True, null=True)
