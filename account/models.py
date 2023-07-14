from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
    CHOICES = (
        ('male','Male'),
        ('female','Female'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_pro')
    full_name = models.CharField(max_length=50,blank=True,null=True)
    profession = models.CharField(max_length=50,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=10,choices=CHOICES,default='male')

    def __str__(self):
        return str(self.user.id)
    

    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    
    @receiver(post_save,sender=User)
    def profile_save(sender,instance, **kwargs):
        instance.user_pro.save()
    



