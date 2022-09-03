from django.contrib.auth.models import AbstractUser
from django.db import models
from distutils.command.upload import upload

class User(AbstractUser):
    username=models.CharField(unique=True, max_length=50)
    email= models.EmailField(max_length=500)
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    
    
    class Meta:
        verbose_name ='User'
        verbose_name_plural='Users'
      

    def __str__(self):
        return self.username
    
