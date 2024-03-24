from django.db import models


# from authentication.models import User

from django.contrib.auth.models import AbstractUser


# Create your models here.




class Friends(models.Model):
    source_user = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='source_friend')
    target_user = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='target_friend')
    created_at = models.DateTimeField(auto_now_add=True)
    status =  models.CharField(max_length=20)

    class Meta:
        ordering = ['-id']



class Requests(models.Model):
    source_user = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='source_user')
    target_user = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='target_user')
    created_at = models.DateTimeField(auto_now_add=True)
    status =  models.CharField(max_length=20)

    class Meta:
        ordering = ['-id']


