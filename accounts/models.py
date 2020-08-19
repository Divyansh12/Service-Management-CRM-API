from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType

# Common Model to add common fields to all the models and handle the archive functionality while deleting
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    def delete(self,*args, **kwargs):
        # if not self.id:
        self.archived = True
        super().save(*args, **kwargs)
    class Meta:
        abstract = True


# Common Model for User 
class UserCommonModel(AbstractUser):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    def delete(self,*args, **kwargs):
        # if not self.id:
        self.archived = True
        super().save(*args, **kwargs)
    class Meta:
        abstract = True

class UserModel(UserCommonModel):
    is_management_team = models.BooleanField(default=False,blank=True, null=True)
    is_sale_team = models.BooleanField(default=False,blank=True, null=True)
    is_support_team = models.BooleanField(default=False,blank=True, null=True)
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def save(self,*args, **kwargs):
        if not self.id:
            if self.is_management_team==True:
                self.is_staff=True
                group, created= Group.objects.get_or_create(name="management")
                if(created):
                    group.permissions.add(*Permission.objects.exclude(content_type__app_label="auth"))
                super().save(self,*args, **kwargs)
                self.groups.add(group)
            else:
                super().save(self,*args, **kwargs)
        else:
            print(self.groups.all())
            if self.is_management_team==True:
                self.is_staff=True
                group, created= Group.objects.get_or_create(name="management")
                if(created):
                    group.permissions.add(*Permission.objects.exclude(content_type__app_label="auth"))
                print(group.permissions.all())
                super().save(*args, **kwargs)
                self.groups.add(group)
                super().save(*args, **kwargs)
                print(self)
                print(self.groups.all())
            else:
                super().save(*args, **kwargs)

        return self.username

class ClientModel(CommonModel):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254,blank=True, null=True)
    mobile= models.CharField(max_length=10,blank=True, null=True)
    company_name = models.CharField(max_length=100,blank=True, null=True)
    sales_contact = models.ForeignKey(UserModel, on_delete=models.CASCADE,blank=True, null=True, related_name='CLIENTS')

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return '%s %s - %s' % (self.first_name, self.last_name, self.company_name)