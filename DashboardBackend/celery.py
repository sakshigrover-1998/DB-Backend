from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
import DashboardBackend
# import click
# import click.exceptions
# import traceback
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'DashboardBackend.settings')

# UNABLE_TO_LOAD_APP_MODULE_NOT_FOUND = click.style("""
# Unable to load celery application.
# The module {traceback.print_exc()} was not found.""", traceback.print_exc())

# UNABLE_TO_LOAD_APP_ERROR_OCCURRED = click.style("""
# Unable to load celery application.
# While trying to load the module {0} the following error occurred:
# {1}""", traceback.print_exc())

app=Celery('DashboardBackend')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.conf.beat_schedule ={
    'AccountFetch':{
        'task':'Accounting.tasks.Accounting_Data_Fetch',
        'schedule':5
    }
}
app.autodiscover_tasks()