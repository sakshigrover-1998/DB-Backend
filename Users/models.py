from django.db import models
from django.db.models.fields import DateField
# Create your models here.

class UserData(models.Model):
    user_ID=models.IntegerField()
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    user_business_line=models.CharField(max_length=20,null=True, default="NA")
    user_region=models.CharField(max_length=20, null = True, default="NA")
    
    
    
