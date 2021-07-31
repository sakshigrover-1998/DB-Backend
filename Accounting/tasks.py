from __future__ import absolute_import,unicode_literals
from Accounting.models import AccountingData
from celery import shared_task
from Accounting.views import Accounting_Query

@shared_task
def Accounting_Data_Fetch():
    return(Accounting_Query())
    