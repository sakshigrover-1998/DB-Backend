from __future__ import absolute_import,unicode_literals
from Exceptions import views
from celery import shared_task

@shared_task
def insert_db_task(filePath,filename):
    return views.readFile(filePath,filename)

