from django.db import models

# Create your models here.

class ExceptionType(models.Model):

    exception_ID=models.IntegerField()
    exception_name=models.CharField(max_length=50,null=True,default='')
    exception_component=models.CharField(max_length=20,null=True,default='')
    exception_level=models.CharField(max_length=20,null=True,default='')
    exception_description=models.CharField(max_length=50,null=True,default='')
    exception_COBDT=models.DateField(default='2000-01-01')
    exception_LegalEntity=models.CharField(max_length=50,null=True,default='')
    exception_ProfitCenter=models.CharField(max_length=50,null=True,default='')
    exception_BusinessLine=models.CharField(max_length=50,null=True,default='')
    exception_Region=models.CharField(max_length=50,null=True,default='')    
    def __str__(self):
        return str(self.exception_ID)