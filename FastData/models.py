from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class FlagInsertTable(models.Model):

    Flag = models.BooleanField()
    isException = models.BooleanField()