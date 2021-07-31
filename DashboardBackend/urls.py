"""DashboardBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import TAI
from TAI import views as tai_views
from Exceptions import views as exceptions_views
from Users import views as users_views
from Filters import views as filters_views
from FastData import views as fastDataViews

#from Accounting import views as accounting_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('readFile/path=<str:path>', exceptions_views.readFile),
    path('fileIsReady/', exceptions_views.fileIsReady),
    
    path('', exceptions_views.apiOverview),
    path('getProcessedRecords/bl=<str:userBL>/region=<str:userRegion>/startDate=<str:startDate>/endDate=<str:endDate>', exceptions_views.getProcessedRecords),
    path('getUserRecords/', users_views.getUserRecords),
    path('getFilteredRecords/bl=<str:userBL>/region=<str:userRegion>/startDate=<str:startDate>/endDate=<str:endDate>', filters_views.getFilteredRecords),
    #path('getAccountingRecords/', accounting_views.getAccountingRecords),

   #path('getCurrentData/businessLine=<str:businessLine>/region=<str:region>/', fastDataViews.getCacheContent),
    path("getCurrentData/", exceptions_views.getCurrentData),
    path("getCacheData/bl=<str:userBL>/region=<str:userRegion>",fastDataViews.getCacheContent),
    path("getFilterCacheData/bl=<str:userBL>/region=<str:userRegion>",fastDataViews.getFilterCacheContent)
    
]
