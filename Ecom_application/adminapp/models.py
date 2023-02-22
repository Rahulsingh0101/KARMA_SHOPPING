from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Adminuser(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100,blank=True,null=True)
    is_active=models.BooleanField(default=True)

