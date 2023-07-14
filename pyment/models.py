from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BillingAdress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{first_name} x {last_name}'
    
    # def is_fully_filled(self):
    #     fields_names = [f.name for f in self._meta.get_fields()]
    #     for fields_name in fields_names:
    #         value = getattr(self,fields_name)
    #         if value is None or value =='':
    #             return False
        # return True
    
    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self,field_name)
            if value is None or value == '':
                return False
            else:
                return True
