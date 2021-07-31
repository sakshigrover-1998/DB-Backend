from Users.models import UserData
from django.contrib import admin

# Register your models here.
from .models import UserData
admin.site.register(UserData)