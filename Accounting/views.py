from typing import final
from django.shortcuts import render
from django.http import HttpResponse
from Accounting.models import AccountingData
from Exceptions.models import ExceptionType
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from Accounting.serializers import AccountingDataSerializer
from FastData import views as FastDataViews

# Create your views here.

def Accounting_Query(): 
    final_buffer=[]
    entry_list = list(AccountingData.objects.filter(exception_component="Accounting"))
    for j in entry_list:
       if not (ExceptionType.objects.filter(exception_ID=j.exception_ID).exists()):
           final_buffer.append(j)
    
    print("this is final buffer",final_buffer)
    for i in final_buffer:
        new_entry = ExceptionType(exception_ID=i.exception_ID,
           exception_name=i.exception_name,exception_component=i.exception_component,
           exception_level=i.exception_level,exception_description=i.exception_description,
           exception_COBDT=i.exception_COBDT,exception_LegalEntity=i.exception_LegalEntity,
           exception_ProfitCenter=i.exception_ProfitCenter,exception_BusinessLine=i.exception_BusinessLine,
           exception_Region=i.exception_Region)
        new_entry.save()
    print("Sending cache a trigger from accounting")
    FastDataViews.onDataInsert(True)
    
    #     exception_BusinessLine = i.exception_BusinessLine
    #     exception_Region = i.exception_Region
        
      
    #     print("Appended into finaldict,", finalDict)

   
   
    # cache.set('data_dict', finalDict)

    # # cache.get('data_dict').append(result)

    # print("The cache is updated")
    # print("Cache data:")
    # print("Cache check")
    # print(cache.get('data_dict'))
    #print(entry_list)

  
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'getAccountingRecords': '/getAccountingRecords/',
       
    }

    return Response(api_urls)


@api_view(['GET'])
def getAccountingRecords(request):
    records = AccountingData.objects.all()
    serializer = AccountingDataSerializer(records, many=True)
    return Response(serializer.data)   
"""
