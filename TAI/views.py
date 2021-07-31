from typing import final
from Exceptions.models import ExceptionType
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
import tarfile
import os
from Exceptions import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
import FastData.views as FastDataViews

# from TAI.tasks import insert_db_task

from TAI import models
from django.core.cache import cache

def insert_data_exceptionTable(data_dict):
    for result in data_dict:
        ExceptionType.objects.create(
        exception_ID = int(result['exception_ID']),
        exception_name= result['exception_name'],
        exception_component=result['exception_component'],
        exception_level = result['exception_level'],
        exception_description  = result['exception_description'],
        exception_COBDT = result['exception_COBDT'],
        exception_LegalEntity= result['exception_LegalEntity'],
        exception_ProfitCenter= result['exception_ProfitCenter'],
        exception_BusinessLine = result['exception_BusinessLine'],
        exception_Region= result['exception_Region'] 
        )
        
        
    # if(cache.get('data_dict')==None):
    
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # 'List': '/subject-list/',
        # 'Detail View': '/subject-detail/<str:pk>/',
        # 'Create': '/subject-create/',
        # 'Update': '/subject-update/<str:pk>/',
        # 'Delete': '/subject-delete/<str:pk>/',
    }

    return Response(api_urls)



    # # Input XML 
    # <cm:ta_control_message xmlns:val="TAValuation" xmlns:acc="TAAccounting" xmlns:tra="TATrade" xmlns:ps="TAProcessStatus" xmlns:ece="TAExpectedCreditEvent" xmlns:adj="TAAdjustment" xmlns:sett="TASettlement" xmlns:cm="TAControlMessage" xmlns:bal="TABalance" xmlns:et="TAExtendedAttributes" xmlns:mov="TAMovement" xmlns:conv="TAConversion" xmlns:ns15="TACallAccountInterest" xmlns:mh="TAMessageHeader" xmlns:ns14="TACompoundInterest">
    #         <header>
    #             <mh:business_object_id>148</mh:business_object_id>
    #             <mh:business_object_type>CONTROL</mh:business_object_type>
    #             <mh:business_object_owner>FDW</mh:business_object_owner>
    #             <mh:business_object_version>578806</mh:business_object_version>
    #             <mh:business_event_type>NEW</mh:business_event_type>
    #             <mh:business_event_timestamp>2020-12-31T00:00:00</mh:business_event_timestamp>
    #             <mh:delivery_unit_id>148</mh:delivery_unit_id>
    #             <mh:delivery_unit_instance_id>578806</mh:delivery_unit_instance_id>
    #             <mh:delivery_unit_instance_entity_id>148</mh:delivery_unit_instance_entity_id>
    #         </header>
    #         <feed_meta_data>
    #             <status>PROCESSED</status>
    #             <module>ACCOUNTING</module>
    #             <num_accountables>9391</num_accountables>
    #             <value_date>2020-12-31</value_date>
    #             <remote_data>
    #                 <transport>
    #                     <type>HDFS</type>
    #                     <host>hdfs://sdl-uat</host>
    #                     <port>8020</port>
    #                     <location>Exceptions/MyZippedJsons/ExceptionJsons/Exception2.tar.gz</location>
    #                 </transport>
    #                 <file_list>
    #                     <relativeURI>IFRS9_AMERICAS_LATIN_AM_ME578806part-00000.gz</relativeURI>
    #                     <compression>GZIP</compression>
    #                     <digest type="SHA1">c76192518f8292d9ff617de978cf4c1692220742</digest>
    #                 </file_list>
    #             </remote_data>
    #         </feed_meta_data>
    #     </cm:ta_control_message>
