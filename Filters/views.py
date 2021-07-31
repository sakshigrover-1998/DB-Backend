from django.shortcuts import render
from Filters.models import FilterData
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Filters.models import FilterData
from Filters.serializers import FilterDataSerializer
from Filters.models import FilterData
# Create your views here.
# Create your views here.


from django.core.cache import cache

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser   


def insert_data_filterTable(filter_data_dict):
    # if(cache.get('filter_data_dict') == None):
    #     print("Cache is empty")
    #     finalDict = {

    #     }


    # format for this finalDict will be
        # {

        #     region1:
        #     {
        #         bLine1: [ data for bLine1 ]
        #         bLine2: [data for bLine1]

        #     }
        #     region2:
        #     {
        #         bLine1: [ data for bLine1 ]
        #         bLine2: [data for bLine1]

        #     }
        # }
    # else:
    #     print("Data in cache")
    #     finalDict = cache.get("filter_data_dict")
    #     print(finalDict)
    print(filter_data_dict)
    for result in filter_data_dict:
        
        FilterData.objects.create(
           filter_ID = int(result['filter_ID']),
           filter_name= result['filter_name'],
           filter_component=result['filter_component'],
           book_name = result['book_name'],
           filter_description  = result['filter_description'],
           cob_dt = result['cob_dt'],
           legal_entity= result['legal_entity'],
           profit_center= result['profit_center'],
           business_line = result['business_line'],
           region= result['region'] 
        ) 
    #     exception_BusinessLine = result['exception_BusinessLine']
    #     exception_Region = result['exception_Region']
    #     if(exception_BusinessLine not in finalDict):
    #         print(exception_BusinessLine,"not in cache")
    #         finalDict[exception_BusinessLine] = {}
    #         finalDict[exception_BusinessLine][exception_Region] = []
    #     elif(exception_Region not in finalDict[exception_BusinessLine]):
    #         print(exception_Region, "not in cache")

    #         finalDict[exception_BusinessLine][exception_Region] = []
    #     else:
    #         print(exception_BusinessLine, exception_Region, "in cache")
    #     print("Appending into finaldict,", finalDict)
    #     finalDict[exception_BusinessLine][exception_Region].append(result)
    #     print("Appended into finaldict,", finalDict)
    # cache.set("filter_data_dict",finalDict)

        


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'getFilteredRecords': '/getFilteredRecords/',
       
    }

    return Response(api_urls)


@api_view(['GET'])
def getFilteredRecords(request,userBL,userRegion,startDate = None,endDate = None):
    print(userBL, userRegion, startDate, endDate)

    try:
        if userBL == "ALL" :
            print("ALL")
            if startDate == "None" and endDate == "None":
                records = FilterData.objects.all()
            else:
                print("ALL BUT DATE")
                records = FilterData.objects.filter(cob_dt__gte = startDate,cob_dt__lte = endDate)
        elif userBL == "NA" :
            print("NA")
            if startDate == "None" and endDate == "None":
                records = FilterData.objects.all()
            else:
                print("ALL BUT DATE")
                records = FilterData.objects.filter(cob_dt__gte = startDate,cob_dt__lte = endDate)
        
        else:
            if startDate == "None" and endDate == "None":
                print("INSDIE NONE")
                records = FilterData.objects.filter(business_line = userBL,region = userRegion)

            else:    
                records = FilterData.objects.filter(business_line = userBL,region = userRegion,cob_dt__gte = startDate,cob_dt_lte = endDate)
        
        serializer = FilterDataSerializer(records, many=True)

        return Response(serializer.data)

    except Exception as e:
        print(e)
        return Response(e)



    # Input XML 
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
    #                     <location>Exceptions/MyZippedJsons/FilterJsons/Filterxyzjsono.tar.gz</location>
    #                 </transport>
    #                 <file_list>
    #                     <relativeURI>IFRS9_AMERICAS_LATIN_AM_ME578806part-00000.gz</relativeURI>
    #                     <compression>GZIP</compression>
    #                     <digest type="SHA1">c76192518f8292d9ff617de978cf4c1692220742</digest>
    #                 </file_list>
    #             </remote_data>
    #         </feed_meta_data>
    #     </cm:ta_control_message>
