from django.db import models
from django.db.models.fields import DateField
# Create your models here.

class FilterData(models.Model):
    filter_ID=models.IntegerField()
    filter_name=models.CharField(max_length=50,null=True,default='')
    filter_component=models.CharField(max_length=50,null=True,default='')
    filter_description=models.CharField(max_length=20,null=True,default='')
    region=models.CharField(max_length=20,null=True,default='')
    business_line=models.CharField(max_length=20,null=True,default='')
    legal_entity=models.CharField(max_length=20,null=True,default='')
    profit_center=models.CharField(max_length=20,null=True,default='')
    book_name=models.CharField(max_length=20,null=True,default='')
    cob_dt=models.DateField(null=True,default='2000-01-01')


    
    
    
